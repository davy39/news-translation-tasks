---
title: How to Create Serverless AI Agents with Langbase Docs MCP Server in Minutes
subtitle: ''
author: Maham Codes
co_authors: []
series: null
date: '2025-05-06T15:38:08.144Z'
originalURL: https://freecodecamp.org/news/how-to-create-serverless-ai-agents-with-langbase-docs-mcp-server-in-minutes
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746545857204/6df2b802-a7dc-4745-ac64-117c1c0f7ee1.png
tags:
- name: mcp
  slug: mcp
- name: AI
  slug: ai
- name: ai agents
  slug: ai-agents
- name: 'LLM''s '
  slug: llms
seo_title: null
seo_desc: Building serverless AI agents has recently become a lot simpler. With the
  Langbase Docs MCP server, you can instantly connect AI models to Langbase documentation
  – making it easy to build composable, agentic AI systems with memory without complex
  inf...
---

Building serverless AI agents has recently become a lot simpler. With the Langbase Docs MCP server, you can instantly connect AI models to Langbase documentation – making it easy to build composable, agentic AI systems with memory without complex infrastructure.

In this guide, you’ll learn how to set up the Langbase Docs MCP server inside Cursor (an AI code editor), and build a summary AI agent that uses Langbase docs as live, on-demand context.

### Here’s what we’ll cover:

