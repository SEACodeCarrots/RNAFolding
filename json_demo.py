#! /usr/bin/python
#
#
# Demonstration of the pickle module
#
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

gozinta = { 'A': { 'A': {'N' : 'U' },
                   'U': 'G' },
            'N': { 'G': 'U' }
        }

pp.pprint(gozinta)

f = open('demo.json', 'w')
json.dump(gozinta,f)
f.close()

g = open('demo.json', 'r')
comzouta=json.load(g)
g.close()
pp.pprint(comzouta)



