result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
total=0
for i in result:
    if i=="heads":
        total+=1

print(total)

for item in range(1,11):
    if item%2==0:
        continue
    print(item*item)

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')

for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)


