# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:41:09 2020

@author: jmsong
"""

import numpy as np
import scipy.constants as sc

def EF(a,n,l):
    return (2-np.exp(-1*(a*n)*l/1000))/(1+(a*n*l))
emission_data = "C:/Users/jmsong/Documents/00_NFRI/00_연구관리/00_실험데이터/01_OES/200102_Ar_emission_no head_24lines.txt"
emis_data = np.loadtxt(emission_data, dtype={'names':('WL', 'lstat','ustat','gl','gu','El','Eu','A'),'formats':('f4','S3','S4','i1','i1','f4','f4','f4')})
optical_l = 20e-3
Tg = float(300.0) #Gas temperature
density_range = ( list(np.arange(1,10,0.1)*1e9) + list(np.arange(1,10,0.1)*1e10) + list(np.arange(1,10,0.1)*1e11)
                + list(np.arange(1,10,0.1)*1e12) + list(np.arange(1,10,0.1)*1e13) + list(np.arange(1,10,0.1)*1e14)
                + list(np.arange(1,10,0.1)*1e15) + list(np.arange(1,10,0.1)*1e16) + list(np.arange(1,10,0.1)*1e17)
                + list(np.arange(1,10,0.1)*1e18) + list(np.arange(1,10,0.1)*1e19) + list(np.arange(1,10,0.1)*1e20))
head =list()
EFs = np.zeros((len(density_range),len(emis_data)+1))
for i, ed in enumerate(emis_data):
    head.append(ed[2].decode('UTF-8') + '->' + ed[1].decode('UTF-8') + '(' + str(ed[0]) + 'nm' + ')')
head = np.transpose(head)
for k, n in enumerate(density_range):
    for i, ed in enumerate(emis_data):
        EFs[k,0] = n
        a = 0
        a = (ed[0]*0.000000001)*(ed[0]*0.000000001)*(ed[0]*0.000000001) / 8 / np.sqrt(sc.pi)*np.sqrt(sc.pi)*np.sqrt(sc.pi) * ed[4] / ed[3] * ed[7] * np.sqrt(sc.proton_mass * 3.9948e+1 / (2.0 * sc.Boltzmann * Tg))
        sEF = EF(a,n,optical_l)
        EFs[k,i+1] = sEF