---
title: How to Make LLMs Better at Math Using AI Agents, MathJS, and BaseAI Tool Calls
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2024-12-19T14:53:46.717Z'
originalURL: https://freecodecamp.org/news/make-llms-better-at-math-with-ai-agents
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1734537732263/2ec966b6-d1d3-4d0f-ae37-982ef26ebc55.jpeg
tags:
- name: llm
  slug: llm
- name: AI
  slug: ai
- name: ai agents
  slug: ai-agents
- name: openai
  slug: openai
seo_title: null
seo_desc: Large Language Models (LLMs) like GPT often struggle to answer mathematical
  questions. In fact, if you ask a human a tough math question, like what is 185 cm
  in ft, they’ll struggle as well. They’d likely need a calculator to perform this
  conversion ...
---

Large Language Models (LLMs) like GPT often struggle to answer mathematical questions. In fact, if you ask a human a tough math question, like what is 185 cm in ft, they’ll struggle as well. They’d likely need a calculator to perform this conversion – and so do LLMs.

LLMs are built to handle natural language. While generally being good at generating words and stringing together language, when it comes to math, they often need help.

Unlike a calculator or math library, LLMs cannot sometimes reason or process symbolic logic. So, while they can manage basic arithmetic, especially if it's something familiar from their training data, they typically struggle with more complex problems, particularly word problems.

The main question is how to fix this LLM limitation?

No doubt, LLMs have evolved with the launch of reasoning models like GPT-o1 or Llama 3.3. But they still hallucinate, lack real-time data access, struggle with complex math, and produce non-deterministic outputs. Fortunately, we can solve this problem using AI agents.

## What is an AI Agent?

AI agents are autonomous software that use LLMs to perform tasks beyond simple text generation.

They make decisions and execute actions. AI agents rely on LLMs for language understanding but add capabilities like memory, real-time interaction, and decision-making.

## How AI Agents Solve LLM Limitations

Agents augment the capabilities of LLMs in the following ways:

* **Memory:** AI agents help LLMs retain context from past interactions, improving long-term conversation coherence.
    
* **Asynchronous processing:** Agents handle multiple tasks at once, enhancing efficiency.
    
* **Fact-checking:** They connect to real-time data sources to verify information.
    
* **Enhanced math:** They integrate tools to handle complex calculations.
    
* **Consistent output:** Agents standardize LLM outputs for uniform formatting.
    

To help address some of the math limitations LLMs experience, let’s create an AI agent that builds a calculator using MathJS and BaseAI tool calls.

## Prerequisites

In this tutorial, I’ll be using the following tech stack:

