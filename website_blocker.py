import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"/Macintosh HD/private/etc/hosts"
redirect = "10.0.0.131"
website_list = ["www.buzzfeed.com","buzzfeed.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+ "\n")
    else:
        with open(hosts_temp,'r+') as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("Fun hours!")
    time.sleep(5) #don't run loop for 5 seconds
