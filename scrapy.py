import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
"""
This a test for requests module
"""
# import requests
# url = 'https://me.csdn.net/qq_30319851'       #这里的URL就是通过开发者工具找到的网页的请求信息里的Request URL
# res = requests.get(url)   #requests后面的方法要根据网页的请求信息来判断
# # res.encoding='utf-8'      #可加可不加，爬虫结果乱码，可以用这个代码更正
# # print(res.text)           #输出获取到的东西
#
# soup = BeautifulSoup(res.text, "html5lib")
# # print(soup.select('.tab_page_list'))
#
# for item in soup.select(".tab_page_list"):
#     try:
#         print(item.select("a")[0].text.strip())
#     except OSError:
#         pass
#     continue


import requests
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
form_data = {'first': 'true',
             'pn': '1',
             'kd': 'python'}
HEADERS = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Cookie': 'user_trace_token=20190520160706-b4af01bf-ef0f-4367-a3f5-4cf3a09e68a8; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558339628; _ga=GA1.2.1966389265.1558339628; _gat=1; LGSID=20190520160708-437ef701-7ad6-11e9-a0ea-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0tbFB0FNkUs0MmrFT00000ZBec7C00000v9Q-_t.THL0oUhY1x60UWdBmy-bIfK15y79myRvuj79nj0snAD4uW00IHY3wjm4fYwKPW03fHujP1PjPHTkf19AfRRYwDnsrHc1f6K95gTqFhdWpyfqn1czP1ckrHfknzusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYEUA78uA-8uzdsmyI-QLKWQLP-mgFWpa4CIAd_5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAPBI0KWThnqnHb4nWc%26tpl%3Dtpl_11534_19713_15764%26l%3D1512094584%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3227219413_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D7%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26oq%3Dbs4.FeatureNotFound%25253A%252520%252526lt%25253Bouldn%252526%25252339%25253Bt%252520find%252520a%252520tree%252520builder%252520with%252520the%252520features%252520you%252520requ%26rqlang%3Dcn%26inputT%3D2052; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LGUID=20190520160708-437ef94a-7ad6-11e9-a0ea-5254005c3644; _gid=GA1.2.1521489055.1558339653; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ad4480cfb6d7-049da5fe612c6-3b654200-1327104-16ad4480cfc70f%22%2C%22%24device_id%22%3A%2216ad4480cfb6d7-049da5fe612c6-3b654200-1327104-16ad4480cfc70f%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=f4486eb489ac3715da389861616b5d41ecce9b09db460610cf677ccd24abdf00; LG_HAS_LOGIN=1; _putrc=04B7B7FE4C0E8C54123F89F2B170EADC; JSESSIONID=ABAAABAAAIAACBI6A695AA4B4F6062DA91490B4BE17CC84; login=true; unick=%E7%8E%8B%E9%9D%99; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=e2043ac6d130773a547188f3193bac1455a226b9f591ff46fb0856cf0ab3f2f2; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=7590ddf8b19031932389338551774df0511cb6311b; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558339832; LGRID=20190520161032-bd0fab37-7ad6-11e9-a447-525400f775ce; SEARCH_ID=adfcf3cf658c45fd932e18bdf0f1af6f',
    # User-Agent(UA) 服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等。也就是说伪装成浏览器进行访问
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    # 用于告诉服务器我是从哪个页面链接过来的，服务器基此可以获得一些信息用于处理。如果不加入，服务器可能依旧会判断为非法请求
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
  }

def getJobs():
    res = requests.post(url=url, headers=HEADERS, data=form_data)
    result = res.json()
    print(result)

getJobs()