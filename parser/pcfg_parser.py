import nltk
from nltk.grammar import PCFG
from nltk.parse import EarleyChartParser
import streamlit as st

def parse_sentence(sentence: str):
    # Define the probabilistic context-free grammar (PCFG)
    grammar = """
    S -> NP VP [1.0]
    VP -> V NP [0.5] | V NP PP [0.5]
    V -> "saw" [0.5] | "ate" [0.5]
    NP -> "John" [0.33] | "Mary" [0.33] | "I" [0.34]
    PP -> P NP [1.0]
    P -> "with" [1.0]
    """

    # Create a probabilistic context-free grammar (PCFG) from the string
    pcfg = PCFG.fromstring(grammar)

    # Initialize the parser
    parser = EarleyChartParser(pcfg)
    
    # Tokenize the input sentence
    sentence_tokens = sentence.split()

    try:
        # Parse the sentence
        parsed_trees = list(parser.parse(sentence_tokens))

        if parsed_trees:
            # Return the list of parsed trees
            return parsed_trees

        else:
            return "No parse tree found."

    except ValueError as e:
        return f"Parsing error: {e}"

# Streamlit code to interact with the user
input_sentence = st.text_input("Enter a sentence:", key="unique_input_key")
if input_sentence:
    parsed_trees = parse_sentence(input_sentence)
    
    if isinstance(parsed_trees, list):
        for tree in parsed_trees:
            st.text(str(tree))  # Display each parsed tree as a string
    else:
        st.text(parsed_trees)  # Display the error message or "No parse tree found"
