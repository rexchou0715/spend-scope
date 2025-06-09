# Spend-Scope 🧾

**Spend-Scope** is a semi-automated personal finance tool that classifies your transactions from **ING** and **Revolut** using a combination of keyword rules, fuzzy matching, and a language model (LLM) fallback. It's designed to give you a clearer view of your spending patterns with minimal manual effort.

---

## 💡 Why I Built This

I wanted to deeply understand my financial behavior by integrating ING and Revolut data and categorizing each transaction meaningfully. Manual categorization was slow and error-prone — this system automates that process while still allowing manual control where needed.

---

## 📂 Data Sources

Transactions are read from the following sources:

* `data/raw/ing_bank_statement_sample.csv`
* `data/raw/revolut_bank_statement_sample.csv`
* `data/processed/cleaned_transactions_previous.csv` (used for appending new entries)

Each file has a different structure, and Spend-Scope handles normalization internally.

---

## 🧼 Cleaning & Transformation Pipeline

### ING:

* Converts `Date` to `Year`, `Month`, `Day`
* Converts `14,95` ➝ `14.95`
* Maps `Debit/Credit` to negative/positive amount
* Cleans `Name / Description` and normalizes it

### Revolut:

* Uses `Completed Date` as transaction date
* Maps positive/negative amount to credit/debit
* Normalizes description as name

---

## 🔍 Categorization Logic

Each transaction is classified through these steps:

1. **Normalize Name** ➝ Lowercase + remove special characters
2. **Fuzzy Matching** against keyword rules (using `rapidfuzz`)
3. If no match:

   * Add to pending batch (credit or debit)
   * When batch reaches threshold (e.g., 15), send to **Gemini API** for classification
4. LLM response adds a new entry to `rules_credit.json` or `rules_debit.json` using `add_to_keyword_rules()`.

---

## 🧠 Rules Engine

Keyword rules are stored in JSON:

```json
"bagels&be": [
    {
        "Category": "Food & Dining",
        "Subcategory": "Restaurants",
        "Country": [
        "Netherlands"
        ],
        "City": [
        "Eindhoven"
        ],
        "Original Name": [
        "CCV*Lieshout bagels&be EINDHOVEN"
        ],
        "Flags": {
        "lock_location": false,
        "manual_check": true
        }   
    }   
]
```

### Flags:

* `manual_check: true` ➝ Do not update this rule anymore
* `lock_location: true` ➝ Skip updating country/city fields

---

## 🚀 How to Use

1. Clone the repo:

   ```bash
   git clone https://github.com/rexchou0715/spend-scope.git
   cd spend-scope
   ```

2. Install dependencies:

   ```bash
   pip install pandas rapidfuzz openai
   ```

3. Run `main.ipynb` (e.g., `main.py` or `main.ipynb`)

4. View results in:

   * `data/processed/cleaned_transactions.csv`
   * Rules: `rules_credit.json`, `rules_debit.json`
   * Unlabeled entries are saved as pending and optionally sent to LLM

---

## 🧪 Example Match Flow

1. Name: `"Revolut**8458* Dublin IRL"`
2. Normalize ➝ `"revolut"`
3. Match rule from `rules_debit.json`
4. If flag `manual_check = true`, skip all updates

---


## 📌 Known Limitations

* Still needs occasional manual review
* Gemini API requires batching
* Rules can grow large and may need pruning

---

## 🌱 Future Plans

* Integrate rule priority / expiry logic
* Auto-suggest edits based on user corrections
* Add category confidence score

---

## 📚 License

This is a personal tool released for learning purposes. Sample data is anonymized.


