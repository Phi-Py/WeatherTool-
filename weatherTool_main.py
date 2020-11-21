import requests as req  #for OpenWeather API
import datetime 
import pytz


#files
import weatherTool_data as data
import speechtool as speech
 


#PERSONAL VARS
weather_time_switch = 18  #prompt time that switches weather data from today to tomorrow in 24-hour time 
jacket_weather = 55  #temperature in f that suggests a jacket
snowgear_cap = 30  #the amount of snow in mm that requires you to bring snow gear



# Tells user whether they need a jacket now (or tomorrow if it is after weather_time_switch)


activeLocation = data.Location("14850", "us", "42.444471", "-76.491595", "Ithaca")



def currentDescription():
	activeLocation.liveCall()
	currentData = activeLocation.currentData()
	
	time = str(activeLocation._current_time_est_hour_12hour +" " + activeLocation._current_time_est_minute_12hour)  # code to give spoken time 
	if str(activeLocation._current_time_est_hour_12hour)[0] == "0":
		time = str(activeLocation._current_time_est_hour_12hour)[-1] +" " + str(activeLocation._current_time_est_minute_12hour)

	speech.speak(speech.mimir, activeLocation._location+" at "+ time+ " currently feels like "+str(currentData[0])+"degrees and"+currentData[2])
	


def wearjacket(): 
	umbrella=0
	jacket=0
	snow=0

	activeLocation.liveCall()
	tomorrowData = activeLocation.tomorrowData()
	todayData = activeLocation.dailyData()

	if int(activeLocation._current_time_est[:2]) >= weather_time_switch:  # Setting jacket logic for tomorrow
		date = 'tomorrow'
		if tomorrowData[1] == "Snow" and (int(tomorrowData[-1]) > snowgear_cap):
			snow = 1
		else: 
			if tomorrowData[1] == "Rain":
				umbrella=1
			elif tomorrowData[0] < jacket_weather:
				jacket=1		
	elif int(activeLocation._current_time_est[:2]) < weather_time_switch:  # Setting jacket logic for today 
		date = 'today'
		if todayData[1] == "Snow" and int(todayData[-1]) > snowgear_cap:
			snow = 1
		else: 
			if todayData[1] == "Rain":
				umbrella = 1
			elif todayData[0] < jacket_weather:
				jacket = 1	

	if snow==1:  # snow decision 
		speech.speak(speech.mimir,"Bring snow gear "+date) 
	else:
		if umbrella==1 and jacket==1:  # cold rain decision
			speech.speak(speech.mimir,"Bring a jacket and umbrella "+date)
		elif umbrella==1 and jacket==0:  # rain decision
			speech.speak(speech.mimir,"Bring an umbrella "+date)
		elif umbrella==0 and jacket==1:  # jacket decision
			speech.speak(speech.mimir,"Bring a jacket "+date)
		else:
			if date == 'today':  # no jacket decision 
				speech.speak(speech.mimir, date+" is a nice "+ str(todayData[0]) + " degrees. You don't need a jacket.")
			elif date == 'tomorrow':  # no jacket decision
				speech.speak(speech.mimir, date+" will be a nice "+ str(tomorrowData[0]) + " degrees. You don't need a jacket.")

			


currentDescription()
#wearjacket()



			


