
class Pelicula:
	def __init__(self,titulo,precio,poster,imgfondo,director,estreno,desc):
		self.titulo=titulo
		self.precio=precio
		self.poster=poster
		self.imgfondo=imgfondo
		self.director=director
		self.estreno=estreno
		self.desc=desc
		
	def __getitem__ (self, name):
		if name=='titulo':
			return titulo
		if name=='precio':
			return precio
		if name=='poster':
			return poster
		if name=='imgfondo':
			return imgfondo
		if name=='director':
			return director
		if name=='estreno':
			return estreno
		if name=='desc':
			return desc
