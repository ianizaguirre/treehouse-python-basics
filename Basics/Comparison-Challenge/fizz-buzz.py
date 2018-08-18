name = input("Please enter your name: ")
number = int(input("Please enter a number: "))

by_three = (number % 3 == 0)
by_five = (number % 5 == 0)
by_both = (by_three and by_five)

grab_name = print("Hey {}!".format(name))
grab_number = print("The number {}...".format(number))

if by_both:
  deduce_number_type = print("is a FizzBuzz number.")

elif by_three:
  deduce_number_type = print("is a Fizz number.")

elif by_five:
  deduce_number_type = print("is a Buzz number")

else:
  deduce_number_type = print("is nether a fizzy or a buzzy number.")

# My Program
grab_name
grab_number
deduce_number_type