---
title: How to Build Autonomous Agents using Prompt Chaining with AI Primitives (No
  Frameworks)
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2025-04-21T15:22:42.999Z'
originalURL: https://freecodecamp.org/news/build-autonomous-agents-using-prompt-chaining-with-ai-primitives
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745248868960/12efd5ab-3d9b-4c93-979f-45bde796639b.png
tags:
- name: llm
  slug: llm
- name: ai-agent
  slug: ai-agent
- name: AI
  slug: ai
seo_title: null
seo_desc: 'Autonomous agents might sound complex, but they don’t have to be. These
  are AI systems that can make decisions and take actions on their own to achieve
  a goal – usually by using LLMs, various tools, and memory to reason through a task.

  You can build ...'
---

Autonomous agents might sound complex, but they don’t have to be. These are AI systems that can make decisions and take actions on their own to achieve a goal – usually by using LLMs, various tools, and memory to reason through a task.

You can build powerful agentic systems without heavyweight frameworks or orchestration engines. One of the simplest and most effective ways to do that is to use Langbase agentic architectures (built with AI primitives that don't require a framework to ship scalable AI agentic systems).

In this article, we’ll dive into one of Langbase's agentic architectures: prompt chaining. We’ll look at why it’s useful and how to implement it by building a prompt chaining agent.

### Table of Contents

1. [Prerequisites](#heading-prerequisites)
    
2. [AI primitives (agentic architecture)](#heading-ai-primitives-agentic-architecture)
    
3. [What is prompt chaining?](#heading-what-is-prompt-chaining)
    
4. [Prompt chaining architecture](#heading-prompt-chaining-architecture)
    
5. [Langbase SDK](#heading-langbase-sdk)
    
6. [Building a prompt chaining agent using Langbase Pipes](#heading-building-a-prompt-chaining-agent-using-httpslangbasecomlangbase-pipes)
    
    * [Step 1: Setup your project](#heading-step-1-setup-your-project)
        
    * [Step 2: Get Langbase API Key](#heading-step-2-get-langbase-api-key)
        
    * [Step 3: Add LLM API keys](#heading-step-3-add-llm-api-keys)
        
    * [Step 4: Add logic in prompt-chaining.ts file](#heading-step-4-add-logic-in-prompt-chainingts-file)
        
    * [Step 5: Run the file](#heading-step-5-run-the-file)
        
7. [The result](#heading-the-result)
    

## Prerequisites

Before we begin creating a prompt chaining agent, you’ll need to have the following setup and tools ready to go.

In this tutorial, I’ll be using the following tech stack:

* [Langbase](http://langbase.com/) – the platform to build and deploy your serverless AI agents.
    
* [Langbase SDK](https://langbase.com/docs/sdk) – a TypeScript AI SDK, designed to work with JavaScript, TypeScript, Node.js, Next.js, React, and the like.
    
* [OpenAI](https://openai.com/) – to get the LLM key for the preferred model.
    

You’ll also need to:

* Sign up on Langbase to get access to the API key.
    
* Sign up on OpenAI to generate the LLM key for the model you want to use (for this demo, I’ll be using the `openai:gpt-4o-mini` model). You can generate the key [here](https://platform.openai.com/api-keys).
    

## AI Primitives (Agentic Architecture)

An AI primitive level approach means building AI systems using the most basic building blocks – without relying on heavy abstractions, orchestration engines, or full-blown frameworks.

Langbase Pipe and Memory agents serve as these building blocks.

[Pipe agents](https://langbase.com/docs/pipe) on Langbase are different from other agents. They are serverless AI agents with agentic tools that can work with any language or framework. Pipe agents are easily deployable, and with just one API they let you connect 250+ LLMs to any data to build any developer API workflow.

[Langbase memory agents](https://langbase.com/docs/memory) (long-term memory solution) are designed to acquire, process, retain, and retrieve information seamlessly. They dynamically attach private data to any LLM, enabling context-aware responses in real time and reducing hallucinations. Memory, when connected to a pipe agent, becomes a memory agent.

With these building blocks (AI primitives) you can build entire agentic workflows. For this, Langbase agentic architectures serves as a boilerplate in building, deploying, and scaling autonomous agents.

Let’s look at one of the agentic architectures: prompt chaining.

## What is Prompt Chaining?

Prompt chaining is an agent architecture where a task is broken down into a sequence of prompts. Each step passes its output to the next, enabling the LLM to handle more complex workflows with higher accuracy.

This is particularly useful for structured tasks like:

* Document summarization and analysis
    
* Multi-step content generation
    
* Data transformation and cleanup
    
* Content validation and refinement
    

Rather than relying on a single prompt to do everything, you split the work into focused steps. This makes it easier to debug, improves output quality, and introduces natural "checkpoints" in your AI workflow.

## Prompt Chaining Architecture

Here’s a reference architecture explaining the workflow:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXchmBDXvU8DXnQu7EjqKoSUTdxQ__KsTZemZ9yaTGpeCAMUc1RX_Swby9NOtxXwONFdKGPrjFcjVZhQmQoKe1eu2nceFWGLaPA8bpu-JYB7rh4ChJmExLRRWJzjB4686HjUsP_t?key=l4b_IFG3ufUXGX7WLcs4Dknq align="left")

This diagram is a visual reference for how prompt chaining can be used to build a lightweight agentic system using just LLM calls and conditional logic – without any heavyweight frameworks.

Here’s a breakdown of what’s happening in the flow:

1. **In → LLM Call**
    

* Takes the initial input and runs the first LLM call.
    
* Produces Output 1.
    

2. **Gate**
    

* Evaluates Output 1 to decide the next step.
    
* Acts as a conditional checkpoint (for example, success/failure, intent validation, confidence threshold).
    

3. **If Gate passes:**
    

* Proceeds to LLM Call 2 with Output 1 as input.
    
* LLM Call 2 produces Output 2.
    
* Output 2 goes into LLM Call 3, which generates the final result.
    
* Final output flows into the Out.
    

4. **If Gate fails:**
    

* The flow terminates early at Exit.
    
* Skips further LLM calls, saving compute and avoiding invalid outputs.
    

## Langbase SDK

The Langbase SDK makes it easy to build powerful AI agents using TypeScript. It gives you everything you need to work with any LLM, connect your own embedding models, manage document memory, and build AI agents that can reason and respond.

The SDK [i](http://langbase.com)s designed to work with Node.js, Next.js, React, or any modern JavaScript stack. You can use it to upload documents, create semantic memory, and run AI workflows (called Pipes agents) with just a few lines of code.

Langbase is an API-first AI platform, and its TypeScript SDK smooths out the experience – making it easy to get started without dealing with infrastructure. Just drop in your API key, write your logic, and you're good to go.

Now that you know about Langbase SDK, let’s start building the prompt chaining agent.

## Building a Prompt Chaining Agent using Langbase Pipes

Let’s walk through a real prompt chaining agentic system built using Langbase Pipe agents (serverless AI agents with unified APIs for every LLM). For this, we’ll be setting up a basic Node.js project.

We’ll be implementing a sequential product marketing content pipeline that transforms a raw product description into polished marketing copy through three stages (that is, the creation of three Pipe agents):

### First Stage (Summary Agent):

* Takes a raw product description
    
* Condenses it into two concise sentences
    
* Has a quality gate that checks if the summary is detailed enough (at least 10 words)
    

### Second Stage (Features Agent):

* Takes the summary from stage 1
    
* Extracts and formats key product features as bullet points
    

### Final Stage (Marketing Copy Agent):

* Takes the bullet points from stage 2
    
* Generates refined marketing copy for the product
    

All stages will be using the OpenAI 4o-mini model through the Langbase SDK. The best part is that you can use different LLM models for each stage/Pipe agent creation as well.

What makes this interesting is its pipeline approach. Each stage builds upon the output of the previous stage, with a quality check after the summary stage to ensure the pipeline maintains high standards.

Let’s begin with the creation of this prompt chaining agentic system.

### Step 1: Setup Your Project

I’ll be building a basic Node.js app in TypeScript that uses the Langbase SDK to create a scalable prompt chaining agentic system. It will work without any framework, following an AI primitive level approach.

To get started with that, create a new directory for your project and navigate to it:

```bash
mkdir agentic-architecture && cd agentic-architecture
```

Then initialize a Node.js project and create a TypeScript file by running this command in your terminal:

```bash
npm init -y && touch prompt-chaining.ts
```

The `prompt-chaining.ts` file will contain code of all the agent creations in it.

After this, we will be using the Langbase SDK to create the agents and `dotenv` to manage environment variables. So, let's install these dependencies.

```bash
npm i langbase dotenv
```

### Step 2: Get Langbase API Key

Every request you send to Langbase needs an API key. You can generate API keys from the [Langbase studio](https://studio.langbase.com/) by following these steps:

1. Switch to your user or org account.
    
2. From the sidebar, click on the `Settings` menu.
    
3. In the developer settings section, click on the `Langbase API keys` link.
    
4. From here you can create a new API key or manage existing ones.
    

For more details, you can visit the Langbase API keys documentation.

After generating the API key, create an `.env` file in the root of your project and add your Langbase API key in it:

```bash
LANGBASE_API_KEY=xxxxxxxxx
```

Replace xxxxxxxxx with your Langbase API key.

### Step 3: Add LLM API keys

Once you have the Langbase API key, you’ll be needing the LLM key as well to run the RAG agent. If you have set up LLM API keys in your profile, the AI memory and agent pipe will automatically use them. Otherwise navigate to the LLM API keys page and add keys for different providers like OpenAI, Anthropic, and so on.

Follow these steps to add the LLM keys:

1. Add LLM API keys in your account using Langbase studio
    
2. Switch to your user or org account.
    
3. From the sidebar, click on the `Settings` menu.
    
4. In the developer settings section, click on the `LLM API keys` link.
    
5. From here you can add LLM API keys for different providers like OpenAI, TogetherAI, Anthropic, and so on.
    

### Step 4: Add logic in `prompt-chaining.ts` file

In the `prompt-chaining.ts` file you created in Step 1, add the following code:

```typescript
import dotenv from 'dotenv';
import { Langbase } from 'langbase';


dotenv.config();


const langbase = new Langbase({
   apiKey: process.env.LANGBASE_API_KEY!
});


async function main(inputText: string) {
   // Prompt chaining steps
   const steps = [
       {
           name: `summary-agent-${Date.now()}`,
           model: 'openai:gpt-4o-mini',
           description:
               'summarize the product description into two concise sentences',
           prompt: `Please summarize the following product description into two concise
           sentences:\n`
       },
       {
           name: `features-agent-${Date.now()}`,
           model: 'openai:gpt-4o-mini',
           description: 'extract key product features as bullet points',
           prompt: `Based on the following summary, list the key product features as
           bullet points:\n`
       },
       {
           name: `marketing-copy-agent-${Date.now()}`,
           model: 'openai:gpt-4o-mini',
           description:
               'generate a polished marketing copy using the bullet points',
           prompt: `Using the following bullet points of product features, generate a
           compelling and refined marketing copy for the product, be precise:\n`
       }
   ];


   //  Create the pipe agents
   await Promise.all(
       steps.map(step =>
           langbase.pipes.create({
               name: step.name,
               model: step.model,
               messages: [
                   {
                       role: 'system',
                       content: `You are a helpful assistant that can ${step.description}.`
                   }
               ]
           })
       )
   );


   // Initialize the data with the raw input.
   let data = inputText;


   try {
       // Process each step in the workflow sequentially.
       for (const step of steps) {
           // Call the LLM for the current step.
           const response = await langbase.pipes.run({
               stream: false,
               name: step.name,
               messages: [{ role: 'user', content: `${step.prompt} ${data}` }]
           });


           data = response.completion;


           console.log(`Step: ${step.name} \n\n Response: ${data}`);


           // Gate on summary agent output to ensure it is not too brief.
           // If summary is less than 10 words, throw an error to stop the workflow.
           if (step.name === 'summary-agent' && data.split(' ').length < 10) {
               throw new Error(
                   'Gate triggered for summary agent. Summary is too brief. Exiting workflow.'
               );
               return;
           }
       }
   } catch (error) {
       console.error('Error in main workflow:', error);
   }


   // The final refined marketing copy
   console.log('Final Refined Product Marketing Copy:', data);
}


const inputText = `Our new smartwatch is a versatile device featuring a high-resolution display,
long-lasting battery life,fitness tracking, and smartphone connectivity. It's designed for
everyday use and is water-resistant. With cutting-edge sensors and a sleek design, it's
perfect for tech-savvy individuals.`;


main(inputText);
```

Here’s a breakdown of the above code:

Setup and initialization:

* `dotenv` loads `env` variables from the `.env` file for secure API key access.
    
* Langbase is imported from the SDK to interact with the API.
    
* A Langbase client instance is created using your API key.
    

Define the AI steps (prompt chain):

* Three AI agents (steps) are defined for a pipeline:
    
    1. **Summarization Agent**: Summarizes the input product description into 2 sentences.
        
    2. **Feature Extraction Agent**: Extracts key features from the summary as bullet points.
        
    3. **Marketing Copy Agent**: Turns bullet points into polished marketing copy.
        
* Each agent uses `openai:gpt-4o-mini` as the LLM.
    

Create Langbase Pipes (agents):

* Langbase pipes are created for each step using `langbase.pipes.create(...)`.
    
* Each pipe has a unique name (timestamped) and a system message guiding its purpose.
    

Run the workflow (sequential processing):

* Input text flows through each step one by one:
    
    * The output of one step becomes the input for the next.
        
    * Pipes are run using `langbase.pipes.run(...)`.
        
* Intermediate outputs are logged after each step.
    

Validation check (gatekeeping):

* If the summary output is too short (less than 10 words), the workflow stops with an error.
    

Final Output:

* After all steps, the final result is a refined marketing copy printed to the console.
    

For this article, we’re using a demo smartwatch product description to view the result in the `inputText` field.

### Step 5: Run the file

To run the `prompt-chaining.ts` file to view the results, you need to:

* Add TypeScript as a dependency
    
* Add a script to run TypeScript files
    
* Add a TypeScript configuration file
    

For it lets first install `pnpm` by running this command in your terminal:

```bash
pnpm install
```

Then in your terminal again, run this command to add relevant dependencies and configuration files:

```bash
pnpm add -D typescript ts-node @types/node
```

After that, create a TypeScript configuration file `tsconfig.json`:

```bash
pnpm exec tsc --init
```

And update the `package.json` to add the relevant script. This is what your `package.json` should look like after updating:

```json
{
 "name": "agentic-architectures",
 "version": "1.0.0",
 "main": "index.js",
 "scripts": {
   "test": "echo \"Error: no test specified\" && exit 1",
   "prompt-chaining": "ts-node prompt-chaining.ts"
 },
 "keywords": [],
 "author": "",
 "license": "ISC",
 "description": "",
 "dependencies": {
   "dotenv": "^16.5.0",
   "langbase": "^1.1.55"
 },
 "devDependencies": {
   "@types/node": "^22.14.1",
   "ts-node": "^10.9.2",
   "typescript": "^5.8.3"
 }
}
```

Now let’s run the project by pnpm run prompt-chaining

## The Result

After running the project, you’ll see the result of the example smartwatch product description in your console as follows:

```bash
Step: summarize-description
Response: This smartwatch combines fitness tracking and smartphone connectivity with a high-resolution display and long-lasting battery. Designed for everyday use with a sleek, water-resistant build, it's ideal for tech enthusiasts.

Step: extract-features
Response: Okay, here are the key product features extracted from the summary:

Fitness Tracking
Smartphone Connectivity
High-Resolution Display
Long-Lasting Battery
Sleek Design
Water-Resistant Build
Designed for Everyday Use
Step: refine-marketing-copy
Response: ## Elevate Your Everyday with Seamless Connectivity and Unrivaled Performance.

Experience the perfect fusion of style and functionality with our revolutionary device, designed to seamlessly integrate into your active lifestyle. Stay motivated and informed with comprehensive Fitness Tracking, while effortlessly staying connected via Smartphone Connectivity.

Immerse yourself in vibrant clarity with the stunning High-Resolution Display, and power through your day without interruption thanks to the Long-Lasting Battery. Encased in a Sleek Design, this device is as stylish as it is practical.

Built to withstand the rigors of daily life, the Water-Resistant Build ensures worry-free wear, rain or shine. Engineered for comfort and performance, this device is Designed for Everyday Use, empowering you to live your best life, effortlessly.
```

This is how you can build a prompt chaining agentic system with AI primitives (no framework) using the Langbase SDK and Langbase agentic architectures.

Thank you for reading!

Connect with me by 🙌:

* Subscribing to my [YouTube](https://www.youtube.com/@AIwithMahamCodes) Channel. If you are willing to learn about AI and agents.
    
* Subscribing to my free newsletter [“The Agentic Engineer”](https://mahamcodes.substack.com/) where I share all the latest AI and agents news/trends/jobs and much more.
    
* Follow me on [X (Twitter)](https://x.com/MahamDev).
