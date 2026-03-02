from micropython_compat import const


class TurnAmount:
    NONE = const(0)
    QUARTER = const(1)
    HALF = const(2)
    FULL = const(4)

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