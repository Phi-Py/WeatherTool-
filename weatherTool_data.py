import requests as req  #for OpenWeather API
import datetime 
import pytz



#OPENWEATHER VARS
key = "eac567b880fd463cdbc956e98d9dd1dd"
zipcode = '14850'
country = 'us'
latitude = '42.444471'
longitude = '-76.491595'
location = 'Ithaca New York'

#openweather url
url_onecall='https://api.openweathermap.org/data/2.5/onecall?lat='+latitude+'&lon='+longitude+'&appid='+key
 
#openweather data 
data_onecall = (req.get(url_onecall)).json()  #as json->dictionary



#current time
current_date = datetime.date.today()  # native current year-month-day 
current_numberday = current_date.strftime('%d')  # native current day number 
current_weekday = str(datetime.datetime.now().strftime('%A'))  # native current weekday 
current_time_est = str(datetime.datetime.now().strftime('%X'))  # native current time in hours:minute:second



#current data
current_time_unix_utc_weather = data_onecall['current']['dt']  # current unix dt in utc from openweather 
current_date_weather = datetime.datetime.fromtimestamp(data_onecall['current']['dt'])  # current utc date from openweather
current_time_est_weather = datetime.datetime.fromtimestamp(data_onecall['current']['dt']).strftime('%X')  # current est time from openweather
if current_time_est_weather != current_time_est:  # ensuring that the current openweather and native est time are equal
	delay_seconds = abs(int(current_time_est_weather[-2:])-int(current_time_est[-2:]))
	print("ERROR, openweather is not sourcing current time. Delay is "+str(delay_seconds)+" seconds. Check line 33 for more information")
current_temp_f = int(((data_onecall['current']['temp'])-273.15)*(9/5)+32)  # current temperature 
current_feelslike_f = int(((data_onecall['current']['feels_like'])-273.15)*(9/5)+32)  # current feels like temperature  
current_precip = data_onecall['current']['weather'][0]['main']  # current precipitation
current_description = data_onecall['current']['weather'][0]['description']  # current description 



#daily data, always at 11am EST
daily_time_unix_utc_weather = data_onecall['daily'][0]['dt']  # daily (4pm utc) unix dt in utc from openweather
daily_date_weather = datetime.datetime.fromtimestamp(data_onecall['daily'][0]['dt'])  # daily (4pm utc) date from openweather
daily_time_est_weather = datetime.datetime.fromtimestamp(data_onecall['daily'][0]['dt']).strftime('%X')  # daily time (11am est) from openweather
if daily_time_est_weather != "11:00:00":  # ensuring that openweather is taking daily time at 11am est
	print("ERROR, openweather is not sourcing accurate time. Check line 43 for more information.")
daily_temp_day_f = int(((data_onecall['daily'][0]['temp']['day'])-273.15)*(9/5)+32)  # daily (11am est) day temperature
daily_feelslike_f = int(((data_onecall['daily'][0]['feels_like']['day'])-273.15)*(9/5)+32)  # daily (11am est) day feels like temperature  
daily_precip = data_onecall['daily'][0]['weather'][0]['main']  # daily (11am est) precipitation 
daily_description = data_onecall['daily'][0]['weather'][0]['description']  # daily (11am est) description 
try:  #avoiding errors for rain/snow key 
	daily_rainvol = data_onecall['daily'][0]['rain']  # daily (11am est) rain volume
except KeyError:
	print('',end='')
try:  #avoiding errors for rain/snow key 
	daily_snowvol = data_onecall['daily'][0]['snow']  # daily (11am est) snow volume
except KeyError:
	print('',end='')
if int(current_numberday) != int(daily_date_weather.strftime('%d')):  #checking that the request pull is giving today's daily weather
	speech.speak(speech.mimir, "Weather request is not functioning properly. Check line 53 for more information.")



#daily tomorrow, always at 12PM EST
dailytom_time_unix_utc_weather = data_onecall['daily'][1]['dt']  #tomorrow daily unix dt from openweather
dailytom_date_weather = datetime.datetime.fromtimestamp(data_onecall['daily'][1]['dt'])  # tomorrow daily (4pm UTC) date from openweather
dailytom_time_est_weather = datetime.datetime.fromtimestamp(data_onecall['daily'][1]['dt']).strftime('%X')  # tomorrow daily time (11am est) from openweather
if dailytom_time_est_weather != "11:00:00":
		print("ERROR, openweather is not sourcing accurate time. Check line 66 for more information.")
dailytom_temp_day_f = int(((data_onecall['daily'][1]['temp']['day'])-273.15)*(9/5)+32)  # tomorrow daily (11am est) day temperature 
dailytom_feelslike_f = int(((data_onecall['daily'][1]['feels_like']['day'])-273.15)*(9/5)+32)  # tomorrow daily (11am est) day feels like temperature
dailytom_precip = data_onecall['daily'][1]['weather'][0]['main']  # tomorrow daily (11am est) precipitation 
try: 
	dailytom_rainvol = data_onecall['daily'][1]['rain']  # tomorrow daily (11am est) rain volume 
except KeyError:
	print('',end='')
try:
	dailytom_snowvol = data_onecall['daily'][1]['snow']  # tomorrow daily (11am est) snow volume
except KeyError:
	print('',end='')
if int((current_date + datetime.timedelta(days=1)).strftime('%d')) != int(dailytom_date_weather.strftime('%d')):  #checking that the request pull is giving tomorrows's daily weather
	speech.speak(speech.mimir, "Weather request is not functioning properly. Check the weather tool file line 52 for more information.")


