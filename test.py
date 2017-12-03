import requests
import json
import re
response = requests.get('http://localhost:5000/interview/api/v1.0/results')
jason_data = response.json()

#Test 1   
def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False
   
def validating_area_code(ex_data):   
    for i in range(11):   
        jason_areacode = (ex_data[i]['area_code'])
        print jason_areacode
        y = intTryParse(jason_areacode)
        if y[1] == True and len(jason_areacode)==3:
            print "valid area code"
        else:
            print "invalid area code"
print "\nTest 1"    
validating_area_code(jason_data)    
    
#Test 2
    
def area_code_is_not_null(ex_data): 
    for i in range(11):   
        jason_areacode = ex_data[i]['area_code']
        print jason_areacode
        if jason_areacode != " ":
            print "Area code is not empty"
        else :
            print "area code is empty"

print "\nTest 2"            
area_code_is_not_null(jason_data)    

#Test 3
 
def checking_for_successful_get_response(postman_getdata):
    if postman_getdata.status_code == 200: 
        print "GET response successful for the url " + response.url
    else :
        print  "Error"

print "\nTest 3"        
checking_for_successful_get_response(response)

  
  
#Test 4

def validity_of_phonenumber_format(ex_data) :
    for i in range(11) :
        jason_phonenumber = ex_data[i]['phone_number']
        print jason_phonenumber
        if len(jason_phonenumber) ==12 and re.match(r'^\d{3}-\d{3}-\d{4}$', jason_phonenumber) :
            print "phone number is in correct format"
        else :
            print "Please enter the phone number in ***-***-**** format"
            
print "\nTest 4"
validity_of_phonenumber_format(jason_data)
 
 
 
#Test 5


def strTryParse(value):
    try:
        return str(value), True
    except ValueError:
        return value, False



def checking_if_comment_is_string(ex_data):
    for i in range(11):   
        jason_comment = ex_data[i]['comment']
        y = strTryParse(jason_comment)
        print y
        if y[1] == True:
            print "comment is in string format"
        else:
            print "The comment has undefined characters "

        print "\n"
        
print "\nTest 5"        
checking_if_comment_is_string(jason_data)




 