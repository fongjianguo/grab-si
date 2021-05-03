# ### 社會創新組織
# ### https://si.taiwan.gov.tw/Home/News?fid=144

import requests
from bs4 import BeautifulSoup

result = requests.get("https://si.taiwan.gov.tw/Home/News?fid=144",verify=False) 
b = BeautifulSoup(result.text, 'html.parser') 

# 可以發現 href不是完整的網址，所以要把前面的網址補上
headers = 'https://si.taiwan.gov.tw/Files/News/144/'
link = headers + str(b.find(class_="file_item").text).strip()
print(link)


import pandas as pd
newspd = pd.read_excel(link, encoding = "utf-8")
newspd.head()


# test all of encoding
from encodings.aliases import aliases
for encoding in set(aliases.values()):
    try:
        pd.read_excel(link, encoding=encoding)
    except:
        continue
    print('Acceptable coding: ' + encoding)
