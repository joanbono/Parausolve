import requests 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from datetime import date
import argparse

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Flags & args 
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--date", action="store", dest="date", default=date.today(),
                    help="Date to get words YYYY-MM-DD", required=False)
parser.add_argument("-x", "--proxy", action="store_true", dest="proxy", default=False,
                    help="Proxy to be used", required=False)
parser.add_argument("-v", "--version", action="version", version='%(prog)s 1.0.0')
args = parser.parse_args()

def solve(date, x):
    url = "https://paraulogic.rodamots.cat:443/?solucions=%s"%(date)
    headers = {
        "Authorization": "Basic Y29udHJhc2VueWE=",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    }

    if args.proxy:
        proxy = {
            'http': 'http:127.0.0.1:8080',
            'https': 'http:127.0.0.1:8080',
        }
    else: 
        proxy = {}
    req = requests.get(url, headers=headers, proxies=proxy, verify=False)
    #req = requests.get(url, headers=headers, verify=False)
    solution_list = list(req.json()['paraules'].keys())
    for i in range(0, len(solution_list),1):
        print(solution_list[i])

if __name__ == "__main__":
    try:
        solve(args.date, args.proxy)
    except ValueError:
        print("Incorrect date format. It should be YYYY-MM-DD")
