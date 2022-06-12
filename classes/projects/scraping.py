#!/usr/bin/python

#####################
#   project_accesing_DOM elements
#   Jabir Hassan
#   date: 10/6/2022
#####################

import requests
from bs4 import BeautifulSoup as bs

user_name = "samihahassan"#input("enter your username")
url = "github.com/hassanjabir"+user_name#input(Enter site url)
results= requests.get(url)


soup = bs(results.content, "html.parser")
profile_pic = soup.find('img' , {'alt': 'Avatar'})['src']
print(profile_pic)