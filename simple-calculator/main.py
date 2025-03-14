import streamlit as st

def main():
    st.title("Simple Calculator 🧮")
    st.write("This is a simple calculator app built with Streamlit.")
    st.write("Enter two numbers and select an operation to see the result.")

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter the first number 🔢:")
    with col2:
        num2 = st.number_input("Enter the second number 🔢:")

    operation = st.selectbox("Select an operation 🔢:", ["Add (+)", "Subtract(-)", "Multiply(x)", "Divide(\)"])

    if st.button("Calculate 🧮"):
        try:
            if operation == "Add (+)":
                symbol = "+"
                result = num1 + num2
                st.write(f"The sum of {num1} and {num2} is {num1 + num2}")
            elif operation == "Subtract(-)":
                symbol = "-"
                result = num1 - num2
                st.write(f"The difference of {num1} and {num2} is {num1 - num2}")
            elif operation == "Multiply(x)":
                symbol = "x"
                result = num1 * num2
                st.write(f"The product of {num1} and {num2} is {num1 * num2}")
            else :
                if operation == "Divide(\)":
                    if num2 == 0:
                        st.error("Error: Division by zero is not allowed.")
                    else:    
                      symbol = "/"
                      result = num1 / num2
                      st.write(f"The quotient of {num1} and {num2} is {num1 / num2}")
            st.success(f"{num1} {symbol} {num2} = {result}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

                    
if __name__ == "__main__":
    main()
                