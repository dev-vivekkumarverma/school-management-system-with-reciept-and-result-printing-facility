from tkinter import *
from datetime import date
from tkinter.ttk import Combobox

def feepaymentenquiry():

    def clear_data():
    
        id_.set("")
        class_.set("")
        year_.set("")
        text_area.delete(0,END)
     
    def search_data(y,c,i):
        import db_fee_handler as f_dbh
        anss=f_dbh.fee.enquiry(y,c,i)
        if anss=="F" or anss is None or anss==[]:
            import conformation as cnf
            cnf.confomation.warning_alart(" DATA NOT FOUND !")
            feewo.tkraise()
        else:
            i=0
            for ans in anss:
                text_area.insert(i+1,ans)
            feewo.tkraise()

    
    def Print(filename,data):
        import os
        import tempfile
        _file=tempfile.mktemp(f'{filename}.txt')
        open(_file,'w').write(data) 
        os.startfile(_file,"print")

    def print_data_selected():
        import conformation as conf
        indices=text_area.curselection()
        if indices==():
            conf.confomation.info_show("NO DATA IS SELECTED !")
        else:
            msg=""
            for ind in indices:
                response=text_area.get(ind)
                msg=msg+F"""
    HOLY CHILD SCHOOL,Toluvi Village
             Dimapur, Nagaland
     ***** FEE PAYMENT RECIEPT ******
        YEAR        : {year_entry.get()}   
        ID          : {response[1]}
        CLASS       : {_class_entry.get()}
        FROM        : {response[2]}    
        TO          : {response[3]}
        SUBMITTED BY: {response[4]}
        AMOUNT      : {response[5]}
        FID : {response[0]}       
    
    ****arr:@vksoftwaresolution*****
                """
                x=f"ID_{response[1]}"


            
            Print(x,msg)
            feew.tkraise()
            clear_data()





    feewo=Toplevel()
    feewo.title("HCS\main page\fee\payment enquiry window..")
    feewo.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    feewo.geometry(F"{feewo.winfo_screenwidth()}x{feewo.winfo_screenheight()}+0+0")
    feewo.tk_focusFollowsMouse()
    
    #============================== variables ==================================#
    id_=StringVar()
    class_=StringVar()
    year_=StringVar()

    #============================== 888888888888888888888 ==================================#

    title_frame=Frame(feewo)
    title=Label(title_frame,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    title.pack()
    date_label=Label(title_frame,font=('arial',20,'bold'),fg='red',text=date.today())
    date_label.pack(pady=10)

    
    title_frame.pack()
    Label(feewo,text="  *** FEE ENQUIRY WINDOW *** ",fg='red',bg='yellow',font=('arial',12,'bold')).pack(pady=5)
    Label(feewo,text="  *** Intense care required while filling/selecting each field ! *** ",fg='red',bg='yellow',font=('arial',12,'bold')).pack()

    d_frame=Frame(feewo)

    year=Label(d_frame,font=('arial',20,'bold'),text='Year :',fg='green')
    year.grid(column=0,row=0)
    years=['2020','2021','2022']
    year_entry=Combobox(d_frame,values=years,font=('arial',20,'bold'),width=5,state="readonly",textvariable=year_)
    year_entry.grid(column=1,row=0)

    _class=Label(d_frame,font=('arial',20,'bold'),text='CLASS :',fg='green')
    _class.grid(column=2,row=0)
    classes=['LKG','UKG','01','02','03','04','05','06','07','08','09','10']
    _class_entry=Combobox(d_frame,values=classes,font=('arial',20,'bold'),width=5,state="readonly",height=12,textvariable=class_)
    _class_entry.grid(column=3,row=0)

    id=Label(d_frame,font=('arial',20,'bold'),text='ID :',fg='green')
    id.grid(column=4,row=0)
    id_entry=Entry(d_frame,font=('arial',20,'bold'),fg='black',width=10,textvariable=id_)
    id_entry.grid(column=5,row=0)

    search=Button(d_frame,text=" SEARCH ",font=('arial',15,'bold'),fg='Blue',bg='yellow',bd=5,command=lambda:search_data(year_entry.get(),_class_entry.get(),id_entry.get()))
    search.grid(column=6,row=0,padx=5)

    d_frame.pack()

    output_frame=LabelFrame(feewo,text=f"'-----------FID------------','---- ID ------',-SUBMITTER','--FROM--','----TO----','AMOUNT'",bd=5,fg='dark red',font=('arial',12,'bold'))

    text_area=Listbox(output_frame,font=('arial',12,'bold'),fg='black',height=18,width=70,selectmode=MULTIPLE)
    text_area.pack()

    output_frame.pack(pady=10)

    button_frame=Frame(feewo)

    prints=Button(button_frame,text="PRINT SELECTED ",font=('arial',15,'bold'),bg='yellow',fg='Blue',bd=5,command=print_data_selected)
    prints.grid(column=0,row=0,padx=10)

    clear=Button(button_frame,text=" CLEAR ",font=('arial',15,'bold'),bg='yellow',fg='Blue',bd=5,command=clear_data)
    clear.grid(column=1,row=0,padx=10)

    

    button_frame.pack()
    copyrightlabel=Label(feewo,font=('arial',8,'bold'),bg='yellow',fg='red',text="""   arr. @ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
    copyrightlabel.pack(pady=5)

