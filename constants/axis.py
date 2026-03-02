from micropython_compat import const


class Axis:
    VERTICAL = const(0)
    HORIZONTAL = const(1)

    @staticmethod
    def name(axis: int) -> str:
        if axis == Axis.HORIZONTAL:
            return "HORIZONTAL"
        elif axis == Axis.VERTICAL:
            return "VERTICAL"
        else:
            return "INVALID"