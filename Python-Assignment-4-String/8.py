# 8.Write a Python function that takes a list of words and returns the length of the longest one. 

def length_of_longest(list):
  list1=list[0]
  list2=[]
  for i in list:
    if len(i)>len(list1):
      list2=[i]
    else:
      list2=[list1]
  print("Longest word: ",list2[0])
  print("Length of the longest word: ",len(list2[0]))

length_of_longest(["poornima","nisarga","pacewisdomsolutions"])
