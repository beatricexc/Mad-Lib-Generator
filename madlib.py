loop = 1
# The questions the program asks the user
while(loop < 10):
  noun = input("Choose a noun: ")
  p_noun = input("Choose a plural noun: ")
  noun2 = input("Choose another noun: ")
  place = input("Name a place: ")
  adjective = input("Choose an adjective (Describing word): ")
  noun3= input("Choose a noun: ")
# Outputs the story based on user input
  print("------------------------------------")
  print("Be kind to your", noun, "- footed", p_noun)
  print("For a duck may be somebody's", noun2, ",")
  print("Be kind to your", p_noun, "in", place)
  print("Where the weather is always", adjective, ".")
  print()
  print("You may think that is this the", noun3, ",")
  print("Well it is.")
  print("-------------------------------------")
#Loops back to loop 1
  loop = loop + 1
