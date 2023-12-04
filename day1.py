# Ugly solution to deal with case when two numbers share the same letters
numMap = {'one': 'o1e',
          'two': 't2o',
          'three': 't3e',
          'four': 'f4r',
          'five': 'f5e',
          'six': 's6x',
          'seven': 's7n',
          'eight': 'e8t',
          'nine': 'n9e',
          'zero': 'z0o'}

# Replace instances of spelled out numbers with their numerical counter part
def replaceNums(string):
    for key in numMap.keys():
        if key in string:
            string = string.replace(key, numMap[key])
    return string

# Get the calibration numbers for a given string
def getCalibration(string):
    first = -1
    last = -1
    for c in string:
        if c.isdigit():
            # We only adjust the first when it hasn't been changed
            if first == -1:
                first = c
            # Always adjust last
            last = c
           
    # Concat the two digits and return the value
    return int(str(first)+str(last))

if __name__ == "__main__":
    file1 = open('inputfile.txt', 'r')
    lines = file1.readlines()

    sum = 0
    for line in lines:
        line = str(replaceNums(line))
        output = getCalibration(line)
        sum += output
    print(sum)
