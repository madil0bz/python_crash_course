#Write a series of 10 conditional tests to practice

#1. Check if a number is even or odd
number = 10
if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f'The number {number} is odd')

#2. See if someone is old enough to vote
age = 45
if age >= 18:
    print(f'You are {age} so you are old enough to vote!')
else:
    print(f'You are {age} so you are not old enough to vote!')

#3. Test if a string contains a certain word
car = "bmw"
print(car == "Bmw")
print(car.title() == "Bmw")

#4. Compare two numbers to find which is larger
num_1 = 56
num_2 = 17

if num_1 > num_2:
    print(f'The first number: {num_1}, is greater than the second number: {num_2}')
else:
    print(f'The second number: {num_2}, is greater than the first number: {num_1}')

#5. Check if a list is empty or not
jokes = []
if len(jokes) == 0:
    print(f'The list is empty')

#6. See if a password is long enough
password = '1234!'
pass_length = 10

if len(password) >= 10:
    print('You are good to log in')
else:
    print(f'Your password is too short')

#7. Determine if a temperature is above freezing
freezing_temp = 32
my_temp = 54

if my_temp > 32:
    print('The temperature is above freezing')
else:
    print('The temperature is freezing')

#8. Check if today is a weekend
today = 'Saturday'
weekend = ["Saturday", "Sunday"]

if today in weekend:
    print(f"Today is {today}, so it is a weekend!")
else:
    print(f"Today is {today}, so it is not a weekend!")

#9. Check if someone is able to get a loan
age_loan = 20
credit_score = 709

credit_min = 620
age_min = 18

if age_loan >= age_min and credit_score >= credit_min:
    print(f"You have been approved for a loan.")
else:
    print("Im sorry but you are unable to apply for this loan.")

#10. check if a file name ends with txt
filename = "document.txt"

if filename.endswith(".txt"):
    print("This is a text file.")
else:
    print("This is not a text file.")
