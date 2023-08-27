import torch

# tuModel = torch.hub.load('yolov5', 'custom', path='AI_Models/TapUpay_AI_Processing.pt', source='local', device=0)
# tuModel = torch.hub.load('yolov5', 'custom', path='AI_Models/tap_upay_normalized_AI_model.pt', source='local')#, device=0)
# rModel.conf = 0.4
# rModel.iou = 0.5

tuVal = [
            "tap_table_top_qr",
            'upay_sticker_shutter',
            'upay_sticker_qr_code_1',
            'upay_sticker_qr_code_2',
            'upay_table_top_qr_pvc'
        ]



"""
# tusticker = [
#                 'upay_sticker_qr_code_1',
#                 'upay_sticker_qr_code_2',
#                 'upay_sticker_shutter'
#             ]
# tusticker_dict = {}


# tufestoon = [
#                 'upay_festoon_price',
#                 'upay_festoon_traffic_1',
#                 'upay_festoon_traffic_2'
#             ]
# tufestoon_dict = {}

# tuposter = ['upay_poster_lenden']
# tuposter_dict = {}


# tushopbanner = ['upay_shop_banner']
# tushopbanner_dict = {}


# tuother = [
#             'tap_table_top_qr', 
#             'upay_table_top_qr_pvc'
#         ]
# tuother_dict = {}

# Tap+Upay Result Format
# for item in tusticker:
#     if item in tuDict:
#         result = {item:tuDict[item]}
#         tusticker_dict.update(result)
# for item in tufestoon:
#     if item in tuDict:
#         result = {item:tuDict[item]}
#         tufestoon_dict.update(result)
# for item in tuposter:
#     if item in tuDict:
#         result = {item:tuDict[item]}
#         tuposter_dict.update(result)
# for item in tushopbanner:
#     if item in tuDict:
#         result = {item:tuDict[item]}
#         tushopbanner_dict.update(result)
# for item in tuother:
#     if item in tuDict:
#         result = {item:tuDict[item]}
#         tuother_dict.update(result)
# tapupay_format = {
#                     "Upay Sticker":tusticker_dict,
#                     "Upay Festoon":tufestoon_dict,
#                     "Upay Poster":tuposter_dict,
#                     "Upay Shop-Banner":tushopbanner_dict,
#                     "TapUpay Other Items":tuother_dict
#                 }



nc: 10
names: [
            'tap_table_top_qr', 
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



"""
