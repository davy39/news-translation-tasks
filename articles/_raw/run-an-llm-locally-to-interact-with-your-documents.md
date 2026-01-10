---
title: How to Run an LLM Locally to Interact with Your Documents
subtitle: ''
author: Zoe Isabel Senón
date: '2026-01-10T00:38:09.929Z'
originalURL: https://acceleratingutopia.com/how-to-local-llm-private-docs/
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767976983680/2e3671cd-4280-4a32-9508-47fe9c06ab22.png
tags:
- name: 'LLM''s '
  slug: llms
- name: ollama
  slug: ollama
- name: AI
  slug: ai
seo_title: null
seo_desc: Learn how to run a LLM like ChatGPT locally to interact with your personal
  or business documents privately.
---

Most AI tools require you to send your prompts and files to third-party servers. That’s a non-starter if your data includes private journals, research notes, or sensitive business documents (contracts, board decks, HR files, financials). The good news: you can run capable LLMs locally (on a laptop or your own server) and query your documents without sending a single byte to the cloud.

In this tutorial, you’ll learn how to run an LLM locally and privately, so you can search and chat with sensitive journals and business docs on your own machine. We’ll install **Ollama** and **OpenWebUI**, pick a model that fits your hardware, enable private document search with **nomic-embed-text**, and create a local knowledge base so everything stays on-disk.

## Table of Contents

