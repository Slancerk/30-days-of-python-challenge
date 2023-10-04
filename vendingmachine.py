#basically we have to create a vending machine to print no. of chocolates for the user ,also take care of the number of chocolates the machine have .
#usr_input =3
#output= 
#chocolate
#chocolate
#chocolate


cho=10  #ch== no of chocolates the machine has 

user_inp=int(input("enter number of chocolates you want"))


if user_inp>cho:
    print('out of supply')

elif user_inp<cho:
    cho=cho-user_inp
    print('remaining chocolates= ', cho)
    i=1
    while i<=user_inp:
        print("chocolate ")
        i+=1






