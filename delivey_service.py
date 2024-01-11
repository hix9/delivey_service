def min_platforms(robots: list, limit: int) -> int:
    '''Метод расчёта минимального количества транспортных платформ.'''
    left_index: int
    right_index: int
    platforms: int = 0
    left_index, right_index = 0, len(robots)-1
    while left_index <= right_index:
        platforms += 1
        if robots[left_index] + robots[right_index] <= limit:
            left_index += 1
        right_index -= 1
    return platforms


if __name__ == '__main__':
    robots: list = sorted([int(i) for i in input().split()])
    limit: int = int(input())
    print(min_platforms(robots, limit))
