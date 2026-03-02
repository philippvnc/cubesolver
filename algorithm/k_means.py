from micropython_compat import const


class KMeans:

    @staticmethod
    def cluster(data: list[tuple[float, float, float]],
                centroid_ids: list[int],
                n_clusters: int = const(6),
                max_iterations: int = const(30)) -> list[int]:

        # initial centroids
        centroids = [data[i] for i in centroid_ids]
        # initial assignments
        assignments = []

        for iteration in range(max_iterations):
            # assign cluster to current centroids
            new_assignments = KMeans.__get_nearest_cluster_assignments(centroids, data)
            new_centroids = KMeans.__update_centroids(data, new_assignments, n_clusters)
            # if assignments and centroids converge return
            if new_assignments == assignments and KMeans.__converged(centroids, new_centroids):
                print("found stable cluster after " + str(iteration) + " iterations")
                return new_assignments
            # else repeat
            assignments = new_assignments
            centroids = new_centroids
        # return current assignments after max iterations without converging cluster assignments
        return assignments

    @staticmethod
    def __converged(old_centroids, new_centroids, tol=const(1e-5)) -> bool:
        for a, b in zip(old_centroids, new_centroids):
            if KMeans.__dist(a, b) > tol:
                return False
        return True

    @staticmethod
    def __get_nearest_cluster_assignments(centroids: list[tuple[float, float, float]],
                                          data: list[tuple[float, float, float]]):
        assignments = []
        for point in data:
            best_cluster = 0
            best_dist = KMeans.__dist(point, centroids[0])
            for c in range(1, len(centroids)):
                d = KMeans.__dist(point, centroids[c])
                if d < best_dist:
                    best_dist = d
                    best_cluster = c
            assignments.append(best_cluster)
        return assignments

    @staticmethod
    def __dist(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        dz = a[2] - b[2]
        return dx * dx + dy * dy + dz * dz

    @staticmethod
    def __mean(points: list[tuple[float, float, float]]) -> tuple[float, float, float]:
        n = len(points)
        if n == 0:
            return 0.0, 0.0, 0.0
        sx = sy = sz = 0.0
        for x, y, z in points:
            sx += x
            sy += y
            sz += z
        return sx / n, sy / n, sz / n

    @staticmethod
    def __update_centroids(data: list[tuple[float, float, float]],
                           assignments: list[int],
                           n_clusters: int) -> list[tuple[float, float, float]]:
        clusters = [[] for _ in range(n_clusters)]
        for point, c in zip(data, assignments):
            clusters[c].append(point)
        return [KMeans.__mean(cluster) for cluster in clusters]
