import requests
import time 
import main_script_file 
import os


PgNo=10
TotalPages=40#This number of pages it will scrap data

while PgNo<=TotalPages: 
	base_url="https://www.google.co.in"
	keyword=('QA Companies') # Kewyword to scrap data for
	payload = {'q':keyword, 'start':PgNo}
	#headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
	data=main_script_file.generate_html(base_url,payload)
	final_data=main_script_file.parsing_data(data)
	PgNo=PgNo+10
	time.sleep(60)

print ('Your script has been executed! Bye')


	
