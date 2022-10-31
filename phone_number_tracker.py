import phonenumbers
from phonenumbers import geocoder

phone_num4=phonenumbers.parse(input("Enter a phone number:"))
print(geocoder.description_for_number(phone_num4,"en"))
