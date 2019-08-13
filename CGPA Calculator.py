from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("800x700+0+0")
root.title("CG Calculator")

lb1Info = Label(font=('arial', 25, 'italic'), text="CG CALCULATOR", fg='gray')
lb1Info.grid(row=1, column=1)

Namevar = StringVar()
Name = Label(root, font=('arial', 13, 'italic'), text="ENTER YOUR NAME : ", fg='gray', anchor='w')
Name.grid(row=3, column=0)
txtName = Entry(font=('arial', 13, 'italic'), textvariable=Namevar, fg='gray', justify='left')
txtName.grid(row=3, column=1)

Enroll = StringVar()
EnrollmentNo = Label(root, font=('arial', 13, 'italic'), text="ENROLLMENT No. : ", fg='gray', anchor='w')
EnrollmentNo.grid(row=4, column=0)
txtEnroll = Entry(font=('arial', 13, 'italic'), textvariable=Enroll, fg='gray', justify='left')
txtEnroll.grid(row=4, column=1)

lab = Label(root, font=('arial', 13, 'italic'), text=" ", fg='gray', anchor='w')
lab.grid(row=5, column=0)

Sub1var = StringVar()
Sub1 = Label(root, font=('arial', 13, 'italic'), text="Computer Programming and Numerical Methods : ", fg='gray', anchor='w')
Sub1.grid(row=6, column=0)
txtSub1 = Entry(font=('arial', 13, 'italic'), textvariable=Sub1var, fg='gray', justify='left')
txtSub1.grid(row=6, column=1)

Sub2var = StringVar()
Sub2 = Label(root, font=('arial', 13, 'italic'), text="Introduction to Polymer Science and Engineering : ", fg='gray', anchor='w')
Sub2.grid(row=7, column=0)
txtSub2 = Entry(font=('arial', 13, 'italic'), textvariable=Sub2var, fg='gray', justify='left')
txtSub2.grid(row=7, column=1)

Sub3var = StringVar()
Sub3 = Label(root, font=('arial', 13, 'italic'), text="Introduction to Environmental Studies : ", fg='gray', anchor='w')
Sub3.grid(row=8, column=0)
txtSub3 = Entry(font=('arial', 13, 'italic'), textvariable=Sub3var, fg='gray', justify='left')
txtSub3.grid(row=8, column=1)

Sub4var = StringVar()
Sub4 = Label(root, font=('arial', 13, 'italic'), text="Communication Skills BASIC / ADVANCE : ", fg='gray', anchor='w')
Sub4.grid(row=9, column=0)
txtSub4 = Entry(font=('arial', 13, 'italic'), textvariable=Sub4var, fg='gray', justify='left')
txtSub4.grid(row=9, column=1)

Sub5var = StringVar()
Sub5 = Label(root, font=('arial', 13, 'italic'), text="Ethics and Self Awareness : ", fg='gray', anchor='w')
Sub5.grid(row=10, column=0)
txtSub5 = Entry(font=('arial', 13, 'italic'), textvariable=Sub5var, fg='gray', justify='left')
txtSub5.grid(row=10, column=1)

Sub6var = StringVar()
Sub6 = Label(root, font=('arial', 13, 'italic'), text="Polymer Chemistry : ", fg='gray', anchor='w')
Sub6.grid(row=11, column=0)
txtSub6 = Entry(font=('arial', 13, 'italic'), textvariable=Sub6var, fg='gray', justify='left')
txtSub6.grid(row=11, column=1)

Sub7var = StringVar()
Sub7 = Label(root, font=('arial', 13, 'italic'), text="Mathematics-I : ", fg='gray', anchor='w')
Sub7.grid(row=12, column=0)
txtSub7 = Entry(font=('arial', 13, 'italic'), textvariable=Sub7var, fg='gray', justify='left')
txtSub7.grid(row=12, column=1)



Gap = Label(root, font=('arial', 13, 'italic'), text=" ", fg='gray', anchor='w')
Gap.grid(row=14, column=0)
Gap = Label(root, font=('arial', 13, 'italic'), text=" ", fg='gray', anchor='w')
Gap.grid(row=5, column=0)
Gap = Label(root, font=('arial', 13, 'italic'), text=" ", fg='gray', anchor='w')
Gap.grid(row=16, column=0)



def calcg():
    one = float(Sub1var.get())
    two = float(Sub2var.get())
    three = float(Sub3var.get())
    four = float(Sub4var.get())
    five = float(Sub5var.get())
    six = float(Sub6var.get())
    seven = float(Sub7var.get())

    sg = (((one * 4) + (two * 2) + (three * 3) + (four * 2) + (five * 2) + (six * 4) + (seven * 4) )/ 24)

    cgpa = sg
    name = Namevar.get()
    enroll = Enroll.get()
    output = " Hello %s" % name + "\nEnrollment No. %s" % enroll
    output += "\nYour this semister SGPA is %s" % round(sg,2)
    output += "\nAnd Overall CGPA is %s" % round(cgpa,2)
    tkinter.messagebox.showinfo("CG", output)


button1 = Button(root, text="Calculate CG ", font='Times 15 bold', fg='gray', height=1, width=9, command=calcg)
button1.grid(row=17, column=1, sticky=S + N + E + W)

root.mainloop()
