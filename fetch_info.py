from time import sleep
from selenium import webdriver
import csv
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
import sys, os
import traceback
import datetime
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import time

def scrap(idd,pas,keyy,typee,scrll,num,msgg):
	driver = webdriver.Firefox(executable_path="geckodriver.exe")
	driver.get('https://www.facebook.com/')
	email_bar=driver.find_element_by_name("email").send_keys(idd)#uoyukote@email1.io
	pass_bar=driver.find_element_by_name("pass").send_keys(pas)#Seecs@123
	sleep(2)
	click_login=driver.find_element_by_name("login").click()
	sleep(5)
	groups_link = []

	def user_message(url,count):
		try:
			driver.get(url)
			stringOfWords = msgg
			sleep(10)
			driver.find_element_by_css_selector('div[aria-label="Message"]').click()
			sleep(5)
			driver.find_element_by_css_selector('div[class="x78zum5 x1iyjqo2 xq8finb x16n37ib x1xmf6yo x1e56ztr xeuugli x1n2onr6"]').click()
			# driver.find_element_by_css_selector('div[class="x78zum5 x1a02dak x13a6bvl"]').clear()
			mess = driver.find_element_by_css_selector('div[class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw x1iyjqo2 x1gh3ibb xisnujt xeuugli x1odjw0f notranslate"]')
			for char in stringOfWords:
				mess.send_keys(char)
			sleep(2)	
			mess.send_keys(Keys.ENTER)
			sleep(2)
			driver.find_element_by_css_selector('div[aria-label="Close chat"]').click()

			with open("msg.txt", "w") as file:
				file.write(str(count))
			print("Messages Sent:",count)
			
		except Exception as e :
			count =  int(count)-1
			print("not get ",e)
			pass	

	driver.get(f"https://www.facebook.com/search/{typee}/?q={keyy}")
	for i in range(0,int(scrll)):
		print(i)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(5)
	groups = driver.find_element_by_class_name('x1xwk8fm')
	group = groups.find_elements_by_class_name('x1yztbdb')
	for link in group:
		memb = link.text
		s = " ".join(memb.split())
		print(memb)
		print("111",s)
		members_match = re.search(r'(\d+(\.\d+)?[mkMK]?)\s*(followers|members)', s)
		print("ghgdhgsdh",members_match)
		try:
			members_count = members_match.group(1)
		except:
				members_count = 0 
		print(members_count)
		tagg = link.find_elements_by_tag_name("a")
		print("1",tagg)
		for taggs in tagg:
			print("2",taggs)
			lin = taggs.get_attribute('href')
			print("3",lin)
			if "?" in lin:
				pass
			else:
				print("here")
				name = taggs.text
				print("name",name,lin)
				total = name+" ; "+lin
				groups_link.append(lin)
				data = [name,lin,members_count]
				if typee == 'groups': 
					with open ('groups.csv',   'a', encoding="utf-8", newline='') as files:
						writer = csv.writer(files)
						writer.writerow(data)
						data.clear()
				else:
					with open ('pages.csv',   'a', encoding="utf-8", newline='') as files:
						writer = csv.writer(files)
						writer.writerow(data)
						data.clear()
	user_profiles = []						
	if typee == 'groups':
		ggg = len(groups_link)
		os.remove('group_count.txt')
		a = open('group_count.txt', 'a')
		a.truncate()
		a.write(str(ggg))
		a.close()				
		for lo in groups_link[:1]:#change according how much gorups in loop
			print("lo",lo)
			# loo = lo.split("; ")[1]
			driver.get(lo+"members")
			sleep(5)
			groups_type = driver.find_element_by_class_name('x1nn3v0j').text
			sleep(1)
			if "Private" in groups_type:
				print("THIS is private group")
				try:
					driver.find_element_by_css_selector('div[aria-label="Join Group"]').click()
					sleep(3)
					dat = [lo,'Private','Joined']
					with open ('private_groups.csv',   'a', encoding="utf-8", newline='') as files:
						writer = csv.writer(files)
						writer.writerow(dat)
						dat.clear()
				except Exception as e:
					print(e)
					pass		
			else:
				boxx = driver.find_elements_by_class_name("x1jx94hy")
				try:
					for ii in boxx:
						iii = ii.find_elements_by_class_name("x14l7nz5")
						try:
							iiii = iii[0].text
							iiiii = iii[1]
							print("4",iiii)
							if "New to the group" in iiii:
								print("in")
								all_user = iiiii.find_elements_by_css_selector('div[role="listitem"]')
								count = len(all_user)
								con = 0
								while True:
									driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
									sleep(5)
									all_use = iiiii.find_elements_by_css_selector('div[role="listitem"]')
									count1 = len(all_use)
									print("cou", count1)

									if int(count1) >= int(num):
										break
									
								for user in all_use:
									users = user.find_element_by_tag_name("a").get_attribute('href')
									print("users",users)
									user_profiles.append(users)
									data1 = [users]
									with open ('users.csv',   'a', encoding="utf-8", newline='') as files:
										writer = csv.writer(files)
										writer.writerow(data1)
										data1.clear()
						except Exception as e:
							print("error",e)
							pass			
				except Exception as e:
					exc_type, exc_obj, exc_tb = sys.exc_info()
					fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
					print(exc_type, fname, exc_tb.tb_lineno)
					pass
	else:
		ggg = len(groups_link)
		os.remove('page_count.txt')
		a = open('page_count.txt', 'a')
		a.truncate()
		a.write(str(ggg))
		a.close()
		print("pages")
		for lo in groups_link[:1]:#change according how much page in loop
			print("lo",lo)	
			driver.get(lo+"/mentions")
			sleep(5)
			for i in range(0,int(scrll)):#increase number to increase users if there are
				print(i)
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				sleep(5)
			soup = BeautifulSoup(driver.page_source, 'html.parser')

			print(soup)
			sleep(2)
			profile_links = soup.find_all('a', href=lambda href: href and '/profile.php?id' in href)

			profile_urls = [link['href'] for link in profile_links]

			profile_urls = list(set(profile_urls))
			print("len", len(profile_urls))
			sleep(10)

			if len(profile_urls) > int(num):
				for url in profile_urls[:int(num)]:
				    print(url)
				    user_profiles.append(url)

				    data1 = [url]
				    with open ('users.csv',   'a', encoding="utf-8", newline='') as files:
				    	writer = csv.writer(files)
				    	writer.writerow(data1)
				    	data1.clear()
			else:    	

				for url in profile_urls:
				    print(url)
				    data1 = [url]
				    with open ('users.csv',   'a', encoding="utf-8", newline='') as files:
				    	writer = csv.writer(files)
				    	writer.writerow(data1)
				    	data1.clear()


	try:
		gaggag = len(user_profiles)
		os.remove('user_count.txt')
		a = open('user_count.txt', 'a')
		a.truncate()
		a.write(str(gaggag))
		a.close() 
		print(len(user_profiles))
		sleep(5)
		os.remove('msg.txt')
		a = open('msg.txt', 'a')
		a.truncate()
		a.write(str("0"))
		a.close()
		count = 0
		for usersss in user_profiles:
			print(usersss)
			count += 1
			user_message(usersss,count)
	except:
		print('no data here')
		pass

	driver.close()			








				

