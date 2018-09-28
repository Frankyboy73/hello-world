import requests

url = "http://192.168.10.90/nuova"

payload = "<configConfMos\ncookie=\"1538160519/4ada0585-f3b9-4e51-b6ff-f93fcdf78088\"\ninHierarchical=\"false\">\n    <inConfigs>\n<pair key=\"org-root/org-PythonMaster\">\n    <orgOrg\n    name=\"PythonMaster\"\n    dn=\"org-root/org-PythonMaster\"\n    \n    status=\"created\"\n    \n    sacl=\"addchild,del,mod\">\n    </orgOrg>\n</pair>\n    </inConfigs>\n</configConfMos>"
headers = {'Authorization': 'Basic Y2lzY286Y2lzY28='}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
