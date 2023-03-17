import sqlite3

class result:
    
    def insert_result(year,exam,id,e1,math,sci,ss,hi_evs,e2_alte,gk,ms,hrtg,comp):
        try:
            if (len(year) and len(exam) and len(id) and len(e1) and len(math) and len(math) and len(sci) and len(ss) and len(hi_evs) and len(e2_alte) and len(gk) and len(ms) and len(hrtg) and len(comp))==0:
                return "F"
            else:
                table_name=exam
                db_name=F"HCS_RESULT_{year}.db"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"CREATE TABLE IF NOT EXISTS {table_name} (ID TEXT NOT NULL UNIQUE,E1 TEXT NOT NULL,MATH TEXT NOT NULL,SCI TEXT NOT NULL,SS TEXT NOT NULL,HI_EVS TEXT NOT NULL,E2_ALTE TEXT NOT NULL,GK TEXT NOT NULL,MS TEXT NOT NULL,HRTG TEXT NOT NULL,COMP TEXT NOT NULL)")
                cursor.execute(F"INSERT INTO {table_name} (ID,E1,MATH,SCI,SS,HI_EVS,E2_ALTE,GK,MS,HRTG,COMP) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(id,e1,math,sci,ss,hi_evs,e2_alte,gk,ms,hrtg,comp))
                connection.commit()
                cursor.close()
                connection.close()
                return "T"
        except:
            return "F"

    
    def fetch_result(year,exam,id):
        try:
            if (len(year) and len(exam) and len(id))==0:
                return "F"
            else:
                table_name=exam
                db_name=F"HCS_RESULT_{year}.db"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"SELECT * FROM {table_name} WHERE ID=? ",(id,))
                data=cursor.fetchone()
                cursor.close()
                connection.close()
                return data
        except:
            return "F"




    def correction_result(year,exam,old_id,new_id,e1,math,sci,ss,hi_evs,e2_alte,gk,ms,hrtg,comp):
        try:
            if (len(year) and len(exam) and len(old_id) and len(new_id) and len(e1) and len(math) and len(math) and len(sci) and len(ss) and len(hi_evs) and len(e2_alte) and len(gk) and len(ms) and len(hrtg) and len(comp))==0:
                return "F"
            else:
                table_name=exam
                db_name=F"HCS_RESULT_{year}.db"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"UPDATE '{table_name}' SET ID='{new_id}',E1='{e1}',MATH='{math}',SCI='{sci}',SS='{ss}',HI_EVS='{hi_evs}',E2_ALTE='{e2_alte}',GK='{gk}',MS='{ms}',HRTG='{hrtg}',COMP='{comp}' WHERE ID='{old_id}'")
                connection.commit()
                cursor.close()
                connection.close()
                return "T"
        except:
            return "F"

    def delete_result_(year,exam,id):
        try:
            if (len(year) and len(exam) and len(id))==0:
                return "F"
            else:
                table_name=exam
                db_name=F"HCS_RESULT_{year}.db"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"DELETE FROM '{table_name}' WHERE ID='{id}'")
                connection.commit()
                cursor.close()
                connection.close()
                return "T"
        except:
            return "F"



