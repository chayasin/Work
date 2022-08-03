# https://www.spu.ac.th/directory/school/?do=serach&id=&search=

from tkinter import N

from tqdm import tqdm
from Driver import *
import pandas as pd 
from tqdm import tqdm
import json

school = pd.read_excel("project_school/School.xlsx")
Name = school['ชื่อโรงเรียน'].to_list()

i = 0
dat = []
for name in tqdm(Name):
    driver = createDriver(site=f"https://www.spu.ac.th/directory/school/?do=serach&id=&search={name}")
    
    table = driver.find_element(By.CLASS_NAME,"table.table-striped.table-school-1")
    Item = table.find_elements(By.TAG_NAME,"a")
    for item in Item:
        dat.append([name,item.get_attribute("href")])
    
    
    driver.quit()
    
    i = i+1
    if i > 20:
        break

# with open("sample.json", "w", encoding='utf8') as outfile:
#     json.dump(dat, outfile, ensure_ascii=False)
    
    
df = pd.DataFrame(dat, columns =['Name', 'Link']) 
df.to_csv("school_link.csv",encoding='utf-8-sig')