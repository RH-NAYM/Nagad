import torch
import asyncio
import json
import pandas as pd
from datetime import datetime
from Data.BRTU_Data import *
from Data.Nagad_Data import *



def time():
    time_now = datetime.now()
    current_time = time_now.strftime("%I:%M:%S %p")
    return current_time

async def detect_objects(model, url):
    result = await asyncio.get_event_loop().run_in_executor(None, model, url)
    result = result.pandas().xyxy[0].sort_values(by=['ymax', 'xmin'])
    df = pd.DataFrame(result)
    name_counts = df.groupby('name').size().to_dict()
    result_dict = {}
    for index, row in df.iterrows():
        name = row['name']
        result_dict[name] = name_counts.get(name, 0)
    return result_dict


async def detect_sequence(url):
    nModel.conf = 0.67
    # nModel.conf = 0.68
    # nModel.iou = 0.2
    brtuModel.conf = 0.47
    # brtuModel.conf = 0.40
    # brtuModel.iou = 0.2
    tasks = [
                detect_objects(nModel, url),
                detect_objects(brtuModel, url)
            ]

    results = await asyncio.gather(*tasks)

    nDict, brtuDict = results
    bDict = {}
    rDict = {}
    tDict = {}
    uDict = {}
    nagad = {}

    # del nagad extra items
    for item in ndel_item:
        if item in nDict:
            del nDict[item]
    
    # nagad validation
    for i in nval:
        if i in nDict and nDict[i]!=0:
            nagad_val = {i:"yes"}
            nDict.update(nagad_val)
    for key,value in nDict.items():
        if key in nagad_item1:
            r = {"nagad_board_open_close_pvc":value}
            nagad.update(r)
        elif key in nagad_item2:
            r = {"nagad_sticker_push_pull_door":value}
            nagad.update(r)
        else:
            r = {key:value}
            nagad.update(r)



    
    # brtu validation
    for j in brtu_val:
        if j in brtuDict and brtuDict[j]!=0:
            brtu_validation = {j:"yes"}
            brtuDict.update(brtu_validation)


    # bkash result
    for b in bitem:
        if b in brtuDict:
            res_b = {b:brtuDict[b]}
            bDict.update(res_b)

    
    # rocket result
    for r in ritem:
        if r in brtuDict:
            res_r = {r:brtuDict[r]}
            rDict.update(res_r)

    # tap result
    for t in titem:
        if t in brtuDict:
            res_t = {t:brtuDict[t]}
            tDict.update(res_t)

    
    # upay result
    for u in uitem:
        if u in brtuDict:
            res_u = {u:brtuDict[u]}
            uDict.update(res_u)


    nagad_detection = {
                        'nagad':nagad,
                        'bkash':bDict,
                        'rocket':rDict,
                        'tap':tDict,
                        'upay':uDict
                        }






    nagad_result = json.dumps(nagad_detection)
    return nagad_result


async def mainDetect(url):
    try:
        result = await detect_sequence(url)
        return result
    finally:
        torch.cuda.empty_cache()
        pass

