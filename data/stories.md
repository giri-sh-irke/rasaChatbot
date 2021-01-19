## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mangalore"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_priceRange
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "mangalore"}
    - utter_ask_resultToBeMailed
* sending_email{"emailId": "pai.shreyas08@gmail.com"}
    - slot{"emailId": "pai.shreyas08@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_resultToBeMailed
* sending_email{"emailId": "pai.study08@gmail.com"}
    - slot{"emailId": "pai.study08@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "south indian", "location": "mysore"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "mysore"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_resultToBeMailed
* sending_email{"emailId": "pai.shreyas08@gmail.com"}
    - slot{"emailId": "pai.shreyas08@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "mid", "location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"price": "mid"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_resultToBeMailed
* sending_email{"emailId": "gpoojitha25@gmail.com"}
    - slot{"emailId": "gpoojitha25@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "udupi"}
    - slot{"location": "udupi"}
    - action_check_location
    - slot{"valid_location": false}
    - utter_default
* restaurant_search{"location": "mangalore"}
    - slot{"location": "mangalore"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_priceRange
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "mangalore"}
    - utter_ask_resultToBeMailed
* negation
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_priceRange
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_resultToBeMailed
* sending_email{"emailId": "pai.shreyas08@gmail.com"}
    - slot{"emailId": "pai.shreyas08@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "chennai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_priceRange
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_resultToBeMailed
* negation
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "sakleshpur"}
    - slot{"location": "sakleshpur"}
    - action_check_location
    - slot{"valid_location": false}
    - utter_default
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_priceRange
* restaurant_search{"price": "200"}
    - slot{"price": "200"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_resultToBeMailed
* sending_email{"emailId": "pai.study08@gmail.com"}
    - slot{"emailId": "pai.study08@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_priceRange
* negation{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_resultToBeMailed
* sending_email{"emailId": "pai.study08@gmail.com"}
    - slot{"emailId": "pai.study08@gmail.com"}
    - action_send_mail
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"valid_location": false}
    - utter_default
* restaurant_search{"location": "prayagraj"}
    - slot{"location": "prayagraj"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_priceRange
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "prayagraj"}
    - utter_ask_resultToBeMailed
* sending_email{"emailId": "gpoojitha25@gmail.com"}
    - slot{"emailId": "gpoojitha25@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_priceRange
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_resultToBeMailed
* affirm
    - utter_ask_emailAddress
* sending_email{"emailId": "pai.study08@gmail.com"}
    - slot{"emailId": "pai.study08@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"valid_location": false}
    - utter_default
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_priceRange
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_resultToBeMailed
* affirm
    - utter_ask_emailAddress
* sending_email{"emailId": "pai.study08@gmail.com"}
    - slot{"emailId": "pai.study08@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_priceRange
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_resultToBeMailed
* negation
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "north indian", "location": "Nagpur"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_priceRange
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Nagpur"}
    - utter_ask_resultToBeMailed
* affirm
    - utter_ask_emailAddress
* sending_email{"emailId": "girish.shirke999@gmail.com"}
    - slot{"emailId": "girish.shirke999@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Baramati"}
    - slot{"location": "Baramati"}
    - action_check_location
    - slot{"valid_location": false}
    - utter_default
* restaurant_search{"location": "Wuhan"}
    - slot{"location": "Wuhan"}
    - action_check_location
    - slot{"valid_location": false}
    - utter_default
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_priceRange
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_resultToBeMailed
* negation
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Pune", "cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_priceRange
* restaurant_search
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_resultToBeMailed
* affirm
    - utter_ask_emailAddress
* sending_email{"emailId": "girish.shirke999@gmail.com"}
    - slot{"emailId": "girish.shirke999@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Jaipur", "price": "high"}
    - slot{"location": "Jaipur"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - utter_ask_resultToBeMailed
* affirm
    - utter_ask_emailAddress
* sending_email{"emailId": "girish.shirke999@gmail.com"}
    - slot{"emailId": "girish.shirke999@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "300", "cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "300"}
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_resultToBeMailed
* negation
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "700", "cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "700"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"valid_location": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_resultToBeMailed
* affirm
    - utter_ask_emailAddress
* sending_email{"emailId": "girish.shirke999@gmail.com"}
    - slot{"emailId": "girish.shirke999@gmail.com"}
    - action_send_mail
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "Poona", "cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Poona"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"valid_location": false}
    - utter_default
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_resultToBeMailed
* negation
    - utter_goodbye
    - action_restart
