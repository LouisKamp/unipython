import numpy as np


def closest_match(query: str, collection: str):
    # Splits the word into an array
    words = np.array(collection.split(" "))

    # Initialize array stuff
    matchLettersArray = np.zeros(len(words))
    overLettersArray = np.zeros(len(words))

    # Loop every word in collection
    for i, word in enumerate(words):
        matchChars = 0
        # Count the number of matched chars and letters not matching
        for j, letter in enumerate(query):
            if letter == word[j]:
                matchChars += 1
            else:
                overLettersArray[i] = len(word[j::])
                break
        matchLettersArray[i] = matchChars

    # Find the max value
    maxMatchLetters = np.amax(matchLettersArray)

    # Find the indexes to the max value
    candidatesLettersMatchIndex = matchLettersArray == maxMatchLetters

    # Find the min number of not matching letters and filtering for max match letters
    minOverLetters = np.amin(overLettersArray[candidatesLettersMatchIndex])

    candidatesMinOverLettersIndex = (
        overLettersArray[candidatesLettersMatchIndex] == minOverLetters
    )

    # Return the first match with max number of match letters and min number of non matching letters
    return words[candidatesLettersMatchIndex][candidatesMinOverLettersIndex][0]

