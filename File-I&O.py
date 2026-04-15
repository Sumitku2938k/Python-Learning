s = 'Goutam is a good boy.'

# File ko string mei write karna i.e. Is test.txt file ko banane ke bad isme 's' string ko dal/write kar diya jayega
# Writing to a file
#with open("test.txt", "w") as f: #Context Manager usse ho raha hai means no need to manually close it
#    f.write(s)

#fp = open('file1.txt', 'w') #Same work karta hai but isme context manager use nahi ho raha isliye close karna padta hai
#fp.write(s)
#fp.close()

#Reading a file
#with open("file.txt", "r") as f:
#    a = f.read()
#    print(a)

# f = open('file.txt', 'r') #Same work karta hai but isme context manager use nahi ho raha isliye close karna padta hai
# a = f.read()
# print(a)
# f.close()

# Appending to a file
with open("file.txt", "a") as file: #File ke end mei data dal deta hai append
    file.write(" And sometimes bad")
