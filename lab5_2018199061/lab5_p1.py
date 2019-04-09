max_num = 0
ans = float(input("Enter a number: "))
if ans <= 0:
    print('No positive number was entered')
else:
    while True:
        ans2 = float(input("Enter a number: "))
        ans = max(ans, ans2)
        if ans2 <= 0:
            break
    if ans <= 0:
        print('No positive number was entered')
    else:
        print('The largest number entered was {0:.2f}'.format(ans)) # 수정 필요