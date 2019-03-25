ans = input('Enter the first 12 digits of an EAN: ')
firstSum = int(ans[1]) + int(ans[3]) + int(ans[5]) + int(ans[7]) + int(ans[9]) + int(ans[11])
secondSum = int(ans[0]) + int(ans[2]) + int(ans[4]) + int(ans[6]) + int(ans[8]) + int(ans[10])
checkDigit = 9 - ((firstSum * 3 + secondSum - 1) % 10)

print(f'Check digit: {checkDigit}')