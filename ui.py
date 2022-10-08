from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.feedback = 1
        self.final_score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="some question text",
                                                     font=("Arial", 20, "italic"), )

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Courier", 14))
        self.score_label.grid(row=0, column=1, pady=20)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, borderwidth=0, bg=THEME_COLOR, activebackground=THEME_COLOR,
                                   command=self.true)
        self.right_button.grid(row=2, column=0, padx=20, pady=20)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, borderwidth=0, bg=THEME_COLOR, activebackground=THEME_COLOR,
                                   command=self.false)
        self.wrong_button.grid(row=2, column=1, padx=20, pady=20)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\n\n"
                                                            f"Final score:"
                                                            f" {self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true(self):
        answer = self.quiz.check_answer("True")
        self.change_color(answer)
        self.window.after(1000, self.next_question)

    def false(self):
        answer = self.quiz.check_answer("False")
        self.change_color(answer)
        self.window.after(1000, self.next_question)

    def change_color(self, answer: bool):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
