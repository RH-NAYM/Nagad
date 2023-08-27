import torch

# nModel = torch.hub.load('yolov5', 'custom', path='AI_Models/nagad_normalized_AI_model_version2.pt', source='local')#, device=0)
nModel = torch.hub.load('yolov5', 'custom', path='AI_Models/old/nagad_normalized_AI_model_version2.pt', source='local')#, device=0)
# nModel.conf = 0.4
# nModel.iou = 0.5

nval = [
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

ndel_item = [
            'nagad_poster_1000_cashback',
            'nagad_poster_ananto_bmw',
            'nagad_sticker_payment_bangla'
            ]
nagad_item1 = ['nagad_board_close_pvc','nagad_board_open_pvc']
nagad_item2 = ['nagad_sticker_pull_door','nagad_sticker_push_door']
    # Nagad Result Format 
    # for item in nsticker:
    #     if item in nDict:
    #         result = {item:nDict[item]}
    #         nsticker_dict.update(result)
    # for item in nshop_banner:
    #     if item in nDict:
    #         result = {item:nDict[item]}
    #         nshop_banner_dict.update(result)
    # for item in nfestoon:
    #     if item in nDict:
    #         result = {item:nDict[item]}
    #         nfestoon_dict.update(result)
    # for item in nposter:
    #     if item in nDict:
    #         result = {item:nDict[item]}
    #         nposter_dict.update(result)
    # for item in nboard:
    #     if item in nDict:
    #         result = {item:nDict[item]}
    #         nboard_dict.update(result)
    # for item in nother:
    #     if item in nDict:
    #         result = {item:nDict[item]}
    #         nother_dict.update(result)





"""

# nval_dict = {}

# nsticker = [
#             'nagad_sticker_customized_table',
#             'nagad_sticker_fraud_awareness',
#             'nagad_sticker_hotline',
#             'nagad_sticker_hotline_file_folder',
#             'nagad_sticker_payment',
#             'nagad_sticker_payment_accepted_here',
#             'nagad_sticker_payment_bangla',
#             'nagad_sticker_pull_door',
#             'nagad_sticker_push_door',
#             'nagad_sticker_qr_code',
#             'nagad_sticker_qr_horizontal_new',
#             'nagad_sticker_qr_horizontal_old',
#             'nagad_sticker_qr_vertical',
#             'nagad_sticker_remittance_1_large',
#             'nagad_sticker_remittance_2',
#             'nagad_sticker_running',
#             'nagad_sticker_shutter',
#             'nagad_sticker_table_1',
#             'nagad_sticker_table_2',
#             'nagad_sticker_table_3'
#         ]
# nsticker_dict = {}

# nshop_banner = [
#                 'nagad_shop_banner_customized',
#                 'nagad_shop_banner_lenden',
#                 'nagad_shop_banner_nagad_sheba',
#                 'nagad_shop_banner_price_1',
#                 'nagad_shop_banner_price_2',
#             ]
# nshop_banner_dict = {}

# nfestoon = [
#             'nagad_festoon_bmet',
#             'nagad_festoon_indian_visa',
#             'nagad_festoon_islamic',
#             'nagad_festoon_lenden_1',
#             'nagad_festoon_lenden_2',
#             'nagad_festoon_nagad_sheba',
#             'nagad_festoon_price_1',
#             'nagad_festoon_price_2',
#             'nagad_festoon_remittance',
#             'nagad_festoon_send_money',
#         ]
# nfestoon_dict = {}

# nposter = [
#             'nagad_poster_1000_cashback',
#             'nagad_poster_ananto_bmw',
#             'nagad_poster_fraud_awareness_1',
#             'nagad_poster_fraud_awareness_2',
#             'nagad_poster_islamic',
#             'nagad_poster_mobile_recharge',
#             'nagad_poster_remittance_2',
#         ]
# nposter_dict = {}

# nboard = [
#             'nagad_back_lit_2',
#             'nagad_board_back_lit_1_with_picture'
#         ]
# nboard_dict = {}

# nother = [
#             'nagad_hanging_display',
#             'nagad_board_close_pvc',
#             'nagad_board_open_pvc',
#             'nagad_identifier_nagad',
#             'nagad_ms_standee',
#             'nagad_table_talker',
#             'nagad_table_top_qr_pvc',
#             'nagad_table_top_qr_wooden_base_new',
#             'nagad_table_top_qr_wooden_base_old',
#             'nagad_x_banner' 
#         ]
# nother_dict = {}


# nagad_format = {
#                     "Nagad Sticker":nsticker_dict,
#                     "Nagad Shop-Banner":nshop_banner_dict,
#                     "Nagad Festoon":nfestoon_dict,
#                     "Nagad Poster":nposter_dict,
#                     "Nagad Board":nboard_dict,
#                     "Nagad Other Items":nother_dict
#                 }







# nc: 51
# names: [
#                 'nagad_back_lit_2', 
#                 'nagad_board_back_lit_1_with_picture', 
#                 'nagad_board_close_pvc', 
#                 'nagad_board_open_pvc', 
#                 'nagad_festoon_bmet', 
#                 'nagad_festoon_indian_visa', 
#                 'nagad_festoon_islamic', 
#                 'nagad_festoon_lenden_1', 
#                 'nagad_festoon_lenden_2', 
#                 'nagad_festoon_nagad_sheba', 
#                 'nagad_festoon_price_1', 
#                 'nagad_festoon_price_2', 
#                 'nagad_festoon_remittance', 
#                 'nagad_festoon_send_money', 
#                 'nagad_hanging_display', 
#                 'nagad_identifier_nagad', 
#                 'nagad_ms_standee', 
#                 'nagad_poster_fraud_awareness_1', 
#                 'nagad_poster_fraud_awareness_2', 
#                 'nagad_poster_islamic', 
#                 'nagad_poster_mobile_recharge', 
#                 'nagad_poster_remittance_2', 
#                 'nagad_shop_banner_customized', 
#                 'nagad_shop_banner_lenden', 
#                 'nagad_shop_banner_nagad_sheba', 
#                 'nagad_shop_banner_price_1', 
#                 'nagad_shop_banner_price_2', 
#                 'nagad_sticker_customized_table', 
#                 'nagad_sticker_fraud_awareness', 
#                 'nagad_sticker_hotline', 
#                 'nagad_sticker_hotline_file_folder', 
#                 'nagad_sticker_payment', 
#                 'nagad_sticker_payment_accepted_here', 
#                 'nagad_sticker_pull_door', 
#                 'nagad_sticker_push_door', 
#                 'nagad_sticker_qr_code', 
#                 'nagad_sticker_qr_horizontal_new', 
#                 'nagad_sticker_qr_horizontal_old', 
#                 'nagad_sticker_qr_vertical', 
#                 'nagad_sticker_remittance_1_large',
#                 'nagad_sticker_remittance_2', 
#                 'nagad_sticker_running', 
#                 'nagad_sticker_shutter', 
#                 'nagad_sticker_table_1', 
#                 'nagad_sticker_table_2', 
#                 'nagad_sticker_table_3', 
#                 'nagad_table_talker', 
#                 'nagad_table_top_qr_pvc', 
#                 'nagad_table_top_qr_wooden_base_new', 
#                 'nagad_table_top_qr_wooden_base_old', 
#                 'nagad_x_banner'
#         ]

"""
