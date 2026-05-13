import csv
import os

def audit_dataset(file_path):
    """
    Simple audit tool to verify the presence of gender-neutral 
    honorifics in Amharic financial datasets.
    """
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    print(f"--- Starting Bias Audit for: {file_path} ---")
    
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            context = row['context']
            gold = row['gold_standard_inclusive_amharic']
            
            # Simple check for the 'u' (plural/honorific) ending vs 'e' (masculine singular)
            # Example: ፈቀደ (masculine) vs ፈቀዱ (inclusive/honorific)
            if "ዱ" in gold or "ሙ" in gold or "ን" in gold:
                status = "✅ INCLUSIVE"
            else:
                status = "⚠️ REVIEW NEEDED"
                
            print(f"[{context}] Status: {status} | Text: {gold}")

if __name__ == "__main__":
    # Path to the dataset we created earlier
    dataset_path = 'datasets/gender_bias_financial_amharic.csv'
    audit_dataset(dataset_path)
