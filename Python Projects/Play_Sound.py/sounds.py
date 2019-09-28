# USING PYDUB LOOK INTO DOCUMENTATION FOR MORE 
import time
from pydub import AudioSegment
from pydub.playback import play

alarm = AudioSegment.from_file("alarm.mp3", format="mp3")

alarm = alarm[:10*200]

alarmSet = int(input("How many seconds would you like to sleep?"))

alarmTime = int(time.process_time()) + alarmSet


while True:
	if int(time.process_time()) == alarmSet:
		print("Wake up!")
		play(alarm)

		break
	
