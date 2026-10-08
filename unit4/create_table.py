import mysql.connector
mycon=mysql.connector.connect(
   host='localhost',
   user='root', 
   password=''   
)
mycursor=mycon.cursor()
mycursor.execute("use Marwadi_python")
'''mycursor.execute("create table if not exists customer(name varchar(50),city varchar(50))")'''

'''mycursor.execute("insert into customer(name,city)values('Vashi','Rajkot')")'''
'''mycursor.execute("UPDATE customer SET city='MUMBAI' WHERE city='Rajkot'")'''
'''mycursor.execute("select * from customer")
sele=mycursor.fetchall()'''
    
sql='DROP TABLE customer'
mycursor.execute(sql)

print('its done bro')
mycon.close()
