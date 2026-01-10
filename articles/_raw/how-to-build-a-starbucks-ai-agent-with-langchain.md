---
title: 'How to Build an AI Agent with LangChain and LangGraph: Build an Autonomous
  Starbucks Agent'
subtitle: ''
author: Djibril-M🍀
co_authors: []
series: null
date: '2025-12-19T00:21:01.530Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-starbucks-ai-agent-with-langchain
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765630477745/8dffec85-c3c4-4d83-9aa4-f332439d4663.png
tags:
- name: ai agents
  slug: ai-agents
- name: langchain
  slug: langchain
- name: nestjs
  slug: nestjs
- name: handbook
  slug: handbook
seo_title: null
seo_desc: Back in 2023, when I started using ChatGPT, it was just another chatbot
  that I could ask complex questions to and it would identify errors in my code snippets.
  Everything was fine. The application had no memory of previous states or what was
  said the...
---

Back in 2023, when I started using ChatGPT, it was just another chatbot that I could ask complex questions to and it would identify errors in my code snippets. Everything was fine. The application had no memory of previous states or what was said the day before.

Then in 2024, everything started to change. We went from a stateless chatbot to an AI agent that could call tools, search the internet, and generate download links.

At this point, I started to get curious. How can an LLM search the internet? An infinite number of questions were flowing through my head. Can it create its own tools, programs, or execute its own code? It felt like we were heading toward the Skynet (Terminator) revolution.

I was just ignorant 😅. But that's when I started my research and discovered LangChain, a tool that promises all those miracles without a billion-dollar budget.

In this article, you’ll build a fully functional AI agent using LangChain and LangGraph. You’ll start by defining structured data using Zod schemas, then parsing them for AI understanding. Next, you’ll learn about summarizing data into text, creating tools the agent can call, and setting up LangGraph nodes to orchestrate workflows.

You’ll see how to compile the workflow graph, manage state, and persist conversation history using MongoDB. By the end, you’ll have a working Starbucks barista AI that demonstrates how to combine reasoning, tool execution, and memory in a single agent.

## Table of Contents

