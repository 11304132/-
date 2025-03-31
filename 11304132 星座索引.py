# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 15:30:58 2025

Spyder Editor

@author: ianwu
"""

sdate=[20,19,21,20,21,22,23,23,23,24,23,22]
conts=['摩羯座\n正面特質：領導組織、傳統、成熟穩重、目標遠大、堅持理想\n負面特質：工作狂、不知變通、老成世故、易孤獨、功利主義','水瓶座\n正面特質：與眾不同、獨立、冷靜、好奇心強、聰明、人道主義\n負面特質：冷酷、不合群、孤僻、不穩定、變化大、無法捉摸','雙魚座\n正面特質：想像力強、具有同情心、藝術特質、浪漫多情\n負面特質：不切實際、多愁善感、只說不做、易受傷、軟弱','白羊座\n正面特質：勇氣、面對挑戰、熱情活躍、好奇心強、具領導力、動作快\n負面特質：好戰、不服輸、沒耐性、自我',
       '金牛座\n正面特質：切合實際、確定務實、誠信有決心感官力強\n負面特質：易沒安全感、重視物質、固執倔強、緩慢','雙子座\n正面特質：聰明、反應快、擅溝通、博學、好奇心強、學習力強\n負面特質：不穩定、持續性不高、雙重表現',
       '巨蟹座\n正面特質：溫柔、感性、保護家人、收藏家、敏感、同情心\n負面特質：情緒化、沒安全感、自私、被動、沉溺回憶','獅子座\n正面特質：自信、創造、領導、表演、熱心助人、表達\n負面特質：驕傲、奢侈、不喜被忽略、懶惰、無法認同他人',
       '處女座\n正面特質：組織分析、謹慎、穩定、負責、擅思考、注重養生\n負面特質：嘮叨、神經質、潔癖、狡猾、挑剔','天秤座\n正面特質：機智、公平分析、優雅、具迷人魅力、美感與藝術稚子之心\n負面特質：猶豫不決、依賴、善辯、注重外在、懶惰散漫',
       '天蠍座\n正面特質：持續力強、權威、迎接挑戰、愛恨分明、敏感\n負面特質：多愁善感、隱藏、冷酷無情、毀滅、鑽牛角尖','射手座\n正面特質：大膽冒險、上進好學、樂觀、幽默風趣、好奇心強\n負面特質：不受拘束、害怕承諾、說話犀利、不穩重、不修邊幅','摩羯座\n正面特質：領導組織、傳統、成熟穩重、目標遠大、堅持理想\n負面特質：工作狂、不知變通、老成世故、易孤獨、功利主義']

import sys

birth=input("輸日生日,YYYYMMDD")
cyear=(birth[:4])
cmonth=(birth[4:6])
cdate=(birth[6:])



if  int(cmonth) > 12 or int(cmonth) < 1:
    print('error')
    sys.exit()    
    
elif  int(cmonth) == 1 and int(cdate) > 31 or int(cdate) < 1:
    print('error')
    sys.exit()   
elif ((int(cyear) % 4 == 0 and int(cyear) % 100 != 0) or (int(cyear) % 400 == 0)) and int(cmonth)==2 and int(cdate)>29:
    print('error')
    sys.exit() 
elif ((int(cyear) % 4 == 0 and int(cyear) % 100 != 0) or (int(cyear) % 400 == 0)) and int(cmonth)==2 and int(cdate)==29:
    print('雙魚座\n正面特質：想像力強、具有同情心、藝術特質、浪漫多情\n負面特質：不切實際、多愁善感、只說不做、易受傷、軟弱')
    sys.exit()
elif int(cmonth) == 2 and int(cdate) > 28 or int(cdate) < 1:
    print("error")
    sys.exit()
elif  int(cmonth) == 3 and int(cdate) > 31 or int(cdate) < 1:
    print('error')
    sys.exit()
elif  int(cmonth) == 4 and int(cdate) > 30 or int(cdate) < 1:
    print('error')
    sys.exit()
elif  int(cmonth) == 5 and int(cdate) > 31 or int(cdate) < 1:
    print('error')
    sys.exit()
elif  int(cmonth) == 6 and int(cdate) > 30 or int(cdate) < 1:
    print('error')
    sys.exit()
elif  int(cmonth) == 7 and int(cdate) > 31 or int(cdate) < 1:
    print('error')
    sys.exit()
elif  int(cmonth) == 8 and int(cdate) > 31 or int(cdate) < 1:
    print('error')
    sys.exit()
elif  int(cmonth) == 9 and int(cdate) > 30 or int(cdate) < 1:
    print('error')
    sys.exit()
elif  int(cmonth) == 10 and int(cdate) > 31 or int(cdate) < 1:
    print('error')
    sys.exit()   
elif  int(cmonth) == 11 and int(cdate) > 30 or int(cdate) < 1:
    print('error')
    sys.exit()
elif  int(cmonth) == 12 and int(cdate) > 31 or int(cdate) < 1:
    print('error')
    sys.exit()
      
print(cmonth,cdate)
def sign(cmonth,cdate):
    if int(cdate)<sdate[int(cmonth)-1]:
         print(conts[int(cmonth)-1])
         
    else:
         print(conts[int(cmonth)])
         
sign(cmonth,cdate)


