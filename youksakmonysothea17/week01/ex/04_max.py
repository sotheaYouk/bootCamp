first_num = int(input("Enter a number:\n"))
second_num = int(input("Enter a second number:\n"))
if first_num > second_num:
    print(f"Result : {first_num} > {second_num}")
elif second_num > first_num:
    print(f"Result : {second_num} > {first_num}")
else:
    print(f"Result : {first_num} == {second_num}")
