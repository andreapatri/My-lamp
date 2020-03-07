import datetime
import os

print(str(datetime.datetime.now().time()))
  
while (1==1):
    rn = str(datetime.datetime.now().time())
    if rn >= "16:22:00.000000" and rn <= "16:22:00.000200" :
        print ("ya!!")
        print(rn)
        myCmd = 'cd Downloads/'
        os.system(myCmd)
        myCmd = 'arduino-cli board list'
        os.system(myCmd)
        myCmd = 'arduino-cli compile --fqbn arduino:avr:uno ~/Downloads/Myfirst'
        os.system(myCmd)
        myCmd = 'arduino-cli upload -p /dev/cu.usbmodem14201 --fqbn arduino:avr:uno ~/Downloads/Myfirst'
        os.system(myCmd)
        print("doneeeee")

##    if rn >= "16:22:04.000000" and rn <= "16:22:04.000100" :
##        print ("ya! pues!")
##        myCmd = 'cd Downloads/'
##        os.system(myCmd)
##        myCmd = 'arduino-cli board list'
##        os.system(myCmd)
##        myCmd = 'arduino-cli compile --fqbn arduino:avr:uno ~/Downloads/Myfirst'
##        os.system(myCmd)
##        myCmd = 'arduino-cli upload -p /dev/cu.usbmodem14201 --fqbn arduino:avr:uno ~/Downloads/Myfirst'
##        os.system(myCmd)
##


