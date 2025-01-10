import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st
import google.generativeai as genai


_ = load_dotenv(find_dotenv())
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def main():
    st.set_page_config(page_title="SQL Query Generator 👨🏼‍💻", page_icon=":robot:")
    st.markdown(
        """
            <div style="text-align: center;">
                <h1>SQL Query Generator 👨🏼‍💻 🤖</h1>
                <h3>I can generate SQL queries for you!!!</h3>
                <h4>With Good Explaination as well!!!</h4>
                <p>This tool is a simple tool that allows you to generate SQL queries based on your prompts.</p>

            </div>
        
        """,
        unsafe_allow_html=True,
    )

    text_input = st.text_area("Enter your query here: ")

    submit = st.button("Generate SQL Query")

    if submit:
        with st.spinner("Generating SQL Query..."):
            template = """
                Create a SQL query snippet using the below text:

                ```
                {text_input}

                ```

                I just want a SQL query
    
            
            """
            formatted_template = template.format(text_input=text_input)

            response = model.generate_content(formatted_template)
            sql_query = response.text
            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")

            expected_output = """
                What would be the expected response of this SQL query snippet:
                        ```
                        {sql_query}
                
                        ```
                Provide sample tabular format response with no explanation:
            
                
            """
            expected_formatted_output = expected_output.format(sql_query=sql_query)
            expoutput = model.generate_content(expected_formatted_output)
            expoutputquery = expoutput.text
            

            explanation = """
                Explain this SQL Query:
                        ```
                        {sql_query}
                        ```
                Please provide with simplest explanation:
            
                """
            formatted_explaination = explanation.format(sql_query=sql_query)
            explain_query = model.generate_content(formatted_explaination)
            explain_query_answer = explain_query.text
            
            with st.container():
                st.success("SQL Query Generated Successfully! Here is your SQL Query below:")
                st.code(sql_query, language="sql")

                st.success("Expected Output of this SQL Query will be:")
                st.markdown(expoutputquery)

                st.success("Explanation of this SQL Query:")
                st.markdown(explain_query_answer)
main()
