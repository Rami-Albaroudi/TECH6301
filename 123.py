def main():
    list_1 = [2, 7, 4, 6, 2]
    list_2 = [1, 6, 3, 5, 1]
    
    
    def list_multiplier(ls1, ls2):
        dot_product = 0
        for i, x in enumerate(ls1):
            dot_product += ls1[i] * ls2[i]
        return dot_product
main()