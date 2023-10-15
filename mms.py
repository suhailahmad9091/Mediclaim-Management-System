from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import re
import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="insurance",
    port=3306
)
mycursor = mydb.cursor(buffered=True)
mydb.autocommit = True





def admin_login():
    root = Tk()
    root.title("Admin Login")
    root.geometry("700x420+300+150")
    root.resizable(False, False)
    root.configure(bg="#ccffee")

    label_0 = Label(root,
                    fg="white",
                    bg="red",
                    font="ariel 35 bold",
                    padx=15,
                    pady=9
                )
    label_0.pack(fill="both")

    label_33 = Label(label_0, text="Admin Login",
                    fg="white",
                    bg="red",
                    font="ariel 35 bold",
                    padx=15,
                    pady=9
                    )
    label_33.place(x=180, y=0)

    Label(root,
          text = "Username",
          font="ariel 20 bold",
          bg="#ccffee",
          fg="#000000"
          ).place(x=90,y=130)

    Label(root,
          text="Password",
          font="ariel 20 bold",
          bg="#ccffee",
          fg="#000000"
          ).place(x=90, y=230)

    e1 = Entry(root, width="30", font=('Arial 15'))
    e1.place(x=260,y=137)

    e2 = Entry(root, show="*", width="30", font=('Arial 15'))
    e2.place(x=260, y=237)

    def admin_back_home():
        root.destroy()
        main_menu()

    def move_admin_login():
        email = e1.get()
        password = e2.get()

        if email=="" or password=="":
            mb.showinfo("Error Message", "Please enter Username and Password")
        elif email=="admin" and password=="admin":
            root.destroy()
            admin()

        else:
            mb.showinfo("Error Message","Invalid Username and Password")       

    button1 = Button(root, text="Back", width=10, bg="brown", fg="white",
                      font=("ariel", 18, "bold"), bd=1, relief="solid",
                      command = admin_back_home)
    button1.place(x=110, y=330)

    button2 = Button(root, text="Login", width=10, bg="blue", fg="white",
                    font=("ariel", 18, "bold"), bd=1, relief="solid",
                    command=move_admin_login)
    button2.place(x=420, y=330)

    root.mainloop()





def admin():
    root = Tk()
    root.title("Admin")
    root.geometry("900x460+240+130")
    root.resizable(False, False)
    root.configure(bg="white")

    label_0 = Label(root, text="Welcome Admin",
                    fg="#990000",
                    bg="#ffff33",
                    font="ariel 35 bold",
                    pady=10
                    )
    label_0.pack(fill="both")

    label_11 = Label(root, text="* * * * *",
                     fg="black",
                     bg="#ffff33",
                     font="ariel 30 bold",
                     )
    label_11.place(x=45, y=15)

    label_12 = Label(root, text="* * * * *",
                     fg="black",
                     bg="#ffff33",
                     font="ariel 30 bold",
                     )
    label_12.place(x=710, y=15)

    find = Image.open("images\\admin.jpg")
    my_photo = ImageTk.PhotoImage(find)

    label_1 = Label(root,
                    image=my_photo,
                    bd=0, relief="solid"
                    )
    label_1.place(x=60, y=110)
    
    def logout():
        root.destroy()
        main_menu()

    button0 = Button(root, text="Logout", width=10, bg="black", fg="white",
                     font=("ariel", 20, "bold"), bd=1, relief="solid",
                     command=logout)

    button0.place(x=70, y=370)

    def move_insurance_list():
        root.destroy()
        insurance_list(0)

    button1 = Button(root, text="Insurance List", width=20, bg="#006666", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_insurance_list)

    button1.place(x=300, y=140)

    def move_add_insurance():
        root.destroy()
        add_insurance()

    button2 = Button(root, text="Add Insurance", width=20, bg="green", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_add_insurance)

    button2.place(x=300, y=210)

    def move_delete_insurance():
        root.destroy()
        delete_insurance()

    button3 = Button(root, text="Delete Insurance", width=20, bg="red", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_delete_insurance)

    button3.place(x=300, y=280)

    def move_user_list():
        root.destroy()
        user_list()

    button4 = Button(root, text="User List", width=20, bg="#006666", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                    command=move_user_list)

    button4.place(x=300, y=350)

    def move_policy_list():
        root.destroy()
        policy_list(0)

    button5 = Button(root, text="Policy List", width=20, bg="#006666", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_policy_list)

    button5.place(x=600, y=140)

    def move_add_policy():
        root.destroy()
        add_policy()

    button6 = Button(root, text="Add Policy", width=20, bg="green", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_add_policy)

    button6.place(x=600, y=210)

    def move_delete_policy():
        root.destroy()
        delete_policy()

    button7 = Button(root, text="Delete Policy", width=20, bg="red", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_delete_policy)

    button7.place(x=600, y=280)

    def move_policy_holder():
        root.destroy()
        policy_holder()

    button8 = Button(root, text="Policy Holder", width=20, bg="#006666", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_policy_holder)

    button8.place(x=600, y=350)

    root.mainloop()





