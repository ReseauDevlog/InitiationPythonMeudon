# -*- coding: utf-8 -*-

def myformat(values):
    fe = ['{:+.1f}']*len(values)
    fg = '('+', '.join(fe)+')'
    return fg.format(*values)

def myformat2d(values):
    temp =  []
    for v in values:
        temp.append(myformat(v))
    fe = ['{}']*len(temp)
    fg = '('+', '.join(fe)+')'
    return fg.format(*temp)



