#Brett Lamb
#10/11/2026
#Github: https://github.com/BrettLambSCF/COP2373
# This program has functions to validate phone numbers, social security numbers and
# zip codes using regular expressions. There is a main function to get input from a user
# and then it displays if the phone number, social security number and zip code they entered
# is valid or not.

#Import the regular expression module

import re

#If function is called with a phone# as parameters, it gets stored in phone variable
def check_phone_num(phone):
    #re.match will check if the phone number in phone variable matches the needed pattern
    # the r means it's a raw string, ^ says start pattern here, \d means digits from 0 to 9,
    #3 means it has to be 3 of those digits, - means there has to be a hyphen, \d{3} and \d{4}
    #means there needs to be 3 and 4 digits, and $ signals the end of the input
    if re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
        #if the phone # matches required input, the function returns as true and false if it's invalid
        return True
    else:
        return False

#If function is called with a ssn as parameters, it gets stored in ssn variable
def check_ssn_num(ssn):
    #re.match will check if the social security number in the ssn variable matches the needed pattern
    if re.match(r"^\d{3}-\d{2}-\d{4}$", ssn):
        #if the ssn matches required input, the function returns as true and false if it's invalid
        return True
    else:
        return False

#If function is called with a zipcode as parameters, it gets stored in zipcode variable
def check_zipcode(zipcode):
    #re.match will check if the zipcode in the zipcode variable matches the needed pattern
    if re.match(r"^\d{5}(-\d{4})?$", zipcode):
        #if the zipcode matches required input, the function returns as true and false if it's invalid
        return True
    else:
        return False

def main():

    #Get the phone, ssn, and zipcode from user to be stored in their respective variables
    phone = input("Please enter your phone number: ")
    ssn = input("Please enter your social security number: ")
    zipcode = input("Please enter your zip code: ")

    #Checks if the above check_phone_num function returns true or false
    if check_phone_num(phone):
        print("The entered phone number is valid")
    else:
        print("The entered phone number isn't valid")
    # Checks if the above check_ssn_num function returns true or false
    if check_ssn_num(ssn):
        print("That is a valid social security number")
    else:
        print("That isn't a valid social security number")
    # Checks if the above check_zipcode function returns true or false
    if check_zipcode(zipcode):
        print("That zipcode is valid")
    else:
        print("That zipcode isn't valid")

main()