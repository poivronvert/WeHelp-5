# Task 1

import os
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

with open(csv_file, 'w', newline='',encoding="utf-8") as file:
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

# group by MRT

mrt_spot_dict:dict[str, list] = {}

for item in merged_list:
    mrt = item["MRT"]
    spot = item["stitle"]
    if mrt in mrt_spot_dict.keys(): #mrt在字典裡則把spot按照key放到value後面
       mrt_spot_dict[mrt].append(spot)
    else:
       mrt_spot_dict[mrt] = [spot,] #mrt不在字典裡則把key:mrt, value = [spot]新增到字典

# 寫入到csv
mrt_csv_file = "mrt.csv" 

with open(mrt_csv_file,'w',newline="",encoding="utf-8") as file: # 編碼要用cp950，excel才不會顯示亂碼
    writer = csv.writer(file)
    writer.writerow(['MRT','Spots'])

    for station,spots in mrt_spot_dict.items():
        writer.writerow([station]+spots)


# Task 2
# 抓取PTT Lottery的網頁原始碼(HTML)
import urllib.request as req
import re
import logging
from logging.config import dictConfig
import yaml

LOG_CONF:str = "./logging.yaml"

def init_logger()->logging.Logger:
     with open(LOG_CONF, 'r') as f:
         conf = yaml.safe_load(f)
     dictConfig(conf)
     return logging.getLogger()

log = init_logger()

def get_data(url):
    #建立一個Request物件，附加Request Headers的資訊(模擬人類的request)

    request=req.Request(url, headers={
        "cookie":"over18=1", # 觀察連線得知藉由cookie over18=1之後會導入頁面
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }) # User-Agent的字串可以打開瀏覽器->Inspect->Network->Name->Headers->User-Agent中找到

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 解析原始碼，取得每篇文章的標題
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser") # 讓Beautiful協助我們解析HTML文件

    titles = root.find_all("div",class_="title") # 尋找class="title"的div標籤
    likes_dislikes = root.find_all("div", class_="nrec") # 尋找class="nrec"的div標籤

    result_list = []
    # 使用 zip 函數將 titles、likes_dislikes 和 dates 合併在一起
    for title,like_dislike in zip(titles,likes_dislikes):
        if title.a != None:
            title_text = title.a.string # 如果有標題包含a標籤（沒有被刪除），印出來
            title_url = title.a["href"]
            title_request = req.Request("https://www.ptt.cc"+title_url, headers={
            "cookie":"over18=1", # 觀察連線得知藉由cookie over18=1之後會導入頁面
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }) # User-Agent的字串可以打開瀏覽器->Inspect->Network->Name->Headers->User-Agent中找到

            with req.urlopen(title_request) as title_response:
                title_data = title_response.read().decode("utf-8")
                title_root = bs4.BeautifulSoup(title_data,"html.parser")

            def match_regex(text):
                return re.match(r'\w{3}\s+\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}', str(text))
            date_text = title_root.find(string=match_regex)

            like_dislike_text = like_dislike.span.string if like_dislike.string is not None else None
            result_list.append([title_text, like_dislike_text, date_text])

    article_file = "article.csv" 
    if not os.path.exists(article_file):
        with open(article_file,'w',newline="",encoding="utf-8") as file: 
            writer = csv.writer(file)
            writer.writerow(['Article Title','Like/DoslikeCount','PublishTime'])
 
    with open(article_file,'a',newline="",encoding="utf-8") as file: 
        writer = csv.writer(file)
        for item in result_list:
            writer.writerow(item)

     # 找到下一頁的連結
    nextlink = root.find("a", string="‹ 上頁") # 找到內文是‹ 上頁的 a 標籤
    return (nextlink["href"]) # 印出href的網址，還要再手動加上https://的prefix


def main():
     # 主程序：抓取多個頁面的標題
     try:
         page_url = "https://www.ptt.cc/bbs/Lottery/index.html"
         count = 0
         while count < 3:
             page_url = "https://www.ptt.cc"+ get_data(page_url) #手動加上https://的prefix
             count += 1
                                       
     except Exception as e:
         log.error(e, exc_info=True)

if __name__ == '__main__':
     main()



