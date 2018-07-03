# -*- coding: utf-8 -*-
'''
Created on 25.04.2017

@author: 
'''

import re

import csv

import datetime

import Witness
import ArrayUtils



class CSVReader_Utils(object):
    
    @staticmethod
    def get_listCSVRows_byFile( strCSVFile_In, int_SheetIndex = None):
        '''
        this function is used to get a list of XlrdRow objects with given excel file and a given sheet index
        relations: relations_1: this class, input: strCSVFile_In, Xlrd
        relations: relations_2: this class, output: list of XlrdRow objects

        @param strCSVFile_In: the csv file
        @type strCSVFile_In: string
        @param int_SheetIndex: sheet index of the excel file
        @type int_SheetIndex: integer
        @return: list of XlrdRow objects, otherwise []
        @rtype: list of XlrdRow objects
        '''
        strLocation = Witness.WitnessSys.clsStrWitnessLocation + "get_listCSVRows_byFile: "
        list_list_Output = []
        with open(strCSVFile_In, newline='') as csvfile:
            spamreader = csv.reader(csvfile, dialect='excel', delimiter=';', quotechar='|')
            for row in spamreader:
                list_list_Output.append(row)       

        print (strLocation + Witness.WitnessSys.clsStrWitnessValues + " listOutput size: " + str(len(list_list_Output)))     
        return list_list_Output
    
    @staticmethod
    def filter_Column_ListRows( list2_Rows_In, intColumn_In, str_RegexFilter_In):
        strLocation = Witness.WitnessSys.clsStrWitnessLocation + "filter_Column_ListOpenpyxlRows: "
        listOutput = []

        for list_row in list2_Rows_In:
            if re.match(pattern = str_RegexFilter_In, string = str(list_row[intColumn_In])):
                listOutput.append(list_row)
        print (strLocation + Witness.WitnessSys.clsStrWitnessValues + " listOutput size: " + str(len(listOutput)))    
        return listOutput
    
    @staticmethod
    def get_ListStr_Column_byList2Rows( list2_OpenpyxlRows_In, intColumn_In):
        strLocation = Witness.WitnessSys.clsStrWitnessLocation + "get_ListStr_Column_byListOpenpyxlRows: "
        listOutput = []
        for row in list2_OpenpyxlRows_In:
            listOutput.append(str(row[intColumn_In]))
        return listOutput
    

    
    def f_calib_NRC(self):
        StrWitnessCurrent = Witness.WitnessSys.clsStrWitnessLocation + self.__class__.__name__+ ': f_calib_NRC: '
        if self.dict_Calib_Set == None:
            print(StrWitnessCurrent + "event: error: first run f_setCalibSet")
            raise UserWarning('CalibSet is not set')
        for listItem in self.list2_Rows_with_RowLimit:
            if set(listItem).intersection(self.dict_Calib_Set['list_NRC']):
                set_ColNames = set(listItem).intersection(self.dict_Calib_Set['list_NRC'])
                self.int_NRCTotal_Col = listItem.index(set_ColNames.pop())
                return 1
        raise UserWarning('f_calib_NRC failed')
        
    def f_calib_LT(self):
        StrWitnessCurrent = Witness.WitnessSys.clsStrWitnessLocation + self.__class__.__name__+ ': f_calib_LT: '
        if self.dict_Calib_Set == None:
            print(StrWitnessCurrent + "event: error: first run f_setCalibSet")
            raise UserWarning('CalibSet is not set')
        for listItem in self.list2_Rows_with_RowLimit:
            if set(listItem).intersection(self.dict_Calib_Set['list_LT']):
                list_ColNames = set(listItem).intersection(self.dict_Calib_Set['list_LT'])
                self.int_LT_Col = listItem.index(list_ColNames[0])
                return 1
        raise UserWarning('f_calib_LT failed')
        
    def f_calib_File(self):
        self.f_calib_Ruid()
        self.f_calib_Material()
        self.f_calib_RC()
        self.f_calib_NRC()
        #self.f_calib_LT()
        
          

class Compare_TransferData(object):
    
    def __init__(self, str_RuId_In):
        self.str_RuId = str_RuId_In
        self.list_RuIdBlock=[]
        self.list2_CompareItem=[]
        


class Xlwt_Utils(object):
    clsStr_ClassLocation = "Xlwt_Utils: "
    @staticmethod
    def writListToRow( oSheet_InOut, row_index_In, col_index_Start, list_toWrite_In):
        strLocation = Witness.WitnessSys.clsStrWitnessLocation + Xlwt_Utils.clsStr_ClassLocation + "writListToRow: "
        for col_index, IdItem in enumerate(list_toWrite_In):
            oSheet_InOut.write(row_index_In, col_index+col_index_Start, IdItem)
            col_index_output = col_index+col_index_Start
        return col_index_output
    


    
        

if __name__ == '__main__':
    strExcelFile1=r'C:\Users\xsun\Documents\BMS_Logging\2018-07-02_14-09-19_Power48-5000_0-Kopie.csv'
    list2Str_CSV = CSVReader_Utils.get_listCSVRows_byFile(strCSVFile_In=strExcelFile1.replace('\\', '/'))
    listIndex=[2, 3]
    listStrFilters=['.{0,3}SOC State.{0,3}', '.{0,3}Time.{0,3}']
    listIndex1=[0]
    listStrFilters1=['OnOffLogEvents']
    ArrayUtils.Array_Utils.get_Index_byList2Str_Regex(list2Str_In = list2Str_CSV, listIntColumns_In= listIndex, listStr_RegexFilters_In=listStrFilters)
    ArrayUtils.Array_Utils.get_Index_byList2Str_Regex(list2Str_In = list2Str_CSV, listIntColumns_In= listIndex1, listStr_RegexFilters_In=listStrFilters1)
    
    pass
#     oBB_Excel_Data = BB_Excel_Data()
#     list_tuple_list2_XlrdRows = oBB_Excel_Data.get_list_list2_XlrdRows()
#     listObj_BB_ExcelFileCalib_Data = oBB_Excel_Data.build_BB_ExcelCalib_Data(list_tuple_list2_XlrdRows_In = list_tuple_list2_XlrdRows)
#     list_RuIds = oBB_Excel_Data.get_ListStr_Ruids(list_tuple_list2_XlrdRows_In = list_tuple_list2_XlrdRows)
#     list_Obj_Compare_TransferData = oBB_Excel_Data.get_list_Obj_Compare_TransferData_ByRuids_1_1(listStr_Ruids_In = list_RuIds, listObj_BB_ExcelFileCalib_Data_In = listObj_BB_ExcelFileCalib_Data)
#     oBB_Excel_Data.save_get_list_Obj_Compare_TransferData_To_OutputDir(list_Obj_Compare_TransferData_In = list_Obj_Compare_TransferData)  

    
