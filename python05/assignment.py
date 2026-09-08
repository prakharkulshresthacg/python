#Part 3 - Practical Programs


#Task 1 - Basic Arithmetic
#Create two variables containing integers and perform every arithmetic operation.

a = 17
b = 5

print("Addition       :", a + b)    #22
print("Subtraction    :", a - b)    #12
print("Multiplication :", a * b)    #85
print("Division       :", a / b)    #3.4
print("Floor Division :", a // b)   #3
print("Modulus        :", a % b)    #2
print("Exponentiation :", a ** b)   #1419857

#Note: do int ke beech / hamesha float deta hai (3.4), baaki saare operations int hi rehte hai.


#Task 2 - Integer and Float
#Create one integer and one float, perform all operations, show result and its type.

num_int = 7
num_float = 2.5

print(num_int + num_float,  type(num_int + num_float))    #9.5 <class 'float'>
print(num_int - num_float,  type(num_int - num_float))    #4.5 
print(num_int * num_float,  type(num_int * num_float))    #17.5 
print(num_int / num_float,  type(num_int / num_float))    #2.8 
print(num_int // num_float, type(num_int // num_float))   #2.0 
print(num_int % num_float,  type(num_int % num_float))    #2.0 
print(num_int ** num_float, type(num_int ** num_float))   #129.64181424216494 

#Explanation: jab int aur float mil ke operation karte hai to result hamesha float hota hai.
#Isiliye // bhi 2 nahi balki 2.0 deta hai - value poori hai magar type float hai.
#Python chhote type ko bade type mein badal deta hai taaki precision na kho jaye.


#Task 3 - Student Marks
#Create variables for marks of three subjects, calculate total and average.

maths_marks   = 78
science_marks = 85
english_marks = 92

total_marks = maths_marks + science_marks + english_marks
average_marks = total_marks / 3

print("Total Marks  :", total_marks)     #255
print("Average Marks:", average_marks)   #85.0

#Note: average float aaya kyunki / ka result hamesha float hota hai.


#Task 4 - Product Calculation
#Create variables for product price and quantity, calculate the total price.

product_price = 45.50
quantity = 3

total_price = product_price * quantity

print("Total Price:", total_price)   #136.5


#Task 5 - Even or Odd
#Use the modulus operator to check whether a number is even or odd.

number = 27

print("Number    :", number)          #27
print("Remainder :", number % 2)      #1

#Rule: number % 2 agar 0 aaye to number Even hai, aur 1 aaye to Odd hai.
#Yahan remainder 1 aaya isliye 27 Odd hai.

even_number = 30
print("Number    :", even_number)     #30
print("Remainder :", even_number % 2) #0 -> Even


#Task 6 - Division and Floor Division
#Perform normal division and floor division, first with positive then negative numbers.

x = 17
y = 5

print("Positive ->", x / y)    #3.4
print("Positive ->", x // y)   #3

x = -17
y = 5

print("Negative ->", x / y)    #-3.4
print("Negative ->", x // y)   #-4

#Observation: positive mein 3.4 se 3 mila (neeche wala number),
#magar negative mein -3.4 se -3 nahi balki -4 mila.
#Kyunki floor division hamesha chhote number ki taraf jaata hai, zero ki taraf nahi.


#Task 7 - Negative Number Operations
#Create two negative numbers and perform all operations.

p = -17
q = -5

print("Addition       :", p + q)    #-22
print("Subtraction    :", p - q)    #-12
print("Multiplication :", p * q)    #85
print("Division       :", p / q)    #3.4
print("Floor Division :", p // q)   #3
print("Modulus        :", p % q)    #-2

#Observation: do negative multiply ya divide karne par answer positive ho jaata hai.
#Modulus ka answer -2 aaya yaani negative, kyunki remainder ka sign divisor jaisa hota hai.


#Task 8 - Subtraction Edge Cases
#Display the expression and its result for all four sign combinations.

print("10 - 4     =", 10 - 4)         #6
print("10 - (-4)  =", 10 - (-4))      #14
print("-10 - 4    =", -10 - 4)        #-14
print("-10 - (-4) =", -10 - (-4))     #-6

#Explanation: minus ke baad negative number aaye to wo plus ban jaata hai,
#isliye 10 - (-4) ka matlab 10 + 4 hai.


#Task 9 - Floor Division Edge Cases
#Test floor division with all four sign combinations.

print("17 // 5    =", 17 // 5)        #3
print("-17 // 5   =", -17 // 5)       #-4
print("17 // -5   =", 17 // -5)       #-4
print("-17 // -5  =", -17 // -5)      #3

#Why negative results are different from just removing the decimal part:
#Asli answers ye hai -> 3.4, -3.4, -3.4, 3.4
#Agar hum sirf decimal hata dete to -3.4 ka answer -3 aata,
#magar Python ne -4 diya. Iska reason ye hai ki floor division "floor" leta hai,
#matlab number line par LEFT side wala nearest integer.
#-3.4 ke left mein -4 hai (kyunki -4 < -3.4), isliye answer -4 hai.
#Positive side par left wala number chhota hota hai to 3.4 -> 3 aata hai,
#aur wahi decimal hatane jaisa dikhta hai, isliye positive mein farak nahi dikhta.


#Task 10 - Modulus Edge Cases
#Test modulus with all four sign combinations and observe the sign of the remainder.

print("17 % 5    =", 17 % 5)          #2
print("-17 % 5   =", -17 % 5)         #3
print("17 % -5   =", 17 % -5)         #-3
print("-17 % -5  =", -17 % -5)        #-2

#Observation: remainder ka sign hamesha DIVISOR (right wala number) jaisa hota hai.
#5 positive tha to 2 aur 3 positive mile, -5 negative tha to -3 aur -2 negative mile.
#Reason: Python ka formula hai  a = (a // b) * b + (a % b)
#Jaise -17 % 5 ke liye -> (-17 // 5) = -4, phir (-4 * 5) = -20,
#aur -17 tak pahunchne ke liye +3 chahiye, isliye remainder 3 aaya.


#Part 5 - Boolean Arithmetic


#Task 13 - Arithmetic operations using True and False
#Perform every arithmetic operation on booleans, display results and check type().

t = True
f = False

print("Addition       :", t + f, type(t + f))       #1 <class 'int'>
print("Addition       :", t + t, type(t + t))       #2 <class 'int'>
print("Subtraction    :", t - f, type(t - f))       #1 <class 'int'>
print("Subtraction    :", f - t, type(f - t))       #-1 <class 'int'>
print("Multiplication :", t * f, type(t * f))       #0 <class 'int'>
print("Multiplication :", t * t, type(t * t))       #1 <class 'int'>
print("Division       :", t / t, type(t / t))       #1.0 <class 'float'>
print("Division       :", f / t, type(f / t))       #0.0 <class 'float'>
print("Floor Division :", t // t, type(t // t))     #1 <class 'int'>
print("Floor Division :", f // t, type(f // t))     #0 <class 'int'>
print("Modulus        :", t % t, type(t % t))       #0 <class 'int'>
print("Modulus        :", f % t, type(f % t))       #0 <class 'int'>
print("Exponentiation :", t ** t, type(t ** t))     #1 <class 'int'>
print("Exponentiation :", t ** f, type(t ** f))     #1 <class 'int'>
print("Exponentiation :", f ** t, type(f ** t))     #0 <class 'int'>
print("Exponentiation :", f ** f, type(f ** f))     #1 <class 'int'>

#Important: False ko divisor mat banao, wo zero hai isliye error aayega.
#print(t / f)    #ZeroDivisionError: division by zero
#print(t // f)   #ZeroDivisionError: division by zero
#print(t % f)    #ZeroDivisionError: division by zero

#Explanation: Python mein bool asal mein int ka hi ek chhota version hai.
#Jab bhi True/False ko arithmetic mein use karte hai to True = 1 aur False = 0 ban jaata hai.

print(int(True))    #1
print(int(False))   #0

#Type observation: saare results ka type <class 'int'> aaya, <class 'bool'> nahi.
#Sirf / wale results float aaye, kyunki division hamesha float deta hai.
#Matlab bool arithmetic mein jaate hi apni bool pehchaan kho deta hai aur number ban jaata hai.

#Note: t ** f yaani True ** False ka answer 1 hai aur f ** f yaani False ** False ka bhi 1 hai,
#kyunki kisi bhi number ki power 0 ho to answer hamesha 1 hota hai (0 ** 0 bhi Python mein 1 hai).


#Task 14 - Boolean with numbers
#Run these expressions and explain the results.

print("True + 5   =", True + 5)      #6
print("False + 5  =", False + 5)     #5
print("True * 10  =", True * 10)     #10
print("False * 10 =", False * 10)    #0
print("True - 5   =", True - 5)      #-4
print("False - 5  =", False - 5)     #-5

#Explanation ek ek karke:
#True + 5   -> True 1 ban gaya, to 1 + 5 = 6
#False + 5  -> False 0 ban gaya, to 0 + 5 = 5 (value same rehti hai)
#True * 10  -> 1 * 10 = 10 (number waisa ka waisa aata hai)
#False * 10 -> 0 * 10 = 0 (kuch bhi ho, answer 0 hi aayega)
#True - 5   -> 1 - 5 = -4 (chhote mein se bada ghata to answer negative)
#False - 5  -> 0 - 5 = -5

#Main point: True aur False sirf dikhne mein words hai, arithmetic mein wo 1 aur 0 hai.
#Isiliye True/False ko seedha add, multiply, subtract kiya ja sakta hai bina error ke.


#Part 6 - String Operations


#Task 15 - String concatenation using +
#Create two string variables and join them.

first_name = "Prakhar"
last_name = "Kulshrestha"

full_name = first_name + " " + last_name

print("Full Name:", full_name)   #Prakhar Kulshrestha

#Note: + ne dono strings ko jod diya, jise concatenation kehte hai.
#Beech mein " " (space) isliye lagaya kyunki + apne aap space nahi deta,
#warna "PrakharKulshrestha" chipka hua aata.


#Task 16 - String repetition using *
#Repeat a string multiple times, then try multiplying it by a float.

word = "Python "

print(word * 3)     #Python Python Python

#Ab isko float se multiply karke dekhte hai:
#print(word * 3.0)   #TypeError: can't multiply sequence by non-int of type 'float'

#Explanation: string ko * se repeat karna hai to count POORA number hona chahiye.
#3.0 float hai, aur Python string ko "3.0 baar" repeat nahi kar sakta,
#kyunki aadhi string ka koi matlab nahi banta. Isliye TypeError aata hai.
#3 (int) chalega magar 3.0 (float) nahi chalega, chahe value same hi kyun na dikhe.

print(word * 0)     #(khaali line - 0 baar repeat matlab empty string)


#Task 17 - Which string operations work and which give errors

s1 = "Hello"
s2 = "World"

#1. string + string  -> WORKS
print(s1 + s2)      #HelloWorld

#2. string * integer -> WORKS
print(s1 * 3)       #HelloHelloHello

#3. string - string  -> ERROR
#print(s1 - s2)      #TypeError: unsupported operand type(s) for -: 'str' and 'str'

#4. string / string  -> ERROR
#print(s1 / s2)      #TypeError: unsupported operand type(s) for /: 'str' and 'str'

#Ek aur common error - string + integer
#print(s1 + 5)       #TypeError: can only concatenate str (not "int") to str

#Record:
#string + string   -> chalta hai, dono strings jud jaati hai
#string * integer  -> chalta hai, string utni baar repeat hoti hai
#string - string   -> ERROR, string mein se string "ghatane" ka koi matlab nahi hota
#string / string   -> ERROR, string ko baant nahi sakte
#Reason: + aur * ko Python ne strings ke liye alag meaning diya hai (jodna aur repeat karna),
#magar - aur / ke liye koi meaning define hi nahi hai, isliye TypeError aata hai.


#Part 7 - None Type


#Task 18 - Arithmetic with None

value = None

print("Value:", value, type(value))   #None <class 'NoneType'>

#Saari operations error dengi, isliye comment mein rakhi hai:
#print(value + 5)    #TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
#print(value - 5)    #TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
#print(value * 5)    #TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
#print(value / 5)    #TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'
#print(value // 5)   #TypeError: unsupported operand type(s) for //: 'NoneType' and 'int'
#print(value % 5)    #TypeError: unsupported operand type(s) for %: 'NoneType' and 'int'
#print(value ** 5)   #TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'

#Explanation - None arithmetic mein kyun nahi chalta:
#None ka matlab hai "koi value hai hi nahi" - ye zero nahi hai, khaali jagah nahi hai,
#balki value ka na hona batata hai. Uska type NoneType hai.
#Arithmetic ke liye Python ko koi number chahiye jispar calculation ho sake.
#True ko wo 1 maan leta hai kyunki bool asal mein int hi hai,
#magar NoneType ka int se koi rishta nahi hai, isliye wo 0 bhi nahi banta.
#Jab koi value hi nahi hai to usme 5 jodne ka matlab hi nahi banta, isliye TypeError aata hai.
#Dhyaan do: saari 7 operations mein error same hai - TypeError,
#sirf operator ka naam badalta hai. ** wale message mein "** or pow()" likha aata hai.


#Part 8 - Error Handling Practice


#Task 19 - Demonstrate three common errors

#1. Division by Zero -> ZeroDivisionError
#print(10 / 0)     #ZeroDivisionError: division by zero
#print(10 // 0)    #ZeroDivisionError: division by zero
#print(10 % 0)     #ZeroDivisionError: division by zero
#Reason: kisi bhi cheez ko 0 se baantna maths mein hi allowed nahi hai,
#isliye Python ruk jaata hai aur ZeroDivisionError deta hai.

#2. Invalid String Arithmetic -> TypeError
#print("abc" - "a")    #TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print("abc" / "a")    #TypeError: unsupported operand type(s) for /: 'str' and 'str'
#print("abc" * 2.5)    #TypeError: can't multiply sequence by non-int of type 'float'
#Reason: strings par - aur / ka koi matlab define nahi hai.

#3. Arithmetic with None -> TypeError
#print(None + 5)       #TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
#Reason: None koi number nahi hai, isliye usse calculation nahi ho sakti.

#Summary of errors:
#Division by Zero        -> ZeroDivisionError
#String - String         -> TypeError
#String / String         -> TypeError
#String * Float          -> TypeError
#None + Integer          -> TypeError
#Farak samajhne wali baat: ZeroDivisionError mein types sahi the (dono number the),
#bas value galat thi (0). TypeError mein value se pehle TYPE hi galat hai.


#Part 9 - Combined Challenge


#Task 20 - Mini Calculator

num1 = 24
num2 = 7

print("----- MINI CALCULATOR -----")
print("Number 1:", num1)
print("Number 2:", num2)
print("---------------------------")
print("Addition       :", num1 + num2)    #31
print("Subtraction    :", num1 - num2)    #17
print("Multiplication :", num1 * num2)    #168
print("Division       :", num1 / num2)    #3.4285714285714284
print("Floor Division :", num1 // num2)   #3
print("Modulus        :", num1 % num2)    #3
print("Exponentiation :", num1 ** num2)   #4586471424
print("---------------------------")

#Note: 24 ke andar 7 poore 3 baar aata hai (7*3=21) aur 3 bach jaata hai,
#isliye floor division 3 aur modulus bhi 3 aaya - dono ka 3 hona sirf ittefaq hai.


#Part 10 - Final Challenge


#Task 21 - Arithmetic Expression Analyzer

a = 10
b = -3
c = 2.5

print("===== EXPRESSION ANALYZER =====")

#Expression 1
print("a + b            =", a + b)              #Prediction: 7    | Actual: 7    | Correct

#Expression 2
print("a - b            =", a - b)              #Prediction: 13   | Actual: 13   | Correct
#10 - (-3) matlab 10 + 3 = 13

#Expression 3
print("a * b            =", a * b)              #Prediction: -30  | Actual: -30  | Correct

#Expression 4
print("a / b            =", a / b)              #Prediction: -3.33 | Actual: -3.3333333333333335
#Prediction thoda galat tha. Maine socha tha saaf -3.33 aayega,
#magar Python float ko binary mein store karta hai aur poori lambi value dikhata hai.

#Expression 5
print("a // b           =", a // b)             #Prediction: -3   | Actual: -4   | WRONG
#Galat kyun: maine -3.33 ka decimal hata ke -3 socha tha,
#magar floor division left side wala integer leta hai aur -4 < -3.33 hai, isliye -4.

#Expression 6
print("a % b            =", a % b)              #Prediction: 1    | Actual: -2   | WRONG
#Galat kyun: maine remainder positive socha tha,
#magar remainder ka sign divisor jaisa hota hai aur b negative hai.
#Formula se check: (a // b) * b + (a % b) -> (-4 * -3) + (-2) = 12 - 2 = 10 = a. Sahi hai.

#Expression 7 (float involved)
print("b * c            =", b * c)              #Prediction: -7.5 | Actual: -7.5 | Correct

#Expression 8 (multiple operators - precedence matters)
print("a + b * c        =", a + b * c)          #Prediction: 2.5  | Actual: 2.5  | Correct
#Pehle * chala (-3 * 2.5 = -7.5), phir + chala (10 - 7.5 = 2.5).

#Expression 9 (parentheses change the answer)
print("(a + b) * c      =", (a + b) * c)        #Prediction: 17.5 | Actual: 17.5 | Correct
#Bracket ne pehle 10 + (-3) = 7 karwaya, phir 7 * 2.5 = 17.5.
#Expression 8 aur 9 ke numbers same hai magar answer 2.5 vs 17.5 - sirf bracket ka farak.

#Expression 10 (multiple operators - left to right)
print("a / b // c       =", a / b // c)         #Prediction: -1.0 | Actual: -2.0 | WRONG
#Galat kyun: / aur // ki precedence same hai isliye left se right chalta hai.
#Pehle 10 / -3 = -3.3333333333333335, phir wo // 2.5 = -1.333 ka floor = -2.0.
#Maine -1.33 ka decimal hata ke -1.0 socha tha, magar floor phir se neeche -2.0 le gaya.

#Expression 11 (negative number with power)
print("a ** -b          =", a ** -b)            #Prediction: 1000 | Actual: 1000 | Correct
#-b matlab -(-3) = 3, to 10 ** 3 = 1000.

#Expression 12 (classic precedence trap)
print("-a ** 2          =", -a ** 2)            #Prediction: 100  | Actual: -100 | WRONG
#Galat kyun: ** ki precedence unary minus se ZYADA hai.
#Matlab Python ne -(10 ** 2) = -100 kiya, na ki (-10) ** 2 = 100.
#Agar 100 chahiye to bracket lagana padega:
print("(-a) ** 2        =", (-a) ** 2)          #100

#Expression 13 (multiple operators - ** first)
print("a % b ** 2       =", a % b ** 2)         #Prediction: 1    | Actual: 1    | Correct
#** sabse pehle chala: (-3) ** 2 = 9, phir 10 % 9 = 1.

#Expression 14 (brackets + power + float)
print("(a - b) / c ** 2 =", (a - b) / c ** 2)   #Prediction: 2.08 | Actual: 2.08 | Correct
#Bracket pehle: 10 - (-3) = 13. Phir ** : 2.5 ** 2 = 6.25. Ant mein 13 / 6.25 = 2.08.

#Expression 15 (mixed + - *)
print("a + b - c * 2    =", a + b - c * 2)      #Prediction: 2.0  | Actual: 2.0  | Correct
#Pehle * : 2.5 * 2 = 5.0, phir left se right: 10 - 3 = 7, 7 - 5.0 = 2.0 (float aaya).

print("===============================")

#FINAL LEARNING - jahan prediction galat hui:
#1. Floor division negative mein neeche jaata hai (-4, -2.0), decimal hatana galat tareeka hai.
#2. Modulus ka sign divisor se aata hai, isliye 10 % -3 = -2 hai, 1 nahi.
#3. ** unary minus se pehle chalta hai, isliye -a ** 2 = -100 hai, 100 nahi.
#4. Float division ki lambi value (-3.3333333333333335) binary storage ki wajah se aati hai.
#Operator precedence order: ()  ->  **  ->  unary -  ->  * / // %  ->  + -
