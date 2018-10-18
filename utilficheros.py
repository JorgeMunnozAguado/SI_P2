import json
from pelicula import Pelicula

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
        if pelis_cont[iter2] == mayor:
            pelisFin.append(Pelicula(iter2.titulo,iter2.precio,iter2.poster,iter2.imgfondo,iter2.director,iter2.estreno,iter2.desc, iter2.link))
    return pelisFin
    
def searchFilms(buscar, pelis):

    films = []
    count = 0
    precio = 0

    for peli in pelis:
        for busco in buscar:
        
            if peli.titulo == busco["name"]:
            
                precio += int(peli.precio)
                count += 1
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