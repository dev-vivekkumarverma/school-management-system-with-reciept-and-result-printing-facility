from tkinter import *
from datetime import date
from tkinter.ttk import Combobox


def payfee():

    def clear_data():
        from_.set("")
        to_.set("")
        submitter_.set("")
        amount_.set("")
        id_.set("")
        class_.set("")
        year_.set("")

    def Print(filename,data):
        import os
        import tempfile
        _file=tempfile.mktemp(f'{filename}.txt')
        open(_file,'w').write(data) 
        os.startfile(_file,"print")
        
        
     
    def pay_now(_year_,_class_,_id_,_submitter_,_from_,_to_,_amount_):
        import conformation as cnf
        msg=F"""
    YEAR:{_year_}   
    ID:{_id_}
    CLASS:{_class_}
    FROM  : {_from_}    
    TO  : {_to_}
    SUBMITTED BY : {_submitter_}
    AMOUNT : {_amount_}
    
    ARE THESE DETAILS CORRECT ???
    WOULD YOU LIKE TO PROCEED FURTHER WITH THESE DETAILS ???
    """
        a=cnf.confomation.info_conformation(msg)
        if a is True:
            import db_fee_handler as fdbh_
            ans=fdbh_.fee.submit(_year_,_class_,_id_,_submitter_,_from_,_to_,_amount_)
            if ans=="F":
                cnf.confomation.warning_alart("OOPs ! SOMETHING WENT WRONG , PAYMENT UNSUCCESSFUL !!!")
                feew.tkraise()
            else:
                cnf.confomation.info_show(F""" PAYMENT SUCCESSFUL ! 
                YOUR FID IS {ans}
                COLLECT THE PAYMENT RECIEPT !""")

                msg1=f"""
    HOLY CHILD SCHOOL,Toluvi Village
             Dimapur, Nagaland
     ***** FEE PAYMENT RECIEPT ******
        YEAR        : {year_entry.get()}   
        ID          : {id_entry.get()}
        CLASS       : {_class_entry.get()}
        FROM        : {_from_entry.get()}    
        TO          : {_to_entry.get()}
        SUBMITTED BY: {submitted_by_entry.get()}
        AMOUNT      : {amount_entry.get()}
        FID : {ans}       
    
    ****arr:@vksoftwaresolution*****
                """
                x=f"ID_{id_entry.get()}"
                Print(x,msg1)
                feew.tkraise()
                clear_data()




    feew=Toplevel()
    feew.title("HCS\main page\fee\payment window..")
    feew.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    feew.geometry(F"{feew.winfo_screenwidth()}x{feew.winfo_screenheight()}+0+0")
    feew.tk_focusFollowsMouse()

    #============================== variables ==================================#
    from_=StringVar()
    to_=StringVar()
    submitter_=StringVar()
    amount_=StringVar()
    id_=StringVar()
    class_=StringVar()
    year_=StringVar()

    #============================== 888888888888888888888 ==================================#
    title_frame=Frame(feew)
    title=Label(title_frame,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    title.pack()
    
    date_label=Label(title_frame,font=('arial',20,'bold'),fg='dark red',text=date.today())
    date_label.pack(pady=10)


    title_frame.pack()
    
    Label(feew,text="  *** FEE PAYMENT WINDOW *** ",fg='dark red',bg='yellow',font=('arial',17,'bold')).pack()

    Label(feew,text="  *** Intense care required while filling/selecting each field ! *** ",fg='dark red',bg='yellow',font=('arial',17,'bold')).pack()

    d_frame=Frame(feew)

    year=Label(d_frame,font=('arial',20,'bold'),text='YEAR :',fg='dark green')
    year.grid(column=0,row=0)
    years=['2020','2021','2022']
    year_entry=Combobox(d_frame,values=years,font=('arial',20,'bold'),width=5,state="readonly",textvariable=year_)
    year_entry.grid(column=1,row=0)

    _class=Label(d_frame,font=('arial',20,'bold'),text='CLASS :',fg='dark green')
    _class.grid(column=2,row=0)
    classes=['LKG','UKG','01','02','03','04','05','06','07','08','09','10']
    _class_entry=Combobox(d_frame,values=classes,font=('arial',20,'bold'),width=5,state="readonly",height=12,textvariable=class_)
    _class_entry.grid(column=3,row=0)

    id=Label(d_frame,font=('arial',20,'bold'),text='ID :',fg='dark green')
    id.grid(column=4,row=0)
    id_entry=Entry(d_frame,font=('arial',20,'bold'),fg='black',width=10,textvariable=id_)
    id_entry.grid(column=5,row=0)

    d_frame.pack(pady=20)

    detailframe=Frame(feew)

    months=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']

    _from=Label(detailframe,font=('arial',20,'bold'),text='FROM MONTH :',fg='dark green')
    _from.grid(column=0,row=0)
    _from_entry=Combobox(detailframe,values=months,font=('arial',20,'bold'),width=10,state='readonly',textvariable=from_,height=6)
    _from_entry.grid(column=1,row=0)

    _to=Label(detailframe,font=('arial',20,'bold'),text='TO MONTH :',fg='dark green')
    _to.grid(column=0,row=1)
    _to_entry=Combobox(detailframe,values=months,font=('arial',20,'bold'),width=10,state='readonly',textvariable=to_,height=6)
    _to_entry.grid(column=1,row=1)

    submitted_by=Label(detailframe,font=('arial',20,'bold'),text='SUBMITTED BY :',fg='dark green')
    submitted_by.grid(column=0,row=2)
    submitters=['STUDENT','PARENT','GUARDIAN','OTHERS']
    submitted_by_entry=Combobox(detailframe,values=submitters,font=('arial',20,'bold'),width=10,state='readonly',textvariable=submitter_)
    submitted_by_entry.grid(column=1,row=2)

    amount=Label(detailframe,font=('arial',20,'bold'),text='AMOUNT :',fg='dark green')
    amount.grid(column=0,row=3)
    amount_entry=Entry(detailframe,font=('arial',20,'bold'),fg='black',width=11,textvariable=amount_)
    amount_entry.grid(column=1,row=3)

    detailframe.pack()

    button_frame=Frame(feew)
    pay=Button(button_frame,text="PAY NOW",font=('arial',25,'bold'),fg='dark red',bg='yellow',bd=5,command=lambda:pay_now(year_entry.get(),_class_entry.get(),id_entry.get(),submitted_by_entry.get(),_from_entry.get(),_to_entry.get(),amount_entry.get()))
    pay.grid(row=0,column=0)

    reset=Button(button_frame,text="CLEAR",font=('arial',25,'bold'),fg='dark red',bg='yellow',bd=5,command=clear_data)
    reset.grid(row=0,column=1,padx=10)
    button_frame.pack(pady=50)

    contactframe=Frame(feew)

    copyrightlabel=Label(contactframe,font=('arial',10,'bold'),bg='yellow',fg='dark red',text="""   arr. @ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
    copyrightlabel.pack(pady=5)
    contactframe.pack()

   
  

