from functools import partial
from subprocess import Popen
   #import  time
p=Popen('python screen.py')
# Python program to create a simple GUI
# Simple Quiz using Tkinter
import tkinter as tk
from time import sleep

from tkinter import *
from threading import *
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

#import json to use json file for data
import json
#import time
#from tkinter import messagebox


#class to define the components of the GUI
class Quiz(tk.Tk,Thread):

    # videofram=Frame(master=frame2,width=120,height=120,bg="white").place(x=1100,y=140)

    # pack(side=TOP,anchor=NE)

    # set the title of the Window

    # get the data from the json file

    # create an object of the Quiz Class.

    # This is the first method which is called when a
    # new object of the class is initialized. This method
    # sets the question count to 0. and initialize all the
    # other methoods to display the content and make all the
    # functionalities available
    def __init__(self):



        with open('data.json') as f:
            data = json.load(f)

            # set the question, options, and answer
        self.question = (data['question'])
        self.options = (data['options'])
        self.answer = (data['answer'])

        tk.Tk.__init__(self)
        self.attributes('-fullscreen', True)
        self.frame1 = Frame(master=self, width=200, height=60, bg="red")
        self.frame1.pack(fill=BOTH, side=LEFT)
        self.frame2 = Frame(master=self, width=400)
        self.frame2.pack(fill=BOTH, side=LEFT, expand=True)
        self.frame3 = Frame(master=self, width=60, height=50, bg="white").place(x=1200, y=50)

        self.label = Label(self.frame3, text="",bg="white")

        self.label.place(x=1220,y=60)
        self.remaining = 0
        #timer
        self.countdown(120)

        # set question number to 0
        self.q_no=0

        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()

        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected=IntVar()

        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts=self.radio_buttons()

        # display options for the current question
        self.display_options()

        # displays the button for next and exit.
        self.buttons()

        # no of questions
        self.data_size=len(self.question)

        # keep a counter of correct answers
        self.correct=0
        # Define the codec and create VideoWriter object
        #from subprocess import Popen

        #self.p = Popen('python videorecording.py')

        self.mainloop()
    # This method is used to display the result
    # It counts the number of correct and wrong answers
    # and then display them at the end as a message Box
    #un used


    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
            sleep(0.2)
            self.display_result()

            self.destroy()

        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

    def display_result(self):

        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):

        # checks for if the selected option is correct
        if self.opt_selected.get() == self.answer[q_no]:
            # if the option is correct it return true
            return True
    def display_options1(self,qno):
        val=0

        # deselecting the options
        #self.opt_selected.set(0)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.options[qno]:
            self.opts[val]['text']=option
            val+=1

    def display_question1(self,qno):
        print("display qn")
        # setting the Quetion properties
        q_no = Label(self.frame2, text=self.question[qno], width=60,
                     font=('ariel', 16, 'bold'), anchor='w')


        # placing the option on the screen
        q_no.place(x=70, y=100)

    def quest(self,q_no):
        print(q_no)
        self.display_question1(q_no)
        self.display_options1(q_no)


    # This method is used to check the answer of the
    # current question by calling the check_ans and question no.
    # if the question is correct it increases the count by 1
    # and then increase the question number by 1. If it is last
    # question then it calls display result to show the message box.
    # otherwise shows next question.
    def next_btn(self):

        # Check if the answer is correct
        if self.check_ans(self.q_no):

            # if the answer is correct it increments the correct by 1
            self.correct += 1

        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1

        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:

            # if it is correct then it displays the score
            self.display_result()

            # destroys the GUI

        else:
            # shows the next question
            self.display_question()
            self.display_options()



    def prev_btn(self):

        # Check if the answer is correct

            # if the answer is correct it increments the correct by 1

        # Moves to next Question by incrementing the q_no counter
        if self.q_no==0:print("no move")
        elif self.q_no>=1:self.q_no -= 1
        self.display_question()
        self.display_options()



    # This method shows the two buttons on the screen.
    # The first one is the next_button which moves to next question
    # It has properties like what text it shows the functionality,
    # size, color, and property of text displayed on button. Then it
    # mentions where to place the button on the screen. The second
    # button is the exit button which is used to close the GUI without
    # completing the quiz.
    def buttons(self):

        # The first button is the Next button to move to the
        # next Question
        next_button = Button(self.frame2, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))

        # palcing the button on the screen
        next_button.place(x=750,y=600)

        prev_button = Button(self.frame2, text="Prev",command=self.prev_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))

        # palcing the button on the screen
        prev_button.place(x=50,y=600)
        q1=0
        a =len(self.question)


        #question
        for i in range(a):
                clk = partial(self.quest,q1)
                q = Button(self.frame1, text=q1+1, command=clk, width=5, bg="blue", fg="white", font=("ariel",10, "bold")).pack()
                q1+=1




        # This is the second button which is used to Quit the GUI
        #quit_button = Button(frame2, text="Quit", command=frame2.destroy,
        #width=5,bg="black", fg="white",font=("ariel",16," bold"))

        # placing the Quit button on the screen
        #quit_button.place(x=700,y=50)


    # This method deselect the radio button on the screen
    # Then it is used to display the options available for the current
    # question which we obtain through the question number and Updates
    # each of the options for the current question of the radio button.
    def display_options(self):
        val=0

        # deselecting the options
        self.opt_selected.set(0)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.options[self.q_no]:
            self.opts[val]['text']=option
            val+=1


    # This method shows the current Question on the screen
    def display_question(self):

        # setting the Quetion properties
        q_no = Label(self.frame2, text=self.question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )

        #placing the option on the screen
        q_no.place(x=70, y=100)


    # This method is used to Display Title
    def display_title(self):

        # The title to be shown
        title = Label(self.frame2, text="QUIZ",
        width=100, bg="green",fg="white", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)



    def radio_buttons(self):

        # initialize the list with an empty list of options
        q_list = []

        # position of the first option
        y_pos = 150

        # adding the options to the list
        while len(q_list) < 4:

            # setting the radio button properties
            radio_btn = Radiobutton(self.frame2,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))

            # adding the button to the list
            q_list.append(radio_btn)

            # placing the button
            radio_btn.place(x = 100, y = y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return q_list




# END OF THE PROGRAM
quiz = Quiz()
print("main kill")
p.kill()


