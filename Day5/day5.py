def sourceToDestMap(sources, lines):
    output = []
    for source in sources:
        found = False
        for line in lines:
            dest, start, span = [int(x) for x in line.split(' ')]
            if source >= start and source < start+span:
                output.append(dest + (source-start))
                found = True
        if not found:
            output.append(source)

    return output

if __name__ == "__main__":
    file = open('inputfile_1.txt', 'r')
    lines = file.read().splitlines()

    seeds = [int(x) for x in lines[0].split('seeds: ')[1].split(' ')]

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
                seedToSoilLines.append(lines[i])
                i += 1
            seedToSoilLines = seedToSoilLines[1:]
        
        if 'soil-to-fertilizer' in lines[i]:
            while lines[i]:
                soilToFertilizerLines.append(lines[i])
                i += 1
            soilToFertilizerLines = soilToFertilizerLines[1:]

        if 'fertilizer-to-water' in lines[i]:
            while lines[i]:
                fertilizerToWaterLines.append(lines[i])
                i += 1
            fertilizerToWaterLines = fertilizerToWaterLines[1:]

        if 'water-to-light' in lines[i]:
            while lines[i]:
                waterToLightLines.append(lines[i])
                i += 1
            waterToLightLines = waterToLightLines[1:]

        if 'light-to-temperature' in lines[i]:
            while lines[i]:
                lightToTemperatureLines.append(lines[i])
                i += 1
            lightToTemperatureLines = lightToTemperatureLines[1:]

        if 'temperature-to-humidity' in lines[i]:
            while lines[i]:
                temperatureToHumidityLines.append(lines[i])
                i += 1
            temperatureToHumidityLines = temperatureToHumidityLines[1:]

        if 'humidity-to-location' in lines[i]:
            while lines[i]:
                humidityToLocationLines.append(lines[i])
                i += 1
                if (i == len(lines)):
                    break
            humidityToLocationLines = humidityToLocationLines[1:]

    soils = sourceToDestMap(seeds, seedToSoilLines)
    fertilizers = sourceToDestMap(soils, soilToFertilizerLines)
    waters = sourceToDestMap(fertilizers, fertilizerToWaterLines)
    lights = sourceToDestMap(waters, waterToLightLines)
    temperatures = sourceToDestMap(lights, lightToTemperatureLines)
    humidities = sourceToDestMap(temperatures, temperatureToHumidityLines)
    locations = sourceToDestMap(humidities, humidityToLocationLines)

    print(min(locations))
