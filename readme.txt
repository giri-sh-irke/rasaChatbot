Version of tools used:
- Python 3.7.4
- Rasa 1.10.1


NOTE:
- Updated restaurant_search method in zomatopy.py 
-- to handle sort
-- to handle offset-limit as it responds with only 20 restaurants
(Please use the same zomatopy file)

- The Zomato API sometimes takes longer than expected, and may result in timeout
In this case, please reduce the list to [20] from [20,40] on line 64 of actions.py
- This would affect the number of restaurants displayed in the response/mail
- This logic is needed as Zomato search API gives only 20 results 
OR
- We can set an environment variable to - "export RASA_SHELL_STREAM_READING_TIMEOUT_IN_SECONDS=90"