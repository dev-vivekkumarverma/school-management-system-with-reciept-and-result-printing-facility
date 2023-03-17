from tkinter import *
from datetime import date
from tkinter.ttk import Combobox


def correct_result():

    #================  functions =================#
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
        new_choice.set("")

    def search_result(x,y,z):
        import db_result_handler as t
        response=t.result.fetch_result(x,y,z)
        if response == "F" or response is None:
            import conformation as cnf
            cnf.confomation.warning_alart(" DATA NOT FOUND !")
            rcorrw.tkraise()
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
        

    def update_result_(year_, exam_, old_id_, new_id_, e1_, math_, sci_, ss_, hi_evs_, e2_alte_, gk_, ms_, hrtg_, comp_):
        import conformation as cnf
        msg=f"""
        YEAR:{year_entry.get()}   
        OLD ID:{id_entry.get()}
        EXAM:{exam_entry.get()}

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
        
        WOULD YOU LIKE THIS DATA TO BE UPDATED AT
        NEW ID {id_new_entry.get()}   ???
        
        """
        ans=cnf.confomation.info_conformation(msg)
    
        if ans is True:
            import db_result_handler as t
            resp=t.result.correction_result(year_, exam_, old_id_, new_id_, e1_, math_, sci_, ss_, hi_evs_, e2_alte_, gk_, ms_, hrtg_, comp_)
    
            if resp=="T":
                cnf.confomation.info_show("CONGRATULATIONS ! DATA IS SUCCESSFULLY UPDATED/CORRECTED !")
                clear_data()
                rcorrw.tkraise()
            else:
                import conformation as cnf
                cnf.confomation.warning_alart(" SOMETHING WENT WRONG !")
                rcorrw.tkraise()

            

    #================********************=================#

    rcorrw=Toplevel()
    rcorrw.title("HCS\main page..\result \data correction window..")
    rcorrw.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
    rcorrw.geometry(F"{rcorrw.winfo_screenwidth()}x{rcorrw.winfo_screenheight()}+0+0")
    rcorrw.tk_focusFollowsMouse()




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
    new_choice=StringVar()
    #================88888888888888888=================#

    title_frame=Frame(rcorrw)
    title=Label(title_frame,font=('arial',34,'bold'), text="""HOLY CHILD SCHOOL,
    Toluvi Village""",fg="dark blue")
    title.pack()
    date_label=Label(title_frame,font=('arial',20,'bold'),fg='dark violet',text=f"{date.today()}")
    date_label.pack(pady=5)
    title_frame.pack()

    Label(rcorrw,text="***   RESULT CORRECTION WINDOW...  ***",fg='yellow',font=('arial',15,'bold'),bg='red').pack(pady=15)
    student_info_frame=Frame(rcorrw)
    Label(rcorrw,text="***   EVERY FIELD MUST BE FILLED VERY CAREFULLY...",fg='red',font=('arial',12,'bold'),bg='yellow').pack(pady=15)
    student_info_frame=Frame(rcorrw)

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
    id_entry=Entry(student_info_frame,font=('arial',20,'bold'),fg='black',width=12,textvariable=choice)
    id_entry.grid(column=1,row=1,pady=5)


    search=Button(student_info_frame,font=('arial',20,'bold'),text=" SEARCH ",bd=5,fg='black',bg='orange',command=lambda:search_result(year_entry.get(),exam_entry.get(),id_entry.get()))
    search.grid(column=2,row=1,padx=10)


    student_info_frame.pack(pady=10)

    resultlabel=Label(rcorrw,text="   ****~ MARKS INPUT & DISPLAY FIELD ~****   ",fg='red',font=('arial',10,'bold'),bg='yellow')
    resultlabel.pack()

    marks_entry_frame=Frame(rcorrw)
    e1=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="ENGLISH :")
    e1.grid(column=0,row=0,padx=10)
    e1_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,textvariable=e1marks)
    e1_marks.grid(column=1,row=0)

    math=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="MATHEMATICS :")
    math.grid(column=2,row=0,padx=10)
    math_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,textvariable=mathmarks)
    math_marks.grid(column=3,row=0)

    sci=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="SCIENCE :")
    sci.grid(column=0,row=1,padx=10)
    sci_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,textvariable=scimarks)
    sci_marks.grid(column=1,row=1)

    ss=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="SOCIAL SCIENCE :")
    ss.grid(column=2,row=1,padx=10)
    ss_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,textvariable=ssmarks)
    ss_marks.grid(column=3,row=1)

    hi_evs=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="HINDI/EVS :")
    hi_evs.grid(column=0,row=2,padx=10)
    hi_evs_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,textvariable=hi_evsmarks)
    hi_evs_marks.grid(column=1,row=2)

    e2_alte=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="ENG_2/ALTE :")
    e2_alte.grid(column=2,row=2,padx=10)
    e2_alte_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,textvariable=e2_altemarks)
    e2_alte_marks.grid(column=3,row=2)

    gk=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="G.K. :")
    gk.grid(column=0,row=3,padx=10)
    gk_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,textvariable=gkmarks)
    gk_marks.grid(column=1,row=3)

    ms=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="MORAL SCIENCE :")
    ms.grid(column=2,row=3,padx=10)
    ms_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,textvariable=msmarks)
    ms_marks.grid(column=3,row=3)

    hrtg=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="HERITAGE:")
    hrtg.grid(column=0,row=4,padx=10)
    hrtg_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,textvariable=hrtgmarks)
    hrtg_marks.grid(column=1,row=4)

    comp=Label(marks_entry_frame,font=('arial',20,'bold'),fg='green',text="COMPUTER :")
    comp.grid(column=2,row=4,padx=10)
    comp_marks=Entry(marks_entry_frame,font=('arial',20,'bold'),fg='black',width=3,textvariable=compmarks)
    comp_marks.grid(column=3,row=4)

    marks_entry_frame.pack(pady=20,padx=50)


    button_frame=Frame(rcorrw)

    id_new=Label(button_frame,font=('arial',20,'bold'),fg='green',text="NEW ID :")
    id_new.grid(column=0,row=0)
    id_new_entry=Entry(button_frame,font=('arial',20,'bold'),fg='black',width=12,textvariable=new_choice)
    id_new_entry.grid(column=1,row=0,pady=5)

    update_button=Button(button_frame,font=('arial',20,'bold'),text=" UPDATE RESULT ",bd=5,fg='white',bg="red",command=lambda:update_result_(year_entry.get(),exam_entry.get(),id_entry.get(),id_new_entry.get(),e1_marks.get(),math_marks.get(),sci_marks.get(),ss_marks.get(),hi_evs_marks.get(),e2_alte_marks.get(),gk_marks.get(),ms_marks.get(),hrtg_marks.get(),comp_marks.get()))
    update_button.grid(row=0,column=2,padx=10)

    reset=Button(button_frame,font=('arial',20,'bold'),text=" RESET ",bd=5,fg='white',bg="red",command=clear_data)
    reset.grid(row=0,column=3)

    button_frame.pack(padx=10)
    
    copyrightlabel=Label(rcorrw,font=('arial',8,'bold'),bg='yellow',fg='red',text="""   arr. @ vksoftwaresolution
    CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
    copyrightlabel.pack(pady=5)





