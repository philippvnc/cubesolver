import umath

from algorithm.k_means import KMeans
from constants.face import Face


class LabelPredictor:

    @staticmethod
    def get_cube_labels(scan: list[tuple[int, int, int]]) -> list[int] | None:
        preprocessed_data = LabelPredictor._preprocess_hsv_data(scan)
        labels = KMeans.cluster(preprocessed_data, list(range(54))[4::9])
        LabelPredictor._print_labels(labels)
        if not LabelPredictor._are_labels_of_equal_size(labels):
            print("didnt find exactly 9 facelets for each color")
            return None
        return labels

    @staticmethod
    def _preprocess_hsv_data(scan: list[tuple[int, int, int]]) -> list[tuple[float, float, float]]:
        normalized_data = [LabelPredictor._normalize_hsv(h, s, v) for h, s, v in scan]
        return [LabelPredictor._hsv_to_xyz(h, s, v) for h, s, v in normalized_data]

    @staticmethod
    def _normalize_hsv(hue: int,
                       saturation: int,
                       value: int) -> tuple[float, float, float]:
        return hue / 360.0, saturation / 100.0, value / 100.0

    @staticmethod
    def _hsv_to_xyz(hue: float,
                    saturation: float,
                    value: float) -> tuple[float, float, float]:
        # convert to circular hue space
        hue_angle = 2 * umath.pi * hue
        return (
            saturation * umath.cos(hue_angle),
            saturation * umath.sin(hue_angle),
            value,
        )

    @staticmethod
    def _are_labels_of_equal_size(labels: list[int]) -> bool:
        label_sizes = LabelPredictor._label_sizes(labels)
        return all(x == label_sizes[0] for x in label_sizes)

    @staticmethod
    def _label_sizes(labels: list[int]) -> list[int]:
        k = max(labels) + 1
        counts = [0] * k
        for c in labels:
            counts[c] += 1
        print("label sizes: " + str(counts))
        return counts

    @staticmethod
    def _print_labels(labels: list[int]):
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
