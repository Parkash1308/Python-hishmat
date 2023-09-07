# Python program to illustrate
# Append vs write mode
file1 = open("D:\Github Data\Python\demo.txt.txt", "w")
L="Hello this is Hishmat"
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("D:\Github Data\Python\demo.txt.txt", "a") # append mode
file1.write("yes done it \n")
file1.close()

# file1 = open("D:\Github Data\Python\demo.txt.txt", "r")
# print("Output of Readlines after appending")
# print(file1.read())
# print()
# file1.close()

# # Write-Overwrites
# file1 = open("D:\Github Data\Python\demo.txt.txt", "w") # write mode
# file1.write("Tomorrow \n")
# file1.close()

# file1 = open("D:\Github Data\Python\demo.txt.txt", "r")
# print("Output of Readlines after writing")
# print(file1.read())
# print()
# file1.close()
