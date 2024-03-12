import sqlite3
from email_verification import authenticate_user

def mysql(user,pwd,role):
    class main():
        def display(self,user,pwd,role):
            connetion = sqlite3.Connection('mydatabase.db')
            cursor = connetion.cursor()
            check = cursor.execute(f'''
                                       SELECT USER_NAME,USER_PASSWORD,USER_ROLE FROM CREDENTIALS WHERE USER_NAME="{user}";
                                      ''').fetchall()
            if  check[0][0]==user :
                if  check[0][1]==pwd:
                    if  check[0][2]==role:
            
                     
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
             
    ob = main()   
    if ob.display(user,pwd,role) :
        return True
    else:
        return False
     
  
     
def register(user,pwd,id,email,role,age,gender):
    class re_data():       
        def register(self,user,pwd,id,email,role,age,gender):
            connetion = sqlite3.Connection('mydatabase.db')
            cursor = connetion.cursor()
            cursor.execute(''' 
                            CREATE TABLE IF NOT EXISTS CREDENTIALS(USER_NAME TEXT,USER_PASSWORD TEXT,USER_ID TEXT,USER_EMAIL TEXT,USER_ROLE TEXT,USER_AGE TEXT,USER_GENDER TEXT);
                            ''')
            check_U = cursor.execute(f'''
                                       SELECT USER_NAME FROM CREDENTIALS WHERE "{user}" IN (SELECT USER_NAME FROM CREDENTIALS);
                                      ''').fetchall()
            check_id=cursor.execute(f'''
                                       SELECT USER_NAME FROM CREDENTIALS WHERE "{id}" IN (SELECT ID FROM CREDENTIALS);
                                      ''').fetchall()
            check_e=cursor.execute(f'''
                                       SELECT USER_NAME FROM CREDENTIALS WHERE "{email}" IN (SELECT EMAIL FROM CREDENTIALS);
                                      ''').fetchall()
            if len(check_e)==0:
                if len(check_id)==0:
                    if len(check_U)==0 :
                        cursor.execute(f''' 
                                        INSERT INTO CREDENTIALS(USER_NAME,USER_PASSWORD,USER_ID,USER_EMAIL,USER_ROLE,USER_AGE,USER_GENDER) VALUES("{user}","{pwd}","{id}","{email}","{role}","{age}","{gender}");
                                    ''')
                        connetion.commit()
                        return True
                    else:
                        message='Name already Exist'       
                        return False
                else:
                    meessage="Id already Exist"
                    return False  
            else:
                message='Email already Exist'
                return False                    
    if age>="18":
        ob = re_data()
        if ob.register(user,pwd,id,email,role,age,gender):
            return True
        else:
            return False,message
    else:
        message='Invalid Age!'
        return False,message
def check(id):
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    cursor.execute(f'''
                   SELECT USER_NAME,AGE,VOTER_ID,STATUS,USER_GENDER FROM VOTERS WHERE VOTER_ID="{id}";
                   ''')
    rows = cursor.fetchall() 
    return tuple(rows)
def can_num():
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    cursor.execute(f'''
                        SELECT USER_NAME FROM CREDENTIALS WHERE USER_ROLE="Candidate";
                   ''')
    n=cursor.fetchall()
    return n
def candidates(user,id):
    connetion = sqlite3.connect('mydatabase.db')
    cursor = connetion.cursor()       
    cursor.execute(f'''
                   CREATE TABLE IF NOT EXISTS CANDIDATES(USER_NAME TEXT,USER_ID TEXT,COUNT INT);
                   ''' )
    check_c= cursor.execute(f'''
                            SELECT USER_NAME FROM CANDIDATES WHERE "{user}" IN (SELECT USER_NAME FROM CANDIDATES);
                            ''').fetchall()
    if len(check_c)==0:
        cursor.execute(f''' 
                        INSERT INTO CANDIDATES(USER_NAME,USER_ID,COUNT) VALUES("{user}","{id}",1);
                                 ''')
        connetion.commit() 
def voters(user,age,id,gender):
    connetion = sqlite3.connect('mydatabase.db')
    cursor = connetion.cursor()       
    cursor.execute(f'''
                   CREATE TABLE IF NOT EXISTS VOTERS(USER_NAME TEXT,AGE TEXT,VOTER_ID TEXT,STATUS TEXT,USER_GENDER TEXT);
                   ''' )
    check_c= cursor.execute(f'''
                            SELECT USER_NAME FROM VOTERS WHERE "{user}" IN (SELECT USER_NAME FROM VOTERS);
                            ''').fetchall()
    if len(check_c)==0:
        cursor.execute(f''' 
                        INSERT INTO VOTERS(USER_NAME,AGE,VOTER_ID,STATUS,USER_GENDER) VALUES("{user}","{age}","{id}","Yet To Vote","{gender}");
                                 ''')
        connetion.commit() 
def up_count(candidate):
    connetion = sqlite3.connect('mydatabase.db')
    cursor = connetion.cursor()       
    cursor.execute(f'''
                        UPDATE CANDIDATES SET COUNT=COUNT+1 WHERE USER_NAME="{candidate}";
                        ''')
    connetion.commit()  
def count():
    connetion = sqlite3.connect('mydatabase.db')
    cursor = connetion.cursor()
    return cursor.execute(f'''
                                SELECT USER_NAME,COUNT FROM CANDIDATES;
                          ''') 
def max():
    connetion = sqlite3.connect('mydatabase.db')
    cursor = connetion.cursor()
    return cursor.execute(f'''
                                SELECT USER_NAME FROM CANDIDATES WHERE COUNT IN(SELECT MAX(COUNT) FROM CANDIDATES );
                            ''')

def auther(username):
    connetion=sqlite3.connect('mydatabase.db')
    cursor = connetion.cursor()
    data = cursor.execute(f''' 
                            select USER_EMAIL from CREDENTIALS where "{username}" IN(SELECT USER_EMAIL FROM CREDENTIALS);
                            ''').fetchall()[0][0]
    if len(data)!=0:
            otp = authenticate_user(data)
            return True,otp
    else:
            return False,0
def u_p(email,pas):
    connetion=sqlite3.connect('mydatabase.db')
    cursor = connetion.cursor()
    cursor.execute(f'''
                                UPDATE CREDENTIALS SET USER_PASSWORD="{pas}" WHERE USER_EMAIL="{email}";
                                ''')
    connetion.commit()
def find(user):
    connetion=sqlite3.connect('mydatabase.db')
    cursor = connetion.cursor()
    a=cursor.execute(f'''
                        SELECT USER_NAME FROM CANDIDATES WHER USER_ID="{user}";
                        ''')
    if len(a)!=0:
        return True
    else:
        return False


            
          
