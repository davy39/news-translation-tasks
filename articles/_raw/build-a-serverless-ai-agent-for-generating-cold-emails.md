---
title: How to build a Serverless AI Agent to Generate Cold emails for Your Dream Job
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2025-02-19T13:41:44.886Z'
originalURL: https://freecodecamp.org/news/build-a-serverless-ai-agent-for-generating-cold-emails
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1739971173263/869c0c1c-9b45-48af-a1d1-0982436b8630.png
tags:
- name: AI
  slug: ai
- name: llm
  slug: llm
- name: ai-agent
  slug: ai-agent
seo_title: null
seo_desc: 'Cold emails can make a huge difference in your job search, but writing
  the perfect one takes time. You need to match your skills with the job description,
  find the right tone, and do it over and over again—it’s exhausting.

  This guide will walk you th...'
---

Cold emails can make a huge difference in your job search, but writing the perfect one takes time. You need to match your skills with the job description, find the right tone, and do it over and over again—it’s exhausting.

This guide will walk you through building a cold email generator agent using serverless memory agents by Langbase to automate this entire process. We’ll integrate the memory agent into a Node.js project, enabling it to read your résumé, analyze the job description, and generate a personalized, high-impact cold email in seconds.

### Here’s what I’ll cover:

1. [Large language models (LLMs) are stateless by nature](#heading-large-language-models-llms-are-stateless-by-nature)
    
2. [What are Memory agents?](#heading-what-are-memory-agents)
    
3. [Prerequisites](#heading-prerequisites)
    
4. [Reference Architecture](#heading-reference-architecture)
    
5. [Step 1: Create a directory and initialize npm](#heading-step-1-create-a-directory-and-initialize-npm)
    
6. [Step 2: Create a serverless Pipe agent](#heading-step-2-create-a-serverless-pipe-agent)
    
7. [Step 3: Add a .env file](#heading-step-3-add-a-env-file)
    
8. [Step 4: Create a serverless memory agent](#heading-step-4-create-a-serverless-memory-agent)
    
9. [Step 5: Add documents to the memory agent](#heading-step-5-add-documents-to-the-memory-agent)
    
10. [Step 6: Generate memory embeddings](#heading-step-6-generate-memory-embeddings)
    
    * [Understanding memory embeddings](#heading-understanding-memory-embeddings)
        
    * [How to generate embeddings?](#heading-how-to-generate-embeddings)
        
11. [Step 7: Integrate memory in Pipe agent](#heading-step-7-integrate-memory-in-pipe-agent)
    
12. [Step 8: Integrate the memory agent in Node.js](#heading-step-8-integrate-the-memory-agent-in-nodejs)
    
13. [Step 9: Start the BaseAI server](#heading-step-9-start-the-baseai-server)
    
14. [Step 10: Run the memory agent](#heading-step-10-run-the-memory-agent)
    
15. [The result](#heading-the-result)
    

## Large Language Models (LLMs) Are Stateless by Nature

LLMs (Large Language Models) are stateless because they don’t retain any memory of previous interactions or the context of past queries beyond the input they're given in a session. Each time an LLM processes a prompt, it operates on that specific prompt without any history from prior ones.

This stateless nature allows the model to treat each request as independent, which simplifies its architecture and training process. But this also means that without mechanisms like RAG (Retrieval-Augmented Generation) or memory (long-term), LLMs can't carry forward information from one interaction to the next.

To introduce continuity or context, developers can implement external systems to manage and inject context, but the model itself doesn't "remember" anything between requests.

### How do we solve this?

By integrating **Memory Agents** by Langbase, we can give LLMs long-term memory—allowing them to store, retrieve, and use information dynamically, making them much more useful for real-world applications.

## What Are Memory Agents?

[Langbase serverless memory agents](https://langbase.com/docs/memory) (long-term memory solution) are designed to acquire, process, retain, and retrieve information seamlessly. They dynamically attach private data to any LLM, enabling context-aware responses in real time and reducing hallucinations.

These agents combine vector storage, Retrieval-Augmented Generation (RAG), and internet access to create a powerful managed context search API. Developers can use them to build smarter, more capable AI applications.

In a RAG setup, memory – when connected directly to a Langbase Pipe Agent – becomes a memory agent. This pairing gives the LLM the ability to fetch relevant data and deliver precise, contextually accurate answers—addressing the limitations of LLMs when it comes to handling private data.

Memory agents ensure secure local memory storage. Data used to create memory embeddings stays protected, processed within secure environments, and only sent externally if explicitly configured. Access is strictly controlled via API keys, ensuring sensitive information remains safe.

Note that pipe is a serverless AI agent. It has agentic memory and tools.

## Prerequisites

Before we begin creating a cold email generator agent, you’ll need to have the following setup and tools ready to go.

In this tutorial, I’ll be using this tech stack:

* [BaseAI](http://baseai.dev/) — the web framework for building AI agents locally.
    
* [Langbase](http://langbase.com/) — the platform to build and deploy your serverless AI agents.
    
* [OpenAI](https://openai.com/) — to get the LLM key for the preferred model.
    

You’ll also need to:

* Sign up on Langbase to get access to the API key.
    
* Sign up on OpenAI to generate the LLM key for the model you want to use (for this demo, I’ll be using GPT-4o mini). You can generate the key [here](https://platform.openai.com/api-keys).
    

## Reference Architecture

Here’s a diagrammatic representation of the entire process of building a serverless AI agent to generate cold emails for job applications:

![Reference architecture of memory agents working](https://cdn.hashnode.com/res/hashnode/image/upload/v1739900463621/e2b6753e-287f-4d69-b453-36d50f316fb8.png align="center")

Let’s start building the agent!

## Step 1: Create a Directory and Initialize npm

To start creating a serverless AI agent that generates cold emails for a job opening, you need to create a directory in your local machine and install all the relevant dev dependencies in it. You can do this by navigating to it and running the following command in the terminal:

```bash
mkdir my-project
npm init -y
npm install dotenv
```

This command will create a package.json file in your project directory with default values. It will also install the `dotenv` package to read environment variables from the `.env` file.

## Step 2: Create a Serverless Pipe Agent

Next, we’ll be creating a [pipe agent](https://langbase.com/docs/pipe/quickstart). Pipes are different from other agents, as they are serverless AI agents with agentic tools that can work with any language or framework. They are easily deployable, and with just one API they let you connect more than 250 LLMs to any data to build any developer API workflow.

To create your AI agent pipe, navigate to your project directory. Run the following command:

```bash
npx baseai@latest pipe
```

Upon running, you’ll see the following prompts:

```bash
BaseAI is not installed but required to run. Would you like to install it? Yes/No
Name of the pipe? email-generator-agent
Description of the pipe? Generates emails for your dream job in seconds
Status of the pipe? Public/Private
System prompt? You are a helpful AI assistant
```

Once you are done with the name, description, and status of the AI agent pipe, everything will be set up automatically for you. Your pipe will be created successfully at `/baseai/pipes/email-generator-agent.ts`.

## Step 3: Add a .env File

Create a `.env` file in the root directory of your project and add the OpenAI and Langbase API keys in it. You can access your Langbase API key from [here](https://langbase.com/docs/api-reference/api-keys).

## Step 4: Create a Serverless Memory Agent

Next, we’ll be creating a memory and then attaching it with the Pipe to make it a memory agent. To do this, run this command in your terminal:

```bash
npx baseai@latest memory
```

Upon running this command, you’ll see the following prompts:

```bash
Name of the memory? email-generator-memory
Description of the memory? Contains my resume
Do you want to create memory from the current project git repository? Yes/No
```

After this, everything will be set up automatically for you and you can access your memory created successfully at `/baseai/memory/email-generator-memory.ts`.

## Step 5: Add Documents to the Memory Agent

Inside `/baseai/memory/email-generator-memory.ts` you’ll see another folder called documents. This is where you’ll store the files you want your AI agent to access. Let’s save your résumé as either a `.pdf` or `.txt` file. Then, I’ll convert it to a markdown file and place it in the `/baseai/memory/email-generator-memory/documents` directory.

This step ensures that the memory agent can process and retrieve information from your documents, making the AI agent capable of generating accurate cold emails based on the experiences and skills provided in the résumé attached.

## Step 6: Generate Memory Embeddings

With your documents added to memory, the next step is generating memory embeddings. But before that, let me quickly explain what embeddings are and why they matter.

### Understanding memory embeddings

Memory embeddings are numerical representations of your documents that enable an AI to grasp context, relationships, and meaning within text. They act as a bridge, converting raw data into a structured format AI can process for semantic search and retrieval.

Without embeddings, AI agents wouldn’t effectively connect user queries with relevant content. Generating embeddings creates a searchable index, allowing the memory agent to deliver accurate, context-aware responses efficiently.

### How to generate embeddings

To generate embeddings for your documents, run the following command in your terminal:

```bash
npx baseai@latest embed -m email-generator-memory
```

Your memory is now ready to be connected with a Pipe (memory agent), enabling your AI agent to fetch precise, context-aware responses from your documents.

## Step 7: Integrate Memory in Pipe Agent

Next, you have to attach the memory you created to your Pipe agent to make it a memory agent. For that, go to `/baseai/pipes/email-generator-agent.ts`. This is what it will look like at the moment:

```typescript
import { PipeI } from '@baseai/core';

const pipePipeWithMemory = (): PipeI => ({
    apiKey: process.env.LANGBASE_API_KEY!, // Replace with your API key https://langbase.com/docs/api-reference/api-keys
    name: 'email-generator-agent',
    description: 'Generates emails for your dream job in seconds',
    status: 'public',
    model: 'openai:gpt-4o-mini',
    stream: true,
    json: false,
    store: true,
    moderate: true,
    top_p: 1,
    max_tokens: 1000,
    temperature: 0.7,
    presence_penalty: 1,
    frequency_penalty: 1,
    stop: [],
    tool_choice: 'auto',
    parallel_tool_calls: false,
    messages: [
        { role: 'system', content: You are a helpful AI assistant. }],
    variables: [],
    memory: [],
    tools: []
});

export default pipePipeWithMemory;
```

Now integrate the memory in the pipe by importing it at the top and calling it as a function in the `memory` array. Also, add the following in the messages content:

```bash
Based on the job description and my resume attached, write a compelling cold email tailored to the job, highlighting my most relevant skills, achievements, and experiences. Ensure the tone is professional yet approachable, and include a strong call to action for a follow-up or interview.
```

This is what the code will look like after doing all of this:

```typescript
import { PipeI } from '@baseai/core';
import emailGeneratorMemoryMemory from '../memory/email-generator-memory';

const pipeEmailGeneratorAgent = (): PipeI => ({
 // Replace with your API key https://langbase.com/docs/api-reference/api-keys
 apiKey: process.env.LANGBASE_API_KEY!,
 name: 'email-generator-agent',
 description: 'Generates emails for your dream job in seconds',
 status: 'private',
 model: 'openai:gpt-4o-mini',
 stream: true,
 json: false,
 store: true,
 moderate: true,
 top_p: 1,
 max_tokens: 1000,
 temperature: 0.7,
 presence_penalty: 1,
 frequency_penalty: 1,
 stop: [],
 tool_choice: 'auto',
 parallel_tool_calls: true,
 messages: [{ role: 'system', content: Based on the job description and my resume attached, write a compelling cold email tailored to the job, highlighting my most relevant skills, achievements, and experiences. Ensure the tone is professional yet approachable, and include a strong call to action for a follow-up or interview. }],
 variables: [],
 memory: [emailGeneratorMemoryMemory()],
 tools: []
});

export default pipeEmailGeneratorAgent;
```

## Step 8: Integrate the Memory Agent in Node.js

Now we’ll integrate the memory agent you created into the Node.js project to build an interactive command-line interface (CLI) for the document attached. This Node.js project will serve as the base for testing and interacting with the memory agent (in the beginning of the tutorial, we set up a Node.js project by initializing npm).

Now, create an index.ts file:

```bash
touch index.ts
```

In this TypeScript file, import the pipe agent you created. We will use the pipe primitive from `@baseai/core` to run the pipe.

Add the following code to the `index.ts` file:

```typescript
import 'dotenv/config';
import { Pipe } from '@baseai/core';
import inquirer from 'inquirer';
import ora from 'ora';
import chalk from 'chalk';
import pipeEmailGeneratorAgent from './baseai/pipes/email-generator-agent';

const pipe = new Pipe(pipeEmailGeneratorAgent());

async function main() {

   const initialSpinner = ora('Conversation with Memory agent...').start();
   try {
       const { completion: calculatorTool} = await pipe.run({
           messages: [{ role: 'user', content: 'Hello' }],
       });
       initialSpinner.stop();
       console.log(chalk.cyan('Report Generator Agent response...'));
       console.log(calculatorTool);
   } catch (error) {
       initialSpinner.stop();
       console.error(chalk.red('Error processing initial request:'), error);
   }

   while (true) {
       const { userMsg } = await inquirer.prompt([
           {
               type: 'input',
               name: 'userMsg',
               message: chalk.blue('Enter your query (or type "exit" to quit):'),
           },
       ]);


       if (userMsg.toLowerCase() === 'exit') {
           console.log(chalk.green('Goodbye!'));
           break;
       }


       const spinner = ora('Processing your request...').start();


       try {
           const { completion: reportAgentResponse } = await pipe.run({
               messages: [{ role: 'user', content: userMsg }],
           });


           spinner.stop();
           console.log(chalk.cyan('Agent:'));
           console.log(reportAgentResponse);
       } catch (error) {
           spinner.stop();
           console.error(chalk.red('Error processing your request:'), error);
       }
   }
}

main();
```

This code creates an interactive CLI for chatting with an AI agent, using a pipe from the `@baseai/core` library to process user input. Here's what happens:

* It imports necessary libraries such as `dotenv` for environment configuration, `inquirer` for user input, `ora` for loading spinners, and `chalk` for colored output. Make sure you install these libraries first using this command in your terminal: `npm install ora inquirer`.
    
* A pipe object is created from the BaseAI library using a predefined memory called `email-generator-agent`.
    

In the `main()` function:

* A spinner starts while an initial conversation with the AI agent is initiated with the message 'Hello'.
    
* The response from the AI is displayed.
    
* A loop runs to continually ask the user for input and send queries to the AI agent.
    
* The AI's responses are shown, and the process continues until the user types "exit”.
    

## Step 9: Start the BaseAI Server

To run the memory agent locally, you need to start the BaseAI server first. Run the following command in your terminal:

```bash
npx baseai@latest dev
```

## Step 10: Run the Memory Agent

Run the `index.ts` file using the following command:

```bash
npx tsx index.ts
```

## The Result

In your terminal, you’ll be prompted to "Enter your query." For example, let’s paste a job description and ask to generate an email from our end showing interest. And it will give us the response with correct sources/citations as well.

With this setup, we’ve built a Cold Email Generator agent that uses the power of LLMs and Langbase memory agents to overcome LLMs' limitations, ensuring accurate responses without hallucinating on private data.

Here’s a demo of the end result:

%[https://youtu.be/ns7UqX6Ycs8] 

Thank you for reading!

Connect with me by 🙌:

* Subscribing to my [YouTube](https://www.youtube.com/@AIwithMahamCodes) Channel. If you are willing to learn about AI and agents.
    
* Subscribing to my free newsletter [“The Agentic Engineer”](https://mahamcodes.substack.com/) where I share all the latest AI and agents news/trends/jobs and much more.
    
* Follow me on [X (Twitter)](https://x.com/MahamDev).
