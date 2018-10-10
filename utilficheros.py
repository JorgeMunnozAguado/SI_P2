import json
from pelicula import Pelicula
def jsonAPelicula(fichero):
	pelis=[]
	pelis_j=json.loads(open(fichero).read())
	for iter_pelis in pelis_j["peliculas"]:
		pelis.append(Pelicula(iter_pelis['titulo'],iter_pelis['precio'],iter_pelis['poster'],iter_pelis['imgfondo'],iter_pelis['director'],iter_pelis['estreno'],iter_pelis['desc']))
	
	return pelis