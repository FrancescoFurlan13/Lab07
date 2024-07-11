from database.DB_connect import DBConnect
from model.situazione import Situazione


class MeteoDao():

    @staticmethod
    def getUmiditaMedia(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, AVG(s.Umidita) as media
                        FROM situazione s
                        WHERE MONTH(s.Data)=%s
                        GROUP BY s.Localita"""
            cursor.execute(query,(mese,))
            for row in cursor:
                result.append((row["Localita"],row["media"]))
            cursor.close()
            cnx.close()
        return result


