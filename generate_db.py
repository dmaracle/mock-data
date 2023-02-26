from generate_data import generate_array
import sqlite3

database_name = 'data2'
conn = sqlite3.connect(f"{database_name}.db")
cursor = conn.cursor()
data_array = generate_array(10)
def create_tables():
    cursor.execute("""CREATE TABLE IF NOT EXISTS customer_info(
        Name text, 
        Address text,
        Phone text,
        City text,
        Email text,
        Client_Type text,
        Client_Acquisition text)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS customer_finances(
        Name text, 
        Annual_Occurence integer,
        Windows_Price integer,
        Pressure_Wash_Price integer,
        Handywork_Price integer,
        Expenses integer,
        Profit integer)""")

def insert_table_data():
    for x in range(len(data_array)):
        cursor.execute("""INSERT INTO customer_info(
            Name, Address, Phone, City, Email, Client_Type, Client_Acquisition) VALUES (?,?,?,?,?,?,?)""", 
            (data_array[x][0], data_array[x][1], data_array[x][2], data_array[x][3], data_array[x][4], data_array[x][5], data_array[x][6]))
        cursor.execute("""INSERT INTO customer_finances(
            Name, Annual_Occurence, Windows_Price, Pressure_Wash_Price, Handywork_Price, Expenses, Profit) VALUES (?,?,?,?,?,?,?)""", 
            (data_array[x][0], data_array[x][7], data_array[x][8], data_array[x][9], data_array[x][10], data_array[x][11], data_array[x][12], ))

conn.commit()
conn.close()