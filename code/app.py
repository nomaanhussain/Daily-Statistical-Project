from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

Fields = ["Date","Inquiry_Call_In","Inquiry_Walk_In","Inquiry_Web","Inquiry_Referral","Inquiry_Other","Total_Inquiries_Warm_Leads","Appointments_Set","Intro_1","Intro_1_Attended_Showed","Intro_2","Intro_2_Attended_Showed","Enrollment_Conferences","Renewal_Upgrade_Conferences","no_of_Cancellations","Dragon","Basic","Mastery","Adults","Total","no_of_Enrollments","Student_Count_1st_Day","Student_Count_2nd_Day","no_of_Upgrades_Renewals","Tuition","Compression","Retail","Special_Event","Promotion_Fee","Down_Payments_Daily","Cancellation_Fees","Other_Revenue","Refunds","Total_Gross_Revenue","Net_Billing_Change","Down_Payments","Monthly_Payment_Total","Down_Payments_Total","Monthly_Payment_Increase","Cancellation_Fee_Collected","Reduction_in_Monthly_Payment","no_upgrades_renewals_total","Down_payments_total_total","Monthly_Payments_Increase_total"]

# POST /store_data data
@app.route('/store_data', methods= ["POST"])
def insert_record():
    try:
        request_data = request.get_json()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        
        
        insert_query = "INSERT INTO records VALUES (?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?,?,?,?)"
        # data = (request_data["Date"],request_data["Inquiry_Call_In"],request_data["Inquiry_Walk_In"],request_data["Inquiry_Web"],request_data["Inquiry_Referral"],request_data['Inquiry_Other'],request_data["Total_Inquiries_Warm_Leads"],request_data["Appointments_Set"],request_data["Intro_1"],request_data["Intro_1_Attended_Showed"],request_data["Intro_2"],request_data["Intro_2_Attended_Showed"],request_data["Renewal_Upgrade_Conferences"],request_data["Enrollment_Conferences"],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[],request_data[])
        data =[]
        for k,y in request_data.items():
            data.append(y)
        record = tuple(data)

        cursor.execute(insert_query , record)

        connection.commit()
        connection.close()
        return jsonify({"msg": "Record Inserted"}), 201
    except:
        return jsonify({"msg": "Error in inserting record"}), 500



# GET /records_by_date
@app.route('/records_by_date/<string:start_date>/<string:end_date>')
def get_store(start_date,end_date):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    select_query = "SELECT * FROM records where Date>=? AND Date <=?"
    result =[]
    for row in cursor.execute(select_query,(start_date,end_date)):
        single_dict= {}

        for index, value in enumerate(row,0):
            single_dict[Fields[index]] = value
        result.append(single_dict)

    
    total= []
    for field in Fields[1:]:
        single_dict= {}
        select_query = "SELECT SUM({}) FROM records where Date>=? AND Date <=?".format(field)
        for row in cursor.execute(select_query,(start_date,end_date)):
            single_dict[field] = row
        total.append(single_dict)
    return jsonify({'records':result,'total':total}), 200





app.run(port=5000)