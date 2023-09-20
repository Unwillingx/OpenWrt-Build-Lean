#!/usr/bin/env python
import yaml
import os
os.system('rm ./rule_provider/Google.yaml')
os.system('rm ./rule_provider/Youtube.yaml')
os.system('rm ./rule_provider/Disneyplus.yaml')
os.system('rm ./rule_provider/Netflix.yaml')
os.system('rm ./rule_provider/Instagram.yaml')
os.system('rm ./rule_provider/Facebook.yaml')
os.system('rm ./rule_provider/Spotify.yaml')
os.system('rm ./rule_provider/Github.yaml')
os.system('rm ./rule_provider/Twitter.yaml')
os.system('rm ./rule_provider/Telegram.yaml')
os.system('rm ./rule_provider/Microsoft.yaml')
os.system('rm ./rule_provider/ProxyGFW.yaml')
os.system('wget -cO ./rule_provider/Google.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Google.yaml')
os.system('wget -cO ./rule_provider/Youtube.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/YouTube.yaml')
os.system('wget -cO ./rule_provider/Disneyplus.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/DisneyPlus.yaml')
os.system('wget -cO ./rule_provider/Netflix.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Netflix.yaml')
os.system('wget -cO ./rule_provider/Instagram.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Instagram.yaml')
os.system('wget -cO ./rule_provider/Facebook.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Facebook.yaml')
os.system('wget -cO ./rule_provider/Spotify.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Spotify.yaml')
os.system('wget -cO ./rule_provider/Github.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Github.yaml')
os.system('wget -cO ./rule_provider/Twitter.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Twitter.yaml')
os.system('wget -cO ./rule_provider/Telegram.yaml https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt')
os.system('wget -cO ./rule_provider/Microsoft.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Microsoft.yaml')
os.system('wget -cO ./rule_provider/ProxyGFW.yaml https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/ProxyGFWlist.yaml')

with open('./config/xy.yaml', 'rb') as f:
    x = yaml.safe_load(f)
Proxy = ['HK', 'SGP', 'JP', 'TW', 'USA', 'ML', 'TK']
HK = []
SGP = []
JP = []
TW = []
ML = []
USA = []
TK = []
for p in x['proxies']:
    name = p['name']
    if 'Hong Kong' in name:
        Proxy.append(name)
        HK.append(name)
    elif 'Japan' in name:
        Proxy.append(name)
        JP.append(name)
    elif 'Singapore' in name:
        Proxy.append(name)
        SGP.append(name)
    elif 'Tai' in name:
        Proxy.append(name)
        TW.append(name)
    elif 'USA' in name:
        Proxy.append(name)
        USA.append(name)
    elif 'Malaysia' in name:
        Proxy.append(name)
        ML.append(name)
    elif 'Turkey' in name:
        Proxy.append(name)
        TK.append(name)
Google = Proxy[7:]
Disneyplus = Google
Netflix ＝ Google
Instagram = ['HK', 'SGP', 'JP', 'TW', 'USA', 'ML', 'TK']
Youtube = ['HK', 'SGP', 'JP', 'TW', 'USA', 'ML', 'TK']
Spotify = ['HK', 'SGP', 'JP', 'TW', 'USA', 'ML', 'TK', 'DIRECT']
Github = ['HK', 'SGP', 'JP', 'TW', 'USA', 'ML', 'TK']
Twitter = ['HK', 'SGP', 'JP', 'TW', 'USA', 'ML', 'TK']
Telegram = ['HK', 'SGP', 'JP', 'TW', 'USA', 'ML', 'TK']
Microsoft = ['HK', 'SGP', 'JP', 'TW', 'USA', 'ML', 'TK', 'DIRECT']

pgs = []
pgs.append({'name':'Proxy', 'type':'select', 'proxies':Proxy})
pgs.append({'name':'Google', 'type':'select', 'proxies':Google})
pgs.append({'name':'Disneyplus', 'type':'select', 'proxies':Disneyplus})
pgs.append({'name':'Netflix', 'type':'select', 'proxies':Netflix})
pgs.append({'name':'Instagram', 'type':'select', 'proxies':Instagram})
pgs.append({'name':'Youtube', 'type':'select', 'proxies':Youtube})
pgs.append({'name':'Spotify', 'type':'select', 'proxies':Spotify})
pgs.append({'name':'Github', 'type':'select', 'proxies':Github})
pgs.append({'name':'Twitter', 'type':'select', 'proxies':Twitter})
pgs.append({'name':'Telegram', 'type':'select', 'proxies':Telegram})
pgs.append({'name':'Microsoft', 'type':'select', 'proxies':Microsoft})
pgs.append({'name':'HK', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':HK, 'url': 'http://www.gstatic.com/generate_204', 'interval': '300'})
pgs.append({'name':'SGP', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':SGP, 'url': 'http://www.gstatic.com/generate_204', 'interval': '300'})
pgs.append({'name':'TW', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':TW, 'url': 'http://www.gstatic.com/generate_204', 'interval': '300'})
pgs.append({'name':'JP', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':JP, 'url': 'http://www.gstatic.com/generate_204', 'interval': '300'})
pgs.append({'name':'USA', 'type': 'url-test', 'proxies':USA,
            'url': 'http://www.gstatic.com/generate_204', 'interval': '300'})
pgs.append({'name':'ML', 'type': 'url-test', 'proxies':ML,
            'url': 'http://www.gstatic.com/generate_204', 'interval': '300'})
pgs.append({'name':'TK', 'type': 'url-test', 'proxies':TK,
            'url': 'http://www.gstatic.com/generate_204', 'interval': '300'})
rps = {}
rps['Google'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Google.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Google.yaml'}
rps['Youtube'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Youtube.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/YouTube.yaml'}
rps['Disneyplus'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Disneyplus.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/DisneyPlus.yaml'}
rps['Netflix'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Netflix.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Netflix.yaml'}
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
rs.append('DOMAIN-SUFFIX,ipify.org,Youtube')
rs.append('DOMAIN-SUFFIX,ip.sb,Github')
rs.append('DOMAIN-KEYWORD,ieee,DIRECT')
rs.append('DOMAIN-KEYWORD,elsevier,DIRECT')
rs.append('DOMAIN-KEYWORD,sciencedirect,DIRECT')
rs.append('DOMAIN-KEYWORD,springer,DIRECT')
rs.append('RULE-SET,Disneyplus,Disneyplus')
rs.append('RULE-SET,Netflix,Netflix')
rs.append('RULE-SET,ProxyGFW,Proxy')
rs.append('GEOIP,CN,DIRECT')
rs.append('MATCH,Proxy')
z = {}
for k in x.keys():
    if k == 'proxy-groups':
        z[k] = pgs
    elif k == 'rules':
        z[k] = rs 
    else:    
        z[k] = x[k]
z['rule-providers'] = rps
with open('./config/myconfig2.yaml', 'w', encoding='utf-8') as file:
    file.write(yaml.dump(z, allow_unicode=True))
os.system('service openclash restart')
