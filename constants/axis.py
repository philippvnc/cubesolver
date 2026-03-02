class Axis:
    VERTICAL = 0
    HORIZONTAL = 1

    @staticmethod
    def name(axis: int) -> str:
        if axis == Axis.HORIZONTAL:
            return "HORIZONTAL"
        elif axis == Axis.VERTICAL:
            return "VERTICAL"
        else:
            return "INVALID"