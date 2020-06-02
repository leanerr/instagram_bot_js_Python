# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

# f= open("ps","r")
# ps = f.readline()
# f.close()

# f= open("un","r")
# un = f.readline()
# f.close()

ps = "password"
un = "username"

driver = webdriver.Chrome(executable_path='C:/Users/negin/Desktop/instaBot/chromedriver.exe')

  


driver.get("https://www.instagram.com/accounts/emailsignup/")
sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[2]/p/a").click()

sleep(1)

if (driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(un)):
    print("login error!")
    exit()
sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(ps)
sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
sleep(3)
if driver.find_elements_by_id("slfErrorAlert"):
    print("username ya password eshtebah ast")
    exit()
else:
    print("login was successful")

driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()      
driver.get("https://www.instagram.com/p/B_c1sYQgdmX/")
sleep(2)

# post = str(driver.find_elements_by_tag_name("li")[0].text)
# flw = str(driver.find_elements_by_tag_name("li")[1].text)
# fli = str(driver.find_elements_by_tag_name("li")[2].text)

# print(f"tedade post ha {post} \n {flw} \n {fli}")

driver.execute_script("document.getElementsByClassName('wpO6b')[0].click()")
sleep(2)
driver.find_elements_by_tag_name("textarea")[0].click()
sleep(1)
comment = input("...")
driver.find_elements_by_tag_name("textarea")[0].send_keys(comment)
sleep(3)
driver.execute_script('for (i = 0 ; i<document.getElementsByTagName("button").length;i++){if(document.getElementsByTagName("button")[i].textContent == "Post") {m = i;break;}} document.getElementsByTagName("button")[m].click()')
sleep(2)
driver.execute_script('for (i = 0 ; i<document.getElementsByTagName("button").length;i++){if(document.getElementsByTagName("button")[i].textContent == "Follow") {m = i;break;}} document.getElementsByTagName("button")[m].click()')


# var xx = document.querySelectorAll('button.sqdOP.yWX7d.y3zKF');
# for (i=0;i<xx.length;i++){
#    if(document.querySelectorAll('button.sqdOP.yWX7d.y3zKF')[i].textContent == 'Post'); m =i
#    break;         
# }document.querySelectorAll('button.sqdOP.yWX7d.y3zKF')[m].click()


