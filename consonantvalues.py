def solve(word):
    def get_consonant_value(s):
        return sum(ord(c) - ord('a') + 1 for c in s)

    consonant_values = [get_consonant_value(s) for s in word.split('aeiou')]

    return max(consonant_values)


print(solve("zodiacs"))  
print(solve("strength"))  
