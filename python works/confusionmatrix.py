def calculate_accuracy(ground_truth_text, extracted_text):
    correct_count = 0
    total_count = len(ground_truth_text)

    for gt, extracted in zip(ground_truth_text, extracted_text):
        if gt.strip() == extracted.strip():
            correct_count += 1

    accuracy = (correct_count / total_count)*100
    return accuracy

# Example ground truth and extracted text (replace with actual values)
extracted_text = ["johiram","Divakar","vasudevan","sukumar","selva"]
ground_truth_text = ["jothiram","Divakar","vasudevan","sukumar","selva"]

accuracy = calculate_accuracy(ground_truth_text, extracted_text)
print(f"Accuracy: {accuracy}%")

def calculate_precision(extracted_text, ground_truth_text):
    # Count the number of characters that are both in the extracted text and the ground truth text
    common_characters = sum(1 for char in extracted_text if char in ground_truth_text)
    
    # Calculate precision
    precision = common_characters / len(extracted_text) if len(extracted_text) > 0 else 0
    return precision*100

# Example:
extracted_text = ["johiram","Divakar","vasudevan","sukumar","selva"]
ground_truth_text = ["jothiram","Divakar","vasudevan","sukumar","selva"]

precision = calculate_precision(extracted_text, ground_truth_text)
print(f"Precision: {precision}%")

def calculate_recall(extracted_text, ground_truth_text):
    # Count the number of characters that are both in the extracted text and the ground truth text
    common_characters = sum(1 for char in extracted_text if char in ground_truth_text)
    
    # Calculate recall
    recall = common_characters / len(ground_truth_text) if len(ground_truth_text) > 0 else 0
    return recall*100

# Example:
extracted_text =["johiram","Divakar","vasudevan","sukumar","selva"]
ground_truth_text = ["jothiram","Divakar","vasudevan","sukumar","selva"]

recall = calculate_recall(extracted_text, ground_truth_text)
print(f"Recall: {recall}%")

def calculate_f1_score(extracted_text, ground_truth_text):
    precision = calculate_precision(extracted_text, ground_truth_text)
    recall = calculate_recall(extracted_text, ground_truth_text)
    
    # Calculate F1-Score
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return f1_score*100

# Example:
extracted_text = ["johiram","Divakar","vasudevan","sukumar","selva"]
ground_truth_text = ["jothiram","Divakar","vasudevan","sukumar","selva"]

f1_score = calculate_f1_score(extracted_text, ground_truth_text)
print(f"F1-Score: {f1_score}%")
2 * (precision * recall) / (precision + recall)
print(f"2 * ({precision} * {recall}) / ({precision} + {recall})")