from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1500x1000+0+0")

        #text variable for taking data from entry fill and combobox
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        #""""""""""""""""""background image"""""""""
        original_image = Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\register.jpg")

        # Resize the background image to match the window dimensions
        resized_image = original_image.resize((1550, 800), resample=Image.LANCZOS)

        # Convert the resized image to PhotoImage
        self.bg = ImageTk.PhotoImage(resized_image)

        # Create a label to display the background image
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #"""""""""""""""""""""""""""""left image"""""""
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\neelkanth.png")
        #now show it on windows
        left_lbl = Label(self.root, image=self.bg1)  # Change self.bg to self.bg1
        left_lbl.place(x=480, y=100, width=300, height=450)  # relation width and height place over whole window
        

        #"""""""""""""""""""""""main frame"""""""""
        frame=Frame(self.root,bg="white")
        frame.place(x=780,y=100,width=400,height=450)
       #register label
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)
        
        #""""""label and entry fill"""""""""""""1st
        fname=Label(frame,text="First Name",font=("times new roman",10,"bold"),bg="white")
        fname.place(x=30,y=90)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",10,"bold"))
        fname_entry.place(x=30,y=110,width=140)

        #""""""label and entry fill"""""""""""""2nd
        l_name=Label(frame,text="Last Name",font=("times new roman",10,"bold"),bg="white")
        l_name.place(x=220,y=90)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",10,"bold"))
        self.txt_lname.place(x=220,y=110,width=160)

        #""""""lbel and entry fill"""""""""""""3rd
        contact= Label(frame, text="Contact No", font=("times new roman", 10, "bold"), bg="white")
        contact.place(x=30, y=140)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 10, "bold"))
        self.txt_contact.place(x=30, y=160, width=140)
        self.txt_contact.insert(0, " Enter Only Numbers")  # Add sample text

        # Bind <FocusIn> event to remove sample text when clicked
        self.txt_contact.bind("<FocusIn>", self.contact_sample_text)


        # Configure entry to accept only numbers
        self.txt_contact.config(validate="key", validatecommand=(self.root.register(self.validate_contact_number), "%P"))
      
         #""""""label and entry fill"""""""""""""5th
        email=Label(frame,text="Email",font=("times new roman",10,"bold"),bg="white")
        email.place(x=220,y=140)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",10,"bold"))
        self.txt_email.place(x=220,y=160,width=160)
        self.txt_email.insert(0, "e.g. abhi@123@gmai.com")  # Add sample text

        # Bind <FocusIn> event to remove sample text when clicked
        self.txt_email.bind("<FocusIn>", self.clear_sample_text)

        #""""""label and entry fill"""""""""""""6th
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",10,"bold"),bg="white")
        security_Q.place(x=30,y=190)
        
        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 10, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your BestFriend Name", "Your Favorite Number", "Your Childhood Name","Your Favorite Food")
        self.combo_security_Q.place(x=30,y=210,width=140)
        self.combo_security_Q.current(0)  
       
          #""""""label and entry fill"""""""""""""7th
        security_A=Label(frame,text="Security Answer",font=("times new roman",10,"bold"),bg="white")
        security_A.place(x=220,y=187)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",10,"bold"))
        self.txt_security.place(x=220,y=205,width=160)

        #    #""""""label and entry fill"""""""""""""8th
        pswd=Label(frame,text="Password",font=("times new roman",10,"bold"),bg="white")
        pswd.place(x=30,y=240)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",10,"bold"))
        self.txt_pswd.place(x=30,y=260,width=140)

        #     #""""""label and entry fill"""""""""""""thth
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",10,"bold"),bg="white")
        confirm_pswd.place(x=220,y=240)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",10,"bold"))
        self.txt_confirm_pswd.place(x=220,y=260,width=160)

        #"""""'Check button"""""""
        self.var_check = IntVar()
        Checkbtn = Checkbutton(frame, text="I Agree Terms and Conditions", font=("times new roman", 10, "bold"), variable=self.var_check, onvalue=1, offvalue=0)
        Checkbtn.place(x=30, y=300)

        
         #""""""""""""REGISTER buttton"""
        register_btn=Button(frame,command=self.register_data,cursor="hand2",text="Register Now",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="Green",activeforeground="white",activebackground="green")
        register_btn.place(x=30,y=350,width=170)    

           #""""""""""""login buttton""""
        login_btn=Button(frame,text="login Now",command=self.return_login,cursor="hand2",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_btn.place(x=220,y=350,width=170)   


        # """"""""""""""""""function declarartion and DATABSE Work""
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Eror","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0: #we are taking 0 instead of empty because we have to work on integer
            messagebox.showerror("Error","Please agree our Terms and Conditions")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),) #getting email
            #taking from db
            my_cursor.execute(query,value)
            row=my_cursor.fetchone() #fetching data from db
            if row !=None:
                messagebox.showerror("Error","Email id already exist,Please try another email")  #avoid duplicate email
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                  self.var_fname.get(),
                                                                                  self.var_lname.get(),
                                                                                  self.var_contact.get(),
                                                                                  self.var_email.get(),
                                                                                  self.var_securityQ.get(),
                                                                                  self.var_securityA.get(),
                                                                                  self.var_pass.get()

                                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered successfully, If You have not seen this Error before 'Email id already exist,Please try another email'")

                
               



               
            
           


    def clear_sample_text(self, event):
        """Clears the sample text when the entry box is clicked."""
        if self.txt_email.get() == "e.g. abhi@123@gmai.com":
            self.var_email.set("")

    def contact_sample_text(self, event):
        """Clears the sample text when the entry box is clicked."""
        if self.txt_contact.get() == " Enter Only Numbers":
            self.var_contact.set("")

    # Function to validate contact number input
    def validate_contact_number(self, input_text):
        if input_text.isdigit() or input_text == "":
            return True
        else:
            return False
    
    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
