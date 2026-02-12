import umath

from algorithm.k_means import KMeans
from constants.face import Face


class LabelPredictor:

    def __init__(self, k_means: KMeans) -> None:
        self.__k_means = k_means

    def get_cube_labels(self, scan: list[tuple[int, int, int]]) -> list[int] | None:
        # preprocess data
        preprocessed_data = self.__preprocess_hsv_data(scan)
        # predict labels
        labels = self.__k_means.cluster(preprocessed_data, list(range(54))[4::9])
        self.__print_labels(labels)
        if not self.__are_labels_of_equal_size(labels):
            print("didnt find exactly 9 facelets for each color")
            return None
        return labels

    def __preprocess_hsv_data(self,
                              scan: list[tuple[int, int, int]]) -> list[tuple[float, float, float]]:
        normalized_data = [self.__normalize_hsv(h, s, v) for h, s, v in scan]
        xyz_data = [self.__hsv_to_xyz(h, s, v) for h, s, v in normalized_data]
        return xyz_data

    def __normalize_hsv(self,
                        hue: int,
                        saturation: int,
                        value: int) -> tuple[float, float, float]:
        return hue / 360.0, saturation / 100.0, value / 100.0

    def __hsv_to_xyz(self,
                     hue: float,
                     saturation: float,
                     value: float) -> tuple[float, float, float]:
        # convert to circular hue space
        hue_angle = 2 * umath.pi * hue
        return (
            saturation * umath.cos(hue_angle),
            saturation * umath.sin(hue_angle),
            value,
        )

    def __are_labels_of_equal_size(self, labels: list[int]) -> bool:
        label_sizes = self.__label_sizes(labels)
        return all(x == label_sizes[0] for x in label_sizes)

    def __label_sizes(self, labels: list[int]) -> list[int]:
        k = max(labels) + 1
        counts = [0] * k
        for c in labels:
            counts[c] += 1
        print("label sizes: " + str(counts))
        return counts

    def __print_labels(self, labels):
        print("labels: " + str(labels))
        label_names = [Face.short_name(label) for label in labels]
        print("label names: " + str("".join(label_names)))
        # split into faces (9 labels each)
        up_face = label_names[0:9]
        right_face = label_names[9:18]
        front_face = label_names[18:27]
        down_face = label_names[27:36]
        left_face = label_names[36:45]
        back_face = label_names[45:54]
        empty_row = "        "

        def row(face, r):
            i = r * 3
            return f"{face[i]} {face[i + 1]} {face[i + 2]}"

        # U
        for r in range(3):
            print(empty_row + row(up_face, r))
        print()

        # L F R B
        for r in range(3):
            print(
                row(left_face, r) + "   " +
                row(front_face, r) + "   " +
                row(right_face, r) + "   " +
                row(back_face, r)
            )
        print()

        # D
        for r in range(3):
            print(empty_row + row(down_face, r))
