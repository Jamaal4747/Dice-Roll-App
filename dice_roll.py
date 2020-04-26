from helpers import dice


quit_app = ""
while quit_app is not "q": 
    print(f"The sum of the 2 die is: {dice()}")
    quit_app = input('Type any key to continue. Type q to quit. ')