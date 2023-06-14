#!/usr/bin/env python
import os
import base64
import yaml

with open('./fig.txt', 'r') as f:
    c = f.readlines()
    f.close()
print(c)
d = c[0]
d = base64.b64decode(d)
d = str(d)
print(d)
e = d[2:-1]
e = e.split(r'\r\n')
e = e[3:-1]
pp = []
for f in e:
    f = f[9:].split('@')
    passwd = f[0]
    f = f[1].split(':') 
    server = f[0]
    f = f[1].split('#')
    f = f[1].split('-')
    name = []
    for i in f:
        tmp = ''
        for j in i:
            if j == '%':
                continue
            else:
                tmp = tmp + j
        n = bytes.fromhex(tmp)
        n = n.decode('utf-8')
        name.append(n)
        n = '-'.join(name)
    pp.append({'name':n, 'type':'trojan', 'server':server, 'port':'443', 'password':passwd, 'udp':True, 'skip-cert-verify':True})
    

with open('./config/xyz.yaml', 'rb') as f:
    x = yaml.safe_load(f)
Proxy = ['HK', 'SGP', 'JP', 'TW', 'USA']
HK = []
SGP = []
JP = []
TW = []
VN = []
USA = []
for p in pp:
    name = p['name']
    if '香' in name:
        Proxy.append(name)
        HK.append(name)
    elif '日' in name:
        Proxy.append(name)
        JP.append(name)
    elif '新' in name:
        Proxy.append(name)
        SGP.append(name)
    elif '台' in name:
        Proxy.append(name)
        TW.append(name)
    elif '美' in name:
        Proxy.append(name)
        USA.append(name)
Google = Proxy[5:]
Disneyplus = Google
Instagram = ['HK', 'SGP', 'JP', 'TW', 'USA']
Youtube = ['HK', 'SGP', 'JP', 'TW', 'USA']
Spotify = ['HK', 'SGP', 'JP', 'TW', 'USA', 'DIRECT']
Github = ['HK', 'SGP', 'JP', 'TW', 'USA']
Twitter = ['HK', 'SGP', 'JP', 'TW', 'USA']
Telegram = ['HK', 'SGP', 'JP', 'TW', 'USA']
Microsoft = ['HK', 'SGP', 'JP', 'TW', 'USA', 'DIRECT']

pgs = []
pgs.append({'name':'Proxy', 'type':'select', 'proxies':Proxy})
pgs.append({'name':'Google', 'type':'select', 'proxies':Google})
pgs.append({'name':'Disneyplus', 'type':'select', 'proxies':Disneyplus})
pgs.append({'name':'Instagram', 'type':'select', 'proxies':Instagram})
pgs.append({'name':'Youtube', 'type':'select', 'proxies':Youtube})
pgs.append({'name':'Spotify', 'type':'select', 'proxies':Spotify})
pgs.append({'name':'Github', 'type':'select', 'proxies':Github})
pgs.append({'name':'Twitter', 'type':'select', 'proxies':Twitter})
pgs.append({'name':'Telegram', 'type':'select', 'proxies':Telegram})
pgs.append({'name':'Microsoft', 'type':'select', 'proxies':Microsoft})
pgs.append({'name':'HK', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':HK, 'url': 'http://www.gstatic.com/generate_204', 'interval': '60'})
pgs.append({'name':'SGP', 'type': 'url-test', 'proxies':SGP,
            'url': 'http://www.gstatic.com/generate_204', 'interval': '60'})
pgs.append({'name':'TW', 'type': 'url-test', 'proxies':TW,
            'url': 'http://www.gstatic.com/generate_204', 'interval': '60'})
pgs.append({'name':'JP', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':JP, 'url': 'http://www.gstatic.com/generate_204', 'interval': '60'})
pgs.append({'name':'USA', 'type': 'url-test', 'proxies':USA,
            'url': 'http://www.gstatic.com/generate_204', 'interval': '60'})
rps = {}
rps['Google'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Google.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Google.yaml'}
rps['Youtube'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Youtube.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/YouTube.yaml'}
rps['Disneyplus'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Disneyplus.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/DisneyPlus.yaml'}
rps['Instagram'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Instagram.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Instagram.yaml'}

rps['Facebook'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Facebook.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Facebook.yaml'}

rps['Spotify'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Spotify.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Spotify.yaml'}

rps['Github'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Github.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Github.yaml'}

rps['Twitter'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Twitter.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Twitter.yaml'}
rps['Telegram'] = {'type': 'http', 'behavior': 'ipcidr', 'path':'./rule_provider/Telegram.yaml',
                           'url':'https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt'}
rps['Microsoft'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Microsoft.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Microsoft.yaml'}
rps['ProxyGFW'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/ProxyGFW.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/ProxyGFWlist.yaml'}
rs = []
rs.append('RULE-SET,Telegram,Telegram')
rs.append('RULE-SET,Twitter,Twitter')
rs.append('RULE-SET,Instagram,Instagram')
rs.append('RULE-SET,Facebook,Instagram')
rs.append('RULE-SET,Youtube,Youtube')
rs.append('RULE-SET,Google,Google')
rs.append('RULE-SET,Spotify,Spotify')
rs.append('RULE-SET,Github,Github')
rs.append('RULE-SET,Microsoft,Microsoft')
rs.append('RULE-SET,ProxyGFW,Proxy')
rs.append('GEOIP,CN,DIRECT')
rs.append('MATCH,Proxy')
z = {}
for k in x.keys():
    if k == 'proxy-groups':
        z[k] = pgs
    elif k == 'rules':
        z[k] = rs 
    elif k == 'proxies':
        z[k] = pp
    else:    
        z[k] = x[k]
z['rule-providers'] = rps
with open('./config/myconfig2.yaml', 'w', encoding='utf-8') as file:
    file.write(yaml.dump(z, allow_unicode=True))
os.system('service openclash restart')
