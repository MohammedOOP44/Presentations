list = [["apple","banana"],["milk","water"]]
input("press Enter to change the content...")
list.append([1,2,3])
list[0].insert(0,"orange")
list[0].append("kiwis")
list[1].append("tea")
list[1].insert(0,"coffee")
list[1].remove("water")
print(list)
