inputarr = [1, 2, 3, 4, 5]


def fuc(inputarr):
    productforZero = 1
    product = 1
    for i in inputarr:
        product = product * i
        if i != 0:
            productforZero = productforZero * i
    # print("prod", product)
    # print("prod_zero", productforZero)

    output = []
    for item in inputarr:
        if item == 0:
            output.append(productforZero)
        else:
            output.append(int(product/item))
    print(output)


fuc(inputarr)
