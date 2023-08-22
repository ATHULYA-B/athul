def get_season(month,day):
    if(month==3 and day>=20)or (month==4)or (month==5)or (month==6 and day<=20):
        return "Spring"
    elif(month==6 and day>=21)or (month==7)or (month==8 and day>=22)or (month==9 and day<=21):
        return "Summer"
    elif(month==9 and day>=21)or (month==10)or (month==12 and day<20):
        return "Fall"
    else:
        return "Winter"
while True:
    month=int(input("enter the month as an integer"))
    day=int(input("enter the day"))
    if 1<= month<=12 and 1<=day <=31:
      season=season(month,day)
      print(f"the season for {month}/{day} is {season}")
    else:
        print("invalid input")                                                                                                                                                                 