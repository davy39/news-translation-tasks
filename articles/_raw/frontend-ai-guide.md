---
title: How to Build AI Apps – A Frontend Developer's Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-01-23T22:05:41.000Z'
originalURL: https://freecodecamp.org/news/frontend-ai-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Mojito-Cocktail-Recipe-Blog-Banner--1-.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Front-end Development
  slug: front-end-development
seo_title: null
seo_desc: 'By Mahmud Adeleye

  Artificial Intelligence: The New Frontier for Frontend Developers

  The demand for AI-powered applications is growing at a fast pace. As a front-end
  developer, you can take advantage of this trend and advance your career by integratin...'
---

By Mahmud Adeleye

## Artificial Intelligence: The New Frontier for Frontend Developers

The demand for AI-powered applications is growing at a fast pace. As a front-end developer, you can take advantage of this trend and advance your career by integrating your skills in frontend development with AI technologies. 

This integration allows you to build intelligent applications that improve user experiences and provide valuable insights that can positively impact a user's decisions.

To highlight the exciting opportunities out there right now, consider these statistics:

1. In 2023, [more than 60% of startups accepted into the renowned Y Combinator](https://www.theinformation.com/articles/what-we-can-learn-from-ai-startups-in-y-combinators-latest-batch) were focused on AI.
2. Despite a [slowdown in global investments, funding to AI startups surged and reached an impressive $50 billion in 2023.](https://news.crunchbase.com/venture/global-funding-data-analysis-ai-eoy-2023/)

In this guide, we'll cover the following:

1. The role of frontend developers in advancing AI innovation.
2. Key steps to follow when integrating AI services into your frontend workflow
3. How to ensure the optimal performance and security of the AI apps you build.
4. Lastly, we will incorporate the tips in 1-3 to build an AI Website Critic that can roast your websites and portfolio apps using React and OpenAI's GPT4-Vision Model.

## Prerequisites

- Knowledge of HTML
- Basic understanding of React hooks
- Node and npm installed on your local computer.

## The Role of Frontend Developers in Crafting AI-driven Experiences

Frontend developers play a crucial role in crafting AI-driven experiences by leveraging their expertise in user interface design, data visualization, and technical implementation. 

They are responsible for creating the user interface, designing the interaction flows, and integrating AI functionality seamlessly into the app. 

Frontend developers also collaborate with back-end developers and data scientists to ensure the efficient and accurate functioning of AI algorithms.

In addition, frontend developers play a critical role in the performance of web apps that leverage the latest AI models. They are responsible for optimizing the app's performance, ensuring cross-platform compatibility, and implementing responsive designs that adapt to different devices and screen sizes.

## How to Integrate AI Services Into Your Frontend Workflow

To integrate AI services into your frontend workflow, you should follow a systematic approach that includes these steps:

1. Identify the task or problem that AI capabilities can solve or enhance.
2. Research and evaluate AI companies that provide APIs and node SDKs for the specific AI capabilities required for the task or problem you identified. By understanding the offerings of different AI companies, you can choose the most suitable AI services to integrate into your applications. 

Let's take a look at some popular AI models and their core tasks:

| AI Model | Task |
| --- | --- |
| GPT-4 | Multimodal model (capable of text, image etc) |
| Stable Diffusion | Text to Image Generative AI Model |
| Mistral 7B | Multimodal model (capable of text, image etc) |
| Voicebox | Speech generative AI model |
| DALL·E 3 | Text to Image Generative AI Model |

You can explore more of these models on [Replicate Explore](https://replicate.com/explore) and [Huggingface explore models](https://huggingface.co/models) pages.

3. Integrate the selected AI services into your frontend application by leveraging the provided APIs and node SDKs. This involves understanding the documentation and guidelines the AI companies offer to ensure seamless integration and proper utilization of the AI capabilities.
4. Test and validate the integrated AI services within your frontend application to ensure accurate and efficient functionality. This step is crucial for identifying and addressing technical issues or optimization requirements.

It's also important to design with empathy by providing clear explanations and visualizations, giving users a sense of control and ownership over AI-generated outputs. 

### Example application

Let's go over an example. Suppose you want to make a custom meme generator. In that case, you should search for AI models specifically trained to work with images, such as Stability's Stable Diffusion and OpenAI's DALL·E 3.

After that, you can explore the best APIs and SDKs that you can use to take advantage of these AI models and create a basic sample. 

To illustrate, let's use the Replicate Node SDK, which provides a convenient method to interact with the Stable Diffusion AI model and set up a basic Node.js program that we can later integrate into our React application.

Step 1. Get your token from https://replicate.com/account
Step 2: Install the Node SDK with the npm command: `npm install replicate`
Step 3: Query the Stable Diffusion AI model via the replicate SDK.
```
const Replicate = require("replicate");
const replicate = new Replicate({
  
  auth: "", // defaults to process.env.REPLICATE_API_TOKEN
});

async function iLoveCats(){
    const model = "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478";
  const input = {
    prompt: "a cat wearing a suit",
  };
  const output = await replicate.run(model, { input });
  console.log(output[0]);
  
}

iLoveCats()
```

When you log the output, you get an image URL that you can easily display in your frontend app. `https://replicate.delivery/pbxt/ng6Tb0HNdzYwFZXMNv3qmIBxc2GIwU4t7edephtDvuWZ5wNSA/out-0.png`

<figure>
    <img src="https://www.freecodecamp.org/news/content/images/2024/01/catsuit.png"
         alt="A cat in a suit">
    <figcaption>A cat in a suit.</figcaption>
</figure>

## How to Optimize for Performance and Security in AI-driven Frontend Applications

Optimizing for performance and security in AI-driven frontend apps is essential for creating a smooth user experience and for data protection as well. 

Thankfully, the techniques listed below are similar to standard practices in traditional frontend development. This overlap means that developers who are familiar with conventional frontend optimization and security practices can more easily adapt and apply those skills to the unique demands of AI-driven applications:

1. Employ lazy loading and code-splitting techniques to reduce initial loading times and improve performance.
2. Utilize caching and resource optimization techniques to minimize unnecessary API calls and improve data retrieval speed.
3. Implementing secure API endpoints and authentication mechanisms to ensure only authorized access to AI services and data.

## **How to Build an AI Website Critic using React and OpenAI's GPT4-Vision Model**

In this section, we will build a React app that utilizes a Vision model to analyze images of websites and provide feedback. To do this, we will follow the previously described 4-step workflow for integrating AI services into frontend apps.   

Since we need for a vision model that can analyze images, we should look at the available options in the market, which you can find [here](https://replicate.com/collections/vision-models) and [here](https://huggingface.co/models?pipeline_tag=visual-question-answering&sort=downloads). [After examining the performance benchmarks of available vision models](https://encord.com/blog/gpt-vision-vs-llava/), we will go with OpenAI's GPT-4 vision model.  

OpenAI's GPT-4 vision model is a state-of-the-art AI model released in late 2023. It can accept images as inputs, analyze them, and provide detailed feedback based on the prompts. 

Apart from performance reasons, we will use it for our Website Critique application because it offers relatively cheaper pricing than other vision models, and has an easy-to-use API endpoint bundled with the popular OpenAI developer interface.

It's now time to integrate it into our React app.

### Step 1: Install React + Vite

You can do that with the following command:

```
npm create vite@latest my-website-critic -- --template react
```

### Step 2: Install OpenAI Node package

Open the generated project folder in your favorite IDE and install the OpenAI Node package, which you will use to interact with the GPT4 Vision model.

Here's how to install it:

```
cd my-website-critic
npm install openai
```

### Step 3: Install the React markdown package 

This will help you format the model's textual responses in a readable format.

```
npm install react-markdown
```

### Step 4: Run npm install

Now run `npm install`:

```
  npm install
  npm run dev
```

### Step 5: Manage state in React

In this step, you will use React's **`useState`** and **`useEffect`** hooks for managing the state and handling the asynchronous request to OpenAI's API in `src/App.jsx`.

<figure>
    <img src="https://i.ibb.co/sWM573X/Screenshot-2024-01-18-at-10-34-28-AM.png"
         alt="freeCodeCamp hero section">
    <figcaption>freeCodeCamp hero section</figcaption>
</figure>


For our image input, we will be using a screenshot of the freeCodeCamp homepage hero section uploaded to a image storage platform like [IMGBB](https://imgbb.com/). Feel free to use any image URL you want.

Here's the code - I'll explain it below:

```jsx
import { useState, useEffect } from 'react';
import OpenAI from 'openai';
import ReactMarkdown from 'react-markdown';

const App = () => {
  const [response, setResponse] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const openai = new OpenAI({
      apiKey: "YOUR_OPENAI_API_KEY",
      dangerouslyAllowBrowser: true,
    });

    const fetchUICriticResponse = async () => {
      setIsLoading(true);
      try {
        const result = await openai.chat.completions.create({
          model: "gpt-4-vision-preview",
          messages: [
            {
              role: "user",
              content: [
                { type: "text", text: "You're an expert UI critic. What can I improve in this website?" },
                {
                  type: "image_url",
                  image_url: {
                    "url": "https://i.ibb.co/sWM573X/Screenshot-2024-01-18-at-10-34-28-AM.png",
                  },
                },
              ],
            },
          ],
          "max_tokens": 1500
        });
        if (result && result.choices && result.choices.length > 0 && result.choices[0].message) {
          console.log(1, result);
          setResponse(result.choices[0].message.content);
        }
      } catch (error) {
        console.error("Error fetching AI response:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchUICriticResponse();
  }, []);

  return (
    <div>
      <h3>Hi! UI Expert Here</h3>
      {isLoading ? (
        <p>Loading...</p>
      ) : response ? (
        <div>
          <h3>My Feedback:</h3>
          <ReactMarkdown>{response}</ReactMarkdown>
        </div>
      ) : (
        <p>No response received.</p>
      )}
    </div>
  );
};

export default App;
```

In the above component:

- The **`useEffect`** hook runs the `fetchUICriticResponse` function when the component mounts.
- The **`useState`** hooks manage the AI response (**`response`**) and the loading state (**`isLoading`**).
- `fetchUICriticResponse` is an asynchronous function that fetches the response using the OpenAI API.
- The component renders a loading message while the response is being fetched. Once the fetch is complete, it displays the response or a fallback message using the React Markdown package we installed earlier.

You should get a result similar to the image below containing the result of the GPT4 Vision model analysis of the provided image and prompt given.

<figure>
    <img src="https://i.ibb.co/DCNSHy7/critic.png"
         alt="result of the GPT4 Vision model analysis">
    <figcaption>result of the GPT4 Vision model analysis.</figcaption>
</figure>

As you can see, the analysis goes through each element on the page and offers feedback – both positive, and more constructive – on things like navigation clarity, whitespace usage, search functions, and so on.


**Note:** Handling API keys directly in the frontend is not recommended due to security concerns. The example is just for learning. In production, create an `.env` file and put your `YOUR_OPENAI_API_KEY` in it.


## What's Next?

You can enhance these code examples by creating a simple input field for users to enter their image links. You may also set up an image uploader to allow users to upload images from their local device.

Please refer to the [official documentation](https://platform.openai.com/docs/guides/vision) for instructions on how to achieve this.

When deciding which AI applications to develop, it is crucial to consider the intended impact, user requirements, and available resources. 

Some other potential AI application ideas include a language translation app and a virtual personal assistant.

## Conclusion

If you're interested in incorporating AI into your frontend apps, start by exploring open and closed-source AI models. You'll also want to understand how to work with APIs and external libraries. 

You should also focus on familiarizing yourself with handling AI model responses and interactivity.

With this knowledge, you can position yourself for the several consumer-ready AI innovations that will spring up and require the services of a frontend developer skilled in building AI-powered apps.


