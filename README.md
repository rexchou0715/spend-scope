# Spend-Scope 🧾

**Spend-Scope** is a personal finance project that helps you understand your spending habits by integrating and categorizing transactions from **ING** and **Revolut**. It cleans and unifies data from both banks, extracts useful fields like date components, and assigns a category to each transaction using a hand-crafted keyword dictionary.

---

## 💡 Why I Built This

I wanted to clearly understand my financial behavior by combining ING and Revolut data. This project helps me clean and structure those transactions, and categorize them to reveal where my money goes.

While it’s built for personal use, I’ve included **anonymized sample data** so others can practice with it. If you use ING or Revolut, you can adapt it to your own finances too!

---

## 📂 Data Sources

- `data/raw/ing_bank_statement_sample.csv`
- `data/raw/revolut_bank_statement_sample.csv`

The raw data includes fields like:

### ING
- `Date`, `Name / Description`, `Debit/Credit`, `Amount (EUR)`

### Revolut
- `Type`, `Started Date`, `Completed Date`, `Description`, `Amount`

---

## 🧼 Cleaning Pipeline

The pipeline (in `main.ipynb`) performs the following:

1. **Date ➝ Year, Month, Day**
2. **Price format ➝** `14,95` ➝ `14.95`
3. **Transaction Name cleaning ➝** remove special characters like `*`, `/`
4. **Categorization ➝** uses a custom dictionary in `category_keywords.py`

The cleaned output is saved in:  
data/processed/cleaned_transactions.csv


---

## 🔖 Categorization

Categorization is based on **hand-written keyword rules** stored in `category_keywords.py`. Transactions are matched to categories like:

- Groceries, Dining, Transportation, Entertainment
- Shopping (Clothing, Electronics, etc.)
- Utilities, Rent, Medical
- Income types (Salary, Refund, Top Up, etc.)

Unmatched entries are labeled as `"Uncategorized"`.

---

## 🚀 How to Use

1. Clone this repository.
2. Install the required dependencies:
    ```bash
    pip install pandas notebook
    ```
3. Run `main.ipynb` to clean and categorize the transactions.
4. View the result in `data/processed/`.

> 💡 I use the output in **Tableau** to build visual dashboards.

---

## ⚠️ Known Limitations

- Not scalable — based on fixed rules and keywords
- No ML or fuzzy matching (yet)
- Unknown transactions are not automatically categorized

---

## 🔮 Future Plans

- Add **language model (LLM) API** to suggest categories for unknown transactions
- Explore more automated or intelligent categorization methods

---

## 📚 License

This project is shared for learning and personal finance tracking. The included sample data is anonymized and provided only for practice purposes.

---

## 🙌 Contributions

Feel free to fork, adapt, or expand the keyword list — especially if you're also using ING or Revolut!
