from urllib import request
from collections import OrderedDict
import json
import re
import csv


SRC_URL_1:str = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
SRC_URL_2:str = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

def split_url(url):
    pattern = re.compile(r'\.jpghttps://',re.I) # 定義正則表達式模式，re.I 不區分大小寫
    reg_url = re.sub(pattern, '.jpg ',url) # 將.jpg後面加一個空格
    modified_url = reg_url.split() #按照空格分開，並返回一個list
    return modified_url[0] # 返回第一個imgurl

def extra_dist(address):
    return address[5:8] #取出區(三個字)

spot_elements = ["stitle", "SERIAL_NO", "longitude", "latitude", "filelist"] 

with request.urlopen(SRC_URL_1) as response_1:
    spot_list = []
    taipei_sources_1:bytes = response_1.read() 
    taipei_sources_dict_1:dict = json.loads(taipei_sources_1)
    for spots in taipei_sources_dict_1['data']['results']:
        spot_info = {} # spot_elements會放進這個空字典
        for k1,v1 in spots.items():
            if k1 in spot_elements:
                spot_info[k1] = v1
        spot_list.append(spot_info) # 每跑一次for，spot_info這個字典會放進spot_list

with request.urlopen(SRC_URL_2) as response_2:
    location_list = []
    taipei_sources_2:bytes = response_2.read() 
    taipei_sources_dict_2:dict = json.loads(taipei_sources_2)
    for locations in taipei_sources_dict_2['data']:
        location_info = {}
        for k2,v2 in locations.items():
            location_info[k2] = v2
        location_list.append(location_info)

merged_dict = {} # 合併兩個字典by SERIAL_NO

for _,value in enumerate(spot_list):
    value["filelist"] = split_url(value["filelist"])
    serial_number = value.get("SERIAL_NO")
    merged_dict[serial_number] = value # 鍵:serial_number : 值: location字典

for value in location_list:
    value["address"] = extra_dist(value["address"])
    serial_number = value.get("SERIAL_NO")
    if serial_number in merged_dict:
        merged_dict[serial_number].update(value) #如果已經有serial_number這個key，則更新spot這個字典
    else:
        merged_dict[serial_number] = value

merged_list = merged_dict.values()

# 寫入到csv
csv_file = "spot.csv"
fieldnames = ["SpotTitle","District","Longitude","Latitude","ImageURL"]

with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    # 寫入csv的標題(column)
    writer.writeheader()
    #將每個字典的數據寫進csv的row
    for row in merged_list:
        # 將merged_list的row對照給csv
        new_row = {
            "SpotTitle": row["stitle"],
            "District": row["address"],
            "Longitude": row["longitude"],
            "Latitude": row["latitude"],
            "ImageURL":row["filelist"]
        }
        writer.writerow(new_row)












    
 
    





        