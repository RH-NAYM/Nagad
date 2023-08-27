import torch
brtuModel = torch.hub.load('yolov5', 'custom', path='AI_Models/old/BRTU_normalized_AI_model.pt', source='local')#, device=0)
# brtuModel.conf = 0.6
# brtuModel.iou = 0.2


bitem = [   'bkash_festoon_bill_pay', 
            'bkash_festoon_digital', 
            'bkash_festoon_price', 
            'bkash_festoon_qr', 
            'bkash_festoon_remittance', 
            'bkash_festoon_savings', 
            'bkash_hanger_push_pull_door', 
            'bkash_hanging_board_open_close', 
            'bkash_pos_pointer_back_led', 
            'bkash_poster_islamic', 
            'bkash_poster_mobile_recharge', 
            'bkash_poster_remittance', 
            'bkash_poster_savings', 
            'bkash_poster_send_money', 
            'bkash_poster_table_messi', 
            'bkash_poster_western_union', 
            'bkash_shop_banner_price', 
            'bkash_sticker_bill_pay_table', 
            'bkash_sticker_fraud_awareness', 
            'bkash_sticker_mask_bangla', 
            'bkash_sticker_mask_english', 
            'bkash_sticker_payment_dai_cut', 
            'bkash_sticker_payment_large', 
            'bkash_sticker_payment_running', 
            'bkash_sticker_price', 
            'bkash_sticker_push_pull_door', 
            'bkash_sticker_qr_code', 
            'bkash_sticker_qr_vertical_1', 
            'bkash_sticker_running', 
            'bkash_sticker_shutter', 
            'bkash_sticker_table', 
            'bkash_sticker_transaction', 
            'bkash_table_top_qr_pvc_dai_cut', 
            'bkash_table_top_qr_pvc_running', 
            'bkash_table_top_qr_smart']

ritem = [
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

titem = ['tap_table_top_qr']
uitem = [
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

brtu_val = [
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
            'upay_table_top_qr_pvc',
            'bkash_sticker_table',
            'bkash_sticker_bill_pay_table',
            'bkash_sticker_running',
            'bkash_sticker_qr_code',
            'bkash_sticker_transaction',
            'bkash_sticker_price',
            'bkash_sticker_mask_bangla',
            'bkash_sticker_fraud_awareness',
            'bkash_sticker_shutter',
            'bkash_table_top_qr_pvc_running',
            'bkash_table_top_qr_pvc_dai_cut',
            'bkash_table_top_qr_smart',
            'bkash_sticker_qr_vertical_1',
            'bkash_sticker_payment_running',
            'bkash_sticker_payment_dai_cut',
            'bkash_sticker_payment_large',
            'bkash_sticker_push_pull_door',
            'bkash_sticker_mask_english',
            'bkash_hanger_push_pull_door',
            'bkash_pos_pointer_back_led',
            'bkash_hanging_board_open_close',
            'bkash_board_back_lit_1_with_image'
        ]




