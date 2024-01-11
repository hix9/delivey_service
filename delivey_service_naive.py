def min_platforms() -> int:
    '''Метод расчёта минимальных транспортных платформ.'''
    robots: list = [int(i) for i in input().split()]
    limit: int = int(input())
    left_value: int
    right_value: int
    platforms: int = 0
    robots.reverse()

    for i in robots:
        if i == limit:
            platforms += 1
            robots.pop()

    for left_value in robots:
        for right_value in reversed(robots):
            while left_value + right_value <= limit:
                platforms += 1

                try:
                    robots.remove(right_value)
                    robots.remove(left_value)
                    left_value = robots[0]
                    right_value = robots[-1]

                except:
                    if robots == []:
                        break
    while robots != []:
        platforms += 1
        robots.pop()

    return platforms


if __name__ == '__main__':
    print(min_platforms())
