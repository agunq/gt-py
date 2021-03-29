#created by agunq <agunq.e@gmail.com>

import json
import random
import re
import sys

if sys.version_info[0] < 3:
  class urllib:
    parse = __import__("urllib")
    request = __import__("urllib2")
  input = raw_input 
else:
  import urllib.request
  import urllib.parse


class GT:

    def __init__(self):
        self.url = "https://translate.google.com/"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        self.GWxKcf = ""
        self.cfb2h = ""

    def genSid(self):
        return str(random.randrange(10 ** 19 , 10 ** 20))

        
    def genAuth(self):
        url = self.url + "?op=translate"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', self.user_agent)
        res = urllib.request.urlopen(req).read().decode("utf-8")
        self.cfb2h = re.findall("\"cfb2h\":\"(.*?)\"", res)[0]
        self.GWxKcf = re.findall("\"GWxKcf\":(.*?),", res)[0]

    def genUrl(self):
        self.genAuth()
        sid = self.genSid()
        url = self.url + "_/TranslateWebserverUi/data/batchexecute?rpcids=MkEWBc&f.sid=%s&bl=%s&hl=id&soc-app=1&soc-platform=1&soc-device=1&_reqid=%s&rt=c" % (sid, self.cfb2h, self.GWxKcf)
        return url

    def genForm(self, text, text_from, text_to):
        form = {"f.req" : "[[[\"MkEWBc\",\"[[\\\"%s\\\",\\\"%s\\\",\\\"%s\\\",true],[null]]\",null,\"generic\"]]]" % (text.replace("\\", "\\\\\\\\"), text_from, text_to)}
        return form
        
    def t(self, text, text_to="en", text_from="auto"):
        url = self.genUrl()
        data = self.genForm(text, text_from, text_to)
        form = urllib.parse.urlencode(data)
        form = form.encode('ascii')
        req = urllib.request.Request(url)
        req.add_header("User-Agent", self.user_agent)
        res = urllib.request.urlopen(req, form).read().decode("utf-8").split("\n")
        json_1 = res[3][1::]  
        json_2 = json.loads(json_1)[2]
        json_3 = json.loads(json_2)
        tl1 = json_3[0][0]
        tl2 = json_3[1][0][0][1] 
        tl3l = json_3[1][0][0][5]
        tl3s = []
        for data in tl3l:
            dt1, dt2 = data
            tl3s.append(dt1)
        tl3 = " ".join(tl3s)
        tl4 = json_3[1][4][0]
        tf = json_3[0][2]
        if not tf:
          tf = json_3[1][4][1]
        tt = json_3[1][4][2]
        
        #output = [tl3, tl2, tl4, tl1, tf, tt]
        output = {"translate": tl3,
                  "pronunciation" : tl2,
                  "text": tl4,
                  "pronunciation_text": tl1,
                  "lang_from": tf,
                  "lang_to": tt}
        
        return output

    #this alias for def t
    def text(self, text, text_to="en", text_from="auto"):
      return self.t(text, text_to, text_from)
