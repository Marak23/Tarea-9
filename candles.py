
def candles(a: list[int]) -> int:
    """
    Args:
        a (list[int]): The candles heights.
    
    Returns:
        int: The number of candles that are tallest
    """
    # Encuentra la altura máxima de las velas
    max_height = max(a)
    
    # Cuenta cuántas velas tienen la altura máxima
    return a.count(max_height)

if __name__ == "__main__":
    print(candles([4, 4, 1, 3]))  # 2
    print(candles([1, 1, 1, 1, 1]))  # 5
    print(candles([5, 3, 1, 3, 5, 3, 1, 3, 5]))  # 3
    print(candles([10000, 10001, 10002, 10002, 10000]))  # 2
    print(candles([999, 1000, 99, 912, 100]))  # 1
