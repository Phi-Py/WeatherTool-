import requests as req  #for OpenWeather API
import datetime 
import pytz



#OPENWEATHER VARS
key = "eac567b880fd463cdbc956e98d9dd1dd"
zipcode = '10504'
country = 'us'
latitude = '42.444471'
longitude = '-76.491595'
location = 'Ithaca New York'

#openweather url
url_onecall='https://api.openweathermap.org/data/2.5/onecall?lat='+latitude+'&lon='+longitude+'&appid='+key
 
#openweather data 
data_onecall = (req.get(url_onecall)).json()  #as json->dictionary

#current time
current_date = datetime.date.today()
current_numberday = current_date.strftime('%d')  #turning the datetime object into a string as day with the strftime method
current_time_est = datetime.datetime.now()

#current data
current_time_unix = data_onecall['current']['dt']
current_time_utc = datetime.datetime.utcfromtimestamp(data_onecall['current']['dt'])  # changing unix time to UTC
current_feelslike_f = int(((data_onecall['current']['feels_like'])-273.15)*(9/5)+32)
current_precip = data_onecall['current']['weather'][0]['main']
current_description = data_onecall['current']['weather'][0]['description']

#daily today, always at 12PM EST
daily_time_unix = data_onecall['daily'][0]['dt']
daily_time_utc = datetime.datetime.utcfromtimestamp(data_onecall['daily'][0]['dt'])
daily_temp_day_f = int(((data_onecall['daily'][0]['feels_like']['day'])-273.15)*(9/5)+32)
daily_precip = data_onecall['daily'][0]['weather'][0]['main']
try:  #avoiding errors for rain/snow key 
	daily_rainvol = data_onecall['daily'][0]['rain']
except KeyError:
	print('')
try:  #avoiding errors for rain/snow key 
	daily_snowvol = data_onecall['daily'][0]['snow']
except KeyError:
	print('')
if int(current_numberday) != int(daily_time_utc.strftime('%d')):  #checking that the request pull is giving today's daily weather
	speech.speak(speech.mimir, "Weather request is not functioning properly. Check the weather tool file line 44 for more information.")


#daily tomorrow, always at 12PM EST
dailytom_time_unix = data_onecall['daily'][1]['dt']
dailytom_time_utc = datetime.datetime.utcfromtimestamp(data_onecall['daily'][1]['dt'])
dailytom_temp_day_f = int(((data_onecall['daily'][1]['feels_like']['day'])-273.15)*(9/5)+32)
dailytom_precip = data_onecall['daily'][1]['weather'][0]['main']
try: 
	dailytom_rainvol = data_onecall['daily'][1]['rain']
except KeyError:
	print('')
try:
	dailytom_snowvol = data_onecall['daily'][1]['snow']
except KeyError:
	print('')
if int(current_numberday)+1 != int(dailytom_time_utc.strftime('%d')):  #checking that the request pull is giving tomorrows's daily weather
	speech.speak(speech.mimir, "Weather request is not functioning properly. Check the weather tool file line 52 for more information.")




