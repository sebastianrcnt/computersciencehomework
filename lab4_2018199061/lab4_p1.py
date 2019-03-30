# get input
ans = int(input('Enter the taxable income in USD: '))

# set due
due = 0.0

# case seperation
if ans < 750:
    due = ans * 0.01
elif 750 <= ans < 2250:
    due = 7.50 + 0.02 * (ans - 750)
elif 2250 <= ans < 3750:
    due = 37.50 + 0.03 * (ans - 2250)
elif 3750 <= ans < 5250:
    due = 82.50 + 0.04 * (ans - 3750)
elif 5250 <= ans < 7000:
    due = 142.50 + 0.05 * (ans - 5250)
elif ans >= 7000:
    due = 230.00 + 0.06 * (ans - 7000)

# print result
print('Tax due: %.2f USD' %  due)