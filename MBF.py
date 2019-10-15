#!/bin/usr/python
import requests
id = input("Enter ID list : ")
pw = input("password to crack : ")

link = "https://m.facebook.com/login.php"
data = ("email":id. "pass":pw")
r = requests.post(link. data-data)
print (r-url)

