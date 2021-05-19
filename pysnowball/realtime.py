import json
import os
import time
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def quotec(symbols):
    url = api_ref.realtime_quote+symbols
    return utls.fetch_without_token(url)

def share_quotec(symbols):
    url = api_ref.share_quote+symbols + '&extend=detail'
    return utls.fetch(url)



def pankou(symbol):
    url = api_ref.realtime_pankou+symbol
    return utls.fetch_without_token(url)

def his_data(symbols, def_cnt=1):
    url = api_ref.his_data+symbols
    url = url +  "&begin=" + str(round(time.time() * 1000))
    tail = "&period=day&type=before&count=-" + str(def_cnt) + "&indicator=kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance"
    url = url + tail
    #print('his_data url=%s' % url)
    return utls.fetch(url)

