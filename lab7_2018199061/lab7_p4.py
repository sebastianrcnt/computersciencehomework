def evalPolynomial(x):
    """
    Input: x: number
    Returns 3*x**5 + 2*x**4 - 5*x**3 - x**2 + 7*x - 6
    """
    return 3*x**5 + 2*x**4 - 5*x**3 - x**2 + 7*x - 6


ans = int(input('Enter a value for x: '))
print('Polynomial for x='+str(ans)+': '+str(evalPolynomial(ans)))
