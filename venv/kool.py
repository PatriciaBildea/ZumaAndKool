n = 0
k = 0

def cool(k):
    distinct = 0
    distinct_list = []
    for i in range(k):
        if sorted(A[:k])[i] not in distinct_list:
            if 0 < i < k-1 and sorted(A[:k])[i-1] != sorted(A[:k])[i] != sorted(A[:k])[i+1]:
                distinct += 1
                distinct_list.append(sorted(A[:k])[i])
            elif i == 0 and sorted(A[:k])[i] != sorted(A[:k])[i+1]:
                distinct += 1
                distinct_list.append(sorted(A[:k])[i])
            elif i == k-1 and sorted(A[:k])[i-1] != sorted(A[:k])[i]:
                distinct += 1
                distinct_list.append(sorted(A[:k])[i])
    consecutive = True
    for i in range(len(distinct_list)-1):
        if sorted(distinct_list)[i] + 1 != sorted(distinct_list)[i+1]:
            consecutive = False
            break
    print(distinct)
    if sorted(distinct_list) == sorted(A[:k]) and consecutive:
        print(f"""The sequence: {A[:k]} is Cool.
The max value in the sequence is {sorted(distinct_list)[-1]}""")
    else:
        print(f"""The sequence: {A[:k]} is not Cool.
There are {distinct} unique values in the sequence.""")
        if distinct != 0:
            print(f"These are: {distinct_list}")


incorrect_input = True
while incorrect_input:
    try:
        n = int(input("The length of the list: "))
        k = int(input("The length of the sequence to be checked if Cool: "))
    except:
        print("Data not valid. Please try again:")
    else:
        if n <= 0 or k <= 0 or n < k:
            print("Data not valid. Please try again:")
        else:
            incorrect_input = False

A = []
i = 0
while i < n:
    for j in range(i, n):
        try:
            a = int(input(f"Number {i+1} in the list is: "))
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

cool(k)

