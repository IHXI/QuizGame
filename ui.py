from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
NUM = 0

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.question_number = 1
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg= THEME_COLOR, pady= 20, padx= 20)

        self.score= Label(text="score = 0", bg= THEME_COLOR, fg="white")
        self.score.grid(column= 1, row= 0)


        self.photoX = PhotoImage(file= "./images/false.png")
        self.photo_true = PhotoImage(file= "./images/true.png")

        self.buttonX = Button(image=self.photoX, highlightthickness= 0, command= self.wrong)
        self.buttonX.grid(column=1, row=2)
        self.button_true = Button(image=self.photo_true, highlightthickness= 0, command= self.right)
        self.button_true.grid(column= 0, row= 2)

        self.canvas = Canvas(height=250, width=300, bg= "white")
        self.question_text = self.canvas.create_text(150, 125, text="ko", font= ("Ariel", 20, "italic"), fill= THEME_COLOR, width= 280)
        self.canvas.grid(column= 0, row= 1, columnspan=2, pady= 50)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text= q_text)

    def right(self):
        global NUM
        check = self.quiz.check_answer("True")
        if check:
            NUM +=1
            self.score.config(text=f"score = {NUM}")
            self.canvas.config(bg= "Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(500, self.quiz_end)

    def wrong(self):
        global NUM
        check = self.quiz.check_answer("True")
        if check:
            NUM += 1
            self.score.config(text=f"score = {NUM}")
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(500, self.quiz_end)

    def quiz_end(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.get_next_question()
            self.question_number += 1
        else:
            self.buttonX.config(state="disabled")
            self.button_true.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text= f"You've completed the quiz."
                                                             f"\nYour final score was: {NUM}/{self.question_number}")
