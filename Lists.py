# In[2]:
num = [10,20,30,40,50]

print("List:",num)
print("First element:", num[0])
print("Second element:", num[1])
print("Third element:", num[2])
print("Fourth element:", num[3])
print("Fifth element:", num[4])

# In[6]:
num = [10,20,30,40,50]
num.append(70)
print("After Appending:",num)

# In[7]:
num = [10,20,30,40,50]
print("original list:",num)
num.reverse()
print("Reversed List:", num)

# In[9]:
num = [10,30,27,40,27,30,30,18,30]
element = int(input("Enter Element: "))
count=num.count(element)
print("Occurence:", count)

# In[11]:
list1=[10,20,30]
list2=[40,50,60,70]
list1 = list1 + list2
print("List1:", list1)

# In[12]:
list1=[10,20,30]
list2=[40,50,60,70]
list2 = list2 + list1
print("List2:", list2)

# In[19]:
numbers = [10,20,30,40,50,60]
numbers.insert(1, 15)
print("List:", numbers)

# In[17]:
numbers = [10,20,30,40,50,60]
index = int(input("Enter the Number to remove:"))
numbers.pop(index)
print("Updated List:", numbers)

# In[21]:
numbers = [10,20,30,40,50,60]
element = int(input("Enter the element:"))
numbers.remove(element)
print("Updated List:", numbers)

# In[23]:
numbers = []
for i in range(20): 
    num = int(input("Enter value")) 
    numbers.append(num)

print("\nList:" , numbers)

# In[24]:
for i in range(20):
    if numbers.count(numbers[i])>1:
        print(numbers[i],"->",end="")

        for j in range(20):
            if numbers[j]==numbers[i]:
                print(j,end="")

        print()

# In[26]:
even_count=0
odd_count=0

for num in numbers:
    if num%2==0:
        even_count += 1
    else:
        odd_count += 1

print("Even Values:",even_count)
print("Odd Values:",odd_count)

# In[29]:
positive_count=0
negative_count=0

for num in numbers:
    if num>0:
        positive_count += 1
    else:
        negative_count += 1

print("Positive Numbers:",positive_count)
print("Negative Numbers:",negative_count)

# In[32]:
numbers=[]

for i in range(10):
    num=int(input("Enter a Value:"))
    numbers.append(num)

print("List:",numbers)

# In[35]:
ascending = sorted(numbers)

print("Ascending Order:",ascending)

# In[36]:
numbers.sort(reverse=True)

print("Descending Order:", numbers)

# In[37]:
print("Length of List:", len(numbers))

# In[40]:
list1=[]
for num in range (5):
    num=int(input("Enter a number:"))
    list1.append(num)
print("List1:", list1)

list2=[]
for num in range (5):
    num=int(input("Enter a number:"))
    list2.append(num)
print("List2:",list1)

list1= list1 + list1
print("Merged list:", list1)

# In[41]:
phrase = input("enter a phrase:")
words = phrase.split()
acronym=""
for word in words:
    acronym=acronym + word[0]


print("Acronym:",acronym.upper())

# In[42]:
months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
month_number=int(input("Enter month number(1-12):"))
if month_number>=1 and month_number<=12:
    print("Month abbreviation:",months[month_number-1])
else:
    print("Invalid Month Number")

# In[43]:
fruit =["Apple","banana","cherry","watermelon"]
fruit.remove("banana")
print(fruit)

# In[44]:
fruit =["Apple","banana","cherry","watermelon"]
removed_item=fruit.pop(0)
print(fruit)

# In[45]:
fruit =["Apple","banana","cherry","watermelon"]
del fruit[0]
print(fruit)

# In[46]:
fruit =["Apple","banana","cherry","watermelon"]
del fruit[0:2]
print(fruit)

# In[47]:
fruit =["Apple","banana","cherry","watermelon"]
fruit.clear()
print(fruit)

# In[49]:
key=[101,102,103,104,105]
values=["amit","rahul","krishna","priya"]
student_dict=dict(zip(key, values))
print("Dictionary:",student_dict)

# In[50]:
list1=[10,20,30,40,50]
list2=[40,60,70,80]
common=[]

for n in list1:
    if n in list2:
        common.append(n)

print("Common Elemet:", common)
