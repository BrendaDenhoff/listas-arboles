import re

class NodoLista:
  def __init__(self, dato = None):
    #Se crea el constructor del nodoLista..
    self.dato = dato
    self.siguiente = None

  def tieneSiguiente(self):
    return self.siguiente!=None

  def append(self, nodoNuevo):
    #Agrega un nuevo nodo en la lista.
    if self.tieneSiguiente(): 
      #Si ya tiene un dato, entonces se fija en el siguiente hasta encontrar donde ubicar el nodo.
      self.siguiente.append(nodoNuevo)
    else:
      self.siguiente = nodoNuevo
    
  def len(self):
    #Retorna la cantidad de elemento de la lista.
    cant = 1
    if self.tieneSiguiente():
      cant += self.siguiente.len()
    return cant
  
  def get(self, getPos, actPos = 0):
    #Dada una posicion retorna el dato que se encuentra ahi.
    dato = None
    if actPos == getPos:
      dato = self.dato
    else:
      dato = self.siguiente.get(getPos, actPos+1)
    return dato
  
  def tieneDato(self, dato):
    #Busca en toda la lista el dato pasado por parametro y retorna si esta o no.
    if self.dato == dato:
      return self.dato == dato
    elif self.tieneSiguiente():
      return self.siguiente.tieneDato(dato)
    if self.dato != dato:
      return False

  def deleteAll(self, dato):
    #Busca el dato pasado por parametro y lo elimina.
    if self.tieneSiguiente():
      if self.siguiente.dato == dato:
        self.siguiente = self.siguiente.siguiente
      else:
        self.siguiente.deleteAll(dato) 


class Lista:
  def __init__(self):
    self.primero = None

  def estaVacio(self):
    #Retorna si esta vacia o no.
    return self.primero == None

  def __repr__(self):
    out = ""
    aux = self.primero
    while aux != None:
      out += " -> " + str(aux.dato)
      aux = aux.siguiente
    out += " -|"
    return out

  def append(self, dato):
    #Recursiva del nodoLista
    nodoNuevo = NodoLista(dato)
    if self.estaVacio():
      self.primero = nodoNuevo
    else:
      self.primero.append(nodoNuevo)
    
  def len(self):
    #Recursiva del nodoLista
    cant = 0
    if not self.estaVacio():
      cant = self.primero.len()
    return cant
  

  def get(self, pos):
    #Recursiva del nodoLista
    if 0 <= pos < self.len() and not self.estaVacio():
      return self.primero.get(pos)
    else:
      raise Exception("Posicion invalida")
    
  def tieneDato(self, dato):
    #Recursiva del nodoLista
    if not self.estaVacio():
      return self.primero.tieneDato(dato)

  def insertarLista(self, lista, pos=0):
    #Agrega una lista dada por parametro a la lista. 
    while pos < lista.len():
      #Repite mientras la posicion sea menor a la cantidad de elementos 
      #de la lisla del parametro. 
      datoAPoner = lista.get(pos)
      #Cada vez que repita el proceso el datoAPoner va a cambiar segun la posicion.
      if not self.tieneDato(datoAPoner):
        #Si en la lista que estamos trabajando el dato no esta entonces lo agrega
        #y tambien le suma 1 a la posicion para volver a repetir el proceso.
        self.append(datoAPoner)
        pos += 1
      elif self.tieneDato(datoAPoner):
        #En caso de ya tener el dato entonces solo le suma 1 a la posicion.
        pos += 1

  def datosCompartidos(self, lista, pos=0):
    datosEnComun = Lista()
    #Se crea una lista nueva.
    while pos < lista.len():
      #Repite el procedimiento hasta que la posicion lo permite.
      dato = lista.get(pos)
      if self.tieneDato(dato):
        #Agrega a la lista el dato en comun que tiene la lista que estamos 
        #trabajando con la ingresada por parametro
        datosEnComun.append(dato)
        pos+=1
      elif not self.tieneDato(dato):
        pos+=1
    return datosEnComun
  
  def deleteAll(self, cancion):
    #Recursiva del nodoLista
    if not self.estaVacio():
      if self.primero.dato == cancion:
        self.primero = self.primero.siguiente
      else:
        self.primero.deleteAll(cancion)

  
