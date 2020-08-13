x = 0
SumGrade = 0
SumCredit = 0
Count = int(input("Enter Number Of Subject: "))
while x < Count:
    Subject = input("Enter Subject: ")
    Credit = int(input("Enter Credit: "))
    SumCredit = SumCredit + Credit
    Grade = float(input("Enter Grade: "))
    SumGrade = SumGrade + (Grade * Credit)
    x +=1
    Formula = SumGrade  / SumCredit

def Cal_Value(Formula):
  "This function calculate CGPA by input user"
  if Formula >= 3.67 and Formula <=4.00: return "Dean List"
  elif Formula >= 2.75 and Formula <=3.66: return "Pass"
  elif Formula >= 2.00 and Formula <=2.74: return "Conditional Pass"
  else : return "Fail"

print("CGPA is {:0.2f} and Result is {}. Total Credit is {}".format(Formula,Cal_Value(Formula),SumCredit))
