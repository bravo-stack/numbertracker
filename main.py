import json
from typing import List
import phonenumbers 
from phonenumbers import geocoder
from urllib import response
from urllib.request import urlopen

phonenumbers00 = phonenumbers.parse("+2349048188177")
output_info = geocoder.description_for_number(phonenumbers00, 'en')

print(output_info)

url = 'https://ipinfo.io/'

response = urlopen(url)











