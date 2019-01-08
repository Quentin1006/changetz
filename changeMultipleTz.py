# coding: utf-8


"""
Bien lire le fichier de config avant de lancer le script, pour comprendre comment fonctionne changeDataTime,
se référer au fichier homonyme.
"""

import config as conf
from changeDataTimezone import changeDataTimezone
from threading import Thread


list_files = [
	'/Users/kant1_sahal/Desktop/QuentinCocoon/donnees/HistData/EURGBP/EURGBP_2002_2016.csv',
	'/Users/kant1_sahal/Desktop/QuentinCocoon/donnees/HistData/EURJPY/EURJPY_2005_2016.csv',
	'/Users/kant1_sahal/Desktop/QuentinCocoon/donnees/HistData/NZDUSD/NZDUSD_2005_2016.csv',
	'/Users/kant1_sahal/Desktop/QuentinCocoon/donnees/HistData/USDCAD/USDCAD_2000_2016.csv'
]


def changeDataTimezoneWrapper(fct):

	def wrapper(*args, **kwargs):
		print 'hello world'
		fct(*args, **kwargs)
		print 'goodbye world'

	return wrapper

changeDataTimezone = changeDataTimezoneWrapper(changeDataTimezone)


if __name__ == '__main__':
	for file_ in list_files:
		arguments = (file_, conf.src_tz, conf.dest_tz, conf.date_fmt, conf.time_fmt)
		if conf.use_threads:
			Thread(target=changeDataTimezone, args=arguments).start()
		else:
			changeDataTimezone(*arguments)
