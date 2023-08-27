
import torch

rtuModel = torch.hub.load('yolov5', 'custom', path='AI_Models/RTU_model.pt', source='local', device=0)

rItem = [
            'rocket_sticker_qr_code', 
            'rocket_festoon_bill_pay', 
            'rocket_festoon_lenden', 
            'rocket_festoon_price', 
            'rocket_festoon_send_money', 
            'rocket_poster_add_money', 
            'rocket_poster_insurance', 
            'rocket_shop_banner_bill_pay', 
            'rocket_shop_banner_lenden', 
            'rocket_shop_banner_price', 
            'rocket_shop_banner_send_money', 
            'rocket_sticker_running', 
            'rocket_sticker_shutter', 
            'rocket_sticker_table', 
            'rocket_sticker_table_price', 
            'rocket_table_top_qr_1_pvc'
        ]
# rVal = [
#             'rocket_sticker_qr_code',
#             'rocket_sticker_shutter',
#             'rocket_sticker_running',
#             'rocket_sticker_table',
#             'rocket_sticker_table_price',
#             'rocket_table_top_qr_1_pvc'
#         ]

rtuVal = [            
            'rocket_sticker_qr_code',
            'rocket_sticker_shutter',
            'rocket_sticker_running',
            'rocket_sticker_table',
            'rocket_sticker_table_price',
            'rocket_table_top_qr_1_pvc',
            'tap_table_top_qr',
            'upay_sticker_shutter',
            'upay_sticker_qr_code_1',
            'upay_sticker_qr_code_2',
            'upay_table_top_qr_pvc']

uItem = [
            'upay_festoon_price', 
            'upay_festoon_traffic_1', 
            'upay_festoon_traffic_2', 
            'upay_poster_lenden', 
            'upay_shop_banner', 
            'upay_sticker_qr_code_1', 
            'upay_sticker_qr_code_2', 
            'upay_sticker_shutter', 
            'upay_table_top_qr_pvc'
         ]
tItem = ['tap_table_top_qr']

# tuVal = [
#             "tap_table_top_qr",
#             'upay_sticker_shutter',
#             'upay_sticker_qr_code_1',
#             'upay_sticker_qr_code_2',
#             'upay_table_top_qr_pvc'
#         ]
