from tkinter import *
from datetime import date

#=========================function definition =======================================#

def exit_():
    root.destroy()
#========================== function importing fom modules ====================================#
import result_input_record as res_inp
import result_enquiry as res_enq
import result_correction as res_corr
import result_delete as res_del
import student_input_record as std_inpr
import student_update_record as  std_upd
import student_delete_record as std_delr
import student_enquire_record as std_enqr
import fee_correction_record as fee_corrr
import fee_delete_record as fee_delr
import fee_payment as fee_pay
import fee_payment_enquiry as fee_enq
#=====================================8888888888888888========================================#



root=Tk()
root.geometry(F"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
root.title("HCS/main window..")
root.tk_focusFollowsMouse()
root.iconbitmap('M:\programs\projects 2019\school app\HOLY CHILD SCHOOL\MAIN PAGE\HCS_icon.ico')
root.config(background="light GREY")
root.tkraise()

titleframe=Frame(root)
titleframe.config(background="light GREY")
title=Label(titleframe,font=('arial',20,'bold'),fg="dark blue",text=f"""HOLY CHILD SCHOOL,Toluvi
    Dimapur, Nagaland
    Pin:797112""",bg="light grey")
title.pack()

titleframe.pack()

date_=Label(root,font=('arial',13,'bold'),text=f"  {date.today()}  ",fg="red",bg="yellow")
date_.pack()

#=========================== Services ==================================#
serviceframe=LabelFrame(root,text='WELCOME TO HCS APP SERVICE',fg="dark red",font=('arial',10,'bold'),bd=10,relief='ridge',pady=2)


recordframe=LabelFrame(serviceframe,text='STUDENT FRAME',fg="dark red",font=('arial',12,'bold'),bd=5,padx=12)
recordframe.config(background="light GREY")

inputrecord=Button(recordframe,text="INSERT STD RECORD",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=std_inpr.inputstudentdata)
inputrecord.pack(pady=10)

fetchrecord=Button(recordframe,text="ENQUIRE STD RECORD",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=std_enqr.enquirystudentdata) 
fetchrecord.pack(pady=10)

correctrecord=Button(recordframe,text="CORRECT STD RECORD",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=std_upd.updatestudentdata)
correctrecord.pack(pady=10)

deleterecord=Button(recordframe,text="DELETE STD RECORD",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=std_delr.deletestudentdata) 
deleterecord.pack(pady=10)

recordframe.grid(row=0,column=0,padx=50,pady=10)

feeframe=LabelFrame(serviceframe,text='FEE FRAME',fg="dark red",font=('arial',12,'bold'),bd=5,padx=20)
feeframe.config(background="light GREY")

feepayment=Button(feeframe,text="   FEE PAYMENT   ",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=fee_pay.payfee)
feepayment.pack(pady=10)

enquirefeerecord=Button(feeframe,text="ENQUIRE FEE RECORD",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=fee_enq.feepaymentenquiry)
enquirefeerecord.pack(pady=10)

correctfeerecord=Button(feeframe,text="CORRECT FEE RECORD",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=fee_corrr.record_correct)
correctfeerecord.pack(pady=10)

deletefeerecord=Button(feeframe,text="DELETE FEE RECORD",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=fee_delr.feedel) 
deletefeerecord.pack(pady=10)

feeframe.grid(row=0,column=1,padx=50,pady=10)

resultframe=LabelFrame(serviceframe,bd=5,text='RESULT FRAME',fg="dark red",font=('arial',12,'bold'),padx=20)
resultframe.config(background="light GREY")

inputresult=Button(resultframe,text="INSERT RESULT",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=res_inp.inserresult)
inputresult.pack(pady=10)

fetchresult=Button(resultframe,text="ENQUIRE RESULT",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=res_enq.resultenquiry)
fetchresult.pack(pady=10)

correctresult=Button(resultframe,text="CORRECT RESULT",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=res_corr.correct_result)
correctresult.pack(pady=10)

deleteresult=Button(resultframe,text="DELETE RESULT",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=res_del.delete_result)
deleteresult.pack(pady=10)

resultframe.grid(row=1,column=0,padx=50)

buttonframe=LabelFrame(serviceframe,bd=5,text='CONTROL FRAME',fg="dark red",font=('arial',12,'bold'),padx=20)
buttonframe.config(background="light GREY")

exit_=Button(buttonframe,text="      EXIT      ",bd=5,bg='yellow',fg='dark blue',font=('arial',10,'bold'),command=exit_)
exit_.pack(pady=10)

buttonframe.grid(row=1,column=1,padx=50,pady=20)

serviceframe.pack(padx=10)

#=========================== 88888888 ==================================#

contactframe=Frame(root,bg='light grey')

copyrightlabel=Label(contactframe,font=('arial',10,'bold'),bg='yellow',fg='dark red',text="""   arr. @ vksoftwaresolution
CONTACT: vivekkumarverma332@gmail.com / 07005833385   """)
copyrightlabel.pack(pady=10)
contactframe.pack()

root.mainloop()