import sqlite3
from datetime import date
class fee:
    def submit(year,_class,id,submitter,_from,_to,amount):
        try:
            if (len(year) and len(_class) and len(id) and len(submitter) and len(_from) and len(_to) and len(amount))==0:
                return "F"
            else:
                fid=F"{date.today()}:{id}"
                db_name=F"HCS_FEE_DETAILS_{year}.db"
                table_name=F"CLASS_{_class}_FEE"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"CREATE TABLE IF NOT EXISTS {table_name}(FID TEXT NOT NULL UNIQUE,"
                "ID TEXT NOT NULL,SUBMITTER TEXT NOT NULL,FROM_MONTH TEXT NOT NULL,TO_MONTH TEXT NOT NULL,AMOUNT TEXT NOT NULL)")
                cursor.execute(F"INSERT INTO {table_name} (FID,ID,SUBMITTER,FROM_MONTH,TO_MONTH,AMOUNT) VALUES (?,?,?,?,?,?)",(fid,id,submitter,_from,_to,amount))
                connection.commit()
                cursor.close()
                connection.close()
                return(fid)
        except:
            return "F"
    

    def enquiry(year,_class,id):
        try:
            if (len(year) and len(_class) and len(id))==0:
                return "F"
            else:
                db_name=F"HCS_FEE_DETAILS_{year}.db"
                table_name=F"CLASS_{_class}_FEE"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"SELECT * FROM '{table_name}' WHERE ID=?",(id,))
                data=cursor.fetchall()
                cursor.close()
                connection.close()
                return data
        except:
            return "F"


    def search_by_fid(year,_class,fid):
        try:
            if (len(year) and len(_class) and len(fid))==0:
                return "F"
            else:
                db_name=F"HCS_FEE_DETAILS_{year}.db"
                table_name=F"CLASS_{_class}_FEE"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"SELECT * FROM '{table_name}' WHERE FID=?",(fid,))
                data=cursor.fetchone()
                cursor.close()
                connection.close()
                return data
        except:
            return "F"
        
    def correction(year,_class,new_id,submitter,_from,_to,amount,old_fid):
        try:
            if (len(year) and len(_class) and len(new_id) and len(submitter) and len(_from) and len(_to) and len(amount) and len(old_fid))==0:
                return "F"
            else:
                new_fid=F"{date.today()}:{new_id}"
                db_name=F"HCS_FEE_DETAILS_{year}.db"
                table_name=F"CLASS_{_class}_FEE"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"UPDATE '{table_name}' SET FID='{new_fid}',ID='{new_id}',SUBMITTER='{submitter}',FROM_MONTH='{_from}',TO_MONTH='{_to}',AMOUNT={amount} WHERE FID='{old_fid}'")
                connection.commit()
                cursor.close()
                connection.close()
                return(new_fid)
        except:
            return "F"


    def delete_record(year,_class,fid):
        try:
            if (len(year) and len(_class) and len(fid))==0:
                return "F"
            else:
                db_name=F"HCS_FEE_DETAILS_{year}.db"
                table_name=F"CLASS_{_class}_FEE"
                connection=sqlite3.connect(db_name)
                cursor=connection.cursor()
                cursor.execute(F"DELETE FROM '{table_name}' WHERE FID=?",(fid,))
                connection.commit()
                cursor.close()
                connection.close()
                return "T"
        except:
            return "F"

