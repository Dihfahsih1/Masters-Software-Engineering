__author__ = 'BackOffice-3'


import builtwith
import requests




#url = input("Enter url")


website = builtwith.parse("itechlabs.com.au")
print (website)
for key, value in website.items():
    print(key + ":",", ".join(value))


