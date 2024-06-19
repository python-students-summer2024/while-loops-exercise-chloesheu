def get_starting_number():
    while True:
        number = input("")
        if number.isnumeric() and int(number) > 0:
            return int(number)
        
def sing(num):
    loop = True
    while loop:
        print(f"{num} bottle{'s' if num > 1 else ''} of beer on the wall, {num} bottle{'s' if num > 1 else ''} of beer.")
        num -= 1
        if (num == 0):
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            loop = False
        else:
            print(f"Take one down, pass it around, {num} bottle{'s' if num > 1 else ''} of beer on the wall.")
            print("\n")