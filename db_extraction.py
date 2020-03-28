import mysql.connector

def get_person(bg):

    mydb = mysql.connector.connect(user='samkiller007', password='Incorrect@11',host='localhost',database='docker')

    mycursor = mydb.cursor()

    query="SELECT * FROM bloodgroup where blood_group like \""+bg+"\""
    data=[]
    mycursor.execute(query)
    for i in mycursor:
        print(i)
        data.append(i)
    
    return data