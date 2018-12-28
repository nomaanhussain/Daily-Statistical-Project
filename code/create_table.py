import sqlite3
from datetime import datetime, date

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# create_table = "CREATE TABLE IF NOT EXISTS record (id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(create_table)


create_table = """CREATE TABLE IF NOT EXISTS records (Date date PRIMARY KEY, Inquiry_Call_In int, Inquiry_Walk_In int, Inquiry_Web int,
 Inquiry_Referral int, Inquiry_Other int, Total_Inquiries_Warm_Leads int, Appointments_Set int, Intro_1 int,
 Intro_1_Attended_Showed int, Intro_2 int, Intro_2_Attended_Showed int, Enrollment_Conferences int, 
 Renewal_Upgrade_Conferences int, no_of_Cancellations int, Dragon int, Basic int, Mastery int, Adults int, 
 Total int, no_of_Enrollments int, Student_Count_1st_Day int, Student_Count_2nd_Day int, no_of_Upgrades_Renewals int, 
 Tuition real, Compression real, Retail real, Special_Event real, Promotion_Fee real, Down_Payments_Daily real, Cancellation_Fees real, Other_Revenue real, Refunds real,
 Total_Gross_Revenue real, Net_Billing_Change real, Down_Payments real, Monthly_Payment_Total real, Down_Payments_Total real, 
 Monthly_Payment_Increase real, Cancellation_Fee_Collected real, Reduction_in_Monthly_Payment real)"""
cursor.execute(create_table)

# d = "25-06-2003"

# record = (d, 1, 1 , 1,1, 1 , 1,1, 1 , 1,1, 1 , 1,1, 1 , 1,1, 1 , 1,1, 1 , 1,1,1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1)

# insert_query = "INSERT INTO records VALUES (?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?)"

# cursor.execute(insert_query , record)

# d = "28-06-2003"
# record = (d, 1, 1 , 1,1, 1 , 1,1, 1 , 1,1, 1 , 1,1, 1 , 1,1, 1 , 1,1, 1 , 1,1,1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1)
# cursor.execute(insert_query , record)

# select_query = "SELECT * FROM records"

# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT * FROM records where Date>=? AND Date <=? "

# for row in cursor.execute(select_query,("25-06-2003","27-06-2003")):
#     print(row)

connection.commit()

connection.close()