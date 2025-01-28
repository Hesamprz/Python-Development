original_list = []
rotated_list = []
rotation_count = int(input("Enter the rotation count: "))
counter = 0
list_len = int(input("Enter the length of list: "))

while counter < list_len:
    num = int(input(f"Enter number {counter + 1}: "))
    original_list.append(num)
    counter += 1
    

rotation_count = rotation_count % len(original_list)

for i in range(rotation_count):
    rotated_list.append(original_list[-rotation_count + i])

for i in range(len(original_list) - rotation_count):
    rotated_list.append(original_list[i])

print("Rotated list:", rotated_list)
