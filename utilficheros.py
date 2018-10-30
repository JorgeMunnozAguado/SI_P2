import json
import os
import sys

from pelicula import Pelicula

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

def jsonAPelicula(fichero):

	pelis=[]
	pelis_j=json.loads(open(fichero).read())
	for iter_pelis in pelis_j["peliculas"]:
		pelis.append(Pelicula(iter_pelis['titulo'],iter_pelis['precio'],iter_pelis['poster'],iter_pelis['imgfondo'],iter_pelis['director'],iter_pelis['estreno'],iter_pelis['desc'],iter_pelis['link']))
	
	return pelis
    
    
def resultadoPeliculas(search,tipo,pelis):

    pelis_cont={}
    pelisFin=[]
    mayor=0
    list_search=search.lower().split(" ")
    if tipo == "titulo":
        for iter_pelis in pelis:
            aux=iter_pelis.titulo.lower().split(" ")
            cont=0
            for elem in aux:
                for elemS in list_search:
                    if elem == elemS:
                        cont=cont+1
                        break
            pelis_cont[iter_pelis]=cont
            if cont > mayor:
                mayor=cont
    elif tipo == "director":
        for iter_pelis in pelis:
            aux=iter_pelis.director.lower().split(" ")
            cont=0
            for elem in aux:
                for elemS in list_search:
                    if elem == elemS:
                        cont=cont+1
                        break
            pelis_cont[iter_pelis]=cont
            if cont > mayor:
                mayor=cont
    for iter2 in pelis:
        if mayor == 0:
            pelisFin=[]
        else:
            if pelis_cont[iter2] == mayor:
                pelisFin.append(Pelicula(iter2.titulo,iter2.precio,iter2.poster,iter2.imgfondo,iter2.director,iter2.estreno,iter2.desc, iter2.link))
    return pelisFin
    
def searchFilms(buscar):

    films = []
    count = 0
    precio = 0

    json_url = os.path.join(SITE_ROOT, "data", "catalogo.json")
    pelis = jsonAPelicula(json_url)

    for peli in pelis:
        for busco in buscar:
        
            if peli.titulo == busco["name"]:
            
                count += 1
                
                if "number" in busco:
                    precio += int(peli.precio) * int(busco['number'])
                    films.append({"titulo":peli.titulo, "precio":int(peli.precio) * int(busco['number']), "poster":peli.poster, "fondo":peli.imgfondo, "director":peli.director, "estreno":peli.estreno, "desc":peli.desc, "link":peli.link, "number":busco['number']})
                else:
                    precio += int(peli.precio)
                    films.append(Pelicula(peli.titulo, peli.precio, peli.poster, peli.imgfondo, peli.director, peli.estreno, peli.desc, peli.link))
                
                if count == len(buscar): return [films, precio]

    return [films, precio]

def crearDatosUsuario(user_url,dict_res):
	if os.path.exists(user_url) == False:
		os.mkdir(user_url,0777)
		with open('datos.json', 'w') as fp:
			json.dump(dict_res, fp)
		return True
	else:
		return False

def peliculaEnCarrito(buscar):

    films = {}
    count = 0
    precio = 0

    json_url = os.path.join(SITE_ROOT, "data", "catalogo.json")
    pelis = jsonAPelicula(json_url)

    for peli in pelis:
        for busco in buscar:
            if peli.titulo == busco["name"]:
                pelicula=Pelicula(peli.titulo,peli.precio,peli.poster,peli.imgfondo,peli.director,peli.estreno,peli.desc,peli.link)
                films[pelicula]="True"
    '''for peli in pelis:
        if peli not in films.keys():
            films[peli]="False"'''

    for peli in pelis:
        esta=0
        for key,value in films.items():
            if key.titulo == peli.titulo:
                esta=1
        if esta == 0:
            films[peli]="False"

    return films