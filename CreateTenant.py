import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY29hcGlj'}
cookie = {"APIC-cookie": "0OAHstKJTn/P1lpCMVwFDbwp9sJpYy56s7k3k53TpgboogeON1XUrU0mau1Yz9ftaQoBbf1iAgzJ3NVA0KXDFlTmXNFpLYBwtEM72Uk7Hyy9okZzfNyJGHb0G+ujl4jF+2whhYDnRsep/GTLluG798YUddaQmHce7F7n+FHshaQ="}


response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)

print(response.text)