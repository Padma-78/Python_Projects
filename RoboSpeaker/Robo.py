import os

if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1")
    while True:
    x = input("What do you want to speak : ")
    if x == "q":
        os.system("Bye Bye Friends...")
        break
    command = f"say {x}"
    os.system(command)