from tkinter import *
from datetime import date
from db_admin_handler import adm
import conformation as w


def SignUP():

    def signup(id_,name,adhar_,pin):
        a=adm.admin_signup(id_,name,adhar_,pin)
        if a=="T":
            w.confomation.info_show(f"""
            SIGN UP SUCCESSFULL
            hello mr./mrs., {name} 
            your info
            ID:{id_}
            PIN:{pin}
            """)
            admsupw.destroy()
        else:
            w.confomation.info_show("""OOPs,
                SOMETHING WENT WRONG!
                SIGNUP UNSUCCESSFULL !
                """)
            admsupw.destroy()




    admsupw=Toplevel()
    admsupw.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    admsupw.geometry(F"{admsupw.winfo_screenwidth()}x{admsupw.winfo_screenheight()}+0+0")
    admsupw.title(f'HOLY CHILD SCHOOL/admin/verification/sign up.....       @ {date.today()}')  
    admsupw.tk_focusFollowsMouse()  

    title_frame=Frame(admsupw)
    title=Label(title_frame,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    title.pack()
    date_label=Label(title_frame,font=('arial',20,'bold'),fg='orange',text=f"""{date.today()}
    ADMIN SIGN-UP""")
    date_label.pack(pady=5)
    title_frame.pack()

    dataframe=Frame(admsupw)
    id=Label(dataframe,text="ADMIN-ID :",font=('arial',20,'bold'),fg='green')
    id.grid(column=0,row=0)
    id_entry=Entry(dataframe,font=('arial',20,'bold'),fg='black')
    id_entry.grid(column=1,row=0,pady=5)

    name=Label(dataframe,text="NAME :",font=('arial',20,'bold'),fg='green')
    name.grid(column=0,row=1)
    name_entry=Entry(dataframe,font=('arial',20,'bold'),fg='black')
    name_entry.grid(column=1,row=1,pady=5)

    adhar=Label(dataframe,text="ADHAR NO. :",font=('arial',20,'bold'),fg='green')
    adhar.grid(column=0,row=2)
    adhar_entry=Entry(dataframe,font=('arial',20,'bold'),fg='black')
    adhar_entry.grid(column=1,row=2,pady=5)

    pin=Label(dataframe,text="PIN :",font=('arial',20,'bold'),fg='green')
    pin.grid(column=0,row=3)
    pin_entry=Entry(dataframe,font=('arial',20,'bold'),fg='black')
    pin_entry.grid(column=1,row=3,pady=5)

    dataframe.pack(pady=40)

    button_frame=Frame(admsupw)

    submit=Button(button_frame,font=('arial',20,'bold'),text="Sign-up",bd=5,fg='green',command=lambda:signup(id_entry.get(),name_entry.get(),adhar_entry.get(),pin_entry.get()))
    submit.pack()

    button_frame.pack(pady=50)
    copyrightlabel=Label(admsupw,font=('arial',8,'bold'),bg='yellow',fg='red',text=""" arr. @ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385""")
    copyrightlabel.pack(pady=10)
    

