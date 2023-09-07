import os

import requests
import pandas as pd
from bs4 import BeautifulSoup
import pdfkit
from urllib import request
from docx import Document
import html2text
import openpyxl

path="D:\Github Data\Python\WebScrapping\CompanyData.xlsx"
   
DIR_PATH = os.getcwd()
#FILE_NAME = 'CIK_GVKEY.xlsx'
FILE_NAME = 'WRDS CUSIP CIK.xls'
FILE_PATH = os.path.join(DIR_PATH, FILE_NAME)


fileYear=""
period=""

df = pd.read_excel(FILE_PATH)

df['cik'] = df['cik'].apply(lambda x: "{:0>{}}".format(x, 10))
def extract_companies_data(df):
    companies = []
    for idx, record in df.iterrows():
        companies.append((
            record['cik'],
            "{} (CIK {})".format(
                record['CN'],
                record['cik']
            )
        ))
    return companies

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}


companies = extract_companies_data(df)
for cik, company in companies:
    dir_path = os.path.join(DIR_PATH, company)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    url = "https://efts.sec.gov/LATEST/search-index?dateRange=all&category=custom&ciks={}&entityName={}&forms=10-K&startdt=2001-01-01&enddt=2023-08-27".format(
        cik,
        company
    )
    response = requests.get(url, headers=headers)
    data = response.json()
    hits = data.get('hits')
    total_records = hits.get('total', {}).get('value')

    for hit in hits.get('hits'):
        #print(hit)
        print()
        id_ = hit.get('_id')
#########################Create Excel File###################################
        c = hit['_source']['ciks']
        period = hit['_source']['period_ending']
        fileDate = hit['_source']['file_date']
        CIKs =' '.join(map(str, c))
        workbook=openpyxl.load_workbook(path)
        sheet= workbook.active
        newRow=[CIKs,fileDate,period]
        sheet.append(newRow)
        workbook.save(path)
        print("Yes")
############################################################      
        unique_key, filename = id_.split(':')
        unique_key = "".join(unique_key.split('-'))
        #url = "https://www.sec.gov/Archives/edgar/data/1750/000110465923082069/air-20230531x10k.htm"
        file_url = "https://www.sec.gov/Archives/edgar/data/{}/{}/{}".format(
            cik,
            unique_key,
            filename
        )

        file_name = cik+" "+period+".pdf"
        file_path = os.path.join(dir_path, file_name)
        
        config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
        pdfkit.from_url(file_url, file_path, configuration = config)
#################################################################################################################################