##NODO ARBOL
class NodoArbolDeCanciones:
  def __init__(self, interprete, canciones = None):
    self.interprete = interprete
    self.canciones = Lista()
    self.izquierdo = None
    self.derecho = None

  
  def tieneDerecho(self):
    return self.derecho != None
  def tieneIzquierdo(self):
    return self.izquierdo != None
  def estaVacio(self):
    return self.interprete == None
  def esHoja(self):
    return not self.tieneDerecho() and not self.tieneIzquierdo()

  def insertarInterprete(self, nuevoNodo):
    #Inserta al arbol un interprete nuevo.
    if self.interprete == nuevoNodo.interprete:
      #En caso de que el interprete ya este en el arbol nos indica por pantalla
      #que esta en el arbol.
      print("El interprete ya esta en el arbol")
    #En caso de ya haber un interprete en el arbol busca en que posicion ubicarlo
    #si es mayor lo ubica por la derecha y si es menor lo ubica por la izquierda.
    elif nuevoNodo.interprete < self.interprete:
      if self.tieneIzquierdo():
        self.izquierdo.insertarInterprete(nuevoNodo)
      else:
        self.izquierdo = nuevoNodo
    else:
      if self.tieneDerecho():
        self.derecho.insertarInterprete(nuevoNodo)
      else:
        self.derecho = nuevoNodo

  def estaInterprete(self, interprete):
    #Busca el interprete y retorna el inteprete.
    nodoDato = None
    if self.interprete == interprete:
      nodoDato = self
    else:
      if interprete < self.interprete:
        if self.tieneIzquierdo():
          nodoDato = self.izquierdo.estaInterprete(interprete)
      else:
        if self.tieneDerecho():
          nodoDato = self.derecho.estaInterprete(interprete)
    return nodoDato 

  def buscarInterprete(self, interprete):
    nodoDato = None
    if self.interprete == interprete:
      nodoDato = self
    else:
      if interprete < self.interprete:
        if self.tieneIzquierdo():
          nodoDato = self.izquierdo.buscarInterprete(interprete)
      else:
        if self.tieneDerecho():
          nodoDato = self.derecho.buscarInterprete(interprete)
    return nodoDato

  def cancionesDelInterprete(self):
    #Retorna las canciones del interprete.
    return self.canciones

  def interpretesDeCancion(self, nombreCancion, listaInterpretes = Lista()): 
    #Se busca si esta la cancion ingresada por parametro y si esta se agrega 
    #al interprete a una lista
    if self.canciones.tieneDato(nombreCancion):
      listaInterpretes.append(self.interprete)
    if self.tieneIzquierdo():
      self.izquierdo.interpretesDeCancion(nombreCancion)
    if self.tieneDerecho():
      self.derecho.interpretesDeCancion(nombreCancion)
    return listaInterpretes

  def buscaMaximo(self):
    dato = None
    if self.tieneDerecho():
      dato = self.derecho.buscaMaximo()
    else:
      dato = self
    return dato

  def sucesor(self):
    sucesor = None
    if self.tieneDerecho():
      sucesor = self.derecho.buscaMinimo()
    return sucesor

  def predecesor(self):
    predecesor = None
    if self.tieneIzquierdo():
      predecesor = self.izquierdo.buscaMaximo()
    return predecesor

  def grado(self):
    grado = 0
    if self.tieneIzquierdo():
      grado += 1
    if self.tieneDerecho():
      grado += 1
    return grado

  def altura(self):
    altura = 0
    if self.grado() == 2:
      altura = 1 + max(self.izquierdo.altura() , self.derecho.altura())
    elif self.tieneIzquierdo():
      altura = 1 + self.izquierdo.altura()
    elif self.tieneDerecho():
      altura = 1 + self.derecho.altura()
    return altura

  def buscaPadre(self, interprete):
    nodoHijo = None
    nodoPadre = None
    lado = None
    if interprete < self.interprete:
      if self.tieneIzquierdo():
        if self.izquierdo.interprete == interprete:
          nodoHijo = self.izquierdo
          nodoPadre = self
          lado = "izq"
        else:
          nodoHijo, nodoPadre, lado = self.izquierdo.buscaPadre(interprete)
    else:
      if self.tieneDerecho():
        if self.derecho.interprete == interprete:
          nodoHijo = self.derecho
          nodoPadre = self
          lado = "der"
        else:
          nodoHijo, nodoPadre, lado = self.derecho.buscaPadre(interprete)
    return nodoHijo, nodoPadre, lado

  def eliminarInterprete(self, nombreInterprete):
    nodoEliminar, nodoPadre, lado = self.buscaPadre(nombreInterprete)  ##lado = "izq" / "der"
    if nodoEliminar != None:
      if nodoEliminar.grado() == 2:
        nodoPred = nodoEliminar.predecesor()
        self.eliminarInterprete(nodoPred.interprete)
        nodoPred.izquierdo = nodoEliminar.izquierdo
        nodoPred.derecho = nodoEliminar.derecho
        if lado == "izq":
          nodoPadre.izquierdo = nodoPred
        else:
          nodoPadre.derecho = nodoPred
      elif nodoEliminar.tieneIzquierdo():
        if lado == "izq":
          nodoPadre.izquierdo = nodoEliminar.izquierdo
        else:
          nodoPadre.derecho = nodoEliminar.izquierdo
      elif nodoEliminar.tieneDerecho():
        if lado == "izq":
          nodoPadre.izquierdo = nodoEliminar.derecho
        else:
          nodoPadre.derecho = nodoEliminar.derecho
      else:
        if lado == "izq":
          nodoPadre.izquierdo = None
        else:
          nodoPadre.derecho = None

  def eliminarCanción(self, nombreCancion):
    #Recibe una cancion por parametro y se busca en todos los interpretes que tenga 
    #la cancion para eliminarla de todos los interpretes.
    if self.canciones.tieneDato(nombreCancion):
      self.canciones.deleteAll(nombreCancion)
    if self.tieneDerecho():
      self.derecho.eliminarCanción(nombreCancion)
    if self.tieneIzquierdo():
      self.izquierdo.eliminarCanción(nombreCancion)

  def cancionesEnNivel(self, nivel, listaCancionesNivel = Lista(), nivelNodo = 0):
    #Busca las canciones que esten en el nivel dado por parametro y retorna una lista 
    #de todas las canciones que se encuentren en ese nivel.
    if nivelNodo == nivel:
      listaCancionesNivel.insertarLista(self.cancionesDelInterprete())
    else:
      if self.tieneDerecho():
        self.derecho.cancionesEnNivel(nivel, listaCancionesNivel, nivelNodo+1)
      if self.tieneIzquierdo():
        self.izquierdo.cancionesEnNivel(nivel, listaCancionesNivel, nivelNodo+1)
    return listaCancionesNivel

  def cantidadCancionesDelInterprete(self):
    #Retorna la cantidad de canciones del interprete
    return self.canciones.len()

  def interpretesConMasCanciones(self, cantidadCancionesMinima, listaInterpretes = Lista()):
    #Se crea una lista de interpretes 
    if self.cantidadCancionesDelInterprete() > cantidadCancionesMinima:
      #En el caso de que el interprete tenga mas canciones que la cantidad minima
      #dada por parametro la agrega a la lista.
      listaInterpretes.append(self.interprete)
    if self.tieneIzquierdo():
      self.izquierdo.interpretesConMasCanciones(cantidadCancionesMinima)
    if self.tieneDerecho():
      self.derecho.interpretesConMasCanciones(cantidadCancionesMinima)
    return listaInterpretes.len()

  def cantidadTotalInterpretes(self, palabra, listaInterpretes=Lista()):
    if re.search(palabra,self.interprete):
      listaInterpretes.append(self.interprete)
    if self.tieneIzquierdo():
      self.izquierdo.cantidadTotalInterpretes(palabra)
    if self.tieneDerecho():
      self.derecho.cantidadTotalInterpretes(palabra)
    return listaInterpretes

  def internosAlfabetico(self):
    #crea su lista de internos
    listaInternos = Lista()
    if not self.esHoja():
      #agrega el nodo en el que esta parado
      #si este no es hoja.
      listaInternos.append(self.interprete)
    if self.tieneIzquierdo():
      #y luego va recorriendo el arbol llamando 
      #al mismo metodo recursivamente
      listaInternos.insertarLista(self.izquierdo.internosAlfabetico())
    if self.tieneDerecho():
      listaInternos.insertarLista(self.derecho.internosAlfabetico())
    return listaInternos

  def treePlot(self, dot):
        if self.tieneIzquierdo():
            dot.node(str(self.izquierdo.interprete), str(self.izquierdo.interprete))
            dot.edge(str(self.interprete), str(self.izquierdo.interprete))
            self.izquierdo.treePlot(dot)
        else:
            dot.node("None"+str(self.interprete)+"l", "None")
            dot.edge(str(self.interprete), "None"+str(self.interprete)+"l")
        if self.tieneDerecho():
            dot.node(str(self.derecho.interprete), str(self.derecho.interprete))
            dot.edge(str(self.interprete), str(self.derecho.interprete))
            self.derecho.treePlot(dot)
        else:
            dot.node("None"+str(self.interprete)+"r", "None")
            dot.edge(str(self.interprete), "None"+str(self.interprete)+"r")
