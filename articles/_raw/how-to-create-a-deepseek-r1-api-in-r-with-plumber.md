---
title: How to Create a DeepSeek R1 API in R with Plumber
subtitle: ''
author: Adejumo Ridwan Suleiman
co_authors: []
series: null
date: '2025-02-20T23:22:01.999Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-deepseek-r1-api-in-r-with-plumber
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740093558918/453118b9-3c93-4e57-a1ad-7471e1046ef1.png
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Deep Learning
  slug: deep-learning
- name: APIs
  slug: apis
seo_title: null
seo_desc: 'To create an AI chatbot and integrate it with another platform, you have
  to communicate with large language model using an API. This API receives prompts
  from the client and sends them to the model to generate answers.

  In this tutorial, you will lear...'
---

To create an AI chatbot and integrate it with another platform, you have to communicate with large language model using an API. This API receives prompts from the client and sends them to the model to generate answers.

In this tutorial, you will learn how to create such an API using the DeepSeek R1 large language model so external applications can call it. We will use the [DeepSeek R1 model](https://huggingface.co/deepseek-ai/DeepSeek-R1), available on HuggingFace, and the Plumber R package to deploy it as an API.

HuggingFace is an open source platform for building, training, and deploying machine learning models, while Plumber is an R package that expose R code as a RESTful APIs accessible to other applications through HTTP requests.

With this API, you can:

* Build AI applications
    
* Connect to external data and extract meaningful insights
    
* Integrate into existing applications to provide customer support, create documentations, and so on.
    

## What is the DeepSeek R1 Model?

DeepSeek R1 is the latest large language model from the Chinese company [DeepSeek](https://www.deepseek.com/). It was designed to enhance the problem-solving and analytic capabilities of AI systems.

DeepSeek-R1 uses reinforcement learning and supervised fine-tuning to handle complex reasoning tasks. Unlike proprietary models, DeepSeek R1 is open-source and free to use.

## Prerequisites

* Sign up for a [HuggingFace account](https://huggingface.co/) if you don’t already have one
    
* Install [R and R Studio](https://posit.co/download/rstudio-desktop/).
    
* Install the [`plumber`](https://www.rplumber.io/) R package to build the API endpoint
    
* Install the [`httr2`](https://httr2.r-lib.org/) R package to work with HTTP requests and interact with the Hugging Face API
    

## Step 1: Create Your Project Repository

You need to create an R project to create an API application in R. This ensures that all the files needed to keep your API working are kept together under the same directory. R Studio already has a template provided for API projects, so you can follow the steps below to create yours.

In your R Studio IDE, click on the File menu and go to New Project to open the New Project Wizard. Once in the wizard, select New Directory, then click New Plumber API Project. Inside the directory name field, give it a name (for example `DeepSeek-R1 API`), and then click on Create Project.

You will see a file called `plumber.R` with a sample API template. This is where you’ll write the code to connect to the DeepSeek R1 model on HuggingFace. Make sure that you clear this template before proceeding.

![GIF showing how to create a new Plumber project in R](https://cdn.hashnode.com/res/hashnode/image/upload/v1738503866976/60b959cd-b564-486d-8b65-c9ca0278e239.gif align="center")

Next, go to your terminal and create a `.env` file. This is where you will store the Hugging Face API key.

```plaintext
touch .env
```

![Image showing how to create a .env variable on the terminal](https://cdn.hashnode.com/res/hashnode/image/upload/v1738504109388/6ce9bda3-305a-4f2e-87b8-adbe4c245861.png align="center")

Create a `.gitignore` file and add the `.env` file to it. This ensures that sensitive information like access tokens and API keys are not pushed to your Git repository.

![Image showing the .env file in the .gitignore file](https://cdn.hashnode.com/res/hashnode/image/upload/v1738504889229/0d433bcb-2a7d-4379-a0c7-e09fb53e288f.png align="center")

## Step 2: Create a Hugging Face Access Token

We need to create an access token to connect to Hugging Face models. Go to your profile, click Settings, and click Create New Token to create your access token for the Hugging Face repository.

![Image showing the access tokens page, with options to create a new token ](https://cdn.hashnode.com/res/hashnode/image/upload/v1738504360986/077a2778-d790-4ff9-94e1-c2c372b2efef.png align="center")

Copy the access token and paste it into your `.env` file, and give it the name `HUGGINGFACE_ACCESS_TOKEN`.

```plaintext
HUGGINGFACE_ACCESS_TOKEN="<your-access-token>"
```

Next is to install the `dotenv` package, and paste the following code at the top of your `plumber.R` file:

```r
# Load environment variables from .env
dotenv::load_dot_env()
```

`dotenv::load_dot_env()` loads all environment variables in the `.env` file, making them available to the `plumber.R` script.

## Step 3: Build the DeepSeek API Endpoint

Now that we have our project environment set up and API token ready, we’ll write the code to build the API application by connecting to the DeepSeek R1 model on HuggingFace.

Go to the `plumber.R` file and load the following libraries:

```r
library(plumber)
library(httr2)
```

Copy and paste the following code into `plumber.R`:

```r

api_key <- Sys.getenv("HUGGINGFACE_ACCESS_TOKEN")



#* @post /deepseek_chat
function(prompt) {
  url <- "https://huggingface.co/api/inference-proxy/together/v1/chat/completions"

  # Create a request object
  req <- request(url) |>
    req_auth_bearer_token(api_key) |>
    req_body_json(list(
      model = "deepseek-ai/DeepSeek-R1",
      messages = list(
        list(role = "user", content = prompt)
      ),
      max_tokens = 500,
      stream = FALSE
    ))

  # Perform the request and capture the response
  res <- req_perform(req)

  # Parse the JSON response
  parsed_data <- res |>
    resp_body_json()

  # Extract the content from the response
  content <- parsed_data$choices
  return(content)
}
```

Here’s what’s going on in the above code:

* `Sys.getenv` gets the HuggingFace access token and stores it in the variable `access_token`.
    
* The `url` variable contains the API link to access the DeepSeek model on HuggingFace. You can get this by searching the model name `deepseek-ai/DeepSeek-R1` on HuggingFace. Go to the **View Code** button, and under the **cURL** tab, copy the API URL
    
    ![GIF showing how to copy the API url you are going to use in your plumber API code](https://cdn.hashnode.com/res/hashnode/image/upload/v1739177037117/0781bce2-7bf8-411d-ad71-cb2bf11fe1bb.gif align="left")
    
* `#* @post /deepseek_chat` means that the endpoint makes a POST request through the path `/deepseek_chat`.
    
* This endpoint takes an argument `prompt`, a text, or a question a user is expected to give.
    
* The `req` object is a chain of various operations, which makes a `request()` to the `url`, and then takes the `api_key` inside the `req_auth_bearer_token()` function. Model properties such as `model` name, `role`, `prompt`, and `max_tokens` are passed to the `req` object through the `req_body_json` function.
    
* The `headers` variable contains the authorization required to make a request to HuggingFace API.
    
* The request is performed and captured in a response object `res` using the `req_perform()` function.
    
* The `res` object returns a JSON object, which is now parsed to R using the`resp_body_json()` function.
    
* The `content` of the `parsed_data` is now returned so you can extract the information you need from the application for which you want to use the API.
    

## Step 4: Test the API Endpoint

Let’s run the API endpoint to see how the application performs. Click on Run API. This will automatically open the API endpoint on your browser on the URL [`http://127.0.0.1:8634/docs/`](http://127.0.0.1:8634/docs/).

![Image showing the Run API button](https://cdn.hashnode.com/res/hashnode/image/upload/v1739282692303/82a029ea-31f5-4088-9e72-2fe1b69d0f7d.png align="center")

Click on the API endpoint dropdown, provide a prompt, and click the Execute button. You should receive a reply in a few minutes.

![Image showing how the API endpoint returns a response when a prompt is given](https://cdn.hashnode.com/res/hashnode/image/upload/v1739282620577/b1a52679-b397-4d82-af56-0f81ebc5888e.gif align="center")

## Conclusion

With your API, you can make inferences to the Hugging Face model and build AI applications in R or other programing languages. You need to host your API to make it accessible to clients online. There are various [ways of hosting an R Plumber application](https://www.rplumber.io/articles/hosting.html): you can use Docker or host it on DigitalOcean using the plumberDeploy R package. However, the simplest and easiest way is to use [Posit Connect](https://posit.co/products/enterprise/connect/).

You can use the same approach used in this tutorial to try out other HuggingFace models, build an API to generate images or translate different languages. R Plumber is easy to use, and the documentation provides many resources.

If you are interested in model deployment using R Plumber, you can check out [this article](https://learndata.xyz/posts/forecasting%20time%20series%20data%20with%20facebook%20prophet/) on how to deploy a Time Series model built on Prophet using R Plumber.

If you find this article interesting, please check my other articles on [learndata.xyz](https://learndata.xyz/blog).
