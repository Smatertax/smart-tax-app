import pandas as pd

def estimate_refund(income, withheld, filing_status, dependents):
    standard_deduction = {
        "single": 13850,
        "head_of_household": 20800,
        "married": 27700
    }
    taxable_income = max(0, income - standard_deduction.get(filing_status, 0))
    est_tax = taxable_income * 0.1
    refund = withheld - est_tax
    return round(refund, 2)

# Sample usage
if __name__ == "__main__":
    sample = {
        "income": 45000,
        "withheld": 5200,
        "filing_status": "single",
        "dependents": 1
    }
    result = estimate_refund(**sample)
    print("Estimated refund:", result)
