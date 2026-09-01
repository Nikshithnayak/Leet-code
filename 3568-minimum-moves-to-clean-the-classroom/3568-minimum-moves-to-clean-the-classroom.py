from collections import deque


class Solution(object):
    def minMoves(self, classroom, energy):

        m = len(classroom)
        n = len(classroom[0])

        # Find start and litter
        litter = {}
        litter_count = 0

        sr = sc = 0

        for r in range(m):
            for c in range(n):

                if classroom[r][c] == 'S':
                    sr, sc = r, c

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        all_mask = (1 << litter_count) - 1

        # best[r][c][mask] = maximum remaining energy
        best = {}

        queue = deque()

        queue.append((sr, sc, energy, 0, 0))

        best[(sr, sc, 0)] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:

            r, c, remaining, mask, moves = queue.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Outside grid
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Need at least 1 energy to move
                if remaining == 0:
                    continue

                new_energy = remaining - 1
                new_mask = mask

                # Collect litter
                if (nr, nc) in litter:
                    bit = litter[(nr, nc)]
                    new_mask |= (1 << bit)

                # Reset area
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # All litter collected
                if new_mask == all_mask:
                    return moves + 1

                state = (nr, nc, new_mask)

                # IMPORTANT OPTIMIZATION:
                # Skip if we've already reached this state
                # with equal or more energy
                if state in best and best[state] >= new_energy:
                    continue

                best[state] = new_energy

                queue.append(
                    (nr, nc, new_energy, new_mask, moves + 1)
                )

        return -1