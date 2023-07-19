import random

class Student:
    def __init__(self, name, email, student_id, grade):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.grade = grade

    def answer_question(self, question):
        answer = input(f"What is the answer to {question}? ")
        return answer

class Teacher:
    def __init__(self, name, email, teacher_id, subject):
        self.name = name
        self.email = email
        self.teacher_id = teacher_id
        self.subject = subject

class Parent:
    def __init__(self, name, email, parent_id, child_name, child_grade):
        self.name = name
        self.email = email
        self.parent_id = parent_id
        self.child_name = child_name
        self.child_grade = child_grade

class Quiz:
    def __init__(self, title, description, questions, answers, due_date):
        self.title = title
        self.description = description
        self.questions = questions
        self.answers = answers
        self.due_date = due_date
        self.participants = []
        self.is_submitted = False

    def add_participant(self, participant):
        self.participants.append(participant)

    def submit_answers(self, participant, answers):
        if participant not in self.participants:
            raise ValueError(f"Participant {participant} is not a participant of quiz {self.title}.")

        self.is_submitted = True
        participant.answers = answers

class QuizManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.parents = []
        self.quizzes = []

    def create_quiz(self, title, description, questions, answers, due_date):
        quiz = Quiz(title, description, questions, answers, due_date)
        self.quizzes.append(quiz)
        return quiz

    def invite_participants(self, email_addresses):
        for email_address in email_addresses:
            participant = None
            for student in self.students:
                if student.email == email_address:
                    participant = student
                    break
            for teacher in self.teachers:
                if teacher.email == email_address:
                    participant = teacher
                    break
            for parent in self.parents:
                if parent.email == email_address:
                    participant = parent
                    break
            if participant is not None:
                participant.quizzes.append(quiz)

    def enable_quiz_submissions(self):
        for quiz in self.quizzes:
            quiz.is_submitted = False

    def retrieve_quiz_results(self):
        quiz_results = []
        for quiz in self.quizzes:
            if quiz.is_submitted:
                results = {}
                for participant in quiz.participants:
                    correct_answers = 0
                    for question, answer in zip(quiz.questions, quiz.answers):
                        if participant.answer_question(question) == answer:
                            correct_answers += 1
                    results[participant.name] = correct_answers
                quiz_results.append(results)
        return quiz_results


if __name__ == "__main__":
    quiz_management_system = QuizManagementSystem()

    quiz = quiz_management_system.create_quiz(
        title="Math Quiz",
        description="A quiz about math concepts",
        questions=["What is 2 + 2?", "What is the square root of 16?", "What is the answer to 6 x 7?"],
        answers=["4", "4", "42"],
        due_date="2023-08-01",
    )

    quiz_management_system.invite_participants(["student1@email.com", "student2@email.com"])

    quiz_management_system.enable_quiz_submissions()

    print("The quiz is now enabled. Participants can start taking the quiz.")
