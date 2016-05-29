# -*- coding: utf-8 -*-

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
#  Estudiante 1: Bruno Garate Schapira - 4941297-5
#  Estudiante 2: Santiago Paez Castro - 4848301-0
#  Estudiante 3: Guillermo Daniel Siriani Cabrera - 4333712-7
#
#

import nltk
import ancora  #(Modulo para leer AnCora)
from __future__ import division

# Parte 1 - Corpus
###################

class Corpus:
    """
    Clase de funcionalidades sobre el corpus AnCora.
    """

    def __init__(self, corpus_path='./ancora/ancora-2.0/'):
        # Cargar corpus desde 'corpus_path'
        self.corpus =  ancora.AncoraCorpusReader(corpus_path)
        self.lemas = self.corpus.stemmed_words()

    ## Parte 1.1
    # a.
    def cant_oraciones(self):
        """
        Retorna la cantidad de oraciones del corpus.
        """
        return  len(self.corpus.tagged_sents())

    # b.
    def oracion_mas_larga(self):
        """
        Retorna la oracion mas larga.
        (la primera si hay mas de una con el mismo largo)
        """
        word_count = lambda sentence: len(sentence)
        return ' '.join(max(self.corpus.sents(), key=word_count))

    # c.
    def largo_promedio_oracion(self):
        """
        Retorna el largo de oracion promedio.
        """
        return  len(self.corpus.tagged_words())/len(self.corpus.tagged_sents())

    # d.
    def palabras_frecs(self):
        """
        Retorna un diccionario (dict) palabra-frecuencia de las palabras del corpus.
        (considerar las palabras en minúsculas)
        """
        
        return dict(nltk.FreqDist([t[0].lower() for t in self.corpus.tagged_words()]))
        

    # e.
    def palabras_frecs_cat(self):
        """
        Retorna un diccionario (dict) palabra-lista de las palabras del corpus.
        Cada lista contiene la frecuencia por cada categoría de la palabra.
        (considerar las palabras en minúsculas)
        """
        from collections import defaultdict
        
        dicc1 = dict(nltk.FreqDist([(w.lower(), c) for (w, c) in self.corpus.tagged_words()]))

        dicc2 = defaultdict(list)
        for k, v in dicc1.iteritems():
            dicc2[k[0]].append((k[1], v))
        
        return dict(dicc2)
    
    def obtener_lema(self, palabra):
        """
        Retorna el lema de la palabra pasada por parametro.
        El lema es el que se encuentra en el corpus AnCora.
        """
        return self.lemas[palabra].lower()
    
    
    ## Parte 1.2
    # a
    def arbol_min_nodos(self):
        """
        Retorna el árbol del corpus con la mínima cantidad de nodos.
        (el primero si hay mas de uno con la misma cantidad)
        """
        trees = self.corpus.parsed_sents()

        helper = [(index, len(t.treepositions())) for index, t in enumerate(trees)]
        helper.sort(key=lambda x: x[1])
        
        return trees[helper[0][0]]

    def arbol_max_nodos(self):
        """
        Retorna el árbol del corpus con la máxima cantidad de nodos.
        (el primero si hay mas de uno con la misma cantidad)
        """
        trees= self.corpus.parsed_sents()
        
        helper = [(index, len(t.treepositions())) for index, t in enumerate(trees)]
        helper.sort(key=lambda x: x[1])
        
        return trees[helper[-1][0]]


    # b
    def arboles_con_lema(self, lema):
        """
        Retorna todos los árboles que contengan alguna palabra con lema 'lema'.
        """
        
        return [t for t in self.corpus.parsed_sents() if lema in map(lambda x: self.obtener_lema(x.lower()), t.leaves())]

   
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
        
        productions = []
        S = nltk.Nonterminal('sentence')
        for tree in corpus.corpus.parsed_sents():
            # Trasnformamos los arboles para obtener las reglas en Forma Normal de Chomsky.
            #tree.collapse_unary(collapsePOS = True, collapseRoot = True)
            #tree.chomsky_normal_form(horzMarkov = 2)
            
            # Transformo todas las hojas del arbol a minuscula
            for t in tree.treepositions('leaves'):
                tree[t] = tree[t].lower()
            
            productions += tree.productions()

        return nltk.induce_pcfg(S, productions)

    # a
    def reglas_no_lexicas(self):
        """
        Retornas las reglas que no son léxicas.
        """
        return [regla for regla in self.grammar.productions() if regla.is_nonlexical()]

    # b 
    def categorias_lexicas(self):
        """
        Retorna las categorías léxicas (se infieren de las reglas léxicas).
        """
        # La lista devuelta no tiene elementos repetidos.
        set_categorias = set([regla.rhs()[0] for regla in self.grammar.productions() if regla.is_lexical()])
        lista_categorias = list(set_categorias)
        return lista_categorias
        

    # c
    def reglas_lexicas(self, c):
        """
        Retorna las reglas léxicas de categoría 'c'
        """
        # Debe recibir un string, se realiza la conversion a simbolo no-terminal dentro de la funcion.
        return [regla for regla in self.grammar.productions() if regla.is_lexical() and regla.lhs() == nltk.Nonterminal(c)]

    ## Parte 2.2 (parser)
    def _generate_parser(self):
        """
        Generate Viterbi parser from grammar.
        """
        return nltk.ViterbiParser(self.grammar)

    ## Parte 2.3 (sentences)
    def parse(self, sentence):
        """
        Parse sentence and return ProbabilisticTree.
        """
        # TODO: Tratar el caso cuando hay palabras en la oracion que no esten en la gramatica.
        
        tokens = [w.lower() for w in nltk.word_tokenize(sentence)]
        
        return self.parser.parse_one(tokens)


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
            # Trasnformamos los arboles para obtener las reglas en Forma Normal de Chomsky.
            #tree.collapse_unary(collapsePOS = True, collapseRoot = True)
            #tree.chomsky_normal_form(horzMarkov = 2)
            
            # Transformo todas las hojas a minusculas.
            for t in tree.treepositions('leaves'):
                tree[t] = tree[t].lower()
            
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
        
        return self.parser.parse_one(unk_tokens)

