def fibonacci(n):
    if n <= 0:
        raise ValueError("0以下の数字は適切ではありません。")
    elif n <= 2:
        return 1
    else:
        fibArray = [1, 1]
        for i in range(3, n):
            result = fibArray[0] + fibArray[1]
            fibArray[0] = fibArray[1]
            fibArray[1] = result
        return result
