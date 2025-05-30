age=18
if age < 18:
    print("You are a minor.")
    
num = 5
if num%2==0:
    print("Even")
else:
    print("Odd")
    
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
    
    
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

#for loop

for i in range(1,5):
    print(i)
    
    
    for char in "python":
        print(char)
        
#while loop
count=1
while count <= 5:
    print(count)
    count += 1
    
    # Sum of numbers 1 to 5 using for loop
total = 0
for i in range(1, 6):
    total += i
print("Total:", total)

# Sum using while loop
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Total:", total)


#break

for i in range(1, 10):
    if i == 5:
        break
    print(i)
    
#continue
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
    
#pass
for i in range(3):
        pass  # Do nothing for 5
