user_list = []
unique_list = []
list_len = int(input("Enter the length of list: "))
counter = 0

while counter < list_len:
    num = int(input(f"Enter number {counter + 1}: "))
    user_list.append(num)
    counter += 1

for i in user_list:
    if i not in unique_list:
        unique_list.append(i)
        
print(f"unique list: {unique_list}")
