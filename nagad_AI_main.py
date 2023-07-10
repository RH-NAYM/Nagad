import torch
import asyncio
import json
import pandas as pd
from datetime import datetime
from Data.Nagad_Data import nModel,nval,ndel_item
from Data.Rocket_Data import rModel,rVal
from Data.TapUpay_Data import tuModel,tuVal
from Data.Bkash_Data import *

def time():
    time_now = datetime.now()
    current_time = time_now.strftime("%I:%M:%S %p")
    return current_time



# # Nagad AI Load
# nModel = torch.hub.load('yolov5', 'custom', path='AI_Models/nagad_normalized_AI_model.pt', source='local', device=0)
# # nModel.conf = 0.4
# # nModel.iou = 0.5
# nval = [
#         'nagad_festoon_nagad_sheba',
#         'nagad_festoon_bmet',
#         'nagad_festoon_indian_visa',
#         'nagad_shop_banner_customized',
#         'nagad_shop_banner_nagad_sheba',
#         'nagad_sticker_running',
#         'nagad_sticker_shutter',
#         'nagad_sticker_table_3',
#         'nagad_sticker_table_2',
#         'nagad_sticker_table_1',
#         'nagad_sticker_customized_table',
#         'nagad_sticker_remittance_1_large',
#         'nagad_sticker_remittance_2',
#         'nagad_sticker_fraud_awareness',
#         'nagad_sticker_qr_code',
#         'nagad_sticker_hotline',
#         'nagad_sticker_hotline_file_folder',
#         'nagad_identifier_nagad',
#         'nagad_board_back_lit_1_with_picture',
#         'nagad_back_lit_2',
#         'nagad_table_top_qr_wooden_base_old',
#         'nagad_table_top_qr_wooden_base_new',
#         'nagad_table_top_qr_pvc',
#         'nagad_sticker_qr_horizontal_new',
#         'nagad_sticker_qr_horizontal_old',
#         'nagad_sticker_qr_vertical',
#         'nagad_sticker_push_door',
#         'nagad_sticker_pull_door',
#         'nagad_board_open_pvc',
#         'nagad_board_close_pvc',
#         'nagad_sticker_payment',
#         'nagad_sticker_payment_accepted_here',
#         'nagad_hanging_display',
#         'nagad_x_banner',
#         'nagad_ms_standee',
#         'nagad_table_talker'
#         ]
# ndel_item = [
#             'nagad_poster_1000_cashback',
#             'nagad_poster_ananto_bmw',
#             'nagad_sticker_payment_bangla'
#             ]


# # Tap Upay AI Load
# tuModel = torch.hub.load('yolov5', 'custom', path='AI_Models/tap_upay_normalized_AI_model.pt', source='local', device=0)
# # rModel.conf = 0.4
# # rModel.iou = 0.5
# tuVal = [
#             "tap_table_top_qr",
#             'upay_sticker_shutter',
#             'upay_sticker_qr_code_1',
#             'upay_sticker_qr_code_2',
#             'upay_table_top_qr_pvc'
#         ]


# # Rocket AI Load
# rModel = torch.hub.load('yolov5', 'custom', path='AI_Models/rocket_normalized_AI_model.pt', source='local', device=0)
# # rModel.conf = 0.4
# # rModel.iou = 0.5
# rVal = [
#             'rocket_sticker_qr_code',
#             'rocket_sticker_shutter',
#             'rocket_sticker_running',
#             'rocket_sticker_table',
#             'rocket_sticker_table_price',
#             'rocket_table_top_qr_1_pvc'
#         ]


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
                detect_objects(nModel, url),
                detect_objects(rModel, url),
                detect_objects(tuModel,url),
                detect_objects(tuModel,url)
            ]

    results = await asyncio.gather(*tasks)

    nDict,rDict,tuDict,bDict = results


    # Filter Extra Nagad
    for item in ndel_item:
        if item in nDict:
            del nDict[item]

    # Nagad Validation Filter
    for item in nval:
        if item in nDict and nDict[item]!=0:
            result = {item:"Yes"}
            nDict.update(result)

    # Tap+Upay Validation Filter
    for item in tuVal:
        if item in tuDict and tuDict[item]!=0:
            result = {item:"Yes"}
            tuDict.update(result)

    # Rocket Validation Filter
    for item in rVal:
        if item in rDict and rDict[item]!=0:
            result = {item:"Yes"}
            rDict.update(result)


    # Tap Result    
    tap = ["tap_table_top_qr"]
    for i in tap:
        if i in tuDict:
            tap_dict = {i:tuDict[i]}
        else:
            tap_dict = {}

    # Upay Result
    upay_dict = {}
    for key,value in tuDict.items():
        if key!= "tap_table_top_qr":
            upay = {key:value}
            upay_dict.update(upay)

    nagad_detection = {
                        "nagad" : nDict,
                        "rocket" : rDict,
                        "tap" : tap_dict,
                        "upay" : upay_dict,
                        "bkash" : bDict
                    }
    # Split Result
    # nagad_format = {
    #                     "Nagad Detection": nagad_format,
    #                     "Tap & Upay Detection": tapupay_format,
    #                     "Rocket Detection": rocket_format   
    #                     }
    

    nagad_result = json.dumps(nagad_detection)
    return nagad_result
    

async def mainDetect(url):
    result = await detect_sequence(url)
    # print("Result Sent to User:", result)
    # print("###################################################################################################")

    return result

