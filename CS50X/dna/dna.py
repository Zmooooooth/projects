import csv
import sys
import string


def main():
    if len(sys.argv) != 3:
        exit("Usage: python dna.py <file1> <file2>")
    try:
        open(sys.argv[1], "r")
    except:
        exit("Invalid database path")
    try:
        open(sys.argv[2], "r")
    except:
        exit("Invalid sequence path")
    with open(sys.argv[1], "r") as file:
        rows = []
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)
    with open(sys.argv[2], "r") as file:
        sequence = file.read()
    dict_list = []
    for name in fieldnames:
        if name == "name":
            pass
        else:
            result = longest_match(sequence, name)
            dict = {
                f"{name}": f"{result}"
            }
            dict_list.append(dict)
    for dictionary in rows:
        if all(dictionary[key] == value for dict in dict_list for key, value in dict.items()):
            print(f"{dictionary['name']}.")
            return 0
    print("No match.")
    return 0


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
