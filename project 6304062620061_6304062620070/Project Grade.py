from tkinter import*
from tkinter import ttk
import os #เอาไว้เปิด
import csv #เอาไว้เขียนไฟล์
import json
grade_list = ["A","B+","B","C+","C","D+","D"]  #list ตัวแปรเกรดที่จะเรียกไปใช้  

# ---------------------------------------------------------------------
def main(): 
    global score1,score2,score3,Grade,inp2,inp3,inp4,inp5
    Grade = Tk()
    name=StringVar()

    score1=DoubleVar()
    score2=DoubleVar()
    score3=DoubleVar()
    name = username.get()
    json_name = vertify.get(name, '')
    iname=json_name[1]        #สร้างตัวแปรรับค่าในตำแหน่งที่1 (ชื่อผู้ใช้)
    a='Welcome '+ iname       #กำหนดตัวแปรรับค่า

    Grade.title('Calculate Grade')
    Grade.minsize(900,600)
    Grade.config(bg='#D1EAF5')

    head=Label(Grade,text='Grade',font='Tahoma 20 bold',bg='#294867',fg='#D1EAF5')
    head.grid(row=0,column=0,pady=20,padx=100)

    lb1=Label(Grade,text=a,font='Tahoma 15 bold',fg='#294867',bg='#D1EAF5')
    lb1.grid(row=1,column=0,pady=20,padx=100)

    lb2=Label(Grade,text='Your Subject',font='Tahoma 15 bold',fg='#294867',bg='#D1EAF5')
    lb2.grid(row=4,column=0,pady=10,padx=190,sticky=W)

    s=["Math","Eng","ComPro","FunCom","Digital","Econ","Physic"]     #จะนำเอาชื่อไปใช้ ให้ ___.getได้เลย
    inp2 = ttk.Combobox(values=s,state="readonly",width=9,font='Tahoma 15 bold')
    inp2.grid(row=4,column=0,sticky=E,pady=10,padx=320)

    lb3=Label(Grade,text='Your Stack Scores',font='Tahoma 15 bold',fg='#294867',bg='#D1EAF5')
    lb3.grid(row=5,column=0,pady=10,padx=190,sticky=W)

    inp3=Entry(Grade,textvariable=score1,width=8,font='Tahoma 15 bold',fg='#294867',bg='#FCF0CF')
    inp3.grid(row=5,column=0,sticky=E,pady=10,padx=349)
    inp3.focus()        #กระพริบๆ

    lb4=Label(Grade,text='Your Midterm Scores',font='Tahoma 15 bold',fg='#294867',bg='#D1EAF5')
    lb4.grid(row=6,column=0,pady=10,padx=190,sticky=W)

    inp4=Entry(Grade,textvariable=score2,width=8,font='Tahoma 15 bold',fg='#294867',bg='#FCF0CF')
    inp4.grid(row=6,column=0,sticky=E,pady=10,padx=350)
    inp4.focus()

    lb5=Label(Grade,text='Your Final Scores',font='Tahoma 15 bold',fg='#294867',bg='#D1EAF5')
    lb5.grid(row=7,column=0,pady=10,padx=190,sticky=W)

    inp5=Entry(Grade,textvariable=score3,width=5,font='Tahoma 15 bold',fg='#294867',bg='#FCF0CF')
    inp5.grid(row=7,column=0,sticky=E,pady=10,padx=390)
    inp5.focus()


    btOK=Button(Grade,text='OK',width=10,font='Tahoma 15 bold',bg='#294867',fg='#FFAAFF',command=cal)
    btOK.grid(row=12,column=0,pady=10,padx=400,sticky=W)

    bt=Button(Grade,text='Back',command=colse,width=10,font='Tahoma 15 bold',bg='#294867',fg='#CCFFEE')
    bt.grid(row=12,column=0,pady=10,padx=200,sticky=W)

    mainloop()
