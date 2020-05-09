
def UIAskAMV():
  while True:
    print("""Is your object a mineral, plant or animal
    
 1)Mineral
 2)Plant
 3)Animal
    """)
    answer = input("")
    if answer == "Mineral" or answer == "1":
      return 0
    elif answer == "Plant" or answer == "2":
      return 1
    elif answer == "Animal" or answer == "3":
      return 2
    else:
      print("Invalid Answer please try again")

def UIQuestionYesNo(question):
  while True:
    print(question, """?
      
 Yes
 No
  
  """)
    answer = input("")
    if answer == "Yes" or answer == "y":
      return True
    elif answer == "No" or answer == "n":
      return False
    else:
      print("Invalid Answer please try again")
QuestionYesNo = UIQuestionYesNo

def UIWhatWereYouThinkingOf():
  return input("What were you thinking of?\n")

def UIWhatQuestionShouldIHaveAsked():
  return input("What question should I have asked instead?\n")


def KeepPlaying():
  question = "Do you want to keep playing"
  if QuestionYesNo(question):
    return True
  else:
    return False
#######

def StoneTestAskAnimalVegetableOrMineral():
  print("Answering Mineral")
  return 0

def StoneTestQuestionYesNo(question):
  answer = {
    malleable.text: False,
    copper.text: False,
    "What would you have answered for a stone": False,
    "Is it a metal": False,
    "Is it a stone": True
    }[question]

  print("Answering ", answer, " to ", question)
  
  return answer

def StoneTestWhatWereYouThinkingOf():
  print("Saying I was thinking of a stone")
  return "a stone"

def StoneTestWhatQuestionShouldIHaveAsked():
  print("Saying you should have asked if a metal")
  return "Is it a metal"