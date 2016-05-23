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
#  Estudiante 2: Santiago Paez Castro - 4848301-0
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
        # Creo el diccionario
        diccionario = {}
        # Obtengo lista de palabras
        palabras = self.corpus.tagged_words()
        # Recorro la lista de palabras
        for (p,t) in palabras:
            p_min = p.lower()
            if diccionario.has_key(p_min):
                if diccionario[p_min].has_key(t):
                    diccionario[p_min][t] += 1
                else:
                    diccionario[p_min][t] = 1
            else:
                diccionario[p_min] = {}
                diccionario[p_min][t] = 1
        return diccionario


        
    ## Parte 1.2

    # Funcion auxiliar para contar los nodos de un arbol
    def cantidad_nodos(self, t):
        cant = 0
        # Sumo todos los subarboles (nodos intermedios)
        for subtree in t.subtrees():
            cant += 1
        # Sumo todas las hojas
        for hoja in t.leaves():
            cant += 1
        return cant

    # a
    def arbol_min_nodos(self):
        """
        Retorna el árbol del corpus con la mínima cantidad de nodos.
        (el primero si hay mas de uno con la misma cantidad)
        """
        arboles = self.corpus.parsed_sents()
        min_t = arboles[0]
        min_nodos = self.cantidad_nodos(arboles[0])
        for t in arboles:
            c = self.cantidad_nodos(t)
            if c < min_nodos:
                min_nodos = c
                min_t = t
        return min_t

    def arbol_max_nodos(self):
        """
        Retorna el árbol del corpus con la máxima cantidad de nodos.
        (el primero si hay mas de uno con la misma cantidad)
        """
        arboles = self.corpus.parsed_sents()
        max_t = arboles[0]
        max_nodos = self.cantidad_nodos(arboles[0])
        for t in arboles:
            c = self.cantidad_nodos(t)
            if c > max_nodos:
                max_nodos = c
                max_t = t
        return max_t


    # b
    def arboles_con_lema(self, lema):
        """
        Retorna todos los árboles que contengan alguna palabra con lema 'lema'.
        """
        arboles = self.corpus.parsed_sents()
        res = []
        for subtree in arboles:
            for aux in subtree.subtrees(filter = lambda t: t.label()==lema):
                res.append(subtree)
                break
        return res

   


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
		  unk_words = {k for k,v in self.wordfrecs.iteritems() if v == 1}
        
        productions = []
        for tree in corpus.corpus.parsed_sents():
             productions += tree.productions()

        new_productions = []
        for pr in productions:
            if len(pr.rhs()) == 1 and pr.rhs()[0] in unk_words:
                new_pr = nltk.grammar.Production(pr.lhs(), ['UNK'])
                new_productions.append(new_pr)
            else:
                new_productions.append(pr)


        
        S = nltk.Nonterminal('sentence')
        
        return nltk.induce_pcfg(S, new_productions)



    # Parte 3.2 (y 3.3)

    def parse(self, sentence):
        """
        Retorna el análisis sintáctico de la oración contemplando palabras UNK.
        """
        tokens = [w.lower() for w in nltk.word_tokenize(sentence)]
        
        all_words = {k for k,v in self.wordfrecs.iteritems()}
        
        unk_words = {k for k,v in self.wordfrecs.iteritems() if v == 1}
        
        unk_tokens = [w if w not in unk_words and w in all_words else "UNK" for w in tokens]
        
        # Si se hace esto, las palabras con frecuencia 1 no son reconocidas y el parser tira error, ej: juan.
        #unk_tokens = [w if w in all_words else "UNK" for w in tokens]
        
        return self.parser.parse_one(unk_tokens)

'''
Parte 3.3
pcfg_unk = PCFG_UNK()

pcfg_unk.parse(pcfg_unk.sents[0])

 En este caso, la unica palabra de la oracion que no se encuentra en la gramatica es "opera".
 Por lo que la palabra se cambia por "UNK" y el parser la identifica como un nombre comun.
 En este caso esta tecnica (cambiar palabras desconocidas por "UNK") produce un buen resultado.
'''

'''
Parte 3.3b
pcfg_unk.parse(pcfg_unk.sents[1])

 En este caso, existen cuatro palabras que no se encuentran en el corpus y por ende son cambiadas por "UNK".
 Dichas palabras son: pedro, juan, jugaran y campeonato.
 El resultado que obtiene el parser no es bueno en este caso, no ayuda el hecho de que la mitad de la oracion
 este compuesta por palabras desconocidas.
'''

'''
Parte 3.4

El uso de una tecnica como la utilizada en las partes 3.1 y 3.2 permite que nuestro parser sea capaz de procesar 
oraciones que tengan palabras que no se encuentren en el corpus utilizado.
Poder analizar oraciones con palabras desconocidas es una buena propiedad para un parser, ya que independientemente
del tamanio del corpus utilizado para deducir las reglas de la gramatica, es dificil que dicho corpus posea todas las
palabras del vocabulario.

Como vimos en las oraciones de ejemplo analizadas, esta tecnica produce resultados de variada calidad. A medida que 
que aumente la proporcion de palabras desconocidas en una oracion, resultara mas dificil para el parser realizar un
analisis de calidad.

Otro problema de esta tecnica es que al agrupar todas las reglas de palabras poco frecuentes como "UNK", corremos el
riesgo de clasificar erroneamente algunas palabras. Esto sucede por ejemplo con la palabra "juan", la cual en el
analisis obtenido es clasificada como un verbo, cuando en realidad es un nombre propio.

Un enfoque alternativo podria ser el de analizar las palabras desconocidas de la oracion. Por ejemplo los nombres
propio comienzan con mayuscula, como Pedro y Juan (con la salvedad de que en este caso Pedro se encuentra al comienzo
de la oracion, donde resulta ambiguo su analisis), jugaran es una variacion del verbo jugar, el cual se encuentra en el 
corpus y por lo tanto podria ser etiquetado como verbo.
Aplicar este enfoque tiene una parte negativa, es necesario, una vez determinadas las categorias de las palabras
desconocidas encontradas en la oracion a analizar, hay que agregar dichas reglas a la gramatica y hay que volver a 
inferir el parser (actividades que son computacionalmente costosas).
'''


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



