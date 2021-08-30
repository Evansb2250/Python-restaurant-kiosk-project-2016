from tkinter import *



class Functionality():
    state = True
    index = 0
    finalPrice = 0

    mealPrice = {0 :{"name" : "Cheese Burger $1.29", "price": 1.29, "quanitity": 0},
             1 :{"name" : "Bacon Burger $1.99", "price": 1.99, "quanitity": 0},
             2 :{"name" : "Double Cheese Burger $1.79", "price": 1.79, "quanitity": 0},
             3 :{"name" : "Texas Melt $2.09", "price": 2.09, "quanitity": 0},
             4 :{"name" : "Chicken Burger $4.05", "price": 4.05, "quanitity": 0},
             5 :{"name" : "Small Fry $0.99", "price": 0.99, "quanitity": 0},
             6 :{"name" : "Medium Fry $1.44", "price": 1.44, "quanitity": 0},
             7 :{"name" : "Large $2.00", "price": 2.00, "quanitity": 0},
             8 :{"name" : "Apple slice $1.00", "price": 1.00, "quanitity": 0},
             9 :{"name" : "10 piece Chicken Nuggets $3.00", "price": 3.00, "quanitity": 0},
            10 :{"name" : "Small drink $0.89", "price":.89, "quantity":0},
            11 :{"name" : "Medium drink $1.09", "price":1.09, "quantity":0},
            12 :{"name" : "Vanilla Ice Cream $2.50", "price":2.50, "quantity":0},
            13 :{"name" : "Chocolate Ice Cream $2.50", "price":2.50, "quantity":0},
            14 :{"name" : "Strawberry Ice Cream $2.50", "price":2.50, "quantity":0},
            15 :{"name" : "Fudge Sundae $3.50", "price":3.50, "quantity":0},
            16 :{"name" : "Large drink $1.50", "price":1.50, "quantity":0}}


    def passwordCheck(self, username, password):
        fileExist = True
        try:
            file = open("users.txt", "r")
            users = file.readlines()
            file.close()
        except IOError :
            fileExist = False
            messagebox.showinfo("", "No users created for system\nPlease sign up")
            
        if(fileExist): 
            for x in range(len(users)):
                if(username.lower() in users[x]):
                    line = str(users[x])
                    line = line.split(" ")
                    name = line[0]
                    realPassword = line[1]
                    if(username.lower() == name and password == realPassword.strip()):
                        return True
                    else:
                        return False

    def add_to_database(self,username, password, fullname):
        validUserName = True
        #read database
        try:
            data = open("users.txt", "r")
            file = []
            file = data.readlines()
            data.close()

            for x in range(len(file)):
                if(username.lower() in file[x].strip()):
                    validUserName = False
        except IOError:
            messagebox.showinfo("", "Setting up a new database")
            

        if(validUserName == True):
            writeToFile = open("users.txt", "+a")
            writeToFile.write(username.lower() + " " +password +" " + fullname+"\n")
            writeToFile.close()

        else:
            return False

        return True

    

    def calculate_price(self, cartTuple, amountObj):
        total = 0
        for item in range(len(cartTuple)):
          for priceMenu in range(len(self.mealPrice)):
             if(cartTuple[item].strip() in self.mealPrice[priceMenu]["name"].strip()):
                total += self.mealPrice[priceMenu]["price"]

        total = round(total,2)
        self.finalPrice = total
        self.update(amountObj, total)













