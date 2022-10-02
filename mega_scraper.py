import requests
from urllib3.exceptions import InsecureRequestWarning
import sys

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
headers = {
    'Host': 'guk01pacbcjl.click',
    'Sec-Ch-Ua': '"Not;A=Brand";v="99", "Chromium";v="106"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
}

params = {
    'source': '310',
}

url = input("What link do you wanna scrape (example: https://guk01pacbcjl.click/file/633900ce4ea1d/): ")
response = requests.get(url, params=params, headers=headers, verify=False)
response_list = response.text.split()
#print(response_list)
for item in response_list:
    if "href.li" in item:
        href_li = item.replace("url=","")
        print("Your mega.nz link is " + href_li.replace("https://href.li/?", "").replace('"',""))
        sys.exit()
