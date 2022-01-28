
import time


class Computer():

    def __init__(self, status_Computer= "close", volume_Computer=10, directory_list=[], brand_Computer="apple",
                memory_Computer=512, status_Player="close"):
        self.status_Computer = status_Computer
        self.volume_Computer = volume_Computer
        self.brand_Computer = brand_Computer
        self.memory_Computer = memory_Computer
        self.directory_list = directory_list
        self.status_Player = status_Player

    def open(self):
        if (self.status_Computer == "close"):
            print("Computer is starting...")
            time.sleep(3)
            print("Computer is opened...")
            self.status_Computer = "open"
        else:
            print("Computer has already opened")

    def close(self):
        if (self.status_Computer == "open"):
            print("Computer is closing...")
            time.sleep(3)
            self.status_Computer = "close"

    def volume(self):
        command = input("for your command press, increase '>', decrease '<'")
        while True:
            if (self.volume_Computer >= 0):
                if (command == ">"):
                    print("volume is increasing...")
                    time.sleep(1)
                    self.volume_Computer += 1
                    print("volume:", self.volume_Computer)
                elif (command == "<"):
                    print("volume is decreasing...")
                    time.sleep(1)
                    self.volume_Computer -= 1
                    print("volume:", self.volume_Computer)

                else:
                    print("your command is declined")
            break
    def directory(self):
        command = input("for your command press, upload 'up',delete 'del'")
        file = input("write your file name")
        if (command == "up"):
            print("your file {} is uploading...".format(file))
            self.directory_list.append(file)
        elif (command == "down"):
            print("file{} that you selected is deleting...".format(file))
            self.directory_list.pop(-1)
        else:
            print("your command is declined")

    def information(self):
        print("status_Computer:{}\nvolume_Computer:{}\ndirectory_list:{}\nbrand_computer:{}\nmemory_Computer:{}\n".format(
            self.status_Computer, self.volume_Computer, self.directory_list, self.brand_Computer, self.memory_Computer))

    def player(self):
        command = input("for your command press , start '>', resume '=', stop '#'")
        if (command == ">"):
            print("your player is started")
            self.status_Player = "start"
        elif (command == "="):
            print(" your player is resumed")
            self.status_Player = "resume"
        elif (command == "#"):
            print("your player is stopped")
            self.status_Player = "stop"

    def camera(self):
        function = input("choose function; camera:c and video:v",)
        if (function == "c"):
            print("photo is taking")
            time.sleep(1)
        elif (function == "v"):
            print("video is taking")


computer = Computer()

print("""
*********************
    COMPUTER
    FUNCTIONS
1.OPEN
2.CLOSED
3.VOLUME
4.DIRECTORY DOWNLOAD/DELETE
5.INFORMATION   
6.PLAYER
7.CAMERA
**********************

""")

while True:
    function = int(input("choose the function which you want the computer makes:"))
    if (function == 1):
        computer.open()
    elif ( function == 2):
        computer.close()
    elif (function == 3):
        computer.volume()
    elif (function == 4):
        computer.directory()
    elif (function == 5 ):
        computer.information()
    elif (function == 6 ):
        computer.player()
    elif (function == 7):
        computer.camera()
    else:
        print("your request is denied")




