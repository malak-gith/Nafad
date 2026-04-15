username = "admin"
password = "1234"
balance = 1000  # assum its 1000

def login():#login function
  while True:# لوب يستمر الى ان تدخل البيانات الصحيحه فقط
    userName =(input("Dear User Enter Your Name:"))
    passWord =(input("Enter Your password:"))
    
    if userName == username and passWord == password:#يقارن المدخلات
      print("Successfuly Login..")
      break
    else:
      print("Access Denied. Try again.")# اذا غلط يطلع من اللوب و يطلب من المستخدم البيانات مره ثانيه
     
      

    
def checkBalance():#function 1
        print("Your balance is:", balance)
        
def deposit():#function 2 تكون void يعني بدون ريتين و برنت
    global balance # لازم نعرفه عشان البرنامج يعرف يفرق بين الاثنين
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("New balance:", balance)
        
def withdraw():#function 3
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:# لازم نحط شرط عشان اذا كان المبلغ اكثر يرسل رفض
            balance -= amount
            print("New balance:", balance)
    else:
            print("Insufficient balance")

    
def main():# main function اهم فنكشن لانه البرنامج يشتغل عليها اصلا فيعرض القائمه اذا المدخلات صحيحه و ترتبط بباقي الفنكشنس
    login()
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    service = input("Enter your choice: ")#input for the list
    if service == "1":
        checkBalance()
    elif service == "2":
        deposit()
    elif service == "3":
        withdraw()
    else:
        print("Invalid choice!")
while True:
 main()  #call main function

                                