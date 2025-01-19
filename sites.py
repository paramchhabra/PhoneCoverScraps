import asyncio
import os
from bs4 import BeautifulSoup
import requests
from db_stat import *
import json
import re
from rich import print
import time
import datetime as dt

proxies = {"http":os.getenv("PROXY"), "https":os.getenv("PROXY")}


async def zapvi():
    cookies = {
        'pys_first_visit': 'true',
        'pysTrafficSource': 'zapvi-in.webpkgcache.com',
        'pys_landing_page': 'https://zapvi.in/samsung-galaxy-a54-5g-back-cover/',
        '_fbp': 'fb.1.1737034263204.4957097626',
        'pbid': '75ad7c31d2d4a6b8010a0f64c60128a200367d9666309af9f8f63495d8e83fac',
        '_ga': 'GA1.1.994638080.1737034264',
        '_gcl_au': '1.1.682262625.1737034264',
        'productlist': 'undefined',
        'wp_woocommerce_session_a9189db53d0ab423c025205a2521ab44': 't_2135a0a447330eca17770e95920957%7C%7C1737207840%7C%7C1737204240%7C%7C59109caaffa6900aa8a258af06de0bf1',
        'pysAddToCartFragmentId': '9a7d34865f013a410b5e9bacbf95ff59',
        'last_pysTrafficSource': 'direct',
        'PHPSESSID': 'c057lpml08m24oogpudiiuq35q',
        'woocommerce_items_in_cart': '1',
        'woocommerce_cart_hash': '9a7d34865f013a410b5e9bacbf95ff59',
        'pys_session_limit': 'true',
        'pys_start_session': 'true',
        'last_pys_landing_page': 'https://zapvi.in/samsung-galaxy-a54-5g-back-cover/page/9/',
        'cf_clearance': 'DLugJpROrnq629Y5w7a8DJkNq6TBydd_Z381GQgPWKc-1737088148-1.2.1.1-3RTBztKkOgbte53vGPAHfssWi11loivE0p6wyD3axPigNyrYYxLDtgbrTlY7dW6sO_xktKx0PEjYj_NFB7xed4Ir7_fmEQ_GbHL4CxNYuKFEBX.QC44M_RGCUBRLcbhSdPoyCgmsu8mJq1pNppFjNT10QmIp1m80gn3Vm1KT2N92CnIExu9PyOpzzOmHiSlT6_0iicTUcz6O5JSGqJCvcb6x9lqbOh_7PCYy731265yWwPY4MCRaIPfKy1fmhJhBbFxaa2iCa9nRzQ_jDEx8PSa1TthZxlNSNZEO4.ApgBE',
        '_ga_GT38X63LQM': 'GS1.1.1737088148.3.1.1737088165.43.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,eu;q=0.8',
        # 'cookie': 'pys_first_visit=true; pysTrafficSource=zapvi-in.webpkgcache.com; pys_landing_page=https://zapvi.in/samsung-galaxy-a54-5g-back-cover/; _fbp=fb.1.1737034263204.4957097626; pbid=75ad7c31d2d4a6b8010a0f64c60128a200367d9666309af9f8f63495d8e83fac; _ga=GA1.1.994638080.1737034264; _gcl_au=1.1.682262625.1737034264; productlist=undefined; wp_woocommerce_session_a9189db53d0ab423c025205a2521ab44=t_2135a0a447330eca17770e95920957%7C%7C1737207840%7C%7C1737204240%7C%7C59109caaffa6900aa8a258af06de0bf1; pysAddToCartFragmentId=9a7d34865f013a410b5e9bacbf95ff59; last_pysTrafficSource=direct; PHPSESSID=c057lpml08m24oogpudiiuq35q; woocommerce_items_in_cart=1; woocommerce_cart_hash=9a7d34865f013a410b5e9bacbf95ff59; pys_session_limit=true; pys_start_session=true; last_pys_landing_page=https://zapvi.in/samsung-galaxy-a54-5g-back-cover/page/9/; cf_clearance=DLugJpROrnq629Y5w7a8DJkNq6TBydd_Z381GQgPWKc-1737088148-1.2.1.1-3RTBztKkOgbte53vGPAHfssWi11loivE0p6wyD3axPigNyrYYxLDtgbrTlY7dW6sO_xktKx0PEjYj_NFB7xed4Ir7_fmEQ_GbHL4CxNYuKFEBX.QC44M_RGCUBRLcbhSdPoyCgmsu8mJq1pNppFjNT10QmIp1m80gn3Vm1KT2N92CnIExu9PyOpzzOmHiSlT6_0iicTUcz6O5JSGqJCvcb6x9lqbOh_7PCYy731265yWwPY4MCRaIPfKy1fmhJhBbFxaa2iCa9nRzQ_jDEx8PSa1TthZxlNSNZEO4.ApgBE; _ga_GT38X63LQM=GS1.1.1737088148.3.1.1737088165.43.0.0',
        'priority': 'u=1, i',
        'referer': 'https://zapvi.in/samsung-galaxy-a54-5g-back-cover/page/17/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    session = requests.Session()
    session.headers.update(headers)
    session.cookies.update(cookies)
    session.proxies.update(proxies)

    url = "https://zapvi.in/"

    # print()

    for i in range(1,36):
        print(i)
        soup = BeautifulSoup(session.get(f"{url}samsung-galaxy-a54-5g-back-cover/page/{i}/").content, 'html5lib')
        soup_prod = soup.find("script", id="pys-js-extra").string.split("var pysOptions = ")[-1].rsplit(';')[0]
        soup_json = json.loads(soup_prod)['staticEvents']['ga']['woo_view_item_list'][0]['params']['items']
        for j in soup_json:
            link = soup.find("a", attrs={'aria-label':j['name']})['href']
            await insert_in_db(j['name'],j['affiliation'],int(j['price']), link)
        time.sleep(1)
    
    print("Zapvi Data Added")

async def sirphire():
    cookies = {
        '_gcl_au': '1.1.313546774.1737034271',
        '_fbp': 'fb.1.1737034271755.761971131486870583',
        '_ga': 'GA1.1.1033409362.1737034272',
        'mds_pr_659730': '1',
        'mds_app_csrf_cookie': '680b7e7d0f49917883fb0a552117448f',
        'mds_pr_643785': '1',
        'ci_session': 'd40feb0d138abf2efb77001345d4496f54309a22',
        '_ga_0Q71KP56RZ': 'GS1.1.1737204249.5.1.1737205713.0.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,eu;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.313546774.1737034271; _fbp=fb.1.1737034271755.761971131486870583; _ga=GA1.1.1033409362.1737034272; mds_pr_659730=1; mds_app_csrf_cookie=680b7e7d0f49917883fb0a552117448f; mds_pr_643785=1; ci_session=d40feb0d138abf2efb77001345d4496f54309a22; _ga_0Q71KP56RZ=GS1.1.1737204249.5.1.1737205713.0.0.0',
        'origin': 'https://in.sirphire.com',
        'priority': 'u=1, i',
        'referer': 'https://in.sirphire.com/samsung-a54-back-covers?',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    session = requests.Session()

    session.headers.update(headers)
    session.cookies.update(cookies)
    # session.proxies.update(proxies)
    
    for j in range(0,50):
        data = {
            'sysLangId': '1',
            'app_csrf_token': '680b7e7d0f49917883fb0a552117448f',
            'category_id': '33',
            'query_string': '',
            'offset': j,
        }
        response = session.post('https://in.sirphire.com/products/load-more', data=data)


        soup = BeautifulSoup(response.text,'html5lib').find_all("li")
        
        if len(soup) == 0:
            break

        print(j)
        
        for i in soup:
            a_tag = i.find("a", attrs={'target':'_blank'})
            name = a_tag.text
            brand = "Sirphire"
            price = int(i.find("span", attrs={'class':'price'}).text[1:])
            link = a_tag["href"]
            await insert_in_db(name,brand,price,link)

    print("Sirphire Data Added")

async def ringke():
    url = "https://ringke.co.in/"
    session = requests.Session()
    headers = {
        'sec-ch-ua-platform': '"Linux"',
        'Referer': 'https://ringke.co.in/collections/samsung-galaxy-a54-back-cover-case-collections',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
    }
    response = session.get(f"{url}collections/samsung-galaxy-a54-back-cover-case-collections",proxies=proxies, headers=headers)

    soup = BeautifulSoup(response.content,"html5lib")

    data = soup.find_all("a", class_="m-product-card__link")
    count = 1
    for i in data:
        print(count)
        prod_url = f"{url}{str(i["href"])}"
        data_response = requests.get(f"{prod_url}.json",proxies=proxies, headers=headers)
        data_response = data_response.json()["product"]
        name = data_response["title"]
        brand = data_response["vendor"]
        price = int(data_response["variants"][0]["price"][:-3])
        await insert_in_db(name,brand,price,prod_url)
        count+=1
    print("Ringke Data Added")

async def bewakoof():

    cookies = {
        'trkId': '96cca878-bd9b-47cd-aabc-f5930fcb3c86',
        'gbuuid': '8b7e26ab-cc16-4a07-a446-f41a7606a5e5',
        'polaris_session': '67890a2598dca91200c60da4',
        '_gcl_au': '1.1.1344945419.1737034278',
        '_ga': 'GA1.1.907370043.1737034279',
        '_fbp': 'fb.1.1737034279021.878133639448472779',
        'WZRK_G': '8106699a44bd49a5a907ed87d58790b0',
        'abId': '10',
        'WZRK_S_8R9-845-Z84Z': '%7B%22s%22%3A1737220979%2C%22t%22%3A1737221305%2C%22p%22%3A3%7D',
        '_ga_F5TF0XY73D': 'GS1.1.1737220972.7.1.1737221315.0.0.0',
    }

    headers = {
        'ab-id': '10',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,eu;q=0.8',
        'access-control-allow-origin': '*',
        'api-token': 'NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk',
        'client-device-token': 'NGNlNTUwYTc0MjBjYzQzZTdiZTNhMmY1NjNhMThhOGU6OGI1NThkZDgtOGQ5ZS00OWYxLTk4MDAtNzYxMGEzOGNjYzNk',
        'content-type': 'application/json',
        # 'cookie': 'trkId=96cca878-bd9b-47cd-aabc-f5930fcb3c86; gbuuid=8b7e26ab-cc16-4a07-a446-f41a7606a5e5; polaris_session=67890a2598dca91200c60da4; _gcl_au=1.1.1344945419.1737034278; _ga=GA1.1.907370043.1737034279; _fbp=fb.1.1737034279021.878133639448472779; WZRK_G=8106699a44bd49a5a907ed87d58790b0; abId=10; WZRK_S_8R9-845-Z84Z=%7B%22s%22%3A1737220979%2C%22t%22%3A1737221305%2C%22p%22%3A3%7D; _ga_F5TF0XY73D=GS1.1.1737220972.7.1.1737221315.0.0.0',
        'gb-plp-bucket': 'plp_score1',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI1NjM0MTMiLCJhcCI6IjExMzQzOTc2NzIiLCJpZCI6IjdhODM2ZWY1ODJlMmRkNjYiLCJ0ciI6ImQyNGY5ZjYxYjYxYjE1MTZlYjgyMzk2YjM5MjIzNWYzIiwidGkiOjE3MzcyMjEzMTU5NDl9fQ==',
        'preferred-location': 'IN',
        'priority': 'u=1, i',
        'referer': 'https://www.bewakoof.com/samsung-galaxy-a54-5g-back-covers-cases',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-d24f9f61b61b1516eb82396b392235f3-7a836ef582e2dd66-01',
        'tracestate': '2563413@nr=0-1-2563413-1134397672-7a836ef582e2dd66----1737221315949',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-newrelic-id': 'VgMBUlJSCxABVFlRDgUBUVME',
        'x-origin-host': 'www.bewakoof.com/v1/urls/samsung-galaxy-a54-5g-back-covers-cases',
        'x-tmrw-request-trace-id': '',
        'x-tmrw-trace-id': '',
    }

    url = "https://www.bewakoof.com/p/"
    for i in range(0,15):
        print(i)
        datet = dt.datetime.now()
        response = requests.get(
            f'https://www.bewakoof.com/v1/urls/samsung-galaxy-a54-5g-back-covers-cases?qf=true&cover_type=&offer_type=&designer=&preview=&sort=popular&page={i}&limit=20&fields=results&compression=true&product_fields=id,name,url,mrp,price,flip_image,display_image,in_stock,status,product_type,limited_edition,color_name,group_count,category_info,sp,cat_designer,offer,gender&filters=%7B%22filter%22:%7B%7D,%22category%22:%7B%22term%22:%22samsung-galaxy-a54-5g-back-covers-cases%22%7D%7D&plp_score=plp_score1&user_type=new_user_score&dt={datet.day}:{datet.month-1}:{datet.year}:21',
            cookies=cookies,
            headers=headers,
            proxies=proxies
        )

        for j in response.json()["products"]:
            name = j["name"].replace(", ",";")
            price = int(j["price"])
            brand = j["manufacturer_brand"]
            link = f"{url}{j["url"]}"
            await insert_in_db(name,brand,price,link)

        if len(response.json()["products"])<20:
            break

    print("Bewakoof Data Added")

async def casekaro():
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,eu;q=0.8',
        # 'content-length': '0',
        # 'cookie': '__Secure-3PSID=g.a000sQg3UiiAHktah9l-aaeLPLXTvsfx0j9QFt5xg64oMfprs9QaTOLhmYaoA0shaBlz2eF7egACgYKAR8SARQSFQHGX2MiL17HhuG9NV6T1dpEHZ7gQhoVAUF8yKrtRmXNA7BolVJuepIt3YLU0076; __Secure-3PAPISID=TC0vztYLdSIJXMhD/AlxRkmUVsL9k5_e10; NID=520=YcN7krsR5yofWadH9XmFVqjKl8eoIJKXVS7JY0UMTtSHbmIND-pG7jdPQEbdJ-jmpmyr6QgQHOgaqh0E5WuQX-Pr-XuEuPYAFf_iAaXMhiTihRoHNQxD_1Nr0aK33nOxQx6sW-KTGJa1O8oU6t1YO38Vfg0Ec-twmtiN-m3QHQrvMqkrVSPc_iwkrwnpd2ceqC7q4RuMozyzpDBp5OeM9XXXHAdFXsAHnxmYzWBGEjN_WXKhyIVpu0enXDnDZ-PFQAaFZyAS_YbhCAVIyiYTLVZybtjBYwrXvyGG_bTDH4E4slD9rUIZ1nIrSWwmogj0vKdSrIT3CNfV2-PvO4bZtI7c-bA5nglNsECMNdPeikAGNS8cHsZ7k0MBtTQcy4alL90BgPsLFBofdVR6gSl3fNxJmJHnRiMrbiskhK82XkcBpxGEcW_RucFi6sgMaRpO0We-4wLztEZRKeDXYor6c9lOCbCD1mPY56PrGYnGiDDVwrM-fign_9hw9RP8_iPohzGoYqmaEI18BbiewfdM_Sv3UB12VNcg6E7RiQesId3FqBb71XtLdYdb_bvznNpdPQD0UZJL-_2q82py4oYE18KNNeOF1CazbfJ4FnsNQdG8pcKTehm2Mwwlswu6ZH6o2mYZTNXBwKMO1Q1QuE9k7TSltV6TPqDlZOrP9eUTyTlwh60ipFkCLGuiVWZjlt1gtEPTyW8A0pdaAPqFPrd41hOIZ1BmuCrET1pqW5vJ_GhdGA8gGqDsLicqZgrXjnC2i5GPzBg9wW_IJQDYKBw0j79FmGfVuGQbAJhpew; __Secure-3PSIDTS=sidts-CjABmiPuTVx3GdF9ZZ3MXsaY_azkPyk6SyM_jRpYoHteznmSAx-vg8t7bVu52vU1_LsQAA; __Secure-3PSIDCC=AKEyXzXCX3CmNKBuddN2KUiqZ8B5lBtN1oCyjYUUIMidaegufPtTImGKu512x-MrZ-kpemkHRN4',
        'origin': 'https://casekaro.com',
        'priority': 'u=1, i',
        'referer': 'https://casekaro.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-client-data': 'CJW2yQEIpbbJAQipncoBCMH3ygEIk6HLAQiKo8sBCIegzQEI+tfOAQjW284BGMDLzAE=',
    }

    page_num = 32
    for page_num in range(1,35):
        print(page_num)
        url = "https://casekaro.com/"
        response = requests.get(f"{url}collections/samsung-a54-5g-back-covers?page={page_num}",headers=headers,proxies=proxies)
        soup = BeautifulSoup(response.content, "html5lib").find("script", id="web-pixels-manager-setup").string.split("\"productVariants\":")[2].split("}});},\"https://casekaro.com/cdn\",")[0].replace("[","{\"data\":[").replace("]","]}")
        data = json.loads(soup)
        if len(data["data"])==0:
            break
        
        for item in data["data"]:
            name = item["product"]["title"]
            price = int(item["price"]["amount"])
            brand = item["product"]["vendor"]
            link = f"{url}{item["product"]["url"]}"
            await insert_in_db(name,brand,price,link)
        time.sleep(1)
    
    print("Casekaro Data Added")

async def croma():
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,eu;q=0.8',
        'debug_trace': 'ca05dce507b454ed3d6f0396b57959bc',
        'if-none-match': 'W/"67-bLAuLaKDKa0UkfDZ1iO+0BVGnTg"',
        'origin': 'https://www.croma.com',
        'priority': 'u=1, i',
        'referer': 'https://www.croma.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'use-cache': 'false',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    response = requests.get("https://www.croma.com/l/samsung-a54-back-cover-0afz00a.html", headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text, "html5lib").find("ul",id="product-list-back").find_all("div",class_="product-info")
    count = 1
    for item in soup:
        print(count)
        name = item.find("a").text
        brand = "Croma"
        link = item.find("a")["href"]
        price = int(item.find("span",attrs={"data-testid":"new-price"}).text[2:])
        await insert_in_db(name,brand,price,link)
        count+=1
    
    print("Croma Data Added")

async def mainfunc():
    await zapvi()
    await sirphire()
    await ringke()
    await bewakoof()
    await casekaro()
    await croma()

