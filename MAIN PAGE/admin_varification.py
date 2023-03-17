from tkinter import *
from datetime import date
from db_admin_handler import adm
import conformation as y

def verifyadmin():
    def verification(username,password):
        a=adm.admin_verification(username,password)
        if(a=='T'):
            b=y.confomation.info_conformation("""WELCOME DEAR ADMIN
            I AM HAPPY TO ASSIST YOU !
                WOULD YOU LIKE TO MOVE FORWORD ?""")
            if b is True:
                return b
        else:
            y.confomation.warning_alart("WRONG ATTEMPT")
            admvarificationpw.destroy()
            
            

    def signup():
        import adminsignup as ad
        ad.SignUP()


    admvarificationpw=Toplevel()
    admvarificationpw.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    admvarificationpw.geometry(F"{admvarificationpw.winfo_screenwidth()}x{admvarificationpw.winfo_screenheight()}+0+0")
    admvarificationpw.title(f'HOLY CHILD SCHOOL/admin/sign in.....       @ {date.today()}')
    admvarificationpw.tk_focusFollowsMouse()
    title_frame=Frame(admvarificationpw)

    title=Label(title_frame,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    title.pack(pady=10)
    date_label=Label(title_frame,font=('arial',20,'bold'),fg='orange',text=f"""{date.today()}

    ADMIN SIGN-UP""")
    date_label.pack()

    title_frame.pack(pady=5)

    dataframe=Frame(admvarificationpw)

    id=Label(dataframe,text="ADMIN-ID :",font=('arial',20,'bold'),fg='green')
    id.grid(column=0,row=0)
    id_entry=Entry(dataframe,font=('arial',20,'bold'),fg='black')
    id_entry.grid(column=1,row=0,pady=5)

    pin=Label(dataframe,text="4-DIGIT PIN :",font=('arial',20,'bold'),fg='green')
    pin.grid(column=0,row=1)
    pin_entry=Entry(dataframe,font=('arial',20,'bold'),fg='black')
    pin_entry.grid(column=1,row=1,pady=5)

    dataframe.pack(pady=40)

    buttonframe=Frame(admvarificationpw)

    sign_in=Button(buttonframe,font=('arial',20,'bold'),fg='blue',bd=5,text='SIGN_IN',bg='yellow',command= lambda:verification(id_entry.get(),pin_entry.get()))
    sign_in.pack()

    buttonframe.pack()
    Label(admvarificationpw,text="don't have an pre-existing account..",bg="yellow",fg="red").pack(pady=30)
    Button(admvarificationpw,text=" sign-up here ",bg="yellow",fg="black",command=signup).pack()

    copyrightlabel=Label(admvarificationpw,font=('arial',8,'bold'),bg='yellow',fg='red',text="""   arr.@ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
    copyrightlabel.pack(pady=20)