* [Prerequisites](#heading-prerequisites)
    
* [Installation](#heading-installation)
    
* [Settings for Documents](#heading-settings-for-documents)
    
* [How to Upload Your Documents](#heading-how-to-upload-your-documents)
    
    * [(Optional) Adding a system prompt](#heading-optional-adding-a-system-prompt)
        
* [How to Run Your LLM Locally](#heading-how-to-run-your-llm-locally)
    
* [Conclusion](#heading-conclusion)
    

## Prerequisites

You’ll need a terminal (all systems—Windows, Mac, Linux—include one, and you can find yours with a quick search), and either Python and pip or Docker, depending on your preferred installation method for OpenWebUI.

## Installation

You’ll need [**Ollama**](https://ollama.com/download) and [**OpenWebUI**](https://docs.openwebui.com/getting-started/quick-start/). Ollama runs the models, while OpenWebUI gives you a browser interface to interact with your local LLM, like you would with ChatGPT.

### Step 1: Install Ollama

Download and install Ollama from its [official site](https://ollama.com/download). Installers are available for **macOS**, **Linux**, and **Windows**. Once installed, verify it’s running by opening a terminal and executing:

```bash
ollama list
```

If Ollama is running, this will return a list of active models (or an empty list).

### Step 2: Install OpenWebUI

You can install OpenWebUI either with Python (pip) or with Docker. Here, we will show how to do it with pip, but you can find instructions for Docker on the [official openwebui docs](https://docs.openwebui.com/getting-started/quick-start/).

Install OpenWebUI with the following command:

```bash
pip install open-webui
```

This works on **macOS, Linux, and Windows**, as long as you have Python ≥ 3.9 installed.

Next, start the server:

```bash
open-webui serve
```

Then open your browser and go to:

```bash
http://localhost:8080
```

### Step 3: Install a Model

Choose a model from the [Ollama model list](https://ollama.com/library) and pull it locally by copying the command provided.

![Screenshot of the model download page with an arrow pointing to the upper-right corner box that includes the installation command with a shortcut to copy-paste](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302463715/fbbaabf7-6612-460c-8e09-1c5143eacc1a.png align="center")

For example:

```bash
ollama pull gemma3:4b
```

If you’re unsure which model your machine can handle, ask an AI to recommend one based on your hardware. Smaller models (1B–4B) are safer on laptops.

I would recommend Gemma3 as a starter (you can download multiple models and easily switch between them). Pick the **parameter number** at the end (“:4b”, “:1b”, and so on) based on this guide:

* Tier 1 (small laptops or weak computers): RAM ≤8 GB or no GPU → 1B–2B.
    
* Tier 2: RAM 16 GB, weak GPU → 2B–4B.
    
* Tier 3: RAM ≥16 GB, 6–8 GB VRAM → 4B–9B.
    
* Tier 4: RAM ≥32 GB, 12 GB+ VRAM → 12B+.
    

Once you have installed Ollama and your desired model, confirm that they are active by running `ollama list` in the terminal:

![Image showing the output of running the "ollama list" command (shows the list of downloaded models, in this case "gemma3:1b")](https://cdn.hashnode.com/res/hashnode/image/upload/v1767465401368/d1b8abc0-7aaa-4c2f-ad4c-30ae908f9e8b.png align="left")

Run WebOpenUI to launch the browser interface with:

```bash
open-webui serve
```

Then head over to [http://localhost:8080/](http://localhost:8080/). Now you are ready to start using your LLM locally!

**Note**: it will ask you for login credentials, but these don’t really matter if you only intend to use it locally.

![Screenshot of the frontend of a running instance of OpenWebUI, showing the homepage, which includes a text input box in the center with the placeholder "how can I help you today?", and a side panel with the list of previous chats, and links to "search", "notes", "workspace", and "new chat", as well as a setting button. At the top there is a model selector that currently has "gemma3:1b" selected as the model to use.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302486263/14d93c7e-415c-463f-82da-fc515f28663a.png align="center")

## Settings for Documents

Now we are going to set up everything we need to interact with our local documents. First of all, we need to install the “[**nomic-embed-text**](https://ollama.com/library/nomic-embed-text)” model to process our documents. Install it with:

```bash
ollama pull nomic-embed-text
```

**Note**: If you are wondering why we need another model (nomic-embed-text) besides our main one:

* The embedding model (`nomic-embed-text`) maps each text chunk from your documents to a numerical vector so OpenWebUI can quickly find semantically similar chunks when you ask a question.​
    
* The chat model (for example `gemma3:1b`) receives your question plus those retrieved chunks as context and generates the natural-language response.
    

Next, you should enable the “**memory**” feature if you want the LLM to remember the context of your past conversations in your future ones.

Download the adaptive memory function [**here**](https://openwebui.com/f/alexgrama7/adaptive_memory_v2). Functions are like plug-ins.

![Screenshot showing the page (website) for the "adaptive memory v3" function. It shows a big "get" button, that when clicked opens a pop-up view named "Open WebUI URL" with the current placeholder being "http:localhost:8080" (the default WebUI port) and a button to "import to WebUI" and another one below to "Download as JSON export" in case the first one doesn't work)](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302505221/b247316c-0863-410a-84c9-abc084a6631f.png align="center")

Now we will update our settings to enable these features. Click on your name in the bottom-left corner, then “Settings”.

![Screenshot showing the menu panel that pops up when clicking on the bottom-left round icon with the user's initital and name, showing a list of options, starting with "Settings" and followed by "Archived Chats", "Playground", "Admin Panel" and "Sign out"](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302517617/e73983f3-0e36-4c0a-a61c-96a0a42f1fab.png align="left")

Click on the first one, then go to “Personalization” and enable “Memory”.

![“Screenshot of the OpenWebUI settings panel with the Personalization tab open and the Memory toggle switched on for saving past conversation context.”](https://cdn.hashnode.com/res/hashnode/image/upload/v1752935284007/aa42c76b-f38c-4485-b442-8844c6c3a544.png align="center")

Now we are going to access the other settings panel (“Admin Panel”). Click again on your name in the bottom-left corner and go to **Admin panel → Settings → Documents**.

![Screenshot of the OpenWebUI Admin → Settings → Documents page, showing a text input field called "Chunk size" currently set to 512](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302570583/96784c55-484b-4c66-bdc4-ce23a7e901a1.png align="center")

In this section (Admin Panel → Settings → Documents), find the “**Embedding**” section, go to “**Embedding Model Engine**” and choose Ollama (find the selectable to the right). Leave the API Key blank.

Now, under “**Embedding Model**” write `nomic-embed-text`. Then go to “Retrieval” → enable “Full Context Mode”.

### Chunking settings

You should also set the **chunk size** and **overlap**. OpenWebUI splits documents into smaller chunks before indexing them, since models can’t embed or retrieve very long texts in one piece.

A good default is **128–512 tokens per chunk**, with **10–20% overlap**. Larger chunks preserve more context but are slower and more memory-intensive, while smaller chunks are faster but can lose higher-level meaning. Overlap helps prevent important context from being cut off when text is split.

Here’s a guiding table, but I recommend obtaining the recommended values for your specific use case and setup by sharing them (including GPU or laptop model, storage, RAM, and so on) with an LLM like ChatGPT or Claude, **as changing the chunking/overlap values later on requires reuploading the documents.**

### Suggested chunk/overlap by tier

| **Tier / scenario** | **Typical hardware** | **Chunk size (tokens)** | **Overlap (%)** | **Notes** |
| --- | --- | --- | --- | --- |
| Tier 1 – constrained | ≤8 GB RAM, no/weak GPU | 128–256 | 10–15 | Prioritizes speed and low memory use. ​ |
| Tier 2 – mid | 16 GB RAM, modest GPU or strong CPU | 256–384 | 15–20 | Balanced context vs. performance. ​ |
| Tier 3 – comfortable | ≥16 GB RAM, 6–8 GB VRAM | 384–512 | 15–20 | More semantics per chunk, still practical. ​ |
| Dense technical PDFs / legal docs | Any, but especially Tier 2–3 | 384–512 | 15–20 | Keeps paragraphs and arguments intact. ​ |
| Short notes, tickets, emails | Any | 128–256 | 10–15 | Items are small, large chunks not needed. ​ |
| Very long queries, need many retrieved chunks | Any with larger context window | 256–384 | 10–15 | Smaller chunks fit more pieces into context. ​ |

## How to Upload Your Documents

Now, the final step: uploading your documents! Go to “Workspace” in the side panel, then “Knowledge”, and create a new collection (database). You can start uploading files here.

![Screenshot of the "Workspace" page (after clicking on "workspace" in the side panel) highlight the "Workspace" button on the lefthand side, the "Knowledge" tab being selected from the options at the top within this Workspace page, then "Upload files" which is the first option shown on the list after clicking the "+" (plus) sign button at the right of the text input with the placeholder that says "Search Collection".](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302584485/63c04901-f5d3-4ac7-bab5-b23362fb83cb.png align="center")

<div data-node-type="callout">
<div data-node-type="callout-emoji">⚠</div>
<div data-node-type="callout-text">Make sure to check for any errors during the upload. Unfortunately, they only show as temporary pop-ups. Some errors might be due to the format of your files, so make sure to check the console for further error logs.</div>
</div>

Then, within “Workspace”, switch to the “Models” tab and create a new custom model. Creating a custom model and attaching your knowledge base tells OpenWebUI to automatically search your document collection and include the most relevant chunks as context whenever you ask a question.

![Screenshot of the "Workspace" page (after clicking on "workspace" in the side panel), highlighting the first tab/option in the upper menu named "Models", which when clicked shows the list of custom models and an option to create new ones (in this case the user has created one called "Gemma-custom-knowledge")](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302593445/b5316a4a-8c8a-4348-a31e-1c10fe0e1abb.png align="center")

Here, make sure to select your model (in my case “gemma3:1b”) and attach your knowledge base.

![Screenshot of the model creation page, highlighting the selectable options under the "Base model (from)" field, specifically highlighting "gemma3:1b" or the model of choice, under the selected-by-default option "select a base model". The second element highlighted in red is the other field below titled "Knowledge", with a buttom called "Select Knowledge". There are 2 other elements highlighted in yellow (indicating lower priority): the first one is "Model Params" that includes a "system prompt" input field right below, and the other one is "Filters" which includes multiple selectable options depending on the different plugins or "functions" installed.](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302604758/df0c7948-bb9b-4615-8f09-21faaa64fdde.png align="center")

![Screenshot showing the options available after clicking "Select Knowledge" under "Knowledge", highlighting the option that says "COLLECTION" in green followed by the title "Test-knowledge-base" (example title chosen by the author) and the description added by the author ("adding my documents")](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302612285/8247d1c3-5f84-42de-9861-34416d0b7f10.png align="center")

### (Optional) Adding a system prompt

When creating your custom model in **Workspace → Models**, you can define a **system prompt** that the model will use for context throughout all your conversations.

Here are some examples of information you might want to add:

* context about yourself *(“I am a 20-year-old student in bioengineering interested in…”)*
    
* your preferred communication style *(“no fluff", “be direct”, “be analytical”…)*
    
* context about how your data is structured
    

**Example system prompt:**

> You are a thoughtful, analytical assistant helping me explore patterns and insights in my personal journals. Be direct, avoid speculation, and clearly distinguish between facts from the documents and interpretation.

This prompt will automatically apply to every chat using this custom model, helping keep responses consistent and aligned with your goals.

## How to Run Your LLM Locally

Now open a new chat and make sure to select your custom model:

![Screenshot showing the "New chat" page after clicking on the "+" (plus) symbol/button next to the custom model name. It shows the options shown when clicking on the input field that says "Search a model" as a placeholder, and the option highlighted within it is the name of the custom model (in this case the author chose the name "Gemma-custom-knowledge")](https://cdn.hashnode.com/res/hashnode/image/upload/v1758302621012/241f461c-acf6-41ae-b68d-ad187790aef4.png align="center")

Now you are ready to chat with your own docs in a private local environment!

<div data-node-type="callout">
<div data-node-type="callout-emoji">⚠</div>
<div data-node-type="callout-text"><strong>Note</strong>: By default, the frontend/browser will stop streaming the response after five minutes, even though it will keep processing your query in the background. This means that if your query takes more than five minutes to process, it will not be displayed on the browser. You can reload the page and click “continue response” to get the latest output.</div>
</div>

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">I recommend installing the <a target="_self" rel="noopener noreferrer nofollow" href="https://openwebui.com/f/alexgrama7/enhanced_context_tracker_v4" style="pointer-events: none">Enhanced Context Tracker</a> function (plugin) to get more visibility into the progress of your query.</div>
</div>

## Conclusion

You now have a private LLM stack (**Ollama** for models, **OpenWebUI** for the UI, and **nomic-embed-text** for embeddings) wired to your on-disk knowledge base. Your journals and business docs stay local; nothing is sent to third parties. The main dials are simple: pick a model that fits your hardware, enable memory and full-context retrieval, use sensible chunk/overlap, and check the console when runs stall.

If you need more headroom, deploy the same setup on your own server and keep the privacy guarantees. From here, iterate on model choice, chunking, and prompts, and add the optional functions if you need deeper visibility during long jobs.
