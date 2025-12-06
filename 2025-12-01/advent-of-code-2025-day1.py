def main():
    """ Main program """
    # Read input
    file_path = 'day1-input.txt'
    with open(file_path, 'r') as file:
    # rstrip() removes trailing whitespace, including '\\n'
        rotations = [line.rstrip() for line in file]
    print(rotations)

    password = 0
    currentPosition = 50
    highNum = 100
    for rotation in rotations:
        direction = rotation[0]
        move = int(rotation[1::])
        x = move % highNum
        if direction == 'L':
            if currentPosition - x < 0:
                currentPosition = highNum - abs(x - currentPosition)
            else:
                currentPosition = currentPosition - x
        else: # R
            if currentPosition + x > highNum - 1:
                currentPosition = (currentPosition + x - highNum)
            else:
                currentPosition = currentPosition + x

        if currentPosition == 0:
            password += 1
            
    print(f"Password: {password}")

    return password

if __name__ == "__main__":
    main()