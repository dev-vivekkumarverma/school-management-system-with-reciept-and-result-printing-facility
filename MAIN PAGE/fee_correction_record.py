from tkinter import *
from datetime import date
from tkinter.ttk import Combobox


def record_correct():
    
    def clear_data():
        from_.set("")
        to_.set("")
        submitter_.set("")
        amount_.set("")
        id_.set("")
        newid_.set("")
        class_.set("")
        year_.set("")
        fid_.set("")


    def Print(filename,data):
        import os
        import tempfile
        _file=tempfile.mktemp(f'{filename}.txt')
        open(_file,'w').write(data) 
        os.startfile(_file,"print")


    def search_data(_year_,_class_,_fid_):
        import db_fee_handler as db_rh
        response=db_rh.fee.search_by_fid(_year_,_class_,_fid_)
        if response=="F" or response is None:
            import conformation as cnfd
            cnfd.confomation.warning_alart(" DATA NOT FOUND !")
            fdcorrw.tkraise()
        else:
            id_.set(response[1])
            submitter_.set(response[2])
            from_.set(response[3])
            to_.set(response[4])
            amount_.set(response[5])


    def update_record(_year_,_class_,_new_id_,_submitter_,_from_,_to_,_amount_,_old_fid_):
        import conformation as cnf
        msg=F"""
    YEAR : {_year_}   
    CLASS : {_class_}
    NEW ID : {_new_id_}
    FROM  : {_from_}    
    TO  : {_to_}
    SUBMITTED BY : {_submitter_}
    AMOUNT : {_amount_}
    OLD ID : {id_entry.get()}
    WOULD YOU LIKE TO PROCEED TO UPDATE THESE RECORD IN PLACE OF 
    FID : {_old_fid_}            ???
        """
        ans=cnf.confomation.info_conformation(msg)
        if ans is True:
            import db_fee_handler as dbrh
            resp=dbrh.fee.correction(_year_,_class_,_new_id_,_submitter_,_from_,_to_,_amount_,_old_fid_)
            if resp=="F" or resp is None:
                cnf.confomation.warning_alart(F""" OPPs ! 
                SOMETHING WENT WRONG ,
                DATA UPDATE IS UNSUCCESSFUL !!!!
                """)
                fdcorrw.tkraise()
            else:
                cnf.confomation.info_show(F""" 
                CONGRATULATIONS ....
                UPDATE SUCCESSFULL !
                COLLECT RECIEPT WITH,
                NEW FID is: {resp}
                """)
                msg1=f"""
    HOLY CHILD SCHOOL,Toluvi Village
             Dimapur, Nagaland
     ***** FEE PAYMENT RECIEPT ******
        YEAR        : {_year_}   
        ID          : {_new_id_}
        CLASS       : {_class_}
        FROM        : {_from_}    
        TO          : {_to_}
        SUBMITTED BY: {_submitter_}
        AMOUNT      : {_amount_}
        FID : {resp}       
    
    ****arr:@vksoftwaresolution*****
                """
                x="ID"+_new_id_
                Print(x,msg1)
                clear_data()
                fdcorrw.tkraise()
                






    fdcorrw=Toplevel()
    fdcorrw.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    fdcorrw.title("HCS\main page\fee\payment correction window..")
    fdcorrw.geometry(F"{fdcorrw.winfo_screenwidth()}x{fdcorrw.winfo_screenheight()}+0+0")
    fdcorrw.tk_focusFollowsMouse()

    #============================== variables ==================================#
    from_=StringVar()
    to_=StringVar()
    submitter_=StringVar()
    amount_=StringVar()
    id_=StringVar()
    class_=StringVar()
    year_=StringVar()
    newid_=StringVar()
    fid_=StringVar()
    #============================== 888888888888888888888 ==================================#
    title_frame=Frame(fdcorrw)
    title=Label(title_frame,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    title.pack()
    
    date_label=Label(title_frame,font=('arial',20,'bold'),fg='dark red',text=date.today())
    date_label.pack(pady=10)


    title_frame.pack()
    
    Label(fdcorrw,text="  *** FEE RECORD CORRECTION WINDOW *** ",fg='dark red',bg='yellow',font=('arial',17,'bold')).pack()

    Label(fdcorrw,text="  *** Intense care required while filling/selecting each field ! *** ",fg='dark red',bg='yellow',font=('arial',17,'bold')).pack(pady=5)

    d_frame=Frame(fdcorrw)

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

    fid=Label(d_frame,font=('arial',20,'bold'),text='FID :',fg='dark green')
    fid.grid(column=0,row=1)
    fid_entry=Entry(d_frame,font=('arial',20,'bold'),fg='black',width=21,textvariable=fid_)
    fid_entry.grid(column=1,row=1,columnspan=2)

    search=Button(d_frame,text="SEARCH",font=('arial',15,'bold'),fg='dark red',bg='yellow',bd=5,command=lambda:search_data(year_entry.get(),_class_entry.get(),fid_entry.get()))
    search.grid(column=3,row=1,padx=10,pady=5)
    d_frame.pack(pady=20)

    detailframe=Frame(fdcorrw)

    months=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']

    id=Label(detailframe,text="ID :",font=('arial',20,'bold'),fg='dark green')
    id.grid(row=0,column=0)
    id_entry=Entry(detailframe,textvariable=id_,font=('arial',20,'bold'),fg='black',width=11)
    id_entry.grid(row=0,column=1,padx=10)

    _from=Label(detailframe,font=('arial',20,'bold'),text='FROM MONTH :',fg='dark green')
    _from.grid(column=0,row=1)
    _from_entry=Combobox(detailframe,values=months,font=('arial',20,'bold'),width=10,state='readonly',textvariable=from_,height=6)
    _from_entry.grid(column=1,row=1)

    _to=Label(detailframe,font=('arial',20,'bold'),text='TO MONTH :',fg='dark green')
    _to.grid(column=0,row=2)
    _to_entry=Combobox(detailframe,values=months,font=('arial',20,'bold'),width=10,state='readonly',textvariable=to_,height=6)
    _to_entry.grid(column=1,row=2)

    submitted_by=Label(detailframe,font=('arial',20,'bold'),text='SUBMITTED BY :',fg='dark green')
    submitted_by.grid(column=0,row=3)
    submitters=['STUDENT','PARENT','GUARDIAN','OTHERS']
    submitted_by_entry=Combobox(detailframe,values=submitters,font=('arial',20,'bold'),width=10,state='readonly',textvariable=submitter_)
    submitted_by_entry.grid(column=1,row=3)

    amount=Label(detailframe,font=('arial',20,'bold'),text='AMOUNT :',fg='dark green')
    amount.grid(column=0,row=4)
    amount_entry=Entry(detailframe,font=('arial',20,'bold'),fg='black',width=11,textvariable=amount_)
    amount_entry.grid(column=1,row=4)

    detailframe.pack()

    button_frame=Frame(fdcorrw)
    
    newid=Label(button_frame,text="NEW ID :",font=('arial',20,'bold'),fg='dark green')
    newid.grid(row=0,column=0)
    newid_entry=Entry(button_frame,textvariable=newid_,font=('arial',20,'bold'),fg='black',width=11)
    newid_entry.grid(row=0,column=1,padx=10)

    update=Button(button_frame,text="UPDATE RECOURD",font=('arial',20,'bold'),fg='dark red',bg='yellow',bd=5,command=lambda:update_record(year_entry.get(),_class_entry.get(),newid_entry.get(),submitted_by_entry.get(),_from_entry.get(),_to_entry.get(),amount_entry.get(),fid_entry.get()))
    update.grid(row=0,column=2)

    reset=Button(button_frame,text="CLEAR",font=('arial',20,'bold'),fg='dark red',bg='yellow',bd=5,command=clear_data)
    reset.grid(row=0,column=3,padx=10)
    button_frame.pack(pady=10)
    
    contactframe=Frame(fdcorrw)

    copyrightlabel=Label(contactframe,font=('arial',10,'bold'),bg='yellow',fg='dark red',text="""   arr. @ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
    copyrightlabel.pack(pady=5)
    contactframe.pack()
    


