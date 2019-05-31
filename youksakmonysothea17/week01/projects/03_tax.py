amount = input("Please enter your amount: \n")
condition = True
while condition:
    if amount[0] == '-':
        amount = input("Number is incorrect, try again.\n")
    elif amount.isdigit() is False:
        amount = input("Number is incorrect, try again.\n")
    else:
        amount = int(amount)
        condition = False
rate = int(input("Please enter tax rate:\n"))
condition = True
while condition:
    if not 1 <= rate <= 99:
        rate = input("Rate is incorrect, try again.\n")
    else:
        condition = False
rate = int(rate)
tax = (amount * rate) / 100
net = amount - tax
net = '{:.2f}'.format(net)
tax = '{:.2f}'.format(tax)
print("\n===== ===== ===== ===== ====="
      + f"\nAMOUNT: {amount}$"
      + f"\nRATE: {rate}%"
      + "\n===== ===== ===== ===== ====="
      + f"\nTAX: {tax}$"
      + f"\nNET: {net}$"
      + "\n===== ===== ===== ===== =====")
