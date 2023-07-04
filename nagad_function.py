import torch
import asyncio
import json
import pandas as pd
from datetime import datetime
from data import *



# nagad_model = torch.hub.load('yolov5', 'custom', path='yolov5/weights/Nagad_Old_Model_july3.pt', source='local', device=0)
# nagad_model.conf = 0.4
# nagad_model.iou = 0.5



async def detect_objects(model, url):
    result = await asyncio.get_event_loop().run_in_executor(None, model, url)
    result = result.pandas().xyxy[0].sort_values(by=['ymax', 'xmin'])
    df = pd.DataFrame(result)
    name_counts = df.groupby('name').size().to_dict()
    result_dict = {}
    for index, row in df.iterrows():
        name = row['name']
        result_dict[name] = name_counts.get(name, 0)
        json.dumps(result_dict)
        # json.loads(result_dict)
    return result_dict

async def detect_sequence(url):




    tasks = [
        detect_objects(nagad_model, url),
        detect_objects(nagad_model, url)
    ]

    results = await asyncio.gather(*tasks)

    dict1, dict2 = results

    # Filter Extra
    for item in del_item:
        if item in dict1:
            del dict1[item]

    # Validation Filter
    for item in validation:
        if item in dict1 and dict1[item]!=0:
            result = {item:"Yes"}
            dict1.update(result)

    # Result Format 
    for item in sticker:
        if item in dict1:
            result = {item:dict1[item]}
            sticker_dict.update(result)
    for item in shop_banner:
        if item in dict1:
            result = {item:dict1[item]}
            shop_banner_dict.update(result)
    for item in festoon:
        if item in dict1:
            result = {item:dict1[item]}
            festoon_dict.update(result)
    for item in poster:
        if item in dict1:
            result = {item:dict1[item]}
            poster_dict.update(result)
    for item in board:
        if item in dict1:
            result = {item:dict1[item]}
            board_dict.update(result)
    for item in other:
        if item in dict1:
            result = {item:dict1[item]}
            other_dict.update(result)


    nagad_format = {
                        "Nagad Detection": {
                                                "Sticker":sticker_dict,
                                                "Shop Banner":shop_banner_dict,
                                                "Festoon":festoon_dict,
                                                "Poster":poster_dict,
                                                "Board":board_dict,
                                                "Other":other_dict
                                            }                    
                        }
    nagad_result = json.dumps(nagad_format)
    print(nagad_result)
    return nagad_result
    

async def mainDetect(url):
    result = await detect_sequence(url)
    # print("Result Sent to User:", result)
    # print("###################################################################################################")

    return result

def time():
    time_now = datetime.now()
    current_time = time_now.strftime("%I:%M:%S %p")
    return current_time
