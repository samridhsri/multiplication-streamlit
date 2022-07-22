import streamlit as st

def main():
    st.header("Multiplication of two numbers:")
    num1 = st.number_input("first number")
    num2 = st.number_input("second number")

    st.header(str(num1*num2))

    st.text("Made by Samridh Srivastava")

if __name__ == "__main__":
    main()