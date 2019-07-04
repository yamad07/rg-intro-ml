class Model:

    def fit(self, x, y):
        self.w = (x * y).sum() / (x**2).sum()

    def predict(self, x):
        return self.w * x
