# 1. Digit and Character Analyzer
# Take a string containing letters, digits, spaces, and special characters.

# Using a for loop:

# Count uppercase letters.
# Count lowercase letters.
# Count digits.
# Count spaces.
# Count special characters.
# Print which category has the highest count.
# If two or more categories have the same highest count, print "Tie".

Str=input("Enter a string: ")
ct_up=0
ct_lw=0
ct_dig=0
ct_spac=0
ct_spe=0

for i in Str:
    if(i>='A' and i<='Z'):
        ct_up+=1
    elif(i>='a' and i<='z'):
        ct_lw+=1
    elif(i>='0' and i<='9'):
        ct_dig+=1
    elif(i==" "):
        ct_spac+=1
    else:
        ct_spe+=1
if(ct_up>ct_lw and ct_up>ct_dig and ct_up>ct_spac and ct_up>ct_spe):
    print("UpperCase characters have the highest count")
elif(ct_lw>ct_up and ct_lw>ct_dig and ct_lw>ct_spac and ct_lw>ct_spe):
    print("LowerCase characters have the highest count")
elif(ct_dig>ct_lw and ct_dig>ct_up and ct_dig>ct_spac and ct_dig>ct_spe):
    print("digit characters have the highest count")
elif(ct_spac>ct_lw and ct_spac>ct_up and ct_spac>ct_dig and ct_spac>ct_spe):
    print("space characters have the highest count")
elif(ct_spe>ct_lw and ct_spe>ct_up and ct_spe>ct_dig and ct_spe>ct_spac):
    print("speical characters have the highest count")
else:
    print("Tie")




# 2. Student Performance Analyzer
# Take marks of 10 students using a for loop.

# For each student:

# Print "Fail" if marks are below 35.
# Print "Pass" for 35–49.
# Print "Good" for 50–74.
# Print "Excellent" for 75–100.
# At the end, print the number of students in each category.



ct_pass=0
ct_good=0
ct_ex=0
ct_fail=0
for i in range(10):
    marks=int(input("Enter marks: "))
    if(marks>=75):
        print("Excellent")
        ct_ex+=1
    elif(marks>=50):
        print("Good")
        ct_good+=1
    elif(marks>=35):
        print("Pass")
        ct_pass+=1
    else:
        print("Fail")
        ct_fail+=1

print("Excellent students are:",ct_ex)
print("Good students are:",ct_good)
print("Pass students are:",ct_pass)
print("Fail students are:",ct_fail)