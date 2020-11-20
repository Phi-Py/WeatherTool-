import requests as req  #for OpenWeather API
import datetime 
import pytz

#files
import weatherTool_data as data
import speechtool as speech


#PERSONAL VARS
weather_time_switch = 20  #prompt time that switches weather data from today to tomorrow in 24-hour time 
jacket_weather = 55  #temperature in f that suggests a jacket
snowgear_cap = 30  #the amount of snow in mm that requires you to bring snow gear



# Tells user whether they need a jacket now (or tomorrow if it is after weather_time_switch)

def fullDescription():
	speech.speak(speech.mimir, data.location+" currently feels like "+str(data.current_feelslike_f)+"degrees and"+data.current_description)
	#speech.speak(speech.mimir, )




def wearjacket(): 
	umbrella=0
	jacket=0
	snow=0

	if int(data.current_time_est[:2]) >= weather_time_switch:  # Setting jacket logic for tomorrow
		date = 'tomorrow'
		if data.dailytom_precip == "Snow" and (int(data.dailytom_snowvol) > snowgear_cap):
			snow = 1
		else: 
			if data.dailytom_precip == "Rain":
				umbrella=1
			elif data.dailytom_temp_day_f < jacket_weather:
				jacket=1		
	elif int(data.current_time_est[:2]) < weather_time_switch:  # Setting jacket logic for today 
		date = 'today'
		if data.daily_precip == "Snow" and int(data.daily_snowvol) > snowgear_cap:
			snow = 1
		else: 
			if data.daily_precip == "Rain":
				umbrella = 1
			elif data.daily_temp_day_f < jacket_weather:
				jacket = 1	

	if snow==1:
		speech.speak(speech.mimir,"Bring snow gear "+date)
	else:
		if umbrella==1 and jacket==1:
			speech.speak(speech.mimir,"Bring a jacket and umbrella "+date)
		elif umbrella==1 and jacket==0:
			speech.speak(speech.mimir,"Bring an umbrella "+date)
		elif umbrella==0 and jacket==1:
			speech.speak(speech.mimir,"Bring a jacket "+date)
		else:
			if date == 'today':
				speech.speak(speech.mimir, date+" is a nice "+ str(data.daily_temp_day_f) + " degrees. You don't need a jacket.")
			elif date == 'tomorrow':
				speech.speak(speech.mimir, date+" will be a nice "+ str(data.dailytom_temp_day_f) + " degrees. You don't need a jacket.")

			

wearjacket()
fullDescription()

			


