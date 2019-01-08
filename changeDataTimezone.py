# coding: utf-8

"""
Objectif du script:
Prendre un fichier de données boursieres de la forme DATE, HEURE (opt), OPEN, HIGH, LOW, CLOSE, VOL (opt)
et de transformer toutes les dates de chaque ligne d'un fuseau horaire vers un autre

Utilisation du script:
Bien lire les commentaires du fichier de config et ajuster le tz des données sources, le tz dans lequel on veut
les données, il faut aussi bien adapter le format de la date et de l'heure, si le format des données regroupe la
date et l'heure dans le meme string, entrer le format de la date et heure uniqument dans le champ date
"""


import config as conf
import os
import re
import time
from DateConvertible import DateConvertible


def changeDataTimezone(fname, from_tz, to_tz, date_fmt, time_fmt):

	"""
	lit un fichier de données boursiere, la 1ere etape est de regarder si la date est en 1 ou 2 partie
	autrement dit si le champ heure est rempli. On recupere ensuite la date et heure complete de la ligne
	on lui change le tz et on recolle les morceaux, on ecrit ensuite la ligne dans le nouveau fichier
	"""

	f_out = fname[:-4] + "_" + to_tz.replace("/", "-") + ".csv"

	with open(fname, 'r') as fd:
		with open(f_out, 'w') as fd_out:
			data_src = re.split('\r\n|\n', fd.read())

			# on regarde en combien de partie est divisée la date dans les données
			if time_fmt is not '':
				dateparts = 2
			else:
				dateparts = 1

			for data_min in data_src:
				try:
					datalist = re.split('[,;]', data_min)
					date_str = ' '.join(datalist[:dateparts])

					if dateparts == 2:
						fmt = date_fmt + ' ' + time_fmt
					else:
						fmt = date_fmt

					date_c = DateConvertible(date_str, fmt, from_tz)
					date_c.changeTimeZone(to_tz)

					new_tz_date = date_c.toFullString(format='%Y/%m/%d;%H:%M')
					data_transformed = new_tz_date + ';' + ';'.join(datalist[dateparts:])

					fd_out.write(data_transformed + "\n")
				except Exception as e:
					print 'error: ', e

	print "Les données se trouvent dans le fichier ", f_out


if __name__ == '__main__':

	fn = raw_input("Entrer le nom du fichier a traiter:\n>> ")
	fn = os.path.join(conf.data_path, fn)

	time_start = time.time()
	changeDataTimezone(fn, conf.src_tz, conf.dest_tz, conf.date_fmt, conf.time_fmt)
	time_end = time.time()
	print "temps de calcul pour le transfo des données: ", time_end - time_start









