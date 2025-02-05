from nltk import precision, recall, f_measure

def evaluate_parser(parser, test_sentences):
    total_precision, total_recall, total_f1 = 0, 0, 0
    num_samples = len(test_sentences)

    for sentence in test_sentences:
        parsed_tree = parser(sentence)
        
        # For simplicity, assume that we have a predefined gold-standard tree for comparison
        # (In a real-world scenario, this would be retrieved from a treebank)
        gold_tree = get_gold_standard_tree(sentence)
        
        if parsed_tree:
            total_precision += precision(gold_tree, parsed_tree)
            total_recall += recall(gold_tree, parsed_tree)
            total_f1 += f_measure(gold_tree, parsed_tree)

    precision_score = total_precision / num_samples
    recall_score = total_recall / num_samples
    f1_score = total_f1 / num_samples
    
    return precision_score, recall_score, f1_score

def get_gold_standard_tree(sentence):
    # Placeholder for retrieving the gold-standard tree for comparison.
    # This is usually done by matching the sentence to its treebank equivalent.
    pass
