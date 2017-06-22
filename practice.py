import time
import datetime
import glob

temperatures = [10,-20,-280,100]

def celcius_to_fahrenheit(celcius):
    if celcius > -273.3:
        fahrenheit = celcius * 9/5 + 32
        return fahrenheit
    else:
        return "That temperature doesn't make sense?!"

for t in temperatures:
    print(celcius_to_fahrenheit(t))

def file_open():
    file = open('prac.txt', 'r')
    content = file.read()
    print(content)
    file.close()

file_open()

def fizz_buzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

fizz_buzz()


temperatures = [10,-20,-280,100]

def write_temps(temperatures):
    with open('temp.text','w') as file: #the 'as file' is a variable, called in the end with .write
        for c in temperatures:
            if c > -273.15:
                f = c * 9/5 + 32
                file.write(str(f)+"\n")

write_temps(temperatures)

filenames = glob.glob('*.txt')

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,'r') as f:
            file.write(f.read()+"\n")
