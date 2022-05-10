# using string concatenation
name = "Dillip"

print("The most active programmer is " + name)
print("The highly enthusiastic programmer is {}".format(name))
print(f"The problem solver is {name}")

# inputing or taking input from the user and printing them accordingly

username = input("enter name:")
password = input("enter password :")
madlib = (f"your username is : {username} \n your password is {password} \n"
          "Don't share your password with anyone ! \n Welcome {username} to Python world")
print(madlib)
