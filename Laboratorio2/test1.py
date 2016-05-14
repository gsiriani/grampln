from ancora_pcfg import Corpus

c = Corpus()

print 'cant_oraciones:'
print c.cant_oraciones()

print '\nOracion mas larga:'
print c.oracion_mas_larga()

print '\nLargo promedio oracion:'
print c.largo_promedio_oracion()

print '\nPalabras-frecuencia:'
print c.palabras_frecs()