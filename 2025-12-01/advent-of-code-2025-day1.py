import math

def part1(rotations):
    password = 0
    current_position = 50
    dial_limit = 100

    for rotation in rotations:
        direction = rotation[0]
        move = int(rotation[1::])

        for i in range(0, move):
            if current_position == 0 and direction == 'L':
                current_position = dial_limit -1
            elif current_position == 99 and direction == 'R':
                current_position = 0
            else:
                if direction == 'L':
                    current_position -= 1
                else:
                    current_position += 1
            
        if current_position == 0:
            password += 1
            
    print(f"Password: {password}")

    return password

def part2(rotations):
    password = 0
    current_position = 50
    dial_limit = 100
    for rotation in rotations:
        direction = rotation[0]
        move = int(rotation[1::])

        for i in range(0, move):
            if current_position == 0 and direction == 'L':
                current_position = dial_limit -1
            elif current_position == 99 and direction == 'R':
                current_position = 0
            else:
                if direction == 'L':
                    current_position -= 1
                else:
                    current_position += 1
            
            if current_position == 0:
                password += 1

    print(f"Password: {password}")

    return password

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.rstrip() for line in file]
    
if __name__ == "__main__":
    file_path = 'day1-input.txt'
    rotations = read_input(file_path)
    part1(rotations)
    part2(rotations)