mylist = ["a","b","d","f"]

try:
    myindex = mylist.index("d")
except Exception as firstvote:
    mylist.append("d")
    myindex = mylist.index("d")

print (myindex)

try:
    myindex = mylist.index("c")
except Exception as firstvote:
    mylist.append("c")
    myindex = mylist.index("c")

print (myindex)