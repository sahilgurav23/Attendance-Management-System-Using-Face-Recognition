from tkinter import *  # for GUI purpose
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # for image editing
from tkinter import messagebox
from pymongo.mongo_client import MongoClient
import cv2                                # ML algorithum


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # window size geometry(width,height,x-axis,y-axis)
        self.root.title("Face Recognition System")

        # Title
        title_lb1 = Label(self.root, text="Developer", font=("times new roman", 35, "bold"), bg="white",fg="blue")  # Title
        title_lb1.place(x=0, y=0, width=1530, height=55)

        img_top = Image.open("Images/dev.jpg")  # Set Image Path
        img_top = img_top.resize((1530, 750))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg_top = ImageTk.PhotoImage(img_top)  # set image

        lb_img = Label(self.root, image=self.photoimg_top)
        lb_img.place(x=0, y=55, width=1530, height=750)  # image show on window place(x_axis,y_axis)

        # frame
        main_frame = Frame(lb_img, bd=2, bg="white")
        main_frame.place(x=900, y=10, width=560, height=250)

        # 1st
        lbl1 = Label(main_frame, text="Name : sahil shrikrushna gurav ", font=("verdana", 20, "bold"), bg="white")
        lbl1.place(x=0, y=20)

        # 2nd
        lbl2 = Label(main_frame, text="Name : Durgesh Narendra Chirmade ", font=("verdana", 20, "bold"), bg="white")
        lbl2.place(x=0, y=90)

        # 3rd
        lbl3 = Label(main_frame, text="Name : Kiran jagannath Padole ", font=("verdana", 20, "bold"), bg="white")
        lbl3.place(x=0, y=160)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()