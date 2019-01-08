# coding: utf-8

# /Users/kant1_sahal/Desktop/QuentinCocoon/donnees/HistData/EURUSD/DAT_MT_EURUSD_M1_2015.csv


# /Users/kant1_sahal/Downloads/HISTDATA_COM_NT_EURUSD_M1201709/DAT_NT_EURUSD_M1_201709.csv

# /Users/kant1_sahal/Downloads/HISTDATA_COM_NT_EURUSD_M12015(1)/DAT_NT_EURUSD_M1_2015.csv
import re
from datetime import datetime, timedelta
from pytz import timezone
from dateutil import parser


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False


class DateConvertible(object):
	""" docstring for DateConvertible """

	def __init__(self, date, date_fmt, tz=''):
		super(DateConvertible, self).__init__()
		self.date = self.setDate(date, date_fmt)
		if not tz == '':
			self.setTimeZone(tz)

	def setDate(self, d, d_fmt):
		return datetime.strptime(d, d_fmt)


	def setTimeZone(self, tz='UTC'):
		#print "setTimeZone : avant ", self.date
		tz = timezone(tz)
		self.date = tz.localize(self.date)

		#print "setTimeZone: apres ", self.date
		#print "---------"
		return self.date

	def changeTimeZone(self, to):
		#print "changeTimeZone : avant ", self.date
		tz = timezone(to)
		#print "changeTimeZone ", tz
		self.date = self.date.astimezone(tz)
		#print "changeTimeZone : apres ", self.date

	def isSameDayAs(self, dateConv):
		if not isinstance(dateConv, DateConvertible):
			raise("l'arg 1 n'est pas de type DateConvertible")

		d1 = datetime.strftime(self.date, "%Y-%m-%d")
		d2 = datetime.strftime(dateConv.date, "%Y-%m-%d")

		return d1 == d2

	def timeInMin(self):
		return self.date.minute + self.date.hour * 60

	def toString(self, format="%d.%m.%Y"):
		""" retourne simplement la date sous forme de string, pour retourner l'heure également, appeler toFullString() """

		return self.date.strftime(format)
		

	def toFullString(self, format="%d.%m.%Y %H:%M"):
		return self.date.strftime(format)



	@staticmethod
	def printing():
		print 'class DateConvertible'



















	

