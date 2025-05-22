import streamlit as st

st.set_page_config(page_title="Smart Tax Refund Estimator")

st.title("🧾 Smart Tax Refund Estimator")
st.markdown("Estimate your refund instantly using basic tax info 👇")

income = st.number_input("Enter your total income ($)", min_value=0)
withheld = st.number_input("Enter total federal tax withheld ($)", min_value=0)
status = st.selectbox("Filing Status", ["single", "head_of_household", "married"])

def estimate_refund(income, withheld, filing_status):
    deductions = {"single": 13850, "head_of_household": 20800, "married": 27700}
    taxable_income = max(0, income - deductions.get(filing_status, 0))
    tax = taxable_income * 0.1
    return withheld - tax

if st.button("Estimate My Refund"):
    refund = estimate_refund(income, withheld, status)
    if refund >= 0:
        st.success(f"🎉 You may receive a refund of: **${refund:,.2f}**")
    else:
        st.error(f"⚠️ You may owe: **${-refund:,.2f}**")
