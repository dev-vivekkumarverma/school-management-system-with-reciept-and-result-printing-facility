from tkinter import *
from datetime import date
from tkinter.ttk import Combobox

def updatestudentdata():
    def search_data(x,y,z):

        import db_studentdata_handler as std_d_h
        response=std_d_h.student.data_fetch(x,y,z)
        if response=="F" or response is None:
            import conformation as cnf
            cnf.confomation.warning_alart("DATA NOT FOUND") 
            stddupw.tkraise()
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
        choice.set("")

    def update_data(year,_class,old_id,new_id,name,roll,dob,f_n,phone,id_mark):
        import conformation as cnf
        msg=f"""
        YEAR:{year}   ID:{old_id}
        CLASS:{_class}

        NAME  : {name}    
        ROLL  : {roll}
        DOB   : {dob}
        FATHER N.: {fn}
        PHONE  : {phone}
        ID MARK: {id_mark}
        
        WOULD YPU LIKE THIS DATA TO BE UPDATED TO NEW ID:{new_id}

        ??????
        """
        a=cnf.confomation.info_conformation(msg)
        if a is True:
            import db_studentdata_handler as std_d_hnd
            ans=std_d_hnd.student.update_datails(year,_class,old_id,new_id,name,roll,dob,f_n,phone,id_mark)
            if ans=="T":
                cnf.confomation.info_show("CONGRATULATIONS ! DATA UPDATED SUCCESSFULLY !")
                clear_data()
                stddupw.tkraise()     
            else:
                cnf.confomation.warning_alart("OOPs !  SOMETHING WENT WRONG !")
                stddupw.tkraise()


    stddupw=Toplevel()
    stddupw.geometry(F"{stddupw.winfo_screenwidth()}x{stddupw.winfo_screenheight()}+0+0")
    stddupw.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    stddupw.title("HCS\main page..\student \data correction window..")
    stddupw.tk_focusFollowsMouse()
    #============variables================#
    name_=StringVar()
    roll_=StringVar()
    dob_=StringVar()
    fn_=StringVar()
    phone_=StringVar()
    idm_=StringVar() 
    choice=StringVar()
    #============variables================#
    titleframe=Frame(stddupw)

    schooltitle=Label(titleframe,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    schooltitle.pack()
    date_l=Label(titleframe,text=date.today(),fg='red',bg='yellow',font=('arial',17,'bold'))
    date_l.pack(pady=10)
    titleframe.pack(pady=10)

    Label(stddupw,text="  *** STUDENT DATA CORRECTION WINDOW *** ",fg='dark red',bg='yellow',font=('arial',17,'bold')).pack(pady=5)
    Label(stddupw,text="  *** Intense care required while filling/selecting each field ! *** ",fg='red',bg='yellow',font=('arial',17,'bold')).pack()

    choose_frame=Frame(stddupw)

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

    s_detail_f=Frame(stddupw)

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

    buttonframe=Frame(stddupw)

    id_new=Label(buttonframe,text='NEW ID :',font=('arial',20,'bold'),fg='green')
    id_new.grid(row=0,column=0)
    id_new_entry=Entry(buttonframe,font=('arial',20,'bold'),fg='Black',textvariable=choice)
    id_new_entry.grid(row=0,column=1)
    update_=Button(buttonframe,font=('arial',20,'bold'),fg='red',bg='yellow',bd=5,text="UPDATE DATA",command=lambda:update_data(year_entry.get(),_class_entry.get(),id_entry.get(),id_new_entry.get(),name_entry.get(),roll_entry.get(),dob_entry.get(),fn_entry.get(),phone_entry.get(),id_mark_entry.get()))
    update_.grid(row=0,column=2,padx=10)
    clear=Button(buttonframe,font=('arial',20,'bold'),fg='red',bg='yellow',bd=5,text="CLEAR DATA",command=clear_data)
    clear.grid(row=0,column=3,padx=10)

    buttonframe.pack(pady=10)

    copyrightlabel=Label(stddupw,font=('arial',8,'bold'),bg='yellow',fg='red',text="""   arr. @ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
    copyrightlabel.pack(pady=5)
    



  

