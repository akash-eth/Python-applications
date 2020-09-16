# To-Do Application

import time

def main():
    print("!! Starting the Apllication please hold tight !!")
    while True:
        command = input("$ ").lower()
        if (command == "quit"):
            time.sleep(2)
            print("!! Exiting out the apllication !!")
            break
        else:
            continue


if __name__ == '__main__':
    main()