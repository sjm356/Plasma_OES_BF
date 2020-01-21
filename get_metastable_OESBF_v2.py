# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 16:37:38 2020

@author: jmsong

v1: Creating code for calculating branching fraction of theoritical and experiment
v2: Adding function for finding peak height from OES data 
"""
from tkinter import *
from tkinter import filedialog
import os
import re
import numpy as np
import scipy.constants as sc
Tg = float(300.0) #Gas temperature

######################################################################################################
########################################### Calculation ##############################################
######################################################################################################

######################################################################################################
#################################### Branching fraction from emission data ###########################
######################################################################################################
emission_data = "C:/Users/jmsong/Documents/00_NFRI/00_연구관리/00_실험데이터/01_OES/200102_Ar_emission_no head_24lines.txt"
emis_data = np.loadtxt(emission_data, dtype={'names':('WL', 'lstat','ustat','gl','gu','El','Eu','A'),'formats':('f4','S3','S4','i1','i1','f4','f4','f4')})
a=np.zeros(len(emis_data))

# Function: Escape factor calculation
def EF(a,n,l):
    return (2-np.exp(-1*(a*n)*l/1000))/(1+(a*n*l))
    
# Setting metastable density range
'''
density_range = ( list(np.arange(1e9,10e9,1e9)) + list(np.arange(1e10,10e10,1e10))
                + list(np.arange(1e11,10e11,1e11)) + list(np.arange(1e12,10e12,1e12))
                + list(np.arange(1e13,10e13,1e13)) + list(np.arange(1e13,10e13,1e13)*10)
                + list(np.arange(1e13,10e13,1e13)*100) + list(np.arange(1e13,2e13,1e12)*1000) + list(np.arange(2e13,10e13,1e13)*1000)
                + list(np.arange(1e13,10e13,1e13)*10000) + list(np.arange(1e13,10e13,1e13)*100000))
'''
density_range = ( list(np.arange(1,10,0.1)*1e9) + list(np.arange(1,10,0.1)*1e10) + list(np.arange(1,10,0.1)*1e11)
                + list(np.arange(1,10,0.1)*1e12) + list(np.arange(1,10,0.1)*1e13) + list(np.arange(1,10,0.1)*1e14)
                + list(np.arange(1,10,0.1)*1e15) + list(np.arange(1,10,0.1)*1e16) + list(np.arange(1,10,0.1)*1e17)
                + list(np.arange(1,10,0.1)*1e18) + list(np.arange(1,10,0.1)*1e19) + list(np.arange(1,10,0.1)*1e20))
###############################################################################
########## Setting optical length #############################################
###############################################################################
optical_l = 10e-3
###############################################################################

nn = len(density_range)
BF = np.zeros((nn,31),dtype=float)
    
new_file_path = "C:\\Users\\jmsong\\Documents\\00_NFRI\\00_연구관리\\00_실험데이터\\01_OES"
new_file_name = 'Branching fraction'
new_file = open(new_file_path + "/" + new_file_name + ".dat",'w')
new_file.write(f'density(m-3) \t 1s2/2p1 \t 1s4/2p1 \t 1s2/2p2 \t 1s4/2p2 \t 1s3/2p2 \t 1s5/2p2 \t 1s2/2p3 \t 1s4/2p3 \t 1s5/2p3 \t 1s2/2p4 \t 1s4/2p4 \t 1s5/2p4 \t 1s2/2p6 \t 1s4/2p6 \t 1s5/2p6 \t 1s4/2p7 \t 1s3/2p7 \t 1s2/2p8 \t 1s4/2p8 \t 1s5/2p8 \t 1s4/2p10 \t 1s5/2p10 \n')

BF_deno_2p1 = 0
BF_deno_2p2 = 0
BF_deno_2p3 = 0
BF_deno_2p4 = 0
BF_deno_2p5 = 0
BF_deno_2p6 = 0
BF_deno_2p7 = 0
BF_deno_2p8 = 0
BF_deno_2p9 = 0
BF_deno_2p10 = 0

BF_1s2_2p1 = 0
BF_1s4_2p1 = 0
BF_nu_1s2_2p1 = 0
BF_nu_1s4_2p1 = 0

BF_1s2_2p2 = 0
BF_1s4_2p2 = 0
BF_1s3_2p2 = 0
BF_1s5_2p2 = 0
BF_nu_1s2_2p2 = 0
BF_nu_1s4_2p2 = 0
BF_nu_1s3_2p2 = 0
BF_nu_1s5_2p2 = 0

BF_1s2_2p3 = 0
BF_1s4_2p3 = 0
BF_1s5_2p3 = 0
BF_nu_1s2_2p3 = 0
BF_nu_1s4_2p3 = 0
BF_nu_1s5_2p3 = 0

BF_1s2_2p4 = 0
BF_1s4_2p4 = 0
BF_1s3_2p4 = 0
BF_1s5_2p4 = 0
BF_nu_1s2_2p4 = 0
BF_nu_1s4_2p4 = 0
BF_nu_1s3_2p4 = 0
BF_nu_1s5_2p4 = 0

BF_1s2_2p5 = 0
BF_1s4_2p5 = 0
BF_nu_1s2_2p5 = 0
BF_nu_1s4_2p5 = 0

BF_1s2_2p6 = 0
BF_1s4_2p6 = 0
BF_1s5_2p6 = 0
BF_nu_1s2_2p6 = 0
BF_nu_1s4_2p6 = 0
BF_nu_1s5_2p6 = 0

BF_1s2_2p7 = 0
BF_1s4_2p7 = 0
BF_1s3_2p7 = 0
BF_1s5_2p7 = 0
BF_nu_1s2_2p7 = 0
BF_nu_1s4_2p7 = 0
BF_nu_1s3_2p7 = 0
BF_nu_1s5_2p7 = 0

BF_1s2_2p8 = 0
BF_1s4_2p8 = 0
BF_1s5_2p8 = 0
BF_nu_1s2_2p8 = 0
BF_nu_1s4_2p8 = 0
BF_nu_1s5_2p8 = 0

BF_1s5_2p9 = 0
BF_nu_1s5_2p9 = 0

BF_1s2_2p10 = 0
BF_1s4_2p10 = 0
BF_1s3_2p10 = 0
BF_1s5_2p10 = 0
BF_nu_1s2_2p10 = 0
BF_nu_1s4_2p10 = 0
BF_nu_1s3_2p10 = 0
BF_nu_1s5_2p10 = 0

###############################################################################
#################### Branching fraction Calculation data ######################
###############################################################################
for k, n in enumerate(density_range):
    BF[k,0] = n
    for i, ed in enumerate(emis_data):
        a[i] = (ed[0]*0.000000001)*(ed[0]*0.000000001)*(ed[0]*0.000000001) / 8 / np.sqrt(sc.pi)*np.sqrt(sc.pi)*np.sqrt(sc.pi) * ed[4] / ed[3] * ed[7] * np.sqrt(sc.proton_mass * 3.9948e+1 / (2.0 * sc.Boltzmann * Tg))
        if ed[2] == b'2p1':
            BF_deno_2p1 = BF_deno_2p1 + EF(a[i],n,optical_l) * ed[7]
            #print(EF(a[i],n,optical_l))
            if ed[1] == b'1s2':
                BF_nu_1s2_2p1 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s4':
                BF_nu_1s4_2p1 = EF(a[i],n,optical_l) * ed[7]
            BF[k,1] = BF_nu_1s2_2p1 / BF_deno_2p1
            BF[k,2] = BF_nu_1s4_2p1 / BF_deno_2p1
            BF_1s2_2p1 = BF_nu_1s2_2p1 / BF_deno_2p1
            BF_1s4_2p1 = BF_nu_1s4_2p1 / BF_deno_2p1
            
        elif ed[2] == b'2p2':
            BF_deno_2p2 = BF_deno_2p2 + EF(a[i],n,optical_l) * ed[7]
            if ed[1] == b'1s2':
                BF_nu_1s2_2p2 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s4':
                BF_nu_1s4_2p2 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s3':
                BF_nu_1s3_2p2 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s5':
                BF_nu_1s5_2p2 = EF(a[i],n,optical_l) * ed[7]
            BF[k,3] = BF_nu_1s2_2p2 / BF_deno_2p2
            BF[k,4] = BF_nu_1s4_2p2 / BF_deno_2p2
            BF[k,5] = BF_nu_1s3_2p2 / BF_deno_2p2
            BF[k,6] = BF_nu_1s5_2p2 / BF_deno_2p2
            BF_1s2_2p2 = BF_nu_1s2_2p2 / BF_deno_2p2
            BF_1s4_2p2 = BF_nu_1s4_2p2 / BF_deno_2p2
            BF_1s3_2p2 = BF_nu_1s3_2p2 / BF_deno_2p2
            BF_1s5_2p2 = BF_nu_1s5_2p2 / BF_deno_2p2
            
        elif ed[2] == b'2p3':
            BF_deno_2p3 = BF_deno_2p3 + EF(a[i],n,optical_l) * ed[7]
            if ed[1] == b'1s2':
                BF_nu_1s2_2p3 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s4':
                BF_nu_1s4_2p3 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s5':
                BF_nu_1s5_2p3 = EF(a[i],n,optical_l) * ed[7]
            BF[k,7] = BF_nu_1s2_2p3 / BF_deno_2p3
            BF[k,8] = BF_nu_1s4_2p3 / BF_deno_2p3
            BF[k,9] = BF_nu_1s5_2p3 / BF_deno_2p3
            BF_1s2_2p3 = BF_nu_1s2_2p3 / BF_deno_2p3
            BF_1s4_2p3 = BF_nu_1s4_2p3 / BF_deno_2p3
            BF_1s5_2p3 = BF_nu_1s5_2p3 / BF_deno_2p3
            
        elif ed[2] == b'2p4':
            BF_deno_2p4 = BF_deno_2p4 + EF(a[i],n,optical_l) * ed[7]
            if ed[1] == b'1s2':
                BF_nu_1s2_2p4 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s4':
                BF_nu_1s4_2p4 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s3':
                BF_nu_1s3_2p4 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s5':
                BF_nu_1s5_2p4 = EF(a[i],n,optical_l) * ed[7]
            BF[k,10] = BF_nu_1s2_2p4 / BF_deno_2p4
            BF[k,11] = BF_nu_1s4_2p4 / BF_deno_2p4
            BF[k,12] = BF_nu_1s3_2p4 / BF_deno_2p4
            BF[k,13] = BF_nu_1s5_2p4 / BF_deno_2p4
            BF_1s2_2p4 = BF_nu_1s2_2p4 / BF_deno_2p4
            BF_1s4_2p4 = BF_nu_1s4_2p4 / BF_deno_2p4
            BF_1s3_2p4 = BF_nu_1s3_2p4 / BF_deno_2p4
            BF_1s5_2p4 = BF_nu_1s5_2p4 / BF_deno_2p4
            
        elif ed[2] == b'2p5':
            BF_deno_2p5 = BF_deno_2p5 + EF(a[i],n,optical_l) * ed[7]
            if ed[1] == b'1s2':
                BF_nu_1s2_2p5 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s4':
                BF_nu_1s4_2p5 = EF(a[i],n,optical_l) * ed[7]
            BF[k,14] = BF_nu_1s2_2p5 / BF_deno_2p5
            BF[k,15] = BF_nu_1s4_2p5 / BF_deno_2p5
            BF_1s2_2p4 = BF_nu_1s2_2p5 / BF_deno_2p5
            BF_1s4_2p4 = BF_nu_1s4_2p5 / BF_deno_2p5
            
        elif ed[2] == b'2p6':
            BF_deno_2p6 = BF_deno_2p6 + EF(a[i],n,optical_l) * ed[7]
            if ed[1] == b'1s2':
                BF_nu_1s2_2p6 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s4':
                BF_nu_1s4_2p6 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s5':
                BF_nu_1s5_2p6 = EF(a[i],n,optical_l) * ed[7]
            BF[k,16] = BF_nu_1s2_2p6 / BF_deno_2p6
            BF[k,17] = BF_nu_1s4_2p6 / BF_deno_2p6
            BF[k,18] = BF_nu_1s5_2p6 / BF_deno_2p6
            BF_1s2_2p6 = BF_nu_1s2_2p6 / BF_deno_2p6
            BF_1s4_2p6 = BF_nu_1s4_2p6 / BF_deno_2p6
            BF_1s5_2p6 = BF_nu_1s5_2p6 / BF_deno_2p6
            
        elif ed[2] == b'2p7':
            BF_deno_2p7 = BF_deno_2p7 + EF(a[i],n,optical_l) * ed[7]  
            if ed[1] == b'1s2':
                BF_nu_1s2_2p7 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s4':
                BF_nu_1s4_2p7 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s3':
                BF_nu_1s3_2p7 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s5':
                BF_nu_1s5_2p7 = EF(a[i],n,optical_l) * ed[7]
            BF[k,19] = BF_nu_1s2_2p7 / BF_deno_2p7
            BF[k,20] = BF_nu_1s4_2p7 / BF_deno_2p7
            BF[k,21] = BF_nu_1s3_2p7 / BF_deno_2p7
            BF[k,22] = BF_nu_1s5_2p7 / BF_deno_2p7
            BF_1s2_2p7 = BF_nu_1s2_2p7 / BF_deno_2p7
            BF_1s4_2p7 = BF_nu_1s4_2p7 / BF_deno_2p7
            BF_1s3_2p7 = BF_nu_1s3_2p7 / BF_deno_2p7
            BF_1s5_2p7 = BF_nu_1s5_2p7 / BF_deno_2p7
            
        elif ed[2] == b'2p8':
            BF_deno_2p8 = BF_deno_2p8 + EF(a[i],n,optical_l) * ed[7]
            if ed[1] == b'1s2':
                BF_nu_1s2_2p8 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s4':
                BF_nu_1s4_2p8 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s5':
                BF_nu_1s5_2p8 = EF(a[i],n,optical_l) * ed[7]
            BF[k,23] = BF_nu_1s2_2p8 / BF_deno_2p8
            BF[k,24] = BF_nu_1s4_2p8 / BF_deno_2p8
            BF[k,25] = BF_nu_1s5_2p8 / BF_deno_2p8
            BF_1s2_2p8 = BF_nu_1s2_2p8 / BF_deno_2p8
            BF_1s4_2p8 = BF_nu_1s4_2p8 / BF_deno_2p8
            BF_1s5_2p8 = BF_nu_1s5_2p8 / BF_deno_2p8
            
        elif ed[2] == b'2p9':
            BF_deno_2p9 = BF_deno_2p9 + EF(a[i],n,optical_l) * ed[7]
            if ed[1] == b'1s5':
                BF_nu_1s5_2p9 = EF(a[i],n,optical_l) * ed[7]
            BF[k,26] = BF_nu_1s5_2p9 / BF_deno_2p9
            BF_1s2_2p8 = BF_nu_1s5_2p9 / BF_deno_2p9
            
            
        elif ed[2] == b'2p10':
            BF_deno_2p10 = BF_deno_2p10 + EF(a[i],n,optical_l) * ed[7]
            if ed[1] == b'1s2':
                BF_nu_1s2_2p10 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s4':
                BF_nu_1s4_2p10 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s3':
                BF_nu_1s3_2p10 = EF(a[i],n,optical_l) * ed[7]
            elif ed[1] == b'1s5':
                BF_nu_1s5_2p10 = EF(a[i],n,optical_l) * ed[7]
            BF[k,27] = BF_nu_1s2_2p10 / BF_deno_2p10
            BF[k,28] = BF_nu_1s4_2p10 / BF_deno_2p10
            BF[k,29] = BF_nu_1s3_2p10 / BF_deno_2p10
            BF[k,30] = BF_nu_1s5_2p10 / BF_deno_2p10
            BF_1s2_2p10 = BF_nu_1s2_2p10 / BF_deno_2p10
            BF_1s4_2p10 = BF_nu_1s4_2p10 / BF_deno_2p10
            BF_1s3_2p10 = BF_nu_1s3_2p10 / BF_deno_2p10
            BF_1s5_2p10 = BF_nu_1s5_2p10 / BF_deno_2p10

    new_file.write(f'{n} \t {BF_1s2_2p1} \t {BF_1s4_2p1} \t {BF_1s2_2p2} \t {BF_1s4_2p2} \t {BF_1s3_2p2} \t {BF_1s5_2p2} \t {BF_1s2_2p3} \t {BF_1s4_2p3} \t {BF_1s5_2p3} \t {BF_1s2_2p4} \t {BF_1s4_2p4} \t {BF_1s5_2p4} \t {BF_1s2_2p6} \t {BF_1s4_2p6} \t {BF_1s5_2p6} \t {BF_1s4_2p7} \t {BF_1s3_2p7} \t {BF_1s2_2p8} \t {BF_1s4_2p8} \t {BF_1s5_2p8} \t {BF_1s4_2p10} \t {BF_1s5_2p10} \n')

######### Initialization ###########
    BF_deno_2p1 = 0
    BF_deno_2p2 = 0
    BF_deno_2p3 = 0
    BF_deno_2p4 = 0
    BF_deno_2p5 = 0
    BF_deno_2p6 = 0
    BF_deno_2p7 = 0
    BF_deno_2p8 = 0
    BF_deno_2p9 = 0
    BF_deno_2p10 = 0
    
    BF_1s2_2p1 = 0
    BF_1s4_2p1 = 0
    BF_nu_1s2_2p1 = 0
    BF_nu_1s4_2p1 = 0
    
    BF_1s2_2p2 = 0
    BF_1s4_2p2 = 0
    BF_1s3_2p2 = 0
    BF_1s5_2p2 = 0
    BF_nu_1s2_2p2 = 0
    BF_nu_1s4_2p2 = 0
    BF_nu_1s3_2p2 = 0
    BF_nu_1s5_2p2 = 0
    
    BF_1s2_2p3 = 0
    BF_1s4_2p3 = 0
    BF_1s5_2p3 = 0
    BF_nu_1s2_2p3 = 0
    BF_nu_1s4_2p3 = 0
    BF_nu_1s5_2p3 = 0
    
    BF_1s2_2p4 = 0
    BF_1s4_2p4 = 0
    BF_1s3_2p4 = 0
    BF_1s5_2p4 = 0
    BF_nu_1s2_2p4 = 0
    BF_nu_1s4_2p4 = 0
    BF_nu_1s3_2p4 = 0
    BF_nu_1s5_2p4 = 0
    
    BF_1s2_2p5 = 0
    BF_1s4_2p5 = 0
    BF_nu_1s2_2p5 = 0
    BF_nu_1s4_2p5 = 0
    
    BF_1s2_2p6 = 0
    BF_1s4_2p6 = 0
    BF_1s5_2p6 = 0
    BF_nu_1s2_2p6 = 0
    BF_nu_1s4_2p6 = 0
    BF_nu_1s5_2p6 = 0
    
    BF_1s2_2p7 = 0
    BF_1s4_2p7 = 0
    BF_1s3_2p7 = 0
    BF_1s5_2p7 = 0
    BF_nu_1s2_2p7 = 0
    BF_nu_1s4_2p7 = 0
    BF_nu_1s3_2p7 = 0
    BF_nu_1s5_2p7 = 0
    
    BF_1s2_2p8 = 0
    BF_1s4_2p8 = 0
    BF_1s5_2p8 = 0
    BF_nu_1s2_2p8 = 0
    BF_nu_1s4_2p8 = 0
    BF_nu_1s5_2p8 = 0
    
    BF_1s5_2p9 = 0
    BF_nu_1s5_2p9 = 0
    
    BF_1s2_2p10 = 0
    BF_1s4_2p10 = 0
    BF_1s3_2p10 = 0
    BF_1s5_2p10 = 0
    BF_nu_1s2_2p10 = 0
    BF_nu_1s4_2p10 = 0
    BF_nu_1s3_2p10 = 0
    BF_nu_1s5_2p10 = 0
    
new_file.close()

###############################################################################
######################## Experimental data ####################################
###############################################################################

# Loading OES data files
# root = Tk()
file_path = filedialog.askdirectory(initialdir="C:\\Users\\jmsong\\Documents\\00_NFRI\\00_연구관리\\00_실험데이터\\01_OES", title="Select OES data Folder")
file_list = os.listdir(file_path)
new_file_list = []
file_list.sort()

# Defining new directory for new output file
new_file_path = file_path + '/new_output'

# Making new folder in directory
if not os.path.exists(new_file_path):
    os.mkdir(new_file_path)
# Making files for density values depending on the experiment condition
new_file_name_density = file_path[67:] + '_density'
new_file_density = open(new_file_path + "/" + new_file_name_density + ".dat",'w')
new_file_density.write(f'Pressure(mT) \t Power(W) \t Material \t 1s2 \t 1s4 \t 1s3 \t 1s5 \t LR_811/750 \n')

OES_data = "C:/Users/jmsong/Documents/00_NFRI/00_연구관리/00_실험데이터/01_OES/200113_HR4000_WL.txt"
OES_peak = np.loadtxt(OES_data, dtype={'names':('WL', 'lstat','ustat','peak'),'formats':('f4','S3','S4','f4')})

# Loading Calibration coefficient file
calibration_coeff_file = "C:/Users/jmsong/Documents/00_NFRI/00_연구관리/00_실험데이터/01_OES/200113_HR4000_cal.txt"
with open(calibration_coeff_file) as data_cal:
    lines_cal = data_cal.readlines()
    cal_lines_array = np.array(lines_cal[0:])

# Loading OES files and finding peak intensity
for t,k in enumerate(file_list):
    if k == 'new_output':
        continue
    with open(file_path + "/"+ k) as data:
        lines = data.readlines()
        lines_array = np.array(lines[14:-1])     # reading each line with string type with list format
        new_lines_array = np.zeros((len(lines_array),4),dtype = float)      # making new array with [n,2] matrix form for saving with floating type
        data.close()
    pressure = k[9:11]
    power = k[14:17]
    material = k[19:24]
    
    # Making new data file
    update_file = k + "_cal"
    new_file_data = open(new_file_path + "/" + update_file + ".dat",'w')
    new_file_data.write(f'Wavelength(nm) \t Original intensity \t Calibrated intensity \n')

    # Making and opening new output file (ph=peak height)
    ph_file_name = "ph_intensity_" + k
    intensity_file = open(file_path + "/new_output/" + ph_file_name,'w')
    intensity_file.write(f'Wavelength(nm) \t Intensity \n')
                
    for l, new_line in enumerate(lines_array):
        nnew_line = new_line.split('\t')  # Splitting with tap
        new_lines_array[l,0] = nnew_line[0]     # Wavelength
        new_lines_array[l,1] = nnew_line[1]     # raw intensity
        new_lines_array[l,2] = new_lines_array[l,1] * float(cal_lines_array[l].split('\t')[1])     # Multiplying calibration coefficient

        # For writing files
        temp_1 = new_lines_array[l,0]
        temp_2 = new_lines_array[l,1]
        temp_3 = new_lines_array[l,2]
        new_file_data.write(f'{temp_1} \t {temp_2} \t {temp_3} \n')
    new_file_data.close()
    
####### Finding intensity #########
    I750 = 0
    I811 = 0
    IR811_750 = 0
    for i,ii in enumerate(OES_peak):
        WL = round(float(ii[0]),3)
        ii[3] = new_lines_array[(np.where(new_lines_array[:,0] == WL)), 2]
        intensity_file.write(f'{WL} \t {ii[3]} \n')
        if round(float(ii[0]),3) == 750.209:
            I750 = ii[3]
        elif round(float(ii[0]),3) == float(811.376):
            I811 = ii[3]
        if I750 and I811 is not 0:
            IR811_750 = I811 / I750
    intensity_file.close()
    
    n1s2 = 0
    n1s4 = 0
    n1s3 = 0
    n1s5 = 0
    
    BF_exp = np.zeros((1,31),dtype=float)
    BF_exp[0,0] = t
    
    BF_deno_2p1_exp = 0
    BF_deno_2p2_exp = 0
    BF_deno_2p3_exp = 0
    BF_deno_2p4_exp = 0
    BF_deno_2p5_exp = 0
    BF_deno_2p6_exp = 0
    BF_deno_2p7_exp = 0
    BF_deno_2p8_exp = 0
    BF_deno_2p9_exp = 0
    BF_deno_2p10_exp = 0
    
    BF_1s2_2p1_exp = 0
    BF_1s4_2p1_exp = 0
    BF_nu_1s2_2p1_exp = 0
    BF_nu_1s4_2p1_exp = 0
    
    BF_1s2_2p2_exp = 0
    BF_1s4_2p2_exp = 0
    BF_1s3_2p2_exp = 0
    BF_1s5_2p2_exp = 0
    BF_nu_1s2_2p2_exp = 0
    BF_nu_1s4_2p2_exp = 0
    BF_nu_1s3_2p2_exp = 0
    BF_nu_1s5_2p2_exp = 0
    
    BF_1s2_2p3_exp = 0
    BF_1s4_2p3_exp = 0
    BF_1s5_2p3_exp = 0
    BF_nu_1s2_2p3_exp = 0
    BF_nu_1s4_2p3_exp = 0
    BF_nu_1s5_2p3_exp = 0
    
    BF_1s2_2p4_exp = 0
    BF_1s4_2p4_exp = 0
    BF_1s3_2p4_exp = 0
    BF_1s5_2p4_exp = 0
    BF_nu_1s2_2p4_exp = 0
    BF_nu_1s4_2p4_exp = 0
    BF_nu_1s3_2p4_exp = 0
    BF_nu_1s5_2p4_exp = 0
    
    BF_1s2_2p5 = 0
    BF_1s4_2p5 = 0
    BF_nu_1s2_2p5_exp = 0
    BF_nu_1s4_2p5_exp = 0
    
    BF_1s2_2p6_exp = 0
    BF_1s4_2p6_exp = 0
    BF_1s5_2p6_exp = 0
    BF_nu_1s2_2p6_exp = 0
    BF_nu_1s4_2p6_exp = 0
    BF_nu_1s5_2p6_exp = 0
    
    BF_1s2_2p7_exp = 0
    BF_1s4_2p7_exp = 0
    BF_1s3_2p7_exp = 0
    BF_1s5_2p7_exp = 0
    BF_nu_1s2_2p7_exp = 0
    BF_nu_1s4_2p7_exp = 0
    BF_nu_1s3_2p7_exp = 0
    BF_nu_1s5_2p7_exp = 0
    
    BF_1s2_2p8_exp = 0
    BF_1s4_2p8_exp = 0
    BF_1s5_2p8_exp = 0
    BF_nu_1s2_2p8_exp = 0
    BF_nu_1s4_2p8_exp = 0
    BF_nu_1s5_2p8_exp = 0
    
    BF_1s5_2p9 = 0
    BF_nu_1s5_2p9_exp = 0
    
    BF_1s2_2p10_exp = 0
    BF_1s4_2p10_exp = 0
    BF_1s3_2p10_exp = 0
    BF_1s5_2p10_exp = 0
    BF_nu_1s2_2p10_exp = 0
    BF_nu_1s4_2p10_exp = 0
    BF_nu_1s3_2p10_exp = 0
    BF_nu_1s5_2p10_exp = 0
    
    for i, pd in enumerate(OES_peak):
        if pd[2] == b'2p1':
            BF_deno_2p1_exp = BF_deno_2p1_exp + pd[3]
            if pd[1] == b'1s2':
                BF_nu_1s2_2p1_exp = pd[3]
            elif pd[1] == b'1s4':
                BF_nu_1s4_2p1_exp = pd[3]
            BF_exp[0,1] = BF_nu_1s2_2p1_exp / BF_deno_2p1_exp
            BF_exp[0,2] = BF_nu_1s4_2p1_exp / BF_deno_2p1_exp
            BF_1s2_2p1_exp = BF_nu_1s2_2p1_exp / BF_deno_2p1_exp
            BF_1s4_2p1_exp = BF_nu_1s4_2p1_exp / BF_deno_2p1_exp
            
        elif pd[2] == b'2p2':
            BF_deno_2p2_exp = BF_deno_2p2_exp + pd[3]
            if pd[1] == b'1s2':
                BF_nu_1s2_2p2_exp = pd[3]
            elif pd[1] == b'1s4':
                BF_nu_1s4_2p2_exp = pd[3]
            elif pd[1] == b'1s3':
                BF_nu_1s3_2p2_exp = pd[3]
            elif pd[1] == b'1s5':
                BF_nu_1s5_2p2_exp = pd[3]
            BF_exp[0,3] = BF_nu_1s2_2p2_exp / BF_deno_2p2_exp
            BF_exp[0,4] = BF_nu_1s4_2p2_exp / BF_deno_2p2_exp
            BF_exp[0,5] = BF_nu_1s3_2p2_exp / BF_deno_2p2_exp
            BF_exp[0,6] = BF_nu_1s5_2p2_exp / BF_deno_2p2_exp
            BF_1s2_2p2_exp = BF_nu_1s2_2p2_exp / BF_deno_2p2_exp
            BF_1s4_2p2_exp = BF_nu_1s4_2p2_exp / BF_deno_2p2_exp
            BF_1s3_2p2_exp = BF_nu_1s3_2p2_exp / BF_deno_2p2_exp
            BF_1s5_2p2_exp = BF_nu_1s5_2p2_exp / BF_deno_2p2_exp
            
        elif pd[2] == b'2p3':
            BF_deno_2p3_exp = BF_deno_2p3_exp + pd[3]
            if pd[1] == b'1s2':
                BF_nu_1s2_2p3_exp = pd[3]
            elif pd[1] == b'1s4':
                BF_nu_1s4_2p3_exp = pd[3]
            elif pd[1] == b'1s5':
                BF_nu_1s5_2p3_exp = pd[3]
            BF_exp[0,7] = BF_nu_1s2_2p3_exp / BF_deno_2p3_exp
            BF_exp[0,8] = BF_nu_1s4_2p3_exp / BF_deno_2p3_exp
            BF_exp[0,9] = BF_nu_1s5_2p3_exp / BF_deno_2p3_exp
            BF_1s2_2p3_exp = BF_nu_1s2_2p3_exp / BF_deno_2p3_exp
            BF_1s4_2p3_exp = BF_nu_1s4_2p3_exp / BF_deno_2p3_exp
            BF_1s5_2p3_exp = BF_nu_1s5_2p3_exp / BF_deno_2p3_exp
            
        elif pd[2] == b'2p4':
            BF_deno_2p4_exp = BF_deno_2p4_exp + pd[3]
            if pd[1] == b'1s2':
                BF_nu_1s2_2p4_exp = pd[3]
            elif pd[1] == b'1s4':
                BF_nu_1s4_2p4_exp = pd[3]
            elif pd[1] == b'1s3':
                BF_nu_1s3_2p4_exp = pd[3]
            elif pd[1] == b'1s5':
                BF_nu_1s5_2p4_exp = pd[3]
            BF_exp[0,10] = BF_nu_1s2_2p4_exp / BF_deno_2p4_exp
            BF_exp[0,11] = BF_nu_1s4_2p4_exp / BF_deno_2p4_exp
            BF_exp[0,12] = BF_nu_1s3_2p4_exp / BF_deno_2p4_exp
            BF_exp[0,13] = BF_nu_1s5_2p4_exp / BF_deno_2p4_exp
            BF_1s2_2p4_exp = BF_nu_1s2_2p4_exp / BF_deno_2p4_exp
            BF_1s4_2p4_exp = BF_nu_1s4_2p4_exp / BF_deno_2p4_exp
            BF_1s3_2p4_exp = BF_nu_1s3_2p4_exp / BF_deno_2p4_exp
            BF_1s5_2p4_exp = BF_nu_1s5_2p4_exp / BF_deno_2p4_exp
            
        elif pd[2] == b'2p5':
            BF_deno_2p5_exp = BF_deno_2p5_exp + pd[3]
            if pd[1] == b'1s2':
                BF_nu_1s2_2p5_exp = pd[3]
            elif pd[1] == b'1s4':
                BF_nu_1s4_2p5_exp = pd[3]
            BF_exp[0,14] = BF_nu_1s2_2p5_exp / BF_deno_2p5_exp
            BF_exp[0,15] = BF_nu_1s4_2p5_exp / BF_deno_2p5_exp
            BF_1s2_2p5_exp = BF_nu_1s2_2p5_exp / BF_deno_2p5_exp
            BF_1s4_2p5_exp = BF_nu_1s4_2p5_exp / BF_deno_2p5_exp
            
        elif pd[2] == b'2p6':
            BF_deno_2p6_exp = BF_deno_2p6_exp + pd[3]
            if pd[1] == b'1s2':
                BF_nu_1s2_2p6_exp = pd[3]
            elif pd[1] == b'1s4':
                BF_nu_1s4_2p6_exp = pd[3]
            elif pd[1] == b'1s5':
                BF_nu_1s5_2p6_exp = pd[3]
            BF_exp[0,16] = BF_nu_1s2_2p6_exp / BF_deno_2p6_exp
            BF_exp[0,17] = BF_nu_1s4_2p6_exp / BF_deno_2p6_exp
            BF_exp[0,18] = BF_nu_1s5_2p6_exp / BF_deno_2p6_exp
            BF_1s2_2p6_exp = BF_nu_1s2_2p6_exp / BF_deno_2p6_exp
            BF_1s4_2p6_exp = BF_nu_1s4_2p6_exp / BF_deno_2p6_exp
            BF_1s5_2p6_exp = BF_nu_1s5_2p6_exp / BF_deno_2p6_exp
            
        elif pd[2] == b'2p7':
            BF_deno_2p7_exp = BF_deno_2p7_exp + pd[3]
            if pd[1] == b'1s2':
                BF_nu_1s3_2p7_exp = pd[3]
            elif pd[1] == b'1s4':
                BF_nu_1s4_2p7_exp = pd[3]
            elif pd[1] == b'1s3':
                BF_nu_1s4_2p7_exp = pd[3]
            elif pd[1] == b'1s5':
                BF_nu_1s4_2p7_exp = pd[3]
            BF_exp[0,19] = BF_nu_1s2_2p7_exp / BF_deno_2p7_exp
            BF_exp[0,20] = BF_nu_1s4_2p7_exp / BF_deno_2p7_exp
            BF_exp[0,21] = BF_nu_1s3_2p7_exp / BF_deno_2p7_exp
            BF_exp[0,22] = BF_nu_1s5_2p7_exp / BF_deno_2p7_exp
            BF_1s2_2p7_exp = BF_nu_1s2_2p7_exp / BF_deno_2p7_exp
            BF_1s4_2p7_exp = BF_nu_1s4_2p7_exp / BF_deno_2p7_exp
            BF_1s3_2p7_exp = BF_nu_1s3_2p7_exp / BF_deno_2p7_exp
            BF_1s5_2p7_exp = BF_nu_1s5_2p7_exp / BF_deno_2p7_exp
            
        elif pd[2] == b'2p8':
            BF_deno_2p8_exp = BF_deno_2p8_exp + pd[3]
            if pd[1] == b'1s2':
                BF_nu_1s2_2p8_exp = pd[3]
            elif pd[1] == b'1s4':
                BF_nu_1s4_2p8_exp = pd[3]
            elif pd[1] == b'1s5':
                BF_nu_1s5_2p8_exp = pd[3]
            BF_exp[0,23] = BF_nu_1s2_2p8_exp / BF_deno_2p8_exp
            BF_exp[0,24] = BF_nu_1s4_2p8_exp / BF_deno_2p8_exp
            BF_exp[0,25] = BF_nu_1s5_2p8_exp / BF_deno_2p8_exp
            BF_1s2_2p8_exp = BF_nu_1s2_2p8_exp / BF_deno_2p8_exp
            BF_1s4_2p8_exp = BF_nu_1s4_2p8_exp / BF_deno_2p8_exp
            BF_1s5_2p8_exp = BF_nu_1s5_2p8_exp / BF_deno_2p8_exp
            
        elif pd[2] == b'2p9':
            BF_deno_2p9_exp = BF_deno_2p9_exp + pd[3]
            if pd[1] == b'1s5':
                BF_nu_1s5_2p9_exp = pd[3]
            BF_exp[0,26] = BF_nu_1s5_2p9_exp / BF_deno_2p9_exp
            BF_1s5_2p9_exp = BF_nu_1s5_2p9_exp / BF_deno_2p9_exp
            
        elif pd[2] == b'2p10':
            BF_deno_2p10_exp = BF_deno_2p10_exp + pd[3]
            if pd[1] == b'1s2':
                BF_nu_1s2_2p10_exp = pd[3]
            elif pd[1] == b'1s4':
                BF_nu_1s4_2p10_exp = pd[3]
            elif pd[1] == b'1s3':
                BF_nu_1s3_2p10_exp = pd[3]
            elif pd[1] == b'1s5':
                BF_nu_1s5_2p10_exp = pd[3]
            BF_exp[0,27] = BF_nu_1s2_2p10_exp / BF_deno_2p10_exp
            BF_exp[0,28] = BF_nu_1s4_2p10_exp / BF_deno_2p10_exp
            BF_exp[0,29] = BF_nu_1s3_2p10_exp / BF_deno_2p10_exp
            BF_exp[0,30] = BF_nu_1s5_2p10_exp / BF_deno_2p10_exp
            BF_1s2_2p10_exp = BF_nu_1s2_2p10_exp / BF_deno_2p10_exp
            BF_1s4_2p10_exp = BF_nu_1s4_2p10_exp / BF_deno_2p10_exp
            BF_1s3_2p10_exp = BF_nu_1s3_2p10_exp / BF_deno_2p10_exp
            BF_1s5_2p10_exp = BF_nu_1s5_2p10_exp / BF_deno_2p10_exp
            
    # Chi-2 Calculation
    #### !!! Confirming BF[0,2] inclusinon
    Chi2 = np.zeros((nn,5))
    for j, sBF in enumerate(BF):
        Chi2[j,0] = sBF[0]  # density
        #1s2
        Chi2[j,1] = ((sBF[1] - BF_exp[0,1])*(sBF[1] - BF_exp[0,1]) + (sBF[3] - BF_exp[0,3])*(sBF[3] - BF_exp[0,3]) + (sBF[7] - BF_exp[0,7])*(sBF[7] - BF_exp[0,7])
               + (sBF[10] - BF_exp[0,10])*(sBF[10] - BF_exp[0,10]) + (sBF[14] - BF_exp[0,14])*(sBF[14] - BF_exp[0,14]) + (sBF[16] - BF_exp[0,16])*(sBF[16] - BF_exp[0,16])
               + (sBF[19] - BF_exp[0,19])*(sBF[19] - BF_exp[0,19]) + (sBF[23] - BF_exp[0,23])*(sBF[23] - BF_exp[0,23]) + (sBF[27] - BF_exp[0,27])*(sBF[27] - BF_exp[0,27]))
        #1s4
        Chi2[j,2] = ((sBF[2] - BF_exp[0,2])*(sBF[2] - BF_exp[0,2]) + (sBF[4] - BF_exp[0,4])*(sBF[4] - BF_exp[0,4]) + (sBF[8] - BF_exp[0,8])*(sBF[8] - BF_exp[0,8])
               + (sBF[11] - BF_exp[0,11])*(sBF[11] - BF_exp[0,11]) + (sBF[15] - BF_exp[0,15])*(sBF[15] - BF_exp[0,15]) + (sBF[17] - BF_exp[0,17])*(sBF[17] - BF_exp[0,17])
               + (sBF[20] - BF_exp[0,20])*(sBF[20] - BF_exp[0,20]) + (sBF[24] - BF_exp[0,24])*(sBF[24] - BF_exp[0,24]) + (sBF[28] - BF_exp[0,28])*(sBF[28] - BF_exp[0,28]))
        #1s3
        Chi2[j,3] = ((sBF[5] - BF_exp[0,5])*(sBF[5] - BF_exp[0,5]) + (sBF[12] - BF_exp[0,12])*(sBF[12] - BF_exp[0,12]) + (sBF[21] - BF_exp[0,21])*(sBF[21] - BF_exp[0,21])
               + (sBF[29] - BF_exp[0,29])*(sBF[29] - BF_exp[0,29]))
        #1s5
        Chi2[j,4] = ((sBF[6] - BF_exp[0,6])*(sBF[6] - BF_exp[0,6]) + (sBF[9] - BF_exp[0,9])*(sBF[9] - BF_exp[0,9]) + (sBF[13] - BF_exp[0,13])*(sBF[13] - BF_exp[0,13])
               + (sBF[18] - BF_exp[0,18])*(sBF[18] - BF_exp[0,18]) + (sBF[22] - BF_exp[0,22])*(sBF[22] - BF_exp[0,22]) + (sBF[25] - BF_exp[0,25])*(sBF[25] - BF_exp[0,25])
               + (sBF[26] - BF_exp[0,26])*(sBF[26] - BF_exp[0,26]) + (sBF[30] - BF_exp[0,30])*(sBF[30] - BF_exp[0,30]))
    
    n1s2 = Chi2[np.argmin(Chi2[:,1]), 0]
    n1s4 = Chi2[np.argmin(Chi2[:,2]), 0]
    n1s3 = Chi2[np.argmin(Chi2[:,3]), 0]
    n1s5 = Chi2[np.argmin(Chi2[:,4]), 0]
    new_file_density.write(f'{pressure} \t {power} \t {material} \t {n1s2} \t {n1s4} \t {n1s3} \t {n1s5} \t {IR811_750} \n')
new_file_density.close()