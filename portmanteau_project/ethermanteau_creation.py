import itertools
import syllables

def generate_portmanteaus(words):
    # Define a set to store the portmanteau words
    portmanteaus = set()

    # Generate all possible combinations of two words
    combinations = itertools.combinations(words, 2)

    # Iterate over the combinations and generate portmanteaus
    for combo in combinations:
        word1, word2 = combo
        for i in range(1, len(word2)):
            portmanteau = word1 + word2[i:]
            if len(portmanteau) > 2 and syllables.estimate(portmanteau) <= 3:
                portmanteaus.add(portmanteau)

    return portmanteaus

def main():
    # Define a list of words related to the Ethereum ecosystem
    words = ['ethereum', 'smart', 'contracts', 'decentralized', 'dapps', 'tokens', 'blockchain', 'crypto', 'finance', 'nft']

    # Generate portmanteau words
    portmanteaus = generate_portmanteaus(words)

    # Write the portmanteaus to the file
    with open('ethermanteau.txt', 'w') as file:
        for portmanteau in portmanteaus:
            file.write(portmanteau + '\n')

    print("Portmanteaus written to ethermanteau.txt")

if __name__ == '__main__':
    main()
