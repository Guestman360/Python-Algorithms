#Homework Helper

weather = open("weather.txt","r")
newText = open("newText.txt","w")
counter_weather = 0
counter_whether = 0

for line in weather:
    rep = line
    if rep.find("Weather" or "weather"):
        print(rep)
        rep = rep.replace("Weather","Whether")
        print(rep)
        rep = rep.replace("weather","whether")
        print(rep)
        counter_weather += 1
    if rep.find("Whether" or "whether"):
        #print(rep)
        rep = rep.replace("Whether","Weather")
        rep = rep.replace("whether","weather")
        counter_whether += 1

print("The word \"whether\" appears {} times and the word \"weather\" appears {} times".format(counter_whether,counter_weather))
weather.close()
newText.close()
