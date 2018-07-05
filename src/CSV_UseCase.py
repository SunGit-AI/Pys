# -*- coding: utf-8 -*-
'''
Created on 25.04.2017

@author: 
'''

import re
import csv

import datetime

import src.Witness as Witness
import src.CSV_Tools as CSV_Tools
import src.ArrayUtils as ArrayUtils

import pandas as pd
import numpy as np
import matplotlib as plt

class BMS_Logging_CSV_V10():
    
    clsStrExcelFile1=r'C:\Users\xsun\Documents\BMS_Logging\2018-07-02_14-09-19_Power48-5000_0-Kopie.csv'
    
    clsListIndex_STDependenndTimers=[2, 3]
    clsListStrFilters_STDependenndTimers=['.{0,3}SOC State.{0,3}', '.{0,3}Time.{0,3}']
    clsListIndex_OnOffLogEvents=[0]
    clsListStrFilters_OnOffLogEvents=['OnOffLogEvents']
    
    clsListIndex_STDependenndTimers_Not0=[3]
    clsListStrFilters_STDependenndTimers_Not0=['^[1-9]\d{0,10}$']
    
    clsIntTimerColum=3
    clsIntSOCColum=2
    
    clsStrReFilter_Digits20='\d{1,20}'
    
    clsListStrs_TemperatureStates=['BelowMinus10Degrees', 'Minus10to0Degrees', 'Over0to10Degrees', '11to20Degrees', '21to30Degrees', '31to40Degrees', '41to45Degrees', '46to50Degrees', '51to55Degrees', '56to60Degrees', '61to65Degrees', '66to70Degrees', 'Over70Degrees']
    clsListInts_TemperatureStates=[-20, -10, 0,10,20,30,40,45,50,55,60,65,70]
    
    clsListStrs_Current_States_Discharge=['DischargeOver225A', 'Discharge224to175A', 'Discharge174to125A', 'Discharge124to75A', 'Discharge74to25A', 'Discharge24to1A', 'WithinPlusMinus1A']
    clsListStrs_Current_States_Discharge_Labels=['over225A', '224to175A', '174to125A', '124to75A', '74to25A', '24to1A', 'PlusMinus1A']  
    clsListStrs_Current_States_Charge=['Charge1to24A', 'Charge1to24A', 'Charge25to74A', 'Charge75to124A', 'Charge125to174A', 'Charge175to224A', 'ChargeOver225A']
    
    def filter_list2Strs_STDependenndTimersData(self, list2Str_CSVData_In, list_STDependenndTimers_1_In, list_STDependenndTimers_2_In, listStrFilters_STDependenndTimers_1_In, listStrFilters_STDependenndTimers_2_In):
        strLocation=Witness.WitnessSys.clsStrWitnessLocation + str(self.__class__) +': filter_list2Strs_STDependenndTimersData: '
        i_Index1 = ArrayUtils.Array_Utils.get_Index_byList2Str_Regex(list2Str_In = list2Str_CSVData_In, listIntColumns_In= list_STDependenndTimers_1_In, listStr_RegexFilters_In=listStrFilters_STDependenndTimers_1_In)
        i_Index2 = ArrayUtils.Array_Utils.get_Index_byList2Str_Regex(list2Str_In = list2Str_CSVData_In, listIntColumns_In= list_STDependenndTimers_2_In, listStr_RegexFilters_In=listStrFilters_STDependenndTimers_2_In)
        if i_Index1!= -1 and i_Index2!= -1 and i_Index1<i_Index2:
            list2Str_CSV_STDependenndTimers = list2Str_CSVData_In[i_Index1+1: i_Index2]
            print(strLocation + Witness.WitnessSys.clsStrWitnessValues + " output list size: " + str(len(list2Str_CSV_STDependenndTimers)))
            return list2Str_CSV_STDependenndTimers
        return []
     
    def filter_list2Strs_STDependenndTimersData_Not0(self, list2Str_CSVData_In, list_Colums_Not0_In, list_Filters_Not0_In ):
        strLocation=Witness.WitnessSys.clsStrWitnessLocation + str(self.__class__) +': filter_list2Strs_STDependenndTimersData_Not0: '    
        listOut = ArrayUtils.Array_Utils.filter_subList_byList2Str_Regex(list2Str_In = list2Str_CSVData_In, listIntColumns_In = list_Colums_Not0_In, listStr_RegexFilters_In = list_Filters_Not0_In)
        print(strLocation + Witness.WitnessSys.clsStrWitnessValues + " output list size: " + str(len(listOut)))
        return listOut
    
    def estimate_Int_TimeHisto_bySTDependenndTimersData_ColumnFilters(self, list2Str_CSVData_In, list_Colums_In, list_Filters_In, int_timeColumn_In ):
        strLocation=Witness.WitnessSys.clsStrWitnessLocation + str(self.__class__) +': estimate_Int_TimeHisto_bySTDependenndTimersData_ColumnFilters: '    
        listOut = ArrayUtils.Array_Utils.filter_subList_byList2Str_Regex(list2Str_In = list2Str_CSVData_In, listIntColumns_In = list_Colums_In, listStr_RegexFilters_In = list_Filters_In)
        listStrTimes=[row[int_timeColumn_In] for row in listOut]
        intOut = sum(list(map(int, listStrTimes)))
        print(strLocation + Witness.WitnessSys.clsStrWitnessValues + "%s time sum: %d" %(list_Filters_In[0], intOut))
        return intOut
    
    def decompose_listInts_Time_bySTDependenndTimersData_Not0(self, list2Str_CSVData_In, intTimeColume_In ):
        strLocation=Witness.WitnessSys.clsStrWitnessLocation + str(self.__class__) +': decompose_listInts_Time_bySTDependenndTimersData_Not0: '    
        listOut = []
        i_TimeCurr=0
        for list_STDependenndTimersData in list2Str_CSVData_In:
            listOut.append(i_TimeCurr)
            listOut.append(i_TimeCurr+int(list_STDependenndTimersData[intTimeColume_In]))
            i_TimeCurr+=int(list_STDependenndTimersData[intTimeColume_In])
        return listOut
    
    def decompose_listInts_SOCs_bySTDependenndTimersData_Not0(self, list2Str_CSVData_In, intSOCColume_In , str_SOC_DigitFilter_In):
        strLocation=Witness.WitnessSys.clsStrWitnessLocation + str(self.__class__) +': decompose_listInts_SOCs_bySTDependenndTimersData_Not0: '    
        listOut = []
        for list_STDependenndTimersData in list2Str_CSVData_In:
            strSOC = self.preproces_Str_SOC_Item(str_SOC_In=list_STDependenndTimersData[intSOCColume_In])
            listOut.extend(re.findall(pattern = str_SOC_DigitFilter_In, string = strSOC))
        return list(map(int, listOut))
    
    def preproces_Str_SOC_Item(self, str_SOC_In ):
        strLocation=Witness.WitnessSys.clsStrWitnessLocation + str(self.__class__) +': preproces_Str_SOC_Item: '    
        if str_SOC_In.startswith('Below'):
            return '0'+ str_SOC_In
        if str_SOC_In.startswith('Over'):
            return str_SOC_In +'100'
        return str_SOC_In
        
