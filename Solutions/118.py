from prime import miller_rabin
import itertools

def count(digits : list, lower_bound : int):
    if len(digits) == 0:
        return 1
    output = 0
    for numberOfDigits in range(len(digits)):
        for permutation in itertools.permutations(digits, numberOfDigits+1):
            digitsCopy = digits.copy()
            for element in permutation:
                digitsCopy.remove(element)
            number = int(''.join(permutation))
            if miller_rabin(number) and number > lower_bound:
                output += count(digitsCopy, number)
    return output

print(count([str(i+1) for i in range(9)], 0))