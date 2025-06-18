# Python quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abudant gas in the Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ") # tuple of questions
options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), 
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")) # We've 4 options for every questions that's why we're using 2D tuple

answers = () # tuple of answers
guesses = [] # list of guesses
score = 0
question_num = 0