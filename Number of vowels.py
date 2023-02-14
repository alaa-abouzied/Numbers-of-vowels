str1 = input("Please Enter Your Own String : ")

vowels = set("aeiou")
count = 0
str = str1.lower()

for i in str:
    if i in vowels:
        count += 1
print("Total Number of Vowels in this String = ", count)
