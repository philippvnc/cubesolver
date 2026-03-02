from constants.face import Face
from constants.facelet import Facelet


class Cubie:
    # the identity of the 8 corners
    # assumption: starting with UP/DOWN face, then clockwise
    CORNER_URF = 0
    CORNER_URL = 1
    CORNER_ULB = 2
    CORNER_UBR = 3
    CORNER_DFR = 4
    CORNER_DLF = 5
    CORNER_DBL = 6
    CORNER_DRB = 7

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

    N_CORNER_ORIENTATIONS = 3

    # the identity of the 12 edges
    # assumptions:
    # starting with UP/DOWN face for top and bottom layer
    # starting with FRONT/BACK face for middle layer
    EDGE_UR = 0
    EDGE_UF = 1
    EDGE_UL = 2
    EDGE_UB = 3
    EDGE_DR = 4
    EDGE_DF = 5
    EDGE_DL = 6
    EDGE_DB = 7
    EDGE_FR = 8
    EDGE_FL = 9
    EDGE_BL = 10
    EDGE_BR = 11

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

    N_EDGE_ORIENTATIONS = 2

    SOLVED = (
            [(i, 0) for i in range(8)],
            [(i, 0) for i in range(12)]
        )