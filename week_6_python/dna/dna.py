import csv
import sys


def stringSearch(STR, sequence):
    count = 0
    finalCount = 0
    i = 0
    while i < len(sequence):
        if (sequence[i:i+len(STR)]) == STR:
            count = count + 1
            if (sequence[i+len(STR):(i+len(STR)*2)]) != STR and count > finalCount:
                finalCount = count
                count = 0
            i = i + len(STR)
        else:
            if (count > finalCount):
                finalCount = count
            count = 0
            i = i + 1
    return finalCount


def main():

    if len(sys.argv) != 3:
        print("USAGE: python dna.py DATABASE.csv SEQUENCE.txt")
        sys.exit()

    with open(sys.argv[2]) as txtfile:
        sequence = txtfile.read()

    with open(sys.argv[1], newline='') as csvfile:
        DNA_dict = {}
        database = csv.DictReader(csvfile)
        rows = list(database)
        STRs = database.fieldnames[1:]
        for row in rows:
            for STR in STRs:
                finalCount = stringSearch(STR, sequence)
                DNA_dict[STR] = finalCount

    for row in rows:
        individual_dict = {STR: int(row[STR]) for STR in STRs}
        if individual_dict == DNA_dict:
            print(row['name'])
            break
    else:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
