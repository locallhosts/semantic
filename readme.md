# Semantic Similarity

This project uses the spaCy library to calculate semantic similarity between words. The semantic.py script loads the medium English language model (en_core_web_md) by default, but you can also switch to the simpler language model (en_core_web_sm) by editing the script. The similarity between words is calculated using the cosine similarity metric.


# Installation
To run the project, you'll need to have Python 3 and the spaCy library installed on your machine. You can install spaCy using pip:

**pip install spacy**

You'll also need to download the English language model. To download the medium model, run:

**python -m spacy download en_core_web_md**

Or, to download the smaller model, run:

**python -m spacy download en_core_web_sm**



# Usage
To run the script, simply execute the semantic.py file:

The script will output the similarity between three target words (apple, banana, and orange) using the loaded spaCy model. You can edit the script to compare other words, or to switch to a different spaCy model

# Docker
If you have Docker installed, you can also run the project in a Docker container. First, build the Docker image:


**docker build -t semantic-similarity .**


Then, run the Docker container:
  docker run semantic-similarity




