#if condition
var1=200
if var1:
    print("1-got a true expression")
    print(var1)
var2=100
if var2:
    print("2-got a true erpression value")
    print(var2)
    print("good bye")

#elif statement:
var=100
if var==200:
    print("var=",var)
elif(var==150):
    print("var=",var)
elif var==100:
    print("var=",var)
else:
    print(var)
    print,"good bye!"

#nested if statement:
var=100
if var<200:
    print("expression value is less than 200")
if var==150:
    print("which is 150")
elif (var==100):
    print("which is 100")
elif var==50:
    print("which is 50")
elif var<50:
    print("expression value is less 50")
else:
    print("could not find true expression")
    print("good bye!")