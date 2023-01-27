#!/usr/bin/python3
import os
import re
import random
import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import json
import socket
from random import randint
from urllib.request import Request, urlopen
from urllib.parse import urljoin
# import scrapy

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


# Display Banner
def banner():
    print("\n\n")
    print("""\033[1;32;40m
                         .............  
                      ................. 
                    .......        .....
                 ........          .....
               .......            ......
            ***********        ........ 
          ***************    .......    
       ********......*****........      
     *******    ...............         
  ********        ..........            
 ******            *******              
******          ********                
 *****        *******                   
 ******************                     
   *************     
    *════════════════════════════════════════════════════════════════*
      ╔════════════════════════════════════════════════════════════╗
      ║     By        : SUJAY ADKESAR                              ║                                                                          
      ║     Github    : https://github.com/sujayadkesar            ║
      ║     Licence   : MIT                                        ║
      ║     Code      : Python                                     ║ 
      ╚════════════════════════════════════════════════════════════╝
    *════════════════════════════════════════════════════════════════*
    """)
    print("\n")



# Get inputs from user
def get_user_inputs():
    global target_domain
    global website_name
    website_name = input("\033[1;36;40m [*] Enter the target website name! :-  ")
    target_domain = f"https://{website_name}"
    # dir_name = input("\n\n [*] Enter the name of new directory to store scan results :- ")
    # os.system('cd ~/Desktop')
    # path = os.getcwd()
    # os.system(f'mkdir {path}/{dir_name}')
    # os.system(f'cd {dir_name}')



# Finding Domai ip_address
def domain_ip():
    print("\n\n======================={   IP Details   }===========================\n\n")
    global website
    website = website_name
    try:
        print(f"\n\033[0;35m\033[1m\tHost name: \033[1m\033[0;32m \t{target_domain} \n")
        host_ip = socket.gethostbyname(website)
        print(f"\n\033[0;35m\033[1m\tDomain IP: \033[1m\033[0;32m \t{host_ip} \n")
        # print(host_ip)
    except:
        print("Unable to get Hostname and IP")

    response = requests.get(f'https://ipapi.co/{host_ip}/json/').json()
    print("\n\n\033[0;35m\033[1m\tDouble IP verification using IPinfo.io")
    print("\n\033[0;35m\033[1m\tResults:\033[0m\033[0;32m")
    response = requests.get(f'https://ipinfo.io/{host_ip}/json')
    data = json.loads(response.text)
    ip = data['ip']
    organization = data['org']
    city = data['city']
    region = data['region']
    country = data['country']
    location = data['loc']
    postal = data['postal']
    timezone = data['timezone']
    print("\tip            :", ip)
    print("\torganization  :", organization)
    print("\tcity          :", city)
    print("\tregion        :", region),
    print("\tcountry       :", country)
    print("\tpostal        :", postal)
    print("\tlocation      :", location)
    print("\ttimezone      :", timezone)
    print("\n\n")
    
    for i in tqdm(range(100)):
        time.sleep(0.06)
    print("\n\n")






def find_all_links():
    url = f"{target_domain}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")


    links = []
    for link in soup.find_all("a"):
        link_url = link.get("href")
        
        if link_url is not None:
            if "http" in link_url:
                links.append(link_url)
            else:
                links.append(urljoin(url, link_url))
    
    for ln in links:
        print(f"{ln}\n")


        

def main():
    banner()
    get_user_inputs()
    domain_ip()
    find_all_links()

main()



def everylink():
    class MySpider(scrapy.Spider):
        name = 'example.com'
        start_urls = ['https://www.example.com']
        
    def parse(self, response):
        for link in response.css('a::attr(href)'):
            yield response.follow(link, self.parse)