def  cal():  
    global check
    isubject = inp2.get()
    if isubject == '':     #เช็คว่าใส่วิชารึยัง?
        lbe=Label(Grade,text='please insert subject',font='Tahoma 15 bold',bg='#FFAAFF',fg='#294867')
        lbe.grid(row=12,column=0,pady=10,padx=100,sticky=E)
        return
    
    score = 0  #เป็นการรีเซ็ตค่า
    score=score1.get()+score2.get()+score3.get()
    if score > 100:
        score = 100
    
    if score > 45:
        check = 76     #ตัวเช็คในฟังก์ชัน grading ในการแสดงเกรด   
        for i in grade_list:
            if score >= check:
                grade = i
                break
            else:
                check -= 5
    else:
        grade = 'F'
    send_data(isubject,score,grade) #เรียกใช้ฟังก์ชัน send_data    
    Grading()   #เรียกใช้ฟังก์ชัน frame ต่อ
   

def send_data(subject,score,grade):
    data = []
    name = username.get()
    json_name = vertify.get(name)   #คือการเอาข้อมูลในไฟล์ json_name มา โดย name คือคีย์ 
    iname = json_name[1]        #สร้างตัวแปรรับค่า
    
    data.append(iname)      #เพิ่มข้อมูลเข้าลิส data
    data.append(subject)
    data.append(score)
    data.append(grade)
    

    try:
        with open("History.csv", "a") as f:  
            writer = csv.writer(f, lineterminator="\n") #สร้างเครื่องมือเขียน เพราะ csv เขียนเลยไม่ได้
            writer.writerow(data)  #สั่งให้เขียน
            return
    except Exception as e:                         #Exception กรอง error ทุกชนิด
        print("2",e)
        print("not save")
        return
    
def colse():
    Grade.destroy()  #ปิดหน้าต่าง Grade
    login()
def close1():
    window.destroy() #ปิดหน้าต่าง window
    
def Grading():       #ฟังก์ชันหน้าต่างแสดงผลลัพธ์ (หน้าต่าง grading)
    try:
        with open("History.csv") as f:  
            read = csv.reader(f)  #สร้างตัวอ่าน
            read_list = list(read)  #สั่งให้อ่าน
            n = len(read_list) - 1  #การหาตำแหน่งของลิสตัวล่าสุดที่อยู่ใน history.csv
            data_list = read_list[n]  #สร้างตัวรับลิสตัวล่าสุดมาใช้
    except Exception as e:      #Exception กรอง error ทุกชนิด
        print("3",e)
        print("not save")
        return

    screen = Toplevel(Grade)  # Toplevel คือ การลิ้งค์หน้าต่างใหม่
    screen.title("Grading")  # ตั้งชื่อหน้าต่าง
    screen.minsize(250, 100)  # ตั้งขนาดหน้าต่าง
    screen.config(bg='#D1EAF5')  # พื้นหลัง


    lb1 = Label(screen, text='Name : '+ data_list[0], font='Tahoma 15 bold', fg='#294867', bg='#D1EAF5')
    lb1.grid(row=2, column=0, pady=10, padx=50, sticky=W)
        
        
    lb2 = Label(screen, text='Subject : '+ data_list[1], font='Tahoma 15 bold', fg='#294867', bg='#D1EAF5')
    lb2.grid(row=3, column=0, pady=10, padx=50, sticky=W)

    lb3 = Label(screen, text='Score : ' + str(data_list[2]), font='Tahoma 15 bold', fg='#294867', bg='#D1EAF5')
    lb3.grid(row=4, column=0, pady=10, padx=50, sticky=W)
 

    lb = Label(screen, text='Grade : ' + data_list[3], font='Tahoma 15 bold', fg='#294867', bg='#D1EAF5')
    lb.grid(row=5, column=0, pady=10, padx=50, sticky=W)

    btHis = Button(screen, text='History', command=open_file, width=10, bg='#ffaacc')
    btHis.grid(row=10, column=0, pady=10, padx=150, sticky=E)

    bt = Button(screen, text='Close', command=screen.destroy, width=10, bg='#FFB7B7')
    bt.grid(row=10, column=0, pady=10, padx=30, sticky=E)