##ARBOL
class ArbolDeCanciones:
  def __init__(self, startList = None):
    self.raiz = None
    if startList != None:
      for element in startList:
        self.insertar(element)

  def estaVacio(self):
    return self.raiz == None
  
  def insertarInterprete(self, interprete):
    #Recursiva del nodoArbolDeCanciones
    nuevoNodo = NodoArbolDeCanciones(interprete)
    if self.estaVacio():
      self.raiz = nuevoNodo
    else:
      self.raiz.insertarInterprete(nuevoNodo)

  def estaInterprete(self, interprete):
    #Recursiva del nodoArbolDeCanciones. Devuelve si esta o no.
    estaDato = False
    if not self.estaVacio():
      estaDato = self.raiz.estaInterprete(interprete) != None
    return estaDato

  def buscarInterprete(self, interprete):
    #Recursiva del nodoArbolDeCanciones. Devuelve el interprete.
    estaDato = None
    if not self.estaVacio():
      estaDato = self.raiz.estaInterprete(interprete) 
    return estaDato

  def cancionesDelInterprete(self, interprete):
    #Recursiva del nodoArbolDeCanciones. Devuelve las canciones del inteprete 
    #dado por parametro.
    if self.estaInterprete(interprete): 
      return self.buscarInterprete(interprete).cancionesDelInterprete()
    else:
      print("El interprete no esta en el arbol.")

  def insertarCanciones(self, listaCanciones, nombreInterprete):
    #Ingresa las canciones de la lista dada por parametro.
    if not self.estaInterprete(nombreInterprete):
      #Si el interprete no esta ingresa el interprete y las canciones al interprete.
      self.insertarInterprete(nombreInterprete)
      self.cancionesDelInterprete(nombreInterprete).insertarLista(listaCanciones)
    else:
      #Si el interprete ya esta en el arbol entonces solo ingresa las canciones.
      self.cancionesDelInterprete(nombreInterprete).insertarLista(listaCanciones)  

  def interpretesDeCancion(self, cancion):
    #Recursiva del nodoArbolDeCanciones
    if not self.estaVacio():
      return self.raiz.interpretesDeCancion(cancion)

  def buscarCanciones(self, listaInterpretes, pos=0, cancionesEnComun=Lista()):
    #Busca las canciones en comun que tienen todos los interpretes de la lista
    #ingresada por parametro.
    while pos < listaInterpretes.len():
      #Repite mientras la posicion sea menos a la cantidad de elementos de la lista.
      interprete = listaInterpretes.get(pos)
      canciones = self.cancionesDelInterprete(interprete)
      if pos == 0:
        if self.estaInterprete(interprete):
          cancionesEnComun.insertarLista(canciones)
          pos+=1
        else:
          pos+=1
      else:
        if self.estaInterprete(interprete):
          cancionesEnComun = cancionesEnComun.datosCompartidos(canciones)
          pos+=1
        else:
          pos+=1
    return cancionesEnComun

  def maximo(self):
    maximo = None 
    if not self.estaVacio():
      maximo = self.raiz.buscaMaximo().interprete
    return maximo

  def eliminarInterprete(self, nombreInterprete):
    if not self.estaVacio():
      if nombreInterprete == self.raiz.interprete:
        if self.raiz.grado() == 2:
          nodoPred = self.raiz.predecesor()
          self.eliminarInterprete(nodoPred.interprete)
          nodoPred.izquierdo = self.raiz.izquierdo
          nodoPred.derecho = self.raiz.derecho
          self.raiz = nodoPred
        elif self.raiz.tieneIzquierdo():
          self.raiz = self.raiz.izquierdo
        elif self.raiz.tieneDerecho():
          self.raiz = self.raiz.derecho
        else:
          self.raiz = None
      else:
        self.raiz.eliminarInterprete(nombreInterprete)

  def eliminarCancion(self, nombreCancion):
    #Recursiva del nodoArbolDeCanciones
    return  self.raiz.eliminarCanción(nombreCancion) 



  def cancionesEnNivel(self, nivel):
    #Recursiva del nodoArbolDeCanciones
    if not self.estaVacio():
      return self.raiz.cancionesEnNivel(nivel)

  def cantidadCancionesDelInterprete(self, interprete):
    #Recursiva del nodoArbolDeCanciones
    return self.buscarInterprete(interprete).cantidadCancionesDelInterprete()

  def interpretesConMasCanciones(self, cantidadCancionesMinima):
    #Recursiva del nodoArbolDeCanciones
    return self.raiz.interpretesConMasCanciones(cantidadCancionesMinima)

  def raizBalanceada(self):
    subArbol1 = 0  #el 1 es el izquierdo, y el 2: el derecho
    subArbol2 = 0
    if self.raiz.tieneIzquierdo():
      subArbol1 = self.raiz.izquierdo.altura()
    if self.raiz.tieneDerecho():
      subArbol2 = self.raiz.derecho.altura()
    return subArbol1 in (subArbol2 - 1, subArbol2 + 2)

  def cantidadTotalInterpretes(self, palabra):
    #Recursiva del nodoArbolDeCanciones
    if not self.estaVacio():
      return self.raiz.cantidadTotalInterpretes(palabra)

  def internosAlfabetico(self):
    #crea la lista con los internos a llenar
    listaInternos = Lista()
    if not self.estaVacio():
      #si no esta vacio, inserta a la lista de
      #internos, otra lista que devuelve el nodo
      listaInternos.insertarLista(self.raiz.internosAlfabetico())
    #retorna listaInternos con los nodos
    return listaInternos

