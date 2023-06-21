#Question 1. This is print the final grade of the user.
hwWeight = 0.40
hwGrade = float(input('What is your homework grade? '))
examWeight = 0.50
examGrade = float(input('What is your exam grade? '))
discussionWeight = 0.10
discussionGrade = float(input('What is your discussion grade? '))
total_Grade = (hwWeight*hwGrade)+(examWeight*examGrade)+(discussionGrade*discussionWeight)
print('Your total grade is: ' + str(total_Grade) +'\n\n')


#Question 4. This is to calculate a user's GPA and tell if the student will graduate with honours
GPA = 0.00
def calculateGPA():
    global GPA
    overall_score = float(input('What did you score out of 100? '))
    if overall_score > 100:
       print('You need to input a value between 0 and 100.')
       print('Try again')
       calculateGPA()
    elif overall_score <= 100 and overall_score>=80:
        GPA=4.00
        print('Your GPA is '+ str(GPA))
    elif overall_score<=79 and overall_score>=75:
        GPA=3.50
        print('Your GPA is '+ str(GPA))
    elif overall_score <= 74 and overall_score >= 70:
        GPA = 3.00
        print('Your GPA is '+ str(GPA))
    elif overall_score<=69 and overall_score>=65:
        GPA = 2.50
        print('Your GPA is '+ str(GPA))
    elif overall_score<= 64 and overall_score>=60:
        GPA = 2.00
        print('Your GPA is '+ str(GPA))
    elif overall_score <= 59 and overall_score >= 55:
        GPA = 1.50
        print('Your GPA is '+ str(GPA))
    elif overall_score <= 54 and overall_score >= 50:
        GPA = 1.00
        print('Your GPA is '+ str(GPA))
    else:
        print('You failed!')
    return GPA

def getHonours():
    calculateGPA()
    print(GPA)
    if GPA<=4.00 and GPA>=3.85:
        print('You get Summa Cum Laude!\n\n')
    elif GPA<=3.84 and GPA>=3.70:
        print('You get Magna Cum Laude!\n\n')
    elif GPA<=3.69 and GPA>=3.50:
        print('You get Cum Laude!\n\n')
    else:
        print('No honours\n\n')

Honours_Obtained=getHonours()


#Question 5. This calculates the area of a circle with any radius given
import math
radius = float(input('What is the radius of the circle? '))
r = radius
Area_of_Circle= math.pi*r*r
Area_of_Circle= '{:.2f}'.format(Area_of_Circle)
print('The area of your circle is: '+ str(Area_of_Circle) + '\n\n')

#Question 3. This to calculate the amount after t years
principal= 12000
rate= 8/100
n=2
time= int(input('How many years will the amount be compounded for? '))
t=time
r=rate
p=principal
Amount = float((p*(1+r/n))**(n*t))
Amount = "{:.2f}".format(Amount)
print('The final amount after '+str(t)+' years is '+str(Amount) + '\n\n')

#Question 6. This is about a function that determines whether 3 differents lengths can form a triangle.

def is_triangle(side1,side2, side3) :
    if (side1+side2) > side3 and (side2+side3) > side1 and (side1+side3) > side2 :
        possibility= False
        print(str(possibility) + ',No triangle forms')
        return possibility
    else :
        possibility = True
        print(str(possibility) + ', Triangle can be formed')
        return possibility

Default_Triangle = is_triangle(25,12,13)

length1 = int(input('What is the length of the first side? '))
length2 = int(input('What is the length of the second side? '))
length3 = int(input('What is the length of the third side? '))

Formation_of_your_triangle = is_triangle(length1,length2,length3)