##This is a customer survey function. Feel free to modify the questions

def survey():
  userInput=[]

  name = input(f"Hello! What's your name? ")
  print(f"Hi {name}! I will ask you a series 5 of questions regarding your recent customer experience.")
  print("--------------------------------------------------------------\n")

  userInput1 = input("1. How would you describe your buying experience with us? ")
  userInput.append(userInput1)
  print(" ")

  userInput2 = input("2. How would you describe your experience with our agent yesterday? ")
  userInput.append(userInput2)
  print(" ")

  userInput3 = input("3. Do you agree that the issue was resolved? If not, why? ")
  userInput.append(userInput3)
  print(" ")

  userInput4 = input("4.How likely is it that you would recommend our products to others? ")
  userInput.append(userInput4)
  print(" ")

  userInput5 = input(f"5. {name}, is there anything else you would add before we end the survey? ")
  userInput.append(userInput5)
  print("-------------------------------------------------------------------------- ")

  response = " ".join(userInput)
  return response



