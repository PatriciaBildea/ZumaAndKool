n = 0
k = 0

incorrect_input = True
while incorrect_input:
    try:
        n = int(input("The length of the sequence: "))
        k = int(input("The length of the sequence to be checked if Cool: "))
    except:
        print("Data not valid. Please try again:")
    else:
        if n <= 0 or k <= 0:
            print("Data not valid. Please try again:")
        else:
            incorrect_input = False

A = []
i = 0
while i < n:
    for j in range(i, n):
        try:
            a = int(input(f"Number {i+1} in the sequence is: "))
            A.append(a)
            i += 1
        except:
            print("Data not valid. Please try again:")
        else:
            if a <= 0:
                print("Data not valid. Please try again:")
                i -= 1
                A.remove(a)
        if i == n:
            incorrect_input = False

# def cool(n, k):
#     i = 0
#     for x in range(i, n-1):
#         for y in range(i, k+i-1):

print(A)

