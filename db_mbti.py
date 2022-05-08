import sqlite3

class MBTI():
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

    def consultar(self,y,t):
        return self.cur.execute("""SELECT   R.ID_MEANING,
                                            M.NAME
                                    FROM    RELATION R,
                                            MEANING M
                                    WHERE   R.ID_MEANING = M.ID
                                    AND     R.YOU = ?
                                    AND     R.THEIR = ?;""", (y.get(),t.get())).fetchall()
        
    

