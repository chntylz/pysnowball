import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls



def cash_flow(symbol, is_annuals=0, count=10):

    url = api_ref.finance_cash_flow_url+symbol
    
    if is_annuals == 1:
        url = url + '&type=Q4'
    
    url = url + '&count='+str(count)

    return utls.fetch(url)


def indicator(symbol, is_annuals=0, count=10):
    
    url = api_ref.finance_indicator_url+symbol
    
    if is_annuals == 1:
        url = url + '&type=Q4&count='
    else:
        url += '&type=all&is_detail=true&count='

    url += str(count)

    return utls.fetch(url)


def balance(symbol, is_annuals=0, count=10):

    url = api_ref.finance_balance_url+symbol

    if is_annuals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url)


def income(symbol, is_annuals=0, count=10):
    
    url = api_ref.finance_income_url+symbol

    if is_annuals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url)


def business(symbol, is_annuals=0, count=10):

    url = api_ref.finance_business_url+symbol

    if is_annuals == 1:
        url = url + '&type=Q4'

    url = url + '&count='+str(count)

    return utls.fetch(url)
 
