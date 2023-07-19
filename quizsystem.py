# Import required modules
import random

# User Classes
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.score = 0

class Teacher:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.quizzes = []

class Parent:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.children = []

# Quiz Class
class Quiz:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions
        self.participants = []

# Question Class
class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

# Quiz Management System Class
class QuizManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.parents = []
        self.quizzes = []

    def create_quiz(self, title, questions):
        quiz = Quiz(title, questions)
        self.quizzes.append(quiz)

    def invite_participant(self, quiz, participant):
        quiz.participants.append(participant)

    def enable_submissions(self, quiz):
        quiz.submissions_enabled = True

    def retrieve_results(self, quiz):
        results = {}
        for participant in quiz.participants:
            results[participant] = participant.score
        return results

    def display_quiz(self, quiz, participant):
        for question in quiz.questions:
            print(question.question)
            answer = input("Your answer: ")
            if answer == question.correct_answer:
                participant.score += 1

    def display_score(self, quiz, participant):
        print("Your score for the quiz is {}.".format(participant.score))

    def quit_or_retake(self, quiz, participant):
        choice = input("Would you like to quit (q) or retake the quiz (r)? ")
        if choice == "q":
            print("Thanks for taking the quiz!")
        elif choice == "r":
            self.display_quiz(quiz, participant)
        else:
            print("Invalid choice. Please enter 'q' or 'r'.")

# Testing and Usage
def main():
    # Create students
    student1 = Student("John Doe", 12345)
    student2 = Student("Jane Doe", 67890)

    # Create teachers
    teacher1 = Teacher("Mr. Smith", 123456)
    teacher2 = Teacher("Mrs. Jones", 789012)

    # Create parents
    parent1 = Parent("John Doe Sr.", 123457)
    parent2 = Parent("Jane Doe Sr.", 789013)

    # Create a quiz
    question1 = Question("What is 2+2?", "4")
    question2 = Question("What is the capital of France?", "Paris")
    quiz = Quiz("Math Quiz", [question1, question2])

    # Add participants
    quiz.participants.append(student1)
    quiz.participants.append(student2)

    # Enable submissions
    quiz.submissions_enabled = True

    # Display quiz to student1
    QuizManagementSystem().display_quiz(quiz, student1)

    # Display score for student1
    QuizManagementSystem().display_score(quiz, student1)

    # Give the user the option to quit or retake the quiz
    QuizManagementSystem().quit_or_retake(quiz, student1)

if __name__ == "__main__":
    main()
