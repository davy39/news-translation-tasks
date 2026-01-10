---
title: 'How to Use the ChatGPT Apps SDK: Build a Pizza App with Apps SDK'
subtitle: ''
author: Shola Jegede
co_authors: []
series: null
date: '2025-10-15T18:32:52.088Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-chatgpt-apps-sdk
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760552846436/808fcd59-4dbc-4874-bd62-2e13965f956c.png
tags:
- name: AI
  slug: ai
- name: openai
  slug: openai
- name: chatgpt
  slug: chatgpt
seo_title: null
seo_desc: 'OpenAI recently introduced ChatGPT Apps, powered by the new Apps SDK and
  the Model Context Protocol (MCP).

  Think of these apps as plugins for ChatGPT:


  You can invoke them naturally in a conversation.


  They can render custom interactive UIs inside Ch...'
---

OpenAI recently introduced ChatGPT Apps, powered by the new [Apps SDK](https://developers.openai.com/apps-sdk) and the Model Context Protocol (MCP).

Think of these apps as plugins for ChatGPT:

* You can invoke them naturally in a conversation.
    
* They can render custom interactive UIs inside ChatGPT (maps, carousels, videos, and more).
    
* They run on an MCP server that you control, which defines the tools, resources, and widgets the app provides.
    

In this step-by-step guide, you’ll build a ChatGPT App using the official [Pizza App example](https://github.com/openai/openai-apps-sdk-examples/tree/main/pizzaz_server_node). This app shows how ChatGPT can render UI widgets like a pizza map or carousel, powered by your local server.

## What You’ll Learn

By following this tutorial, you’ll learn how to:

* Set up and run a ChatGPT App with the OpenAI Apps SDK.
    
* Understand the core building blocks: tools, resources, and widgets.
    
* Connect your local app server to ChatGPT using Developer Mode.
    
* Render custom UI directly inside a ChatGPT conversation.
    

## Table of Contents

* [What You’ll Learn](#heading-what-youll-learn)
    
* [Table of Contents](#heading-table-of-contents)
    
* [How ChatGPT Apps Work (Big Picture)](#heading-how-chatgpt-apps-work-big-picture)
    
* [Step 1. Clone the Examples Repo](#heading-step-1-clone-the-examples-repo)
    
* [Step 2. Run the Pizza App Server](#heading-step-2-run-the-pizza-app-server)
    
* [Step 3. Expose Your Local Server](#heading-step-3-expose-your-local-server)
    
    * [3.1 Get ngrok](#heading-31-get-ngrok)
        
    * [3.2 Install ngrok](#heading-32-install-ngrok)
        
    * [3.3 Connect Your Account](#heading-33-connect-your-account)
        
    * [3.4 Start a Tunnel](#heading-34-start-a-tunnel)
        
* [Step 4. Walk Through the Pizza App Code](#heading-step-4-walk-through-the-pizza-app-code)
    
    * [4.1 Imports and Setup](#heading-41-imports-and-setup)
        
    * [4.2 Defining Pizza Widgets](#heading-42-defining-pizza-widgets)
        
    * [4.3 Mapping Widgets to Tools and Resources](#heading-43-mapping-widgets-to-tools-and-resources)
        
    * [4.4 Handling Requests](#heading-44-handling-requests)
        
    * [4.5 Creating the Server](#heading-45-creating-the-server)
        
* [Step 5. Enable Developer Mode in ChatGPT](#heading-step-5-enable-developer-mode-in-chatgpt)
    
    * [5.1 Enable Developer Mode](#heading-51-enable-developer-mode)
        
    * [5.2 Create App](#heading-52-create-app)
        
    * [5.3 Use Your App](#heading-53-use-your-app)
        
* [Challenges (Try These Yourself)](#heading-challenges-try-these-yourself)
    
    * [Challenge A: Add a “Pizza Specials” widget (text-only)](#heading-challenge-a-add-a-pizza-specials-widget-text-only)
        
    * [Challenge B: Support Multiple Toppings](#heading-challenge-b-support-multiple-toppings)
        
    * [Challenge C: Fetch Real Pizza Data from an External API](#heading-challenge-c-fetch-real-pizza-data-from-an-external-api)
        
* [Conclusion](#heading-conclusion)
    

## How ChatGPT Apps Work (Big Picture)

Here’s the architecture in simple terms:

```markdown
ChatGPT (frontend)
   |
   v
MCP Server (your backend)
   |
   v
Widgets (HTML/JS markup displayed inside ChatGPT)
```

* **ChatGPT** sends requests like: *“Show me a pizza carousel.”*
    
* **MCP Server** responds with resources (HTML markup) and tool logic.
    
* **Widgets** are rendered inline in ChatGPT.
    

## Step 1. Clone the Examples Repo

OpenAI provides an official examples repo that includes the Pizza App. Clone it and install the dependencies using these commands:

```powershell
git clone https://github.com/openai/openai-apps-sdk-examples.git
cd openai-apps-sdk-examples
pnpm install
```

After installing, build the components and start the dev server:

```powershell
pnpm run build  
pnpm run dev
```

## Step 2. Run the Pizza App Server

Navigate to the Pizza App server and start it:

```powershell
cd pizzaz_server_node
pnpm start
```

If it works, you should see:

```powershell
Pizzaz MCP server listening on http://localhost:8000
  SSE stream: GET http://localhost:8000/mcp
  Message post endpoint: POST http://localhost:8000/mcp/messages
```

This means your server is running locally.

## Step 3. Expose Your Local Server

To let ChatGPT communicate with your app, your local server needs a public URL. ngrok provides a quick way to expose it during development.

### 3.1 Get ngrok

Sign up at [ngrok.com](https://ngrok.com) and copy your **authtoken**.

### 3.2 Install ngrok

**macOS:**

```powershell
brew install ngrok
```

**Windows:**

* Download and unzip ngrok.
    
* Optionally, add the folder to your PATH.
    

### 3.3 Connect Your Account

```powershell
ngrok config add-authtoken <your_authtoken>
```

### 3.4 Start a Tunnel

```powershell
ngrok http 8000
```

This gives you a public HTTPS URL (like [`https://xyz.ngrok.app/mcp`](https://xyz.ngrok.app/mcp)).

## Step 4. Walk Through the Pizza App Code

The full Pizza App server code is long, so let’s break it down into digestible parts.

### 4.1 Imports and Setup

```typescript
import { createServer } from "node:http";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";
import { z } from "zod";
```

* `Server` and `SSEServerTransport` come from the Apps SDK.
    
* `zod` validates input to ensure ChatGPT sends the right arguments.
    

### 4.2 Defining Pizza Widgets

Widgets are the heart of the app. Each one represents a piece of UI ChatGPT can display.

Here’s the Pizza Map widget:

```typescript
{
  id: "pizza-map",
  title: "Show Pizza Map",
  templateUri: "ui://widget/pizza-map.html",
  html: `
    <div id="pizzaz-root"></div>
    <link rel="stylesheet" href=".../pizzaz-0038.css">
    <script type="module" src=".../pizzaz-0038.js"></script>
  `,
  responseText: "Rendered a pizza map!"
}
```

* `id` → unique name of the widget.
    
* `templateUri` → how ChatGPT fetches the UI.
    
* `html` → actual markup and assets.
    
* `responseText` → message that shows in chat.
    

The app defines five widgets:

* Pizza Map
    
* Pizza Carousel
    
* Pizza Album
    
* Pizza List
    
* Pizza Video
    

### 4.3 Mapping Widgets to Tools and Resources

Next, widgets are converted into **tools** (things ChatGPT can call) and **resources** (UI markup ChatGPT can render).

```typescript
const tools = widgets.map((widget) => ({
  name: widget.id,
  description: widget.title,
  inputSchema: toolInputSchema,
  title: widget.title,
  _meta: widgetMeta(widget)
}));

const resources = widgets.map((widget) => ({
  uri: widget.templateUri,
  name: widget.title,
  description: `${widget.title} widget markup`,
  mimeType: "text/html+skybridge",
  _meta: widgetMeta(widget)
}));
```

This makes each widget callable and displayable.

### 4.4 Handling Requests

The MCP server responds to ChatGPT’s requests. For example, when ChatGPT calls a widget tool:

```typescript
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const widget = widgetsById.get(request.params.name);
  const args = toolInputParser.parse(request.params.arguments ?? {});
  return {
    content: [{ type: "text", text: widget.responseText }],
    structuredContent: { pizzaTopping: args.pizzaTopping },
    _meta: widgetMeta(widget)
  };
});
```

This:

* Finds the widget requested.
    
* Validates the input (`pizzaTopping`).
    
* Responds with text + metadata so ChatGPT can render the widget.
    

### 4.5 Creating the Server

Finally, the server is bound to HTTP endpoints (`/mcp` and `/mcp/messages`) so ChatGPT can stream messages to and from it.

```typescript
const httpServer = createServer(async (req, res) => {
  // handle requests to /mcp and /mcp/messages
});

httpServer.listen(8000, () => {
  console.log("Pizzaz MCP server running on port 8000");
});
```

## Step 5. Enable Developer Mode in ChatGPT

### 5.1 Enable Developer Mode

* Open ChatGPT
    
* Go to **Settings → Apps & Connectors → Advanced Settings**
    
* Toggle **Developer Mode**
    

![Toggle developer mode](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313826734/7cf96d44-ae03-48d1-92b9-7fee42d895ad.png align="center")

When **Developer Mode** is enabled, ChatGPT should look like this:

![Developer mode enabled](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313206155/f2677b50-8bc0-4c10-b971-b0a60d66181f.png align="center")

### 5.2 Create App

* Go back to **Settings → Apps & Connectors**
    
* Click **Create**
    
* Next:
    
    * **Name**: Enter a name for your app (for example, *Pizza App*)
        
    * **Description**: Enter any description for your app (or leave empty)
        
    * **MCP Server URL**: Paste the public HTTPS URL of your MCP endpoint. Make sure it points directly to `/mcp`, not just the server root
        
    * **Authentication**: Choose **No authentication**
        
    * Check **I trust this application**
        
    * Click **Create** to finish
        

![Create your app in ChatGPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313317398/93d30263-59db-4606-8066-467b7949efb9.png align="center")

Once your app is connected to ChatGPT, it should look like this:

![App is connected to ChatGPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313733914/944b363a-7004-4737-a102-bd1e328f717d.png align="center")

When you click on the **Back** icon, you should see your app and other apps that you can connect to and use with ChatGPT:

![View all apps that can be connected to ChatGPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313649918/627594a8-a89b-4cd5-90a6-1fa2d804063e.png align="center")

### 5.3 Use Your App

To use your app,

* Open a new chat in ChatGPT
    
* Click on the **+** icon
    
* Scroll down to **more**
    
* You would see your app
    
* Choose **Pizza App** to start using your app
    

![How to use your app in ChatGPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313495700/e978f689-622b-4ceb-aa73-6459302e8b3b.png align="center")

Here are some commands you can try out with your pizza app in ChatGPT:

* *Show me a pizza map with pepperoni topping*
    
* *Show me a pizza carousel with mushroom topping*
    
* *Show me a pizza album with veggie topping*
    
* *Show me a pizza list with cheese topping*
    
* *Show me a pizza video with chicken topping*
    

Each command tells ChatGPT which widget to render, and you can swap in any topping you like.

![Type in a command into ChatGPT to make tool calls to your app](https://cdn.hashnode.com/res/hashnode/image/upload/v1760313589161/07b69ab7-fd36-4a14-84de-883a0f634b82.png align="center")

Below are samples:

* Pepperoni topping map:
    

![Sample app response: Pepperoni topping map](https://cdn.hashnode.com/res/hashnode/image/upload/v1760314642952/6527fe96-061b-433c-94b9-86b8152fd082.png align="center")

* Extra cheese carousel:
    

![Sample app response: Extra cheese carousel](https://cdn.hashnode.com/res/hashnode/image/upload/v1760314675799/8b65e9b3-4547-40a2-9269-cec56aa8705f.png align="center")

* Mushroom topping album:
    

![Sample app response: Mushroom topping album](https://cdn.hashnode.com/res/hashnode/image/upload/v1760314714658/ae6edf57-44c9-421b-a140-364cc8873db4.png align="center")

## Challenges (Try These Yourself)

Here are three practical ways to extend your Pizza App. Each one ties directly to the code you already have.

### Challenge A: Add a “Pizza Specials” widget (text-only)

**Goal:** Create a widget that just shows a short message like *“Today’s special: Margherita with basil.”*

**Where to change:**

* `resources.widgets` → duplicate an entry and give it a new `id`/`title`.
    
* `tools` → register it as a new tool.
    
* `CallTool` handler → detect when it’s called (`if (request.params.name === "pizza-special")`) and return your special.
    

**Hint:**  
This widget doesn’t need extra CSS/JS files. Just keep its `html` to something like `<div>🍕 Today’s special: Margherita</div>`. The idea is to show that widgets can be as simple as plain HTML.

### Challenge B: Support Multiple Toppings

**Goal:** Let users order a pizza with more than one topping, like `["pepperoni", "mushroom"]`.

**Where to change:**

* `toolInputSchema` → switch from `z.string()` to `z.array(z.string())`.
    
* `CallTool` handler → after parsing, `args.pizzaTopping` will be an array. Join it into a string before inserting into HTML/response.
    
* Widget HTML → update the display so it lists all chosen toppings.
    

**Hint:**  
Console.log the parsed `args` first to confirm you’re actually getting an array. Then try something like:

```typescript
const toppings = args.pizzaTopping.join(", ");
return { responseText: `Pizza ordered with ${toppings}` };
```

### Challenge C: Fetch Real Pizza Data from an External API

**Goal:** Instead of hard-coding content, fetch real pizza info. For example, you could call Yelp’s API to list pizza places in a location, or use a free placeholder API to simulate data.

**Where to change:**

* Inside the `CallTool` handler for your widget.
    
* Replace the static HTML with a `fetch(...)` call that builds dynamic HTML from the response.
    

**Hint:**  
Start small with a free API like [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts). For example:

```typescript
const res = await fetch("https://jsonplaceholder.typicode.com/posts?_limit=3");
const data = await res.json();

const html = `
  <ul>
    ${data.map((p: any) => `<li>${p.title}</li>`).join("")}
  </ul>
`;

return { responseText: "Fetched pizza places!", content: [{ type: "text/html", text: html }] };
```

Once that works, swap in a real API such as Yelp or Google Maps Places to render actual pizza places.

## Conclusion

You just built your first ChatGPT App using the **OpenAI Apps SDK**. With a bit of JavaScript and HTML, you created a server that ChatGPT can talk to, and rendered interactive widgets right inside the chat window.

This example focused on the pizza app sample provided by OpenAI, but you could build:

* A weather dashboard,
    
* A movie finder,
    
* A financial data viewer,
    
* Or even a mini-game.
    

The SDK makes it possible to blend **conversation + interactive UI** in powerful new ways.

Explore the [OpenAI Apps SDK documentation](https://developers.openai.com/apps-sdk) to go deeper and start building your own apps.
