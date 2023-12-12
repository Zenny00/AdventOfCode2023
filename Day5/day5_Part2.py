def sourceToDestMap(source, lines):
    for line in lines:
        dest, start, span = line
        if source >= start and source < start+span:
            return (dest + (source-start))

    return source

if __name__ == "__main__":
    file = open('inputfile_1.txt', 'r')
    lines = file.read().splitlines()

    seed_indicies = [int(x) for x in lines[0].split('seeds: ')[1].split(' ')]

    seedToSoilLines = []
    soilToFertilizerLines = []
    fertilizerToWaterLines = []
    waterToLightLines = []
    lightToTemperatureLines = []
    temperatureToHumidityLines = []
    humidityToLocationLines = []

    for i in range(len(lines)):
        if 'seed-to-soil' in lines[i]:
            while lines[i]:
                if 'seed-to-soil' not in lines[i]:
                    seedToSoilLines.append([int(x) for x in lines[i].split(' ')])
                i += 1
        
        if 'soil-to-fertilizer' in lines[i]:
            while lines[i]:
                if 'soil-to-fertilizer' not in lines[i]:
                    soilToFertilizerLines.append([int(x) for x in lines[i].split(' ')])
                i += 1

        if 'fertilizer-to-water' in lines[i]:
            while lines[i]:
                if 'fertilizer-to-water' not in lines[i]:
                    fertilizerToWaterLines.append([int(x) for x in lines[i].split(' ')])
                i += 1

        if 'water-to-light' in lines[i]:
            while lines[i]:
                if 'water-to-light' not in lines[i]:
                    waterToLightLines.append([int(x) for x in lines[i].split(' ')])
                i += 1

        if 'light-to-temperature' in lines[i]:
            while lines[i]:
                if 'light-to-temperature' not in lines[i]:
                    lightToTemperatureLines.append([int(x) for x in lines[i].split(' ')])
                i += 1

        if 'temperature-to-humidity' in lines[i]:
            while lines[i]:
                if 'temperature-to-humidity' not in lines[i]:
                    temperatureToHumidityLines.append([int(x) for x in lines[i].split(' ')])
                i += 1

        if 'humidity-to-location' in lines[i]:
            while lines[i]:
                if 'humidity-to-location' not in lines[i]:
                    humidityToLocationLines.append([int(x) for x in lines[i].split(' ')])
                i += 1
                if (i == len(lines)):
                    break

    # do one range at a time
    minLocation = 9999999999999
    counter = 0
    for i in range(0, len(seed_indicies), 2):
        print(f'Progress: {(counter/(len(seed_indicies)))*100}%')
        start = seed_indicies[i]
        num = seed_indicies[i+1]
        mid = start + (seed_indicies[i+1]//2)
        values = [start, mid, mid, start+num]
        
        for j in range(0, len(values), 2):
            start = values[j]
            end = values[j+1]
            seeds = []
            for seed in range(start, end):
                seeds.append(seed)

            for seed in seeds:
                soil = sourceToDestMap(seed, seedToSoilLines)
                fertilizer = sourceToDestMap(soil, soilToFertilizerLines)
                water = sourceToDestMap(fertilizer, fertilizerToWaterLines)
                light = sourceToDestMap(water, waterToLightLines)
                temperature = sourceToDestMap(light, lightToTemperatureLines)
                humidity = sourceToDestMap(temperature, temperatureToHumidityLines)
                location = sourceToDestMap(humidity, humidityToLocationLines)

                if location < minLocation:
                    minLocation = location
            
        counter+=2

    print(minLocation)
