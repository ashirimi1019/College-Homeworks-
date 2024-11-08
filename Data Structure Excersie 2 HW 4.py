def find_repeated_dna_sequences(s):
    sequences = {}  # Use a dictionary to keep track of sequence counts
    repeated = set()  # Set to store repeated sequences
    
    for i in range(len(s) - 9):
        seq = s[i:i+10]
        if seq in sequences:
            repeated.add(seq)
        else:
            sequences[seq] = 1
    
    return list(repeated)

def test_find_repeated_dna_sequences():
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    expected_output = ['CCCCCAAAAA', 'AAAAACCCCC']
    assert find_repeated_dna_sequences(s) == expected_output, f"Expected: {expected_output}, Got: {find_repeated_dna_sequences(s)}"

if __name__ == "__main__":
    # Run the test case
    test_find_repeated_dna_sequences()
    print("Test case passed.")
