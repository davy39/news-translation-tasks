---
title: Build a Support Agent with Vercel AI SDK
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2025-12-23T16:34:48.007Z'
originalURL: https://freecodecamp.org/news/build-a-support-agent-with-vercel-ai-sdk
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1766507669760/bf3fe42c-d729-4b59-9eca-2677e1b49e2a.jpeg
tags:
- name: Vercel
  slug: vercel
- name: JavaScript
  slug: javascript
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Vercel AI SDK is a TypeScript-first toolkit for building AI features. It
  streamlines text generation, embeddings, and structured outputs.

  We just posted a course on the freeCodeCamp.org YouTube channel that will teach
  you to use the Vercel AI SDK to ...'
---

Vercel AI SDK is a TypeScript-first toolkit for building AI features. It streamlines text generation, embeddings, and structured outputs.

We just posted a course on the freeCodeCamp.org YouTube channel that will teach you to use the Vercel AI SDK to create and ship a customer support agent that makes autonomous decisions to either answer questions based on your support docs or search the web in real time.

In this course, you’ll ship a customer support agent that:

* Embeds support docs into a Supabase vector store.
    
* Uses retrieval and web search as tools, selected on-the-fly based on the user’s question.
    
* Classifies intents with structured outputs (via generateObject + Zod).
    
* Answers questions with grounded, trustworthy responses—pulling from your docs when relevant or searching the web in real time when needed
    

The course covers these topics.

* Explain RAG & embeddings and decide when to use each of them.
    
* Set up Supabase as a vector store: create tables, embed documents, and handle chunking/text splitting for large files.
    
* Implement retrieval with Supabase RPC so your agent can fetch the right context for any question.
    
* Use Vercel AI SDK basics: embeddings and generateText for fast, reliable model calls.
    
* Produce structured outputs with generateObject and Zod to validate and route intents.
    
* Call tools with the AI SDK—define schemas, wire execution, and keep everything type-safe.
    
* Treat retrieval and web search as tools, and compose them into a single agent decision flow.
    
* Use the OpenAI web search tool to pull fresh, real-time information when your docs aren’t enough.
    
* Combine it all into a support agent that chooses the best strategy (retrieve, search, or answer directly) and explains its answers.
    

Watch the full course [on the freeCodeCamp.org YouTube channel](https://youtu.be/WKIjkxxNH0c) (2-hour watch).

%[https://youtu.be/WKIjkxxNH0c]
