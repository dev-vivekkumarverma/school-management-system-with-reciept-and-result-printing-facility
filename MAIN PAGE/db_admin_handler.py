import sqlite3

class adm:
    def admin_signup(adm_id,name,adhar,pin):
        try:
            connection=sqlite3.connect("HCS_ADMIN.db")
            cursor=connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS ADMIN (ID  TEXT NOT NULL UNIQUE, NAME TEXT NOT NULL, ADHAR TEXT NOT NULL UNIQUE, PIN TEXT NOT NULL)")
            cursor.execute("INSERT INTO ADMIN (ID,NAME,ADHAR,PIN) VALUES (?,?,?,?)",(adm_id,name,adhar,pin))
            connection.commit()
            cursor.close()
            connection.close()
            return("T")
        except:
            return("F")

    def admin_verification(adm_id,pin):
        try:
            connection=sqlite3.connect("HCS_ADMIN.db")
            cursor=connection.cursor()
            cursor.execute("SELECT PIN FROM ADMIN WHERE ID=?",(adm_id,))
            fpin=cursor.fetchone()
            if(pin==fpin[0]):
                connection.commit()
                cursor.close()
                connection.close()
                return("T")                
        except:
            return("F")

