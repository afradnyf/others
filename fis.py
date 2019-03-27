import pandas as pd
import time
import psutil
from ap import *
def freq(k, f, name):
    t1=time.time()
    m1=psutil.virtual_memory().available
    dw = 'docword.{}.txt'.format(name)
    vocab = 'vocab.{}.txt'.format(name)
    support = f
    frequency = k
    print('Loading Files...')
    with open(vocab) as g:
        words = g.read().splitlines()
    df = pd.read_csv(dw, header = None, delimiter = ' ', dtype = int, skiprows = 3)
    print('Converting to Transactions Format...')
    tr=[]
    for i in range(len(df.values)):
        tr.append([])
    for i in df.values:
        tr[i[0]-1].append(i[1])
    print('Carrying out Apriori Algorithm...')
    itemsets = apr(tr, min_support=support, max_length=frequency)
    print('Finalizing resutls...')
    p=[]
    try:
        for x in list(itemsets[frequency].items()):
            p.append(x[0])
    except KeyError:
        t2=time.time()
        print('Total time taken = {}'.format(t2-t1))
        print('No {}-sized sets are frequent in the data'.format(frequency))
        return (0,0,0)
    tw=[]
    for i in range(len(p)):
        tw.append([])
    x=0
    for i in range(len(p)):
        for j in range(frequency):
            tw[x].append(words[p[i][j]-1])
        x=x+1
    t2=time.time()
    m2=psutil.virtual_memory().available
    print('Total time taken = {} seconds'.format(t2-t1))
    print('Total memory used = {} MB'.format((m1-m2)/1000000))
    print(tr)
    return tr
