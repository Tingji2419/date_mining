# -*- coding: utf-8 -*-
import requests
import re
import json
for page in range(1, 11):
    url = 'https://search.51job.com/list/070000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596,2,1.html?'.format(page) 
    params = {
        'lang': 'c',
        'postchannel': '0000',
        'workyear': '99',
        'cotype': '99',
        'degreefrom': '99',
        'jobterm': '99',
        'companysize': '99',
        'ord_field': '0',
        'dibiaoid': '0',
        'line': '',
        'welfare': '',
    }
    cookies = {

    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Host': 'search.51job.com',
        'Referer': 'https://search.51job.com/list/070000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=',     
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }

    response = requests.get(url=url, params=params, headers=headers, cookies=cookies)
    response.encoding = response.apparent_encoding
    r = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text, re.S)
    string = ''.join(r)
    info_dict = json.loads(string)
    dit_py = info_dict['engine_search_result']
    dit = {}
    for i in dit_py:
        attribute_text = ' '.join(i['attribute_text'][1:])
        print(attribute_text)
        # dit['job_href'] = i['job_href']
        dit['job_name'] = i['job_name']
        dit['company_name'] = i['company_name']
        dit['money'] = i['providesalary_text']
        dit['workarea'] = i['workarea_text']
        dit['updatedate'] = i['updatedate']
        dit['companytype'] = i['companytype_text']
        dit['jobwelf'] = i['jobwelf']
        dit['attribute'] = attribute_text
        dit['companysize'] = i['companysize_text']
        print(dit)
        with open('自动化招聘信息.csv', mode='a', encoding='utf-8') as f:
            f.write('{},{},{},{},{},{},{},{}\n'.format(dit['job_name'], dit['company_name'], dit['money'], dit['workarea'], dit['companytype'], dit['jobwelf'], dit['attribute'], dit['companysize']))


