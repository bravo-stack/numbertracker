import json
from re import split
from typing import List
import phonenumbers
from phonenumbers import geocoder
from urllib import response
from urllib.request import urlopen

phone_number = str(input("input your mobile number in the official format: "))

phone_number = phonenumbers.parse(phone_number)
output_info = geocoder.description_for_number(phone_number, 'en')

print(output_info)

url = 'https://ipinfo.io/'

data = json.load(urlopen(url))

# print out data
print(data)