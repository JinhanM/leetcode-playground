def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    result = [0] * (rowIndex + 1)
    print(result)
    for index in range(rowIndex + 1):
        if index == 0:
            result[0] = 1
        elif index == 1:
            result[1] = rowIndex
        elif index <= rowIndex / 2:
            result[index] = int(result[index - 1] * (rowIndex - index + 1) / index)
        else:
            result[index] = result[rowIndex - index]

    return result


print(getRow(5))
