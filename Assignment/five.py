   
def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence.append(1)
    return sequence

num = int(input("Enter a starting number: "))
print("Syracuse Sequence:", collatz_sequence(num))
