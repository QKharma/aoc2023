from datetime import datetime
startTime = datetime.now()

class Beacon():

    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

    def __str__(self):
        return '[x: {}, y: {}, z:{}]'.format(self.x, self.y, self.z)

    def __repr__(self):
        return '[x: {}, y: {}, z:{}]'.format(self.x, self.y, self.z)

class Scanner():

    def __init__(self, scanner_id, beacons, parent=None, children=None):
        self.id = scanner_id

        self.x = 0
        self.y = 0
        self.z = 0

        if not parent:
            self.parent = None
        else:
            self.parent = parent

        if not children:
            self.children = []
        else:
            self.children = children

        self.beacons = []

        if type(beacons[0]) == Beacon:
            for beacon in beacons:
                self.beacons.append(Beacon([beacon.x,beacon.y,beacon.z]))
        else:
            for beacon in beacons:
                self.beacons.append(Beacon(beacon))

        self.calc_relative_positions()
        

    def __str__(self):
        return 'id: {}, pos: {},{},{}, parent: {}, children: {}, beacons: {}'.format(
            self.id, self.x, self.y, self.z, self.parent, self.children, self.beacons)

    def __repr__(self):
        return 'id: {}, pos: {},{},{}, parent: {}, children: {}, beacons: {}'.format(
            self.id, self.x, self.y, self.z, self.parent, self.children, self.beacons)

    def __copy__(self):
        return Scanner(self.id, self.beacons, parent=self.parent, children=self.children)

    def calc_relative_positions(self):
        self.relative_positions = []
        self.sort_beacons()
        for i in range(len(self.beacons)):
            for j in range(i, len(self.beacons)):
                if not i == j:
                    self.relative_positions.append([[
                    abs(self.beacons[i].x - self.beacons[j].x),
                    abs(self.beacons[i].y - self.beacons[j].y),
                    abs(self.beacons[i].z - self.beacons[j].z)
                    ],self.beacons[i], self.beacons[j]])

    def rotate_x(self):
        for beacon in self.beacons:
            x = beacon.x 
            y = beacon.z 
            z = -1*beacon.y
            beacon.x = x
            beacon.y = y
            beacon.z = z
        self.calc_relative_positions()

    def rotate_y(self):
        for beacon in self.beacons:
            x = beacon.z
            y = beacon.y
            z = -1*beacon.x
            beacon.x = x
            beacon.y = y
            beacon.z = z
        self.calc_relative_positions()

    def rotate_z(self):
        for beacon in self.beacons:
            x = beacon.y
            y = -1*beacon.x
            z = beacon.z
            beacon.x = x
            beacon.y = y
            beacon.z = z
        self.calc_relative_positions()

    def sort_beacons(self):
        self.beacons = sorted(self.beacons , key=lambda beacon: beacon.z)
        self.beacons = sorted(self.beacons , key=lambda beacon: beacon.y)
        self.beacons = sorted(self.beacons , key=lambda beacon: beacon.x)

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def get_all_rotations(self):
        r_scanner = self.__copy__()
        rotations = []

        for y in range(4):
            for x in range(4):
                rotations.append(r_scanner.__copy__())
                r_scanner.rotate_x()
            r_scanner.rotate_y()

        r_scanner.rotate_y()

        r_scanner.rotate_z()
        for y in range(4):
            rotations.append(r_scanner.__copy__())
            r_scanner.rotate_y()

        r_scanner.rotate_z()
        r_scanner.rotate_z()
        for y in range(4):
            rotations.append(r_scanner.__copy__())
            r_scanner.rotate_y()

        return rotations

class ScannerTree():
    
    def __init__(self, scanners):
        self.scanners = []

        for idx, beacons in enumerate(scanners):
            self.scanners.append(Scanner(idx, beacons))

        self.root = self.scanners[0]

        self.build_tree()

    def __str__(self):
        output = ''
        for scanner in self.scanners:
            output += '{}\n\n'.format(scanner)
        return output

    def compare_scanners(self, s_1: Scanner, s_2: Scanner, s_original=None):

        matching_beacons = set()

        #print([x[0] for x in s_1.relative_positions])

        for p_1 in s_1.relative_positions:
            for p_2 in s_2.relative_positions:
                if p_1[0] == p_2[0]:
                    matching_beacons.add(p_1[1])
                    matching_beacons.add(p_1[2])
                    print(len(matching_beacons))
                if len(matching_beacons) == 12:
                    s_2.set_parent(s_1.id)
                    if s_original:
                        s_original.add_child(s_2.id)
                    else:
                        s_1.add_child(s_2.id)
                    return True
        return False

    def check_potential_child(self, potential_child, next_scanners_to_check):
            print(next_scanners_to_check[0].id, potential_child.id)
            for idx, rotation in enumerate(next_scanners_to_check[0].get_all_rotations()):
                parent_found = self.compare_scanners(rotation, potential_child, s_original=next_scanners_to_check[0])
                if parent_found:
                    next_scanners_to_check.append(potential_child)
                    return
    
    def build_tree(self):
        next_scanners_to_check = [self.root]
        while next_scanners_to_check:
            for potential_child in self.scanners:
                if potential_child.parent == None and potential_child not in next_scanners_to_check and potential_child.id != 0:
                    self.check_potential_child(potential_child, next_scanners_to_check)
            next_scanners_to_check.pop(0)



