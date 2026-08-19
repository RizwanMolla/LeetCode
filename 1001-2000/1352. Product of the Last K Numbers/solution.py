class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]
        self.last_zero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]
            self.last_zero = len(self.prefix_products) - 1
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.prefix_products) - 1
        if k > n:
            return 0
        return self.prefix_products[-1] // self.prefix_products[-k - 1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)