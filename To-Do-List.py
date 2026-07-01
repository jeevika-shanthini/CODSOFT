to_do_list=[]
def add_task():
    task=input("Enter a task: ")
    to_do_list.append({"Task":task,"Status":"Pending"})
    print("New task added successfully!\n")


def veiw_task():
    print("_"*25)
    print("Your To Do List:")
    print("_"*25)
    if(len(to_do_list)==0):
        print("No pending tasks!")
    else:
        for index,task in enumerate(to_do_list,1):
            print(f"{index}:{task['Task']}-{task['Status']}")    
    print("_"*25)
    print("\n")   

def remove_task():
    if(len(to_do_list)==0):
        print("List is Empty!")
    else:
        try:
            search_index=int(input("Enter the task number that you want to remove: "))-1
            if 0<=search_index<len(to_do_list):
                removed_task=to_do_list.pop(search_index)
                print(f"Task Removed: {removed_task['Task']}")
            else:
                print("Invalid task number")    
        except ValueError:
            print("Please enter a valid number")


def mark_as_done():
    if(len(to_do_list)==0):
        print("List is Empty!")
    else:
        try:
            search_index=int(input("Enter the task number that you want to mark as compeleted: "))-1
            if 0<=search_index<len(to_do_list):
                to_do_list[search_index]['Status']='done'
                print(f"Task {to_do_list[search_index]['Task']}has been marked as Done.")
            else:
                print("Invalid task number")    
        except ValueError:
            print("Please enter a valide number")

def menu():
    while True:
        print('-'*25)
        print("****** MAIN MENU ******")
        print('-'*25)
        print("1.|  Add a New Task")
        print("2.|  veiw All Task")
        print("3.|  Remove a Task")
        print("4.|  Mark a Task as Compeleted")
        print("5.|  Exit")
        print('-'*25)

        choice=input("Enter your choice:")
        if choice=="1":
            add_task()
        elif choice=="2":
            veiw_task()
        elif choice=="3": 
            remove_task()
        elif choice=="4": 
            mark_as_done()
        elif choice=="5": 
            print("Exiting the application...")  
            exit()
        else:
            print("Invalid input")

menu()               