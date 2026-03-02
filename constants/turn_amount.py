class TurnAmount:
    NONE = 0
    QUARTER = 1
    HALF = 2
    FULL = 4

    @staticmethod
    def name(amount: int) -> str:
        if amount == TurnAmount.QUARTER:
            return "QUARTER"
        elif amount == TurnAmount.HALF:
            return "HALF"
        elif amount == TurnAmount.FULL:
            return "FULL"
        else:
            return "INVALID"