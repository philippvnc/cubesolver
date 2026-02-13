from constants.cubie import Cubie
from constants.face import Face


class CubieConverter:

    @staticmethod
    def convert_to_cubie(labels: list[int]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]] | None:
        if len(labels) != 54:
            print("labels have wrong length")
            return None

        print("cubie labels: " + str(labels))

        corners = CubieConverter.__get_corners(labels)
        edges = CubieConverter.__get_edges(labels)

        if corners is None or edges is None:
            print("cubie conversion failed")
            return None

        return corners, edges

    # ------------------------------------------------
    # Returns the labels at corner positions
    # ------------------------------------------------
    @staticmethod
    def __get_corner_labels(labels: list[int]) -> list[tuple[int, int, int]]:
        """
        Given a list of 54 labels, return a list of 8 tuples (3 labels each)
        """
        corner_colors = []
        for corner in Cubie.CORNERS:
            faces = Cubie.CORNER_FACES[corner]
            facelets = Cubie.CORNER_FACELETS[corner]
            # pick the actual labels at these faces + facelets
            colors = [labels[faces[i] * 9 + facelets[i]] for i in range(3)]
            corner_colors.append(tuple(colors))
        return corner_colors

    # ------------------------------------------------
    # Returns the labels at edge positions
    # ------------------------------------------------
    @staticmethod
    def __get_edge_labels(labels: list[int]) -> list[tuple[int, int]]:
        """
        Given a list of 54 labels, return a list of 12 tuples (2 labels each)
        """
        edge_colors = []
        for edge in Cubie.EDGES:
            faces = Cubie.EDGE_FACES[edge]
            facelets = Cubie.EDGE_FACELETS[edge]
            colors = [labels[faces[i] * 9 + facelets[i]] for i in range(2)]
            edge_colors.append(tuple(colors))
        return edge_colors

    # get all the edges in cubie representation for a given labeling
    @staticmethod
    def __get_edges(labels: list[int]) -> list[tuple[int, int]] | None:
        edges = []
        for edge_labels in CubieConverter.__get_edge_labels(labels):
            identity, target = CubieConverter.__get_edge_identity(edge_labels)
            orientation = CubieConverter.__get_edge_orientation(edge_labels, target)
            if identity is None or orientation is None:
                return None
            edges.append((identity, orientation))
        print("cubie edges: " + str(edges))
        return edges

    # determine a given edges identity by its facelet labels
    # also returns the faces this edge is relating its orientation to
    @staticmethod
    def __get_edge_identity(edge_labels: tuple[int, int]) -> tuple[int,tuple[int,int]] | None:
        for edge in Cubie.EDGES:
            faces = Cubie.EDGE_FACES[edge]
            if set(edge_labels) == set(faces):
                return edge, faces
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
    @staticmethod
    def __get_corners(labels: list[int]) -> list[tuple[int, int]] | None:
        corners = []
        for corner_labels in CubieConverter.__get_corner_labels(labels):
            identity = CubieConverter.__get_corner_identity(corner_labels)
            orientation = CubieConverter.__get_corner_orientation(corner_labels)
            if identity is None or orientation is None:
                return None
            corners.append((identity, orientation))
        print("cubie corners: " + str(corners))
        return corners

    # determine the corner identity for a given combination of 3 corner facelet labels
    @staticmethod
    def __get_corner_identity(corner_labels: tuple[int, int, int]) -> int | None:
        for corner in Cubie.CORNERS:
            faces = Cubie.CORNER_FACES[corner]
            if set(corner_labels) == set(faces):
                return corner
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