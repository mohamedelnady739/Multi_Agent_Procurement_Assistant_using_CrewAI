from crewai import Task

from agents import (
    search_agent,
    data_agent,
    scraping_agent,
    comparison_agent,
    ranking_agent,
    report_agent
)




company_context = """
Company: ABC Technology

Goal:
Purchase the best laptops for software engineers.

Budget:
1000 Euro per laptop.

Requirements:
- Minimum RAM: 16 GB
- SSD Storage
- Intel Core i5 or AMD Ryzen 5 and above
- Lightweight
- Good battery life

Return the top 5 products.
"""




search_task = Task(
    description=f"""
    {company_context}

    Search for suitable business laptops that match
    the company requirements.

    Find multiple candidate products and collect:
    - Product name
    - Company
    - Price
    - CPU
    - RAM
    - Storage
    - Weight
    - Battery information
    - Product URL

    Return the best candidate laptops.
    """,

    expected_output="""
    A list of candidate laptops with their names,
    prices, specifications and URLs.
    """,

    agent=search_agent
)



data_task = Task(
    description=f"""
    {company_context}

    Organize the laptop information obtained from
    the search stage.

    For each laptop identify:
    - Company
    - Product
    - Price
    - RAM
    - CPU
    - Storage
    - GPU
    - Weight
    - Operating System
    - URL

    Remove products that clearly do not satisfy
    the company requirements.
    """,

    expected_output="""
    A clean structured list of laptops and their
    specifications.
    """,

    agent=data_agent,

    context=[search_task]
)



scraping_task = Task(
    description="""
    Review the product URLs obtained from the previous
    agents.

    Extract additional laptop information when available:

    - Product name
    - CPU
    - RAM
    - Storage
    - GPU
    - Weight
    - Battery life
    - Operating system
    - Price

    Do not invent specifications.
    If information is unavailable, mark it as
    "Not available".
    """,

    expected_output="""
    A structured collection of verified laptop
    specifications from the available webpages.
    """,

    agent=scraping_agent,

    context=[data_task]
)




comparison_task = Task(
    description=f"""
    {company_context}

    Compare all laptops collected by the previous agents.

    Compare them according to:

    1. Price
    2. CPU performance
    3. RAM
    4. SSD storage
    5. GPU
    6. Weight
    7. Battery life
    8. Overall value

    Explain the strengths and weaknesses of each
    candidate.

    Do not recommend products that exceed the budget
    unless clearly marked as over-budget.
    """,

    expected_output="""
    A detailed comparison of the candidate laptops
    followed by the best-value candidates.
    """,

    agent=comparison_agent,

    context=[scraping_task]
)




ranking_task = Task(
    description=f"""
    {company_context}

    Rank the candidate laptops from best to worst.

    Give higher priority to:

    - Meeting all requirements
    - Price under 1000 Euro
    - At least 16 GB RAM
    - SSD storage
    - Intel Core i5 / AMD Ryzen 5 or better
    - Lightweight design
    - Good battery life
    - Overall value for money

    Return exactly the TOP 5 products.

    For every product provide:
    - Rank
    - Product name
    - Price
    - Main specifications
    - Reason for ranking
    """,

    expected_output="""
    A ranked TOP 5 list of laptops with explanations
    for each ranking.
    """,

    agent=ranking_agent,

    context=[comparison_task]
)



report_task = Task(
    description=f"""
    {company_context}

    Create a professional procurement report based
    on the final ranking.

    The report must contain:

    1. Executive Summary

    2. Company Requirements

    3. Top 5 Recommended Laptops

    4. Product Comparison

    5. Ranking

    6. Advantages and Disadvantages

    7. Final Procurement Recommendation

    8. Conclusion

    Keep the report clear and professional.

    Do not invent product specifications.
    """,

    expected_output="""
    A professional procurement report containing
    the final Top 5 laptop recommendations.
    """,

    agent=report_agent,

    context=[ranking_task]
)