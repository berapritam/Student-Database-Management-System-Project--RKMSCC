# importing MySQL-Connector library.
import mysql.connector

# import my Establishing the Connection to the
# database.

conn = mysql.connector.Connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "hackers"
)

# creating a cursor object
cursor = conn.cursor()
def home():
    print("************************************")
    print(" STUDENT DATABASE MANAGEMENT SYSTEM ")
    print("************************************")
    print("1. Add Record")
    print("2. View Record")
    print("3. View All Record")
    print("4. Edit Record")
    print("5. Delete Record")
    print("6. Exit")
    try:
        ch = int(input("Enter your choice:"))
    except ValueError:
        print ("It is not a number")
        exit()
    if (ch == 1):
        add ()
    elif (ch == 2):
        view ()
    elif (ch == 3):
        viewAll ()
    elif (ch == 4):
        edit ()
    elif (ch == 5):
        delete ()
    elif (ch == 6):
        conn.close()
        quit ()
    else:
        print ("\nInvalid choice!!\n Enter number between 1 to 6\n")
    home()
    
def add():
    print("\n\t\t* ADD STUDENT RECORD *")
    print("\t\t-------------------")
    data = []
    id = input("Enter ID:")
    data.append(id)
    sname = input("Enter name:")
    data.append(sname.upper())
    address = input("Enter your Address:")
    data.append(address.upper())
    mobile = input("Enter mobile number:")
    data.append(mobile)
    email = input("Enter email:")
    data.append(email.lower())
    adate = input("Enter Admission date:")
    data.append(adate)
    course = input("Enter course:")
    data.append(course.upper())
    insert_sql_stmt = "INSERT INTO cyber_squad VALUES (%s, %s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(insert_sql_stmt, data)
        conn.commit()
        print(cursor.rowcount, "record added")
    except mysql.connector.Error as e:
        print(f"Error adding record: {e}")
    home()


def view():
    print("\t\t\t\t DETAILS OF SPECIFIC STUDENT")
    print("\t\t\t\t----------------------------")
    id = input("Enter ID: ")
    
    # Retrieving specific records using the WHERE clause.
    # Using parameterized query to prevent SQL injection.
    view_sql_stmt = "SELECT * FROM cyber_squad WHERE id = %s"
    
    try:
        cursor.execute(view_sql_stmt, (id,))
        result = cursor.fetchall()
        
        if not result:
            print("No record found for the given ID.\n")
        else:
            for field in result:
                print("ID :", field[0])
                print("Name :", field[1])
                print("Address :", field[2])
                print("Mobile No. :", field[3])
                print("Email :", field[4])
                print("Admit date:", field[5])
                print("Course :", field[6], "\n")
    except mysql.connector.Error as e:
        print(f"Error retrieving record: {e}\n")
    
    home()

    
def viewAll():
    print("\t\t\t\t DETAILS OF ALL STUDENT")
    print("\t\t\t\t-----------------------")
    viewAll_sql_stmt = "SELECT * FROM cyber_squad"
    
    try:
        cursor.execute(viewAll_sql_stmt)
        result = cursor.fetchall()
        
        if not result:
            print("No records found in the database.\n")
        else:
            for field in result:
                print("ID:", field[0])
                print("Name:", field[1])
                print("Address:", field[2])
                print("Mobile No.:", field[3])
                print("Email:", field[4])
                print("Admit date:", field[5])
                print("Course:", field[6], "\n")
    except mysql.connector.Error as e:
        print(f"Error retrieving records: {e}\n")
    
    home()


def edit():
    print("\t\t\t\t EDIT SPECIFIC STUDENT RECORD")
    print("\t\t\t\t-----------------------------")
    id = input("Enter id: ")  # Added colon for clarity
    edit_sql_stmt = "SELECT * FROM cyber_squad WHERE id = %s"
    
    try:
        cursor.execute(edit_sql_stmt, (id,))
        result = cursor.fetchall()
        
        if not result:
            print("No record found for the given ID.\n")
        else:
            for field in result:
                print("ID:", field[0])
                print("Name:", field[1])
                print("Address:", field[2])
                print("Mobile No.:", field[3])
                print("Email:", field[4])
                print("Admit Date:", field[5])
                print("Course:", field[6], "\n")
                
                print("\t\t\t\t Enter new Data")
                data = []
                
                sname = input("Enter new name:")
                data.append(sname.upper())
                address = input("Enter new address:")
                data.append(address.upper())
                mobile = input("Enter new mobile number:")
                data.append(mobile)
                email = input("Enter new email id:")
                data.append(email.lower())
                aDate = input("Enter new admission date:")
                data.append(aDate)
                course = input("Enter new course:")
                data.append(course.upper())
                data.append(id)  # ID for WHERE clause
                
                update_sql_stmt = "UPDATE cyber_squad SET sname=%s, address=%s, mobile=%s, email=%s, adate=%s, course=%s WHERE id=%s"
                cursor.execute(update_sql_stmt, data)
                conn.commit()
                print(cursor.rowcount, "record modified")
    except mysql.connector.Error as e:
        print(f"Error editing record: {e}\n")
    
    home()


def delete():
    print("\t\t\t* DELETE SPECIFIC STUDENT RECORD *")
    print("\t\t\t----------------------")
    id = input("Enter ID:")
    edit_sql_stmt = "SELECT * FROM cyber_squad WHERE id = %s"
    
    try:
        cursor.execute(edit_sql_stmt, (id,))
        result = cursor.fetchall()
        
        if not result:
            print("No record found for the given ID.\n")
        else:
            for field in result:
                print("ID :", field[0])
                print("Name :", field[1])
                print("Address :", field[2])
                print("Mobile No.:", field[3])  # Fixed typo: removed "Address :" and corrected to "Mobile No.:"
                print("Email:", field[4])
                print("Admit date :", field[5])
                print("Course :", field[6], "\n")
            
            ans = input("Do you want to delete this record (y/n)?")
            if ans.lower() == 'y':
                delete_sql_stmt = "DELETE FROM cyber_squad WHERE id = %s"
                cursor.execute(delete_sql_stmt, (id,))
                conn.commit()
                print(cursor.rowcount, "record deleted\n")
            else:
                print("Deletion cancelled.\n")
    except mysql.connector.Error as e:
        print(f"Error deleting record: {e}\n")
    
    home()
home()


