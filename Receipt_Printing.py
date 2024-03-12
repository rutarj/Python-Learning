# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:34:02 2024

@author: rutar
"""

#Decarling all the variables 

#Creating a product and price for three items 
p1_name, p1_price = 'Books', 49.95
p2_name, p2_price = "Computer" , 579.99
p3_name, p3_price = "Monitor" , 124.99

#Creating names for company

company_name = "Coding Temple, Inc."
company_location = "283 Franklin St."
company_city = "Boston, MA"

#declaring ending message

message = "Thanks for shopping with us Today!"


#Starting to write the program 

#Top border line
print('\n')
print("*" *50)
print('\n')


print("\t\t", company_name)
print("\t\t", company_location)
print("\t\t", company_city)

print('\n')
print('=' * 50)

print("\t Product Name \t Product Price")
print("\t ", p1_name, "\t\t ${}" .format(p1_price))
print("\t ", p2_name, "\t\t ${}" .format(p2_price))
print("\t ", p3_name, "\t\t ${}" .format(p3_price))
print("\n")


print("=" *50)
total = p1_price+p2_price+p3_price
print("\t\t\t\tTotal")

print("\t\t\t\t" , int(total))
print("=" *50)
print("\t", message)

print("*" *50)



