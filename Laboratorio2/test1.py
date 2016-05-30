from ancora_pcfg import *

#print '****************'
#print 'PARTE 1'
#print '****************'
#
#c = Corpus()
#
#print 'cant_oraciones:'
#print c.cant_oraciones()
#
#print '\nOracion mas larga:'
#print c.oracion_mas_larga()
#
#print '\nLargo promedio oracion:'
#print c.largo_promedio_oracion()
#
#print '\nFrecuencia de palabras:'
#print c.palabras_frecs()
#
#print '\nFrecuencia de palabras por categoria:'
#print c.palabras_frecs_cat()
#
#print '\nArbol con minimos nodos:'
#print c.arbol_min_nodos()
#
#print '\nArbol con maximos nodos:'
#print c.arbol_max_nodos()
#
#print '\nArboles con lema:'
#print c.arboles_con_lema(lema = 'ser')
#

#print '****************'
#print 'PARTE 2'
#print '****************'
#
p = PCFG()
#
#print '\nReglas no lexicas:'
#print p.reglas_no_lexicas()
#
#print '\nCategorias lexicas:'
#print p.categorias_lexicas()
#
#print '\nReglas lexicas:'
#print p.reglas_lexicas('px3mp000')
#
#print '\nAnalisis de sentencias:'
#for str in p.sents:
#	print str + ':\n'
#	print p.parse(str)
#	
#	
print '****************'
print 'PARTE 3'
print '****************'

u = PCFG_UNK()

print '\nAnalisis de sentencias:'
for str in u.sents:
	print str + ':\n'
	print u.parse(str)
		
print '****************'
print 'PARTE 4'
print '****************'

l = PCFG_LEX()

print '\nAnalisis 4.1:'

for str in l.sents:
	print str + ':'
	print '\nAnalisis a:\n'
	print p.parse(str)
	print '\nAnalisis b:\n'
	print l.parse(str)
	
v = PCFG_LEX_VERB()
	
print '\nAnalisis 4.2:'
for str in v.sents:
	print str + ':'
	print '\nAnalisis a:\n'
	print l.parse(str)
	print '\nAnalisis b:\n'
	print v.parse(str)