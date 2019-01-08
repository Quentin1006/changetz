#
# coding: utf-8


# Cette variable permet d'utiliser des threads
# Recommandé de mettre a false si l'ordi n'est pas puissant
use_threads = False

# Ne pas oublier de slash à la fin !!!!
# dataPath correspond au chemin vers le fichier a traiter
data_path = ""
# Pour connaitre les differents timezones possibles se référerau site ci-dessous
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
src_tz = "America/New_York"
dest_tz = "Europe/Paris"

# INDIQUER LE FORMAT DE DATE UTILISE PAR LA SOURCE DE DONNEE
# une plage correspond à une info entre 2 ';' dans un csv
# Si la date n'est renseignée que sur une plage, on ne remplit QUE date_fmt, time_fmt DOIT ETRE vide
# si la date est renseigné sur 2 plages
# Pour renseigner un format on utilise les sigles suivants
# %Y = annee à 4 chiffres
# %y = annee à 2 chiffres
# %m = mois à 2 chiffres 1-12
# %d = jour à 2 chiffres 1-31
# %H = heure à 2 chiffres 0-24
# %M = minutes à 2 chiffres 0-59
# %S = secondes à 2 chiffres 0-59
#
# Combiner les différents sigles avec les separateurs adéquats (ex:'/', '.', '-')
# pour former la date du fichier source
#
# Si un sigle est manquant se référer au bas de page du site:
# https://docs.python.org/2/library/datetime.html#datetime-objects

date_fmt = '%Y.%m.%d'
time_fmt = '%H:%M'
