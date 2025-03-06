import tracemalloc
import time


# Define functions here, for example:
def encode1(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + '#' + s
    return res

def decode1(s):
    res = []
    i = word_start = 0

    while i < len(s):
        start = 1 + (i := i + 1)
        if s[i] == '#':
            word_length = start + int(s[word_start:i])
            res.append(s[start:word_length])
            i = word_start = word_length
        
    return res
    
def encode2(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode2(s):
    res = []
    i = 0
    
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j
        
    return res

# Define variables here, for example:
strs = [
    "apple", "banana", "chocolate", "elephant", "giraffe", "moonlight", "ocean", "penguin", "quasar", "rainbow",
    "sunshine", "tornado", "umbrella", "volcano", "whisper", "xylophone", "yogurt", "zeppelin", "avocado", "butterfly",
    "caterpillar", "diamond", "evergreen", "fireworks", "glacier", "horizon", "island", "jellyfish", "kangaroo",
    "lightning", "mountain", "nebula", "octopus", "parachute", "quicksand", "rhinoceros", "starlight", "thunderstorm",
    "underwater", "vortex", "waterfall", "xenon", "yacht", "zodiac", "asteroid", "breeze", "comet", "dolphin",
    "enchanted", "fossil", "galaxy", "harpoon", "illuminate", "journey", "koala", "labyrinth", "meteor", "nostalgia"
]

# Benchmark function, modify as needed:
def benchmark(encode, decode, strs, iterations=1000):
    tracemalloc.start()
    start_time = time.time()
    
    for _ in range(iterations):
        decode(encode(strs))
    
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Current memory usage: {current / 1024:.2f} KB")
    print(f"Peak memory usage: {peak / 1024:.2f} KB")
    print(f"Execution time: {(end_time - start_time) * 1000:.3f} milliseconds", end = "\n\n")

# Example usage:
benchmark(encode1, decode1, strs)
benchmark(encode2, decode2, strs)
