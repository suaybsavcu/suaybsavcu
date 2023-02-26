import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+905309584025")


print("\nphone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));

#LETS TRACK PHONE NUMBERS