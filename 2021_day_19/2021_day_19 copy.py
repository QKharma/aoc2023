from datetime import datetime
startTime = datetime.now()

class Beacon():

    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

class Scanner():

    def __init__(self, scanner_id, beacons):
        self.id = scanner_id

        self.x = 0
        self.y = 0
        self.z = 0

        self.beacons = beacons

    def rotate_x(self):

        for beacon in self.beacons:
            rotated_scanner.append([beacon[0], beacon[2], -1*beacon[1]])
        return rotated_scanner

    def rotate_y(self):
        for beacon in scanner:
            rotated_scanner.append([beacon[2], beacon[1], -1*beacon[0]])
        return rotated_scanner

    def rotate_z(self):
        for beacon in scanner:
            rotated_scanner.append([beacon[1], -1*beacon[0], beacon[2]])
        return rotated_scanner

class ScannerTree():
    
    def __init__(self, scanner):
        self.root = scanner

    

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

def rotate_x(scanner):
    rotated_scanner = []
    for beacon in scanner:
        rotated_scanner.append([beacon[0], beacon[2], -1*beacon[1]])
    return rotated_scanner

def rotate_y(scanner):
    rotated_scanner = []
    for beacon in scanner:
        rotated_scanner.append([beacon[2], beacon[1], -1*beacon[0]])
    return rotated_scanner

def rotate_z(scanner):
    rotated_scanner = []
    for beacon in scanner:
        rotated_scanner.append([beacon[1], -1*beacon[0], beacon[2]])
    return rotated_scanner

def sort_beacons(scanner):
    scanner = sorted(scanner, key=lambda x: x[2])
    scanner = sorted(scanner, key=lambda x: x[1])
    scanner = sorted(scanner, key=lambda x: x[0])
    return scanner

def compare_scanners(scanner1, scanner2):

    matching_beacons = set()

    scanner1 = sort_beacons(scanner1)
    scanner2 = sort_beacons(scanner2)

    for i in range(len(scanner1)):
        if i == 15 and not matching_beacons:
            return
        for j in range(i, len(scanner1)):
            if i != j:
                sc1_difference = [scanner1[i][0] - scanner1[j][0], scanner1[i][1] - scanner1[j][1], scanner1[i][2] - scanner1[j][2]]
                for i2 in range(len(scanner2)):
                    for j2 in range(i2, len(scanner2)):
                        if i2 != j2:
                            sc2_difference = [scanner2[i2][0] - scanner2[j2][0], scanner2[i2][1] - scanner2[j2][1], scanner2[i2][2] - scanner2[j2][2]]
                            if sc1_difference == sc2_difference:
                                matching_beacons.add(','.join([str(x) for x in scanner1[i]]))
                                matching_beacons.add(','.join([str(x) for x in scanner1[j]]))
                                if len(matching_beacons) == 12:
                                    return True
    return False

def check_all_rotations(scanner1, scanner2, i, j):
    for y in range(4):
        for x in range(4):
            if compare_scanners(scanner1, scanner2):
                return [i, j]
            scanner1 = rotate_x(scanner1)
        scanner1 = rotate_y(scanner1)

    scanner1 = rotate_y(scanner1)

    scanner1 = rotate_z(scanner1)
    for y in range(4):
        if compare_scanners(scanner1, scanner2):
            return [i, j]
        scanner1 = rotate_y(scanner1)

    scanner1 = rotate_z(scanner1)
    scanner1 = rotate_z(scanner1)
    for y in range(4):
        if compare_scanners(scanner1, scanner2):
            return [i, j]
        scanner1 = rotate_y(scanner1)

matching_scanners = []

count = 0

for i in range(len(scanners)):
    for j in range(i+1, len(scanners)):
        print(count)
        count += 1
        match = check_all_rotations(scanners[i],scanners[j], i, j)
        if match:
            matching_scanners.append(match)

print(matching_scanners)

print(datetime.now() - startTime)
