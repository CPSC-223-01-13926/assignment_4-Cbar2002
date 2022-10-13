from weather import *

myfile = "weather.dat"

mychoice = 0

while(True):
    print("         *** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print("1. Set data FileName")
    print("2. Add Weather Data")
    print("3. Print Daily Report")
    print("4. Print Historical Report")
    print("9. Exit the Program")

    mychoice = int(input("Enter Menu choice "))
    print()

    if mychoice ==  1:
        myfile = input("Enter Data Filename: ")
        weather = read_data(myfile)
   
    elif mychoice ==2:
        dt = input("Enter date: ")
        tm = input("Enter time: ")
        t = int(input("Enter Temperature:"))
        h = int(input("Enter humidity:"))
        r = float(input("Enter the Rainfall: "))
       
        weather[dt+tm] = {'t':t,'h' :h, 'r' :r}
        write_data(weather , myfile)
    
    
    elif mychoice == 3:
        d =input("Enter date: ")
    display = report_daily(weather , d)
    print(display)

    