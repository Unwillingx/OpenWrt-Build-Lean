module.exports.parse = async (raw, { axios, yaml, notify, console }, { name, url, interval, selected }) => {
        const obj = yaml.parse(raw);
        var Proxy = ["HK", "JP", "SGP", "TW", "USA"];
        var HK = new Array();
        var JP = new Array();
        var SGP = new Array();
        var TW = new Array();
        var USA =new Array();
        for (var i=0;i<obj["proxies"].length;i++){
          var name = obj["proxies"][i]["name"];
          console.log(name)
          if (/香/.test(name)){
            HK.push(name);
            Proxy.push(name);            
          } else if (/日/.test(name)){
            JP.push(name);
            Proxy.push(name);
          } else if (/新/.test(name)){
            SGP.push(name);
            Proxy.push(name);
          } else if (/台/.test(name)){
            TW.push(name);
            Proxy.push(name);
          } else if (/美/.test(name)){
            USA.push(name);
            Proxy.push(name);
          }
        };
        var n = ["HK", "JP", "SGP", "TW", "USA"];
        var nn = ["HK", "JP", "SGP", "TW", "USA", "DIRECT"];
        var p = [HK, JP, SGP, TW, USA];
        var l = "http://www.gstatic.com/generate_204";
        var config = {};
        var proxygroups = new Array();
        proxygroups.push({"name":"Proxy", "type":"select", "proxies":Proxy});
        for (var i=0;i<n.length;i++){
          var t = {"name":n[i], "type":"url-test", "url":l, "interval":60, "proxies":p[i]};
          proxygroups.push(t);
        };
        proxygroups.push({"name":"Youtube", "type":"select", "proxies":n});
        proxygroups.push({"name":"Google", "type":"select", "proxies":n});
        proxygroups.push({"name":"Github", "type":"select", "proxies":n});
        proxygroups.push({"name":"Spotify", "type":"select", "proxies":n});
        proxygroups.push({"name":"Microsoft", "type":"select", "proxies":nn});
        for (var key in obj){
          if (key == "rules"){
            continue;
          } else if (key == "proxy-groups"){
            config[key] = proxygroups;
          } else {
            config[key] = obj[key];
          }
        };
        return yaml.stringify(config);
      }
