from ancora_pcfg import Corpus

c = Corpus()

print 'cant_oraciones:'
print c.cant_oraciones()

print '\nOracion mas larga:'
print c.oracion_mas_larga()

print '\nLargo promedio oracion:'
print c.largo_promedio_oracion()

print '\nFrecuencia de palabras:'
print c.palabras_frecs()

print '\nFrecuencia de palabras por categoria:'
print c.palabras_frecs_cat()

print '\nArbol con minimos nodos:'
print c.arbol_min_nodos()

print '\nArbol con maximos nodos:'
print c.arbol_max_nodos()

print '\nArboles con lema:'
print c.arboles_con_lema(lema = 'vaic3s0')