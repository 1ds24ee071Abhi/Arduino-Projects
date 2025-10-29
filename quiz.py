import serial
import time
Arduino = serial.Serial('COM8',9600)
quiz = {
    "What is the capital of France?": {
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 2
    },
    "Which planet is known as the Red Planet?": {
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": 1
    },
    "What is the largest mammal?": {
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippo"],
        "answer": 1
    },
    "Who wrote 'Hamlet'?": {
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": 1
    },
    "Which element has the chemical symbol 'O'?": {
        "options": ["Gold", "Oxygen", "Osmium", "Iron"],
        "answer": 1
    },
    "What is the square root of 64?": {
        "options": ["6", "7", "8", "9"],
        "answer": 2
    },
    "Which language is primarily spoken in Brazil?": {
        "options": ["Spanish", "Portuguese", "French", "English"],
        "answer": 1
    },
    "Who painted the Mona Lisa?": {
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
        "answer": 1
    },
    "What is the boiling point of water at sea level?": {
        "options": ["90°C", "100°C", "110°C", "120°C"],
        "answer": 1
    }
}

score = 0

for question, data in quiz.items():
    print("\n" + question)
    for i, option in enumerate(data["options"]):
        print(f"{i + 1}. {option}")
    try:
        user_input = int(input("Enter your answer (1-4): ")) - 1
        if user_input == data["answer"]:
            print("Correct!")
            score += 1
            Arduino.write(b'G')
            time.sleep(2)
        else:
            print(f"Wrong! Correct answer: {data['options'][data['answer']]}")
            Arduino.write(b'R')
            time.sleep(2)
    except ValueError:
        print("Invalid input. Skipping question.")

print(f"\nYour final score: {score}/{len(quiz)}")