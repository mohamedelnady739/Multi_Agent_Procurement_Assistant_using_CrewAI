import streamlit as st

from crewai import Crew, Process

from agents import (
    search_agent,
    data_agent,
    scraping_agent,
    comparison_agent,
    ranking_agent,
    report_agent
)

from tasks import (
    search_task,
    data_task,
    scraping_task,
    comparison_task,
    ranking_task,
    report_task
)




st.set_page_config(
    page_title="Multi-Agent Procurement Assistant",
    page_icon="💻",
    layout="wide"
)




st.title("💻 Multi-Agent Procurement Assistant")

st.write(
    "AI-powered laptop procurement system using CrewAI."
)




st.sidebar.header("Company Requirements")

company = st.sidebar.text_input(
    "Company Name",
    "ABC Technology"
)

budget = st.sidebar.number_input(
    "Budget per Laptop (€)",
    min_value=300,
    max_value=5000,
    value=1000
)

ram = st.sidebar.selectbox(
    "Minimum RAM",
    [8, 16, 32, 64],
    index=1
)


st.sidebar.write("Storage: SSD")

st.sidebar.write(
    "Processor: Intel Core i5 / AMD Ryzen 5+"
)

st.sidebar.write(
    "Requirement: Lightweight"
)

st.sidebar.write(
    "Requirement: Good Battery Life"
)




st.subheader("Procurement Requirements")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Budget",
        f"€{budget}"
    )

with col2:
    st.metric(
        "Minimum RAM",
        f"{ram} GB"
    )

with col3:
    st.metric(
        "Recommended Products",
        "Top 5"
    )




if st.button(
    " Run Procurement Assistant",
    use_container_width=True
):

    st.info(
        "Starting Multi-Agent Procurement Workflow..."
    )

    # Update company context dynamically
    company_context = f"""
    Company: {company}

    Budget: {budget} Euro per laptop.

    Requirements:
    - Minimum RAM: {ram} GB
    - SSD Storage
    - Intel Core i5 or AMD Ryzen 5 and above
    - Lightweight
    - Good battery life
    """

    st.write("### Company Context")
    st.write(company_context)



    crew = Crew(

        agents=[
            search_agent,
            data_agent,
            scraping_agent,
            comparison_agent,
            ranking_agent,
            report_agent
        ],

        tasks=[
            search_task,
            data_task,
            scraping_task,
            comparison_task,
            ranking_task,
            report_task
        ],

        process=Process.sequential,

        verbose=True
    )



    with st.spinner(
        "Agents are working... Please wait."
    ):

        result = crew.kickoff()



    st.success(
        "Procurement process completed!"
    )

    st.subheader(
        "📊 Final Procurement Recommendation"
    )

    st.write(result)

    # Save result
    st.session_state["result"] = str(result)



if "result" in st.session_state:

    report_text = st.session_state["result"]

    html_report = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Procurement Report</title>

        <style>

        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
        }}

        .container {{
            background: white;
            padding: 35px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}

        h1 {{
            text-align: center;
        }}

        h2 {{
            margin-top: 25px;
        }}

        pre {{
            white-space: pre-wrap;
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }}

        </style>

    </head>

    <body>

        <div class="container">

            <h1>Multi-Agent Procurement Assistant</h1>

            <h2>Company</h2>
            <p>{company}</p>

            <h2>Procurement Requirements</h2>

            <ul>
                <li>Budget: €{budget}</li>
                <li>Minimum RAM: {ram} GB</li>
                <li>SSD Storage</li>
                <li>Intel Core i5 or AMD Ryzen 5 and above</li>
                <li>Lightweight laptop</li>
                <li>Good battery life</li>
            </ul>

            <h2>Final Procurement Recommendation</h2>

            <pre>{report_text}</pre>

        </div>

    </body>
    </html>
    """


    st.divider()

    st.subheader("📄 Procurement Report")

    st.components.v1.html(
        html_report,
        height=800,
        scrolling=True
    )



    st.download_button(
        label="⬇️ Download HTML Report",
        data=html_report,
        file_name="procurement_report.html",
        mime="text/html",
        use_container_width=True
    )