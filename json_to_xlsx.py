import pandas as pd
import json

def json_to_xlsx(json_file_path, xlsx_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    df = pd.DataFrame(data)
    
    df.to_excel(xlsx_file_path, index=False)

json_file_path = './otto_scrape/sonuc.json'  
xlsx_file_path = 'output.xlsx'  

json_to_xlsx(json_file_path, xlsx_file_path)
