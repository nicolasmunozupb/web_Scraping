import urllib
import requests
import csv
from bs4 import BeautifulSoup


def productos():
    print("empieza productos")
    contador = 0
    for i in auc:
        contador = contador + 1
        print("Agregado el producto: " + str(contador))
        url = i
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        comentarios = soup.find_all("div", {"class": "review-tooltip-full-body"})
        eq = soup.find_all("div", {"class": "review-tooltip-full-body"})
        titulo = soup.find("h1", {"class": "item-title__primary"}).text.replace('\n',' ').replace('\r',' ').replace('\t',' ').replace("b'",' ').strip()
        precio = soup.find("span", {"class": "price-tag-fraction"}).text.replace('.','')
        estrellas = soup.find_all('input', {'id': 'reviewFullStar0'})
        buscarId = soup.find(attrs={"name" : "itemId"})
        resultadoId = buscarId["value"]
        array = []
        array2 = []
        for i in estrellas:
            array2.append(i["value"])
        if(len(array2)!=0):
            array2.pop(0)
        for i in comentarios:
            array.append(i.text)
        for i in range(0, len(array)):
            writer.writerow([resultadoId,titulo, precio, array[i], array2[i]])


def obtenerProductos():
    for i in range(0, len(listaPaginas)):
        dir = listaPaginas[i]
        page = urllib.request.urlopen(dir)
        soup = BeautifulSoup(page, 'html.parser')
        eq = soup.find_all("li", {"class": "ui-search-layout__item"})
        for i in eq:
            auc.append(i.a["href"])
    print("hay: " +str(len(auc))+ " productos")

            
def obtenerPaginas(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    pagina = soup.find_all("li", {"class": "andes-pagination__button"})
    pagina.pop()
    j=1
    for i in pagina:
        listaPaginas.append((i.a["href"]))

#Crear Archivo
file = open('ProductosModaHombre.csv', 'w')
writer = csv.writer(file)
writer.writerow(["id","producto", "precio", "comentario", "estrellas"]) 

#Variables
listaPaginas = []
auc = []
urlhombres = "https://listado.mercadolibre.com.co/hombre"

#Ejecucion Metodos
print("hombres")
obtenerPaginas(urlhombres)
obtenerProductos()
productos()
file.close()