file = []
with open('2021_day_19.txt') as f:
    file = f.read()
file = file.split('\n')

scanners = []

scanner = -1
for row in file:
    if 'scanner' in row:
        scanners.append([])
        scanner += 1
    else:
        if row:
            scanners[scanner].append([int(x) for x in row.split(',')])

scanner_tree = ScannerTree(scanners)

# for scanner in scanner_tree.scanners:
#     print([x[0] for x in scanner.relative_positions])
#     print('\n')

print(scanner_tree)

# def rotate_x(scanner):
#     rotated_scanner = []
#     for beacon in scanner:
#         rotated_scanner.append([beacon[0], beacon[2], -1*beacon[1]])
#     return rotated_scanner

# def rotate_y(scanner):
#     rotated_scanner = []
#     for beacon in scanner:
#         rotated_scanner.append([beacon[2], beacon[1], -1*beacon[0]])
#     return rotated_scanner

# def rotate_z(scanner):
#     rotated_scanner = []
#     for beacon in scanner:
#         rotated_scanner.append([beacon[1], -1*beacon[0], beacon[2]])
#     return rotated_scanner

# def sort_beacons(scanner):
#     scanner = sorted(scanner, key=lambda x: x[2])
#     scanner = sorted(scanner, key=lambda x: x[1])
#     scanner = sorted(scanner, key=lambda x: x[0])
#     return scanner

# def compare_scanners(scanner1, scanner2):

#     matching_beacons = set()

#     scanner1 = sort_beacons(scanner1)
#     scanner2 = sort_beacons(scanner2)

#     for i in range(len(scanner1)):
#         if i == 15 and not matching_beacons:
#             return
#         for j in range(i, len(scanner1)):
#             if i != j:
#                 sc1_difference = [scanner1[i][0] - scanner1[j][0], scanner1[i][1] - scanner1[j][1], scanner1[i][2] - scanner1[j][2]]
#                 for i2 in range(len(scanner2)):
#                     for j2 in range(i2, len(scanner2)):
#                         if i2 != j2:
#                             sc2_difference = [scanner2[i2][0] - scanner2[j2][0], scanner2[i2][1] - scanner2[j2][1], scanner2[i2][2] - scanner2[j2][2]]
#                             if sc1_difference == sc2_difference:
#                                 matching_beacons.add(','.join([str(x) for x in scanner1[i]]))
#                                 matching_beacons.add(','.join([str(x) for x in scanner1[j]]))
#                                 if len(matching_beacons) == 12:
#                                     return True
#     return False

# def check_all_rotations(scanner1, scanner2, i, j):
#     for y in range(4):
#         for x in range(4):
#             if compare_scanners(scanner1, scanner2):
#                 return [i, j]
#             scanner1 = rotate_x(scanner1)
#         scanner1 = rotate_y(scanner1)

#     scanner1 = rotate_y(scanner1)

#     scanner1 = rotate_z(scanner1)
#     for y in range(4):
#         if compare_scanners(scanner1, scanner2):
#             return [i, j]
#         scanner1 = rotate_y(scanner1)

#     scanner1 = rotate_z(scanner1)
#     scanner1 = rotate_z(scanner1)
#     for y in range(4):
#         if compare_scanners(scanner1, scanner2):
#             return [i, j]
#         scanner1 = rotate_y(scanner1)

# matching_scanners = []

# count = 0

# for i in range(len(scanners)):
#     for j in range(i+1, len(scanners)):
#         print(count)
#         count += 1
#         match = check_all_rotations(scanners[i],scanners[j], i, j)
#         if match:
#             matching_scanners.append(match)

# print(matching_scanners)

print(datetime.now() - startTime)