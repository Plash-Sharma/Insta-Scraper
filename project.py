from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import sys
import time
import maskpass
from tabulate import tabulate
import csv
import os

def main():
    username,password,target,num_posts=enter()
    driver=webdriver.Chrome()
    login(driver,username,password)
    link=links(driver,target,(num_posts-1)) #get list of links
    if(len(link)==0):
        raise Exception("No posts available")
    likes,dates=scrape(driver,link) #get list of dates and likes by visiting links
    #create Table on terminal window
    tablulate_(link,likes,dates)
    #create CSV File
    csv_file(link,dates,likes)
    driver.close()
    path="C:\CS50\CS50P Project\I_SCRAPE.csv"
    openexcel(path)


def enter():
    try :
        username=input("Enter your Username : ")
        password=maskpass.askpass(prompt = "Enter your Password : ", mask='*')
        target=input("Enter the profile you want to scrape : ")
        num_posts=int(input("Enter number of posts you want to scrape : "))
        return username,password,target,num_posts
    except:
        sys.exit("values not in proper format")

def login(driver,username,password):
    url=requests.get(f"https://www.instagram.com/{username}")
    if(url.status_code !=200):
        raise NameError


    #Visiting instagram page
    driver.get(f"https://www.instagram.com/")
    time.sleep(3)
    username_element=driver.find_element(By.NAME,"username") #taking username element
    password_element=driver.find_element(By.NAME,"password") #taking password element
    username_element.send_keys(f"{username}")
    time.sleep(3)
    password_element.send_keys(f"{password}")
    time.sleep(3)
    password_element.send_keys(Keys.RETURN)
    time.sleep(6)

def links(driver,target,num_posts):
    #extracting links
    #visiting profile
    driver.get(f"https://www.instagram.com/{target}")
    time.sleep(6)
    url=requests.get(f"https://www.instagram.com/{target}")

    #check for availability of account
    if(url.status_code !=200):
        raise NameError
        
    posts=driver.find_elements(By.TAG_NAME,'a')

    post_links=[]

    for post in posts:
        href=post.get_attribute('href')
        if '/p/' in href:
            post_links.append(href)
            
        if(len(post_links)>num_posts):
            break
    return post_links

def scrape(driver,links):
    likes=[]
    dates=[]
    #extracting links
    for link in links:
        driver.get(f"{link}")
        time.sleep(3)
        spans = driver.find_elements(By.TAG_NAME, 'span')
        time.sleep(1)
        for span in spans:
            like=span.get_attribute('innerHTML')
            if 'html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs'in span.get_attribute('class'):
                likes.append(like)
                time_=driver.find_element(By.TAG_NAME, 'time')
                date=time_.get_attribute('title')
                dates.append(date)
    return likes,dates

def tablulate_(links,likes,dates):
    #creating table
    table=[]
    for i in range(len(links)):
        table.append([links[i],likes[i],dates[i]])
    headers=["POST LINK","LIKES","DATES"]
    print(tabulate(table,headers,tablefmt="pretty"))

def csv_file(links,dates,likes):
    #create csv file
    with open("I_SCRAPE.csv","w+") as f:
        headers=["POST LINKS","LIKES","DATES"]
        csvfile=csv.DictWriter(f,fieldnames=headers)
        csvfile.writeheader()
        for i in range(len(links)):
            csvfile.writerow({"POST LINKS":links[i],"LIKES":likes[i],"DATES":dates[i]})

def openexcel(path):
    permission=input("Enter Y or N to open excel sheet for csv file : ").lower()
    if(path!='C:\CS50\CS50P Project\I_SCRAPE.csv'):
        raise FileNotFoundError
    elif(path=='C:\CS50\CS50P Project\I_SCRAPE.csv' and permission=='y'):
        os.startfile(path)
    else:
        raise ValueError
if __name__=="__main__":
    main()

