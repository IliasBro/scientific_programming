print("\n")
print("         \\|||||/          ")
print("         ( O O )           ")
print("|--ooO-----(_)------------|")
count = 10
for row in range(5):
    for col in range(row + 1):
        print("  ", count, end="")
        count += 1
    print("")
print("|------------------Ooo----|")
print("         |__||__|          ")
print("          ||  ||           ")
print("         ooO  Ooo          ")