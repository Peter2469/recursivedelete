import shutil

numbernow = startingnumber

name = input("What is the folders/files name you want to delete?\n")
amount = input("\nHow many folders/files with the same name but differentiated by numbers exist?\n")
startingnumber = input("\nWhat is the first number?\n")


while True:
    shutil.rmtree(f"{name}{amount}")
    print(f"Deleted {name}")
    numbernow = numbernow + 1
