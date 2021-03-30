from dbhelper import DBHelper

def main():
    db=DBHelper()
    while True:
        print("**********WELCOME**********")
        print("PRESS 1 to insert user new user ")
        print("PRESS 2 to display all user ")
        print("PRESS 3 to delete user ")
        print("PRESS 4 to update user ")
        print("PRESS 5 to exit program ")


        try:
            choice=int(input())
            if(choice==1):
                uid=int(input("Enter user id: "))
                username=input("Enter user name: ")
                userphone=input(("Enter user phone: "))
                db.insert_user(uid, username, userphone)

            elif choice==2:
                db.Fetch_all()

            elif choice == 3:
                userid=int(input("Enter user id towhich you want to Delete"))
                db.delete_user(userid)

            elif choice == 4:
                uid = int(input("Enter id of user: "))
                username = input("Enter new user name: ")
                userphone = input(("Enter new user phone: "))
                db.update_user(uid, username, userphone)

            elif choice == 5:
                break
            else:
                print("Invalid input ! Try again")

        except Exception as e:
            print("Invalid Details !! Try again",e)

if __name__ == "__main__":
    main()