def open_file():
    try:
        file = "History.csv" #ชื่อไฟล์
        os.startfile(file) #เปิดไฟล์
    except:
        print("error")
        return


def ReadData():
    global vertify         #การอัพเดทค่า vertify
    global display         #การอัพเดทค่า display
    PATH_USERNAMES = "user.json"

    try:
        with open(PATH_USERNAMES) as js:
            info = json.load(js)                            #โหลดข้อมูลจากไฟล์ json มาเป็น dictionary
            list_user = info.get("User", '')                #เอาข้อมูลจากคีย์ User มาใช้
    except FileNotFoundError:
        print("ไม่มีไฟล์ที่ต้องการอ่าน")
    except Exception as e:
        print("4", e)
        return

    name = username.get()
    passw = password.get()

    try:
        for item in list_user:  #ตรวจสอบว่าชื่อผู้ใช้งานถูกต้องไหม?
            if name in item:
                vertify = item
                break
        else:
            vertify = ''

        if name in vertify:
            json_password = vertify.get(name, '')
            if passw == json_password[0]:   #ถ้า password ถูกต้อง ให้ print
                print("Password OK")
                display.set('Welcome {}'.format(name)) 
                close1()   #เรียกฟังก์ชันมาใช้
                main()  #เรียกฟังก์ชันใช้
            else:
                display.set('Username or Password wrong please try again ')  #ถ้า user หรือ password ไม่มีในลิส ให้แสดงค่าใน ' '
        else:
            lb = Label(window,text='Username or Password wrong please try again ', pady=8,bg='#FFAAFF',fg='#294867', font='Tahoma 12 bold')
            lb.grid(row=8, column=2)
            print("ไม่เจอ User")
    except :
        lb = Label(window,text='Username or Password wrong please try again ', pady=8,bg='#FFAAFF',fg='#294867', font='Tahoma 12 bold')
        lb.grid(row=8, column=2)
        return


# -----------------------------------------------------------------------
def login():
    global window
    global display
    global username        #การที่ global ไว้ตรงนี้ด้วยเพราะว่า ตัวแปรเหล่านี้มีการใช้ในฟังก์ชันอื่นด้วย
    global password
    # ------------------------------------------------------------------------
    window = Tk()
    window.title('Login')
    window.minsize(500, 350)
    window.config(bg='#D1EAF5')
    
    display = StringVar()
    username = StringVar()
    password = StringVar()

    head = Label(window, text="HELLO RB'S STUDENTS", font='Tahoma 15 bold',bg='#294867',fg='#D1EAF5')
    head.grid(row=0, column=2 )
    head = Label(window, text='Welcome to School System', font='Tahoma 15 bold',bg='#294867',fg='#FCF0CF')
    head.grid(row=1, column=2)
    
    head = Label(window, text='User Name',font='Tahoma 15 bold',fg='#294867',bg='#D1EAF5')
    head.grid(row=3, column=1, pady=20, padx=15)

    inp = Entry(window, textvariable=username, width=20, font='Tahoma 15 bold',fg='#294867',bg='#FCF0CF')
    inp.grid(row=3, column=2)
    inp.focus()

    head = Label(window, text='Password', font='Tahoma 15 bold', fg='#294867',bg='#D1EAF5')
    head.grid(row=4, column=1, pady=20,)

    inp = Entry(window, textvariable=password, width=20, font='Tahoma 15 bold', show='*',fg='#294867',bg='#FCF0CF')
    inp.grid(row=4, column=2,padx=50,sticky=E)
    inp.focus()

    btlog = Button(window, text='login', font='Tahoma 15 bold', width=10,bg='#294867',fg='#FFAAFF', command=ReadData)
    btlog.grid(row=5, column=2)

    btclose = Button(window, text='Exit', font='Tahoma 15 bold', width=10,bg='#294867',fg='#CCFFEE', command=window.destroy)
    btclose.grid(row=5, column=1,padx=40)
    
    mainloop()
login()

    





