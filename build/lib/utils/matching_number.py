"""
matching_number.py 


function that given a list of char numbers detected in a 
signle frame compare , returns the best possible registration number
and serie number 
 
Input:
        list of strings contains numeric chars

Returns:
            regist_num_detection    (bool):
            serie_num_detection     (bool):
            possible_serie_num      (int) : 
            possible_regist_num     (int) : 
    
Note:
        Default return is False, False , 0 , 0
     
©cil4sys
"""
def matching_number(plate_list):
    regist_num_detection    =False
    serie_num_detection     =False
    possible_regist_num     =0000
    possible_serie_num      =00
    if   len(plate_list) != 0  :
        #list is not empty
        reg_list=[]
        serie_list=[]
        for item in plate_list:
            if item !='':
                reg_list.append(int(item[:3]))
                serie_list.append(int(item[-4:]))
        # if a reg number or serie number 
        # is present twice it will raise detection flag 
        for serie in serie_list :
            serie_occ=serie_list.count(serie)
            if serie_occ >1 :
                serie_num_detection=True
                possible_serie_num=serie
        for reg in reg_list :
            reg_occ=reg_list.count(reg)
            if reg_occ >1 :
                regist_num_detection=True
                possible_regist_num=reg
       
        
    return serie_num_detection,regist_num_detection,possible_serie_num,possible_regist_num

 