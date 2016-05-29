# -*- coding: utf-8 -*-

from nltk.corpus.reader import SyntaxCorpusReader
from nltk.corpus.reader import api
from nltk.corpus.reader import xmldocs
from nltk import tree
from nltk import util
from nltk.corpus.reader.util import concat
from nltk.util import LazyMap


def parsed(element):
	if element:
		# element viewed as a list is non-empty (it has subelements)
		subtrees = map(parsed, element)
		subtrees = [t for t in subtrees if t is not None]
		return tree.Tree(element.tag, subtrees)
	else:
		# element viewed as a list is empty. we are in a terminal.
		if element.get('elliptic') == 'yes':
			return None
		else:
			return tree.Tree(element.get('pos') or element.get('ne') or 'unk', [element.get('wd')])


def lem_parsed(element):
	if element:
		# element viewed as a list is non-empty (it has subelements)
		subtrees = map(lem_parsed, element)
		subtrees = [t for t in subtrees if t is not None]
		return tree.Tree(element.tag, subtrees)
	else:
		# element viewed as a list is empty. we are in a terminal.
		if element.get('elliptic') == 'yes':
			return None
		else:
			return tree.Tree(element.get('lem') or element.get('ne') or 'unk', [element.get('wd')])


def stemmed(element):
	return filter(lambda x: x != (None, None), lem_parsed(element).pos())

def tagged(element):
    # http://www.w3schools.com/xpath/xpath_syntax.asp
    # XXX: XPath '//*[@wd]' not working
    #return [(x.get('wd'), x.get('pos') or x.get('ne')) for x in element.findall('*//*[@wd]')] + [('.', 'fp')]
    return filter(lambda x: x != (None, None), parsed(element).pos())


def untagged(element):
    # http://www.w3schools.com/xpath/xpath_syntax.asp
    # XXX: XPath '//*[@wd]' not working
    #return [x.get('wd') for x in element.findall('*//*[@wd]')] + [('.', 'fp')]
    return filter(lambda x: x is not None, parsed(element).leaves())


class AncoraCorpusReader(SyntaxCorpusReader):

    #def __init__(self, xmlreader):
    #    self.xmlreader = xmlreader
	def __init__(self, path):
		super(AncoraCorpusReader, self).__init__(path + '3LB-CAST', '.*\.xml')
		self.xmlreader = xmldocs.XMLCorpusReader(path + '3LB-CAST', '.*\.xml')

	def parsed_sents(self, fileids=None):
	  if not fileids:
		   fileids = self.xmlreader.fileids()
	  return LazyMap(parsed, concat([list(self.xmlreader.xml(fileid)) for fileid in fileids]))

	def tagged_sents(self, fileids=None):
	  if not fileids:
		   fileids = self.xmlreader.fileids()
	  return LazyMap(tagged, concat([list(self.xmlreader.xml(fileid)) for fileid in fileids]))

	def sents(self, fileids=None):
	  # FIXME: not lazy!
	  if not fileids:
		   fileids = self.xmlreader.fileids()
	  return LazyMap(untagged, concat([list(self.xmlreader.xml(fileid)) for fileid in fileids]))

	def tagged_words(self, fileids=None):
	  return concat(self.tagged_sents(fileids))


	def stemmed_sents(self, fileids=None):
		if not fileids:
			fileids = self.xmlreader.fileids()
		return LazyMap(stemmed, concat([list(self.xmlreader.xml(fileid)) for fileid in fileids]))

	def stemmed_words(self, fileids=None):
		return { t[0].lower(): t[1].lower() for t in concat(self.stemmed_sents(fileids)) }

