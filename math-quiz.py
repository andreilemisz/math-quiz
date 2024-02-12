# Create a math quiz with options and display the end results
# The framework must be created using a dictionary
counter = 1 # To prevent the indexes from starting at 0 to the user
answer = None # User input
correct_answers = 0 # Number os answers got right

quiz = [
    
    {
        "Question": "How much is 7 x 7?",
        "Options": [36, 45, 49, 62],
        "Answer": 49,
        
    },
    
    {
        "Question": "How much is 55 / 5?",
        "Options": [11, 8, 6, 13],
        "Answer": 11,
    },
    
    {
        "Question": "How much is 10 + 20 + 37?",
        "Options": [57, 47, 77, 67],
        "Answer": 67,
    },
    
    {
        "Question": "How much is the square of 8?",
        "Options": [56, 78, 68, 80],
        "Answer": 68,
    },
    
]
print('Welcome to the Math Quiz! Please type the correct alternative to each question!\n')

for header in quiz:
    print(header["Question"])
    for options in header["Options"]:
        print(f"{counter}) {options}")
        counter += 1
    answer = input("Choose an option: ")
    
    try:
        answer = int(answer)
        if answer < 5 and answer >= 1:
            answer = answer - 1
            pass
        
        else: 
            print("Incorret answer!")
            print()
            counter = 1
            continue
        
    except:
        print("Incorret answer!")
        print()
        counter = 1
        continue
    
    if header["Options"][answer] == header["Answer"]:
        print("Thats the correct answer!")
        correct_answers += 1
    else:
        print("That is not the correct answer!")
    
    print()
    counter = 1

print()
print(f"You got {correct_answers} answers right!")