# from pdfloader import textss
import re

def clean_text(text):

    text = re.sub(
        r'https?://\S+',
        '',
        text
    )

    text = re.sub(
        r'\d+/\d+/\d+.*?AWS Customer Agreement',
        '',
        text
    )

    return text


def chunk_text(text,
               chunk_size=500,
               chunk_overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(
            text[start:end]
        )

        start += chunk_size - chunk_overlap

    return chunks
# tex = clean_text(textss)
# chunks = chunk_text(tex)