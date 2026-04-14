#l1 = [1,2,3,4,5,6, "Goutam"]
#print(l1)
#print(type(l1))

#List are imutable i.e. Dusri list banane ki jarurat nahi hoti ussi mei changes apply ho jate hain

#l1.remove("Goutam")
#print(l1)

#print(l1.count(4))
l1 = [1,7,9,3,4,5,6]
print(l1)
#l1.sort()
#l1.pop()
#l1.append(92) -> push to last in list
#l1.clear() -> clear/remove all elem in list
#l1.extend([2,3,4,5,6]) -> add all these elem in the list
#print(l1.index(5)) -> return index of 5 in l1
print(l1[0:4])

l1[0] = 25 #List can be changeable
print(l1)