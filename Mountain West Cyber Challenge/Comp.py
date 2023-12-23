"""
Sari I. Younan
02/12/2023 13:32:48
Comp.py
"""


def processLog(path):
    idCounts = {}

    with open(path, 'r') as file:
        for line in file:
            # Split the line by whitespace
            parts = line.split()

            # Extract the ID part after the '#'
            if len(parts) > 1:
                idPart = parts[1].split('#')[0]

                idCounts[idPart] = idCounts.get(idPart, 0) + 1

    # Rank the ID codes based on ascending number of occurrences
    rankedIds = sorted(idCounts, key=idCounts.get)

    print(f'\nOpen door happened once and closed door happened once\n\n{chr(0x2234)} Door code ID must repeat twice '
          f'at most OR open door and closed door codes must repeat one time each\n')

    # Print the ranked IDs and their occurrences
    for rank, idCode in enumerate(rankedIds, start=1):
        occurrences = idCounts[idCode]
        print(f'Rank {rank}: ID {idCode} - Occurrences: {occurrences}')


filePath = '/Users/syounan/Downloads/CAN.log'
processLog(filePath)
