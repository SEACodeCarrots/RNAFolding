#! /usr/bin/python
#
#
# Demonstration of the pickle module
#
import pickle
import pprint
pp = pprint.PrettyPrinter(indent=4)

gozinta = { 'A': { 'A': {'N' : 'U' },
                   'U': 'G' },
            'N': { 'G': 'U' }
        }

pp.pprint(gozinta)

f = open('demo.pickle', 'w')
pickle.dump(gozinta,f)
f.close()

g = open('demo.pickle', 'r')
comzouta=pickle.load(g)
g.close()
pp.pprint(comzouta)



