#!/usr/bin/env python3
import yaml
import os

with open('./config/ab.yaml', 'rb') as f:
    x = yaml.safe_load(f)
Proxy = ['HK', 'SGP', 'TW', 'USA', 'OT']
HK = []
SGP = []
TW = []
USA = []
OT = []
testtime='60'
for p in x['proxies']:
    name = p['name']
    if '香' in name:
        Proxy.append(name)
        HK.append(name)
    elif '新' in name:
        Proxy.append(name)
        SGP.append(name)
    elif '台' in name:
        Proxy.append(name)
        TW.append(name)
    elif '美' in name:
        Proxy.append(name)
        USA.append(name)
    else:
        Proxy.append(name)
        OT.append(name)
Google = Proxy[5:]
Disneyplus = Google
Netflix = Google
OpenAI = Google
Instagram = Proxy[:5]
Youtube = Proxy[:5]
Spotify = Proxy[:5] + ['DIRECT']
Github = Proxy[:5]
Twitter = Proxy[:5]
Telegram = Proxy[:5]
Microsoft = Spotify

pgs = []
pgs.append({'name':'Proxy', 'type':'select', 'proxies':Proxy})
pgs.append({'name':'Google', 'type':'select', 'proxies':Google})
pgs.append({'name':'Disneyplus', 'type':'select', 'proxies':Disneyplus})
pgs.append({'name':'Netflix', 'type':'select', 'proxies':Netflix})
pgs.append({'name':'OpenAI', 'type':'select', 'proxies':OpenAI})
pgs.append({'name':'Instagram', 'type':'select', 'proxies':Instagram})
pgs.append({'name':'Youtube', 'type':'select', 'proxies':Youtube})
pgs.append({'name':'Spotify', 'type':'select', 'proxies':Spotify})
pgs.append({'name':'Github', 'type':'select', 'proxies':Github})
pgs.append({'name':'Twitter', 'type':'select', 'proxies':Twitter})
pgs.append({'name':'Telegram', 'type':'select', 'proxies':Telegram})
pgs.append({'name':'Microsoft', 'type':'select', 'proxies':Microsoft})
pgs.append({'name':'HK', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':HK, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'SGP', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':SGP, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'TW', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':TW, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'USA', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':USA, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'OT', 'type': 'select', 'proxies':OT})
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
rps['NetflixIP'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/NetflixIP.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/NetflixIP.yaml'}
rps['Microsoft'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Microsoft.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Microsoft.yaml'}
rps['OpenAI'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/OpenAI.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/OpenAi.yaml'}
rps['Scholar'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Scholar.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Scholar.yaml'}
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
rs.append('RULE-SET,OpenAI,OpenAI')
rs.append('RULE-SET,Microsoft,Microsoft')
rs.append('DOMAIN-SUFFIX,ipify.org,Youtube')
rs.append('DOMAIN-SUFFIX,ip.sb,Github')
rs.append('RULE-SET,Disneyplus,Disneyplus')
rs.append('RULE-SET,Netflix,Netflix')
rs.append('RULE-SET,NetflixIP,Netflix')
rs.append('RULE-SET,Scholar,DIRECT')
rs.append('RULE-SET,ProxyGFW,Proxy')
rs.append('GEOIP,CN,DIRECT,no-resolve')
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
os.system('rm ./config/myconfig5.yaml')
with open('./config/myconfig5.yaml', 'w') as file:
    file.write(yaml.dump(z, allow_unicode=True))
# os.system('/etc/init.d/openclash restart')