# Parte 4 - PCFG lexicalizada
##############################

# 4.1

from nltk.stem.snowball import SpanishStemmer

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
        
        #stemmer = SpanishStemmer()
        
        S = nltk.Nonterminal('sentence')
        
        arboles = []
        for tree in corpus.corpus.parsed_sents():
            # Trasnformamos los arboles para obtener las reglas en Forma Normal de Chomsky.
            #tree.collapse_unary(collapsePOS = True, collapseRoot = True)
            #tree.chomsky_normal_form(horzMarkov = 2)
            arboles.append(tree.copy())      
    
        # Hago parent annotation del nivel superior a las hojas utilizando el lema de la hoja.
        productions = []
        for arbol in arboles:
            for t in arbol.treepositions('leaves'):
                arbol[t] = arbol[t].lower()
                t_p = tuple(x[1] for x in enumerate(t) if x[0] != len(t)-1)
                arbol[t_p].set_label(arbol[t_p].label() + "#" + corpus.obtener_lema(arbol[t]))
            productions.extend(arbol.productions())


        return nltk.induce_pcfg(S, productions)

# 4.2

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
        S = nltk.Nonterminal('sentence')
        
        # Hago parent annotation del nivel superior a las hojas utilizando el lema de la hoja.
        productions = []
        for arbol in corpus.corpus.parsed_sents():
            for t in arbol.treepositions('leaves'):
                arbol[t] = arbol[t].lower()
                t_p = tuple(x[1] for x in enumerate(t) if x[0] != len(t)-1)
                arbol[t_p].set_label(arbol[t_p].label() + "#" + corpus.obtener_lema(arbol[t]))
                verbo = corpus.obtener_lema(arbol[t])
                if verbo.endswith(("ar", "er", "ir",)) and "_" not in verbo:
                    t_p2 = tuple(x[1] for x in enumerate(t_p) if x[0] != len(t_p)-1)
                    if arbol[t_p2].label() == "grup.verb":
                        arbol[t_p2].set_label(arbol[t_p2].label() + "#" + verbo)
            productions.extend(arbol.productions())

        return nltk.induce_pcfg(S, productions)

