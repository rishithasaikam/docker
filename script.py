import os
import re
import socket
from collections import Counter

# Define paths inside the container
input_dir = "/home/data"
output_file = os.path.join(input_dir, "result.txt")
file1 = os.path.join(input_dir, "IF.txt")
file2 = os.path.join(input_dir, "AlwaysRememberUsThisWay.txt")

# Function to read and count words
def count_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        words = re.findall(r"\b\w+'\w+|\w+\b", f.read().lower())  # Handles contractions
    return words, Counter(words)

# Process test.txt
words1, counter1 = count_words(file1)
total_words1 = len(words1)
top_3_words1 = counter1.most_common(3)

# Process AlwaysRememberUsThisWay.txt
words2, counter2 = count_words(file2)
total_words2 = len(words2)
top_3_words2 = counter2.most_common(3)

# Get container IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Ensure output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Write results to file
with open(output_file, "w") as f:
    f.write(f"Total words in test.txt: {total_words1}\n")
    f.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words2}\n")
    f.write(f"Grand total of words: {total_words1 + total_words2}\n")
    f.write(f"Top 3 words in test.txt: {top_3_words1}\n")
    f.write(f"Top 3 words in AlwaysRememberUsThisWay.txt (handling contractions): {top_3_words2}\n")
    f.write(f"Container IP Address: {ip_address}\n")

# Print the output
with open(output_file, "r") as f:
    print(f.read())
