'''
Created on 15.07.2016

@author: wtmuc-0021-User
'''
import re
from collections import OrderedDict

class Test1():
    clsListStr1 = ['DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'DischargeOver225A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge224to175A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge174to125A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge124to75A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge74to25A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'Discharge24to1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'WithinPlusMinus1A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge1to24A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge25to74A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge75to124A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge125to174A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'Charge175to224A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A', 
'ChargeOver225A']
    
    clsListStr2= ['BelowMinus10Degrees', 
'Minus10to0Degrees', 
'Minus10to0Degrees', 
'Minus10to0Degrees', 
'Minus10to0Degrees', 
'Minus10to0Degrees', 
'Minus10to0Degrees', 
'Minus10to0Degrees', 
'Minus10to0Degrees', 
'Over0to10Degrees', 
'Over0to10Degrees', 
'Over0to10Degrees', 
'Over0to10Degrees', 
'Over0to10Degrees', 
'Over0to10Degrees', 
'Over0to10Degrees', 
'Over0to10Degrees', 
'11to20Degrees', 
'11to20Degrees', 
'11to20Degrees', 
'11to20Degrees', 
'11to20Degrees', 
'11to20Degrees', 
'11to20Degrees', 
'11to20Degrees', 
'21to30Degrees', 
'21to30Degrees', 
'21to30Degrees', 
'21to30Degrees', 
'21to30Degrees', 
'21to30Degrees', 
'21to30Degrees', 
'21to30Degrees', 
'31to40Degrees', 
'31to40Degrees', 
'31to40Degrees', 
'31to40Degrees', 
'31to40Degrees', 
'31to40Degrees', 
'31to40Degrees', 
'31to40Degrees', 
'41to45Degrees', 
'41to45Degrees', 
'41to45Degrees', 
'41to45Degrees', 
'41to45Degrees', 
'41to45Degrees', 
'41to45Degrees', 
'41to45Degrees', 
'46to50Degrees', 
'46to50Degrees', 
'46to50Degrees', 
'46to50Degrees', 
'46to50Degrees', 
'46to50Degrees', 
'46to50Degrees', 
'46to50Degrees', 
'51to55Degrees', 
'51to55Degrees', 
'51to55Degrees', 
'51to55Degrees', 
'51to55Degrees', 
'51to55Degrees', 
'51to55Degrees', 
'51to55Degrees', 
'56to60Degrees', 
'56to60Degrees', 
'56to60Degrees', 
'56to60Degrees', 
'56to60Degrees', 
'56to60Degrees', 
'56to60Degrees', 
'56to60Degrees', 
'61to65Degrees', 
'61to65Degrees', 
'61to65Degrees', 
'61to65Degrees', 
'61to65Degrees', 
'61to65Degrees', 
'61to65Degrees', 
'61to65Degrees', 
'66to70Degrees', 
'66to70Degrees', 
'66to70Degrees', 
'66to70Degrees', 
'66to70Degrees', 
'66to70Degrees', 
'66to70Degrees', 
'66to70Degrees', 
'Over70Degrees', 
'Over70Degrees']
    
if __name__ == '__main__':
    str1='0Below5Percent'
    clsStrReFilter_Digits20='\d{1,20}'
    print(str1.startswith('Below')) 
    print(re.findall(pattern = clsStrReFilter_Digits20, string = str1))

    
    print(list(OrderedDict.fromkeys(Test1.clsListStr1)))
    #print 'haha %d, nihao %s, to %d' %(2016, 'sun', 13)