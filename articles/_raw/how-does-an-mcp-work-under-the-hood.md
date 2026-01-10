---
title: How Does an MCP Work Under the Hood? MCP Workflow Explained
subtitle: ''
author: Ajay Patel
co_authors: []
series: null
date: '2025-12-16T18:35:11.600Z'
originalURL: https://freecodecamp.org/news/how-does-an-mcp-work-under-the-hood
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765909617721/fa533504-3dab-48c3-9b92-0b89a81af025.png
tags:
- name: mcp
  slug: mcp
- name: Model Context Protocol
  slug: model-context-protocol
- name: AI
  slug: ai
seo_title: Understanding MCP in Artificial Intelligence
seo_desc: Understand how MCP enables AI to interact with external systems, enhancing
  capabilities beyond initial training limits.
---

We’ve all faced that awkward limitation with AI: it can write code or explain complex topics in seconds, but the moment you ask it to check a local file or run a quick database query, it hits a wall. It’s like having a genius assistant who is locked in an empty room—smart, but completely cut off from your actual work. This is where the Model Context Protocol (MCP) changes the game. In this article, we’ll explore MCP in depth.

## Table of Contents

* [MCP Server: A-Z of Model Context Protocol](#heading-mcp-server-a-z-of-model-context-protocol)
    
* [What is MCP (Model Context Protocol)?](#heading-what-is-mcp-model-context-protocol)
    
* [Architecture of MCP](#heading-architecture-of-mcp)
    
* [How Does MCP Work?](#heading-how-does-mcp-work)
    
* [MCP vs RAG](#heading-mcp-vs-rag)
    
* [MCP vs A2A](#heading-mcp-vs-a2a)
    
* [Resources](#heading-resources)
    
* [Conclusion](#heading-conclusion)
    

## MCP Server: A-Z of Model Context Protocol

LLMs possess impressive knowledge and reasoning skills, which allow them to perform many complex tasks. But the problem is that their knowledge is limited to their initial training data. It means they can’t access your calendar, run SQL queries, or send an email.

It was clear that, to give the LLMs real-world knowledge, we have to provide some integrations that enable them to access real-time knowledge or perform some actions in the real world. This leads to the classic MxN problems, where developers have to build and maintain custom integrations for every combination of M models and N tools.

The image below properly demonstrates the MxN Problem:

![mxn problem - connecting every model to every tool individually](https://cdn.hashnode.com/res/hashnode/image/upload/v1764841852514/f4279e47-416d-4559-8908-16199eab3820.jpeg align="center")

Function calling (also known as tool calling) provides a powerful and flexible way for OpenAI models to interface with external systems and access data outside their training data. However, this feature is currently exclusive to OpenAI models, creating vendor lock-in.

That’s where MCP steps in. MCP is a write once, use anywhere approach to the problem. An app developer can write a single MCP server for any AI system to use and expose a set of tools and data. Similarly, an AI system can implement the protocol and connect to any MCP server that exists today or in the future.

## What is MCP (Model Context Protocol)?

MCP is an open-source standard, developed by Anthropic, for connecting AI applications to external systems.

By using an MCP, AI applications like Claude or ChatGPT can connect to data sources like local files and databases, tools like search engines and calculators, and workflows like specialized prompts—enabling them to access key information and perform tasks.

Think of an MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, an MCP provides a standardized way to connect AI applications to external systems.

The image below will help you to better understand the MCP Server:

![structure of model context protocol](https://cdn.hashnode.com/res/hashnode/image/upload/v1764763126029/45a8d0a7-a4f4-47e4-afb9-268930bd1c47.png align="center")

## Architecture of MCP

The Model Context Protocol has a clear structure with components that work together to help LLMs and outside systems interact easily. An MCP follows a simple client-server architecture, which can be broken down into three simple key components:

### **MCP Host**

The host is the user-facing AI application, the environment where the AI model lives and interacts with the user. Hosts manage the discovery, permissions, and communication between clients and servers. This ca be a chat application like OpenAI’s ChatGPT interface or Anthropic’s Claude desktop app, or an AI-enhanced IDE like Cursor & Windsurf.

### **MCP Client**

The MCP client is a component within the host that handles the low-level communication with the MCP server. MCP clients are instantiated by host applications to communicate with particular MCP servers. Each client handles one direct communication with one server.

Here, the difference is important: the host is the application users interact with, while clients are the components that enable server connections.

### **MCP Server**

The MCP server is the external program or service that exposes the capabilities (tools, data, and so on) to the application. An MCP server can be seen as a wrapper around some functionality, which exposes a set of tools or resources in a standardized way so that any MCP client can invoke them.

Servers can run locally on the same machine as the host, or remotely on some cloud service, since an MCP is designed to support both scenarios seamlessly

The image below will help you to better understand the concept:

![how does mcp work](https://cdn.hashnode.com/res/hashnode/image/upload/v1764841995822/fdec43d4-705e-4385-8eac-b436ec22c386.jpeg align="center")

An MCP server can expose one or more capabilities to the client. Capabilities are essentially the features or functions that the server makes available.

The MCP server provides the following capabilities:

* **Tools:** Tools are the functions that do something on behalf of the AI model. An AI can use this tool whenever required. Tools are triggered by the AI model’s choice, which means the LLM (via the host) decides to call a tool when it determines it needs to perform a specific task. For example: send\_email -&gt; send the email to the user
    
* **Resources:** Resources provide read-only data to the AI model. A resource can be a database record or a knowledge base that the AI can query to get information, but can’t modify.
    
* **Prompts:** Prompts are the predefined templates or workflows that the server can provide.
    

### **Transport Layer**

The transport layer uses JSON-RPC 2.0 messages to communicate between the client and server. For this, we have mainly two transport methods:

* **Standard Input/Output (stdio):** Ideal for local environments, providing fast and synchronous message transmission.
    
* **Server-Sent Events (SSE):** Best suited for remote resources, enabling efficient, real-time, one-way data streaming from the server to the client.
    

## How Does MCP Work?

An MCP gives an AI assistant the ability to securely use external tools, databases, and services. Imagine you ask Claude:

> “Find the latest sales report in our database and email it to my manager.”

### **Step #1 - Tool Discovery**

When we launch any MCP client (Claude Desktop), it connects to your configured MCP servers and asks: “What can I do with available tools?”

Each server responds with its available tools:

`database_query` ,`email_sender` ,`file_browser`

Now, Claude knows about the tools it has.

### **Step #2 - Understanding Your Requirement**

Claude reads your query and realizes:

* It needs to retrieve information it doesn’t have (in this case, it has to find the sales data `database_query`)
    
* It needs to take an external action (send email `email_sender` )
    

So Claude plans a 2-step tool sequence.

### **Step #3 - Ask for Permission**

Before any external action happens, Claude Desktop prompts you: “Claude wants to query your sales database. Allow?”

Nothing proceeds without your approval. This is core to the MCP’s security model.

### **Step #4 - Querying the Database**

Once you grant the permission, Claude sends a structured MCP tool call to the `database_query` server.

Next, the server will run a secure database lookup and return the latest sales report data. This doesn’t give Claude direct access to the database.

### **Step #5 - Sending the Email**

Once Claude has the data, Claude triggers a second permission prompt: “Claude wants to send an email on your behalf. Approve?”

Once approved, MCP sends the information to the `email_sender` server, and Claude will format the email & deliver it to your manager

### **Step #6 - Natural Answer**

Claude wraps everything up nicely and sends a response to you, “Done! I found the latest sales report and emailed it to your manager.”

The entire process typically happens in seconds. From your perspective, Claude simply "knows" how to access your database and send emails, but in reality, the MCP has orchestrated a secure, standardized exchange between multiple systems.

The beauty of MCP is that it transforms AI assistants from isolated conversational tools into genuine productivity partners that can interact with your entire digital ecosystem, safely and with your explicit permission every step of the way.

## MCP vs RAG

Fundamentally, MCP and RAG are built for serving different purposes.

RAG is a technique that is used to supply the relevant knowledge that we have stored in a vector database. In RAG, the user’s query is converted to a vector embedding, which searches through embeddings in the vector database and finds the relevant context based on similarity. This relevant context is then provided to the LLM. It is great for answering questions from large documents like company wikis, knowledge bases, or research papers.

An MCP enables AI models to perform real-world actions with the help of tools. It lets the AI connect to tools and services like databases, APIs, Gmail, calendar, and so on.

## MCP vs A2A

The Model Context Protocol (MCP) and the Agent-to-Agent (A2A) protocol are complementary open standards in AI architecture that serve different purposes in how AI agents connect with external systems.

* MCP standardizes how a single AI agent connects to tools, data, and external systems (agent-to-tool communication).
    
* A2A standardizes how multiple, independent AI agents communicate and collaborate with each other (agent-to-agent communication).
    

## Resources

For more information on the MCP, you can refer to the official website: [modelcontextprotocol.io](http://modelcontextprotocol.io).

**Some of the awesome MCP Servers which you can check:**

* [Brave Search MCP Server](https://github.com/brave/brave-search-mcp-server)
    
    * An MCP server implementation that integrates the Brave Search API, providing both web and local search capabilities.
        
* [Sentry MCP server](https://github.com/getsentry/sentry-mcp)
    
    * This server provides tools to inspect error reports, stacktraces, and other debugging information from your Sentry account.
        
* [Google Maps MCP Server](https://developers.google.com/maps/ai/mcp)
    
    * MCP Server for the Google Maps API.
        
* [Tailwind MCP Server](https://flyonui.com/mcp) by FlyonUI
    
    * MCP Server for FlyoUI - Generate Amazing UIs/Themes/Sections with just a single prompt.
        
* [git MCP server](https://github.com/idosal/git-mcp)
    
    * A Model Context Protocol server for Git repository interaction and automation. This server provides tools to read, search, and manipulate Git repositories via Large Language Models.
        
* [GitHub MCP Server](https://github.com/github/github-mcp-server)
    
    * MCP Server for the GitHub API, enabling file operations, repository management, search functionality, and more.
        
* [Shadcn MCP Server](https://shadcnstudio.com/mcp)
    
    * MCP Server for shadcn/studio - Generate Amazing UIs/Themes/Sections with just a single prompt.
        

You can explore a list of available MCP servers here: [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

If you're interested in learning how to build your own MCP server, check out this detailed course on Hugging Face: [https://huggingface.co/mcp-course](https://huggingface.co/mcp-course**).

## Conclusion

MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems. With MCP, AI models are not just chatbots, they are fully capable agents that can work with your local files, query your database, send emails with your permission and control.

It has also solved the classic MxN problem—developers only need to build the MCP server once, then all other AI systems can integrate the MCP server in their application.

MCP is the revolution in how AI systems can interact with the real world. As the ecosystem of the MCP continues to grow, it will enable AI agents to become more powerful assistants that can operate across diverse environments with reliability and security.
