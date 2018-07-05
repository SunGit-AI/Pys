# -*- coding: utf-8 -*-
'''
Created on 25.04.2017

@author: 
'''

import re


import src.Witness 
from numpy.core.tests.test_mem_overlap import xrange



class Array_Utils(object):
    
    @staticmethod
    def get_Index_byList2Str_Regex(list2Str_In, listIntColumns_In, listStr_RegexFilters_In):
        
        strLocation = Witness.WitnessSys.clsStrWitnessLocation + "get_Index_byList2Str_Regex: "
        
        for list_Index_1 in xrange(0, len(list2Str_In)):
            listRes = []
            for int_Index_t in xrange(0, len(listIntColumns_In)):
                if len(list2Str_In[list_Index_1])>listIntColumns_In[int_Index_t]:
                    listRes.append(re.match(pattern = listStr_RegexFilters_In[int_Index_t], string = list2Str_In[list_Index_1][listIntColumns_In[int_Index_t]]))
            if len(listRes) and all(listRes):
                #print (strLocation + Witness.WitnessSys.clsStrWitnessValues + " found list at list index: " + str(list_Index_1))   
                return list_Index_1
        return -1

    @staticmethod
    def filter_subList_byList2Str_Regex(list2Str_In, listIntColumns_In, listStr_RegexFilters_In):
        
        strLocation = Witness.WitnessSys.clsStrWitnessLocation + "filter_subList_byList2Str_Regex: "
        listOutput=[]
        for list_Index_1 in xrange(0, len(list2Str_In)):
            listRes = []
            for int_Index_t in xrange(0, len(listIntColumns_In)):
                if len(list2Str_In[list_Index_1])>listIntColumns_In[int_Index_t]:
                    listRes.append(re.match(pattern = listStr_RegexFilters_In[int_Index_t], string = list2Str_In[list_Index_1][listIntColumns_In[int_Index_t]]))
            if len(listRes) and all(listRes):
                #print (strLocation + Witness.WitnessSys.clsStrWitnessValues + " found list at list index: " + str(list_Index_1))   
                listOutput.append(list2Str_In[list_Index_1])
        return listOutput


    
        

if __name__ == '__main__':

    strT1 = ' SOC State'
    pass
#     oBB_Excel_Data = BB_Excel_Data()
#     list_tuple_list2_XlrdRows = oBB_Excel_Data.get_list_list2_XlrdRows()
#     listObj_BB_ExcelFileCalib_Data = oBB_Excel_Data.build_BB_ExcelCalib_Data(list_tuple_list2_XlrdRows_In = list_tuple_list2_XlrdRows)
#     list_RuIds = oBB_Excel_Data.get_ListStr_Ruids(list_tuple_list2_XlrdRows_In = list_tuple_list2_XlrdRows)
#     list_Obj_Compare_TransferData = oBB_Excel_Data.get_list_Obj_Compare_TransferData_ByRuids_1_1(listStr_Ruids_In = list_RuIds, listObj_BB_ExcelFileCalib_Data_In = listObj_BB_ExcelFileCalib_Data)
#     oBB_Excel_Data.save_get_list_Obj_Compare_TransferData_To_OutputDir(list_Obj_Compare_TransferData_In = list_Obj_Compare_TransferData)  

    
