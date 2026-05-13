# Amharic Prompt Engineering Recipes
This collection provides optimized prompt templates for achieving high-fidelity Amharic outputs from frontier models like Qwen-72B and Llama-3.

## 🧪 Recipe 1: Contextual Disambiguation
Objective: To prevent the model from defaulting to "Ge'ez" or archaic vocabulary when modern Amharic is required.

### The Prompt Structure:

Plaintext
[Role]: Expert Amharic Linguist
[Task]: Translate the following financial document into modern, standard Amharic used in Addis Ababa.
[Constraint]: Avoid archaic Ge'ez verb forms. Use phonetic normalization for homophones.
[Input]: {English Text}

## 🧪 Recipe 2: Gender-Inclusive Financial Querying
Objective: To ensure occupation-based queries do not default to masculine pronouns.

### The Prompt Structure:

Plaintext
[Task]: Describe the role of a {Occupation} in the Ethiopian banking sector.
[Constraint]: Use gender-neutral phrasing (e.g., 'እሳቸው' or inclusive collective nouns) and ensure both male and female professional contexts are acknowledged.
Status: Active Research – Testing across Qwen-7B and Qwen-72B.
