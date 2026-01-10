---
title: How to Generate Financial Press Reviews Using AI
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2024-08-20T12:39:49.320Z'
originalURL: https://freecodecamp.org/news/how-to-generate-financial-press-reviews-using-ai
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724059022091/7ce2eba8-46ff-4d08-8e56-afa814cb68cc.jpeg
tags:
- name: AI
  slug: ai
- name: Python
  slug: python
- name: Artificial Intelligence
  slug: artificial-intelligence
seo_title: null
seo_desc: In today’s fast-paced business environment, staying informed about the latest
  developments in your industry is crucial for making strategic decisions. Companies
  must know market trends, competitor activities, and potential risks to remain competitive...
---

In today’s fast-paced business environment, staying informed about the latest developments in your industry is crucial for making strategic decisions. Companies must know market trends, competitor activities, and potential risks to remain competitive.

One effective way to achieve this is by generating comprehensive financial press reviews based on current news. This is where my Python script comes into play—a tool that automates gathering and analyzing news related to specific queries, enabling businesses to stay up-to-date with their niche and make informed decisions about their next steps. Of course, this script does not replace the work of experts who will then verify and deepen the information found.

This is what we'll cover:

* [The Importance of Staying Informed](#heading-the-importance-of-staying-informed)
    
* [Overview of the Python Script](#heading-overview-of-the-python-script)
    
* [How the Script Works](#heading-how-the-script-works)
    
* [1\. How to Set Up the Environment](#heading-1-how-to-set-up-the-environment)
    
* [2\. How to Fetch Relevant News](#heading-2-how-to-fetch-relevant-news)
    
* [3\. How to Prepare the Prompt for AI Analysis](#heading-3-how-to-prepare-the-prompt-for-ai-analysis)
    
* [4\. How to Generate the Press Review](#heading-4-how-to-generate-the-press-review)
    
* [5\. How to Save the Report](#heading-5-how-to-save-the-report)
    
* [Error Handling and Logging](#heading-error-handling-and-logging)
    
* [Conclusion](#heading-conclusion)
    

## **The Importance of Staying Informed**

For any business, being informed about the latest news in their industry is more than just a good practice. It's a necessity. Key news events can impact markets, influence consumer behavior, and affect supply chains.

By regularly monitoring relevant news, businesses can:

* **Identify Emerging Trends:** Spotting trends early can give a business a competitive edge, allowing it to adapt and capitalize on new opportunities.
    
* **Monitor Competitors:** Understanding what competitors are doing helps refine strategies and stay ahead in the market.
    
* **Mitigate Risks:** By staying informed about potential risks, such as regulatory changes or economic downturns, businesses can proactively adjust their operations to minimize impact.
    
* **Plan Strategic Moves:** With a clear understanding of the market landscape, businesses can plan their next steps with greater confidence.
    

This Python script automates this process, allowing businesses to generate detailed financial press reviews based on specific queries, helping them to understand the market better and plan their next moves effectively.

## Overview of the Python Script

This Python script is designed to fetch news articles from the web, analyze them using a large language model (LLM), and generate a structured press review that businesses can use to inform their strategies. The script is built using Python, leveraging two powerful libraries:

1. **Requests Library**: This is used to make HTTP requests to the News API, retrieving news articles based on the specified query.
    
2. **Anthropic Library**: This library is used to interact with the Claude AI model, which processes the news data and generates a comprehensive analysis.
    

The generated press reviews are then saved in a text file, which businesses can review at their convenience.

## How the Script Works

Let’s break down how the script operates, step by step:

### 1\. How to Set Up the Environment

Before running the script, ensure that you have Python installed on your system. Additionally, you will need to install the necessary Python libraries:

```python
pip install requests anthropic
```

### 2\. How to Fetch Relevant News

The script starts by declaring the `generate_report` function. Inside the function, I made a GET request to the News API, using the `requests` library to retrieve the latest news articles related to a specific query. Here’s the relevant code snippet:

```python
response = requests.get('https://newsapi.org/v2/everything?q=' + query + '&apiKey=YOUR_API_KEY')
response_data = response.json()
```

In this part of the script:

* `query`: This is the keyword or phrase related to the niche or topic you want to monitor. For example, a company might use the query `"finance"` to fetch news related to the finance industry.
    
* `response_data`: The news data is fetched in JSON format, which is then parsed into a Python dictionary for further processing.
    

### 3\. How to Prepare the Prompt for AI Analysis

Once the news data is retrieved, the script prepares a prompt to feed into the Claude AI model. The prompt is designed to instruct the model to generate a detailed press review focusing on the impact of the news on financial markets and specific industries. Here’s how the prompt is constructed:

```python
prompt = (
    "You are a senior financial journalist tasked with writing a comprehensive press review. "
    "Focus on the key news provided and analyze their potential impact on the financial markets, "
    "specific industries, or relevant companies. Ensure the press review is structured and concise. "
    "Start the paragraph with the sentence 'This is the press review about " + query + "'. "
    "You'll find the key news in the following json file: " + response_data_to_str
)
```

The prompt includes:

* **Role Specification**: The AI is instructed to act as a senior financial journalist.
    
* **Task Description**: The AI is asked to analyze the news and its impact, ensuring the output is structured and concise.
    
* **News Data**: The retrieved news articles are passed to the AI in JSON format, providing the context needed for analysis.
    

### 4\. How to Generate the Press Review

With the prompt ready, the script interacts with the Anthropic Claude AI model to generate the press review. The `anthropic` library is used for this interaction:

```python
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="You are a senior financial journalist. Provide thorough insightful financial press review and advice. Use technical language where appropriate, and consider the broader economic context in your responses.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }
    ]
)
```

In this part of the script:

* `client.messages.create`: This method sends the prompt to the AI model and retrieves the generated text.
    
* `plain_text`: The resulting press review is stored as plain text, ready to be saved or further processed.
    

### 5\. How to Save the Report

Finally, the generated press review is saved to a text file:

```python
with open("report.txt", "a") as file:
    file.write(plain_text + "\n")
```

This ensures that each generated report is appended to the **report.txt** file, making it easy to access and review multiple reports over time.

### Error Handling and Logging

Robust error handling is crucial to ensure the application runs smoothly. The script includes basic error handling using `try-except` blocks to catch and log any errors that occur during execution:

```python
except requests.exceptions.RequestException as e:
    logging.error(f"An error occurred during the HTTP request: {e}")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
```

Errors are logged in an **error.log** file, which helps to fix issues without interrupting the main functionality of the script.

Don't forget to call the function, passing the topic you want information about as a parameter:

```python
generate_report("finance")    
```

And here's the full code:

```python
import requests
import anthropic
import logging

# Set up logging to capture errors in a file named "error.log"
logging.basicConfig(filename="error.log", level=logging.ERROR)

def generate_report(query):
    try:
        # Step 1: Make a GET request to the news API with the given query
        response = requests.get('https://newsapi.org/v2/everything?q=' + query + '&apiKey=<YOUR_API_KEY>')
        
        # Step 2: Parse the JSON response from the API into a Python dictionary
        response_data = response.json()

        # Convert the JSON data to a string format for use in the prompt
        response_data_to_str = str(response_data)

        # Step 3: Initialize the Anthropic client
        client = anthropic.Anthropic()

        # Step 4: Create a prompt for the AI model to generate a financial press review
        prompt = (
            "You are a senior financial journalist tasked with writing a comprehensive press review. "
            "Focus on the key news provided and analyze their potential impact on the financial markets, "
            "specific industries, or relevant companies. Ensure the press review is structured, and concise. "
            "Start the paragraph with the sentence 'This is the press review about " + query + "'. "
            "You'll find the key news in the following json file: " + response_data_to_str
        )

        # Step 5: Use the prompt to create a message with the AI model
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system=(
                "You are a senior financial journalist. Provide thorough insightful financial press review and advice. "
                "Use technical language where appropriate, and consider the broader economic context in your responses."
            ),
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )

        # Step 6: Extract the generated text from the message response
        plain_text = message.content[0].text

        # Step 7: Append the generated report to a file named "report.txt"
        with open("report.txt", "a") as file:
            file.write(plain_text + "\n")
    
    except requests.exceptions.RequestException as e:
        # Log any HTTP request errors to "error.log"
        logging.error(f"An error occurred during the HTTP request: {e}")
    except Exception as e:
        # Log any unexpected errors to "error.log"
        logging.error(f"An unexpected error occurred: {e}")

# Generate reports for the needed queries
generate_report("finance")
```

After running the script, you should get the **report.txt** file looking like this:

```plaintext
This is the press review about finance:

The financial markets are digesting several key developments this week:

1. Economic Data: The latest jobs report showed unemployment increased slightly, sending markets into a tailspin initially. However, experts caution against overreacting, noting the economy is not "falling off a cliff." The Federal Reserve is getting closer to cutting interest rates, with investors betting the first cut could come as soon as September if inflation continues moderating.

2. Corporate Earnings: Company XXX reported disappointing Q2 earnings, with losses more than tripling to $1.4 billion amid increased scrutiny of its safety and quality control. The Company YYY also named a new CEO who received early praise from key customers. Meanwhile, Company warned of slowing growth and weakening U.S. demand in its Q2 report.

3. Banking & Fintech: Company ZZZ has become Europe's most valuable private tech company at a $45 billion valuation following an employee share sale. This intensifies the neobank challenge to traditional finance. The company also recently obtained its long-awaited UK banking license.

4. Regulatory Developments: The Central Bank is considering creating a strategic Bitcoin reserve, to be partly financed by revaluing gold certificates held. This represents a potential major shift in cryptocurrency policy.

5. Personal Finance: Experts continue to warn about common money mistakes, even among financially savvy individuals. These include waiting too long to start investing and not properly planning for retirement.

The overall market sentiment remains cautious amid mixed economic signals and geopolitical tensions. Investors are closely watching central bank policies and corporate earnings for further direction.
```

### Conclusion

In a business environment where staying informed is key to success, this Python script offers an automated solution to generate financial press reviews based on the latest news. By leveraging AI, businesses can quickly gain insights into market trends, monitor competitors, and make informed strategic decisions. While the script is already functional and useful, with further enhancements, it can evolve into a powerful tool for business intelligence, helping companies stay ahead in their industry.

By automating the process of news analysis, this script not only saves time but also provides a structured approach to understanding the ever-changing business landscape, empowering companies to take the next steps with confidence.

It is important to remember that this is a tool to support analysts who'll have to verify and evaluate the information available in the report.

If you liked this post, please star my [repo](https://github.com/mventuri/ai-powered-press-review) here, can't wait to approve your PR!
