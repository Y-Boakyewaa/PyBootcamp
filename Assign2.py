#This is to print a multiplication table
number = int(input('This is a Multiplication table for: '))
for times in range(1,13):
    print(str(number) + ' * ' + str(times) + ' = ' + str(number*times))

# This to find the length of a string given
def customlen():
    string = str(input('Enter anything: '))
    length_of_string = 'The lenghth of the string above is: ' + str(len(string))
    print(length_of_string)
len_string= customlen()

# This is a guessing game
magic_number = 58
guess = int(input('Enter your guess: '))
if guess > 100 :
    raise ValueError
else :
    if guess > magic_number:
        print('Guess is high')
    elif guess < magic_number:
        print('Guess is low')
    else:
        print('You are correct!!')

# This to check if a letter is a vowel
def is_vowel():
    letter= str(input('Enter a character: '))
    length_of_letter = len(letter)
    if length_of_letter != 1:
        print('''The length of letter must be 1
        try again!
        ''')
        is_vowel()
    else:
        if letter in "AaEeIiOoUu":
            return True
        else:
            return False

if_vowel= is_vowel()
print(if_vowel)


# This is to find the sum of numbers less than and equal to number given
your_num = int(input('Your number: '))
sum = 0
while 0 <= your_num:
    sum = sum + your_num
    your_num = your_num - 1
total_sum = 'The sum of numbers less than and equal to the number given is {}'
print(total_sum.format(sum))

# This is for comparison
common = 0
uncommon = 0
def compareStrings():
    garlands = str(input('Enter letters to represent flowers in your garland: '))
    flowers = str(input('Enter letters to represent flowers in general: '))
    global common
    global uncommon
    if len(garlands) < 1 or len(flowers) > 50:
        print('Error, try again!')
        compareStrings()
    else:
        for a in garlands:
            for b in flowers:
                if a == b:
                    common += 1
                else:
                    uncommon += 1
    print('common_flowers= ' + str(common))
    print('uncommon_flowers= ' + str(uncommon))


flowers_comparison = compareStrings()



score=0
def inputScore():
    percent = float(input('What did you score out of 100? '))
    if percent > 100:
        print('You need to input a value between 0 and 100.')
        print('Try again')
        inputScore()
    else:
        return percent
def calculateGPA():
    # global score
    score = inputScore()
    if 80 <= score <= 100:
        return 'A+', 4.00
    elif 75 <= score <= 79:
        return 'B+', 3.50
    elif 70 <= score <= 74:
        return 'B', 3.00
    elif 65 <= score <= 69:
        return 'C+', 2.50
    elif 60 <= score <= 64:
        return 'C', 2.00
    elif 55 <= score <= 59:
        return 'D+', 1.50
    elif 50 <= score <= 54:
        return 'E', 1.00
    elif 0 <= score <= 49:
        return 0.00
    else:
        return "Invalid score"



def getHonours():
    gpa = calculateGPA()[1]

    if 3.85 <= gpa <= 4.00:
        return "Summa Cum Laude"
    elif 3.70 <= gpa <= 3.84:
        return "Magna Cum Laude"
    elif 3.50 <= gpa <= 3.69:
        return "Cum Laude"
    else:
        return "No honours"
honours_obtained=getHonours()
print(honours_obtained)

mark = 0
def mark_allocation():
    if 80 <= mark <= 100:
        return 'A+', 4.00
    elif 75 <= mark <= 79:
        return 'B+', 3.50
    elif 70 <= mark <= 74:
        return 'B', 3.00
    elif 65 <= mark <= 69:
        return 'C+', 2.50
    elif 60 <= mark <= 64:
        return 'C', 2.00
    elif 55 <= mark <= 59:
        return 'D+', 1.50
    elif 50 <= mark <= 54:
        return 'E', 1.00
    elif 0 <= mark <= 49:
        return 'No grade letter', 0.00
    else:
        return 'Invalid'


def individual_courses():
    marks = []
    num_courses = int(input('How many courses would you like to enter information for?'))
    for i in range(num_courses):
        global mark
        mark = float(input('What was your score out of hundred? '))
        print(mark_allocation())

individual_courses()

