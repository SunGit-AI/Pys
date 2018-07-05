'''
Created on 02.07.2018

@author: xsun
'''

import numpy as np



def test_f1():
    a = np.matrix('1 2; 3 4')
    v1 = np.matrix('3; 3')
    v2 = np.matrix('2; 5')
    v3 = a*v1 + a*v2
    v4 = a*(v1 + v2)
    print("v3 is %s, v4 is %s" %(v3, v4))

    
if __name__ == '__main__':

    test_f1()