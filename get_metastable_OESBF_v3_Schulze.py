# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 16:37:38 2020

@author: jmsong

v1: Creating code for calculating branching fraction of theoritical and experiment
v2: Adding function for finding peak height from OES data
v3: Changing method to M.Schulze's method
"""
from tkinter import filedialog
import os
import numpy as np
import pandas as pd
import scipy.constants as sc
from scipy.special import comb
from itertools import combinations

    
# Function: Escape factor calculation
def EF(a,n,l):
    return (2-np.exp(-1*(a*n)*l/1000))/(1+(a*n*l))

Tg = float(300.0) #Gas temperature        
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
new_file_name_density = file_path[69:] + '_density'
new_file_density = open(new_file_path + "/" + new_file_name_density + ".dat",'w')
new_file_density.write(f'Pressure(mT) \t Power(W) \t Material \t 1s2 \t 1s4 \t 1s3 \t 1s5 \t LR_811/750 \n')

ref_OES_data = "/Users/jaemin/Documents/00_Projects/Plasma_OES_BF/test data/200113_HR4000_WL.txt"
ref_OES_peak = np.loadtxt(ref_OES_data, dtype={'names':('WL', 'lstat','ustat','peak'),'formats':('f4','S3','S4','f4')})
ref_OES_peak_pd = pd.DataFrame(ref_OES_peak)

# Loading Calibration coefficient file
calibration_coeff_file = "/Users/jaemin/Documents/00_Projects/Plasma_OES_BF/test data/200113_HR4000_cal.txt"
cal_coeff = np.loadtxt(calibration_coeff_file, dtype={'names':('WL','coeff'),'formats':('f4','f4')})
cal_coeff_pd = pd.DataFrame(cal_coeff)

# Loading OES files and finding peak intensity
for t,k in enumerate(file_list):
    if k == 'new_output':
        continue
    file_path_re = file_path + "/" + k
    file_path_out = file_path + "/new_output/" + "/" + k + "_cal.txt"
    OES_data = np.loadtxt(file_path_re, dtype={'names':('WL','I'),'formats':('f4','f4')}, skiprows = 14)
    OES_data_pd = pd.DataFrame(OES_data)
    #OES_data_pd = pd.read_csv(file_path_re,sep='\t', names = ['WL','I'], dtype = {"WL":"float", "I":"float"}, skiprows = 14, index_col = 0)
    
    pressure = k[9:11]
    power = k[14:17]
    material = k[19:24]
    
    # Making and opening new output file (ph=peak height)
    ph_file_name = "ph_intensity_" + k
    intensity_file = open(file_path + "/new_output/" + ph_file_name,'w')
    intensity_file.write(f'Wavelength(nm) \t Intensity \n')
    
    OES_data_pd['cal_I'] = OES_data_pd.I * cal_coeff_pd.coeff
    OES_data_pd.to_csv(file_path_out, sep= '\t')
####### Finding intensity #########
# Changing OES_peak value
# option: line ratio, 750/811
    np.same
    I750 = 0
    I811 = 0
    IR811_750 = 0
    for i in OES_data_pd.WL:
        if i in ref_OES_peak_pd.WL:
            ref_OES_peak_pd['exp_I'] = 
    for i,WL in enumerate(OES_peak_pd.WL):
        OES_peak_pd.peak[i] = new_lines_array[(np.where(new_lines_array[:,0] == WL)), 2]
        intensity_file.write(f'{WL} \t {ii[3]} \n')
        if round(float(ii[0]),3) == 750.209:
            I750 = ii[3]
        elif round(float(ii[0]),3) == float(811.376):
            I811 = ii[3]
        if I750 and I811 is not 0:
            IR811_750 = I811 / I750
    intensity_file.close()
    
    ed_ex_2p1 = list();ed_ex_2p2 = list();ed_ex_2p3 = list();ed_ex_2p4 = list();ed_ex_2p5 = list();
    ed_ex_2p6 = list();ed_ex_2p7 = list();ed_ex_2p8 = list();ed_ex_2p9 = list();ed_ex_2p10 = list();
    
    for ed_ex in OES_peak:
        if ed_ex[2] == b'2p1':
            ed_ex_2p1.append(ed_ex)
        if ed_ex[2] == b'2p2':
            ed_ex_2p2.append(ed_ex)
        if ed_ex[2] == b'2p3':
            ed_ex_2p3.append(ed_ex)
        if ed_ex[2] == b'2p4':
            ed_ex_2p4.append(ed_ex)
        if ed_ex[2] == b'2p5':
            ed_ex_2p5.append(ed_ex)
        if ed_ex[2] == b'2p6':
            ed_ex_2p6.append(ed_ex)
        if ed_ex[2] == b'2p7':
            ed_ex_2p7.append(ed_ex)
        if ed_ex[2] == b'2p8':
            ed_ex_2p8.append(ed_ex)
        if ed_ex[2] == b'2p9':
            ed_ex_2p9.append(ed_ex)
        if ed_ex[2] == b'2p10':
            ed_ex_2p10.append(ed_ex)
        
    ed_ex_array = []
    ed_ex_array.append(ed_2p1);ed_ex_array.append(ed_2p2);ed_ex_array.append(ed_2p3);
    ed_ex_array.append(ed_2p4);ed_ex_array.append(ed_2p5);ed_ex_array.append(ed_2p6);
    ed_ex_array.append(ed_2p7);ed_ex_array.append(ed_2p8);ed_ex_array.append(ed_2p9);
    ed_ex_array.append(ed_2p10)
                                
    ######################################################################################################
    ########################################### Calculation ##############################################
    ######################################################################################################
    ed_2p1 = list();ed_2p2 = list();ed_2p3 = list();ed_2p4 = list();ed_2p5 = list();
    ed_2p6 = list();ed_2p7 = list();ed_2p8 = list();ed_2p9 = list();ed_2p10 = list();
    emission_data = "C:/Users/jmsong/Documents/00_NFRI/00_연구관리/00_실험데이터/01_OES/200102_Ar_emission_no head_24lines.txt"
    emis_data = np.loadtxt(emission_data, dtype={'names':('WL', 'lstat','ustat','gl','gu','El','Eu','A'),'formats':('f4','S3','S4','i1','i1','f4','f4','f4')})
    a=np.zeros(len(emis_data))
    for ed in emis_data:
        if ed[2] == b'2p1':
            ed_2p1.append(ed)
        if ed[2] == b'2p2':
            ed_2p2.append(ed)
        if ed[2] == b'2p3':
            ed_2p3.append(ed)
        if ed[2] == b'2p4':
            ed_2p4.append(ed)
        if ed[2] == b'2p5':
            ed_2p5.append(ed)
        if ed[2] == b'2p6':
            ed_2p6.append(ed)
        if ed[2] == b'2p7':
            ed_2p7.append(ed)
        if ed[2] == b'2p8':
            ed_2p8.append(ed)
        if ed[2] == b'2p9':
            ed_2p9.append(ed)
        if ed[2] == b'2p10':
            ed_2p10.append(ed)
                                                                                
    ed_array = []
    ed_array.append(ed_2p1);ed_array.append(ed_2p2);ed_array.append(ed_2p3);
    ed_array.append(ed_2p4);ed_array.append(ed_2p5);ed_array.append(ed_2p6);
    ed_array.append(ed_2p7);ed_array.append(ed_2p8);ed_array.append(ed_2p9);
    ed_array.append(ed_2p10)
    
    num_case_2p1 = comb(len(ed_2p1),2)
    num_case_2p2 = comb(len(ed_2p2),2)
    num_case_2p3 = comb(len(ed_2p3),2)
    num_case_2p4 = comb(len(ed_2p4),2)
    num_case_2p5 = comb(len(ed_2p5),2)
    num_case_2p6 = comb(len(ed_2p6),2)
    num_case_2p7 = comb(len(ed_2p7),2)
    num_case_2p8 = comb(len(ed_2p8),2)
    num_case_2p9 = comb(len(ed_2p9),2)
    num_case_2p10 = comb(len(ed_2p10),2)
    
    num_total_case = (num_case_2p1 + num_case_2p2 + num_case_2p3 + num_case_2p4
                       + num_case_2p5 + num_case_2p6 + num_case_2p7 + num_case_2p8
                       + num_case_2p9 + num_case_2p10)
    ###########################################################################
    ###################### Setting metastable density range ###################
    ###########################################################################
    n_list_1s2 = (list(np.arange(1,10,0.1)*1e13) + list(np.arange(1,10,0.1)*1e14) + list(np.arange(1,10,0.1)*1e15)
                        + list(np.arange(1,10,0.1)*1e16) + list(np.arange(1,10,0.1)*1e17) + list(np.arange(1,10,0.1)*1e18))
    n_list_1s3 = (list(np.arange(1,10,0.1)*1e13) + list(np.arange(1,10,0.1)*1e14)
                    + list(np.arange(1,10,0.1)*1e15) + list(np.arange(1,10,0.1)*1e16) + list(np.arange(1,10,0.1)*1e17)
                    + list(np.arange(1,10,0.1)*1e18))
    n_list_1s4 = (list(np.arange(1,10,0.1)*1e13) + list(np.arange(1,10,0.1)*1e14)
                    + list(np.arange(1,10,0.1)*1e15) + list(np.arange(1,10,0.1)*1e16) + list(np.arange(1,10,0.1)*1e17)
                    + list(np.arange(1,10,0.1)*1e18))
    n_list_1s5 = (list(np.arange(1,10,0.1)*1e13) + list(np.arange(1,10,0.1)*1e14)
                    + list(np.arange(1,10,0.1)*1e15) + list(np.arange(1,10,0.1)*1e16) + list(np.arange(1,10,0.1)*1e17)
                    + list(np.arange(1,10,0.1)*1e18))
    
    ###########################################################################
    ########## Setting optical length #########################################
    ###########################################################################
    optical_l = 10e-3
    
    ###########################################################################
    num_n_1s2 = len(n_list_1s2)
    num_n_1s3 = len(n_list_1s3)
    num_n_1s4 = len(n_list_1s4)
    num_n_1s5 = len(n_list_1s5)
    x = []
    
    for a,n_1s2 in n_list_1s2:
        for b,n_1s3 in n_list_1s3:
            for c,n_1s4 in n_list_1s4:
                for d,n_1s5 in n_list_1s5:
                    for ed_1u in ed_array:
                        if len(ed_1u) is not 1:
                            for ed_1u_1l in ed_1u:
    
    n1s2 = Chi2[np.argmin(Chi2[:,1]), 0]
    n1s4 = Chi2[np.argmin(Chi2[:,2]), 0]
    n1s3 = Chi2[np.argmin(Chi2[:,3]), 0]
    n1s5 = Chi2[np.argmin(Chi2[:,4]), 0]
    new_file_density.write(f'{pressure} \t {power} \t {material} \t {n1s2} \t {n1s4} \t {n1s3} \t {n1s5} \t {IR811_750} \n')
new_file_density.close()