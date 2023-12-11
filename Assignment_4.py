from nltk import ngrams
from nltk.util import ngrams
n=2
text='i am ishwar wagh from washim'
unigrams=ngrams(text.split(),n)
for i in unigrams:
  print(i)

"""
('i', 'am')
('am', 'ishwar')
('ishwar', 'wagh')
('wagh', 'from')
('from', 'washim')

"""