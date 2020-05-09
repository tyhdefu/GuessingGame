import os
import pickle
import GuessingGameFunctions


################################

class Question(object):
  def __init__(self, text, yes=None, no=None):
    self.text = text
    self.yes = yes
    self.no = no
    
################################

AskAMV = GuessingGameFunctions.UIAskAMV
QuestionYesNo = GuessingGameFunctions.UIQuestionYesNo
WhatWereYouThinkingOf = GuessingGameFunctions.UIWhatWereYouThinkingOf
WhatQuestionShouldIHaveAskedInstead = GuessingGameFunctions.UIWhatQuestionShouldIHaveAsked
KeepPlaying = GuessingGameFunctions.KeepPlaying

#QuestionYesNo = GuessingGameFunctions.StoneTestQuestionYesNo
#WhatWereYouThinkingOf = GuessingGameFunctions.StoneTestWhatWereYouThinkingOf
#WhatQuestionShouldIHaveAskedInstead = GuessingGameFunctions.StoneTestWhatQuestionShouldIHaveAsked

################################

filename = "amv.p"

try:
  file = open(filename, "rb")
  print("(Loading previous questions)")
  initialQuestions = pickle.load(file)
except FileNotFoundError:
  print("(Setting up initial questions)")
  
  malleable = Question("Is it malleable at high temperatures")
  growInGround = Question("Does it grow in the ground")
  hasFourLegs = Question("Does it have four legs")

  iron = Question("Is it iron")
  copper = Question("Is it copper")
  carrot = Question("Is it a carrot")
  tree = Question("Is it a tree")
  dog = Question("Is it a dog")
  ant = Question("Is it an ant")

  malleable.yes = iron
  malleable.no = copper
  growInGround.yes = carrot
  growInGround.no = tree
  hasFourLegs.yes = dog
  hasFourLegs.no = ant

  initialQuestions = [malleable, growInGround, hasFourLegs]
  
################################

while True:
  _ = os.system("clear")
  print("Hi Welcome to mineral, plant or animal!")
  print("Think of a a natural object and i will try to guess it")

  answer = AskAMV()
  question = initialQuestions[answer]
  
  while True:
    yes = QuestionYesNo(question.text)
    if question.yes == None:
      if yes:
        print("Haha I win")
        break
      else:
        print("You win")
        newItem = WhatWereYouThinkingOf()
        newQuestionText = WhatQuestionShouldIHaveAskedInstead()
        yes = QuestionYesNo("What would you have answered for " + newItem)
        
        savedText = question.text
        question.text = newQuestionText
        if yes:
          question.yes = Question("Is it " + newItem)
          question.no = Question(savedText)
        else:
          question.yes = Question(savedText)
          question.no = Question("Is it " + newItem)
          
        pickle.dump(initialQuestions, open(filename, "wb"))
        break
    else:
      if yes:
        question = question.yes
      else:
        question = question.no
  if KeepPlaying():
    print("Lets keep playing")
  else:
    quit("Thanks for Playing")