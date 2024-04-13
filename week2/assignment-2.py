# Task 1
print("===Task1===")
def find_and_print(messages, current_station):
    # 綠線的所有站名，小碧潭另外處理
    station_dict = {
        0: 'Songshan',
        1: 'Nanjing Sanmin',
        2: 'Taipei Arena',
        3: 'Nanjing Fuxing',
        4: 'Songjiang Nanjing',
        5: 'Zhongshan',
        6: 'Beimen',
        7: 'Ximen',
        8: 'Xiaonanmen',
        9: 'Chiang Kai-Shek Memorial Hall',
        10: 'Guting',
        11: 'Taipower Building',
        12: 'Gongguan',
        13: 'Wanlong',
        14: 'Jingmei',
        15: 'Dapinglin',
        16: 'Qizhang',
        17: 'Xindian City Hall',
        18: 'Xindian'
    }

    #找到msg裡面的站名對照綠線的位置
    def msg_to_stat(dict,str):
        found_station = None
        for i,stat in dict.items():
            if stat in str:
                found_station = i
                break
        return found_station

    # 找出自己的位置
    me = None
    if current_station in station_dict.values():
        for i,stat in station_dict.items():
            if stat == current_station:
                me = i
                break

    # 找到距離最短的，印出朋友的名字
    distance = {}
    for ppl, msg in messages.items():
        if msg_to_stat(station_dict,msg) and (me is not None): # 當朋友和我都在綠線上的時候
            distance[ppl] = abs(msg_to_stat(station_dict,msg) - me) 
        elif (msg_to_stat(station_dict,msg) is None) and (me is None): # 當朋友和我都不在綠線上，也就是我們都在小碧潭
            distance[ppl] = 0
        elif msg_to_stat(station_dict,msg) is None: # 當朋友在小碧潭，就要先計算七張到我的距離+1
            distance[ppl] = abs(16-me) +1 
        else:
            distance[ppl] = abs(msg_to_stat(station_dict,msg)-16) + 1 # 當我在小碧潭，就要先計算七張到朋友的距離+1
    print(sorted(distance.items(), key=lambda x: x[1])[0][0])

messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

# Task 2
print("===Task2===")
def book(consultants:list[dict[str, str|float|int]], hour:int, duration:int, criteria:str)->None:
    """依顧客標準找出最合適的顧問

    Args:
        consultants (list[dict[str, str | float | int]]): 當天提供服務的問問
        hour (int): 客戶要預約幾點
        duration (int): 客戶要預約多久
        criteria (Literal[&quot;price&quot;, &quot;rate&quot;]): 客戶要依照哪種標準來找適合的顧問
    """
    # 初始化各顧問的時間表。若已初始化過的顧問則跳過
    KEY_SLOT:str="slot"
    for i in consultants:
        if KEY_SLOT not in i.keys():
            i[KEY_SLOT] = [h for h in range(0,24)]# 把KEY_SLOT:time 放進consultants，先假設顧問24小時都可以預約

    # 客戶要預約的時間表，用 list 表示。例: 要預約 15 點，諮詢2個小時，即為 [15, 16]
    appointment = [h for h in range(hour,hour+duration)]

    # 檢查哪些顧問在該時段時有空的
    availables=[]
    for i in consultants:
        if set(appointment).issubset(i.get(KEY_SLOT)): # 利用dict.get()取得KEY_SLOT的值
            availables.append(i)

    # 依照客戶標準找出最合適的
    if availables: #availables不為空list，True
        if criteria == "price": #按照金額由小到大排列
            selected = sorted(availables, key = lambda x:x.get("price"))[0]
        else:
            selected = sorted(availables, key = lambda x:x.get("rate"), reverse=True)[0] # True: 按照評價高到低排列
        # 把預約掉的時段去除
        for i in consultants:
            if i.get("name") == selected.get("name"): # 名字出現選中的顧問名單中
                for h in appointment:
                    i.get("slot").remove(h)
        print(selected.get("name"))
    else:
        print("No Service")

consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
]

book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John


# Task 3
print("===Task3===")

def func(*data):
    def put_to_dict(d:dict[str, int], k:str, v:int=1)->dict[str, int]:
        """檢查指定 key 是否在字典中，若不存在則加入該字典並給一個預設值 v，若已存在，則原值加v

        Args:
            d (dict[str, int]): 字典
            k (str): key
            v (int, optional): 指定預設值. Defaults to 1.
        """
        if k not in d.keys():
            d[k] = v
        else:
            d[k] += v

    def get_mid_n(name:str)->str:
        """取得人名的中間名

        Args:
            name (str): 中文人名

        Returns:
            str: 中間名
        """
        if len(name)==2 or len(name)==3:
            return name[1]
        else:
            return name[2]
    
    names=list(data) #將輸入data(type=tuple)轉為可迭代的list names
    counts={}
    for i in names:
        midn:str = get_mid_n(i) 
        put_to_dict(counts, midn)

    # 找出出現次數只有一次的中間名
    sorted_min_ns = sorted(counts.items(), key=lambda a: a[1])
    times = []

    #for i, name_cnt in enumerate(sorted_min_ns):
    #    for j, _ in enumerate(name_cnt):
    #        if j==1:
    #            times.append(sorted_min_ns[i][1])
    for i in sorted_min_ns:
        times.append(i[1])

    if (all(x == times[0] for x in times)) or (len(times)==1): # 每個中間名出現的次數都相同，表示沒有unique，顯示None
        # 中間名都相同，表示沒有unique，顯示None
        print("沒有")
        return # 遇到return直接跳出整個函數，不管出現在函數的第幾個階層
    else:
        unique_mid_n:str = sorted_min_ns[0][0]

    for i in names:
        """
        對 names 這個 list 裡的每個名字，找出誰的中間名，等於 unique mid n

        """
        if get_mid_n(i)==unique_mid_n:
            print(i)




func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

# Task 4
print("===Task4===")
#觀察數列得知0,+4,+4,-1,+4,+4,-1.....
def get_number(index):
    nums = [0] #初始化nums list，並且nums[0]=0
    for i in range(1, index + 1): #從1開始到index
        if i % 3 == 1 or i % 3 == 2: #除以3餘數為1或2的時候，值為前一個值+4
            num = nums[-1] + 4
        else:#整除3，值為前一個值-1
            num = nums[-1] - 1
        nums.append(num) #把結果num放進nums list

    print(nums[index]) #印出指定index在nums list的值

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70

# Task 5
print("===Task5===")
def find(spaces, stat, n):
    found=False # 初始化 found 變數為 False
    disposibles = list(map(lambda x, y: x * y, spaces, stat)) #將spaces, stat兩個lists作相乘，可載客的車廂的值>0
    result=[] #將符合條件的車廂及可載客數放進去
    for i,j in enumerate(disposibles): #index disposibles函數
        if j>=n:
            result.append([i,j])
            found = True
    if found:
        print(sorted(result,key=lambda x:x[1])[0][0])
    else:
        print(-1)

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
