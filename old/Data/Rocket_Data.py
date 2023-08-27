import torch

# # rModel = torch.hub.load('yolov5', 'custom', path='AI_Models/Rocket_AI_Processing.pt', source='local', device=0)
# rModel = torch.hub.load('yolov5', 'custom', path='AI_Models/rocket_normalized_AI_model.pt', source='local')#, device=0)
# rModel.conf = 0.4
# rModel.iou = 0.5

rVal = [
            'rocket_sticker_qr_code',
            'rocket_sticker_shutter',
            'rocket_sticker_running',
            'rocket_sticker_table',
            'rocket_sticker_table_price',
            'rocket_table_top_qr_1_pvc'
        ]

"""

# rsticker = [
#                 'rocket_sticker_qr_code',
#                 'rocket_sticker_running',
#                 'rocket_sticker_shutter',
#                 'rocket_sticker_table',
#                 'rocket_sticker_table_price',
#             ]
# rsticker_dict = {}


# rfestoon = [
#                 'rocket_festoon_bill_pay',
#                 'rocket_festoon_lenden',
#                 'rocket_festoon_price',
#                 'rocket_festoon_send_money'
#             ]
# rfestoon_dict = {}


# rposter = [
#                 'rocket_poster_add_money',
#                 'rocket_poster_isnsurance'
#             ]
# rposter_dict = {}


# rshopbanner = [
#                     'rocket_shop_banner_bill_pay', 
#                     'rocket_shop_banner_lenden', 
#                     'rocket_shop_banner_price', 
#                     'rocket_shop_banner_send_money'
#                 ]
# rshopbanner_dict = {}


# rother = ['rocket_table_top_qr_1_pvc']
# rother_dict = {}

# rocket_format = {
#                     "Rocket Sticker":rsticker_dict,
#                     "Rocket Festoon":rfestoon_dict,
#                     "Rocket Poster":rposter_dict,
#                     "Rocket Shop-Banner":rshopbanner_dict,
#                     "Rocket Other Items":rother_dict
#                 }




# nc: 16
# names: [
#             'rocket_sticker_qr_code', 
#             'rocket_festoon_bill_pay', 
#             'rocket_festoon_lenden', 
#             'rocket_festoon_price', 
#             'rocket_festoon_send_money', 
#             'rocket_poster_add_money', 
#             'rocket_poster_isnsurance', 
#             'rocket_shop_banner_bill_pay', 
#             'rocket_shop_banner_lenden', 
#             'rocket_shop_banner_price', 
#             'rocket_shop_banner_send_money', 
#             'rocket_sticker_running', 
#             'rocket_sticker_shutter', 
#             'rocket_sticker_table', 
#             'rocket_sticker_table_price', 
#             'rocket_table_top_qr_1_pvc'
#         ]

"""
