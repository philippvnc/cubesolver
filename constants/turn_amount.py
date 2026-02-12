class TurnAmount:
    NONE = 0
    EIGHTH = 0.5
    QUARTER = 1
    HALF = 2

    @staticmethod
    def name(amount: int) -> str:
        if amount == TurnAmount.EIGHTH:
            return "EIGHTH"
        elif amount == TurnAmount.QUARTER:
            return "QUARTER"
        elif amount == TurnAmount.HALF:
            return "HALF"
        else:
            return "INVALID"