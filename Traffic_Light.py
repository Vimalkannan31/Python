import time

def Traffic_auto():
    while True:
        print("GREEN")
        time.sleep(6)
        print("YELLOW")
        time.sleep(5)
        print("RED")
        time.sleep(6)

def Traffic_manual():
    direction=input("Enter the Direction of the Traffic Signal(north,south,east,west):").upper()
    colour=input("Enter the colour of the "+direction+"(green,yellow,red):").upper()
    print("The Traffic light for the",direction,"is",colour)


def main():
    mode=input("Enter the mode of the Traffic Light (auto or manual):").lower()
    if mode == 'auto':
        Traffic_auto()
    elif mode == 'manual':
        Traffic_manual()
    else:
        print("Enter the Valid Input(enter auto or manual...)")
        main()

if __name__ == '__main__':
    main()
    