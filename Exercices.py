# def palindrome(text):
#     if text == text[::-1]:
#         return "It is a palindrome"
#     else:
#         return "it is not a palindrome"
#
#
# text = input("Ce doresti sa verifici azi? --> ")
# print(palindrome(text))

# caracter cu caracter^
def palindrome(text):
    is_palindrome = True
    for i in range(int(len(text)/2 + 1)):
        if text[i] != text[-i-1]:
            is_palindrome = False
            break
    if is_palindrome:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"


letters = input("Ce doresti sa verifici azi? --> ")
print(palindrome(letters))

# Game of Thrones
# Dothraki plănuiesc să usurpe tronul Regelui Robert. Regele Robert aude de această conspirație de la un raven și plănuiește să încuie singura ușă prin care inamicul poate să pătrundă în regat lui.
# Dar această ușă are nevoie de o cheie care este reprezentată de către anagrama unui palindrom.
# începe să caute în cutia lui de șiruri de caractere, verificând pe fiecare în parte dacă poate fi rearanjat într-un palindrom.
# Cerință:
# Pentru un șir de caractere, să se tipărească pe ecran cuvântul DA sau NU dacă acest șir poate fi rearanjat astfel încât să fie un palindrom.
# Constrangeri:
# Poat fi folosite doar caractere din alfabetul latin cu litere mici
# Date de intrare:
# Șirul de caractere.
# Exemplu:
# INPUT:
# aaabbbb
# OUTPUT:
# DA
# Șirul poate fi permutat astfel: bbaaabb

def anagram(letters):
    a = 0  # we use this to count characters that appear an odd amount of time. if there is more than 1 (that could go in the middle of te palindrome) the string cannot be arranged as a palindrome
    letters_list = []  # we use this list to gather all different letters in the string so we don't count their appearance multiple times
    for i in letters:
        if i not in letters_list:
            letters_list.append(i)
    for j in letters_list:
        if letters.count(j) % 2 == 1:
            a += 1
    if a < 2:
        return "YES"
    else:
        return "NO"


letters = input("What string did you find this time? --> ")
print("Let's see if that could be a palindrome...")
print(anagram(letters))
