from __future__ import division
from pylab import *
try:
    import Image
except ImportError:
    from PIL import Image
from pytesseract import image_to_string
import string

img = Image.open('eng.jpg')
story = image_to_string(img, lang = 'eng')

#To do away with punctuations
replace_punc = string.maketrans(string.punctuation,
    ' '*len(string.punctuation))
story = story.translate(replace_punc)

words = {}
for w in filter(None,story.split(' ')):
    if w in words:
        words[w]+=1
    else:
        words[w] = 1

y = array(sorted(words.values(), reverse = True))

x = arange(1,len(y)+1)
plot(x,y)
title('Number of occurences of words')
y0 = 1/y[y>1]

c = average(arange(1,1+len(y0))/y0)
plot(x,c/x)
legend(('Experimental values','Theoretical values'))
show()