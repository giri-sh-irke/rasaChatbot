from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib

#Function to create the list of restaurant objects
def format_restaurant_list(restaurant_list):
	formatted_restaurant_list = []
	for restaurant in restaurant_list:
		rest = {}
		rest['name'] = restaurant['restaurant']['name']
		rest['cost'] = int(restaurant['restaurant']['average_cost_for_two'])
		rest['address'] = restaurant['restaurant']['location']['address']
		rest['rating'] = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
		formatted_restaurant_list.append(rest)
	return formatted_restaurant_list

#Function to fetch the list of restaurants according to the input query
def get_restaurants(loc, cuisine, cost, flag):
	config={ "user_key":"ff70d931f97f11f65ee71c604015fbda"}
	zomato = zomatopy.initialize_app(config)
	location_detail=zomato.get_location(loc, 1)
	d1 = json.loads(location_detail)
	lat=d1["location_suggestions"][0]["latitude"]
	lon=d1["location_suggestions"][0]["longitude"]
	cuisines_dict={'chinese':25,'italian':55,'north indian':50,'south indian':85,'american':1,'mexican':73}

	price = cost
	if cost != None and cost.isnumeric():
		cost_num = int(cost)
		if cost_num < 300:
			price = 'low'
		elif cost_num > 700:
			price = 'high'
		else:
			price = 'mid'

	restaurant_list = []
	matching_restaurants = []
	# If cost is low, then list restaurants by sorting in asc order of cost
	# Else, list restaurants by desc rating order
	if cost == 'low':
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), sort_by="cost", order="asc", start=0, limit=20)
		d = json.loads(results)
		if d['results_found'] == 0:
			return  "Sorry! We didn't find any {cuisine} restuarants at {loc}"
		else:
			restaurant_list.extend(d['restaurants'])

			restaurants = format_restaurant_list(restaurant_list)

			budget_restaurants = list(filter(lambda rest: rest['cost'] < 300, restaurants))
			matching_restaurants = sorted(budget_restaurants, key = lambda k: k['rating'], reverse=True)
	else:
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), sort_by="rating", order="desc", start=0, limit=20)
		d = json.loads(results)
		if d['results_found'] == 0:
			return  "Sorry! We didn't find any {cuisine} restuarants at {loc}"
		else:
			restaurant_list.extend(d['restaurants'])
			for i in [20,40]:
				results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), sort_by="rating", order="desc", start=i, limit=20)
				d = json.loads(results)
				restaurant_list.extend(d['restaurants'])
			
			restaurants = format_restaurant_list(restaurant_list)

			if cost == 'high':
				matching_restaurants = list(filter(lambda rest: rest['cost'] > 700, restaurants))
			else:
				matching_restaurants = list(filter(lambda rest: rest['cost'] >= 300 and rest['cost'] <= 700, restaurants))
	#Reponse by the bot
	response = 'Here are the top five restaurants I found!\n'
	resp_format1 = '%d. %s in %s has been rated %s'
	counter1 = 5
	#Response to be sent through email
	mail_response = '~~~ Please find below the top 10 restaurants list ~~~\n\n'
	resp_format2 = '%d. Name : %s, Address : %s, Price : Rs. %d, Rating : %s'
	counter2 = 10

	for index, rest in enumerate(matching_restaurants):
		if(flag):
			response += resp_format1%(index+1, rest['name'], rest['address'], str(rest['rating']))
			response += '\n'
			counter1 -= 1
			if counter1 == 0:
				break
		else:
			mail_response += resp_format2%(index+1, rest['name'], rest['address'], rest['cost'], str(rest['rating']))
			mail_response += '\n'
			counter2 -= 1
			if counter2 == 0:
				break
	if(flag):
		return response
	else:
		return mail_response

#Custom action for "action_search_restaurants"
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		cost = tracker.get_slot('price')
		response = get_restaurants(loc, cuisine, cost, True)
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

#Custom action for checking the servicable locations
class ActionSearchServicableLocations(Action):
	def name(self):
		return 'action_check_location'
	
	def run(self, dispatcher, tracker, domain):
		f = open('data/location.txt','r')
		valid_cities = f.read().split()
		f.close()
		loc = tracker.get_slot('location')
		
		if loc.lower() in valid_cities:
			is_location_valid = True
		else:
			is_location_valid = False
		
		return [SlotSet('valid_location', is_location_valid)]

#Custom action to send mails
class SendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		emailId = tracker.get_slot('emailId')
		subject = "Foodie: Here are Top restaurants for you!" 
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		cost = tracker.get_slot('price')
		response = get_restaurants(loc, cuisine, cost, False)
		message = 'Subject: {}\n\n{}'.format(subject, response)
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls() 	
		s.login("foodiechatbot890@gmail.com", "Rasa$924") 
		try:
			s.sendmail("foodiechatbot890@gmail.com", emailId, message.encode('utf-8'))
			dispatcher.utter_message("Email sent!") 
		except Exception as e:
			print("Error occured", e)
			dispatcher.utter_message("Error occured while sending mail")