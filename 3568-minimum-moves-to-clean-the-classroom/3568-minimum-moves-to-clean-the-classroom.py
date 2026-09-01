from collections import deque


class Solution(object):
    def minMoves(self, classroom, energy):

        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start_r = start_c = 0
        litter_count = 0

        # Find start and all litter positions
        for i in range(m):
            for j in range(n):

                if classroom[i][j] == 'S':
                    start_r = i
                    start_c = j

                elif classroom[i][j] == 'L':
                    litter[(i, j)] = litter_count
                    litter_count += 1

        # If there is no litter
        if litter_count == 0:
            return 0

        # Mask when all litter is collected
        all_mask = (1 << litter_count) - 1

        # BFS queue:
        # (row, col, remaining_energy, collected_mask, moves)
        queue = deque()

        queue.append(
            (start_r, start_c, energy, 0, 0)
        )

        # Store visited states
        visited = set()

        visited.add(
            (start_r, start_c, energy, 0)
        )

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:

            r, c, remaining, mask, moves = queue.popleft()

            # Try all 4 directions
            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Boundary check
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Cannot pass obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Moving costs 1 energy
                new_energy = remaining - 1

                # Cannot move without energy
                if new_energy < 0:
                    continue

                new_mask = mask

                # Collect litter
                if (nr, nc) in litter:
                    bit = litter[(nr, nc)]
                    new_mask |= (1 << bit)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # All litter collected
                if new_mask == all_mask:
                    return moves + 1

                state = (
                    nr,
                    nc,
                    new_energy,
                    new_mask
                )

                if state not in visited:

                    visited.add(state)

                    queue.append(
                        (
                            nr,
                            nc,
                            new_energy,
                            new_mask,
                            moves + 1
                        )
                    )

        return -1