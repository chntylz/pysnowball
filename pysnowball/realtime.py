import json
import os
import time
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls


def quotec(symbols):
    url = api_ref.realtime_quote+symbols
    return utls.fetch_without_token(url)


def pankou(symbol):
    url = api_ref.realtime_pankou+symbol
    return utls.fetch_without_token(url)

def his_data(symbols):
    url = api_ref.his_data_head+symbols + '&begin=' + str(round(time.time() * 1000))\
            + api_ref.his_data_tail
    print('his_data url=%s' % url)
    return utls.fetch(url)

