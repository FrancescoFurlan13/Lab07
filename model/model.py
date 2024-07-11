from database import meteo_dao


class Model:

    def getUmiditaMedia(self, mese):
        media = meteo_dao.MeteoDao.getUmiditaMedia(mese)
        return media

