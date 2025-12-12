class TransferSwitch:
    def execute(self, amount, currency):
        return {
            "status": "ok",
            "selected_path": "AUREON_GLOBAL_SWITCH",
            "processed_amount": amount,
            "currency": currency
        }