def build_TemperatureTime_Histogram():
    oBMS_Logging_CSV_V10=BMS_Logging_CSV_V10()
    list2Str_CSV = CSV_Tools.CSVReader_Utils.get_listCSVRows_byFile(strCSVFile_In=BMS_Logging_CSV_V10.clsStrExcelFile1.replace('\\', '/'))
    list2Str_CSV_STDependenndTimersData = oBMS_Logging_CSV_V10.filter_list2Strs_STDependenndTimersData(list2Str_CSVData_In = list2Str_CSV, 
                                                                                                         list_STDependenndTimers_1_In = BMS_Logging_CSV_V10.clsListIndex_STDependenndTimers, 
                                                                                                         list_STDependenndTimers_2_In = BMS_Logging_CSV_V10.clsListIndex_OnOffLogEvents, 
                                                                                                         listStrFilters_STDependenndTimers_1_In = BMS_Logging_CSV_V10.clsListStrFilters_STDependenndTimers, 
                                                                                                         listStrFilters_STDependenndTimers_2_In = BMS_Logging_CSV_V10.clsListStrFilters_OnOffLogEvents
                                                                                                         )
    list2Strs_STDependenndTimersData_Not0=oBMS_Logging_CSV_V10.filter_list2Strs_STDependenndTimersData_Not0(list2Str_CSVData_In = list2Str_CSV_STDependenndTimersData, list_Colums_Not0_In = BMS_Logging_CSV_V10.clsListIndex_STDependenndTimers_Not0, list_Filters_Not0_In = BMS_Logging_CSV_V10.clsListStrFilters_STDependenndTimers_Not0)
    listTimes=[]
    for strTemperatureState in BMS_Logging_CSV_V10.clsListStrs_TemperatureStates:
        intTimeSum= oBMS_Logging_CSV_V10.estimate_Int_TimeHisto_bySTDependenndTimersData_ColumnFilters(list2Str_CSVData_In = list2Strs_STDependenndTimersData_Not0, list_Colums_In=[1], list_Filters_In=[strTemperatureState], int_timeColumn_In=3)
        listTimes.append(intTimeSum)

    df = pd.DataFrame({'time in seconds':listTimes}, index=BMS_Logging_CSV_V10.clsListInts_TemperatureStates,)
    ax = df.plot.bar(rot=0, width=0.98, align='edge', edgecolor = 'tab:green', linewidth=1 )
    ax.set_xlabel('temperature state') 
    plt.pyplot.show() 
    
