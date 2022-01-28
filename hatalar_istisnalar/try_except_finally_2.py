# write the functions about the number which is even
#if number is even,use return function
# if not,the function use raise and valueError
# Make a list about number, make it write the even numbers on your window

def even_number():
    number = (input("write your number:"))
    number = int(number)
    for number in range(2,number+1):
        list1 = []
        if( number % 2 == 0):
            list1.append(number)
            print("list1:",list1)
        else:
            continue

while True:
    even_number()





