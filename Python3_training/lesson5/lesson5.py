# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

# In this case, '1 + int(0.5 + 0.5)' is evaluated first due to the precedence rules
# The resulting value is 2. Then, '**' (exponentiation) is applied to 2 ** 10
# The final result is 1024
calculation_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(calculation_1)  # Output: 1024