def build_DischargeTime_Histogram():
    oBMS_Logging_CSV_V10=BMS_Logging_CSV_V10()
    list2Str_CSV = CSV_Tools.CSVReader_Utils.get_listCSVRows_byFile(strCSVFile_In=BMS_Logging_CSV_V10.clsStrExcelFile1.replace('\\', '/'))
    list2Str_CSV_STDependenndTimersData = oBMS_Logging_CSV_V10.filter_list2Strs_STDependenndTimersData(list2Str_CSVData_In = list2Str_CSV, 
                                                                                                         list_STDependenndTimers_1_In = BMS_Logging_CSV_V10.clsListIndex_STDependenndTimers, 
                                                                                                         list_STDependenndTimers_2_In = BMS_Logging_CSV_V10.clsListIndex_OnOffLogEvents, 
                                                                                                         listStrFilters_STDependenndTimers_1_In = BMS_Logging_CSV_V10.clsListStrFilters_STDependenndTimers, 
                                                                                                         listStrFilters_STDependenndTimers_2_In = BMS_Logging_CSV_V10.clsListStrFilters_OnOffLogEvents
                                                                                                         )
    list2Strs_STDependenndTimersData_Not0=oBMS_Logging_CSV_V10.filter_list2Strs_STDependenndTimersData_Not0(list2Str_CSVData_In = list2Str_CSV_STDependenndTimersData, list_Colums_Not0_In = BMS_Logging_CSV_V10.clsListIndex_STDependenndTimers_Not0, list_Filters_Not0_In = BMS_Logging_CSV_V10.clsListStrFilters_STDependenndTimers_Not0)
    print([row[BMS_Logging_CSV_V10.clsIntTimerColum] for row in list2Strs_STDependenndTimersData_Not0])
    listTimes=[]
    for strSearchItem in BMS_Logging_CSV_V10.clsListStrs_Current_States_Discharge:
        intTimeSum= oBMS_Logging_CSV_V10.estimate_Int_TimeHisto_bySTDependenndTimersData_ColumnFilters(list2Str_CSVData_In = list2Strs_STDependenndTimersData_Not0, list_Colums_In=[0], list_Filters_In=[strSearchItem], int_timeColumn_In=3)
        listTimes.append(intTimeSum)

    df = pd.DataFrame({'time in seconds':listTimes}, index=BMS_Logging_CSV_V10.clsListStrs_Current_States_Discharge_Labels,)
    ax = df.plot.bar(rot=0, width=0.98, edgecolor = 'tab:green', linewidth=1 )# align='edge'
    ax.set_xlabel('discharge state') 
    plt.pyplot.show() 

if __name__ == '__main__':
    build_DischargeTime_Histogram()