* [Prerequisites](#heading-prerequisites)
    
* [What is an LLM Agent?](#heading-what-is-an-llm-agent)
    
* [Project Setup](#heading-project-setup)
    
* [Data Schematization with Zod](#heading-data-schematization-with-zod)
    
* [How to Parse the Schema](#heading-how-to-parse-the-schema)
    
* [Data-to-Text Summarization](#heading-data-to-text-summarization)
    
* [How to Persist Orders with MongoDB in NestJS](#heading-how-to-persist-orders-with-mongodb-in-nestjs)
    
* [LangGraph State/Annotation Terms](#heading-langgraph-stateannotation-terms)
    
* [How to Create Tools for the Agent](#heading-how-to-create-tools-for-the-agent)
    
* [LangGraph Nodes (Workflow Components)](#heading-langgraph-nodes-workflow-components)
    
* [Graph Declaration](#heading-graph-declaration)
    
* [Workflow Compilation and State Persistence (Final Part)](#heading-workflow-compilation-and-state-persistence-final-part)
    
* [Conclusion](#heading-conclusion)
    

## Prerequisites

To take full advantage of this article, you should have a basic understanding of TypeScript, Node.js, and a bit of NestJS will help, as it’s the backend framework we’ll be using.

## **What is an LLM Agent?**

By definition, an LLM agent is a software program that’s capable of perceiving its environment, making decisions, and taking autonomous actions to achieve specific goals. It often does this by interacting with tools and systems.

Many frameworks and conventions were created to achieve this, and one of the most famous and widely used is the ReAct (Reason & Act) framework.

With this framework, the LLM receives a prompt, thinks, decides the next action (this can be calling a specific tool), and receives the tool data. Once the tool’s response has been received, the AI model observes the response, generates its own response, and plans its next actions based on the tool’s response.

You can read more about this concept on the official [white paper](https://arxiv.org/abs/2210.03629). And here’s a diagram that summarizes the entire process:

![Diagram illustrating an LLM agent workflow: the agent receives a prompt, reasons, decides an action (such as calling a tool), observes the tool’s response, generates its own response, and iteratively plans its next actions using the ReAct framework](https://cdn.hashnode.com/res/hashnode/image/upload/v1765064426716/b1e6d7b2-4e4b-43c4-af5c-9cd49b27a864.png align="center")

Note that the workflow is not limited to a single tool invocation – it can proceed through several rounds before returning to the user.

But for an LLM agent to be truly human-like and act with knowledge of the past, it requires a memory. This enables it to recall previous prompts and responses, maintaining consistency within the given thread.

There’s no single source of truth for how to approach this. Most agents implement a short-term memory. This means that the agent will append each new chat to the conversation history, and when a new prompt is submitted, the agent will append the previous messages to the new prompt.

This method is very efficient and gives the LLM a strong knowledge of previous states. But it can also introduce problems, because the more the conversation grows, the more the LLM will have to go through all previous messages in order to understand what action to take next.

And this can introduce some context drift, just like humans experience. You can’t watch a two-hour podcast and remember all the spoken words, right? In this scenario, the LLM will focus on the most relevant information, eventually losing some context.

![Illustration showing an LLM agent workflow with memory: the agent processes multiple rounds of prompts and tool interactions, maintains a short-term memory of previous conversations, and uses this context to decide actions, while older context may fade over time causing potential context drift.](https://cdn.hashnode.com/res/hashnode/image/upload/v1765064542431/18b8d0a7-b9f1-4f7d-993d-76b3c4058ccf.png align="center")

You don’t have to implement this from scratch. Many tools and frameworks have been developed to make the implementation as easy as possible. You can build it from scratch if you want, of course, but we won’t be doing that here.

In this article, we’ll build a Starbucks barista that collects order information and calls a `create_order` tool once the order meets the full criteria. This is a tool that we’ll create and expose to the AI.

## Project Setup

Let’s start by initializing our project. We’ll use Nest.js for its efficiency and native TypeScript support. Note that nothing here is tied to Nest.js – this is just a framework preference, and everything we’ll do here can be done with Node.js and Express.js.

Here is a list of all the tools that we’ll use:

1. `langchain/core` - **Always required**
    
    This is the main Langchain engine that defines all core tools and fundamental functions, containing:
    
    * prompt templates
        
    * message types
        
    * runnables
        
    * tool interfaces
        
    * chain composition utilities, and more.
        
    
    Most LangChain project need this.
    
2. `langchain/google-genai` - This package is used to interact with Google’s generative AI models, vector embedding models, and other related tools.
    
3. `langchain/langgraph` - **Important for building an AI agent with total control**
    
    Langgraph is a low-level orchestration framework for building controllable agents. It can be used to build:
    
    * Conversational agents.
        
    * Build complex task automation.
        
    * Agent’s context management.
        
4. `langchain/langgraph-checkpoint-mongodb` - This package provides a MongoDB-based checkpointer for LangGraph, enabling persistence of agent state and short-term memory using MongoDB.
    
5. `@langchain/mongodb` - This package provides MongoDB integrations for LangChain, allowing you to:
    
    * Store and retrieve vector embeddings.
        
    * Persist LangChain documents, agents, or memory states.
        
    * Easily integrate MongoDB as a database backend for your AI workflows.
        
6. `@nestjs/mongoose` - A NestJS wrapper around Mongoose for MongoDB. Provides:
    
    * Dependency injection support for Mongoose models.
        
    * Simplified schema definition and model management.
        
    * Seamless integration of MongoDB into NestJS applications, enabling structured data persistence for AI apps or any backend.
        
7. `langchain` - This is the main npm package that aggregates LangChain functionality. It provides:
    
    * Access to connectors, utilities, and core modules.
        
    * Easy import of different LangChain components in one place.
        
    * Commonly used alongside `@langchain/core` for building applications with minimal setup.
        
8. `mongodb` - The official MongoDB driver for Node.js. It provides:
    
    * Low-level, flexible access to MongoDB databases.
        
    * Support for CRUD operations, transactions, and indexing.
        
    * A required dependency if you plan to connect LangChain components or your backend directly to MongoDB.
        
9. `mongoose` - An ODM (Object Data Modeling) library for MongoDB. Offers:
    
    * Schema-based data modeling for MongoDB documents.
        
    * Middleware, validation, and hooks for MongoDB operations.
        
    * Ideal for structured data management in NestJS or other Node.js applications.
        
10. `zod` - A TypeScript-first schema validation library. Used for:
    
    * Defining strict data schemas and validating inputs/outputs.
        
    * Ensuring type safety at runtime.
        
    * Useful in AI applications to validate responses from models or enforce data consistency.
        

Start by initializing your Nest.js project, and installing all the required dependencies:

```dart
$ npm i -g @nestjs/cli //If you don't have Nest.js installed on your machine
$ nest new project-name

"dependencies" : {
    "@langchain/core": "^0.3.75",
    "@langchain/google-genai": "^0.2.16",
    "@langchain/langgraph": "^0.4.8",
    "@langchain/langgraph-checkpoint-mongodb": "^0.1.1",
    "@langchain/mongodb": "^0.1.0",
    "@nestjs/mongoose": "^11.0.3",
    "langchain": "^0.3.33",
    "mongodb": "^6.19.0",
    "mongoose": "^8.18.1",
    "zod": "^4.1.8"
}

//The versions may not be same at the time you are reading this, so I recommand checking
//The official documentation for each package.
```

Now that we have our project created and all the packages installed, let’s see what we need to do to turn our vision into a project. Think of what you’ll need in order to create a Starbucks barista:

* First, we need to define the structure of our data (creating schemas)
    
* Then we need to create a menu list that our agent will be referring to.
    
* After that, we’ll add LLM interaction
    
* And last but not least, we’ll add the ability to save previous conversations for conversational context.
    

### Folder Structure

You can modify this folder structure and adapt it based on your framework of choice. But the core implementation is the same across all frameworks.

```plaintext
├── .env
├── .eslintrc.js
├── .gitignore
├── .prettierrc
├── nest-cli.json
├── package.json
├── README.md
├── tsconfig.build.json
├── tsconfig.json
├── src/
│   ├── app.controller.ts
│   ├── app.module.ts
│   ├── app.service.ts
│   ├── main.ts
│   ├── chat/
│   │   ├── chat.controller.ts
│   │   ├── chat.module.ts
│   │   ├── chat.service.ts
│   │   └── dtos/
│   │       └── chat.dto.ts
│   ├── data/
│   │   └── schema/
│   │       └── order.schema.ts
│   └── util/
│       ├── constants/
│       │   └── drinks_data.ts
│       ├── schemas/
│       │   ├── drinks/
│       │   │   └── Drink.schema.ts
│       │   └── orders/
│       │       └── Order.schema.ts
│       ├── summeries/
│       │   └── drink.ts
│       └── types/
```

## Data Schematization with Zod

This file contains all our schema definitions regarding drinks and all modifications they can receive. This part is useful for defining the structure of the data that will be used by the AI agent.

### **Importing Zod**

In the `lib/util/schemas/drinks.ts` file, before defining any schemas, import the Zod library, which provides tools for building TypeScript-first schemas.

```typescript
// Imports the 'z' object from the 'zod' library.
// Zod is a TypeScript-first schema declaration and validation library.
// 'z' is the primary object used to define schemas (e.g., z.object, z.string, z.boolean, z.array).
import z from "zod";
```

Zod gives you a simple and expressive way to define and validate the structure of the data our agent will interact with.

### **Drink Schema**

This schema represents the structure of a drink in the Starbucks-style menu. I split and explained each field so the reader clearly understands what each property controls.

```typescript
export const DrinkSchema = z.object({
  name: z.string(),            // Required name of the drink
  description: z.string(),     // Required explanation of what the drink is
  supportMilk: z.boolean(),    // Whether milk options are available
  supportSweeteners: z.boolean(), // Whether sweeteners can be added
  supportSyrup: z.boolean(),   // Whether flavor syrups are allowed
  supportTopping: z.boolean(), // Whether toppings are supported
  supportSize: z.boolean(),    // Whether the drink can be ordered in sizes
  image: z.string().url().optional(), // Optional image URL
});
```

### **What this schema represents**

* It ensures every drink has a proper name and a description.
    
* It defines which customizations apply to the drink.
    
* It prepares the agent to reason about drink options in a structured, validated format.
    

### **Sweetener Schema**

Each sweetener option in the menu is represented with its own schema.

```typescript
export const SweetenerSchema = z.object({
  name: z.string(),                // Sweetener name
  description: z.string(),         // What it is / taste description
  image: z.string().url().optional(), // Optional image URL
});
```

This ensures consistency across all sweetener entries and avoids malformed data.

### **Syrup Schema**

Similar to sweeteners, but for syrup flavors:

```typescript

export const SyrupSchema = z.object({
  name: z.string(),
  description: z.string(),
  image: z.string().url().optional(),
});
```

This can represent flavors like Vanilla, Caramel, or Hazelnut.

### **Topping Schema**

Toppings such as whipped cream or cinnamon are defined here.

```typescript
export const ToppingSchema = z.object({
  name: z.string(),
  description: z.string(),
  image: z.string().url().optional(),
});
```

### **Size Schema**

Drink sizes are modeled as objects as well:

```typescript
export const SizeSchema = z.object({
  name: z.string(),               // e.g. Small, Medium
  description: z.string(),        // A short explanation
  image: z.string().url().optional(),
});
```

### **Milk Schema**

Represents milk types such as Whole, Skim, Almond, or Oat.

```typescript
export const MilkSchema = z.object({
  name: z.string(),
  description: z.string(),
  image: z.string().url().optional(),
});
```

### **Collections of Items**

Now that the individual item schemas exist, we can create **collections** of them. These represent all available toppings, sizes, milk types, syrups, sweeteners, and the entire menu of drinks

```typescript
export const ToppingsSchema = z.array(ToppingSchema);
export const SizesSchema = z.array(SizeSchema);
export const MilksSchema = z.array(MilkSchema);
export const SyrupsSchema = z.array(SyrupSchema);
export const SweetenersSchema = z.array(SweetenerSchema);
export const DrinksSchema = z.array(DrinkSchema);
```

Why arrays? Because in the real world, your agent will receive **lists** from a database or API—not single items.

### **Inferred Types**

Zod also allows TypeScript to infer types from schemas automatically.

This ensures:

* TypeScript types always match the schemas.
    
* You avoid duplicated definitions.
    
* The agent code stays consistent and safe.
    

```typescript
export type Drink = z.infer<typeof DrinkSchema>;
export type SupportSweetener = z.infer<typeof SweetenerSchema>;
export type Syrup = z.infer<typeof SyrupSchema>;
export type Topping = z.infer<typeof ToppingSchema>;
export type Size = z.infer<typeof SizeSchema>;
export type Milk = z.infer<typeof MilkSchema>;

export type Toppings = z.infer<typeof ToppingsSchema>;
export type Sizes = z.infer<typeof SizesSchema>;
export type Milks = z.infer<typeof MilksSchema>;
export type Syrups = z.infer<typeof SyrupsSchema>;
export type Sweeteners = z.infer<typeof SweetenersSchema>;
export type Drinks = z.infer<typeof DrinksSchema>;
```

These provide the rest of your LangChain/LangGraph code with strong typing based on your schema definitions.

This entire file:

* Encodes all drink-related data structures.
    
* Provides validation to ensure clean, predictable data.
    
* Automatically generates TypeScript types.
    
* Helps the AI agent reason reliably about drinks and customization options.
    

You’ll use these schemas later and convert them into string representations for LLM prompts.

*You can find the file containing all the code* [*here*](https://github.com/DjibrilM/langgraph-starbucks-agent/blob/main/src/lib/schemas/drinks.ts)*.*

## How to Parse the Schema

As mentioned earlier, LLMs are **text input–output machines**. They don’t understand TypeScript types or Zod schemas directly. If you include a schema inside a prompt, the model will simply see it as plain text without understanding its structure or constraints.

Because of this, we need a way to convert schemas into a readable string format that can be embedded inside a prompt, such as:

> “The output must be a JSON object with the following fields…”

This is exactly the problem solved by `StructuredOutputParser` from `langchain/output_parsers`. It takes a Zod schema and turns it into:

* A human-readable description that can be sent to an LLM.
    
* A validator that checks whether the model’s output matches the schema.
    

In short, it acts as a bridge between typed application logic and text-based AI output.

### Defining the Order Schema

We’ll start with a simple Zod schema that represents a customer’s drink order. This schema defines the exact shape and constraints of the data we expect the model to produce.

```typescript
export const OrderSchema = z.object({
  drink: z.string(),
  size: z.string(),
  mil: z.string(),
  syrup: z.string(),
  sweeteners: z.string(),
  toppings: z.string(),
  quantity: z.number().min(1).max(10),
});

export type OrderType = z.infer<typeof OrderSchema>;
```

At this point, the schema is useful only inside our TypeScript application. The LLM still has no idea what this structure means.

### Parsing the Schema into Human-Readable Text

This is where schema parsing comes in. Using `StructuredOutputParser.fromZodSchema`, we can transform the Zod schema into:

* Instructions the LLM can understand.
    
* A runtime validator that ensures the response is correct.
    

```typescript
export const OrderParser =
  StructuredOutputParser.fromZodSchema(OrderSchema as any);
```

The parser enables two critical workflows:

#### Generating prompt instructions

The parser can generate a text description of the schema that looks roughly like: “Return a JSON object with the fields `drink`, `size`, `mil`, `syrup`, `sweeteners`, and `toppings` as strings, and `quantity` as a number between 1 and 10.” This string can be injected directly into your prompt so the LLM knows exactly how to format its response.

#### Validating the model’s output

After the LLM responds, its output is still just text. The parser:

* Converts that text into a JavaScript object.
    
* Validates it against the original Zod schema.
    
* Throws an error if anything is missing, malformed, or out of bounds.
    

This prevents invalid AI-generated data (for example, `quantity: 0`) from entering your system.

### Reusing the Same Approach for Other Schemas

Once you understand this pattern, applying it to other schemas is straightforward.

For example, you can do the same thing for a `DrinkSchema`:

```typescript
export const DrinkParser =
  StructuredOutputParser.fromZodSchema(DrinkSchema as any);
```

Now you can confidently say something like: “Hey Gemini, this is what a drink object looks like—please respond using this structure.”

### Why This Matters

Schema parsing allows you to:

* Keep strong typing in your application.
    
* Give clear formatting instructions to the LLM.
    
* Safely convert unstructured AI output into validated, production-ready data.
    

Without this step, working with LLMs at scale becomes unreliable and error-prone.

## Data-to-Text Summarization

In the context of LLM agents, **data-to-text summarization** means converting structured data—such as objects returned from a database or backend API—into **clear, human-readable strings** that can be embedded directly into prompts.

Even the most advanced LLMs operate purely on text. They don’t reason over JavaScript objects, database rows, or JSON structures in the same way humans or programs do. The clearer and more descriptive your text input is, the more accurate and reliable the model’s output will be.

Because of this, a common and recommended pattern when building LLM-powered systems is:

**Fetch structured data → summarize it into natural language → pass the summary into the prompt**

To keep this article focused, we’ll store our data in constants instead of querying a real database. The technique is exactly the same whether the data comes from MongoDB, PostgreSQL, or an API.

### The Core Idea

The goal of data-to-text summarization is simple:

* Take an object with fields and boolean flags
    
* Convert it into a short paragraph that explains what the object represents
    
* Remove ambiguity and guesswork for the LLM
    

Instead of forcing the model to infer meaning from raw data, we *spell it out explicitly*.

### Summarizing a Drink Object

Consider the following drink object:

```typescript
{
  name: 'Espresso',
  description: 'Strong concentrated coffee shot.',
  supportMilk: false,
  supportSweeteners: true,
  supportSyrup: true,
  supportTopping: false,
  supportSize: false,
}
```

While this structure is easy for developers to understand, it’s not ideal for an LLM prompt. Boolean flags like `supportMilk: false` require interpretation, which increases the chance of incorrect assumptions.

Instead, we convert this object into a descriptive paragraph:

“A drink named Espresso. It is described as a strong, concentrated coffee shot. It cannot be made with milk. It can be made with sweeteners. It can be made with syrup. It cannot be made with toppings. It cannot be made in different sizes.”

This transformation is exactly what data-to-text summarization provides.

### A Standard Summarization Pattern

Below is a simplified example of how we convert a `Drink` object into a readable description.

```typescript
export const createDrinkItemSummary = (drink: Drink): string => {
  const name = `A drink named ${drink.name}.`;
  const description = `It is described as ${drink.description}.`;

  const milk = drink.supportMilk
    ? 'It can be made with milk.'
    : 'It cannot be made with milk.';

  const sweeteners = drink.supportSweeteners
    ? 'It can be made with sweeteners.'
    : 'It cannot contain sweeteners.';

  const syrup = drink.supportSyrup
    ? 'It can be made with syrup.'
    : 'It cannot be made with syrup.';

  const toppings = drink.supportTopping
    ? 'It can be made with toppings.'
    : 'It cannot be made with toppings.';

  const size = drink.supportSize
    ? 'It can be made in different sizes.'
    : 'It cannot be made in different sizes.';

  return `${name} ${description} ${milk} ${sweeteners} ${syrup} ${toppings} ${size}`;
};
```

### Why this works well for LLMs

* Boolean logic is converted into **explicit sentences**
    
* Every capability and limitation is clearly stated
    
* The output can be embedded directly into a system or user prompt
    

### Summarizing Collections of Data

This same approach applies to lists of data such as milks, syrups, toppings, or sizes. Instead of passing an array of objects to the model, we convert them into bullet-style text summaries:

```typescript
export const createSweetenersSummary = (): string => {
  return `Available sweeteners are:
${SWEETENERS.map(
  (s) => `- ${s.name}: ${s.description}`
).join('\n')}`;
};
```

This gives the model a **complete, readable overview** of available options without requiring it to interpret raw arrays.

### Applying the Same Idea to Other Domains

This pattern is not limited to drinks or menus. It works for *any* domain. For example, here’s the same summarization technique applied to an object representing a shoe in an online ordering assistant:

```typescript
export const createShoeItemSummary = (shoe: {
  name: string;
  description: string;
  genderCategory: string;
  styleType: string;
  material: string;
  availableInMultipleColors: boolean;
  limitedEdition: boolean;
  supportsCustomization: boolean;
}): string => {
  return `
A shoe named ${shoe.name}.
It is described as ${shoe.description}.
It is categorized as a ${shoe.genderCategory.toLowerCase()} shoe.
It belongs to the ${shoe.styleType.toLowerCase()} fashion style.
It is made of ${shoe.material.toLowerCase()} material.
${shoe.availableInMultipleColors ? 'It is available in multiple colors.' : 'It is available in a single color.'}
${shoe.limitedEdition ? 'It is a limited-edition release.' : 'It is not a limited-edition release.'}
${shoe.supportsCustomization ? 'It supports customization options.' : 'It does not support customization options.'}
`.trim();
};
```

Which produces an output like:

“A shoe named Veloria Canvas Sneaker. It is described as a minimalist everyday sneaker designed for casual wear. It is categorized as a unisex shoe. It belongs to the casual fashion style. It is made of breathable canvas material. It is available in multiple colors. It is not a limited-edition release. It supports light customization options.”

## How to Persist Orders with MongoDB in NestJS

Now that we’ve established the core foundations of our application—schemas, parsers, and data-to-text summaries—it’s time to **persist data**. In a real-world assistant, orders and conversations shouldn’t disappear when the server restarts. They need to be stored reliably so they can be retrieved, analyzed, or continued later.

To achieve this, we’ll use MongoDB as our database and the NestJS Mongoose integration to manage data models and collections.

### Connecting MongoDB to a NestJS Application

In NestJS, the `AppModule` is the root module of the application. This is where global dependencies—such as database connections—are configured.

```typescript
@Module({
  imports: [
    MongooseModule.forRoot(process.env.MONGO_URI),
    ChatsModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

What’s happening here?

* `MongooseModule.forRoot(...)` establishes a global MongoDB connection.
    
* The connection string is read from an environment variable (`MONGO_URI`), which is the recommended practice for security.
    
* Once configured, this connection becomes available throughout the entire application.
    
* `ChatsModule` is imported so it can access the database connection and register its own schemas.
    

This setup ensures that every feature module can safely interact with MongoDB without creating multiple connections.

### Defining an Order Schema with Mongoose

NestJS uses decorators to define MongoDB schemas in a clean, class-based way. Each class represents a MongoDB document, and each property becomes a field in the collection.

```typescript
@Schema()
export class Order {
  @Prop({ required: true })
  drink: string;

  @Prop({ default: null })
  size: string;

  @Prop({ default: null })
  milk: string;

  @Prop({ default: null })
  syrup: string;

  @Prop({ default: null })
  sweeter: string;

  @Prop({ default: null })
  toppings: string;

  @Prop({ default: 1 })
  quantity: number;
}
```

Why this approach?

* Each `@Prop()` decorator maps directly to a MongoDB field.
    
* Default values allow partial orders to be saved incrementally.
    
* Required fields (like `drink`) enforce basic data integrity.
    
* The schema closely mirrors the structured output produced by the LLM.
    

Once the class is defined, it’s converted into a MongoDB schema:

```typescript
export const OrderSchema = SchemaFactory.createForClass(Order);
```

This single line creates:

* A MongoDB collection
    
* A validation layer
    
* A schema that Mongoose can use to create, read, and update orders
    

### How This Fits into the LLM Agent Architecture

At this point, we have:

* **Zod schemas** → for validating AI output
    
* **Summarization functions** → for converting data into readable prompts
    
* **MongoDB schemas** → for persisting finalized orders
    

This separation is intentional:

* Zod handles *AI-facing validation*
    
* Mongoose handles *database persistence*
    
* NestJS acts as the glue that ties everything together
    

### Preparing for the Agent Logic

With the database in place, we’re now ready to implement the agent itself.

The agent’s responsibilities will include:

* Interpreting user messages
    
* Calling tools
    
* Generating structured orders
    
* Validating them
    
* Persisting them to MongoDB
    
* Maintaining conversational state
    

All of this logic will live inside the `src/chats/chats.service.ts` file. The next section introduces the **agent’s core logic**, and we’ll walk through it step by step so every part is easy to follow.

Start by importing the required dependencies:

```tsx

import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { MongoClient } from 'mongodb';
import { Model } from 'mongoose';

import { tool } from '@langchain/core/tools';
import {
  ChatPromptTemplate,
  MessagesPlaceholder,
} from '@langchain/core/prompts';
import { AIMessage, BaseMessage, HumanMessage } from '@langchain/core/messages';

import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
import { StateGraph } from '@langchain/langgraph';
import { ToolNode } from '@langchain/langgraph/prebuilt';
import { Annotation } from '@langchain/langgraph';
import { START, END } from '@langchain/langgraph';

import { MongoDBSaver } from '@langchain/langgraph-checkpoint-mongodb';

import z from 'zod';

import { Order } from './schemas/order.schema';
import { OrderParser, OrderSchema, OrderType } from 'src/lib/schemas/orders';
import { DrinkParser } from 'src/lib/schemas/drinks';
import { DRINKS } from 'src/lib/utils/constants/menu_data';

import {
  createSweetenersSummary,
  availableToppingsSummary,
  createAvailableMilksSummary,
  createSyrupsSummary,
  createSizesSummary,
  createDrinkItemSummary,
} from 'src/lib/summaries';

const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY || '';
const client: MongoClient = new MongoClient(process.env.MONGO_URI || '');
const database_name = 'drinks_db';
```

## LangGraph State/Annotation Terms

In LangGraph, **state** can be thought of as a temporary workspace that exists while the agent is running. It stores all the information that nodes (we’ll cover nodes in detail later) might need to access information like the last message, the history of the conversation, or any intermediate data generated during execution.

This state allows nodes to **read from it, update it, and pass information along** as the agent processes a workflow, making it the agent’s short-term memory for the duration of the run.

```tsx
@Injectable()
export class ChatService {

  chatWithAgent = async ({
    thread_id,
    query,
  }: {
    thread_id: string;
    query: string;
  }) => {

    const graphState = Annotation.Root({
      messages: Annotation<BaseMessage[]>({
        reducer: (x, y) => [...x, ...y],
      }),
    });

  }

}
```

This code defines the **LangGraph state** for the chat agent. The `graphState` object acts as a central memory that every node in the workflow can read from and update.

The `messages` field specifically stores all messages in the conversation, including user messages, AI responses, and tool outputs. The reducer function `[...x, ...y]` appends new messages to the existing array, preserving the conversation history across multiple steps.

LangGraph’s reducer mechanism lets developers control how new state merges with old state. In this chat system, the approach is similar to updating React state with `setMessages(prev => [...prev, ...newMessages])`: it keeps the old messages while adding the new ones.

Together, this state enables the agent, tools, and checkpointing system to maintain a coherent conversation, allowing each node in the LangGraph workflow to access the full context and contribute incrementally.

## How to Create Tools for the Agent

Modern chatbots can do more than just generate text - they can also search the internet, read files, or perform computations. While LLMs are powerful, they cannot execute code or compile programs on their own.

In the code text of LLM agents, a tool is a piece of code written by the agent developer that an LLM can invoke on the host machine. The host machine executes the code, and the LLM only receives the final output of the computation.

Here's how to create a tool that stores orders in the database. Still in the `chatWithAgent` function within the `ChatService` class. Bellow the state store definition:

```tsx
const orderTool = tool(
  async ({ order }: { order: OrderType }) => {
    try {
      await this.orderModel.create(order);
      return 'Order created successfully';
    } catch (error) {
      console.log(error);
      return 'Failed to create the order';
    }
  },
  {
    schema: z.object({
      order: OrderSchema.describe('The order that will be stored in the DB'),
    }),
    name: 'create_order',
    description: 'This tool creates a new order in the database',
  }
);

const tools = [orderTool];
```

## LangGraph Nodes (Workflow Components)

From a definition standpoint, a LangGraph node is a fundamental component of a LangGraph workflow, representing a single unit of computation or an individual step in an AI agent's process.

Each node can perform a specific task, such as generating a message, invoking a tool, or transforming data, and it interacts with the state to read inputs and write outputs. Together, nodes are connected to form the agent’s workflow or execution graph, allowing complex reasoning and multi-step operations.

In our project, we’ll have four nodes.

1. **Agent node:** This node is in charge of interacting with the LLM - it constructs the agent’s main message template and stacks old messages to the new prompt to create context.
    
2. **Tools node:** The tools node introduces external capabilities, which allow the workflow to interact with external APIs
    
3. `START` **node:** This node indicates the entry point of our workflow, or to be precise, which node to call when a user initiates a conversation with the agent. It’s quite simple to define.
    
4. `addConditionalEdges` - `addConditionalEdges('agent', shouldContinue)`: In LangGraph, `.addConditionalEdges('agent', shouldContinue)` lets the workflow branch dynamically after the `'agent'` node runs, based on a condition defined in `shouldContinue`. Unlike a fixed edge, which always goes from one node to the next, a conditional edge evaluates the agent’s output and directs the workflow to different nodes depending on the result, allowing the AI agent to make decisions and adapt its next steps.
    

## Graph Declaration

In LangGraph, a graph is the central structure that models an AI agent’s workflow as interconnected nodes, where each node represents a computation step, tool, or decision. It orchestrates the flow of data and control between nodes, manages conditional branching, and maintains the recursive loop of execution.

Essentially, the graph is the backbone that ensures complex, stateful interactions happen in a coordinated and modular way, connecting nodes like `agent`, `tools`, and conditional edges into a coherent workflow.

With that knowledge in place, we can now create the agent graph with all its nodes.

```tsx
  const callModal = async (states: typeof graphState.State) => {
    const prompt = ChatPromptTemplate.fromMessages([
      {
        role: 'system',
        content: `
            You are a helpful assistant that helps users order drinks from Starbucks.
            Your job is to take the user's request and fill in any missing details based on how a complete order should look.
            A complete order follows this structure: ${OrderParser}.

            **TOOLS**
            You have access to a "create_order" tool.
            Use this tool when the user confirms the final order.
            After calling the tool, you should inform the user whether the order was successfully created or if it failed.

            **DRINK DETAILS**
            Each drink has its own set of properties such as size, milk, syrup, sweetener, and toppings.
            Here is the drink schema: ${DrinkParser}.

            You must ask for any missing details before creating the order.

            If the user requests a modification that is not supported for the selected drink, tell them that it is not possible.

            If the user asks for something unrelated to drink orders, politely tell them that you can only assist with drink orders.

            **AVAILABLE OPTIONS**
            List of available drinks and their allowed modifications:
            ${DRINKS.map((drink) => `- ${createDrinkItemSummary(drink)}`)}

            Sweeteners: ${createSweetenersSummary()}
            Toppings: ${availableToppingsSummary()}
            Milks: ${createAvailableMilksSummary()}
            Syrups: ${createSyrupsSummary()}
            Sizes: ${createSizesSummary()}

            Order schema: ${OrderParser}

            If the user's query is unclear, tell them that the request is not clear.

            **ORDER CONFIRMATION**
            Once the order is ready, you must ask the user to confirm it.
            If they confirm, immediately call the "create_order" tool.
            Only respond after the tool completes, indicating success or failure.

            **FRONTEND RESPONSE FORMAT**
            Every response must include:

            "message": "Your message to the user",
            "current_order": "The order currently being constructed",
            "suggestions": "Options the user can choose from",
            "progress": "Order status ('completed' after creation)"

            **IMPORTANT RULES**
            - Be friendly, use emojis, and add humor.
            - Use null for unfilled fields.
            - Never omit the JSON tracking object.
        `,
      },
      new MessagesPlaceholder('messages'),
    ]);

  const formattedPrompt = await prompt.formatMessages({
    time: new Date().toISOString(),
    messages: states.messages,
  });

  const chat = new ChatGoogleGenerativeAI({
    model: 'gemini-2.0-flash',
    temperature: 0,
    apiKey: GOOGLE_API_KEY,
  }).bindTools(tools);

  const result = await chat.invoke(formattedPrompt);
  return { messages: [result] };
  };     
    const shouldContinue = (state: typeof graphState.State) => {
      const lastMessage = state.messages[
        state.messages.length - 1
      ] as AIMessage;
      return lastMessage.tool_calls?.length ? 'tools' : END;
    };

    const toolsNode = new ToolNode<typeof graphState.State>(tools);

    /**
     * Build the conversation graph.
     */
    const graph = new StateGraph(graphState)
      .addNode('agent', callModal)
      .addNode('tools', toolsNode)
      .addEdge(START, 'agent')
      .addConditionalEdges('agent', shouldContinue)
      .addEdge('tools', 'agent');
```

### Explanation

* **Graph State (**`graphState`)  
    The `graphState` object is the shared memory across all nodes. It stores `messages`, which track the conversation history including user inputs, AI responses, and tool interactions. The reducer `[...x, ...y]` appends new messages, preserving past context. This is similar to React state updates: old messages remain while new ones are added.
    
* **Agent Node (**`callModal`)  
    This node handles the **LLM call**. It formats a prompt containing system instructions, drink schemas, available tools, and frontend response rules. By including `states.messages`, the AI sees the full conversation history, enabling multi-turn dialogue.
    
* **LLM Execution**  
    `ChatGoogleGenerativeAI` generates the AI response. `.bindTools(tools)` allows the AI to call tools like `create_order` directly if needed.
    
* **Conditional Flow (**`shouldContinue`)  
    After the AI responds, the `shouldContinue` function checks if the message includes tool calls. If so, execution moves to the `tools` node; otherwise, the workflow ends. This allows dynamic branching depending on the AI’s output.
    
* **Tool Node (**`ToolNode`)  
    The `tools` node executes the requested tool, such as saving the order to the database. Once completed, control returns to the agent node, enabling the AI to respond to the user with results.
    
* **Graph Construction (**`StateGraph`)  
    Nodes are connected in a coherent workflow:
    
    * `START → agent` begins the conversation
        
    * Conditional edges handle tool execution
        
    * `tools → agent` ensures the agent can respond after tools run
        
* **Overall Flow**  
    Together, the graph and shared state ensure a **stateful, multi-turn conversation**. The AI can ask for missing details, call tools when needed, and maintain context across interactions. Every node reads and writes to the same state.
    

## **Workflow Compilation and State Persistence (Final Part)**

So far, all of our states are temporary, meaning they only exist for the duration of a user’s request. However, we want our agent to **remember and recall conversation context** even when a new request is sent with the same `thread_id` or conversation ID.

To achieve this, we’ll use MongoDB in combination with the `langchain/langgraph-checkpoint-mongo` library. This library simplifies state persistence by associating each conversation with a unique, manually assigned ID. All operations—from retrieving previous messages to saving new ones—are handled internally, you only need to provide the conversation ID you want to work with.

```tsx
const graph = new StateGraph(graphState)
  .addNode('agent', callModal)
  .addNode('tools', toolsNode)
  .addEdge(START, 'agent')
  .addConditionalEdges('agent', shouldContinue)
  .addEdge('tools', 'agent');

  const checkpointer = new MongoDBSaver({ client, dbName: database_name });

  const app = graph.compile({ checkpointer });

  /**
     * Run the graph using the user's message.
     */
    const finalState = await app.invoke(
      { messages: [new HumanMessage(query)] },
      { recursionLimit: 15, configurable: { thread_id } },
    );

  /**
   * Extract JSON payload from AI response.
   */
  function extractJsonResponse(response: any) {
    const match = response.match(/```json\\s*([\\s\\S]*?)\\s*```/i);
    if (match && match[1] && typeof response === 'string') {
      return JSON.parse(match[1].trim());
    }
    throw response;
  }

  const lastMessage = finalState.messages.at(-1) as AIMessage; // Extract the last message of the conversation
  return extractJsonResponse(lastMessage.content); //Response
```

The above code demonstrates how to initialize a checkpoint, compile a graph, and invoke the agent with an incoming prompt.

The `extractJsonResponse` method is used to grab the formatted response that we instructed the LLM to generate whenever it’s sending back something to the user.

Based on this given instruction from the main template, every response must include: "message": "Your message to the user", "current\_order": "The order currently being constructed", "suggestions": "Options the user can choose from", "progress": "Order status ('completed' after creation)"

Every response from the LLM should look like this:

```tsx
'```json\\n' +
  '{\\n' +
  '"message": "Got it! To make sure I get your order just right, can you clarify which coffee drink you\\'d like? We have Latte, Cappuccino, Cold Brew, and Frappuccino. 😊",\\n' +
  '"current_order": {\\n' +
  '"drink": null,\\n' +
  '"size": null,\\n' +
  '"mil": null,\\n' +
  '"syrup": null,\\n' +
  '"sweeteners": null,\\n' +
  '"toppings": null,\\n' +
  '"quantity": null\\n' +
  '},\\n' +
  '"suggestions": [\\n' +
  '"Latte",\\n' +
  '"Cappuccino",\\n' +
  '"Cold Brew",\\n' +
  '"Frappuccino"\\n' +
  '],\\n' +
  '"progress": "incomplete"\\n' +
  '}\\n' +
  '```';
```

This structure allows the frontend to easily render the LLM response and track the state of the current order. This is more of a design choice and less of a convention.

## **Conclusion**

Building an autonomous AI agent with LangChain and LangGraph allows you to combine the reasoning power of LLMs with practical tool execution and persistent memory. By defining schemas, parsing data into human-readable formats, and orchestrating workflows through nodes, you can create intelligent agents capable of handling real-world tasks—like our Starbucks barista.

With MongoDB integration for state persistence, your agent can maintain context across conversations, making interactions feel more natural and human-like. This approach opens the door to building more sophisticated, domain-specific AI assistants without starting from scratch.

In short: **define your data, teach your agent how to reason, and let LangGraph orchestrate the magic.** ☕🤖

Source code here: [https://github.com/DjibrilM/langgraph-starbucks-agent](https://github.com/DjibrilM/langgraph-starbucks-agent)

### **Resources**

* LangGraph documentation: [https://docs.langchain.com/oss/javascript/langgraph/quickstart](https://docs.langchain.com/oss/javascript/langgraph/quickstart)
    
* Synergizing Reasoning and Acting in Language Models: [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)
