import tkinter as tk
import sqlite3

root = tk.Tk()

#table
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''

def delete():
        #create (you would connect a database here as well)
        conn = sqlite3.connect('test_database.db')
        #cursor
        c = conn.cursor()

        c.execute("DELETE from addresses WHERE oid= " + deleteBox.get())
        deleteBox.delete(0, 100)

        #commit
        conn.commit()
        #close
        conn.close()

def submit():
        #create (you would connect a database here as well)
        conn = sqlite3.connect('test_database.db')
        #cursor
        c = conn.cursor()

        #insert into table
        c.execute("INSERT INTO addresses VALUES (:firstName, :lastName, :address, :city, :state, :zipcode)",
                {
                        'firstName': firstName.get(),
                        'lastName': lastName.get(),
                        'address': address.get(),
                        'city': city.get(),
                        'state': state.get(),
                        'zipcode': zipcode.get()
                })

        #commit
        conn.commit()
        #close
        conn.close()

        firstName.delete(0, 100)
        lastName.delete(0, 100)
        address.delete(0, 100)
        city.delete(0, 100)
        state.delete(0, 100)
        zipcode.delete(0, 100)

def query():
        #create (you would connect a database here as well)
        conn = sqlite3.connect('test_database.db')
        #cursor
        c = conn.cursor()

        #query
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        print(records)

        printRecords = ''
        for record in records:
                printRecords += str(record) + "\n"

        queryLabel = tk.Label(root, text=printRecords)
        queryLabel.grid(row=8, column=0, columnspan=2)

        #commit
        conn.commit()
        #close
        conn.close()

#text boxes
firstName = tk.Entry(root, width=30)
firstName.grid(row=0, column=1, padx=20)
lastName = tk.Entry(root, width=30)
lastName.grid(row=1, column=1)
address = tk.Entry(root, width=30)
address.grid(row=2, column=1)
city = tk.Entry(root, width=30)
city.grid(row=3, column=1)
state = tk.Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5, column=1)

deleteBox = tk.Entry(root, width=30)
deleteBox.grid(row=9, column=1)

#labels
firstNameLabel = tk.Label(root, text="First Name")
firstNameLabel.grid(row=0, column=0)
lastNameLabel = tk.Label(root, text="Last Name")
lastNameLabel.grid(row=1, column=0)
addressLabel = tk.Label(root, text="Address")
addressLabel.grid(row=2, column=0)
cityLabel = tk.Label(root, text="City")
cityLabel.grid(row=3, column=0)
stateLabel = tk.Label(root, text="State")
stateLabel.grid(row=4, column=0)
zipcodeLabel = tk.Label(root, text="Zipcode")
zipcodeLabel.grid(row=5, column=0)

deleteBoxLabel = tk.Label(root, text="ID # To Delete")
deleteBoxLabel.grid(row=9, column=0)

#submit
submitButton = tk.Button(root, text="Add Record to Database", command=submit)
submitButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

#query
queryButton = tk.Button(root, text="Show Records", command=query)
queryButton.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#delete
deleteButton = tk.Button(root, text="Delete Record", command=delete)
deleteButton.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

root.mainloop()