def insurance_list(user_id):
    root = Tk()
    root.title("Insurance List")
    root.geometry("600x530+300+100")
    root.resizable(False, False)
    root.configure(bg="#ffffb3")

    style = ttk.Style()
    style.theme_use('alt')

    my_tree = ttk.Treeview(root)
    my_tree.place(x=20, y=20, width=560, height=400)

    my_tree.configure(
        columns=(
        "Insurance ID",
        "Name",
        ), show='headings'
    )

    scrollbary = Scrollbar(my_tree, orient=VERTICAL)

    my_tree.configure(yscrollcommand=scrollbary.set)
    my_tree.configure(selectmode="extended")

    scrollbary.configure(command=my_tree.yview)
    scrollbary.pack(side=RIGHT,fill=Y)
    
    my_tree.heading("#1", text="Insurance ID", anchor=CENTER)
    my_tree.heading("#2", text="Name", anchor=CENTER)
    
    my_tree.column("#1", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#2", minwidth=300, width=300, anchor=CENTER)
    

    mycursor.execute("select * from category")

    for i in mycursor.fetchall():
        my_tree.insert('', 'end', text='1', values=(i[0], i[1]))

    def move_backword():
        root.destroy()
        if user_id == 0:
            admin()
        else:
            user(user_id)

    button1 = Button(root, text="Back", width=10, bg="black", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_backword)
    button1.place(x=400, y=460)

    root.mainloop()





def add_insurance():
    root = Tk()
    root.title("Add Insurance")
    root.geometry("770x200+270+200")
    root.resizable(False, False)
    root.configure(bg="#e6ffee")

    label_1 = Label(root, text="Insurance Name", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_1.place(x=60, y=30)

    entry_1= Entry(root, width=40, font=("Times", 15))
    entry_1.place(x=300, y=30)

    def add_insurance_final(t1):
        query = "insert into category(category_name) values(%s)"
        mycursor.execute(query, (t1,))
        mb.showinfo("Message", "Insurance Added Successfully")

    def move_forward():
        t1 = entry_1.get()
        
        if t1 == "":
            mb.showinfo("Message", "Please fill in every field")
        else:
            flag = True
            pattern = re.compile("^[a-zA-Z\s]+$")
            if not pattern.match(t1):
                flag = False
                mb.showinfo("Message", "Insurance Name is not correct")
            if flag == True :
                add_insurance_final(t1)
                root.destroy()
                admin()
                
    def move_backword():
        root.destroy()
        admin()

    button_1 = Button(root, text="Back", width=10, bg="yellow", fg="red",
                      font=("Times", 20, "bold"), bd=1, relief="solid",
                      command=move_backword)
    button_1.place(x=150, y=100)
    
    button_2 = Button(root, text="Add", width=10, bg="brown", fg="white",
                      font=("Times", 20, "bold"), bd=1, relief="solid",
                      command=move_forward)
    button_2.place(x=440, y=100)

    root.mainloop()





def delete_insurance():
    root = Tk()
    root.title("Delete Insurance")
    root.geometry("600x300+370+150")
    root.resizable(False, False)
    root.configure(bg="#ffffb3")

    label_0 = Label(root, text="Delete Insurance",
                    fg="white",
                    bg="red",
                    font="ariel 20 bold",
                    pady=10
                    )
    label_0.pack(fill="both")

    Label(root,
          text="Insurance ID",
          font="ariel 15 bold",
          bg="#ffffb3",
          fg="#000000"
          ).place(x=90, y=110)

    e1 = Entry(root, width="20", font=('Arial 15'))
    e1.place(x=260, y=113)

    def move_forward():
        t1 = e1.get()

        if t1 == "":
            mb.showinfo("Message", "Please fill the blank")
        else:
            query = "delete from category where category_id = %s"
            mycursor.execute(query, (t1,))
            if mycursor.rowcount == 0:
                mb.showinfo("Message", "Insurance ID is not correct")
            else:
                mb.showinfo("Message", "Insurance Deleted Successfully")
                root.destroy()
                admin()

    def move_backword():
        root.destroy()
        admin()

    button2 = Button(root, text="Back", width=10, bg="black", fg="white",
                     font=("Times", 15, "bold"), bd=1, relief="solid",
                     command=move_backword)
    button2.place(x=120, y=200)

    button1 = Button(root, text="Delete", width=10, bg="#00ff00", fg="red",
                     font=("Times", 15, "bold"), bd=1, relief="solid",
                     command=move_forward)
    button1.place(x=330, y=200)

    root.mainloop()





def user_list():
    root = Tk()
    root.title("User List")
    root.geometry("1210x540+65+70")
    root.resizable(False, False)
    root.configure(bg="#ffffb3")

    style = ttk.Style()
    style.theme_use('alt')

    my_tree = ttk.Treeview(root)
    my_tree.place(x=20, y=20, width=1170, height=400)

    my_tree.configure(
        columns=(
        "User ID",
        "Name",
        "Gender",
        "Address",
        "Mobile Number",
        "Email",
        "Password",
        ), show='headings'
    )

    scrollbarx = Scrollbar(my_tree, orient=HORIZONTAL)
    scrollbary = Scrollbar(my_tree, orient=VERTICAL)

    my_tree.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    my_tree.configure(selectmode="extended")

    scrollbary.configure(command=my_tree.yview)
    scrollbarx.configure(command=my_tree.xview)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx.pack(side=BOTTOM, fill=X)
    
    my_tree.heading("#1", text="User ID", anchor=CENTER)
    my_tree.heading("#2", text="Name", anchor=CENTER)
    my_tree.heading("#3", text="Gender", anchor=CENTER)
    my_tree.heading("#4", text="Address", anchor=CENTER)
    my_tree.heading("#5", text="Mobile Number", anchor=CENTER)
    my_tree.heading("#6", text="Email", anchor=CENTER)
    my_tree.heading("#7", text="Password", anchor=CENTER)
    
    my_tree.column("#1", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#2", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#3", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#4", minwidth=500, width=500, anchor=CENTER)
    my_tree.column("#5", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#6", minwidth=400, width=400, anchor=CENTER)
    my_tree.column("#7", minwidth=200, width=200, anchor=CENTER)

    mycursor.execute("select * from user")

    for i in mycursor.fetchall():
        my_tree.insert('', 'end', text='1', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    def move_backword():
        root.destroy()
        admin()

    button1 = Button(root, text="Back", width=10, bg="black", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_backword)
    button1.place(x=1000, y=460)

    root.mainloop()





def policy_list(user_id):
    root = Tk()
    root.title("Policy List")
    root.geometry("1210x540+65+70")
    root.resizable(False, False)
    root.configure(bg="#ffffb3")

    style = ttk.Style()
    style.theme_use('alt')

    my_tree = ttk.Treeview(root)
    my_tree.place(x=20, y=20, width=1170, height=400)

    my_tree.configure(
        columns=(
        "Policy ID",
        "Name",
        "Sum Assurance",
        "Premium",
        "Tenure",
        "Category",
        ), show='headings'
    )

    scrollbarx = Scrollbar(my_tree, orient=HORIZONTAL)
    scrollbary = Scrollbar(my_tree, orient=VERTICAL)

    my_tree.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    my_tree.configure(selectmode="extended")

    scrollbary.configure(command=my_tree.yview)
    scrollbarx.configure(command=my_tree.xview)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx.pack(side=BOTTOM, fill=X)
    
    my_tree.heading("#1", text="Policy ID", anchor=CENTER)
    my_tree.heading("#2", text="Name", anchor=CENTER)
    my_tree.heading("#3", text="Sum Assurance", anchor=CENTER)
    my_tree.heading("#4", text="Premium", anchor=CENTER)
    my_tree.heading("#5", text="Tenure", anchor=CENTER)
    my_tree.heading("#6", text="Category", anchor=CENTER)
    
    my_tree.column("#1", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#2", minwidth=300, width=300, anchor=CENTER)
    my_tree.column("#3", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#4", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#5", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#6", minwidth=300, width=300, anchor=CENTER)
    
    mycursor.execute("select p.policy_id, p.policy_name, p.sum_assurance \
                    , p.premium, p.tenure, c.category_name from policy \
                    p inner join category c on p.category_id = \
                     c.category_id")

    for i in mycursor.fetchall():
        my_tree.insert('', 'end', text='1', values=(i[0], i[1], i[2], i[3], i[4], i[5]))

    def move_backword():
        root.destroy()
        if user_id == 0:
            admin()
        else:
            user(user_id)

    button1 = Button(root, text="Back", width=10, bg="black", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_backword)
    button1.place(x=1000, y=460)

    root.mainloop()





def add_policy():
    root = Tk()
    root.title("Add Policy")
    root.geometry("610x450+350+130")
    root.resizable(False, False)
    root.configure(bg="#e6ffee")

    label_1 = Label(root, text="Policy Name", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_1.place(x=60, y=30)

    entry_1= Entry(root, width=25, font=("Times", 15))
    entry_1.place(x=300, y=30)

    label_2 = Label(root, text="Sum Assurance", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_2.place(x=60, y=90)

    entry_2 = Entry(root, width=25, font=("Times", 15))
    entry_2.place(x=300, y=90)

    label_3 = Label(root, text="Premium", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_3.place(x=60, y=150)

    entry_3 = Entry(root, width=25, font=("Times", 15))
    entry_3.place(x=300, y=150)

    label_4 = Label(root, text="Tenure", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_4.place(x=60, y=210)

    entry_4 = Entry(root, width=25, font=("Times", 15))
    entry_4.place(x=300, y=210)

    label_5 = Label(root, text="Insurance ID", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_5.place(x=60, y=270)

    entry_5 = Entry(root, width=25, font=("Times", 15))
    entry_5.place(x=300, y=270)

    def add_policy_final(t1,t2,t3,t4,t5):
        query = "insert into policy(policy_name, sum_assurance, \
        premium, tenure, category_id) values(%s,%s,%s,%s,%s)"
        mycursor.execute(query, (t1, t2, t3, t4, t5))
        mb.showinfo("Message", "Policy Added Successfully")

    def move_forward():
        t1 = entry_1.get()
        t2 = entry_2.get()
        t3 = entry_3.get()
        t4 = entry_4.get()
        t5 = entry_5.get()
        
        if t1 == "" or t2 == "" or t3 == "" or t4 == "" or t5 == "":
            mb.showinfo("Message", "Please fill in every field")
        else:
            flag = True
            pattern = re.compile("^\d{5,8}$")
            if not pattern.match(t2):
                flag = False
                mb.showinfo("Message", "Sum Assurance is not correct")
            if flag == True :
                pattern = re.compile("^\d{3,6}$")
                if not pattern.match(t3):
                    flag = False
                    mb.showinfo("Message", "Premium is not correct")
            if flag == True :
                pattern = re.compile("^\d{1,2}$")
                if not pattern.match(t4):
                    flag = False
                    mb.showinfo("Message", "Tenure is not correct")
            if flag == True :
                    query = "select category_id from category where category_id = %s"
                    mycursor.execute(query, (t5,))
                    if mycursor.rowcount == 0:
                        flag = False
                        mb.showinfo("Message", "Insurance ID is not correct")
            if flag == True :
                t2 = int(t2)
                t3 = int(t3)
                t4 = int(t4)
                
                add_policy_final(t1, t2, t3, t4, t5)
                root.destroy()
                admin()
                
    def move_backword():
        root.destroy()
        admin()

    button_1 = Button(root, text="Back", width=10, bg="yellow", fg="red",
                      font=("Times", 20, "bold"), bd=1, relief="solid",
                      command=move_backword)
    button_1.place(x=90, y=350)
    
    button_2 = Button(root, text="Add", width=10, bg="brown", fg="white",
                      font=("Times", 20, "bold"), bd=1, relief="solid",
                      command=move_forward)
    button_2.place(x=340, y=350)

    root.mainloop()    





def delete_policy():
    root = Tk()
    root.title("Delete Policy")
    root.geometry("600x300+370+150")
    root.resizable(False, False)
    root.configure(bg="#ffffb3")

    label_0 = Label(root, text="Delete Policy",
                    fg="white",
                    bg="red",
                    font="ariel 20 bold",
                    pady=10
                    )
    label_0.pack(fill="both")

    Label(root,
          text="Policy ID",
          font="ariel 15 bold",
          bg="#ffffb3",
          fg="#000000"
          ).place(x=90, y=110)

    e1 = Entry(root, width="20", font=('Arial 15'))
    e1.place(x=260, y=113)

    def move_forward():
        t1 = e1.get()

        if t1 == "":
            mb.showinfo("Message", "Please fill the blank")
        else:
            query = "delete from policy where policy_id = %s"
            mycursor.execute(query, (t1,))
            if mycursor.rowcount == 0:
                mb.showinfo("Message", "Policy ID is not correct")
            else:
                mb.showinfo("Message", "Policy Deleted Successfully")
                root.destroy()
                admin()

    def move_backword():
        root.destroy()
        admin()

    button2 = Button(root, text="Back", width=10, bg="black", fg="white",
                     font=("Times", 15, "bold"), bd=1, relief="solid",
                     command=move_backword)
    button2.place(x=120, y=200)

    button1 = Button(root, text="Delete", width=10, bg="#00ff00", fg="red",
                     font=("Times", 15, "bold"), bd=1, relief="solid",
                     command=move_forward)
    button1.place(x=330, y=200)

    root.mainloop()





def policy_holder():
    root = Tk()
    root.title("Policy Holder")
    root.geometry("1210x540+65+70")
    root.resizable(False, False)
    root.configure(bg="#ffffb3")

    style = ttk.Style()
    style.theme_use('alt')

    my_tree = ttk.Treeview(root)
    my_tree.place(x=20, y=20, width=1170, height=400)

    my_tree.configure(
        columns=(
        "Customer Policy ID",
        "Insurance ID",
        "Insurance Name",
        "Policy ID",
        "Policy Name",
        "User ID",
        "User Name",
        ), show='headings'
    )

    scrollbarx = Scrollbar(my_tree, orient=HORIZONTAL)
    scrollbary = Scrollbar(my_tree, orient=VERTICAL)

    my_tree.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    my_tree.configure(selectmode="extended")

    scrollbary.configure(command=my_tree.yview)
    scrollbarx.configure(command=my_tree.xview)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx.pack(side=BOTTOM, fill=X)
    
    my_tree.heading("#1", text="Customer Policy ID", anchor=CENTER)
    my_tree.heading("#2", text="Insurance ID", anchor=CENTER)
    my_tree.heading("#3", text="Insurance Name", anchor=CENTER)
    my_tree.heading("#4", text="Policy ID", anchor=CENTER)
    my_tree.heading("#5", text="Policy Name", anchor=CENTER)
    my_tree.heading("#6", text="User ID", anchor=CENTER)
    my_tree.heading("#7", text="User Name", anchor=CENTER)
    
    my_tree.column("#1", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#2", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#3", minwidth=300, width=300, anchor=CENTER)
    my_tree.column("#4", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#5", minwidth=300, width=300, anchor=CENTER)
    my_tree.column("#6", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#7", minwidth=200, width=200, anchor=CENTER)
    
    mycursor.execute("select cp.customer_policy_id, c.category_id, \
    c.category_name, p.policy_id, p.policy_name, u.user_id, u.name \
    from customer_policy cp, category c, policy p, user u WHERE \
    cp.category_id = c.category_id and cp.policy_id = p.policy_id \
    and cp.user_id = u.user_id")

    for i in mycursor.fetchall():
        my_tree.insert('', 'end', text='1', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    def move_backword():
        root.destroy()
        admin()

    button1 = Button(root, text="Back", width=10, bg="black", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_backword)
    button1.place(x=1000, y=460)

    root.mainloop()





def sign_up():
    root = Tk()
    root.title("Sign Up")
    root.geometry("610x520+350+90")
    root.resizable(False, False)
    root.configure(bg="#e6ffee")

    label_1 = Label(root, text="Name", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_1.place(x=60, y=30)

    entry_1= Entry(root, width=25, font=("Times", 15))
    entry_1.place(x=300, y=30)

    label_2 = Label(root, text="Gender", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_2.place(x=60, y=90)

    entry_2 = Entry(root, width=25, font=("Times", 15))
    entry_2.place(x=300, y=90)

    label_3 = Label(root, text="Address", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_3.place(x=60, y=150)

    entry_3 = Text(root, width=25, height=2, font=("Times", 15))
    entry_3.place(x=300, y=150)

    label_4 = Label(root, text="Mobile Number", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_4.place(x=60, y=230)

    entry_4 = Entry(root, width=25, font=("Times", 15))
    entry_4.place(x=300, y=230)

    label_5 = Label(root, text="Email", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_5.place(x=60, y=290)

    entry_5 = Entry(root, width=25, font=("Times", 15))
    entry_5.place(x=300, y=290)

    label_6 = Label(root, text="Password", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_6.place(x=60, y=350)

    entry_6 = Entry(root, show="*", width=25, font=("Times", 15))
    entry_6.place(x=300, y=350)

    def sign_up_final(t1,t2,t3,t4,t5,t6):
        query = "insert into user(name, gender, address, \
                 mobile_number, email, password) \
                 values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(query, (t1, t2, t3, t4, t5, t6))
        mb.showinfo("Message", "Account Created Successfully")

    def move_forward():
        t1 = entry_1.get()
        t2 = entry_2.get()
        temp = entry_3.get("1.0", END)
        t3 = temp[0:len(temp) - 1]
        t4 = entry_4.get()
        t5 = entry_5.get()
        t6 = entry_6.get()
        
        if t1 == "" or t2 == "" or t3 == "" or t4 == "" or t5 == "" or t6 == "":
            mb.showinfo("Message", "Please fill in every field")
        else:
            flag = True
            pattern = re.compile("^[a-zA-Z\s]+$")
            if not pattern.match(t1):
                flag = False
                mb.showinfo("Message", "Name is not correct")
            if flag == True:
                flag = False
                if t2.lower()=='male' or t2.lower()=='female':
                    flag = True
                else:
                    mb.showinfo("Message", "Gender is not correct")
            if flag == True :
                pattern = re.compile("^\d{10}$")
                if not pattern.match(t4) or t4[0]=="0" :
                    flag = False
                    mb.showinfo("Message", "Mobile Number is not correct")
            if flag == True :
                pattern = re.compile("[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")
                if not pattern.match(t5):
                    flag = False
                    mb.showinfo("Message", "Email is not correct")
            if flag == True :
                t4 = int(t4)
                sign_up_final(t1, t2, t3, t4, t5, t6)
                root.destroy()
                user_login()
                
    def move_backword():
        root.destroy()
        user_login()

    button_1 = Button(root, text="Back", width=10, bg="yellow", fg="red",
                      font=("Times", 20, "bold"), bd=1, relief="solid",
                      command=move_backword)
    button_1.place(x=90, y=430)
    
    button_2 = Button(root, text="Submit", width=10, bg="brown", fg="white",
                      font=("Times", 20, "bold"), bd=1, relief="solid",
                      command=move_forward)
    button_2.place(x=340, y=430)

    root.mainloop()





def user_login():
    root = Tk()
    root.title("User Login")
    root.geometry("700x420+300+150")
    root.resizable(False, False)
    root.configure(bg="#ccffee")

    label_0 = Label(root,
                    fg="white",
                    bg="red",
                    font="ariel 35 bold",
                    padx=15,
                    pady=9
                )
    label_0.pack(fill="both")

    label_33 = Label(label_0, text="User Login",
                    fg="white",
                    bg="red",
                    font="ariel 35 bold",
                    padx=15,
                    pady=9
                    )
    label_33.place(x=210, y=0)

    Label(root,
          text = "Email",
          font="ariel 20 bold",
          bg="#ccffee",
          fg="#000000"
          ).place(x=90,y=130)

    Label(root,
          text="Password",
          font="ariel 20 bold",
          bg="#ccffee",
          fg="#000000"
          ).place(x=90, y=230)

    e1 = Entry(root, width="30", font=('Arial 15'))
    e1.place(x=260,y=137)

    e2 = Entry(root, show="*", width="30", font=('Arial 15'))
    e2.place(x=260, y=237)

    def user_back_home():
        root.destroy()
        main_menu()

    def move_sign_up():
        root.destroy()
        sign_up()

    button1 = Button(root, text="Back", width=10, bg="brown", fg="white",
                      font=("ariel", 18, "bold"), bd=1, relief="solid",
                      command = user_back_home)
    button1.place(x=70, y=330)

    button2 = Button(root, text="Sign Up", width=10, bg="#ff6600", fg="white",
                      font=("ariel", 18, "bold"), bd=1, relief="solid",
                      command = move_sign_up)
    button2.place(x=270, y=330)

    def login():
        email = e1.get()
        password = e2.get()

        if email=="" or password=="":
            mb.showinfo("Error Message", "Please fill in every field")
        else:
            query = "select email, password from user where email = %s and password = %s"
            mycursor.execute(query, (email, password))
            if mycursor.fetchone():
                query = "select user_id from user where email = %s and password = %s";
                mycursor.execute(query, (email, password))
                i = mycursor.fetchone()
                c_id = i[0]
                root.destroy()
                user(c_id)
            else:
                mb.showinfo("Error Message","Invalid Email and Password")

    button3 = Button(root, text="Login", width=10, bg="blue", fg="white",
                      font=("ariel", 18, "bold"), bd=1, relief="solid",
                      command=login)
    button3.place(x=470, y=330)

    root.mainloop()





def user(user_id):
    root = Tk()
    root.title("User")
    root.geometry("900x400+240+130")
    root.resizable(False, False)
    root.configure(bg="white")

    label_0 = Label(root, text="Welcome User",
                    fg="#990000",
                    bg="#ffff33",
                    font="ariel 35 bold",
                    pady=10
                    )
    label_0.pack(fill="both")

    label_11 = Label(root, text="* * * * *",
                     fg="black",
                     bg="#ffff33",
                     font="ariel 30 bold",
                     )
    label_11.place(x=45, y=15)

    label_12 = Label(root, text="* * * * *",
                     fg="black",
                     bg="#ffff33",
                     font="ariel 30 bold",
                     )
    label_12.place(x=710, y=15)

    find = Image.open("images\\user.jpg")
    my_photo = ImageTk.PhotoImage(find)

    label_1 = Label(root,
                    image=my_photo,
                    bd=0, relief="solid"
                    )
    label_1.place(x=50, y=80)
    
    def logout():
        root.destroy()
        main_menu()

    button0 = Button(root, text="Logout", width=10, bg="black", fg="white",
                     font=("ariel", 20, "bold"), bd=1, relief="solid",
                     command=logout)

    button0.place(x=70, y=300)

    def move_insurance_list():
        root.destroy()
        insurance_list(user_id)

    button1 = Button(root, text="Insurance List", width=20, bg="#006666", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_insurance_list)

    button1.place(x=300, y=140)

    def move_apply_policy():
        root.destroy()
        apply_policy(user_id)

    button2 = Button(root, text="Apply Policy", width=20, bg="green", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_apply_policy)

    button2.place(x=300, y=210)

    def move_view_profile():
        root.destroy()
        view_profile(user_id)

    button3 = Button(root, text="View Profile", width=20, bg="red", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_view_profile)

    button3.place(x=300, y=280)

    def move_policy_list():
        root.destroy()
        policy_list(user_id)

    button4 = Button(root, text="Policy List", width=20, bg="#006666", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_policy_list)

    button4.place(x=600, y=140)

    def move_applied_policy():
        root.destroy()
        applied_policy(user_id)

    button5 = Button(root, text="Applied Policy", width=20, bg="green", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_applied_policy)

    button5.place(x=600, y=210)

    def move_update_profile():
        root.destroy()
        update_profile(user_id)

    button6 = Button(root, text="Update Profile", width=20, bg="red", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_update_profile)

    button6.place(x=600, y=280)

    root.mainloop()





def apply_policy(user_id):
    root = Tk()
    root.title("Apply Policy")
    root.geometry("600x300+370+150")
    root.resizable(False, False)
    root.configure(bg="#ffffb3")

    label_0 = Label(root, text="Apply Policy",
                    fg="white",
                    bg="#000066",
                    font="ariel 20 bold",
                    pady=10
                    )
    label_0.pack(fill="both")

    Label(root,
          text="Policy ID",
          font="ariel 15 bold",
          bg="#ffffb3",
          fg="#000000"
          ).place(x=90, y=110)

    e1 = Entry(root, width="20", font=('Arial 15'))
    e1.place(x=260, y=113)

    def move_forward():
        t1 = e1.get()

        if t1 == "":
            mb.showinfo("Message", "Please fill the blank")
        else:
            query = "select category_id from policy where policy_id = %s"
            mycursor.execute(query, (t1,))
            if mycursor.rowcount == 0:
                mb.showinfo("Message", "Policy ID is not correct")
            else:
                i = mycursor.fetchone()
                query = "insert into customer_policy(user_id, \
                category_id, policy_id) values(%s, %s, %s)"
                mycursor.execute(query, (user_id, i[0], t1))
                mb.showinfo("Message", "Policy Applied Successfully")
                root.destroy()
                user(user_id)

    def move_backword():
        root.destroy()
        user(user_id)

    button2 = Button(root, text="Back", width=10, bg="black", fg="white",
                     font=("Times", 15, "bold"), bd=1, relief="solid",
                     command=move_backword)
    button2.place(x=120, y=200)

    button1 = Button(root, text="Apply", width=10, bg="#00ff00", fg="red",
                     font=("Times", 15, "bold"), bd=1, relief="solid",
                     command=move_forward)
    button1.place(x=330, y=200)

    root.mainloop()





def view_profile(user_id):
    root = Tk()
    root.title("View Profile")
    root.geometry("610x520+350+90")
    root.resizable(False, False)
    root.configure(bg="#e6ffee")

    query = "select * from user where user_id = %s"
    mycursor.execute(query, (user_id,))

    i = mycursor.fetchone()

    name = i[1]
    gender = i[2]
    address = i[3]
    mobile_number = i[4]
    email = i[5]
    password = i[6]

    label_1 = Label(root, text="Name", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_1.place(x=60, y=30)

    mystr_name = StringVar()
    mystr_name.set(name)
    entry_1= Entry(root, textvariable=mystr_name, width=25, font=("Times", 15), state="readonly")
    entry_1.place(x=300, y=30)

    label_2 = Label(root, text="Gender", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_2.place(x=60, y=90)

    mystr_gender = StringVar()
    mystr_gender.set(gender)
    entry_2 = Entry(root, textvariable=mystr_gender, width=25, font=("Times", 15), state="readonly")
    entry_2.place(x=300, y=90)

    label_3 = Label(root, text="Address", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_3.place(x=60, y=150)

    entry_3 = Text(root, width=25, height=2, font=("Times", 15))
    entry_3.insert(END, address)
    entry_3.config(state= DISABLED)
    entry_3.place(x=300, y=150)
    

    label_4 = Label(root, text="Mobile Number", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_4.place(x=60, y=230)

    mystr_mobile_number = StringVar()
    mystr_mobile_number.set(mobile_number)
    entry_4 = Entry(root, textvariable=mystr_mobile_number, width=25, font=("Times", 15), state="readonly")
    entry_4.place(x=300, y=230)

    label_5 = Label(root, text="Email", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_5.place(x=60, y=290)

    mystr_email = StringVar()
    mystr_email.set(email)
    entry_5 = Entry(root, textvariable=mystr_email, width=25, font=("Times", 15), state="readonly")
    entry_5.place(x=300, y=290)

    label_6 = Label(root, text="Password", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_6.place(x=60, y=350)

    mystr_password = StringVar()
    mystr_password.set(password)
    entry_6 = Entry(root, textvariable=mystr_password, width=25, font=("Times", 15), state="readonly")
    entry_6.place(x=300, y=350)

    def move_backword():
        root.destroy()
        user(user_id)

    button_1 = Button(root, text="Back", width=10, bg="yellow", fg="red",
                      font=("Times", 20, "bold"), bd=1, relief="solid",
                      command=move_backword)
    button_1.place(x=210, y=430)
    
    root.mainloop()

    


    
def applied_policy(user_id):
    root = Tk()
    root.title("Applied Policy")
    root.geometry("1210x540+65+70")
    root.resizable(False, False)
    root.configure(bg="#ffffb3")

    style = ttk.Style()
    style.theme_use('alt')

    my_tree = ttk.Treeview(root)
    my_tree.place(x=20, y=20, width=1170, height=400)

    my_tree.configure(
        columns=(
        "Customer Policy ID",
        "Insurance ID",
        "Insurance Name",
        "Policy ID",
        "Policy Name",
        "User ID",
        "User Name",
        ), show='headings'
    )

    scrollbarx = Scrollbar(my_tree, orient=HORIZONTAL)
    scrollbary = Scrollbar(my_tree, orient=VERTICAL)

    my_tree.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    my_tree.configure(selectmode="extended")

    scrollbary.configure(command=my_tree.yview)
    scrollbarx.configure(command=my_tree.xview)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx.pack(side=BOTTOM, fill=X)
    
    my_tree.heading("#1", text="Customer Policy ID", anchor=CENTER)
    my_tree.heading("#2", text="Insurance ID", anchor=CENTER)
    my_tree.heading("#3", text="Insurance Name", anchor=CENTER)
    my_tree.heading("#4", text="Policy ID", anchor=CENTER)
    my_tree.heading("#5", text="Policy Name", anchor=CENTER)
    my_tree.heading("#6", text="User ID", anchor=CENTER)
    my_tree.heading("#7", text="User Name", anchor=CENTER)
    
    my_tree.column("#1", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#2", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#3", minwidth=300, width=300, anchor=CENTER)
    my_tree.column("#4", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#5", minwidth=300, width=300, anchor=CENTER)
    my_tree.column("#6", minwidth=150, width=150, anchor=CENTER)
    my_tree.column("#7", minwidth=200, width=200, anchor=CENTER)
    
    mycursor.execute("select cp.customer_policy_id, c.category_id, \
    c.category_name, p.policy_id, p.policy_name, u.user_id, u.name \
    from customer_policy cp, category c, policy p, user u WHERE \
    cp.category_id = c.category_id and cp.policy_id = p.policy_id \
    and cp.user_id = %s", (user_id,))

    for i in mycursor.fetchall():
        my_tree.insert('', 'end', text='1', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    def move_backword():
        root.destroy()
        user(user_id)

    button1 = Button(root, text="Back", width=10, bg="black", fg="white",
                     font=("ariel", 15, "bold"), bd=1, relief="solid",
                     command=move_backword)
    button1.place(x=1000, y=460)

    root.mainloop()





def update_profile(user_id):
    root = Tk()
    root.title("Update Profile")
    root.geometry("610x520+350+90")
    root.resizable(False, False)
    root.configure(bg="#e6ffee")

    def update_profile_final():
        x1 = entry_1.get()
        x2 = entry_2.get()
        z = entry_3.get("1.0", END)
        x3 = z[0:len(z) - 1]
        x4 = entry_4.get()
        x5 = entry_5.get()
        x6 = entry_6.get()        

        query = "update user set name = %s, gender = %s,\
                address = %s, mobile_number = %s, email = %s, \
                password = %s where user_id = %s"
        mycursor.execute(query, (x1, x2, x3, x4, x5, x6, user_id))

        mb.showinfo("Message", "Profile Updated Successfully")
        root.destroy()
        user(user_id)

    query = "select * from user where user_id = %s"
    mycursor.execute(query, (user_id,))

    i = mycursor.fetchone()

    name = i[1]
    gender = i[2]
    address = i[3]
    mobile_number = i[4]
    email = i[5]
    password = i[6]

    label_1 = Label(root, text="Name", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_1.place(x=60, y=30)

    mystr_name = StringVar()
    mystr_name.set(name)
    entry_1= Entry(root, textvariable=mystr_name, width=25, font=("Times", 15))
    entry_1.place(x=300, y=30)

    label_2 = Label(root, text="Gender", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_2.place(x=60, y=90)

    mystr_gender = StringVar()
    mystr_gender.set(gender)
    entry_2 = Entry(root, textvariable=mystr_gender, width=25, font=("Times", 15))
    entry_2.place(x=300, y=90)

    label_3 = Label(root, text="Address", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_3.place(x=60, y=150)

    entry_3 = Text(root, width=25, height=2, font=("Times", 15))
    entry_3.insert(END, address)
    entry_3.place(x=300, y=150)
    

    label_4 = Label(root, text="Mobile Number", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_4.place(x=60, y=230)

    mystr_mobile_number = StringVar()
    mystr_mobile_number.set(mobile_number)
    entry_4 = Entry(root, textvariable=mystr_mobile_number, width=25, font=("Times", 15))
    entry_4.place(x=300, y=230)

    label_5 = Label(root, text="Email", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_5.place(x=60, y=290)

    mystr_email = StringVar()
    mystr_email.set(email)
    entry_5 = Entry(root, textvariable=mystr_email, width=25, font=("Times", 15))
    entry_5.place(x=300, y=290)

    label_6 = Label(root, text="Password", width=15, font=("bold", 15),
                    fg="brown", bg="skyblue", bd=1, relief="solid")
    label_6.place(x=60, y=350)

    mystr_password = StringVar()
    mystr_password.set(password)
    entry_6 = Entry(root, textvariable=mystr_password, width=25, font=("Times", 15))
    entry_6.place(x=300, y=350)

    def move_backword():
        root.destroy()
        user(user_id)

    button_1 = Button(root, text="Back", width=10, bg="yellow", fg="red",
                      font=("Times", 20, "bold"), bd=1, relief="solid",
                      command=move_backword)
    button_1.place(x=80, y=430)
    
    button_2 = Button(root, text="Update", width=10, bg="brown", fg="white",
                      font=("Times", 20, "bold"), bd=1, relief="solid",
                      command=update_profile_final)
    button_2.place(x=360, y=430)
    
    root.mainloop()





def main_menu():
    root = Tk()
    root.title("Mediclaim Management System")
    root.resizable(False, False)
    root.geometry("880x326+240+180")
        
    label_0 = Label(root,
                    fg="white",
                    bg="red",
                    font="ariel 35 bold",
                    padx=15,
                    pady=9
                )
    label_0.pack(fill="both")

    label_33 = Label(label_0, text="Mediclaim Management System",
                    fg="white",
                    bg="red",
                    font="ariel 35 bold",
                    padx=15,
                    pady=9
                    )
    label_33.place(x=60, y=0)

    find = Image.open("images\home.jpg")
    my_photo = ImageTk.PhotoImage(find)

    label_1 = Label(root,
                    image=my_photo,
                    bd=1, relief="solid"
                    )
    label_1.place(x=0, y=77)

    def move_admin_login():
        root.destroy()
        admin_login()

    def move_user_login():
        root.destroy()
        user_login()
    
    button1 = Button(root, text="Admin", width=20, bg="blue", fg="white",
                      font=("ariel", 20, "bold"), bd=1, relief="solid",
                     command=move_admin_login)
    button1.place(x=470, y=120)

    button2 = Button(root, text="User", width=20, bg="orange", fg="white",
                      font=("ariel", 20, "bold"), bd=1, relief="solid",
                      command = move_user_login)
    button2.place(x=470, y=230)

    root.mainloop()

main_menu()
mycursor.close()
mydb.close()
