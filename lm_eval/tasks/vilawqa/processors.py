import random

def preprocess_vilawqa(doc):
    """
    Preprocess the ViLawQA dataset format.
    This function handles the dataset format and ensures proper formatting of options.
    """
    # Ensure we have exactly 4 options
    if len(doc["options"]) != 4:
        raise ValueError(f"Expected 4 options, got {len(doc['options'])}")

    # Ensure answer_index is valid
    if not 0 <= doc["answer_index"] < 4:
        raise ValueError(f"Invalid answer_index: {doc['answer_index']}")

    # Create a copy of options to avoid modifying the original
    options = list(doc["options"])

    # Shuffle options and update answer_index
    indexed_options = [(option, i) for i, option in enumerate(options)]
    random.shuffle(indexed_options)

    new_options = [item[0] for item in indexed_options]
    new_answer_index = [item[1] for item in indexed_options].index(doc["answer_index"])

    # Update the document
    doc["options"] = new_options
    doc["answer_index"] = new_answer_index

    return doc