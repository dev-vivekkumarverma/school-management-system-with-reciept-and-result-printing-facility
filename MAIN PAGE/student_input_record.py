from tkinter import *
from datetime import date
from tkinter.ttk import Combobox

def inputstudentdata():


    def clear_data():
        name_.set("")
        roll_.set("")
        dob_.set("")
        fn_.set("")
        phone_.set("")
        idm_.set("")

    def input_data(year,_class,id,name,roll,dob,f_n,phone,id_mark):
        import conformation as cnf
        msg=f"""
        YEAR:{year}   ID:{id}
        CLASS:{_class}

        NAME  : {name}    
        ROLL  : {roll}
        DOB   : {dob}
        FATHER N.: {f_n}
        PHONE  : {phone}
        ID MARK: {id_mark}
        
        
        WOULD YPU LIKE THIS DATA TO BE STORED IN DATABASE ??????
        """
        a=cnf.confomation.info_conformation(msg)
        if a is True:
            import db_studentdata_handler as std_d_hnd
            ans=std_d_hnd.student.registration(year,_class,id,name,roll,dob,f_n,phone,id_mark)
            if ans=="T":
                cnf.confomation.info_show(F"CONGRATULATIONS ! {name}  is SUCCESSFULLY  REGISTERED !")
                clear_data()
                stdinpw.tkraise()
            else:
                cnf.confomation.warning_alart("OOPs !  SOMETHING WENT WRONG !")
                stdinpw.tkraise()


    stdinpw=Toplevel()
    stdinpw.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    stdinpw.title("HCS\main page..\student \data entry window..")
    stdinpw.geometry(F"{stdinpw.winfo_screenwidth()}x{stdinpw.winfo_screenheight()}+0+0")
    stdinpw.tk_focusFollowsMouse()
    #============variables================#
    name_=StringVar()
    roll_=StringVar()
    dob_=StringVar()
    fn_=StringVar()
    phone_=StringVar()
    idm_=StringVar() 
    choice=StringVar()
    #============variables================#
    titleframe=Frame(stdinpw)

    schooltitle=Label(titleframe,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    schooltitle.pack()
    date_l=Label(titleframe,text=date.today(),fg='red',bg='yellow',font=('arial',17,'bold'))
    date_l.pack(pady=10)
    titleframe.pack(pady=10)
    Label(stdinpw,text="  *** STUDENT DATA INPUT WINDOW *** ",fg='dark red',bg='yellow',font=('arial',17,'bold')).pack(pady=5)
    Label(stdinpw,text="  *** Intense care required while filling/selecting each field ! *** ",fg='red',bg='yellow',font=('arial',17,'bold')).pack()

    choose_frame=Frame(stdinpw)

    year=Label(choose_frame,text='Year :',font=('arial',20,'bold'),fg='green')
    year.grid(row=0,column=0)
    years=['2020','2021','2022']
    year_entry=Combobox(choose_frame,values=years,font=('arial',20,'bold'),width=5,state="readonly",height=12)
    year_entry.grid(row=0,column=1)

    _class=Label(choose_frame,text='Class :',font=('arial',20,'bold'),fg='green')
    _class.grid(row=0,column=2)
    classes=['LKG','UKG','01','02','03','04','05','06','07','08','09','10']
    _class_entry=Combobox(choose_frame,values=classes,font=('arial',20,'bold'),width=5,state="readonly",height=12)
    _class_entry.grid(row=0,column=3)

    id=Label(choose_frame,text='ID :',font=('arial',20,'bold'),fg='green')
    id.grid(row=1,column=0)
    id_entry=Entry(choose_frame,font=('arial',20,'bold'),fg='Black')
    id_entry.grid(row=1,column=1)
    
    choose_frame.pack(pady=10)
    s_detail_f=Frame(stdinpw)

    name=Label(s_detail_f,text='Name :',font=('arial',20,'bold'),fg='green')
    name.grid(row=2,column=0)
    name_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',textvariable=name_)
    name_entry.grid(row=2,column=1)


    roll=Label(s_detail_f,text='Roll :',font=('arial',20,'bold'),fg='green')
    roll.grid(row=3,column=0)
    roll_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',textvariable=roll_)
    roll_entry.grid(row=3,column=1)

    dob=Label(s_detail_f,text='Date Of Birth  :',font=('arial',20,'bold'),fg='green')
    dob.grid(row=4,column=0)
    dob_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',textvariable=dob_)
    dob_entry.grid(row=4,column=1)

    fn=Label(s_detail_f,text="Father's Name :",font=('arial',20,'bold'),fg='green')
    fn.grid(row=5,column=0)
    fn_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',textvariable=fn_)
    fn_entry.grid(row=5,column=1)

    phone=Label(s_detail_f,text='Phone :',font=('arial',20,'bold'),fg='green')
    phone.grid(row=6,column=0)
    phone_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',textvariable=phone_)
    phone_entry.grid(row=6,column=1)

    id_mark=Label(s_detail_f,text='ID MARK :',font=('arial',20,'bold'),fg='green')
    id_mark.grid(row=7,column=0)
    id_mark_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',textvariable=idm_)
    id_mark_entry.grid(row=7,column=1)



    s_detail_f.pack()

    buttonframe=Frame(stdinpw)

    input_=Button(buttonframe,font=('arial',20,'bold'),fg='red',bg='yellow',bd=5,text="INPUT DATA",command=lambda:input_data(year_entry.get(),_class_entry.get(),id_entry.get(),name_entry.get(),roll_entry.get(),dob_entry.get(),fn_entry.get(),phone_entry.get(),id_mark_entry.get()))
    input_.grid(row=0,column=1,padx=10)
    clear=Button(buttonframe,font=('arial',20,'bold'),fg='red',bg='yellow',bd=5,text="CLEAR DATA",command=clear_data)
    clear.grid(row=0,column=2,padx=10)

    buttonframe.pack(pady=10)

    copyrightlabel=Label(stdinpw,font=('arial',8,'bold'),bg='yellow',fg='red',text="""   arr. @ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
    copyrightlabel.pack(pady=5)

    



  