class GUI(Frame, Functionality):
    customFont = ("Arial", 10)
    frontScreenOn = True
    color2 = "#d1d1e0"
    buttonColor = "#b3b3cc"
    color = "#66b3ff"

  

    def __init__(self, master):
        super(GUI, self).__init__(master)
        self.grid()
        self.login_interface()
        self.ordering_interface()
        
        


    def login_interface(self):
        loginInterface = Frame(self, bg = self.color)

        container = LabelFrame(loginInterface, text="Welcome to Inovation",font = self.customFont ,bg = self.color)
        container.grid(row = 0, column = 1 ,padx =(20 ,80), pady=(30,30))
        
      
        # Widgets inside the Label Frame
        userNameLabel = Label(container, text ="Username", font = self.customFont,bg = self.color)
        userNameLabel.grid(row = 0, column = 0, padx = (20,0), pady= (20,0))

        passwordLabel = Label(container, text="Password", font = self.customFont, bg = self.color)
        passwordLabel.grid(row = 1, column = 0, padx = (20,0), pady =(0,20))

        userName = Entry(container)
        userName.grid(row = 0, column = 1, padx =(10,20),pady= (20,0))

        password = Entry(container, show = "*")
        password.grid(row = 1, column = 1, pady =(0,20), padx =(10,20))

        cancelButton = Button(container, text = "Cancel", font = self.customFont,bd = 6, command = self.end_software)
        cancelButton.grid(row = 2, column = 1 ,padx = (0, 40), pady=(0,10))

        enterButton = Button(container, text = "Enter", font = self.customFont, bd = 6, command = lambda : self.logAccepted(userName.get(), password.get(), loginInterface))
        enterButton.grid(row = 2, column = 1, padx = (100,20), pady=(0,10))


            
        registerLabel = Label(loginInterface, text = "New Employees", font = self.customFont, bg = self.color)
        registerLabel.grid(row = 0, column = 0, padx = (20, 0),pady =(0, 20))

        registerButton = Button(loginInterface, text = "Click Me",bd = 2, font = self.customFont, command = lambda : self.bring_up_signup_interface(loginInterface) )
        registerButton.grid(row = 0, column = 0, padx = (20, 0), pady =(40, 0))

        
        # End of Login Interface
        loginInterface.grid()



    def signup_interface(self):
        signUpFrameInterface = Frame(self, bg = self.color)
        
        labelframe = LabelFrame(signUpFrameInterface, text="Registration Page", font = self.customFont, bg = self.color)
        labelframe.grid(padx =(30,30), pady=(30,30))

        titleLabel = Label(labelframe, text ="MANAGER PROFILE SETUP", font = self.customFont ,bg = self.color)
        titleLabel.grid(row = 0, column = 0, columnspan = 13, pady=(0,70))
        
        # First and Last Name
        firstNameLabel = Label(labelframe,  text= "first name:", font = self.customFont, bg = self.color)
        firstNameLabel.grid(row = 0, column = 0, pady=(30,0))
    
        lastNameLabel = Label(labelframe,  text= "last name:", font = self.customFont, bg = self.color)
        lastNameLabel.grid(row = 0, column = 2, pady=(30,0))

        userNameLabel = Label(labelframe,  text= "username:", font = self.customFont , bg = self.color)
        userNameLabel.grid(row = 5, column = 0, pady =(50, 0))
    
        passwordLabel = Label(labelframe,  text= "password:",font = self.customFont ,bg = self.color)
        passwordLabel.grid(row = 5, column = 2,pady= (50,0))
    
        confirmPasswordLabel = Label(labelframe,  text= "confirm password:", font = self.customFont ,bg = self.color)
        confirmPasswordLabel.grid(row = 6, column = 2)

        firstName = Entry(labelframe, bd = 4)
        firstName.grid(row = 0, column = 1, pady=(30,0))
    
        lastName= Entry(labelframe,  bd = 4)
        lastName.grid(row = 0, column = 3, padx=(0, 50), pady=(30,0))

        # 6
        userName = Entry(labelframe,  bd = 4)
        userName.grid(row = 5, column = 1, pady= (50,0))
        # 7
        password = Entry(labelframe,  bd = 4, show="*")
        password.grid(row = 5, column = 3, pady= (50,0))
        # 8
        confirmPassword = Entry(labelframe,  bd = 4, show="*")
        confirmPassword.grid(row = 6, column = 3)

        submitButton = Button(labelframe,  text ="SUBMIT",font = self.customFont , bd = 10, command = lambda : self.new_account(firstName,lastName, userName, password, confirmPassword,
                                                                                                                                signUpFrameInterface))
        submitButton.grid(row = 7, column = 5, pady= (10, 0))

        cancelButton = Button(labelframe,  text ="CANCEL",font = self.customFont, bd = 10, command = lambda : self.restore_login_interface(signUpFrameInterface))
        cancelButton.grid(row = 7, column = 3, pady=(10, 0))


        
        
        #End of Sign Up Interface
        signUpFrameInterface.grid()








    def restore_login_interface(self, signUpFrameInterface):
        signUpFrameInterface.grid_forget()
        self.login_interface()



    def previous_layout(self, objContainer):
        self.variable = objContainer
        
        






    def bring_up_signup_interface(self, loginInterface):
        loginInterface.grid_forget()
        self.signup_interface()



    def logAccepted(self, user, password, loginInterface):

        if(self.passwordCheck(user, password)):
            loginInterface.grid_forget()
            self.frontscreen_interface()
            self.control_panel()
          #  self.ordering_interface()
            super(GUI,self).config(bg= self.color2)
        else:
            messagebox.showerror("","Invalid input")



    def end_software(self):
        root.destroy()


    def new_account(self, firstName, lastName, username, password,confirmPassWord, signUpFrameInterface):
        completedRequirements = False
        
        if(firstName.get().strip() != ""):
            if(lastName.get().strip() != ""):
                if(password.get().strip() != ""):
                    if(confirmPassWord.get().strip() != ""):
                        if(username.get().strip() != ""):
                            if(password.get() != confirmPassWord.get()):
                                messagebox.showerror("","Passwords dont match")
                            else:
                                completedRequirements = True  
                                fullname = firstName.get() +  " " +lastName.get()
                                usernameToBeConfirmed = username.get()
                                passwordConfirm = password.get()
                                if(self.add_to_database(usernameToBeConfirmed, passwordConfirm, fullname) == True):
                                    signUpFrameInterface.grid_forget()
                                    self.login_interface()
                                else:
                                    messagebox.showerror("","User name already Exist")
                            

        if(completedRequirements == False):
            messagebox.showerror("","please complete the form")
                        
                





    def control_panel(self):
        global loginInterface 
        loginInterface = Frame(self,width = 10,bg = self.color2)
         
        
        homeButton = Button(loginInterface, width = 15, height = 5, bd = 7, bg = self.buttonColor, text= "Login/Logout", command = lambda : self.current_interface("home screen"))
        homeButton.grid(row = 0, column = 0, padx = (0, 0),  pady=(0,0))

        orderButton = Button(loginInterface,width = 15, height = 5, bd = 7, bg = self.buttonColor, text = "Orders", command = lambda : self.current_interface("order system"))
        orderButton.grid(row = 3, column =0, padx = (0, 0))

      
        # End of Login Interface
        loginInterface.grid(row = 0, column = 0)



    def frontscreen_interface(self):
        global frontMenuContainer
  
        frontMenuContainer = LabelFrame(self, text = "Sign In/ Sign Out", bg = self.color2)
        frontMenuContainer.grid(row = 0, column = 1, pady = (20, 20), padx = (100,70))
        
        frontMenuContainer.grid(row = 0, column = 1, pady = (20, 20), padx = (100,70))
        frontMenuContainer.grid(row = 0, column = 1, pady = (20, 20), padx = (100,70))
        clockInButton = Button(frontMenuContainer, text = "Go back to login", bd =10, height =10, width = 20,font = ("Helvetica",14), command = self.back_to_sign_up)
        clockOutButton = Button(frontMenuContainer, text = "Clock Out", bd = 10, height =10, width = 20,font = ("Helvetica",14), command = self.end_software)

        clockInButton.grid(row = 0, column = 0, columnspan = 2, pady = (30,30), padx =(50,0))
        clockOutButton.grid(row = 0, column = 3, columnspan = 2, padx = (80, 50))


        


    def ordering_interface(self):
            global orderLayout
            orderLayout = Frame(self, bg = self.color2)
            
            
            container = LabelFrame(orderLayout, text="How can I Take Your Order", bg = self.color2)
            container.grid(row = 0, column = 1, padx = (0, 10), pady = (10, 0))

            padding = (10, 0)
        
            
           

            # Burger setup
            burger = StringVar(container)
            burger.set("Select a Burger")
            burgerMenu = OptionMenu(container, burger ,"NO Burgers", "Cheese Burger $1.29",
                              "Bacon Burger $1.99", "Double Cheese Burger $1.79",
                              "Texas Melt $2.09","Chicken Burger $4.05")
            burgerMenu.grid(row = 1, column = 0, padx = padding)
            #Burger Quantity Setup
            bQuantity = StringVar(container)
            bQuantity.set("Quantity")
            burgerQuantity = OptionMenu(container, bQuantity,"0","1","2","3","4","5")
            burgerQuantity.grid(row = 1, column = 2)

            #Setting up side layout
            side = StringVar(container)
            side.set("Select a Side")
            sideMenu = OptionMenu(container, side ,"No Sides", "Small Fry $0.99",
                              "Medium Fry $1.44", "Large $2.00",
                              "Apple slice $1.00", "10 piece Chicken Nuggets $3.00")

            sideMenu.grid(row = 2, column = 0 , padx = padding)
            sideQuantity = StringVar(container)
            sideQuantity.set("Quantity")
            sideQuantityMenu = OptionMenu(container, sideQuantity, "0", "1", "2", "3", "4", "5")
            sideQuantityMenu.grid(row = 2, column = 2)

            #Setting Up drink Menu Layout
            drinkSize  = StringVar(container)
            drinkSize.set("Select a drink Size")
            setDrinkSize = OptionMenu(container, drinkSize, "No Drink","Small drink $0.89","Medium drink $1.09","Large drink $1.50")
            setDrinkSize.grid(row = 3, column = 0, padx = (20, 0))
            
            drinkQuantity = StringVar(container)
            drinkQuantity.set("Quantity")
            setDrinkQuantity = OptionMenu(container, drinkQuantity, "0","1","2","3","4","5")
            setDrinkQuantity.grid(row = 3, column = 2)
            
            
            dessert = StringVar(container)
           

            # Setting Desert Layout
            dessert.set("Select a Desert")
            dessertMenu = OptionMenu(container, dessert ,"NO Dessert", "Vanilla Ice Cream $2.50",
                              "Chocolate Ice Cream $2.50", "Strawberry Ice Cream $2.50", "Fudge Sundae $3.50")
            dessertMenu.grid(row = 4, column = 0, padx = padding)

            desertQuantity = StringVar(container)
            desertQuantity.set("Quanitity")
            setdesertQuantity = OptionMenu(container, desertQuantity, "Quanitity","1","2","3","4,","5")
            setdesertQuantity.grid(row = 4, column = 2)

            
            

            # Buttons
            addButton = Button(container, text = "Add to Cart", bd=5,font = self.customFont, bg = self.buttonColor, command = lambda : self.cart(cartList,burger.get(), bQuantity.get(), amount))
            addButton.grid(row = 1, column = 4)

            addButton2 = Button(container, text = "Add to Cart", bd=5,font = self.customFont, bg = self.buttonColor, command = lambda : self.cart(cartList,side.get(), sideQuantity.get(), amount))
            addButton2.grid(row = 2, column = 4)

            addButton3 = Button(container, text = "Add to Cart", bd=5,font = self.customFont, bg = self.buttonColor, command = lambda : self.cart(cartList, drinkSize.get()
                                                                                                                                              , drinkQuantity.get(), amount))
            addButton3.grid(row = 3, column = 4)

            addButton4 = Button(container, text = "Add to Cart", bd=5,font = self.customFont, bg = self.buttonColor, command = lambda : self.cart(cartList,dessert.get(),
                                                                                                                                                  desertQuantity.get(), amount))
            addButton4.grid(row = 4, column = 4)

            resetButton = Button(container, text = "Reset", bd = 5, font = self.customFont, bg = self.buttonColor, command =lambda : self.reset_all(cartList, amount, customerChange))
            resetButton.grid(row = 5, column = 2)


            

            removeItemButton = Button(container, text = "Remove", bd = 4,font = self.customFont, bg = self.buttonColor, command = lambda : self.remove_from_cart(cartList, amount) )
            removeItemButton.grid(row = 9, column = 5, padx = (40,80) ,pady =(5, 20))

            doneButton = Button(container, text="Done", bd = 4, font = self.customFont, bg= self.buttonColor, command = lambda : self.enable_payment(enterPayment))
            doneButton.grid(row = 9 , column =5 , padx = (90,0 ),pady = (5,20))

            #List Box
            cartLabel = Label(container, text = "Your Order", font = ("Helvetica", 20 ), bg = self.color2)
            cartLabel.grid(row = 0, column = 5)
            cartList = Listbox(container, width = 40, height = 20)
            cartList.grid(row = 1, column = 5, rowspan = 8, padx = (80,20), pady=(0,0))
            
            paymentLabel = Label(container, text ="Payment:",  font = ("Helvetica",14), bg =self.color2)
            paymentLabel.grid(row = 8, column = 3, padx = (40,0))

            enterPayment = Entry(container, bd = 4, state="disabled")
            enterPayment.grid(row=8 , column = 3, pady =(50,0),padx = (40,0))

            payButton = Button(container, bd =5, text = "Complete Transaction", bg = self.buttonColor, command = lambda : self.make_payment(enterPayment, amount, customerChange))
            payButton.grid(row =9, column =3, padx = (40,0))
            
            customerChange = Label(container, text = "Customer change:$0.00",  font = ("Helvetica",14), bg = self.color2)
            customerChange.grid(row = 14, column = 5, pady =(0,0))

            amount = Label(container, text = "Order Amount\ntotal: $0.00 ", font = ("Helvetica", 14), bg = self.color2)
            amount.grid(row = 14, column = 4, padx = (40, 10), pady =(0,0))




    def current_interface(self, interface):
        #self.remove()
        
        if(interface == "order system"):
            orderLayout.grid(row = 0, column = 1)
            frontMenuContainer.grid_forget()
            

        else:
            frontMenuContainer.grid(row = 0, column = 1, pady = (20, 20), padx = (100,70))
            orderLayout.grid_forget()





    def cart(self,obj, menuItem, numberOfItems, amountObj):
       try:
           if("NO" in menuItem):
               messagebox.showinfo("User input error","please Select a meal of the menu")
           elif("Quantity" in numberOfItems):
               messagebox.showinfo("User input error","please Select a quantity amount")
           else:
               for x in range(int(numberOfItems)):
                   obj.insert( END , menuItem)
                   self.index += int(numberOfItems)
                   cartContents = obj.get(0, self.index)
                   
                   self.calculate_price(cartContents, amountObj)
       except ValueError:
           messagebox.showinfo("User input error"," invalid request\nplease make adjustment to your order")
           
        
       
    


    def update(self,obj, total):
       obj.config(text = "Amount\ntotal: $" + str(total))



    def remove_from_cart(self, obj, amountLabel):
       item_index = obj.curselection()
       if(len(item_index) <= 0):
           messagebox.showinfo("","No item has been selected to be removed")
       else:
           obj.delete(item_index)
           contents = obj.get(0, self.index)
           self.calculate_price(contents, amountLabel)



    def enable_payment(self, payObj):
       if(self.state):
           payObj.config(state = "normal")
       else:
           messagebox.showinfo("","Please press the reset button before taking another order")





    def make_payment(self, enterPayment, amount, customerChange):
       try: 
           cashpayment = float(enterPayment.get())
           enterPayment.delete(0, 5)
           if(self.finalPrice == 0):
              messagebox.showinfo("","Cart List is empty")

           elif(cashpayment >= self.finalPrice):
              amount.config(text = "Order Amount total:\n$0.00")
              customerChange.config(text = "Customer Change : " + str(round((cashpayment - self.finalPrice), 2)))
              enterPayment.config(state ="disabled")
              self.state = False
           else:
              messagebox.showerror("","Funds insufficient")
       except (ValueError):
            messagebox.showerror("input error","Please enter numbers only")







    def reset_all(self, cartList, amount, customerChangeLabel):
          cartList.delete(0, self.index)
          zeroContent = ""
          self.state = True
          customerChangeLabel.config(text="Customer change:$0.00")
          
          


          self.calculate_price(zeroContent,amount)
          
       
          
       

    def back_to_sign_up(self):
        loginInterface.grid_forget()
        frontMenuContainer.grid_forget()
        self.login_interface()









root = Tk()
root.title("Innovation Management ")
app = GUI(root)


root.mainloop()

        

