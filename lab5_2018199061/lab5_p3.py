res = []
ans = 1
while True:
    ans = int(input('Enter an integer: '))
    if ans == 0:
        break
    if ans <= 100:
        res.append(ans)
    else:
        res.append('over')

print(res)