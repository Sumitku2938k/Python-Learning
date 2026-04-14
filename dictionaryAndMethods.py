#a = {}
#b = set() #Empty Set
#print(a, type(a))
#print(b, type(b))

dict1 = {"good": "Something please", "fetch": "to bring", "1": "The no 1"} # Key: value
print(dict1)
print(dict1["good"])

marks = {"Harshit": 34, "Goutam": 99, "Shivani": 8, "Smriti": 45, "Naina": 87, "Sankalp": 78}
print(marks["Goutam"])
marks["Harshit"] = 56 #Dictionaries are mutable means that they can be change
marks["Priyanka"] = 78
print(marks)

print(marks.get("Priyanka Chopra")) #Does not exist therefore return None
#print(marks["Priyanka Chopra"])

print(marks.get("Priyanka"))
print(marks["Priyanka"])

print(marks.keys())
print(marks.values())
print(marks.items())