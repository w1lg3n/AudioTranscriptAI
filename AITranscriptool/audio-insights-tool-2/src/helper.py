import nltk
from nltk.tokenize import sent_tokenize

# Ensure that the necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('punkt_tab')


def chunk_transcript(transcript, chunk_size):
    # Tokenize the text into sentences
    sentences = sent_tokenize(transcript)
    return [" ".join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]


# Function to merge dictionaries with list values
def merge_keywords_dictionaries(d1, d2):
    merged_dict = {**d1}
    for key, value_list in d2.items():
        if key in merged_dict:
            merged_dict[key].extend(value_list)
        else:
            merged_dict[key] = value_list
    return merged_dict
