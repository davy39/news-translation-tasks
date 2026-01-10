---
title: Comment créer un widget de chatbot IA intégrable avec Cloudflare Workers
subtitle: ''
author: Mayur Vekariya
co_authors: []
series: null
date: '2026-01-05T15:51:52.002Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-embeddable-ai-chatbot-widget-with-cloudflare-workers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767626158079/0b9e58c9-9299-4342-8c97-1a2de185cc60.png
tags:
- name: cloudflare
  slug: cloudflare
- name: cloudflare-worker
  slug: cloudflare-worker
- name: AI
  slug: ai
- name: JavaScript
  slug: javascript
- name: AI Chat Bot
  slug: ai-chat-bot
seo_title: Comment créer un widget de chatbot IA intégrable avec Cloudflare Workers
seo_desc: Have you ever wanted to add an AI-powered chatbot to your website, like
  Intercom or Drift, without paying high monthly fees? In this tutorial, you'll learn
  how to build a fully functional, embeddable AI chatbot widget using Cloudflare's
  serverless st...
---

Avez-vous déjà voulu ajouter un chatbot alimenté par IA à votre site web, comme Intercom ou Drift, sans payer de frais mensuels élevés ? Dans ce tutoriel, vous apprendrez à créer un widget de chatbot IA entièrement fonctionnel et intégrable en utilisant la pile serverless de Cloudflare.

Vous allez créer un widget de chatbot IA prêt pour la production que vous pourrez intégrer sur n'importe quel site web avec une seule balise de script. Il sera similaire à Intercom ou Drift — mais il est complètement gratuit et sous votre contrôle.

À la fin, vous aurez un chatbot qui :

* Diffuse les réponses de l'IA en temps réel pour un effet de frappe naturel

* Répond aux questions de votre FAQ en utilisant le RAG (Retrieval Augmented Generation)

* Se souvient des conversations après le rechargement des pages

* Prend en charge les modes sombre et clair

* Fonctionne sur n'importe quel site web avec une seule ligne de code

## **Table des matières**

