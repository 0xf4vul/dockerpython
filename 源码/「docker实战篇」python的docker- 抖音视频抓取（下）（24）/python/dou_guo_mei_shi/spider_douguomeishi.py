#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 11:06
# @Author  : lm
# @Url     : idig8.com
# @Site    : 
# @File    : spider_douguomeishi.py
# @Software: PyCharm
import json

import requests

from multiprocessing import Queue
from handle_mongo import mongo_info
from concurrent.futures import ThreadPoolExecutor


#创建队列
queue_list = Queue()


def handle_request(url,data):
    header ={
        "client": "4",
        "version": "6916.2",
        "device": "SM-G955N",
        "sdk": "22,5.1.1",
        "imei": "354730010002552",
        "channel": "zhuzhan",
        "mac": "00:FF:E2:A2:7B:58",
        "resolution": "1440*900",
        "dpi":"2.0",
        "android-id":"bcdaf527105cc26f",
        "pseudo-id":"354730010002552",
        "brand":"samsung",
        "scale":"2.0",
        "timezone":"28800",
        "language":"zh",
        "cns":"3",
        "carrier": "Android",
        #"imsi": "310260000000000",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36",
        "lon": "105.566938",
        "lat": "29.99831",
        "cid": "512000",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        # "Cookie": "duid=58349118",
        "Host": "api.douguo.net",
        #"Content-Length": "65"
    }

    proxy = {'http': 'http://H79623F667Q3936C:84F1527F3EE09817@http-cla.abuyun.com:9030'}
    response = requests.post(url=url,headers=header,data=data,proxies=proxy)
    return response

def handle_index():
    url = "http://api.douguo.net/recipe/flatcatalogs"
    # client=4&_session=1547000257341354730010002552&v=1503650468&_vs=0
    data ={
        "client":"4",
        "_session":"1547000257341354730010002552",
        "v":"1503650468",
        "_vs":"0"
    }
    response = handle_request(url,data)
    # print(response.text)
    index_response_dic = json.loads(response.text)
    for item_index in index_response_dic["result"]["cs"]:
        # print(item_index)
        for item_index_cs in item_index["cs"]:
            # print(item_index_cs)
            for item in item_index_cs["cs"]:
                #print(item)
                data_2 ={
                    "client":"4",
                    #"_session":"1547000257341354730010002552",
                    "keyword":item["name"],
                    "_vs ":"400",
                    "order":"0"
                }
                #print(data_2)
                queue_list.put(data_2)

def handle_caipu_list(data):
    print("当前的食材：",data["keyword"])
    caipu_list_url = "http://api.douguo.net/recipe/s/0/20";
    caipu_response = handle_request(caipu_list_url, data)
    caipu_response_dict = json.loads(caipu_response.text)
    for caipu_item in caipu_response_dict["result"]["list"]:
        caipu_info ={}
        caipu_info["shicai"] = data["keyword"]
        if caipu_item["type"]==13:
            caipu_info["user_name"] = caipu_item["r"]["an"]
            caipu_info["shicai_id"] = caipu_item["r"]["id"]
            caipu_info["describe"] = caipu_item["r"]["cookstory"].replace("\n","").replace(" ","")
            caipu_info["caipu_name"] = caipu_item["r"]["n"]
            caipu_info["zuoliao_list"] = caipu_item["r"]["major"]
            #print(caipu_info)
            detail_url = "http://api.douguo.net/recipe/detail/"+ str(caipu_info["shicai_id"])
            detail_data ={
                "client":"4",
                "_session":"1547000257341354730010002552",
                "author_id":"0",
                "_vs":"2803",
                "ext":'{"query": {"kw": "'+data["keyword"]+'", "src": "2803", "idx": "1", "type": "13", "id": '+str(caipu_info["shicai_id"])+'}}'
            }

            detail_reponse = handle_request(detail_url,detail_data)
            detail_reponse_dic = json.loads(detail_reponse.text)
            caipu_info["tips"] = detail_reponse_dic["result"]["recipe"]["tips"]
            caipu_info["cookstep"] = detail_reponse_dic["result"]["recipe"]["cookstep"]
            #print(json.dumps(caipu_info))
            mongo_info.insert_item(caipu_info)

        else:
            continue


handle_index()
pool = ThreadPoolExecutor(max_workers=2)
while queue_list.qsize()>0:
    pool.submit(handle_caipu_list,queue_list.get())


