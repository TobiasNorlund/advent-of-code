from collections import defaultdict
from functools import lru_cache

def get_cubes(brick) -> set:
    (x1, y1, z1), (x2, y2, z2) = brick
    cubes = set(
        (x, y, z)
        for x in range(x1, x2+1)
        for y in range(y1, y2+1)
        for z in range(z1, z2+1)
    )
    assert len(cubes) >= 1
    return cubes


def part_1():
    bricks = []
    file = "input.txt"
    for line in open(file):
        p1, p2 = line.strip().split("~")
        x1, y1, z1 = p1.split(",")
        x1, y1, z1 = int(x1), int(y1), int(z1)
        x2, y2, z2 = p2.split(",")
        x2, y2, z2 = int(x2), int(y2), int(z2)
        bricks.append(((min(x1, x2), min(y1, y2), min(z1, z2)), (max(x1, x2), max(y1, y2), max(z1, z2))))

    bricks = sorted(bricks, key=lambda b: b[0][2])

    all_cubes = set()
    for brick in bricks:
        cubes = get_cubes(brick)
        assert len(all_cubes.intersection(cubes)) == 0
        all_cubes.update(cubes)

    # try move all cubes down as much as possible
    for i in range(len(bricks)):
        (x1, y1, z1), (x2, y2, z2) = bricks[i]
        brick_cubes = get_cubes(bricks[i])

        # remove this brick's cubes from all_cubes
        for cube in brick_cubes:
            all_cubes.remove(cube)

        if z1 > 1:
            for delta_z in range(1, z1):
                if any((x, y, z-delta_z) in all_cubes for x, y, z in brick_cubes):
                    # we can move this brick down delta_z-1 levels
                    bricks[i] = (x1, y1, z1-(delta_z-1)), (x2, y2, z2-(delta_z-1))
                    break
            else:
                # Move to z = 1 level
                height = z2 - z1
                bricks[i] = (x1, y1, 1), (x2, y2, 1 + height)

        # add cubes back
        brick_cubes = get_cubes(bricks[i])
        assert len(all_cubes.intersection(brick_cubes)) == 0
        all_cubes.update(brick_cubes)

    # Now, check for every brick if it can be disintegrated
    tot_non_disitegratable = 0
    for i in range(len(bricks)):
        brick_cubes = get_cubes(bricks[i])
        # try removing brick i...
        for cube in brick_cubes:
            all_cubes.remove(cube)

        # ... and see if anything can be moved down
        for j in range(i+1, len(bricks)):

            non_disintegratable = False
            (x1, y1, z1), (x2, y2, z2) = bricks[j]
            candidate_cubes = get_cubes(bricks[j])
            
            if z1 == 1:
                # Already at bottom, this cannot move down
                continue
            
            # temporarity remove candidate cubes to see if it can be moved down
            for cube in candidate_cubes:
                all_cubes.remove(cube)

            for delta_z in range(1, z1):
                if any((x, y, z-delta_z) in all_cubes # and (x, y, z-delta_z) not in candidate_cubes 
                       for x, y, z in candidate_cubes):
                    # we can move this brick down delta_z-1 levels
                    if delta_z > 1:
                        non_disintegratable = True
                    break
            else:
                # Move to z = 1 level
                non_disintegratable = True

            all_cubes.update(candidate_cubes)

            if non_disintegratable:
                tot_non_disitegratable += 1
                break
        
        # add brick i back to all_cubes
        assert len(all_cubes.intersection(brick_cubes)) == 0
        all_cubes.update(brick_cubes)

    print(len(bricks) - tot_non_disitegratable)


def part_2():
    bricks = []
    file = "input.txt"
    for line in open(file):
        p1, p2 = line.strip().split("~")
        x1, y1, z1 = p1.split(",")
        x1, y1, z1 = int(x1), int(y1), int(z1)
        x2, y2, z2 = p2.split(",")
        x2, y2, z2 = int(x2), int(y2), int(z2)
        bricks.append(((min(x1, x2), min(y1, y2), min(z1, z2)), (max(x1, x2), max(y1, y2), max(z1, z2))))

    bricks = sorted(bricks, key=lambda b: b[0][2])

    all_cubes = {}
    for i, brick in enumerate(bricks):
        all_cubes.update({cube: i for cube in get_cubes(brick)})

    # try move all cubes down as much as possible
    for i in range(len(bricks)):
        (x1, y1, z1), (x2, y2, z2) = bricks[i]
        brick_cubes = get_cubes(bricks[i])

        # remove this brick's cubes from all_cubes
        for cube in brick_cubes:
            del all_cubes[cube]

        if z1 > 1:
            for delta_z in range(1, z1):
                if any((x, y, z-delta_z) in all_cubes for x, y, z in brick_cubes):
                    # we can move this brick down delta_z-1 levels
                    bricks[i] = (x1, y1, z1-(delta_z-1)), (x2, y2, z2-(delta_z-1))
                    break
            else:
                # Move to z = 1 level
                height = z2 - z1
                bricks[i] = (x1, y1, 1), (x2, y2, 1 + height)

        # add cubes back
        all_cubes.update({cube: i for cube in get_cubes(bricks[i])})

    # Build tree of which brick supports which
    support_tree = defaultdict(set)  # which nodes does i support upwards?
    for i, brick in reversed(list(enumerate(bricks))):
        brick_cubes = get_cubes(bricks[i])

        for x, y, z in brick_cubes:
            if (x, y, z+1) in all_cubes and (x, y, z+1) not in brick_cubes:
                support_tree[i].add(all_cubes[(x, y, z+1)])

    supportee_tree = {i: 
        tuple(j for j in range(len(bricks)) if i in support_tree[j])
        for i in range(len(bricks))
    }  # all nodes that support i

        
    def num_falling(node):
        """
        Get all nodes (inluding this) that would fall if this node fell
        """
        fallen = set([node])
        q = [n for n in support_tree[node]]
        while len(q) > 0:
            n = q.pop(0)

            # check if n will fall, i.e. if all its dependent nodes have fallen
            if all(sn in fallen for sn in supportee_tree[n]):
                fallen.add(n)
                q += support_tree[n]

        return len(fallen)

    
    tot = 0
    for i in reversed(range(len(bricks))):
        #nodes = set()
        num = num_falling(i)
        if num > 1:
            tot += num - 1 
        #for support_node in support_tree[i]:
        #    # if i is the only node supporting support_node
        #    if len(supportee_tree[support_node]) == 1:
        #        # then support_node will fall, and everything it solely supports
        #        #nodes.update(get_tot_support(support_node))
        #        tot += num_falling(support_node)
        #tot += len(nodes)

    print(tot)


if __name__ == "__main__":
    part_2()