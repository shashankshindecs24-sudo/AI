goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]


def moves(state):
    result = []

    pos = state.index(0)

    row = pos // 3
    col = pos % 3

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:

        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:

            new_pos = r * 3 + c

            new_state = state.copy()

            new_state[pos], new_state[new_pos] = \
                new_state[new_pos], new_state[pos]

            result.append(new_state)

    return result


def depth_limited_search(state, depth, path):

    if state == goal:
        return path

    if depth == 0:
        return None

    for next_state in moves(state):

        if next_state not in path:

            result = depth_limited_search(
                next_state,
                depth - 1,
                path + [next_state]
            )

            if result:
                return result

    return None


def ids(start):

    depth = 0

    while True:

        result = depth_limited_search(
            start,
            depth,
            [start]
        )

        if result:
            return result

        depth += 1


# Initial state
start = [1, 2, 3,
         4, 5, 6,
         0, 7, 8]


# Apply IDS
solution = ids(start)


# Print solution
print("Solution:")

for state in solution:

    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()