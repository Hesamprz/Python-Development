user_list = []
even_list = []
counter = 0
list_len = int(input("Enter the length of list: "))

while counter < list_len:
    num = int(input(f"Enter number {counter+1}: "))
    user_list.append(num)
    counter += 1

for even in user_list:
    if even % 2 == 0:
        even_list.append(even)

print(even_list)