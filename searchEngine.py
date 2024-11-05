import os 
import re 
from collections import defaultdict

DOCUMENT_FOLDER = "documents"

def load_documents():
    documents = {}
    for filename in os.listdir(DOCUMENT_FOLDER):
        if filename.endswith(".txt"):
            with open(os.path.join(DOCUMENT_FOLDER, filename), "r") as file:
                documents[filename] = file.read()
    return documents


def tokenize(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

def tokenize_with_lines(text):
    tokens_with_lines = []
    lines = text.splitlines()
    for line_number, line in enumerate(lines, start=1):
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            tokens_with_lines.append((word, line_number))
    return tokens_with_lines

documents = load_documents()
tokenized_documents = {filename: tokenize_with_lines(content) for filename, content in documents.items()}


def build_inverted_index_with_lines(tokenized_documents):
    inverted_index = defaultdict(lambda: defaultdict(set))
    for filename, tokens_with_lines in tokenized_documents.items():
        for token, line_number in tokens_with_lines:
            inverted_index[token][filename].add(line_number)
    return inverted_index

inverted_index_with_lines = build_inverted_index_with_lines(tokenized_documents)


def search_with_lines(query, inverted_index):
    tokens = tokenize(query)
    results = defaultdict(lambda: defaultdict(set))

    for token in tokens:
        if token in inverted_index:
            for doc, lines in inverted_index[token].items():
                results[doc][token].update(lines)
    return results

query = input("Search for: ")
results = search_with_lines(query, inverted_index_with_lines)

print("Search Results with Line Numbers:")
for doc, tokens in results.items():
    print(f"\nDocument: {doc}")
    for token, lines in tokens.items():
        print(f"  Token '{token}' found on lines: {sorted(lines)}")

