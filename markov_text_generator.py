import random

# Sample input text (replace or load from file)
with open("my_text.txt", "r", encoding="utf-8") as f:
    text = f.read()


# Tokenize the text
words = text.split()

# Build the Markov chain (bi-gram model)
markov_chain = {}

for i in range(len(words) - 2):
    key = (words[i], words[i + 1])  # bi-gram key (word1, word2)
    next_word = words[i + 2]        # the word that follows the bi-gram
    if key not in markov_chain:
        markov_chain[key] = []
    markov_chain[key].append(next_word)

# Generate text
def generate_text(chain, start_pair, length=30):
    if start_pair not in chain:
        raise ValueError("The starting pair is not in the chain.")
    
    word1, word2 = start_pair
    result = [word1, word2]

    for _ in range(length):
        next_words = chain.get((word1, word2))
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        word1, word2 = word2, next_word  # shift window

    return ' '.join(result)

# Choose a random start pair from the chain
start = random.choice(list(markov_chain.keys()))

# Generate and print the result
generated = generate_text(markov_chain, start_pair=start)
print("\n📝 Generated Text:\n")
print(generated)
with open("generated_output.txt", "w", encoding="utf-8") as f:
    f.write(generated)

