import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer the following questions. Let's see how well you know the subject.")
    def present_question(self, question):
        print("\nQuestion:")
        print(question['text'])

        if question['type'] == 'multiple-choice':
            self.present_multiple_choice(question['options'])
        elif question['type'] == 'fill-in-the-blank':
            self.present_fill_in_the_blank()
    def present_multiple_choice(self, options):
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        user_answer = input("Enter the number of your answer: ")
        self.check_answer(int(user_answer) - 1)
    def present_fill_in_the_blank(self):
        user_answer = input("Enter your answer: ")
        self.check_answer(user_answer)
    def check_answer(self, user_answer):
        correct_answer = self.current_question['answer']
        if user_answer == correct_answer:
            print("Correct! Well done!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
    def display_final_results(self):
        print("\nQuiz Completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Congratulations! You got all the questions right!")
        elif self.score >= len(self.questions) / 2:
            print("Good job! You did well.")
        else:
            print("Keep practicing. You can do better!")
    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower() == 'yes'
def main():
    questions = [
        {
            'text': 'What is the capital of France?',
            'type': 'multiple-choice',
            'options': ['Paris', 'London', 'Berlin'],
            'answer': 0
        },
        {
            'text': 'Who wrote "Romeo and Juliet"?',
            'type': 'fill-in-the-blank',
            'answer': 'Shakespeare'
        },
    ]
    quiz = Quiz(questions)
    while True:
        quiz.display_welcome_message()
        for question in questions:
            quiz.current_question = question
            quiz.present_question(question)
        quiz.display_final_results()
        if not quiz.play_again():
            break
if __name__ == "__main__":
    main()
