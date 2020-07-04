from playsound import playsound
from gtts import gTTS
import requests
import json
import time
import os
url = "https://api.thevirustracker.com/free-api?global=stats"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload).json()
print(str(response))
print()

total_cases = response["results"][0]["total_cases"]
text = ("there are " + str(total_cases) + "people infected with corona right now. thats pretty sick ")
op = gTTS(text=text, slow=False)
op.save("op.mp3")
playsound("op.mp3")
os.system("del op.mp3")
