s = input("Enter String : ")
s = s.strip()
count = 0 
space_count = 0
word_count = 1
for i in s :
    count+=1
    if i.isspace():
        space_count+=1
        word_count+=1
print("Total Character Is : ",count)
print("Total Space : ",space_count)
print("Total Word Count : ",word_count)
