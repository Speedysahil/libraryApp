import time
from playsound import playsound
def getdate():
  import datetime
  return datetime.datetime.now()


print("Hello this is a python Healthy programmer App")

my_sound =  'C:\\Users\\Amang\\Downloads\\water.mp3'
water_count = 18

while water_count > 0:
    print("Drink water")
    playsound(my_sound)

    if input("Enter done if drink it\n") == "done":
        f = open("water.txt","a")
        a = f.write("you drink water at "+ "["+str(getdate()) +"]")
        f.close()
        water_count -= 1
    time.sleep(5)




