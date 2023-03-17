import sqlite3

class student:

    def registration(year,_class,id,name,roll,dob,f_n,phone,id_mark):
        try:
            if (len(year) and len(_class) and len(id) and len(name) and len(roll) and len(dob) and len(f_n) and len(phone) and len(id_mark))==0:
                return "F"
            else:
                db_name=F"HCS_STUDENT_DETAILS_{year}.db"
                table_name=F"CLASS_{_class}_STUDENTS"
                roll=int(roll)
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"CREATE TABLE IF NOT EXISTS {table_name} (ID TEXT NOT NULL UNIQUE,NAME TEXT NOT NULL,ROLL TEXT NOT NULL,DOB DATE NOT NULL,FN TEXT NOT NULL,PHONE TEXT NOT NULL,IDM TEXT NOT NULL)")
                cursor.execute(F"INSERT INTO {table_name} (ID,NAME,ROLL,DOB,FN,PHONE,IDM) VALUES (?,?,?,?,?,?,?)",(id,name,roll,dob,f_n,phone,id_mark))
                connection.commit()
                cursor.close()
                connection.close()
                return "T"
        except:
            return "F"


    def data_fetch(year,_class,id):
        try:
            if (len(year) and len(_class) and len(id))==0:
                return "F"
            else:
                db_name=F"HCS_STUDENT_DETAILS_{year}.db"
                table_name=F"CLASS_{_class}_STUDENTS"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"SELECT * FROM {table_name} WHERE ID=?",(id,))
                data=cursor.fetchone()
                connection.commit()
                cursor.close()
                connection.close()
                return data
        except:
            return "F"

    def delete_data(year,_class,id):
        try:
            if (len(year) and len(_class) and len(id))==0:
                return "F"
            else:
                db_name=F"HCS_STUDENT_DETAILS_{year}.db"
                table_name=F"CLASS_{_class}_STUDENTS"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"DELETE FROM '{table_name}' WHERE ID='{id}'")
                connection.commit()
                cursor.close()
                connection.close()
                return "T"
        except:
            return "F"
    
    
    def update_datails(year,_class,old_id,new_id,name,roll,dob,f_n,phone,id_mark):
        try:
            if (len(year) and len(_class) and len(old_id) and len(new_id) and len(name) and len(roll) and len(dob) and len(f_n) and len(phone) and len(id_mark))==0:
                return "F"
            else:
                db_name=F"HCS_STUDENT_DETAILS_{year}.db"
                table_name=F"CLASS_{_class}_STUDENTS"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"UPDATE '{table_name}' SET ID='{new_id}',NAME='{name}',ROLL={roll},DOB='{dob}',FN='{f_n}',PHONE={phone},IDM='{id_mark}' WHERE ID='{old_id}'")
                connection.commit()
                cursor.close()
                connection.close()
            return "T"
        except:
            return "F"


#a=student.data_fetch("2020","10","20.10.10")
