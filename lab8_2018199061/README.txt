Question 1
(a)
Result will be
11 20

at line 7 10 is inputted into foo1 and foo1 returns 11 and assigns to x.
this is because n at line 4 refers to the parameter(local variable) instead of global variable n. global variable n will stay the same(10) after execution.

at line 2, n refers to global variable n in the global frame. Therefore n * 2 = 20 will be assigned to y.

(b)
Result will be
2

At line 3 x refers to a local variable at line 5(x=1), not global variable at line 8(x=0)
When function bar() is executed, it will print x(1) + 1 which is 2, in the screen.

(c)
Result will be
1

At line 3 x refers to the global variable x at line 7(x=0) since there is no local variable x in both foo, and bar.
Therefore, y is assigned to x(0) + 1, which is 1, and it will be printed to the screen when line 4 is executed.