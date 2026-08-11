import streamlit as st
from crewai import Agent




GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

GEMINI_MODEL = "gemini/gemini-flash-lite-latest"




search_agent = Agent(
    role="Product Search Specialist",

    goal="""
    Search for laptops that satisfy the company's
    procurement requirements.
    """,

    backstory="""
    You are an expert procurement researcher.
    You search for suitable laptops based on budget,
    RAM, processor, storage, portability and business needs.
    """,

    llm=GEMINI_MODEL,

    verbose=True
)




data_agent = Agent(
    role="Product Data Collection Specialist",

    goal="""
    Collect and organize detailed information about
    candidate laptops.
    """,

    backstory="""
    You are a data collection specialist.
    Your responsibility is to organize laptop information
    such as company, product, price, RAM, CPU, storage,
    GPU and weight.
    """,

    llm=GEMINI_MODEL,

    verbose=True
)




scraping_agent = Agent(
    role="Website Scraper",

    goal="""
    Extract laptop specifications from product webpages.
    """,

    backstory="""
    You are an expert web scraping specialist.
    Your responsibility is to extract accurate product
    information such as CPU, RAM, storage, GPU,
    battery life, weight, operating system and price.
    """,

    llm=GEMINI_MODEL,

    verbose=True
)



comparison_agent = Agent(
    role="Product Comparison Specialist",

    goal="""
    Compare candidate laptops based on price,
    specifications and overall value.
    """,

    backstory="""
    You are an expert technology analyst.
    You compare laptops objectively using their price,
    processor, RAM, storage, GPU, weight and battery life.
    """,

    llm=GEMINI_MODEL,

    verbose=True
)




ranking_agent = Agent(
    role="Product Ranking Specialist",

    goal="""
    Rank the best laptops according to the company's
    procurement requirements.
    """,

    backstory="""
    You are a procurement decision specialist.
    You rank products according to performance,
    price, portability, specifications and value for money.
    """,

    llm=GEMINI_MODEL,

    verbose=True
)




report_agent = Agent(
    role="Procurement Report Specialist",

    goal="""
    Generate a professional procurement report
    containing the final recommendations.
    """,

    backstory="""
    You are a professional business report writer.
    You transform the analysis and ranking results
    into a clear procurement report with recommendations.
    """,

    llm=GEMINI_MODEL,

    verbose=True
)