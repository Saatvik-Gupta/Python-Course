#-----12hrs format to 24 hrs format

time=input("Enter the timer in 24-hours format:")

if(time[:2]=="12" and time[-2:]=="PM"):
    print(time[:-2])  #12:00:00 PM to 12:59:59 PM
elif(time[:2]=="12" and time[-2:]=="AM"):
    print("00"+time[2:-2])
elif(time[-2:]=="AM"):
    print(time[:-2])
else:
    print(str(int(time[:2])+12)+time[2:-2])