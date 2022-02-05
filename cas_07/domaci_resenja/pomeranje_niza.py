niz = [int(i) for i in input().split()]

"""
ulaz = input()   # ulaz="1 4 5 7 8 3"
niz_stringova = ulaz.split()   # niz_stringova=["1", "4", "5", "7", "8", "3"]
niz = []
for element in niz_stringova:
    niz.append(int(element))
"""

k = int(input())

for i in range(k):
    prvi = niz[0] # sacuvamo prvi element
    niz.pop(0) # izbacimo prvi element
    niz.append(prvi) # dodamo izbaceni element na kraj
    print(i, niz)

print(niz)

