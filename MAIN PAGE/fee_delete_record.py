from tkinter import *
from datetime import date
from tkinter.ttk import Combobox


def feedel():

    def clear_data():
        from_.set("")
        to_.set("")
        submitter_.set("")
        amount_.set("")
        id_.set("")
        class_.set("")
        year_.set("")
        fid_.set("")

    def search_data(_year_,_class_,_fid_):
        import db_fee_handler as db_rh
        response=db_rh.fee.search_by_fid(_year_,_class_,_fid_)
        if response=="F" or response is None:
            import conformation as cnfd
            cnfd.confomation.warning_alart(" DATA NOT FOUND !")
            clear_data()
            fdelrw.tkraise()
        else:
            id_.set(response[1])
            submitter_.set(response[2])
            from_.set(response[3])
            to_.set(response[4])
            amount_.set(response[5])
            
            

    def delete_f_rec(_year_,_class_,_fid_):
        import conformation as cnf
        msg=F"""
    YEAR : {_year_}   
    CLASS : {_class_}
    ID : {id_entry.get()}
    FROM  : {_from_entry.get()}    
    TO  : {_to_entry.get()}
    SUBMITTED BY : {submitted_by_entry.get()}
    AMOUNT : {amount_entry.get()}
    FID : {_fid_}

    WOULD YOU LIKE TO PROCEED TO DELETE THESE DATA FROM DATABASE ???
    """
        ans=cnf.confomation.info_conformation(msg)
        if ans is True:
            import db_fee_handler as dbrh
            res=dbrh.fee.delete_record(_year_,_class_,_fid_)
            if res is None or res=="F":
                cnf.confomation.warning_alart(F"""OOPs ! SOMETHING WENT WRONG !
                DATA IS NOT DELETED !""")
                fdelrw.tkraise()
            else:
                cnf.confomation.info_show(F"""CONGRATULATIONS !
                FEE DATA DELETED SUCCESSFULLY !""")
                clear_data()
                fdelrw.tkraise()
                



    fdelrw=Toplevel()
    fdelrw.title("HCS\main page\fee\delete payment record window..")
    fdelrw.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    fdelrw.geometry(F"{fdelrw.winfo_screenwidth()}x{fdelrw.winfo_screenheight()}+0+0")
    fdelrw.tk_focusFollowsMouse()

    #============================== variables ==================================#
    from_=StringVar()
    to_=StringVar()
    submitter_=StringVar()
    amount_=StringVar()
    id_=StringVar()
    fid_=StringVar()
    class_=StringVar()
    year_=StringVar()

    #============================== 888888888888888888888 ==================================#
    title_frame=Frame(fdelrw)
    title=Label(title_frame,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    title.pack()
    
    date_label=Label(title_frame,font=('arial',20,'bold'),fg='dark red',text=date.today())
    date_label.pack(pady=10)


    title_frame.pack()
    
    Label(fdelrw,text="  *** FEE RECORD DELETE WINDOW *** ",fg='dark red',bg='yellow',font=('arial',17,'bold')).pack()

    Label(fdelrw,text="  *** Intense care required while filling/selecting each field ! *** ",fg='dark red',bg='yellow',font=('arial',17,'bold')).pack()

    d_frame=Frame(fdelrw)

    year=Label(d_frame,font=('arial',20,'bold'),text='YEAR :',fg='dark green')
    year.grid(column=0,row=0)
    years=['2020','2021','2022']
    year_entry=Combobox(d_frame,values=years,font=('arial',20,'bold'),width=5,state="readonly",textvariable=year_)
    year_entry.grid(column=1,row=0)

    _class=Label(d_frame,font=('arial',20,'bold'),text='CLASS :',fg='dark green')
    _class.grid(column=2,row=0)
    classes=['LKG','UKG','01','02','03','04','05','06','07','08','09','10']
    _class_entry=Combobox(d_frame,values=classes,font=('arial',20,'bold'),width=5,state="readonly",height=8,textvariable=class_)
    _class_entry.grid(column=3,row=0)

    fid=Label(d_frame,font=('arial',20,'bold'),text='FID :',fg='dark green')
    fid.grid(column=0,row=1)
    fid_entry=Entry(d_frame,font=('arial',20,'bold'),fg='black',width=21,textvariable=fid_)
    fid_entry.grid(column=1,row=1,columnspan=2)


    search=Button(d_frame,text=" SEARCH",fg='dark red',bg='yellow',font=('arial',15,'bold'),command=lambda:search_data(year_entry.get(),_class_entry.get(),fid_entry.get()))
    search.grid(column=3,row=1,padx=10,pady=10)

    d_frame.pack(pady=20)

    detailframe=LabelFrame(fdelrw,padx=100,pady=10,text="** RESULT DISPLAY AREA **",fg="dark red",font=('arial',12,'bold'),bd=10)

    id=Label(detailframe,font=('arial',20,'bold'),text='ID :',fg='dark green')
    id.grid(column=0,row=0)
    id_entry=Entry(detailframe,font=('arial',20,'bold'),width=10,state='readonly',textvariable=id_)
    id_entry.grid(column=1,row=0)

    _from=Label(detailframe,font=('arial',20,'bold'),text='FROM MONTH :',fg='dark green')
    _from.grid(column=0,row=0)
    _from_entry=Entry(detailframe,font=('arial',20,'bold'),width=10,state='readonly',textvariable=from_)
    _from_entry.grid(column=1,row=0)

    _to=Label(detailframe,font=('arial',20,'bold'),text='TO MONTH :',fg='dark green')
    _to.grid(column=0,row=1)
    _to_entry=Entry(detailframe,font=('arial',20,'bold'),width=10,state='readonly',textvariable=to_)
    _to_entry.grid(column=1,row=1)

    submitted_by=Label(detailframe,font=('arial',20,'bold'),text='SUBMITTED BY :',fg='dark green')
    submitted_by.grid(column=0,row=2)
    submitted_by_entry=Entry(detailframe,font=('arial',20,'bold'),width=10,state='readonly',textvariable=submitter_)
    submitted_by_entry.grid(column=1,row=2)

    amount=Label(detailframe,font=('arial',20,'bold'),text='AMOUNT :',fg='dark green')
    amount.grid(column=0,row=3)
    amount_entry=Entry(detailframe,font=('arial',20,'bold'),state='readonly',fg='black',width=10,textvariable=amount_)
    amount_entry.grid(column=1,row=3)

    detailframe.pack()

    button_frame=Frame(fdelrw)
    delete=Button(button_frame,text="DELETE RECORD",font=('arial',25,'bold'),fg='dark red',bg='yellow',bd=5,command=lambda:delete_f_rec(year_entry.get(),_class_entry.get(),fid_entry.get()))
    delete.grid(row=0,column=0)

    reset=Button(button_frame,text="CLEAR",font=('arial',25,'bold'),fg='dark red',bg='yellow',bd=5,command=clear_data)
    reset.grid(row=0,column=1,padx=10)
    button_frame.pack(pady=20)

    contactframe=Frame(fdelrw)

    copyrightlabel=Label(contactframe,font=('arial',10,'bold'),bg='yellow',fg='dark red',text="""   arr. @ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
    copyrightlabel.pack(pady=5)
    contactframe.pack()
  


  
