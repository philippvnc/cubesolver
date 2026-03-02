from micropython_compat import const

from constants.face import Face
from constants.facelet import Facelet


class Cubie:
    # the identity of the 8 corners
    # assumption: starting with UP/DOWN face, then clockwise
    CORNER_URF = const(0)
    CORNER_URL = const(1)
    CORNER_ULB = const(2)
    CORNER_UBR = const(3)
    CORNER_DFR = const(4)
    CORNER_DLF = const(5)
    CORNER_DBL = const(6)
    CORNER_DRB = const(7)

    # all corners
    CORNERS = [CORNER_URF,
               CORNER_URL,
               CORNER_ULB,
               CORNER_UBR,
               CORNER_DFR,
               CORNER_DLF,
               CORNER_DBL,
               CORNER_DRB]

    # corner tetrads
    CORNER_TETRAD_A = [CORNER_URF,
                       CORNER_ULB,
                       CORNER_DLF,
                       CORNER_DRB]

    CORNER_TETRAD_B = [CORNER_URL,
                       CORNER_UBR,
                       CORNER_DFR,
                       CORNER_DBL]

    # the adjacent faces for each corner
    CORNER_FACES = [
        (Face.UP, Face.RIGHT, Face.FRONT),
        (Face.UP, Face.FRONT, Face.LEFT),
        (Face.UP, Face.LEFT, Face.BACK),
        (Face.UP, Face.BACK, Face.RIGHT),
        (Face.DOWN, Face.FRONT, Face.RIGHT),
        (Face.DOWN, Face.LEFT, Face.FRONT),
        (Face.DOWN, Face.BACK, Face.LEFT),
        (Face.DOWN, Face.RIGHT, Face.BACK)
    ]

    # the adjacent facelets for each corner
    CORNER_FACELETS = [
        (Facelet.LOWER_RIGHT_CORNER, Facelet.UPPER_LEFT_CORNER, Facelet.UPPER_RIGHT_CORNER),
        (Facelet.LOWER_LEFT_CORNER, Facelet.UPPER_LEFT_CORNER, Facelet.UPPER_RIGHT_CORNER),
        (Facelet.UPPER_LEFT_CORNER, Facelet.UPPER_LEFT_CORNER, Facelet.UPPER_RIGHT_CORNER),
        (Facelet.UPPER_RIGHT_CORNER, Facelet.UPPER_LEFT_CORNER, Facelet.UPPER_RIGHT_CORNER),
        (Facelet.UPPER_RIGHT_CORNER, Facelet.LOWER_RIGHT_CORNER, Facelet.LOWER_LEFT_CORNER),
        (Facelet.UPPER_LEFT_CORNER, Facelet.LOWER_RIGHT_CORNER, Facelet.LOWER_LEFT_CORNER),
        (Facelet.LOWER_LEFT_CORNER, Facelet.LOWER_RIGHT_CORNER, Facelet.LOWER_LEFT_CORNER),
        (Facelet.LOWER_RIGHT_CORNER, Facelet.LOWER_RIGHT_CORNER, Facelet.LOWER_LEFT_CORNER)
    ]

    N_CORNER_ORIENTATIONS = const(3)

    # the identity of the 12 edges
    # assumptions:
    # starting with UP/DOWN face for top and bottom layer
    # starting with FRONT/BACK face for middle layer
    EDGE_UR = const(0)
    EDGE_UF = const(1)
    EDGE_UL = const(2)
    EDGE_UB = const(3)
    EDGE_DR = const(4)
    EDGE_DF = const(5)
    EDGE_DL = const(6)
    EDGE_DB = const(7)
    EDGE_FR = const(8)
    EDGE_FL = const(9)
    EDGE_BL = const(10)
    EDGE_BR = const(11)

    # all edges
    EDGES = [EDGE_UR,
             EDGE_UF,
             EDGE_UL,
             EDGE_UB,
             EDGE_DR,
             EDGE_DF,
             EDGE_DL,
             EDGE_DB,
             EDGE_FR,
             EDGE_FL,
             EDGE_BL,
             EDGE_BR]

    # edge slices (tetrads)
    UP_DOWN_EDGE_SLICE = [EDGE_FR,
                          EDGE_FL,
                          EDGE_BL,
                          EDGE_BR]
    FRONT_BACK_EDGE_SLICE = [EDGE_UR,
                             EDGE_UL,
                             EDGE_DR,
                             EDGE_DL]
    LEFT_RIGHT_EDGE_SLICE = [EDGE_UF,
                             EDGE_UB,
                             EDGE_DF,
                             EDGE_DB]

    # the adjacent faces for each edge
    EDGE_FACES = [
        (Face.UP, Face.RIGHT),
        (Face.UP, Face.FRONT),
        (Face.UP, Face.LEFT),
        (Face.UP, Face.BACK),
        (Face.DOWN, Face.RIGHT),
        (Face.DOWN, Face.FRONT),
        (Face.DOWN, Face.LEFT),
        (Face.DOWN, Face.BACK),
        (Face.FRONT, Face.RIGHT),
        (Face.FRONT, Face.LEFT),
        (Face.BACK, Face.LEFT),
        (Face.BACK, Face.RIGHT)
    ]

    # the adjacent facelets for each edge
    EDGE_FACELETS = [
        (Facelet.RIGHT_EDGE, Facelet.UPPER_EDGE),
        (Facelet.LOWER_EDGE, Facelet.UPPER_EDGE),
        (Facelet.LEFT_EDGE, Facelet.UPPER_EDGE),
        (Facelet.UPPER_EDGE, Facelet.UPPER_EDGE),
        (Facelet.RIGHT_EDGE, Facelet.LOWER_EDGE),
        (Facelet.UPPER_EDGE, Facelet.LOWER_EDGE),
        (Facelet.LEFT_EDGE, Facelet.LOWER_EDGE),
        (Facelet.LOWER_EDGE, Facelet.LOWER_EDGE),
        (Facelet.RIGHT_EDGE, Facelet.LEFT_EDGE),
        (Facelet.LEFT_EDGE, Facelet.RIGHT_EDGE),
        (Facelet.RIGHT_EDGE, Facelet.LEFT_EDGE),
        (Facelet.LEFT_EDGE, Facelet.RIGHT_EDGE)
    ]

    N_EDGE_ORIENTATIONS = const(2)

    SOLVED = (
            [(i, 0) for i in range(8)],
            [(i, 0) for i in range(12)]
        )