Mini Search Engine

This project is a simple text-based search engine designed to help locate specific keywords in a collection of text files. The search engine efficiently indexes documents and allows users to search for keywords, returning the documents and line numbers where the keywords are found.

Features

Inverted Index: Efficiently indexes each word in the text files for fast retrieval.

Search Functionality: Supports keyword search across multiple text files.

Line Number Tracking: Identifies the exact line numbers in each document where the keyword appears.

How to Use

Add Documents: Place your .txt files in the documents folder.

Run the Script: Execute the script to build the index and perform searches.

Search for Keywords: Enter a search query to find which documents contain your keywords and on which lines.

Example

Run the script and enter a search query like:

python search_engine.py

Input your search term, and the output will show results like:

Search Results with Line Numbers:

Document: example.txt
  Token 'example' found on lines: [1, 3]
  Token 'search' found on lines: [2]

Requirements

Python 3.x

Setup

Clone the repository.

Ensure your text files are placed in a folder named documents.

Install any necessary dependencies (if any).

git clone https://github.com/yourusername/mini-search-engine.git
cd mini-search-engine

Future Enhancements

Add support for boolean searches (AND, OR).

Include ranking based on keyword relevance.

Add a simple web interface for user-friendly searching.

License

This project is licensed under the MIT License.