* [MathJS](https://mathjs.org/) — an extensive math library for JavaScript and Node.js.
    
* [BaseAI](https://baseai.dev) — the web framework for building AI agents locally.
    
* [Langbase](https://langbase.com) — the platform to build and deploy your serverless AI agents.
    
* [OpenAI](https://openai.com) — to get the LLM key for the preferred model.
    

You’ll also need to:

* Sign up on Langbase to get access to the API key.
    
* Sign up on OpenAI to generate the LLM key for the model you want to use (for this demo, I’ll be using GPT-4o mini).
    

Let’s get started!

## Step 1: Create a Directory and Initialize npm

To start creating an AI agent, you need to create a directory in your local machine and install all the relevant dev dependancies in it. You can do this by navigating to it and running the following command in the terminal:

```bash
mkdir my-project

npm init -y

npm install dotenv mathjs
```

This command will create a `package.json` file in your project directory with default values. It will also install the `dotenv` package to read environment variables from the `.env` file, and `mathjs` to handle math operations.

## Step 2: Create an AI Agent Pipe

Next, we’ll be creating an AI agent pipe. Pipes are different from other agents, as they **are serverless AI agents with agentic tools** that can work with any language or framework. They are easily deployable, and with just one API they let you connect 100+ LLMs to any data to build any developer API workflow.

To create your AI agent pipe, navigate to your project directory. Run the following command:

```bash
npx baseai@latest pipe
```

Upon running that command, you’ll see the following prompts:

```bash
BaseAI is not installed but required to run. Would you like to install it? Yes/No

Name of the pipe? pipe-with-tool

Description of the pipe? An AI agent pipe that can call tools

Status of the pipe? Public/Private

System prompt? You are a helpful AI assistant
```

Once you are done with the name, description, and status of the AI agent pipe, everything will be set up automatically for you. Your pipe will be created successfully at `/baseai/pipes/pipe-with-tool.ts`.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Pipe is a serverless AI agent. It has agentic memory and tools.</div>
</div>

## Step 3: Add a .env File

Create a `.env` file in the root directory of your project and add the [OpenAI](https://platform.openai.com/api-keys) and Langbase API key in it. You can access your Langbase API key from [here](https://langbase.com/docs/api-reference/api-keys).

## Step 4: Configure the AI Agent Pipe

In this step, we’ll configure the AI agent pipe created according to our needs.

Navigate to your project directory and open the AI agent pipe you created. You can add a system prompt to the pipe if you want. I’m sticking to `You are a helpful AI assistant that will work as a calculator.` This is what it will look like:

```typescript
import { PipeI } from '@baseai/core';

const pipePipeWithTool = (): PipeI => ({
   apiKey: process.env.LANGBASE_API_KEY!,
   name: 'pipe-with-tool',
   description: 'An AI agent pipe that can call tools',
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
   messages: [{ role: 'system', content: `You are a helpful AI assistant that will work as a calculator.` }],
   variables: [],
   memory: [],
   tools: []
});

export default pipePipeWithTool;
```

## Step 5: Create a Calculator Tool

Tool calling lets an LLM use external tools, such as functions, APIs, or other resources, to get information or perform tasks beyond its built-in knowledge.

In this step, we'll create a **Calculator Tool** using BaseAI tools. This tool will handle all mathematical computations in your project, ensuring they are error-free and trustworthy. The tool is versatile and suitable for both simple calculations (e.g., `5+7`) and more advanced ones (e.g., `sin(pi/4) + log(10)`).

It will also be particularly helpful in reducing hallucinations, which it can do by offloading computations to an external tool This avoids incorrect or fabricated answers that LLMs might otherwise generate. It also reduces the likelihood of getting incorrect responses from the LLM by rechecking or gathering additional data to ensure accuracy.

By using BaseAI's smart tool-calling and memory features, we can reduce AI hallucinations by **21%** while improving the model's ability to self-correct its outputs.

These enhancements are useful when dealing with complex mathematical expressions or formula evaluations and should really improve the quality and accuracy of the LLM’s answers.

To create a calculator tool in your project that will be responsible for doing all the calculations without errors, run this command in your terminal:

```bash
npx baseai@latest tool
```

You’ll be asked to provide a name and description of the tool in your terminal. This is what I’m providing:

```bash
Name of the tool? Calculator

Description of the tool? Evaluate mathematical expressions
```

Your tool will be created at `/baseai/tools/calculator.ts`.

## Step 6: Configure the Calculator Tool

To configure the tool, navigate to your project directory and open the tool you created. You can find it at `/baseai/tools/calculator.ts`.

This is what the code will look like:

```typescript
import { ToolI } from '@baseai/core';

export async function calculator() {
   // Add your tool logic here
   // This function will be called when the tool is executed
}

const toolCalculator = (): ToolI => ({
   run: calculator,
   type: 'function' as const,
   function: {
       name: 'toolCalculator',
       description: 'Evaluate mathematical expressions',
       parameters: {}
   }
});

export default toolCalculator;
```

The `run` key in the `toolCalculator` object is the function that will be executed when the tool is called. You can write your logic to get the mathematical calculations for a given function.

Update the calculator tool’s description and code by adding parameters to the calculator function. The LLM will give values to these parameters when it calls the tool. And it’ll even import math from `mathjs`. This is the final code:

```typescript
import * as math from 'mathjs';

export async function calculator({expression}: {expression: string}) {
   return math.evaluate(expression);
}

const toolCalculator = () => ({
   run: calculator,
   type: 'function' as const,
   function: {
       name: 'calculator',
       description:
           `A tool that can evaluate mathematical expressions. ` +
           `Example expressions: ` +
           `'5.6 * (5 + 10.5)', '7.86 cm to inch', 'cos(80 deg) ^ 4'.`,
       parameters: {
           type: 'object',
           required: ['expression'],
           properties: {
               expression: {
                   type: 'string',
                   description: 'The mathematical expression to evaluate.',
               },
           },
       },
   },
});

export default toolCalculator;
```

## Step 7: Integrate the Tool in the AI Agent Pipe

In this step, we’ll integrate the tool in the AI agent pipe we created. For that, open the pipe file present at `/baseai/pipes/pipe-with-tool.ts` and import the calculator tool at the top of the file. We will also call the calculator tool in the tools array of the pipe.

```typescript
import {PipeI} from '@baseai/core';
import toolCalculator from '../tools/calculator';

const pipeWithTools = (): PipeI => ({
   apiKey: process.env.LANGBASE_API_KEY!,
   name: 'pipe-with-tool',
   description: 'An AI agent pipe that can call tools',
   status: 'public',
   model: 'openai:gpt-4o-mini',
   stream: false,
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
   messages: [{role: 'system', content: `You are a helpful AI assistant that will work as a calculator.`}],
   variables: [],
   memory: [],
   tools: [ toolCalculator()],
});

export default pipeWithTools;
```

## Step 8: Integrate AI Agent Pipe in Node.js

Now we’ll integrate the AI agent pipe you created into the Node.js project to build an interactive command-line interface (CLI) for the calculator tool. This Node.js project will serve as the base for testing and interacting with the AI agent pipe (in the beginning of the tutorial, we set up a Node.js project by initializing npm).

Now, create an `index.ts` file:

```bash
touch index.ts
```

In this TypeScript file, import the AI agent pipe you created. We will use the pipe primitive from `@baseai/core` to run the pipe.

Add the following code to the `index.ts` file:

```typescript
import 'dotenv/config';
import { Pipe } from '@baseai/core';
import inquirer from 'inquirer';
import ora from 'ora';
import chalk from 'chalk';
import pipePipeWithTool from './baseai/pipes/pipe-with-tool';

const pipe = new Pipe(pipePipeWithTool());

async function main() {

   const initialSpinner = ora('Conversation with Math agent...').start();
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

* It imports necessary libraries such as `dotenv` for environment configuration, `inquirer` for user input, `ora` for loading spinners, and `chalk` for colored output. Make sure you install these libraries first using this command in your terminal `npm install ora inquirer`.
    
* A pipe object is created from the BaseAI library using a predefined tool called `pipe-with-tool`.
    

In the `main()` function:

* A spinner starts while an initial conversation with the AI agent is initiated with the message 'Hello'.
    
* The response from the AI is displayed.
    
* A loop runs to continually ask the user for input and send queries to the AI agent.
    
* The AI's responses are shown, and the process continues until the user types "exit”.
    

## Step 9: Start the BaseAI Server

To run the AI agent pipe locally, you need to start the BaseAI server. Run the following command in your terminal:

```bash
npx baseai@latest dev
```

## Step 10: Run the AI Agent Pipe

Run the `index.ts` file using the following command:

```bash
npx tsx index.ts
```

## Result

In your terminal, you’ll be prompted to **"Enter your query."** For example, let’s ask: **"What is 120 cm in feet?"** LLMs usually hallucinate when converting to feet. But because of the self-healing tool calling of the BaseAI framework, the tool detects and corrects its own errors.

With this setup, we’ve successfully built an AI agent that uses **MathJS** and **BaseAI tool calls** to eliminate the mathematical limitations of LLMs.

Here’s a demo of the end result:

%[https://youtu.be/bBukL1Vte0g] 

## Wrapping Up

As Large Language Models (LLMs) often struggle with mathematical reasoning due to their focus on language, leading to frequent errors in calculations, especially with complex math problems.

AI agents extend LLM capabilities by integrating tool calls. They handle real-time data, ensure more consistent outputs, and reduce hallucination.

By incorporating MathJS and tool calls via the BaseAI framework, developers can create custom serverless AI agents called pipes that serve as reliable calculators and address LLMs' inherent limitations.
