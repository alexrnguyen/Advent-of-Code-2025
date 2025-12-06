def main():
    file_path = 'day1-input.txt'
    rotations = read_input(file_path)
    password = 0
    current_position = 50
    dial_limit = 100

    for rotation in rotations:
        direction = rotation[0]
        move = int(rotation[1::])
        relative_rotation = move % dial_limit
        if direction == 'L':
            if current_position - relative_rotation < 0:
                current_position = dial_limit - abs(relative_rotation - current_position)
            else:
                current_position = current_position - relative_rotation
        else:
            if current_position + relative_rotation > dial_limit - 1:
                current_position = current_position + relative_rotation - dial_limit
            else:
                current_position = current_position + relative_rotation

        if current_position == 0:
            password += 1
            
    print(f"Password: {password}")

    return password

def read_input(file_path):
    with open(file_path, 'r') as file:
    # rstrip() removes trailing whitespace, including '\\n'
        return [line.rstrip() for line in file]
    


if __name__ == "__main__":
    main()