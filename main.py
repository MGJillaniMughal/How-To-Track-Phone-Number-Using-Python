# Import some common used libary

import phonenumbers

# Provide storenumberfile.py name
from storenumberfile import number

from phonenumbers import geocoder
from phonenumbers import carrier

# Write code

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))