from tkinter import *
from datetime import date
from tkinter.ttk import Combobox


def delete_result():
    
    def delresult(year_,exam_,id_):
        import conformation as cnf
        msg=f"""
        YEAR: {year_entry.get()}   
        ID: {id_entry.get()}
        EXAM: {exam_entry.get()}

        ENGLISH           : {e1_marks.get()}    
        MATHEMATICS       : {math_marks.get()}
        SCIENCE           : {sci_marks.get()}
        SOCIAL SCIENCE    : {ss_marks.get()}
        HINDI/EVS         : {hi_evs_marks.get()}
        ENG-2/ALT.ENGLISH : {e2_alte_marks.get()}
        G.K.              : {gk_marks.get()}
        MORAL SCIENCE     : {ms_marks.get()}
        HERITAGE          : {hrtg_marks.get()}
        COMPUTER          : {comp_marks.get()}
        
        WOULD YOU LIKE THIS DATA TO BE DELETED   ???
        
        """
        ans=cnf.confomation.info_conformation(msg)
    
        if ans is True:
            import db_result_handler as t
            resp=t.result.delete_result_(year_,exam_,id_)
    
            if resp=="T":
                cnf.confomation.info_show("CONGRATULATIONS ! DATA IS SUCCESSFULLY DELETED !")
                clear_data()
                rdelw.tkraise()
            else:
                import conformation as cnf
                cnf.confomation.warning_alart(" SOMETHING WENT WRONG !")
                rdelw.tkraise()


    def clear_data():
        e1marks.set("")
        e2_altemarks.set("")
        hi_evsmarks.set("")
        hrtgmarks.set("")
        ssmarks.set("")
        mathmarks.set("")
        scimarks.set("")
        msmarks.set("")
        gkmarks.set("")
        compmarks.set("")
        choice.set("")

    def search_result(x,y,z):
        import db_result_handler as t
        response=t.result.fetch_result(x,y,z)
        if response == "F" or response is None:
            import conformation as cnf
            cnf.confomation.warning_alart(" DATA NOT FOUND !")
            rdelw.tkraise()
        else:
            e1marks.set(response[1])
            mathmarks.set(response[2])
            scimarks.set(response[3])
            ssmarks.set(response[4])
            hi_evsmarks.set(response[5])
            e2_altemarks.set(response[6])
            gkmarks.set(response[7])
            msmarks.set(response[8])
            hrtgmarks.set(response[9])
            compmarks.set(response[10])

    rdelw=Toplevel()
    rdelw.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    rdelw.tk_focusFollowsMouse()
    rdelw.title("HCS\main page..\result \data deletion window..")
    rdelw.geometry(F"{rdelw.winfo_screenwidth()}x{rdelw.winfo_screenheight()}+0+0")
    
    #================variabele=================#
    e1marks=StringVar()
    e2_altemarks=StringVar()
    hi_evsmarks=StringVar()
    hrtgmarks=StringVar()
    ssmarks=StringVar()
    mathmarks=StringVar()
    scimarks=StringVar()
    msmarks=StringVar()
    gkmarks=StringVar()
    compmarks=StringVar()
    choice=StringVar()
    #================88888888888888888=================#


    title_frame=Frame(rdelw)
    title=Label(title_frame,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    title.pack()
    date_label=Label(title_frame,font=('arial',20,'bold'),fg='dark violet',text=f"{date.today()}")
    date_label.pack(pady=5)
    title_frame.pack()

    Label(rdelw,text="***   RESULT DELETION WINDOW...  ***",fg='yellow',font=('arial',15,'bold'),bg='red').pack(pady=15)
    student_info_frame=Frame(rdelw)
    Label(rdelw,text="***   EVERY FIELD MUST BE FILLED VERY CAREFULLY...",fg='red',font=('arial',12,'bold'),bg='yellow').pack(pady=15)
    student_info_frame=Frame(rdelw)

    year=Label(student_info_frame,font=('arial',20,'bold'),fg='green',text='YEAR :')
    year.grid(column=0,row=0)
    years=['2020','2021','2022']
    year_entry=Combobox(student_info_frame,values=years,font=('arial',20,'bold'),width=5,state="readonly")
    year_entry.grid(column=1,row=0)

    exam=Label(student_info_frame,font=('arial',20,'bold'),fg='green',text='exam :')
    exam.grid(column=2,row=0)
    exams=['QUARTERLY_1st','QUARTERLY_2nd','YEARLY']
    exam_entry=Combobox(student_info_frame,values=exams,font=('arial',20,'bold'),state="readonly")

    exam_entry.grid(column=3,row=0)

    id=Label(student_info_frame,font=('arial',20,'bold'),fg='green',text="ID :")
    id.grid(column=0,row=1)
    id_entry=Entry(student_info_frame,font=('arial',20,'bold'),fg='black',width=12,justify=RIGHT,textvariable=choice)
    id_entry.grid(column=1,row=1,pady=5)

    search=Button(student_info_frame,font=('arial',20,'bold'),text=" SEARCH ",bd=5,fg='black',bg='orange',command=lambda:search_result(year_entry.get(),exam_entry.get(),id_entry.get()))
    search.grid(column=2,row=1,padx=10)

    student_info_frame.pack(pady=10)

    resultlabel=Label(rdelw,text="   ****~ MARKS DISPLAY ~****   ",fg='red',font=('arial',10,'bold'),bg='yellow')
    resultlabel.pack()

    marks_entry_frame=Frame(rdelw)
    e1=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="ENGLISH :")
    e1.grid(column=0,row=0,padx=10)
    e1_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,state="readonly",textvariable=e1marks,justify=RIGHT)
    e1_marks.grid(column=1,row=0)

    math=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="MATHEMATICS :")
    math.grid(column=2,row=0,padx=10)
    math_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,state="readonly",textvariable=mathmarks,justify=RIGHT)
    math_marks.grid(column=3,row=0)

    sci=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="SCIENCE :")
    sci.grid(column=0,row=1,padx=10)
    sci_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,state="readonly",textvariable=scimarks,justify=RIGHT)
    sci_marks.grid(column=1,row=1)

    ss=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="SOCIAL SCIENCE :")
    ss.grid(column=2,row=1,padx=10)
    ss_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,state="readonly",textvariable=ssmarks,justify=RIGHT)
    ss_marks.grid(column=3,row=1)

    hi_evs=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="HINDI/EVS :")
    hi_evs.grid(column=0,row=2,padx=10)
    hi_evs_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,state="readonly",textvariable=hi_evsmarks,justify=RIGHT)
    hi_evs_marks.grid(column=1,row=2)

    e2_alte=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="ENG_2/ALTE :")
    e2_alte.grid(column=2,row=2,padx=10)
    e2_alte_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,state="readonly",textvariable=e2_altemarks,justify=RIGHT)
    e2_alte_marks.grid(column=3,row=2)

    gk=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="G.K. :")
    gk.grid(column=0,row=3,padx=10)
    gk_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,state="readonly",textvariable=gkmarks,justify=RIGHT)
    gk_marks.grid(column=1,row=3)

    ms=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="MORAL SCIENCE :")
    ms.grid(column=2,row=3,padx=10)
    ms_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,state="readonly",textvariable=msmarks,justify=RIGHT)
    ms_marks.grid(column=3,row=3)

    hrtg=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="HERITAGE:")
    hrtg.grid(column=0,row=4,padx=10)
    hrtg_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,state="readonly",textvariable=hrtgmarks,justify=RIGHT)
    hrtg_marks.grid(column=1,row=4)

    comp=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="COMPUTER :")
    comp.grid(column=2,row=4,padx=10)
    comp_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,state="readonly",textvariable=compmarks,justify=RIGHT)
    comp_marks.grid(column=3,row=4)

    marks_entry_frame.pack(pady=20)


    button_frame=Frame(rdelw)

    delete=Button(button_frame,font=('arial',20,'bold'),text=" DELETE ",bd=5,fg='white',bg="red",command=lambda:delresult(year_entry.get(),exam_entry.get(),id_entry.get()))
    delete.grid(column=0,row=0)
    clear=Button(button_frame,font=('arial',20,'bold'),text=" CLEAR ",bd=5,fg='white',bg="red",command=clear_data)
    clear.grid(column=1,row=0)

    button_frame.pack(pady=10)
    
    copyrightlabel=Label(rdelw,font=('arial',8,'bold'),bg='yellow',fg='red',text="""   arr. @ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
    copyrightlabel.pack(pady=5)
  



