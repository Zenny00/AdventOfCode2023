def read_maps(filename):
    maps = {}
    with open(filename, 'r') as file:
        current_map = None
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            if line.startswith('seeds:'):
                current_map = None
            elif line.startswith('seed-to-soil map:'):
                current_map = 'seed-to-soil'
            elif line.startswith('soil-to-fertilizer map:'):
                current_map = 'soil-to-fertilizer'
            elif line.startswith('fertilizer-to-water map:'):
                current_map = 'fertilizer-to-water'
            elif line.startswith('water-to-light map:'):
                current_map = 'water-to-light'
            elif line.startswith('light-to-temperature map:'):
                current_map = 'light-to-temperature'
            elif line.startswith('temperature-to-humidity map:'):
                current_map = 'temperature-to-humidity'
            elif line.startswith('humidity-to-location map:'):
                current_map = 'humidity-to-location'
            elif current_map:
                values = list(map(int, line.split()))
                if len(values) == 3:
                    maps.setdefault(current_map, []).append(tuple(values))
                else:
                    print(f"Ignoring invalid line: {line}")
    return maps

def convert(seed, maps):
    current_value = seed
    for map_name, map_data in maps.items():
        for dest_start, src_start, length in map_data:
            if current_value >= src_start and current_value < src_start + length:
                current_value = (current_value - src_start) % length + dest_start
                break
    return current_value

def find_lowest_location(seeds, maps):
    return min(convert(seed, maps) for seed in seeds)

filename = 'inputfile_1.txt'  # Replace with your actual filename
maps = read_maps(filename)

# Initial seed numbers
seeds = [79, 14, 55, 13]

# Find the lowest corresponding location number
lowest_location = find_lowest_location(seeds, maps)

print("Lowest Location Number:", lowest_location)
