import re
import string
from bs4 import BeautifulSoup


def clean_text(text: str) -> str:
    """Cleans a raw text string by removing HTML, URLs, numbers,

    punctuation, and excessive whitespace.
    """
    text = text.lower()
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\d+", "", text)  # Fixed typo: changed \d+^ to \d+
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\W+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text

if __name__ == "__main__":
    file_path='/Users/aabhagajurel/PycharmProjects/PythonProject/spamMailDetectionFile'

try :
    with open(file_path, "r", encoding="utf-8") as file:
        lines= file.readlines()
    print("--- Running Clean Text Pipeline ---\n")
    cleaned_corpus = []
    for line in lines:
        cleaned = clean_text(line)
        if cleaned:  # Skip empty lines
            cleaned_corpus.append(cleaned)
            print(f"Original: {line.strip()}")
            print(f"Cleaned:  {cleaned}\n")
except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found. Please check the file name.")
except IsADirectoryError:
        print(f"Error: '{file_path}' is a folder, not a file. Include a filename at the end.")