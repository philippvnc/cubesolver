from constants.face import Face


class CubieConverter:
    # the identity of the 8 corners
    # assumption: starting with UP/DOWN face, then clockwise
    __CORNERS = [
        (Face.UP, Face.RIGHT, Face.FRONT),
        (Face.UP, Face.FRONT, Face.LEFT),
        (Face.UP, Face.LEFT, Face.BACK),
        (Face.UP, Face.BACK, Face.RIGHT),
        (Face.DOWN, Face.FRONT, Face.RIGHT),
        (Face.DOWN, Face.LEFT, Face.FRONT),
        (Face.DOWN, Face.BACK, Face.LEFT),
        (Face.DOWN, Face.RIGHT, Face.BACK)
    ]

    # where that corners facelets are on the adjacent faces
    __CORNER_FACELETS_PER_FACE = [
        (8, 0, 2),
        (6, 0, 2),
        (0, 0, 2),
        (2, 0, 2),
        (2, 8, 6),
        (0, 8, 6),
        (6, 8, 6),
        (8, 8, 6)
    ]

    # the identity of the 12 edges
    # assumptions:
    # starting with UP/DOWN face for top and bottom layer
    # starting with FRONT/BACK face for middle layer
    __EDGES = [
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

    # where that edges facelets are on the adjacent faces
    __EDGE_FACELETS_PER_FACE = [
        (5, 1),
        (7, 1),
        (3, 1),
        (1, 1),
        (5, 7),
        (1, 7),
        (3, 7),
        (7, 7),
        (5, 3),
        (3, 5),
        (5, 3),
        (3, 5)
    ]

    def __init__(self):
        pass

    def convert_to_cubie(self,
                         labels: list[int]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]] | None:

        if len(labels) != 54:
            print("labels have wrong length")
            return None

        print("cubie labels: " + str(labels))

        corners = self.__get_corners(labels)
        edges = self.__get_edges(labels)

        if corners is None or edges is None:
            print("cubie conversion failed")
            return None

        return corners, edges

    # ------------------------------------------------
    # Returns the labels at corner positions
    # ------------------------------------------------
    def __get_corner_labels(self, labels: list[int]) -> list[tuple[int, int, int]]:
        """
        Given a list of 54 labels, return a list of 8 tuples (3 labels each)
        corresponding to the corner cubies in Kociemba order.
        """
        corner_colors = []
        for corner_idx in range(len(self.__CORNERS)):
            face_triplet = self.__CORNERS[corner_idx]
            local_triplet = self.__CORNER_FACELETS_PER_FACE[corner_idx]
            # pick the actual labels at these facelets
            colors = [labels[face_triplet[i] * 9 + local_triplet[i]] for i in range(3)]
            corner_colors.append(tuple(colors))
        return corner_colors

    # ------------------------------------------------
    # Returns the labels at edge positions
    # ------------------------------------------------
    def __get_edge_labels(self, labels: list[int]) -> list[tuple[int, int]]:
        """
        Given a list of 54 labels, return a list of 12 tuples (2 labels each)
        corresponding to the edge cubies in Kociemba order.
        """
        edge_colors = []
        for edge_idx in range(len(self.__EDGES)):
            face_pair = self.__EDGES[edge_idx]
            local_pair = self.__EDGE_FACELETS_PER_FACE[edge_idx]
            colors = [labels[face_pair[i] * 9 + local_pair[i]] for i in range(2)]
            edge_colors.append(tuple(colors))
        return edge_colors

    # get all the edges in cubie representation for a given labeling
    def __get_edges(self, labels: list[int]) -> list[tuple[int, int]] | None:
        edges = []
        for edge_labels in self.__get_edge_labels(labels):
            identity, target = self.__get_edge_identity(edge_labels)
            orientation = self.__get_edge_orientation(edge_labels, target)
            if identity is None or orientation is None:
                return None
            edges.append((identity, orientation))
        print("cubie edges: " + str(edges))
        return edges

    # determine a given edges identity by its facelet labels
    # also returns the face this edge is relating its orientation to
    def __get_edge_identity(self, edge_labels: tuple[int, int]) -> tuple[int,tuple[int,int]] | None:
        for edge_id, target in enumerate(self.__EDGES):
            if set(edge_labels) == set(target):
                return edge_id, target
        print(f"identity of edge: {edge_labels} can not be determined")
        return None

    # determine the orientation of an edge by its labels and the relating face.
    # for top and bottom layer edges the orientation is 0 if the UP/DOWN edge facelet is on the UP/DOWN face, otherwise 1
    # for middle layer edges (no UP/DOWN edge facelet) the orientation is 0 if the FRONT/BACK edge facelet is on the FRONT/BACK face, otherwise 1
    # this only works if the UP/DOWN (and FRONT/BACK for middle layers edges) edge facelet indexes in __EDGE_FACELETS_PER_FACE are always at position 0
    @staticmethod
    def __get_edge_orientation(edge_labels: tuple[int, int], target: tuple[int, int]) -> int:
        if edge_labels == target:
            return 0
        else:
            return 1

    # get all the corners in cubie representation for a given labeling
    def __get_corners(self, labels: list[int]) -> list[tuple[int, int]] | None:
        corners = []
        for corner_labels in self.__get_corner_labels(labels):
            identity = self.__get_corner_identity(corner_labels)
            orientation = self.__get_corner_orientation(corner_labels)
            if identity is None or orientation is None:
                return None
            corners.append((identity, orientation))
        print("cubie corners: " + str(corners))
        return corners

    # determine the corner identity for a given combination of 3 corner facelet labels defined by __CORNERS
    def __get_corner_identity(self, corner_labels: tuple[int, int, int]) -> int | None:
        for corner_id, target in enumerate(self.__CORNERS):
            if set(corner_labels) == set(target):
                return corner_id
        print(f"identity of corner: {corner_labels} can not be determined")
        return None

    # determine the orientation of a corner by finding the index of its UP/DOWN facelets
    # this only works with the assumption that the corner facelet indexes in __CORNER_FACELETS_PER_FACE
    # always start with the UP/DOWN facelet in the first position and continue clockwise
    @staticmethod
    def __get_corner_orientation(corner_labels: tuple[int, int, int]) -> int | None:
        for orientation, label in enumerate(corner_labels):
            if label == Face.UP or label == Face.DOWN:
                # print(f"U/D pos in corner {i}")
                return orientation
        print(f"corner orientation of corner: {corner_labels} can not be determined")
        return None