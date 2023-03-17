from tkinter import *
from datetime import date
from tkinter.ttk import Combobox

def enquirystudentdata():
    def search_data(x,y,z):
        import db_studentdata_handler as std_d_h
        response=std_d_h.student.data_fetch(x,y,z)
        if response=="F" or response is None:
            import conformation as cnf
            cnf.confomation.warning_alart("DATA NOT FOUND") 
            stdenqw.tkraise()
        else:
            name_.set(response[1])
            roll_.set(response[2])
            dob_.set(response[3])
            fn_.set(response[4])
            phone_.set(response[5])
            idm_.set(response[6])
            


    def clear_data():
        name_.set("")
        roll_.set("")
        dob_.set("")
        fn_.set("")
        phone_.set("")
        idm_.set("")
    
    def Print(filename,data):
        import os
        import tempfile
        _file=tempfile.mktemp(f'{filename}.txt')
        open(_file,'w').write(data) 
        os.startfile(_file,"print")
        

    def prnt():
        
        msg=f"""HOLY CHILD SCHOOL,Toluvi Village
            Dimapur, Nagaland
        ******** STUDENT DATA ********
        YEAR:{year_entry.get()}   ID:{id_entry.get()}
            CLASS:{_class_entry.get()}

    NAME  : {name_entry.get()}    
    ROLL  : {roll_entry.get()}
    DOB   : {dob_entry.get()}
    FATHER N.: {fn_entry.get()}
    PHONE  : {phone_entry.get()}
    ID MARK: {id_mark_entry.get()}
        
    **vivekkumarverma332@gmail.com**
    """
        x=f"ID_{id_entry.get()}"
        Print(x,msg)
        clear_data()
        stdenqw.tkraise()
        
    

    stdenqw=Toplevel()
    stdenqw.title("HCS\main page..\student \data enquiry window..")
    stdenqw.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    stdenqw.geometry(F"{stdenqw.winfo_screenwidth()}x{stdenqw.winfo_screenheight()}+0+0")
    stdenqw.tk_focusFollowsMouse()
    #============variables================#
    name_=StringVar()
    roll_=StringVar()
    dob_=StringVar()
    fn_=StringVar()
    phone_=StringVar()
    idm_=StringVar() 
    #============variables================#
    titleframe=Frame(stdenqw)

    schooltitle=Label(titleframe,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    schooltitle.pack()
    date_l=Label(titleframe,text=date.today(),fg='red',bg='yellow',font=('arial',17,'bold'))
    date_l.pack(pady=10)
    titleframe.pack(pady=10)
    Label(stdenqw,text="  *** STUDENT DATA ENQUIRY WINDOW *** ",fg='dark red',bg='yellow',font=('arial',17,'bold')).pack(pady=5)
    Label(stdenqw,text="  *** Intense care required while filling/selecting each field ! *** ",fg='red',bg='yellow',font=('arial',17,'bold')).pack()

    choose_frame=Frame(stdenqw)

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
    print(year_entry.get())
    search=Button(choose_frame,font=('arial',20,'bold'),text=" SEARCH ",bd=5,fg='black',bg='orange',command=lambda:search_data(year_entry.get(),_class_entry.get(),id_entry.get()))
    search.grid(column=2,row=1,padx=10)
    choose_frame.pack(pady=20)

    s_detail_f=Frame(stdenqw)


    name=Label(s_detail_f,text='Name :',font=('arial',20,'bold'),fg='green')
    name.grid(row=2,column=0)
    name_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',state='readonly',textvariable=name_)
    name_entry.grid(row=2,column=1)


    roll=Label(s_detail_f,text='Roll :',font=('arial',20,'bold'),fg='green')
    roll.grid(row=3,column=0)
    roll_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',state='readonly',textvariable=roll_)
    roll_entry.grid(row=3,column=1)

    dob=Label(s_detail_f,text='Date Of Birth  :',font=('arial',20,'bold'),fg='green')
    dob.grid(row=4,column=0)
    dob_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',state='readonly',textvariable=dob_)
    dob_entry.grid(row=4,column=1)

    fn=Label(s_detail_f,text="Father's Name :",font=('arial',20,'bold'),fg='green')
    fn.grid(row=5,column=0)
    fn_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',state='readonly',textvariable=fn_)
    fn_entry.grid(row=5,column=1)

    phone=Label(s_detail_f,text='Phone :',font=('arial',20,'bold'),fg='green')
    phone.grid(row=6,column=0)
    phone_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',state='readonly',textvariable=phone_)
    phone_entry.grid(row=6,column=1)

    id_mark=Label(s_detail_f,text='ID MARK :',font=('arial',20,'bold'),fg='green')
    id_mark.grid(row=7,column=0)
    id_mark_entry=Entry(s_detail_f,font=('arial',20,'bold'),fg='Black',state='readonly',textvariable=idm_)
    id_mark_entry.grid(row=7,column=1)



    s_detail_f.pack()

    buttonframe=Frame(stdenqw)

    print_=Button(buttonframe,font=('arial',25,'bold'),fg='red',bg='yellow',bd=5,text="PRINT DATA",command=prnt)
    print_.grid(row=0,column=0,padx=10)
    clear=Button(buttonframe,font=('arial',25,'bold'),fg='red',bg='yellow',bd=5,text="CLEAR DATA",command=clear_data)
    clear.grid(row=0,column=1,padx=10)

    buttonframe.pack(pady=10)

    copyrightlabel=Label(stdenqw,font=('arial',8,'bold'),bg='yellow',fg='red',text="""   arr. @ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
    copyrightlabel.pack(pady=5)
  

