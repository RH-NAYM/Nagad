import torch
import asyncio
import json
import pandas as pd
from datetime import datetime

validation = [
                'nagad_festoon_nagad_sheba',
                'nagad_festoon_bmet',
                'nagad_festoon_indian_visa',
                'nagad_shop_banner_customized',
                'nagad_shop_banner_nagad_sheba',
                'nagad_sticker_running',
                'nagad_sticker_shutter',
                'nagad_sticker_table_3',
                'nagad_sticker_table_2',
                'nagad_sticker_table_1',
                'nagad_sticker_customized_table',
                'nagad_sticker_remittance_1_large',
                'nagad_sticker_remittance_2',
                'nagad_sticker_fraud_awareness',
                'nagad_sticker_qr_code',
                'nagad_sticker_hotline',
                'nagad_sticker_hotline_file_folder',
                'nagad_identifier_nagad',
                'nagad_board_back_lit_1_with_picture',
                'nagad_back_lit_2',
                'nagad_table_top_qr_wooden_base_old',
                'nagad_table_top_qr_wooden_base_new',
                'nagad_table_top_qr_pvc',
                'nagad_sticker_qr_horizontal_new',
                'nagad_sticker_qr_horizontal_old',
                'nagad_sticker_qr_vertical',
                'nagad_sticker_push_door',
                'nagad_sticker_pull_door',
                'nagad_board_open_pvc',
                'nagad_board_close_pvc',
                'nagad_sticker_payment',
                'nagad_sticker_payment_accepted_here',
                'nagad_hanging_display',
                'nagad_x_banner',
                'nagad_ms_standee',
                'nagad_table_talker'
            ]

sticker = [
            'nagad_sticker_customized_table',
            'nagad_sticker_fraud_awareness',
            'nagad_sticker_hotline',
            'nagad_sticker_hotline_file_folder',
            'nagad_sticker_payment',
            'nagad_sticker_payment_accepted_here',
            'nagad_sticker_payment_bangla',
            'nagad_sticker_pull_door',
            'nagad_sticker_push_door',
            'nagad_sticker_qr_code',
            'nagad_sticker_qr_horizontal_new',
            'nagad_sticker_qr_horizontal_old',
            'nagad_sticker_qr_vertical',
            'nagad_sticker_remittance_1_large',
            'nagad_sticker_remittance_2',
            'nagad_sticker_running',
            'nagad_sticker_shutter',
            'nagad_sticker_table_1',
            'nagad_sticker_table_2',
            'nagad_sticker_table_3'
        ]

shop_banner = [
                'nagad_shop_banner_customized',
                'nagad_shop_banner_lenden',
                'nagad_shop_banner_nagad_sheba',
                'nagad_shop_banner_price_1',
                'nagad_shop_banner_price_2',
            ]

festoon = [
            'nagad_festoon_bmet',
            'nagad_festoon_indian_visa',
            'nagad_festoon_islamic',
            'nagad_festoon_lenden_1',
            'nagad_festoon_lenden_2',
            'nagad_festoon_nagad_sheba',
            'nagad_festoon_price_1',
            'nagad_festoon_price_2',
            'nagad_festoon_remittance',
            'nagad_festoon_send_money',
        ]

poster = [
            'nagad_poster_1000_cashback',
            'nagad_poster_ananto_bmw',
            'nagad_poster_fraud_awareness_1',
            'nagad_poster_fraud_awareness_2',
            'nagad_poster_islamic',
            'nagad_poster_mobile_recharge',
            'nagad_poster_remittance_2',
        ]

board = [
            'nagad_back_lit_2',
            'nagad_board_back_lit_1_with_picture'
        ]

other = [
            'nagad_hanging_display',
            'nagad_board_close_pvc',
            'nagad_board_open_pvc',
            'nagad_identifier_nagad',
            'nagad_ms_standee',
            'nagad_table_talker',
            'nagad_table_top_qr_pvc',
            'nagad_table_top_qr_wooden_base_new',
            'nagad_table_top_qr_wooden_base_old',
            'nagad_x_banner' 
        ]

del_item = [
            'nagad_poster_1000_cashback',
            'nagad_poster_ananto_bmw',
            'nagad_sticker_payment_bangla'
            ]



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
    nagad_model = torch.hub.load('yolov5', 'custom', path='yolov5/weights/best.pt', source='local', device=0)
    nagad_model.conf = 0.4
    nagad_model.iou = 0.5



    tasks = [
        detect_objects(nagad_model, url),
        detect_objects(nagad_model, url)
    ]

    results = await asyncio.gather(*tasks)

    dict1, dict2 = results
    print(dict1)




    return dict1
    

async def mainDetect(url):
    result = await detect_sequence(url)
    # print("Result Sent to User:", result)
    # print("###################################################################################################")

    return result

def time():
    time_now = datetime.now()
    current_time = time_now.strftime("%I:%M:%S %p")
    return current_time
