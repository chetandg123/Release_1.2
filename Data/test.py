# import csv
#
# from Data.parameters import Data
# from get_dir import pwd
#
# p = pwd()
# districts = ['Ahmedabad','Amreli','Anand','Aravalli','Banaskantha','Bharuch','Bhavnagar','Botad',
#                  'Chhotaudepur','Devbhoomidwarka','Dohad','Gandhinagar','Girsomnath','Jamnagar',
#                  'Junagadh','Kachchh','Kheda','Mahesana','Mahisagar','Morbi','Narmada','Navsari','Patan',
#                  'Porbandar','Rajkot','Sabarkantha','Surat','Surendranagar','Tapi','Thedangs','Vadodara','Valsad']
# # file = p.get_download_dir() + "/Diksha_"+districts[0]+"_Dist_Data_last_day.csv"
# # print(file)
# #
# # with open(file) as fin:
# #     csv_reader = csv.reader(fin, delimiter=',')
# #     header = next(csv_reader)
# #     data = list(csv_reader)
# #     row_count = len(data)
# #     print(row_count)
# i = 0
# for i in range(len(Data.districts)):
#     print(Data.districts[i].text)
# #
# import json
#
# from keycloak_funcs import keyData
#
# data = keyData()
# f = open(data.get_json_file_path(), "r")
# file = json.loads(f.read())
# print("Files contains", file['requiredActions'][0]['enabled'])
import time
import unittest

from selenium import webdriver

from get_dir import pwd

p = pwd()
filename = p.get_download_dir()
print(filename)
