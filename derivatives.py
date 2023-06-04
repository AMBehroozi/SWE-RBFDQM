import numpy as np

class LRB2D:
    def __init__(self, p, e, N_D, c):
        self.IN, self.OUT, self.POINT = self.class_node(p, e)
        self.N_D = N_D
        self.c = c
        self.Point = self.POINT[:, 0:3]

    def main(self):
        return self.coiff_2d_lrbf()

    def coiff_2d_lrbf(self):
        R = self.calculate_distance_matrix()
        Domin = [self.find_dominant_indices(k, R) for k in range(len(self.Point))]
        return self.calculate_W_matrices(Domin)

    def calculate_distance_matrix(self):
        return np.sqrt(((self.Point[:, 1] - self.Point[:, 1].reshape(-1, 1)) ** 2) + ((self.Point[:, 2] - self.Point[:, 2].reshape(-1, 1)) ** 2))

    def find_dominant_indices(self, k, R):
        sorted_indices = np.argsort(R[k, :])
        CC = np.column_stack((sorted_indices, np.arange(len(sorted_indices))))
        d = CC[0:self.N_D, [0, 1]]
        return np.array([[i, d[i, 0], self.Point[d[i, 0], 1], self.Point[d[i, 0], 2]] for i in range(self.N_D)])

    def calculate_W_matrices(self, Domin):
        WW_X, WW_XX, WW_Y, WW_YY = (np.zeros((len(self.Point), len(self.Point))) for _ in range(4))

        for k in range(len(self.Point)):
            G = self.build_G_matrix(Domin[k])
            Gx, Gxx, Gy, Gyy = (np.linalg.solve(G, f(2, self.N_D, Domin[k])) for f in [self.Wx, self.Wxx, self.Wy, self.Wyy])

            for j in range(self.N_D):
                WW_X[k, Domin[k][j, 1]] = Gx[j]
                WW_XX[k, Domin[k][j, 1]] = Gxx[j]
                WW_Y[k, Domin[k][j, 1]] = Gy[j]
                WW_YY[k, Domin[k][j, 1]] = Gyy[j]

        return WW_X, WW_XX, WW_Y, WW_YY

    def build_G_matrix(self, Domin):
        G = np.ones((self.N_D, self.N_D))
        for i in range(1, self.N_D):
            for j in range(self.N_D):
                G[i, j] = self.F_i(i, j, Domin)
        return G

    def F_i(self, i, j, Domin):
        return np.sqrt((Domin[j, 2] - Domin[i, 2]) ** 2 + (Domin[j, 3] - Domin[i, 3]) ** 2 + self.c ** 2)
