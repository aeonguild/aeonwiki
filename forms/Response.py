class Response:
    def __init__(self, tx_id, form_id, hex_msg, amount, unlock_time,signature=None):
        self.tx_id = tx_id
        self.form_id = form_id
        self.hex_msg = hex_msg
        self.msg = bytes.fromhex(hex_msg.lstrip("0")).decode('utf-8')
        self.amount = amount
        self.unlock_time = unlock_time
        self.signature = signature
        
    def verifySignature(tx_id, address, signature, message):
        # check signature is valid
        # check for form in message
        # check lock time >= form end_block
        # check tx_id is unique for form
        return True
        
    def verifyPaymentId(tx_id):
        # check for valid form in message
        # check lock time >= form end_block
        # check tx_id is unique for form
        return True
