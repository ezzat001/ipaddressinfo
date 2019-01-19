###################################################################
# All Rights Reserved to Ahmed Ezzat Haggag and AuroraSoft Company#
# A Simple Script to get Information about Someones IP Address and#
# Get his Location Through Google Maps or any Online Map          #
# Used Modules: geocoder                                          #
# My Facebook Account : ezzat001                                  #
# My Instagram Account : ahmedezzatpy                             #
# My Whatsapp Number : +201553956506                              #
# 2019 © Copyrights AuroraSoft                                    #
###################################################################
import geocoder
print("            AuroraSoft Production\n                -Ahmed Ezzat")
print('Facebook : ezzat001\n')
ipinput = str(input("Enter the ip Address (enter 'me' to see your details):"))
data = geocoder.ip(ipinput)
data = data.geojson
ip = data['features'][0]['properties']['ip'] 
address = data['features'][0]['properties']['address'] 
country = data['features'][0]['properties']['country'] 
hostname = data['features'][0]['properties']['hostname']
city = data['features'][0]['properties']['raw']['city']
region = data['features'][0]['properties']['raw']['region']
latitude = data['features'][0]['properties']['lat']
longitude = data['features'][0]['properties']['lng']
print("\n=============\n*Information*\n=============")
print("IP Address :",ip)
print("Hostname :",hostname)
print("Country :",country)
print("Address :",address)
print("Region :",region)
print("City :",city)
print("===============\nLocation on Map\n===============")
print("Latitude :",latitude)
print("Longitude :",longitude)
print("\nThanks for using the Script !\nRegards,\nAhmed Ezzat Haggag - 001")

