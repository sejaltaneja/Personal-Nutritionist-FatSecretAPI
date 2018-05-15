import tkinter
import pickle
from operator import itemgetter
from PIL import ImageTk, Image
import webbrowser
from fatsecret import Fatsecret
import datetime

global root,f1
root = tkinter.Tk()
root.title("Personal Nutritionist")
root.attributes('-fullscreen', True)

fs = Fatsecret('16fab56f70d1452ea8fbc4619b11f3ae', 'ed2efbca053542d688b24b360df70277')

global id_mob
global bmi_w,bmi_h

bmi_h = 0
bmi_w = 0

##########################################

'''
users_list = []

fo = open("Users.pkl", "wb")
pickle.dump(users_list, fo)
fo.close()
'''

def clear_diet_plan():
    fo = open("Diet Plan.pkl", "rb")
    diet_plan = pickle.load(fo)
    fo.close()

    diet_plan = []

    fo = open("Diet Plan.pkl", "wb")
    pickle.dump(diet_plan, fo)
    fo.close()

def view_reccomendations():
    imgs = Image.open("nutri7.jpg")
    imgs = imgs.resize((1362, 763))
    imgs1 = ImageTk.PhotoImage(imgs)
    myimages1 = tkinter.Label(root, image=imgs1)
    myimages1.place(x=0, y=0)

    head = tkinter.Label(root, text="Recommended Diet Plan", fg='maroon', font=("Arial", 30, "bold italic"), bg='#F7DC6F')
    head.place(x=460, y=100)

    frame = tkinter.Frame(root, bg='#F7DC6F')
    frame.place(x=120, y=230, height=500, width=1150)

    back = tkinter.Button(root, text="Back", command=add_diet_plan, fg='maroon', font=("Arial", 17, "bold italic"),
                          bg='#F7DC6F', bd=0)
    back.place(x=60, y=20)

    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                           bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)

    contact = tkinter.Button(root, text="Contact Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                             bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)

    signout = tkinter.Button(root, text="Sign Out", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                             bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)

    labelname = tkinter.Label(root, text="Item", fg='maroon', font=("Arial", 16, "bold italic"), bg='#F7DC6F')
    labelname.place(x=150, y=300)

    labeldesc = tkinter.Label(root, text="Time", fg='maroon', font=("Arial", 16, "bold italic"), bg='#F7DC6F')
    labeldesc.place(x=1030, y=300)

    bmi = (bmi_w*10000)/(bmi_h*bmi_h)

    if bmi<18.5:

        fo = open("Underweight.pkl", "rb")
        diet_plan = pickle.load(fo)
        fo.close()
        l = "Underweight"

    elif bmi>=25:

        fo = open("Overweight.pkl", "rb")
        diet_plan = pickle.load(fo)
        fo.close()
        l = "Overweight"
    else:

        fo = open("Normal.pkl", "rb")
        diet_plan = pickle.load(fo)
        fo.close()
        l = "Normal"

    mylabel = tkinter.Label(root, text="Your BMI is "+str(bmi)+", you are "+l+".", fg='navy', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
    mylabel.place(x=150, y=250)

    num = 340
    for i in diet_plan:
        label1 = tkinter.Label(root, text=i[0], fg='navy', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
        label1.place(x=150, y=num)
        label2 = tkinter.Label(root, text=i[1].time().strftime("%I:%M %p"), fg='navy', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
        label2.place(x=1030, y=num)
        num = num + 30

    root.mainloop()

def view_diet_plan():

    imgs = Image.open("nutri7.jpg")
    imgs = imgs.resize((1362, 763))
    imgs1 = ImageTk.PhotoImage(imgs)
    myimages1 = tkinter.Label(root, image=imgs1)
    myimages1.place(x=0, y=0)

    head = tkinter.Label(root, text="Diet Plan", fg='maroon', font=("Arial", 30, "bold italic"), bg='#F7DC6F')
    head.place(x=460, y=100)

    frame = tkinter.Frame(root, bg='#F7DC6F')
    frame.place(x=120, y=230, height=360, width=1150)

    back = tkinter.Button(root, text="Back", command=add_diet_plan, fg='maroon', font=("Arial", 17, "bold italic"),
                          bg='#F7DC6F', bd=0)
    back.place(x=60, y=20)

    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                           bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)

    contact = tkinter.Button(root, text="Contact Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                             bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)

    signout = tkinter.Button(root, text="Sign Out", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                             bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)


    labelname = tkinter.Label(root, text="Item", fg='maroon', font=("Arial", 16, "bold italic"), bg='#F7DC6F')
    labelname.place(x=150, y=250)

    labeldesc = tkinter.Label(root, text="Time", fg='maroon', font=("Arial", 16, "bold italic"), bg='#F7DC6F')
    labeldesc.place(x=1030, y=250)

    fo = open("Diet Plan.pkl", "rb")
    diet_plan = pickle.load(fo)
    fo.close()

    diet_plan.sort(key=itemgetter(1))

    fo = open("Diet Plan.pkl", "wb")
    pickle.dump(diet_plan, fo)
    fo.close()

    num = 290
    for i in diet_plan:
        if i[2] == id_mob:
            label1 = tkinter.Label(root, text=i[0], fg='navy', font=("Arial", 14, "bold italic"), bg='#F7DC6F')
            label1.place(x=150, y=num)
            label2 = tkinter.Label(root, text=i[1].time().strftime("%I:%M %p"), fg='navy', font=("Arial", 14, "bold italic"), bg='#F7DC6F')
            label2.place(x=1030, y=num)
            num = num + 30

    root.mainloop()

def convertdatetime():

    global id_mob
    remitem = itemtext.get()
    remtime = datetime.datetime.strptime(timetext.get(),'%I:%M %p')

    '''
    itemtext.delete(0, 'end')
    timetext.delete(0, 'end')

    '''

    print(remitem, remtime.time())
    dplist = [ remitem, remtime, id_mob]

    fo = open("Diet Plan.pkl", "rb")
    diet_plan = pickle.load(fo)
    fo.close()

    diet_plan.append(dplist)
    print(diet_plan)

    fo = open("Diet Plan.pkl", "wb")
    pickle.dump(diet_plan, fo)
    fo.close()



    addsucc = tkinter.Label(root, text="Successfully Added!", fg='maroon', font=("Arial", 30, "bold italic"),
                              bg='#F7DC6F')
    addsucc.place(x=460, y=650)

def add_diet_plan():
    global timetext,itemtext

    imgs = Image.open("nutri7.jpg")
    imgs = imgs.resize((1362, 763))
    imgs1 = ImageTk.PhotoImage(imgs)
    myimages1 = tkinter.Label(root, image=imgs1)
    myimages1.place(x=0, y=0)


    back = tkinter.Button(root, text="Back", command=menupage, fg='maroon', font=("Arial", 17, "bold italic"),
                          bg='#F7DC6F', bd=0)
    back.place(x=60, y=20)

    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                           bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)

    contact = tkinter.Button(root, text="Contact Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                             bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)

    signout = tkinter.Button(root, text="Sign Out", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                             bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)

    head = tkinter.Label(root, text="Add Diet Items", fg='maroon', font=("Arial", 30, "bold italic"), bg='#F7DC6F')
    head.place(x=460, y=100)

    itemlabel = tkinter.Label(root, text="Enter Item", fg='maroon', font=("Arial", 30, "bold italic"), bg='#F7DC6F')
    itemlabel.place(x=200, y=250)

    itemtext = tkinter.Entry(root, font=("Arial", 25, "bold italic"), width=21)
    itemtext.place(x=800, y=250)

    datelabel = tkinter.Label(root, text="Enter Time (HH:MM AM/PM)", fg='maroon', font=("Arial", 30, "bold italic"), bg='#F7DC6F')
    datelabel.place(x=200, y=350)

    timetext = tkinter.Entry(root, font=("Arial", 25, "bold italic"), width=21)
    timetext.place(x=800, y=350)

    addbutton = tkinter.Button(root, text="Add!", fg='maroon', font=("Arial", 17, "bold italic"),
                             bg='#F7DC6F', bd=0, command=convertdatetime)
    addbutton.place(x=700, y=550)

    viewbutton = tkinter.Button(root, text="View My Diet Plan", fg='maroon', font=("Arial", 17, "bold italic"),
                               bg='#F7DC6F', bd=0, command=view_diet_plan)
    viewbutton.place(x=800, y=550)

    recbutton = tkinter.Button(root, text="View Recommendation", fg='maroon', font=("Arial", 17, "bold italic"),
                                bg='#F7DC6F', bd=0, command=view_reccomendations)
    recbutton.place(x=400, y=550)

    root.mainloop()

##########################################

def viewrecipe():
    fo = open("Recipes.pkl", "rb")
    recipes_list = pickle.load(fo)
    fo.close()

    for i in recipes_list:
        if (i[0] == id_mob) and (i[1] == textbox3.get()):
            frame = tkinter.Frame(root, bg='#F7DC6F')
            frame.place(x=120, y=310, height=360, width=1150)

            mylabeldesc = tkinter.Label(root, text="Description: ", fg='maroon', font=("Arial", 12, "bold italic"),
                                        bg='#F7DC6F')
            mylabeldesc.place(x=150, y=330)

            mydesc = tkinter.Label(root, text=i[2], fg='navy', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
            mydesc.place(x=300, y=330)

            mylabelservings = tkinter.Label(root, text="No. of Servings: ", fg='maroon',
                                            font=("Arial", 12, "bold italic"),
                                            bg='#F7DC6F')
            mylabelservings.place(x=1000, y=330)

            myservings = tkinter.Label(root, text=i[3], fg='navy', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
            myservings.place(x=1170, y=330)

            mylabeling = tkinter.Label(root, text="Ingredients: ", fg='maroon', font=("Arial", 12, "bold italic"),
                                       bg='#F7DC6F')
            mylabeling.place(x=150, y=380)

            mying = tkinter.Label(root, text=i[4], fg='navy', font=("Arial", 12, "bold italic"), bg='#F7DC6F',
                                  anchor='w', justify='left')
            mying.place(x=300, y=380)

            mylabeldir = tkinter.Label(root, text="  Directions: ", fg='maroon', font=("Arial", 12, "bold italic"),
                                       bg='#F7DC6F')
            mylabeldir.place(x=600, y=380)

            mydir = tkinter.Label(root, text=i[5], fg='navy', font=("Arial", 12, "bold italic"), bg='#F7DC6F',
                                  anchor='w', justify='left')
            mydir.place(x=760, y=380)

def addrecipe():

    frame = tkinter.Frame(root, bg='#F7DC6F')
    frame.place(x=120, y=310, height=360, width=1150)

    labeldesc = tkinter.Label(root, text="Description: ", fg='maroon', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
    labeldesc.place(x=150, y=330)

    desc = tkinter.Text(root, font=("Arial", 12, "bold italic"), width=70, height=1)
    desc.place(x=300, y=330)

    labelservings = tkinter.Label(root, text="No. of Servings: ", fg='maroon', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
    labelservings.place(x=1000, y=330)

    servings = tkinter.Text(root, font=("Arial", 12, "bold italic"), width=6, height=1)
    servings.place(x=1170, y=330)

    labeling = tkinter.Label(root, text="Ingredients: ", fg='maroon', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
    labeling.place(x=150, y=380)

    ing = tkinter.Text(root, font=("Arial", 12, "bold italic"), width=30, height=13)
    ing.place(x=300, y=380)

    labeldir = tkinter.Label(root, text="  Directions: ", fg='maroon', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
    labeldir.place(x=600, y=380)

    dir = tkinter.Text(root, font=("Arial", 12, "bold italic"), width=51, height=13)
    dir.place(x=760, y=380)

    def submit():
        fo = open("Recipes.pkl", "rb")
        recipes_list = pickle.load(fo)
        fo.close()

        myrepname = textbox2.get()
        myrecdesc = desc.get("1.0", 'end-1c')
        myrecserv = servings.get("1.0", 'end-1c')
        myrecing = ing.get("1.0", 'end-1c')
        myrecdir = dir.get("1.0", 'end-1c')

        mylist=[id_mob,myrepname, myrecdesc, myrecserv, myrecing, myrecdir]

        recipes_list.append(mylist)
        print(recipes_list)

        fo = open("Recipes.pkl", "wb")
        pickle.dump(recipes_list, fo)
        fo.close()
        print(recipes_list)

        addsucc = tkinter.Label(root, text="Successfully Added!", fg='maroon', font=("Arial", 12, "bold italic"),
                                bg='#F7DC6F')
        addsucc.place(x=460, y=630)

    sub = tkinter.Button(root, text="Submit", command=submit, fg='maroon', font=("Arial", 12, "bold italic"),
                        bg='white', bd=0)
    sub.place(x=1150, y=630)

def getrecipe():

    frame = tkinter.Frame(root, bg='#F7DC6F')
    frame.place(x=120, y=310, height=360, width=1150)

    recipes = fs.recipes_search(textbox1.get(), max_results=9, page_number=1)

    labelname = tkinter.Label(root, text="Name", fg='maroon', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
    labelname.place(x=150, y=330)

    labeldesc = tkinter.Label(root, text="Description", fg='maroon', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
    labeldesc.place(x=420, y=330)

    labelurl = tkinter.Label(root, text="URL", fg='maroon', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
    labelurl.place(x=1100, y=330)

    num = 360
    for i in recipes:
        label1 = tkinter.Label(root, text=i['recipe_name'], fg='navy', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
        label1.place(x=150, y=num)
        label2 = tkinter.Label(root, text=i['recipe_description'], fg='navy', font=("Arial", 12, "bold italic"),
                               bg='#F7DC6F')
        label2.place(x=420, y=num)

        def callback(event):
            webbrowser.open_new(i['recipe_url'])

        label3 = tkinter.Label(root, text="Get recipe here", fg='blue', font=("Arial", 12, "bold italic"), bg='#F7DC6F',
                               cursor="hand2")
        label3.place(x=1100, y=num)
        label3.bind("<Button-1>", callback)

        num = num + 30

def searchrecipe():

    global textbox1, textbox2, textbox3

    imgs = Image.open("nutri7.jpg")
    imgs = imgs.resize((1362, 763))
    imgs1 = ImageTk.PhotoImage(imgs)
    myimages1 = tkinter.Label(root, image=imgs1)
    myimages1.place(x=0, y=0)


    back = tkinter.Button(root, text="Back", command=menupage, fg='maroon', font=("Arial", 17, "bold italic"),
                          bg='#F7DC6F', bd=0)
    back.place(x=60, y=20)

    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                           bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)

    contact = tkinter.Button(root, text="Contact Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                             bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)

    signout = tkinter.Button(root, text="Sign Out", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                             bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)


    frame1 = tkinter.Frame(root, bg='#ce2d5c')
    frame1.place(x=180, y=150, height=120, width=200)

    label1 = tkinter.Label(root, text="Search a Recipe:", anchor='w', justify='left', fg='white',font=("Arial", 15, "bold italic"),bg='#ce2d5c')

    label1.place(x=195, y=150)

    textbox1 = tkinter.Entry(root, font=("Arial", 12, "bold italic"), width=17)
    textbox1.place(x=195, y=190)

    go1 = tkinter.Button(root, text="GO >", command=getrecipe, fg='maroon', font=("Arial", 12, "bold italic"), bg='white',
                        bd=0)
    go1.place(x=220, y=230)

    frame2 = tkinter.Frame(root, bg='#ce2d5c')
    frame2.place(x=600, y=150, height=120, width=200)

    label2 = tkinter.Label(root, text="Add a recipe:", anchor='w', justify='left', fg='white',
                           font=("Arial", 15, "bold italic"),
                           bg='#ce2d5c')

    label2.place(x=615, y=150)

    textbox2 = tkinter.Entry(root, font=("Arial", 12, "bold italic"), width=17)
    textbox2.place(x=615, y=190)


    go2 = tkinter.Button(root, text="GO >", command=addrecipe, fg='maroon', font=("Arial", 12, "bold italic"), bg='white',
                         bd=0)
    go2.place(x=650, y=230)

    frame3 = tkinter.Frame(root, bg='#ce2d5c')
    frame3.place(x=1000, y=150, height=120, width=200)

    label3 = tkinter.Label(root, text="View your recipes:", anchor='w', justify='left', fg='white',
                           font=("Arial", 15, "bold italic"),
                           bg='#ce2d5c')

    label3.place(x=1015, y=150)

    textbox3 = tkinter.Entry(root, font=("Arial", 12, "bold italic"), width=17)
    textbox3.place(x=1015, y=190)

    go3 = tkinter.Button(root, text="GO >", command=viewrecipe, fg='maroon', font=("Arial", 12, "bold italic"), bg='white',
                         bd=0)
    go3.place(x=1050, y=230)

    root.mainloop()

##########################################

def displayfood():

    frame = tkinter.Frame(root, bg='#F7DC6F')
    frame.place(x=120, y=230, height=360, width=1150)

    foods = fs.foods_search(search_textbox.get())

    for i in foods:
        if i['food_type'] != 'Generic':
            foods.remove(i)

    foods = foods[0:9]

    labelname = tkinter.Label(root, text="Name", fg='maroon', font=("Arial", 16, "bold italic"), bg='#F7DC6F')
    labelname.place(x=150, y=250)

    labeldesc = tkinter.Label(root, text="Description", fg='maroon', font=("Arial", 16, "bold italic"), bg='#F7DC6F')
    labeldesc.place(x=630, y=250)

    num = 290
    for i in foods:
        label1 = tkinter.Label(root, text=i['food_name'], fg='navy', font=("Arial", 12, "bold italic"), bg='#F7DC6F')
        label1.place(x=150, y=num)
        label2 = tkinter.Label(root, text=i['food_description'], fg='navy', font=("Arial", 12, "bold italic"),
                               bg='#F7DC6F')
        label2.place(x=630, y=num)
        num = num + 30

def searchfood():

    global search_textbox
    imgs= Image.open("nutri7.jpg")
    imgs = imgs.resize((1362,763))
    imgs1 = ImageTk.PhotoImage(imgs)
    myimages1 = tkinter.Label(root, image = imgs1)
    myimages1.place(x=0, y=0)

    head = tkinter.Label(root, text="    Enter Food Item:", anchor='w', justify='left', fg='white', font=("Arial", 17, "bold italic"),
                         bg='#ce2d5c', width=45)
    head.place(x=340, y=150)

    search_textbox = tkinter.Entry(root, font=("Arial", 17, "bold italic"), width=17)
    search_textbox.place(x=630, y=150)

    go = tkinter.Button(root, text="Go >", command=displayfood, fg='maroon', font=("Arial", 12, "bold italic"), bg='white', bd=0)
    go.place(x=900, y=150)

    back = tkinter.Button(root, text="Back", command=menupage, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    back.place(x=60, y=20)

    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)

    contact = tkinter.Button(root, text="Contact Us", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)

    signout = tkinter.Button(root, text="Sign Out", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"),
                             bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)

    '''
    var = tkinter.StringVar(root)
    var.set(TIMESLOTS[0])

    pt_dd = tkinter.OptionMenu(root, var, *TIMESLOTS)
    pt_dd.config(font=("Arial", 12, "bold italic"), width=15, bg="white")
    pt_dd.place(x=140,y=390)

    dt = tkinter.Label(root, text="Drop off time:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    dt.place(x=140, y=440)

    dt_entry = tkinter.Entry(root, font=("Arial", 12, "bold italic"), width=19)
    #dt_entry.insert(0,time.strftime("%x")+" "+time.strftime("%I")+":"+time.strftime("%M")+" "+time.strftime("%p"))
    dt_entry.insert(0,"dd/mm/yyyy")
    dt_entry.place(x=140, y=470)
    #dt_entry.insert(time.strftime("%c"))
    '''

    root.mainloop()

##########################################

def menupage():

    global recipe_textbox
    #f1 = tkinter.Frame(root, bg="#FFA07A")
    #f1.place(height=2000, width=2000)

    img= Image.open("nutri7.jpg")
    img = img.resize((1362,763))
    img1 = ImageTk.PhotoImage(img)
    myimage1 = tkinter.Label(root, image = img1)
    myimage1.place(x=0, y=0)

    back = tkinter.Button(root, text="Back", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    back.place(x=60, y=20)

    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)

    contact = tkinter.Button(root, text="Contact Us", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)

    signout = tkinter.Button(root, text="Sign Out", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)

    search = tkinter.Button(root, command=searchfood)
    button1 = Image.open("facts.jpg")
    button1 = button1.resize((320, 400), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(button1)
    search.config(image=image1, bd=0)
    search.image = image1
    search.grid(row=1, column=1, padx=100, pady=120)

    recipe = tkinter.Button(root, command=searchrecipe)
    button2 = Image.open("recipe.jpg")
    button2 = button2.resize((320, 400), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(button2)
    recipe.config(image=image2)
    recipe.image = image2
    recipe.grid(row=1, column=2, pady=120)

    myaccount = tkinter.Button(root, command=add_diet_plan)
    button3 = Image.open("diet.jpg  ")
    button3 = button3.resize((320, 400), Image.ANTIALIAS)
    image3 = ImageTk.PhotoImage(button3)
    myaccount.config(image=image3)
    myaccount.image = image3
    myaccount.grid(row=1, column=3, padx=100, pady=120)

    head = tkinter.Label(root, text="Get Healthy with NUTRIFRIEND",fg='white', font=("Arial", 35, "bold italic"), bg='#ce2d5c', width=50)
    head.place(x=0, y=590)

    root.mainloop()

def signup():

    global name, mob, id_mob, bmi_h, bmi_w
    name=name_textbox.get()
    mob=mobile_textbox.get()
    pw=pass_textbox.get()
    ht=height_textbox.get()
    wt=weight_textbox.get()

    mylist=[name, mob, pw, ht, wt]
    if name=='' or mob=='' or pw=='':
        error = tkinter.Label(root, text="Empty fields",fg='red', font=("Arial", 10, "bold italic"), bg='#F7DC6F')
        error.place(x=830 , y=485)
        menupage()
    else:
        fo = open("Users.pkl", "rb")
        users_list = pickle.load(fo)
        fo.close()

        users_list.append(mylist)
        print(users_list)

        fo = open("Users.pkl", "wb")
        pickle.dump(users_list, fo)
        fo.close()
        id_mob = mylist[1]
        bmi_h = float(mylist[3])
        bmi_w = float(mylist[4])
        print((bmi_h, bmi_w, id_mob))
        menupage()

def login():
    #global mob
    global id_mob, bmi_w,bmi_h
    mob = mob_textbox.get()
    pw = pw_textbox.get()

    fo = open("Users.pkl", "rb")
    users_list = pickle.load(fo)
    fo.close()

    for row in users_list:
            if ( row[1]== mob and row[2]== pw):
                bmi_h = float(row[3])
                bmi_w = float(row[4])
                id_mob = mob
                print((bmi_h,bmi_w,id_mob))
                menupage()
            else:
               error = tkinter.Label(root, text="Wrong ID / Password",fg='red', font=("Arial", 11, "bold italic"), bg='#F7DC6F')
               error.place(x=1095 , y=470)

def main_fun():

    global mob_textbox, pw_textbox, name_textbox, mobile_textbox, pass_textbox, height_textbox, weight_textbox
    img= Image.open("nutri6final.png")
    img = img.resize((1362,763))
    img1 = ImageTk.PhotoImage(img)
    myimage1 = tkinter.Label(root, image = img1)
    myimage1.place(x=0, y=0)

    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)

    contact = tkinter.Button(root, text="Contact Us", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)

    signout = tkinter.Button(root, text="Exit", command = root.destroy, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)


    #SIGN UP
    sframe = tkinter.Frame(root, bg="#F7DC6F")
    sframe.place(x=750, y=250, height=370, width=250)

    name_label = tkinter.Label(root, text="Name:",fg='maroon', font=("Arial", 14, "bold italic"), bg='#F7DC6F')
    name_label.place(x=780, y=265)

    name_textbox = tkinter.Entry(root, font=("Arial", 13, "bold italic"), width=21)
    name_textbox.place(x=780, y=290)

    mobile_label = tkinter.Label(root, text="Mobile:",fg='maroon', font=("Arial", 14, "bold italic"), bg='#F7DC6F')
    mobile_label.place(x=780, y=320)

    mobile_textbox = tkinter.Entry(root, font=("Arial", 13, "bold italic"), width=21)
    mobile_textbox.place(x=780, y=345)

    pass_label = tkinter.Label(root, text="Create Password:",fg='maroon', font=("Arial", 14, "bold italic"), bg='#F7DC6F')
    pass_label.place(x=780, y=375)

    pass_textbox = tkinter.Entry(root, show="*", font=("Arial", 13, "bold italic"), width=21)
    pass_textbox.place(x=780, y=400)

    height_label = tkinter.Label(root, text="Height:", fg='maroon', font=("Arial", 13, "bold italic"), bg='#F7DC6F')
    height_label.place(x=780, y=435)

    height_textbox = tkinter.Entry(root, font=("Arial", 13, "bold italic"), width=10)
    height_textbox.place(x=780, y=460)
    height_textbox.insert(0,"in cms")

    weight_label = tkinter.Label(root, text="Weight:", fg='maroon', font=("Arial", 13, "bold italic"), bg='#F7DC6F')
    weight_label.place(x=878, y=435)

    weight_textbox = tkinter.Entry(root, font=("Arial", 13, "bold italic"), width=10)
    weight_textbox.place(x=879, y=460)
    weight_textbox.insert(0, "in kgs")

    b1 = tkinter.Button(root, command=signup)
    button1 = Image.open("signup.jpg")
    button1 = button1.resize((80,80), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(button1)
    b1.config(image=image1)
    b1.image = image1
    b1.place(x=830, y=510)

    #LOGIN
    lframe = tkinter.Frame(root, bg='#F7DC6F')
    lframe.place(x=1050, y=250, height=370, width=250)

    mob_label = tkinter.Label(root, text="Mobile:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    mob_label.place(x=1080, y=300)

    mob_textbox = tkinter.Entry(root, font=("Arial", 15, "bold italic"), width=17)
    mob_textbox.place(x=1080, y=340)

    pw_label = tkinter.Label(root, text="Password:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    pw_label.place(x=1080, y=380)

    pw_textbox = tkinter.Entry(root, show="*", font=("Arial", 15, "bold italic"), width=17)
    pw_textbox.place(x=1080, y=420)

    b2 = tkinter.Button(root, command=login)
    button2 = Image.open("login.jpg")
    button2 = button2.resize((80,80), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(button2)
    b2.config(image=image2)
    b2.image = image2
    b2.place(x=1130, y=510)

    root.mainloop()

main_fun()


