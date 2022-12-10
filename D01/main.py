with open('input.txt', 'r') as input_data:
    sonar_readings = [int(line.strip()) for line in input_data.readlines()]


def check_increases(sonar_data, window_size):
    previous = []
    current = []
    increases = 0
    for reading in sonar_data:
        if len(current) < window_size:
            current.append(reading)
        else:
            current.pop(0)
            current.append(reading)

        if len(previous) >= window_size:
            if sum(current) > sum(previous):
                increases += 1

        previous = [number for number in current]
    return increases


print(f"Part 1: {check_increases(sonar_readings, 1)} increases")
print(f"Part 2: {check_increases(sonar_readings, 3)} increases")