* [Prerequisites](#heading-prerequisites)
    
* [What is Model Context Protocol (MCP)?](#heading-what-is-model-context-protocol-mcp)
    
* [Anthropic’s role in launching MCP](#heading-anthropics-role-in-launching-mcp)
    
* [Cursor AI code editor](#heading-cursor-ai-code-editor)
    
* [What is Langbase and why is its Docs MCP server useful?](#heading-what-is-langbase-and-why-is-its-docs-mcp-server-useful)
    
* [How to set up the Langbase Docs MCP server in Cursor](#heading-how-to-set-up-the-langbase-docs-mcp-server-in-cursor)?
    
* [How to use Langbase Docs MCP server in Cursor AI](#heading-how-to-use-langbase-docs-mcp-server-in-cursor-ai)?
    
* [Use case: Build a summary AI Agent with Langbase Docs MCP server](#heading-use-case-build-a-summary-ai-agent-with-langbase-docs-mcp-server)
    

## Prerequisites

Before we begin creating the agent, you’ll need to have some things setup and some tools ready to go.

In this tutorial, I’ll be using the following tech stack:

* [Langbase](http://langbase.com) – the platform to build and deploy your serverless AI agents.
    
* [Langbase SDK](https://langbase.com/docs/sdk) – a TypeScript AI SDK, designed to work with JavaScript, TypeScript, Node.js, Next.js, React, and the like.
    
* [Cursor](http://cursor.com) – An AI code editor just like VS Code.
    

You’ll also need to:

* [Sign up](https://langbase.com/signup) on Langbase to get access to the API key.
    

## **What is Model Context Protocol (MCP)?**

[**Model Context Protocol (MCP)**](https://modelcontextprotocol.io/introduction) is an open protocol that standardizes how applications provide external context to large language models (LLMs). With MCP, developers can connect AI models to various tools and data sources like documentation, APIs, and databases – in a clean, consistent way.

Instead of relying solely on prompts, MCP allows LLMs to call custom tools (like documentation fetchers or API explorers) during a conversation.

### MCP General Architecture

At its core, MCP follows a client-server architecture where a host application can connect to multiple servers.

Here’s the general architecture of what it looks like:

[![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdjfGegMH-jHoYjgT3dRPhigOoIz8em0NyexLrfqwNEwdX7rvnbnCxfJG7nKqLk5fYcFu0_D5D8-DMb3vg0nLF4r-N8LlfH6IyFz18HjGZYlZ2J2_cq-jKq3Y6X_LPVxIz3rPs7?key=aHnkCxEY2NrPpuL4oNSIQJNY align="left")](https://modelcontextprotocol.io/introduction)

The Model Context Protocol architecture lets AI clients (like Claude, IDEs, and developer tools) securely connect to multiple local or remote data sources in real time. MCP clients communicate with one or more MCP servers, which act as bridges to structured data – whether from local files, databases, or remote APIs.

This setup allows AI models to retrieve fresh, relevant context from different sources seamlessly, without embedding data directly into the model.

## **Anthropic’s Role in Launching MCP**

[Anthropic](https://www.anthropic.com/news/model-context-protocol) introduced MCP as part of their vision to make LLMs tool-augmented by default. MCP was originally built to expand Claude’s capabilities, but it's now available more broadly and supported in developer-friendly environments like Cursor and Claude Desktop.

By standardizing how tools integrate into LLM workflows, MCP makes it easier for developers to extend AI systems without custom plugins or API hacks.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746454175998/50ed79a0-3728-4cca-92a1-0f48ded38049.png align="center")

## **Cursor AI Code Editor**

[**Cursor**](https://www.cursor.com/) is a developer-first AI code editor that integrates LLMs (like Claude, GPT, and more) directly into your IDE. Cursor supports MCP, meaning you can quickly attach custom tool servers and make them accessible as AI-augmented tools while you code.

Think of Cursor as VS Code meets AI agents – with built-in support for smart tools like docs fetchers and code examples retrievers.

## **What is Langbase and Why is its Docs MCP Server Useful?**

**Langbase** is a powerful serverless AI platform for building AI agents with memory. It helps developers build AI-powered apps and assistants by connecting LLMs directly to their data, APIs, and documentation.

The [Langbase Docs MCP Server](https://langbase.com/docs/guides/docs-mcp-server) provides access to the Langbase documentation and API reference. This server allows you to use the Langbase documentation as context for your LLMs.

By connecting this server to Cursor (or any MCP-supported IDE), you can make Langbase documentation available to your AI agents on demand. This means less context-switching, faster workflows, and smarter assistance when building serverless agentic applications.

## **How to Set Up the Langbase Docs MCP Server in Cursor**

Let’s walk through setting up the server step-by-step.

### **1\. Open Cursor Settings**

Launch Cursor and open Settings. From the left sidebar, select MCP.

### **2\. Add a New MCP Server**

Click the yellow + Add new global MCP server button.

![Add new global MCP server](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdpv9IyBcpFfY9iUo9xk_hfhwhXmyx7JG_4hCPy8WhYC2dMyxHyCniTB147YnQrjGjjqOyvRQsFpHq5-rPVOz637fAwhlfil9ZFhcoicgy3ggriV4_D9mAcdMMTXXCC3gfQiZE?key=aHnkCxEY2NrPpuL4oNSIQJNY align="left")

### **3\. Configure the Langbase Docs MCP Server**

Paste the following configuration into the `mcp.json` file:

```json
{
    "mcpServers": {
        "Langbase": {
        "command": "npx",
        "args": ["@langbase/cli","docs-mcp-server"]
        }
    }
}
```

### **4\. Start the Langbase Docs MCP Server**

In your terminal, run:

```bash
pnpm add @langbase/cli
```

And then run this command:

```bash
pnpm dlx @langbase/cli docs-mcp-server
```

### **5\. Enable the MCP Server in Cursor**

In the MCP settings, make sure the Langbase server is toggled to Enabled.

![Langbase server toggled to "Enabled" in Cursor](https://lh7-rt.googleusercontent.com/docsz/AD_4nXebJ0x4bjv6jDtvfrHnzHo76upu7JyUxasbsrWu0SVxg-ZyA6qir3_8tnCqAK1d1FixOkOcl0oLJN2FopMJGGNAyHLQfmJvkd4ittBaQyOIz26JHgW36PXdduyRt2qD82qrToJC?key=aHnkCxEY2NrPpuL4oNSIQJNY align="left")

## **How to Use Langbase Docs MCP Server in Cursor AI**

Once everything’s all set up, Cursor’s AI agent can now call Langbase docs tools like:

* `docs_route_finder`
    
* `sdk_documentation_fetcher`
    
* `examples_tool`
    
* `guide_tool`
    
* `api_reference_tool`
    

For example, you can ask the Cursor agent:

```bash
“Show me the API reference for Langbase Memory”
 or
 “Find a code example of creating an AI agent pipe in Langbase”
```

The AI will use the Docs MCP server to fetch precise documentation snippets – directly inside Cursor.

## **Use Case: Build a Summary AI Agent with Langbase Docs MCP Server**

Let’s build a summary agent that summarizes context using the Langbase SDK, powered by the Langbase Docs MCP server inside the Cursor AI code editor.

1. Open an empty folder in Cursor and launch the chat panel (`Cmd+Shift+I` on Mac or `Ctrl+Shift+I` on Windows).
    
2. Switch to Agent mode from the mode selector and pick your preferred LLM (we’ll use Claude 3.5 Sonnet for this demo).
    
3. In the chat input, enter the following prompt:  
    “*In this directory, using Langbase SDK, create the summary pipe agent. Use TypeScript and pnpm to run the agent in the terminal.“*
    
4. Cursor will automatically invoke MCP calls, generate the required files and code using Langbase Docs as context, and suggest changes. Accept the changes, and your summary agent will be ready. You can run the agent using the commands provided by Cursor and view the results.
    

Here’s a demo video of creating this summary agent with a single prompt and Langbase Docs MCP server:

%[https://youtu.be/Pw6Su5hpWwU] 

By combining Langbase’s Docs MCP server with Cursor AI, you’ve learned how to build serverless AI agents in minutes – all without leaving your IDE.

If you’re building AI agents, tools, or apps with Langbase, this is one of the fastest ways to simplify your development process.

Happy building! 🚀

Connect with me by 🙌:

* Subscribing to my [YouTube](https://www.youtube.com/@AIwithMahamCodes) Channel. If you are willing to learn about AI and agents.
    
* Subscribing to my free newsletter [“The Agentic Engineer”](https://mahamcodes.substack.com/) where I share all the latest AI and agents news/trends/jobs and much more.
    
* Follow me on [X (Twitter)](https://x.com/MahamDev).
