import os
import sys
from random import randint

# randomly generate a serial number
serial_number = randint(10000000, 99999999)
serial_number = str(serial_number)

# File containing 100 top city names
if os.path.getsize("cities.txt") < 256000000:
    f1 = open("cities.txt", "r")
    city_list = [line.rstrip() for line in f1]
    f1.close
else:
    raise Exception("File size must be under 256MB")
    sys.exit(1)

# variable to select a random city from city_list
city_number = randint(0, 99)

# set city
city = city_list[city_number]

# variables for random component type
if os.path.getsize("numbers.txt") < 256000000:
    f2 = open("numbers.txt", "r")
    component_number = str(randint(1, 20))
    component_number_typed_out = [line.rstrip() for line in f2]
    f2.close
else:
    raise Exception("File size must be under 256MB")
    sys.exit(1)


component_selector = randint(0, 15)

# add randomization for capitalization of component and number
# and determine if number will be typed out or not
w = randint(0, 50)
x = randint(0, 50)
y = randint(0, 50)
z = randint(0, 50)


component_number_selector = randint(0, 19)

if os.path.getsize("component.txt") < 256000000:
    f3 = open("component.txt", "r")
    component_list = [line.rstrip() for line in f3]
    f3.close
    component = component_list[component_selector]
    component_final = None
else:
    raise Exception("File size must be under 256MB")
    sys.exit(1)

if x % 2 == 0:
    component = component.capitalize()

if y % 2 == 0:
    component_number = component_number_typed_out[component_number_selector]
    if z % 2 == 0:
        component_number = component_number.capitalize()

# if statements to determine whether to print name and/or number
# or number and/or name
if w % 4 == 0:
    component_final = component_number

if w % 4 == 1:
    component_final = component

if w % 4 == 2:
    component_final = component + " " + component_number

if w % 4 == 3:
    component_final = component_number + " " + component


# decide how many parts and what order to create company name
if os.path.getsize("company.txt") < 256000000:
    f4 = open("company.txt", "r")
    co_name = [line.rstrip() for line in f4]
    f4.close
else:
    raise Exception("File size must be under 256MB")
    sys.exit(1)

if os.path.getsize("company_type.txt") < 256000000:
    f5 = open("company_type.txt", "r")
    co_type = [line.rstrip() for line in f5]
    f5.close()
else:
    raise Exception("File size must be under 256MB")
    sys.exit(1)

if os.path.getsize("company_corp_type.txt") < 256000000:
    f6 = open("company_corp_type.txt", "r")
    co_corp = [line.rstrip() for line in f6]
    f6.close()
else:
    raise Exception("File size must be under 256MB")
    sys.exit(1)

co_name_len = len(co_name)
co_name_number = randint(0, co_name_len - 1)

co_type_len = len(co_type)
co_type_number = randint(0, co_type_len - 1)

co_corp_type_len = len(co_corp)
co_corp_type_number = randint(0, co_corp_type_len - 1)

# variables for name creation randomization
a = randint(0, 50)
b = randint(0, 50)
c = randint(0, 50)
d = randint(0, 50)


company = co_name[co_name_number]
company_type = co_type[co_type_number]
company_corp = co_corp[co_corp_type_number]

company_final = None

if a % 2 == 0:
    company = company.lower()

if b % 2 == 0:
    company_type.capitalize()

if c % 2 == 0:
    company_corp.capitalize()

# if statements for name randomization
if d % 4 == 0:
    company_final = company

if d % 4 == 1:
    company_final = company + " " + company_type

if d % 4 == 2:
    company_final = company + " " + company_corp

if d % 4 == 3:
    company_final = company + " " + company_type + " " + company_corp

# read in default.xml so values can be replaced
if os.path.getsize("default.xml") < 256000000:
    f7 = open("default.xml", "r+")
    changed_file = f7.read()
    f7.close()
else:
    raise Exception("File size must be under 256MB")
    sys.exit(1)

# rename defaul.xml to default_original.xml
os.rename("default.xml", "default_original.xml")
print "default.xml renamed to default_original.xml"

# find and replace values that need to be changed
changed_file = changed_file.replace("Mouser Factory", company_final)
changed_file = changed_file.replace("Technodrome", component_final)
changed_file = changed_file.replace("Venus", city)
changed_file = changed_file.replace("88111222", serial_number)

# create new default file with random values created earlier
f8 = open("default.xml", "w")
f8.write(changed_file)
f8.close()


print "changes have now been written to default.xml"
print "Mouser Factory changed to " + company_final
print "Technodrome changed to " + component_final
print "Venus changed to " + city
print "88111222 changed to " + serial_number