* [Prérequis](#heading-prerequis)
    
* [Ce que vous allez créer](#heading-ce-que-vous-allez-creer)
    
* [Comment configurer le projet](#heading-comment-configurer-le-projet)
    
* [Comment configurer Wrangler](#heading-comment-configurer-wrangler)
    
    * [Créer des ressources (configuration unique)](#heading-creer-des-ressources-configuration-unique)
        
    * [Créer un index vectorize (pour RAG) :](#heading-creer-un-index-vectorize-pour-rag)
        
    * [Créer un espace de noms KV (pour l'historique des sessions) :](#heading-creer-un-espace-de-noms-kv-pour-lhistorique-des-sessions)
        
* [Comment créer le Worker backend](#heading-comment-creer-le-worker-backend)
    
* [Comment configurer Tailwind CSS](#heading-comment-configurer-tailwind-css)
    
* [Comment créer le widget frontend](#heading-comment-creer-le-widget-frontend)
    
* [Créer la page de démonstration](#heading-creer-la-page-de-demonstration)
    
* [Comment l'exécuter sur votre système local](#heading-comment-lexecuter-sur-votre-systeme-local)
    
* [Comment déployer sur Cloudflare](#heading-comment-deployer-sur-cloudflare)
    
    * [Comment alimenter la base de données FAQ](#heading-comment-alimenter-la-base-de-donnees-faq)
        
* [Comment intégrer le widget sur n'importe quel site web](#heading-comment-integrer-le-widget-sur-nimporte-quel-site-web)
    
    * [Options de configuration](#heading-options-de-configuration)
        
* [Comment personnaliser votre chatbot](#heading-comment-personnaliser-votre-chatbot)
    
    * [Comment ajouter vos propres FAQ](#heading-comment-ajouter-vos-propres-faq)
        
    * [Comment changer la personnalité de l'IA](#heading-comment-changer-la-personnalite-de-lia)
        
    * [Comment styliser le widget](#heading-comment-styliser-le-widget)
    
* [Conclusion](#heading-conclusion)

## **Prérequis**

Avant de commencer, assurez-vous d'avoir :

* Un [compte Cloudflare](https://dash.cloudflare.com/sign-up) (le niveau gratuit fonctionne parfaitement)

* [Node.js](https://nodejs.org/) version 18 ou supérieure installé sur votre ordinateur

* Des connaissances de base en JavaScript

Vous n'avez pas besoin d'expérience préalable avec Cloudflare Workers.

## **Ce que vous allez créer**

Votre chatbot aura deux parties principales :

1. **Backend Worker** (**src/index.js**) : Gère les requêtes de chat, gère les sessions et se connecte à l'IA

2. **Widget Frontend** (**public/widget.js**) : L'interface utilisateur intégrable avec laquelle les utilisateurs interagissent

Vous utiliserez quatre services Cloudflare :

* **Workers AI** : Alimente les réponses de l'IA en utilisant le modèle Llama 3 de Meta

* **Vectorize** : Stocke et recherche dans votre FAQ pour un contexte pertinent (c'est la partie RAG)

* **KV** : Persiste l'historique des conversations entre les sessions

* **Workers** : Exécute votre backend serverless à la périphérie

## **Comment configurer le projet**

Tout d'abord, créez un nouveau projet Cloudflare Workers. Ouvrez votre terminal et exécutez la commande suivante.

Lorsque l'on vous demande le langage de programmation, sélectionnez `javascript`, et lorsque l'on vous demande, "Voulez-vous déployer votre application ?" sélectionnez `no`, puisque nous allons déployer à la fin.

```powershell
npm create cloudflare@latest ai-chatbot-widget -- --type=hello-world
```

Accédez à votre nouveau répertoire de projet :

```powershell
cd ai-chatbot-widget
```

Et installez les dépendances de développement requises :

```powershell
npm install --save-dev tailwindcss autoprefixer postcss wrangler
```

Votre projet est maintenant prêt pour le développement.

## **Comment configurer Wrangler**

Wrangler est l'outil en ligne de commande de Cloudflare pour développer et déployer des Workers. Vous devez le configurer pour utiliser les services requis.

Un [Cloudflare Worker](https://workers.cloudflare.com) est une fonction serverless qui s'exécute sur le réseau mondial de périphérie de Cloudflare. Contrairement aux serveurs traditionnels qui s'exécutent dans un seul endroit, les Workers s'exécutent aussi près que possible de vos utilisateurs en utilisant plus de 300 centres de données dans le monde. Cela se traduit par des temps de réponse plus rapides et une latence plus faible. Vous écrivez simplement le code JavaScript, et Cloudflare s'occupe de toute l'infrastructure, de la mise à l'échelle et du déploiement.

### Créer des ressources (configuration unique)

Les ressources suivantes sont créées via l'interface de ligne de commande Wrangler (recommandé pour l'automatisation).

Tout d'abord, installez Wrangler (si vous ne l'avez pas déjà) :

```bash
npm install -g wrangler
```

Pour vous connecter, utilisez `wrangler login`. Cette commande ouvrira un onglet de navigateur Cloudflare où vous devrez autoriser.

### Créer un index vectorize (pour RAG) :

Un [**index vectorize**](https://developers.cloudflare.com/vectorize/) est une base de données vectorielle qui vous permet d'effectuer des recherches sémantiques. Au lieu de rechercher des correspondances exactes de mots-clés (comme dans les bases de données traditionnelles), Vectorize trouve du contenu en fonction de la signification.

Voici comment cela fonctionne : Vous convertissez vos questions et réponses de FAQ en vecteurs numériques (appelés embeddings) en utilisant un modèle d'IA. Lorsque l'utilisateur pose une question, le chatbot convertit cette question en un vecteur et trouve les entrées de FAQ avec les vecteurs les plus similaires. C'est la technique "RAG" ([Retrieval Augmented Generation](https://www.freecodecamp.org/news/retrieval-augmented-generation-rag-handbook/)), qui augmente la réponse de l'IA avec un contexte pertinent de votre base de connaissances.

```bash
npx wrangler vectorize create faq-vectors --dimensions=768 --metric=cosine
```

### Créer un espace de noms KV (pour l'historique des sessions) :

[**KV (Key-Value) storage**](https://developers.cloudflare.com/kv/) est la base de données distribuée mondialement de Cloudflare pour stocker des données simples. Pensez-y comme un dictionnaire géant : vous stockez des données en utilisant une clé (l'ID de session) et les récupérez plus tard en utilisant cette même clé.

Pour votre chatbot, KV stocke l'historique des conversations de chaque utilisateur. Lorsque l'utilisateur revient sur votre site web, le chatbot récupère sa session à partir de KV et se souvient de ce dont ils ont parlé auparavant.

```javascript
npx wrangler kv namespace create CHAT_SESSIONS
```

Notez l'ID de la sortie car vous l'ajouterez dans le fichier `wrangler.jsonc`.

Créez un fichier appelé `wrangler.jsonc` à la racine de votre projet (vous devez simplement remplacer `YOUR_KV_NAMESPACE_ID` par l'ID que vous avez reçu à l'étape précédente) :

```json
{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "ai-chatbot-widget",
  "main": "src/index.js",
  "compatibility_date": "2025-12-23",
  "observability": {
    "enabled": true
  },
  "assets": {
    "directory": "./public",
    "binding": "ASSETS"
  },
  "ai": {
    "binding": "AI"
  },
  "vectorize": [
    {
      "binding": "VECTORIZE",
      "index_name": "faq-vectors"
    }
  ],
  "kv_namespaces": [
    {
      "binding": "CHAT_SESSIONS",
      "id": "YOUR_KV_NAMESPACE_ID"
    }
  ]
}
```

Ce fichier de configuration indique à Wrangler quels services Cloudflare votre Worker doit utiliser.

Permettez-moi d'expliquer les liaisons clés :

* **ASSETS** : Sert les fichiers statiques (comme votre JavaScript et CSS de widget) à partir du dossier `public`

* **AI** : Se connecte à l'IA de Cloudflare Workers pour exécuter des modèles de machine learning

* **VECTORIZE** : Se connecte à votre index Vectorize pour stocker et rechercher des embeddings de FAQ

* **CHAT_SESSIONS** : Se connecte à un espace de noms KV pour stocker l'historique des conversations

## Comment créer le Worker backend

Le Worker backend est le cerveau de votre chatbot. Il gère les messages de chat entrants, recherche dans votre FAQ un contexte pertinent, envoie la conversation à l'IA, diffuse la réponse à l'utilisateur et sauvegarde tout dans KV pour plus tard.

Créez le fichier `src/index.js` avec ce code :

```javascript
/** AI Chatbot Widget - Cloudflare Worker */
const SYS = `You are a helpful customer support assistant. Be friendly, professional, and concise. Use the FAQ context to give accurate answers. If you don't know something, say so.`;
const TTL = 30*24*60*60;
const cors = { 'Access-Control-Allow-Origin': '*' };
const json = (d, s=200, h={}) => new Response(JSON.stringify(d), { status: s, headers: { 'Content-Type': 'application/json', ...cors, ...h } });
const cookie = r => r.headers.get('Cookie')?.match(/chatbot_session=([^;]+)/)?.[1];

async function faq(env, q) {
  try {
    const e = await env.AI.run('@cf/baai/bge-base-en-v1.5', { text: [q] });
    if (!e.data) return '';
    const r = await env.VECTORIZE.query(e.data[0], { topK: 3, returnMetadata: 'all' });
    return r.matches.map(m => `Q: ${m.metadata?.question}\nA: ${m.metadata?.answer}`).join('\n\n');
  } catch { return ''; }
}

async function chat(req, env) {
  if (req.method !== 'POST') return new Response('Method not allowed', { status: 405 });
  const { message } = await req.json();
  if (!message?.trim()) return json({ error: 'Message required' }, 400);
  let sid = cookie(req), isNew = !sid;
  let sess = sid ? await env.CHAT_SESSIONS.get(sid, 'json') : null;
  if (!sess) { sid = 'sess_' + crypto.randomUUID(); sess = { id: sid, messages: [], createdAt: Date.now(), updatedAt: Date.now() }; isNew = true; }
  sess.messages.push({ role: 'user', content: message.trim(), timestamp: Date.now() });
  const ctx = await faq(env, message);
  const msgs = [{ role: 'system', content: SYS + (ctx ? `\n\nFAQ:\n${ctx}` : '') }, ...sess.messages.slice(-10).map(m => ({ role: m.role, content: m.content }))];
  const stream = await env.AI.run('@cf/meta/llama-3-8b-instruct', { messages: msgs, stream: true });
  let full = '';
  const { readable, writable } = new TransformStream({
    transform(chunk, ctrl) {
      for (const ln of new TextDecoder().decode(chunk).split('\n'))
        if (ln.startsWith('data: ') && ln.slice(6) !== '[DONE]') try { full += JSON.parse(ln.slice(6)).response || ''; } catch {}
      ctrl.enqueue(chunk);
    },
    async flush() {
      if (full) { sess.messages.push({ role: 'assistant', content: full, timestamp: Date.now() }); sess.updatedAt = Date.now(); await env.CHAT_SESSIONS.put(sid, JSON.stringify(sess), { expirationTtl: TTL }); }
    }
  });
  stream.pipeTo(writable);
  return new Response(readable, { headers: { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache', ...cors, ...(isNew ? { 'Set-Cookie': `chatbot_session=${sid}; Path=/; HttpOnly; SameSite=Lax; Max-Age=${TTL}` } : {}) } });
}

async function seed(req, env) {
  if (req.method !== 'POST') return new Response('Method not allowed', { status: 405 });
  const faqs = [
    ['How long does shipping take?', 'Standard 5-7 days, Express 2-3 days, Same-day in select areas.'],
    ['What is your return policy?', '30-day returns for unused items. Electronics 15 days if defective.'],
    ['Do you offer free shipping?', 'Yes! Orders over $50 get free standard shipping.'],
    ['How can I track my order?', 'Check your email for tracking or log into your account.'],
    ['What payment methods do you accept?', 'Visa, Mastercard, Amex, PayPal, Apple Pay, Google Pay.'],
    ['Do you have a warranty?', 'All products have manufacturer warranty. Extended plans available.'],
    ['Can I cancel my order?', 'Within 1 hour if not processed. Otherwise return after delivery.'],
    ['Do you ship internationally?', 'Yes, 50+ countries. 7-14 days. Duties paid by customer.'],
  ];
  try {
    const vecs = await Promise.all(faqs.map(async ([q,a], i) => {
      const e = await env.AI.run('@cf/baai/bge-base-en-v1.5', { text: [q+' '+a] });
      return { id: `faq-${i+1}`, values: e.data?.[0] || [], metadata: { question: q, answer: a } };
    }));
    await env.VECTORIZE.upsert(vecs);
    return json({ success: true, count: faqs.length });
  } catch { return json({ error: 'Seed failed' }, 500); }
}

export default {
  async fetch(req, env) {
    const p = new URL(req.url).pathname;
    if (req.method === 'OPTIONS') return new Response(null, { headers: { ...cors, 'Access-Control-Allow-Methods': 'GET,POST,OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type' } });
    if (p === '/api/chat') return chat(req, env);
    if (p === '/api/history') { const s = cookie(req); return json({ messages: s ? (await env.CHAT_SESSIONS.get(s, 'json'))?.messages || [] : [] }); }
    if (p === '/api/seed') return seed(req, env);
    if (p === '/api/health') return json({ status: 'ok' });
    return env.ASSETS.fetch(req);
  }
};
```

Permettez-moi de décomposer les parties clés de ce code :

* **Gestion des sessions** : La fonction `cookie` extrait l'ID de session du cookie du navigateur de l'utilisateur. Lorsqu'un utilisateur discute pour la première fois, le Worker génère un ID de session unique, le stocke dans un cookie HTTP-only et sauvegarde l'historique de la conversation dans KV. Lors des visites suivantes, le Worker récupère la session et poursuit la conversation.

* **RAG avec Vectorize** : La fonction `faq` implémente le RAG. Elle convertit la question de l'utilisateur en un vecteur d'embedding en utilisant le modèle BGE, puis interroge Vectorize pour les trois entrées de FAQ les plus similaires. Ce contexte pertinent est ajouté à l'invite de l'IA, aidant l'IA à donner des réponses précises et fondées au lieu d'inventer des choses.

* **Réponses en streaming** : La fonction `chat` utilise un `TransformStream` pour traiter la réponse de l'IA au fur et à mesure qu'elle est diffusée. Chaque jeton est transmis au client immédiatement, créant un effet de frappe naturel. Lorsque le flux se termine, la réponse complète est sauvegardée dans KV.

* **Peuplement des FAQ** : La fonction `seed` remplit votre base de données de FAQ. Elle convertit chaque paire question-réponse en un vecteur d'embedding et le stocke dans Vectorize. Vous n'avez besoin d'appeler cela qu'une seule fois après le déploiement.

Maintenant que votre backend est prêt, créons le frontend. Mais d'abord, vous devez configurer Tailwind CSS pour styliser votre widget.

## **Comment configurer Tailwind CSS**

Votre widget de chatbot doit avoir l'air poli et professionnel. Pour cela, vous allez utiliser [Tailwind CSS](https://tailwindcss.com/), un framework CSS basé sur les utilitaires qui vous permet de styliser des éléments directement dans votre HTML en utilisant de petites classes à usage unique comme `bg-black`, `rounded-full` et `shadow-lg`.

Pourquoi Tailwind ? Eh bien, le CSS traditionnel nécessite d'écrire des feuilles de style séparées et d'inventer des noms de classes. Tailwind élimine cette surcharge en fournissant des classes d'utilitaires pré-construites. Cela est particulièrement utile pour un widget intégrable car tous les styles sont auto-contenus et n'entreront pas en conflit avec le CSS du site hôte.

Créez le fichier `tailwind.config.js` à la racine de votre projet :

```javascript
tail/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.{html,js}'],
  darkMode: 'class',
  theme: { extend: {} },
  plugins: []
};
```

Cette configuration indique à Tailwind de scanner tous les fichiers HTML et JavaScript dans le dossier `public` pour les noms de classes. Le paramètre `darkMode: 'class'` active le basculement du mode sombre en ajoutant une classe `dark` au conteneur du widget.

Créez le fichier source CSS à l'emplacement `src/input.css` :

```typescript
@tailwind base;
@tailwind components;src/input.css;
@tailwind utilities;
```

Ce fichier importe les styles de base de Tailwind, les classes de composants et les classes d'utilitaires. Lorsque vous construisez, Tailwind scanne votre code et génère un fichier CSS minimal contenant uniquement les classes que vous utilisez réellement.

Mettez à jour votre package.json avec les scripts de construction :

```json
{
	"name": "ai-chatbot-widget",
	"version": "1.0.0",
	"private": true,
	"scripts": {
		"build:css": "npx tailwindcss -i ./src/input.css -o ./public/styles.css --minify",
		"deploy": "npm run build:css && wrangler deploy",
		"dev": "npm run build:css && wrangler dev"
	},
	"devDependencies": {
		"autoprefixer": "^10.4.23",
		"postcss": "^8.5.6",
		"tailwindcss": "^3.4.19",
		"wrangler": "^4.56.0"
	}
}
```

Le script `build:css` compile et minifie votre Tailwind CSS. Les scripts `deploy` et `dev` construisent automatiquement le CSS avant de démarrer le serveur de développement ou de déployer.

Avec le style prêt à l'emploi, créons le widget avec lequel les utilisateurs interagiront réellement.

## **Comment créer le widget frontend**

Le widget frontend est un fichier JavaScript autonome qui crée l'ensemble de l'interface de chat. Lorsque quelqu'un ajoute votre script à son site web, il crée automatiquement le bouton de bulle de chat, la fenêtre de chat et gère toutes les fonctionnalités interactives.

Créez le fichier `public/widget.js` :

```javascript
/**
 * AI Chatbot Widget - Embeddable Script
 * Usage: <script src="https://your-domain.com/widget.js"></script>
 */
(function () {
  'use strict';
  const C = {
    u: window.CHATBOT_BASE_URL || '',
    t: window.CHATBOT_TITLE || 'AI Assistant',
    p: window.CHATBOT_PLACEHOLDER || 'Message...',
    g: window.CHATBOT_GREETING || '\ud83d\udc4b Hi! How can I help you today?'
  };
  let open = 0, msgs = [], typing = 0, menu = 0;
  let dark = matchMedia('(prefers-color-scheme:dark)').matches;
  const $ = id => document.getElementById(id);
  const tog = (e, c, on) => e.classList.toggle(c, on);
  function init() {
    const l = document.createElement('link');
    l.rel = 'stylesheet';
    l.href = C.u + '/styles.css';
    document.head.appendChild(l);
    const d = document.createElement('div');
    d.id = 'cb';
    d.innerHTML = `
      <button id="cb-btn" class="fixed bottom-6 right-6 w-14 h-14 bg-black rounded-full shadow-2xl flex items-center justify-center cursor-pointer hover:scale-110 transition-all z-[99999]">
        <svg id="cb-o" class="w-6 h-6 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/>
        </svg>
        <svg id="cb-x" class="w-6 h-6 text-white absolute opacity-0 scale-50 transition-all" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
      <div id="cb-w" class="fixed bottom-24 right-6 w-[400px] h-[600px] rounded-2xl shadow-2xl flex flex-col overflow-hidden z-[99999] opacity-0 scale-95 pointer-events-none transition-all origin-bottom-right bg-white dark:bg-gray-900">
        <!-- Header -->
        <div class="flex items-center justify-between px-5 py-4 border-b bg-white dark:bg-gray-900 border-gray-100 dark:border-gray-800">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-black rounded-full flex items-center justify-center">
              <span class="text-white font-bold text-lg">C</span>
            </div>
            <h3 class="font-semibold text-gray-900 dark:text-white">${C.t}</h3>
          </div>
          <div class="relative">
            <button id="cb-m" class="p-2 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-full">
              <svg class="w-5 h-5 text-gray-500" viewBox="0 0 24 24" fill="currentColor">
                <circle cx="12" cy="5" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="12" cy="19" r="1.5"/>
              </svg>
            </button>
            <div id="cb-d" class="hidden absolute right-0 top-full mt-2 w-44 bg-white dark:bg-gray-800 rounded-xl shadow-xl border border-gray-100 dark:border-gray-700 py-1 z-50">
              <button id="cb-th" class="w-full px-4 py-2 text-left text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-700 flex items-center gap-2">
                <svg id="cb-s" class="w-4 h-4 hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/></svg>
                <svg id="cb-n" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
                <span id="cb-tt">Mode sombre</span>
              </button>
              <button id="cb-cl" class="w-full px-4 py-2 text-left text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-700 flex items-center gap-2">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M3 6h18M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/>
                </svg>
                Effacer la discussion
              </button>
            </div>
          </div>
        </div>
        <!-- Messages -->
        <div id="cb-ms" class="flex-1 overflow-y-auto px-5 py-4 space-y-4 bg-gray-50 dark:bg-gray-950"></div>
        <!-- Typing Indicator -->
        <div id="cb-ty" class="hidden px-5 pb-2 bg-gray-50 dark:bg-gray-950">
          <div class="flex items-center gap-2 text-gray-400 text-sm">
            <div class="flex gap-1">
              <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></span>
              <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay:.15s"></span>
              <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay:.3s"></span>
            </div>
            Réflexion...
          </div>
        </div>
        <!-- Input -->
        <form id="cb-f" class="flex items-center gap-3 px-4 py-4 border-t bg-white dark:bg-gray-900 border-gray-100 dark:border-gray-800">
          <input id="cb-i" type="text" class="flex-1 px-4 py-3 bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-full text-sm text-gray-900 dark:text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:focus:ring-gray-600" placeholder="${C.p}" autocomplete="off"/>
          <button type="submit" id="cb-se" class="p-3 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-full disabled:opacity-50">
            <svg class="w-5 h-5 text-gray-600 dark:text-gray-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 2L11 13M22 2L15 22L11 13L2 9L22 2Z"/>
            </svg>
          </button>
        </form>
      </div>`;
    document.body.appendChild(d);
    bind();
    load();
    theme();
  }
  function bind() {
    $('cb-btn').onclick = flip;
    $('cb-f').onsubmit = send;
    $('cb-m').onclick = e => { e.stopPropagation(); menu = !menu; tog($('cb-d'), 'hidden', !menu); };
    $('cb-th').onclick = () => { dark = !dark; theme(); menu = 0; tog($('cb-d'), 'hidden', 1); };
    $('cb-cl').onclick = () => { msgs = []; draw(); menu = 0; tog($('cb-d'), 'hidden', 1); };
    document.onclick = () => menu && (menu = 0, tog($('cb-d'), 'hidden', 1));
  }
  function theme() {
    tog($('cb'), 'dark', dark);
    $('cb-tt').textContent = dark ? 'Mode clair' : 'Mode sombre';
    tog($('cb-s'), 'hidden', !dark);
    tog($('cb-n'), 'hidden', dark);
  }
  function flip() {
    open = !open;
    const w = $('cb-w'), o = $('cb-o'), x = $('cb-x');
    tog(w, 'opacity-0', !open);
    tog(w, 'scale-95', !open);
    tog(w, 'pointer-events-none', !open);
    tog(w, 'opacity-100', open);
    tog(w, 'scale-100', open);
    tog(o, 'opacity-0', open);
    tog(o, 'scale-50', open);
    tog(x, 'opacity-0', !open);
    tog(x, 'scale-50', !open);
    tog(x, 'opacity-100', open);
    tog(x, 'scale-100', open);
    if (open) {
      $('cb-i').focus();
      if (!msgs.length) add('assistant', C.g);
    }
  }
  function add(r, c) {
    msgs.push({ role: r, content: c });
    draw();
  }
  function esc(t) {
    const d = document.createElement('div');
    d.textContent = t;
    return d.innerHTML.replace(/\n/g, '<br>');
  }
  function draw() {
    $('cb-ms').innerHTML = msgs.map((m, i) => m.role === 'user'
      ? `<div class="flex justify-end">
          <div class="bg-black text-white rounded-2xl rounded-br-md px-4 py-3 max-w-[85%]">
            <div id="m${i}" class="text-sm whitespace-pre-wrap">${esc(m.content)}</div>
          </div>
        </div>`
      : `<div class="flex justify-start">
          <div class="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 rounded-2xl rounded-bl-md px-4 py-3 max-w-[85%] border border-gray-200 dark:border-gray-700 shadow-sm">
            <div class="flex items-center gap-2 mb-2">
              <div class="w-6 h-6 bg-black rounded-full flex items-center justify-center">
                <span class="text-white font-bold text-xs">C</span>
              </div>
              <span class="text-sm font-medium text-gray-700 dark:text-gray-300">${C.t}</span>
            </div>
            <div id="m${i}" class="text-sm leading-relaxed whitespace-pre-wrap">${esc(m.content)}</div>
          </div>
        </div>`
    ).join('');
    $('cb-ms').scrollTop = $('cb-ms').scrollHeight;
  }
  async function send(e) {
    e.preventDefault();
    const m = $('cb-i').value.trim();
    if (!m || typing) return;
    add('user', m);
    $('cb-i').value = '';
    $('cb-se').disabled = 1;
    typing = 1;
    tog($('cb-ty'), 'hidden', 0);
    try {
      const r = await fetch(C.u + '/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: m }),
        credentials: 'include'
      });
      if (!r.ok) throw 0;
      const rd = r.body.getReader();
      const dc = new TextDecoder();
      let t = '', idx = null;
      while (1) {
        const { done, value } = await rd.read();
        if (done) break;
        for (const ln of dc.decode(value, { stream: 1 }).split('\n')) {
          if (!ln.startsWith('data: ')) continue;
          const d = ln.slice(6);
          if (d === '[DONE]') continue;
          try {
            const p = JSON.parse(d);
            if (p.response) {
              t += p.response;
              if (idx === null) {
                tog($('cb-ty'), 'hidden', 1);
                typing = 0;
                msgs.push({ role: 'assistant', content: t });
                idx = msgs.length - 1;
                draw();
              } else {
                msgs[idx].content = t;
                const el = $('m' + idx);
                if (el) el.innerHTML = esc(t);
              }
              $('cb-ms').scrollTop = $('cb-ms').scrollHeight;
            }
          } catch {}
        }
      }
    } catch {
      tog($('cb-ty'), 'hidden', 1);
      typing = 0;
      add('assistant', 'Désolé, une erreur est survenue.');
    } finally {
      $('cb-se').disabled = 0;
      typing = 0;
      tog($('cb-ty'), 'hidden', 1);
    }
  }
  async function load() {
    try {
      const r = await fetch(C.u + '/api/history', { credentials: 'include' });
      if (r.ok) {
        const d = await r.json();
        if (d.messages?.length) {
          msgs = d.messages;
          draw();
        }
      }
    } catch {}
  }
  document.readyState === 'loading'
    ? document.addEventListener('DOMContentLoaded', init)
    : init();
})();
```

Le widget utilise une IIFE (Immediately Invoked Function Expression) pour éviter de polluer l'espace de noms global. Voici les fonctions clés :

* **init()** : Crée le HTML du widget et l'injecte dans la page

* **bind()** : Configure tous les écouteurs d'événements

* **theme()** : Basculer entre le mode sombre et le mode clair

* **flip()** : Ouvre et ferme la fenêtre de chat avec des animations

* **draw()** : Affiche tous les messages

* **send()** : Gère l'envoi des messages avec streaming

* **load()** : Charge l'historique de la discussion depuis le serveur

Le gestionnaire de streaming dans `send()` est particulièrement important. Il lit la réponse de l'IA morceau par morceau et met à jour l'interface utilisateur à chaque token reçu. Au lieu de réafficher toute la liste des messages à chaque token (ce qui causerait un scintillement visuel), il met à jour uniquement le contenu de l'élément de message actuel. Cela crée un effet de frappe fluide.

Maintenant, vous avez besoin d'une page simple pour tester le tout avant le déploiement.

## Créer la page de démonstration

La page de démonstration sert de terrain d'essai pendant le développement et de vitrine pour votre widget. Lorsque vous ou vos utilisateurs visitez directement l'URL de votre Worker déployé, vous verrez cette page avec le widget de chatbot déjà intégré.

Créez `public/index.html` : Cette page de démonstration sera pour vos tests internes.

```xml
<!DOCTYPE html>
<html lang="fr">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Démonstration du Widget de Chatbot IA</title>
  <link rel="stylesheet" href="/styles.css">
</head>

<body class="min-h-screen bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center p-8">
  <div class="text-center text-white">
    <h1 class="text-4xl font-bold mb-4">Widget de Chatbot IA</h1>
  </div>
  <script>    window.CHATBOT_BASE_URL = ''; window.CHATBOT_TITLE = 'Support'; window.CHATBOT_GREETING = "\ud83d\udc4b Bonjour ! Je suis là pour répondre à vos questions !";  </script>
  <script src="/widget.js"></script>
</body>

</html>
```

Cette page minimale affiche un titre et charge le widget de chatbot. La variable `CHATBOT_BASE_URL` est définie sur une chaîne vide car, lorsqu'elle est servie depuis le même Worker, les URL relatives fonctionnent automatiquement. Il s'agit du même code que quelqu'un utiliserait pour intégrer le widget sur son propre site web, simplement avec sa propre URL de base à la place.

Avec tout le code en place, vous êtes prêt à déployer votre chatbot sur Cloudflare.

## Comment l'exécuter sur votre système local

Une fois tous les fichiers ajoutés, exécutez la commande `npm run dev` pour voir à quoi ressemble le widget de chat sur `http://localhost:8787` :

![Comment votre chatbot devrait apparaître](https://cdn.hashnode.com/res/hashnode/image/upload/v1766525553600/6a0dd8ed-5f2f-49ad-924d-3ef2fb143a42.png align="center")

## **Comment déployer sur Cloudflare**

Le déploiement se fait avec une seule commande. Exécutez :

```powershell
npm run deploy
```

Cette commande construit d'abord votre Tailwind CSS, puis déploie tout sur Cloudflare. Une fois le déploiement terminé, vous verrez une URL comme `https://ai-chatbot-widget.VOTRE-SOUS-DOMAINE.workers.dev`.

Dans mon cas, l'URL est [https://ai-chatbot-widget.mv.workers.dev/](https://ai-chatbot-widget.mv.workers.dev/)

### Comment alimenter la base de données FAQ

Avant que votre chatbot puisse répondre aux questions de votre FAQ, vous devez remplir l'index Vectorize. Exécutez cette commande (remplacez l'URL par votre URL de déploiement réelle) :

```powershell
curl -X POST https://ai-chatbot-widget.VOTRE-SOUS-DOMAINE.workers.dev/api/seed
```

Vous devriez voir cette réponse :

```json
{"success":true,"count":8}
```

Cela signifie que huit entrées FAQ ont été converties en vecteurs et stockées dans Vectorize. Votre chatbot est maintenant en ligne et prêt à répondre aux questions !

Visitez votre URL de déploiement pour le tester. Essayez de poser des questions sur la livraison, les retours ou les méthodes de paiement. Le chatbot répondra en utilisant le contexte de la FAQ que vous venez d'alimenter.

Votre chatbot est maintenant en ligne et prêt à répondre aux questions. Vous pouvez vérifier le tableau de bord Cloudflare pour voir le déploiement. (La capture d'écran ci-dessous provient du tableau de bord Cloudflare.)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1766526373608/54e674c1-0c7c-4187-bf6f-e227763f7cef.png align="center")

## Comment intégrer le widget sur n'importe quel site web

Maintenant, la partie excitante : ajouter votre chatbot à n'importe quel site web. Il suffit de deux balises de script avant la balise de fermeture `</body>` :

```xml
<script>
  window.CHATBOT_BASE_URL = 'https://ai-chatbot-widget.VOTRE-SOUS-DOMAINE.workers.dev';
  window.CHATBOT_TITLE = 'Votre Entreprise';
  window.CHATBOT_GREETING = '\ud83d\udc4b Comment puis-je vous aider aujourd'hui ?';
</script>
<script src="https://ai-chatbot-widget.VOTRE-SOUS-DOMAINE.workers.dev/widget.js"></script>
```

Remplacez `VOTRE-SOUS-DOMAINE` par votre sous-domaine Cloudflare Workers réel.

Ou vous pouvez également ouvrir votre URL de déploiement Cloudflare pour les tests.

![Test du chatbot](https://cdn.hashnode.com/res/hashnode/image/upload/v1766526312388/9f9a2b18-839d-44d8-b6c2-6f185c61442d.gif align="center")

### Options de configuration

Vous pouvez personnaliser le widget en utilisant ces variables :

| **Variable** | **Description** | **Valeur par défaut** |
| --- | --- | --- |
| `CHATBOT_BASE_URL` | Votre URL de Worker déployée | `''` (même origine) |
| `CHATBOT_TITLE` | Nom affiché dans l'en-tête | `'AI Assistant'` |
| `CHATBOT_PLACEHOLDER` | Texte de l'espace réservé du champ de saisie | `'Message...'` |
| `CHATBOT_GREETING` | Message de salutation initial | `\ud83d\udc4b Bonjour ! Comment puis-je vous aider aujourd'hui ?` |

## Comment personnaliser votre chatbot

Votre chatbot fonctionne, mais vous souhaitez probablement l'adapter à votre cas d'utilisation spécifique. Voici les personnalisations les plus courantes.

### Comment ajouter vos propres FAQ

Ouvrez `src/index.js` et trouvez la fonction `seed`. Remplacez les FAQ d'exemple par vos propres paires de questions-réponses :

```javascript
const faqs = [
  ['Votre question ici ?', 'Votre réponse ici.'],
  ['Une autre question ?', 'Une autre réponse.']
  // Ajoutez plus de paires Q&R
];
```

Puis redéployez avec `npm run deploy` et appelez à nouveau le point de terminaison `/api/seed` pour mettre à jour votre base de données vectorielle.

### Comment changer la personnalité de l'IA

Modifiez la constante `SYS` en haut de `src/index.js` :

```javascript
const SYS = `Vous êtes un assistant amical pour [Votre Entreprise].
Vous aidez les clients avec [vos principaux services].
Soyez toujours utile et professionnel.`;
```

Cette invite système façonne la manière dont l'IA répond aux utilisateurs.

### Comment styliser le widget

Tous les styles utilisent les classes Tailwind CSS dans `widget.js`. Pour changer l'apparence :

* **Couleurs** : Changez `bg-black` en votre couleur de marque

* **Taille** : Ajustez `w-[400px] h-[600px]` pour les dimensions de la fenêtre de chat

* **Position** : Modifiez `bottom-6 right-6` pour le placement

## **Conclusion**

Félicitations ! Vous avez construit un widget de chatbot IA complet qui rivalise avec les solutions SaaS coûteuses comme Intercom et Drift. Votre chatbot diffuse les réponses de l'IA en temps réel, répond aux questions basées sur votre FAQ en utilisant RAG, et se souvient des conversations entre les sessions—le tout gratuitement.

Voici un récapitulatif rapide de ce que vous avez construit :

* Un backend Worker qui gère le chat, les sessions et la recherche de FAQ

* Un widget frontend qui peut être intégré sur n'importe quel site web

* Intégration avec Workers AI pour des réponses intelligentes

* Vectorize pour la recherche sémantique de FAQ

* KV pour l'historique des conversations persistant

La pile Cloudflare offre des niveaux gratuits généreux qui devraient couvrir la plupart des cas d'utilisation :

* **Workers** : 100 000 requêtes par jour

* **Workers AI** : 10 000 neurones par jour

* **Vectorize** : 5 millions d'opérations vectorielles par mois