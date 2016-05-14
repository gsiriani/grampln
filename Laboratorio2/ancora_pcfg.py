# -*- encoding: utf-8 -*-

#
#  Gramáticas Formales para el Lenguaje Natural
#  Grupo de PLN (InCo) - 2016
#
#  Entrega 2 - Treebanks, PCFG y Parsing
#
#  Este template define clases por sección y tiene metodos a ser completados.
#  Completar las secciones siguiendo su especificación y la letra de la entrega.
#
#
#  Grupo: 08
#
#  Estudiante 1: Nom1 Nom2 Ap1 Ap2 - CI
#  Estudiante 2:
#  Estudiante 3: Guillermo Daniel Siriani Cabrera - 4333712-7
#
#


import nltk
import ancora  # (Modulo para leer AnCora)


# Parte 1 - Corpus
###################

class Corpus:
    """
    Clase de funcionalidades sobre el corpus AnCora.
    """

    def __init__(self, corpus_path='./ancora-2.0/'):
        # Cargar corpus desde 'corpus_path'
        self.corpus =  ancora.AncoraCorpusReader(corpus_path)

    ## Parte 1.1
    # a.
    def cant_oraciones(self):
        """
        Retorna la cantidad de oraciones del corpus.
        """
        return len(self.corpus.sents())

    # b.
    def oracion_mas_larga(self):
        """
        Retorna la oracion mas larga.
        (la primera si hay mas de una con el mismo largo)
        """
        # Obtengo la lista de oraciones
        oraciones = self.corpus.sents()
        # Inicializo las variables con la primer oracion de la lista
        mas_larga = oraciones[0]    # oracion mas larga
        largo_max = len(oraciones[0])          # largo de la oracion mas larga
        for o in oraciones:
            if len(o) > largo_max:
                # Actualizo la oracion mas larga
                largo_max = len(o)
                mas_larga = o
        return mas_larga

    # c.
    def largo_promedio_oracion(self):
        """
        Retorna el largo de oracion promedio.
        """
        # Obtengo la lista de oraciones
        oraciones = self.corpus.sents()
        # Obtengo cantidad de oraciones
        cantidad_oraciones = len(self.corpus.sents())
        # Obtengo suma del largo de las oraciones
        suma_largos = 0
        for o in oraciones:
            suma_largos += len(o)
        # Calculo promedio
        promedio = suma_largos / cantidad_oraciones
        return promedio

    # d.
    def palabras_frecs(self):
        """
        Retorna un diccionario (dict) palabra-frecuencia de las palabras del corpus.
        (considerar las palabras en minúsculas)
        """
        # Creo el diccionario
        diccionario = {}
        # Obtengo lista de palabras
        palabras = self.corpus.tagged_words()
        # Recorro la lista de palabras
        for (p,t) in palabras:
            p_min = p.lower()
            if diccionario.has_key(p_min):
                diccionario[p_min] = diccionario[p_min] + 1
            else:
                diccionario[p_min] = 1
        return diccionario

    # e.
     def palabras_frecs_cat(self):
        """
        Retorna un diccionario (dict) palabra-lista de las palabras del corpus.
        Cada lista contiene la frecuencia por cada categoría de la palabra.
        (considerar las palabras en minúsculas)
        """
        return # ...



    ## Parte 1.2
    # a
    def arbol_min_nodos(self):
        """
        Retorna el árbol del corpus con la mínima cantidad de nodos.
        (el primero si hay mas de uno con la misma cantidad)
        """
        return # ...

    def arbol_max_nodos(self):
        """
        Retorna el árbol del corpus con la máxima cantidad de nodos.
        (el primero si hay mas de uno con la misma cantidad)
        """
        return # ...


    # b
    def arboles_con_lema(self, lema):
        """
        Retorna todos los árboles que contengan alguna palabra con lema 'lema'.
        """
      return # ...

   


# Parte 2 - PCFG y Parsing
###########################


class PCFG:
    """
    Clase de funcionalidades sobre PCFG de AnCora.
    """

    sents = [   u'El juez manifestó que las medidas exigidas por el gobierno actual son muy severas .', #a
                u'El partido entre los equipos europeos tendrá lugar este viernes .', #b
                u'El domingo próximo se presenta la nueva temporada de ópera .', #c
            ]

    def __init__(self):
        corpus = Corpus()
        self.wordfrecs = corpus.palabras_frecs()
        self.grammar = self._induce_pcfg(corpus)
        self.parser  = self._generate_parser()

    ## Parte 2.1 (grammar)
    def _induce_pcfg(self, corpus):
        """
        Induce PCFG del corpus.
        """
        return # ...

    # a
    def reglas_no_lexicas(self):
        """
        Retornas las reglas que no son léxicas.
        """
        return # ...

    # b 
    def categorias_lexicas(self):
        """
        Retorna las categorías léxicas (se infieren de las reglas léxicas).
        """
        return # ...
        

    # c
    def reglas_lexicas(self, c):
        """
        Retorna las reglas léxicas de categoría 'c'
        """
        return # ...

    ## Parte 2.2 (parser)
    def _generate_parser(self):
        """
        Generate Viterbi parser from grammar.
        """
        return # ...

    ## Parte 2.3 (sentences)
    def parse(self, sentence):
        """
        Parse sentence and return ProbabilisticTree.
        """
        return # ...



# Parte 3 - PCFG con palabras desconocidas
##########################################


class PCFG_UNK(PCFG):
    """
    Clase de funcionalidades sobre PCFG de AnCora con UNK words.
    """

    sents = [   u'El domingo próximo se presenta la nueva temporada de ópera .', #a (2.3.c)
                u'Pedro y Juan jugarán el campeonato de fútbol .', #b 
            ]


    # Parte 3.1
    def _induce_pcfg(self, corpus):
        """
        Induce PCFG grammar del corpus (treebank) considerando palabras UNK.
        """
        return # ...


    # Parte 3.2 (y 3.3)

    def parse(self, sentence):
        """
        Retorna el análisis sintáctico de la oración contemplando palabras UNK.
        """
        return # ...



# Parte 4 - PCFG lexicalizada
##############################

# 1

class PCFG_LEX(PCFG):
    """
    PCFG de AnCora con lexicalización en primer nivel.
    """

    sents = [   u'El juez vino que avión .', #
            ]                

    def _induce_pcfg(self, corpus):
        """
        Induce PCFG del corpus considerando lexicalización en primer nivel.
        """
        return # ...





# 2

class PCFG_LEX_VERB(PCFG):
    """
    PCFG de AnCora con lexicalización en primer nivel y grupos verbales (grup.verb).
    """

    sents = [   u'El juez manifestó su apoyo al gobierno .', # i
                u'El juez opinó su apoyo al gobierno .', # ii

                u'El juez manifestó que renunciará .', # 4.2.c
            ]                

    def _induce_pcfg(self, corpus):
        """
        Induce PCFG del corpus considerando lexicalización en primer nivel y grupos verbales.
        """
        return # ...



