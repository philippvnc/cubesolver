class KMeans:

    def __init__(self, n_clusters: int = 6, max_iter: int = 30):
        self.__n_clusters = n_clusters
        self.__max_iter = max_iter

    def cluster(self,
                data: list[tuple[float, float, float]],
                centroid_ids: list[int]) -> list[int]:

        # initial centroids
        centroids = [data[i] for i in centroid_ids]
        # initial assignments
        assignments = []

        for i in range(self.__max_iter):
            # assign cluster to current centroids
            new_assignments = self.__get_nearest_cluster_assignments(centroids, data)
            new_centroids = self.__update_centroids(data, new_assignments)
            # if assignments and centroids converge return
            if new_assignments == assignments and self.__converged(centroids, new_centroids):
                print("found stable cluster after " + str(i) + " iterations")
                return new_assignments
            # else repeat
            assignments = new_assignments
            centroids = new_centroids
        # return current assignments after max iterations without converging cluster assignments
        return assignments

    def __converged(self, old_centroids, new_centroids, tol=1e-5):
        for a, b in zip(old_centroids, new_centroids):
            if self.__dist_sq(a, b) > tol:
                return False
        return True

    def __get_nearest_cluster_assignments(self, centroids: list[tuple[float, float, float]],
                                          data: list[tuple[float, float, float]]):
        assignments = []
        for point in data:
            best_cluster = 0
            best_dist = self.__dist_sq(point, centroids[0])
            for c in range(1, len(centroids)):
                d = self.__dist_sq(point, centroids[c])
                if d < best_dist:
                    best_dist = d
                    best_cluster = c
            assignments.append(best_cluster)
        return assignments

    def __dist_sq(self, a, b):
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        dz = a[2] - b[2]
        return dx * dx + dy * dy + dz * dz

    def __mean(self, points: list[tuple[float, float, float]]):
        n = len(points)
        if n == 0:
            return 0.0, 0.0, 0.0
        sx = sy = sz = 0.0
        for x, y, z in points:
            sx += x
            sy += y
            sz += z
        return sx / n, sy / n, sz / n

    def __update_centroids(self,
                           data: list[tuple[float, float, float]],
                           assignments: list[int])-> list[tuple[float, float, float]]:
        clusters = [[] for _ in range(self.__n_clusters)]
        for point, c in zip(data, assignments):
            clusters[c].append(point)
        return [self.__mean(cluster) for cluster in clusters]
