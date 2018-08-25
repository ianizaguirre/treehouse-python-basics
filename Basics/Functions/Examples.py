# Example 1
def yell(text):
  text = text.upper()
  number_of_characters = len(text)
  result = text + "!" * (number_of_characters // 2)
  print(result)


# Example 2 / "Split the Bill"
import math

def split_check(total, number_of_people):
  cost_per_person = math.ceil(total / number_of_people)
  return cost_per_person

# total_due returns a string so we want to coherce that into a number which is why we wrap it in a float()
total_due = float(input("What is the total? "))
number_of_people = int(input("How many people? "))

amount_due = split_check(total_due, number_of_people)

print("Each person owes ${}".format(amount_due))
