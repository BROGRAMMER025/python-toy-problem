def exactly_two_positive(a, b, c):
    positive_count = (a > 0) + (b > 0) + (c > 0)
    return positive_count == 2


print(exactly_two_positive(2, 4, -3))  
print(exactly_two_positive(-4, 6, 8))  
print(exactly_two_positive(4, -6, 9))  
print(exactly_two_positive(-4, 6, 0))  
print(exactly_two_positive(4, 6, 10))  
print(exactly_two_positive(-14, -3, -4))  
