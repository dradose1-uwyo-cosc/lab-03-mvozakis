Names = [ 'Spencer', 'RJ', 'Fransisco', 'McCoy', 'Rider']
print(Names)

del Names[3]
print(Names)

for Name in Names:
    print(f"{Name} is at my table")

Names.sort()
print(Names)