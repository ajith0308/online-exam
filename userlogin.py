from threading import *
import datetime
from tkinter import *
from tkcalendar import *
from functools import partial
from db import db

#import  screen
root = Tk()

def get_value():


    c=str(cal.get_date())

    return  c


def newfram():
    #root=Tk()
    obj2 = App(root)
    #obj2.start()
    #obj2.start()




def click(username,self):
        s = username.get()
        x=get_value()
        print("usernmae",s)
        print("dob",x)

        z=db(s,x)
        #destory the inner frame
        #self.frame1.destroy()


        #root.destroy()
        if(z==0):
            print("no user found")
        else:
            self.frame1.destroy()
            newfram()






class Register(Thread):

    def __init__(self, root):

        username = StringVar()
        self.root = root
        self.root.title("Login")
        self.root.attributes('-fullscreen',True)
        self.root.configure(bg='#B6FCD5')

        self.frame1 = Frame(self.root, bg='white')
        self.frame1.place(x=500, y=50, width=800, height=600)

        tile = Label(self.frame1, text="Login", font=('time new roman', 20, 'bold'), bg='white', fg='Green').place(x=350,
                                                                                                              y=20)

        login = Label(self.frame1, text="Roll number", font=('time new roman', 15), bg='white', fg='Black').place(x=10,
                                                                                                                  y=100)
        rool_num = Entry(self.frame1, textvariable=username, font=("times new roman", 10), bg='white', fg='gray').place(
            x=150, y=108)

        dob = Label(self.frame1, text="DOB", font=('time new roman', 15), bg='white', fg='Black').place(x=10, y=140)


        clk = partial(click, username,self)

        go = Button(self.frame1, text='go', command=clk).place(x=220, y=180, height=25, width=50)




from tkinter import *
from cv2 import cv2
from PIL import Image, ImageTk



def test():
    print("exam ")
    root.destroy()
    import permision



class App(Thread):
    def __init__(self,root, video_source=0):

        self.root=root
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="#B6FCD5")
        self.video_source = video_source

        self.vid = MyVideoCapture(self.video_source)

        self.canvas = Canvas(self.root, width=root.winfo_screenwidth()/2, height=root.winfo_screenheight()/2)
        self.canvas.place(x=400,y=100)

        self.canvas.btn_snapshot = Button(self.canvas, text="Snapshot", width=30, bg='goldenrod2', activebackground='red',
                                   command=self.snapshot).place(x=100,y=self.vid.height-100)

        self.canvas.btn_next = Button(self.canvas, text="NEXT", width=30, bg='goldenrod2', activebackground='red',
                               command=self.next).place(x=350,y=self.vid.height-100)


        self.update()

        self.root.mainloop()

    def snapshot(self):

        check, frame = self.vid.getFrame()
        if check:
            image = "image.jpg"
            cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            msg = Label(self.root, text='image Captured ' + image, bg='black', fg='green').place(x=430, y=510)


    def update(self):

        isTrue, frame = self.vid.getFrame()

        if isTrue:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.root.after(15, self.update)


    def next(self):
        self.vid.__del__()

       # import face_recognition

        #picture_of_me = face_recognition.load_image_file("image.jpg")
        #my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]


        #unknown_picture = face_recognition.load_image_file("imag1.jpg")
       # unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        # Now we can see the two face encodings are of the same person with `compare_faces`!

       # results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
        #if results[0]==True:
         #   test()
        #else:
        test()
           # newfram()
            
            
            



class MyVideoCapture:
    def __init__(self, video_source=0):


        self.vid = cv2.VideoCapture(video_source)
        #self.vidocode=cv2.VideoWriter_fourcc(*'XVID')

        if not self.vid.isOpened():
            raise ValueError("unable to open this camera \n select another video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def getFrame(self, isTrue=None):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue:

                return (isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (isTrue, None)
        else:
            return (isTrue, None)

    def __del__(self):
        x=self.vid
        if x.isOpened():
            self.vid.release()







#root.overrideredirect(True)
#root.overrideredirect(False)
root.attributes('-fullscreen',True)
obj = Register(root)
today = datetime.date.today()
mindate = datetime.date(year=1999, month=1, day=1)
maxdate = today
cal = DateEntry(obj.frame1, width=18, background='blue',mindate=mindate,maxdate=maxdate,
                foreground='white', borderwidth=4)
cal.place(x=150,y=150)


root.mainloop()
#root.configure()
del obj
del MyVideoCapture
del App


#obj2=App(root)


