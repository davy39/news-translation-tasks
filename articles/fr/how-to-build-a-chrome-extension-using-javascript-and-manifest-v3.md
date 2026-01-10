---
title: Comment créer une extension Chrome qui analyse n'importe quelle page Web en
  utilisant JavaScript et Manifest V3
subtitle: ''
author: Hitesh Chauhan
co_authors: []
series: null
date: '2025-10-28T16:57:54.636Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chrome-extension-using-javascript-and-manifest-v3
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761670419000/13ac96ca-6e28-413f-a0e0-56ed353a007c.png
tags:
- name: chrome extension
  slug: chrome-extension
- name: ai seo
  slug: ai-seo
- name: devtools
  slug: devtools
- name: JavaScript
  slug: javascript
seo_title: Comment créer une extension Chrome qui analyse n'importe quelle page Web
  en utilisant JavaScript et Manifest V3
seo_desc: 'Have you ever visited a website and wondered how well is this page structured?
  Does it have a meta description? How many links or headings does it use?

  Usually, you’d open DevTools or an SEO auditing tool to find answers to these questions.
  But what ...'
---

Avez-vous déjà visité un site Web en vous demandant si la page était bien structurée ? Possède-t-elle une méta-description ? Combien de liens ou de titres utilise-t-elle ?

Habituellement, vous ouvririez les DevTools ou un outil d'audit SEO pour trouver des réponses à ces questions. Mais et si vous pouviez analyser n'importe quelle page Web instantanément, sans quitter votre navigateur ?

Dans ce tutoriel, vous apprendrez à créer une extension Chrome qui scanne et analyse n'importe quelle page Web pour en extraire les titres, les méta-descriptions, les en-têtes et les liens.

À la fin de cet article, vous :

* Comprendrez comment Manifest V3 fonctionne dans les extensions Chrome
    
* Apprendrez à injecter des content scripts dans les pages Web
    
* Construirez une interface utilisateur (UI) de popup qui récupère et affiche des données structurées
    
* Explorerez comment cette même base peut être étendue avec des analyses propulsées par l'IA
    

💡 Ce guide se concentre sur l'apprentissage et l'éducation – aucun Framework ou outil de build n'est requis. Juste du HTML, du CSS et du vanilla JavaScript.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Étape 1 : Comprendre le fonctionnement des extensions Chrome](#heading-etape-1-comprendre-le-fonctionnement-des-extensions-chrome)
    
* [Étape 2 : Configurer la structure du projet](#heading-etape-2-configurer-la-structure-du-projet)
    
* [Étape 3 : Définir le fichier Manifest](#heading-etape-3-definir-le-fichier-manifest)
    
* [Étape 4 : Créer l'interface utilisateur de la popup](#heading-etape-4-creer-l-interface-utilisateur-de-la-popup)
    
* [Étape 5 : Écrire le Content Script (content.js)](#heading-etape-5-ecrire-le-content-script-contentjs)
    
* [Étape 6 : Connecter la popup et le Content Script](#heading-etape-6-connecter-la-popup-et-le-content-script)
    
* [Étape 7 : Charger et tester votre extension](#heading-etape-7-charger-et-tester-votre-extension)
    
* [Étape 8 : Ajouter des améliorations optionnelles](#heading-etape-8-ajouter-des-ameliorations-optionnelles)
    
* [Étape 9 : Publier sur le Chrome Web Store](#heading-etape-9-publier-sur-le-chrome-web-store)
    
* [Dernières réflexions](#heading-dernieres-reflexions)
    

## 🧰 Prérequis

Avant de commencer ce tutoriel, assurez-vous d'avoir :

* Une compréhension de base du HTML, du CSS et du JavaScript
    
* Une version récente de Google Chrome installée sur votre système
    
* Une familiarité avec l'utilisation des DevTools de Chrome (optionnel mais utile)
    
* Un éditeur de code comme VS Code ou Sublime Text
    
* Un dossier local où vous pouvez créer et organiser les fichiers de votre extension
    

💡 Encore une fois, aucun Framework ou outil de build n'est requis. Nous utiliserons uniquement du vanilla JavaScript et des technologies Web simples tout au long de ce guide.

## 🧩 Étape 1 : Comprendre le fonctionnement des extensions Chrome

Une extension Chrome n'est qu'un ensemble de technologies Web – HTML, CSS et JS – qui étend les fonctionnalités du navigateur.

Les extensions peuvent comporter plusieurs parties :

* **Fichier Manifest** (`manifest.json`) : définit les permissions, les icônes et la structure.
    
* **Content scripts** : s'exécutent à l'intérieur des pages Web et accèdent au DOM.
    
* **Background scripts** : gèrent la logique de longue durée ou pilotée par les événements.
    
* **Interface utilisateur de la popup** : ce que les utilisateurs voient lorsqu'ils cliquent sur l'icône de votre extension.
    

Voici le flux de haut niveau de ce que nous allons construire :

```plaintext
[Popup UI] <—> [Content Script] <—> [Web Page DOM]
```

Lorsque l'utilisateur clique sur « Analyser », la popup envoie un message au content script. Le script lit ensuite le DOM et renvoie les résultats tels que le titre de la page, la description, les en-têtes et les liens.

## 🧠 Étape 2 : Configurer la structure du projet

Créez un nouveau dossier appelé `page-analyzer-extension`. À l'intérieur, créez ces fichiers :

```plaintext
page-analyzer-extension/
│
├── manifest.json
├── popup.html
├── popup.js
├── content.js
├── styles.css
└── icons/
    ├── icon16.png
    ├── icon48.png
    └── icon128.png
```

Les icônes sont optionnelles, mais elles donnent à l'extension un aspect professionnel. Vous pouvez utiliser des espaces réservés ou les générer depuis [favicon.io](https://favicon.io/).

## ⚙️ Étape 3 : Définir le fichier Manifest

Créez `manifest.json` et collez ceci :

```json
{
  "manifest_version": 3,
  "name": "Page Analyzer",
  "version": "1.0",
  "description": "Analyze any web page for its title, description, headings, and links.",
  "permissions": ["activeTab", "scripting"],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content.js"]
    }
  ]
}
```

Analysons cela :

* `manifest_version: 3` : la dernière version avec des améliorations de sécurité et de performance
    
* `permissions` : permet à l'extension d'accéder à l'onglet actif et d'exécuter des scripts
    
* `content_scripts` : définit quels fichiers JS doivent s'exécuter automatiquement dans les pages Web
    

## 🧩 Étape 4 : Créer l'interface utilisateur de la popup

La popup apparaît lorsque les utilisateurs cliquent sur l'icône de l'extension.

`popup.html` :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Analyzer</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <h2>Page Analyzer</h2>
    <p>Click below to analyze the current page:</p>
    <button id="analyze">Analyze Page</button>
    <div id="results"></div>

    <script src="popup.js"></script>
  </body>
</html>
```

`styles.css` :

```css
body {
  font-family: system-ui, sans-serif;
  padding: 12px;
  width: 280px;
}
button {
  background: #2563eb;
  color: white;
  border: none;
  padding: 8px 14px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
}
#results {
  margin-top: 12px;
  font-size: 13px;
  line-height: 1.4;
  word-wrap: break-word;
}
```

## 🧠 Étape 5 : Écrire le Content Script (`content.js`)

Ce script analysera la page Web.

```js
function analyzePage() {
  const title = document.title || "No title found";
  const description =
    document.querySelector('meta[name="description"]')?.content || "No description found";
  const headings = Array.from(document.querySelectorAll("h1, h2, h3")).map((h) =>
    h.innerText.trim()
  );
  const links = document.querySelectorAll("a").length;

  return {
    title,
    description,
    headings,
    linkCount: links,
    domain: location.hostname,
  };
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "analyze") {
    sendResponse(analyzePage());
  }
});
```

Ce qui se passe ici :

* Nous extrayons le titre, la description, les en-têtes et le nombre total de liens
    
* Nous renvoyons ces données sous forme d'objet structuré
    
* Le script écoute les messages de la popup et répond avec l'analyse
    

## ⚡ Étape 6 : Connecter la popup et le Content Script

Dans `popup.js`, ajoutez la logique qui déclenche l'analyse de la page.

```js
document.getElementById("analyze").addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.tabs.sendMessage(tab.id, { action: "analyze" }, (response) => {
    const resultContainer = document.getElementById("results");

    if (!response) {
      resultContainer.innerText = "Unable to analyze this page.";
      return;
    }

    const { title, description, headings, linkCount, domain } = response;
    resultContainer.innerHTML = `
      <strong>Domain:</strong> ${domain}<br/>
      <strong>Title:</strong> ${title}<br/>
      <strong>Description:</strong> ${description}<br/>
      <strong>Headings:</strong> ${
        headings.length ? headings.join(", ") : "No headings found"
      }<br/>
      <strong>Links:</strong> ${linkCount}
    `;
  });
});
```

Ceci utilise la **Chrome Tabs API** pour trouver l'onglet actuel et envoyer un message au content script. Lorsque le script répond, nous mettons à jour la popup avec les résultats.

## 🧪 Étape 7 : Charger et tester votre extension

1. Ouvrez chrome://extensions/
    
2. Activez le Mode développeur
    
3. Cliquez sur Charger l'extension non empaquetée
    
4. Sélectionnez votre dossier de projet
    

Maintenant, épinglez votre extension à la barre d'outils, ouvrez n'importe quel site Web et cliquez sur « Analyser la page ».

Vous verrez instantanément :

* Le titre de la page
    
* La méta-description
    
* Les en-têtes extraits (H1–H3)
    
* Le nombre de liens
    
* Le nom de domaine
    

🎉 Félicitations ! Vous avez construit un analyseur de page Web fonctionnel.

## 🧩 Étape 8 : Ajouter des améliorations optionnelles

Maintenant que les bases fonctionnent, voici quelques façons de faire passer votre projet au niveau supérieur.

### 🧠 1. Ajouter des analyses par IA

Vous pouvez vous connecter à une API d'IA (comme OpenAI ou Gemini) pour résumer la page ou évaluer la structure SEO.

```js
// Exemple : pseudo-code pour appeler une API d'IA
const aiResponse = await fetch("https://api.openai.com/v1/chat/completions", {
  method: "POST",
  headers: { Authorization: `Bearer ${API_KEY}` },
  body: JSON.stringify({
    model: "gpt-4o-mini",
    messages: [
      { role: "system", content: "You are an SEO assistant." },
      { role: "user", content: `Analyze the following page info: ${JSON.stringify(pageData)}` }
    ]
  })
});
```

Par exemple, après avoir construit cet analyseur de base, je l'ai étendu pour en faire une extension complète [RankingsFactor AI SEO Extension](https://rankingsfactor.com/extension) qui combine cette même base avec :

* Des suggestions de mots-clés générées par l'IA
    
* Des recommandations d'amélioration des métadonnées
    
* La capture automatique de captures d'écran
    
* La détection de la fraîcheur de la page
    

Cela démontre comment un simple projet de développeur peut évoluer vers un outil puissant et prêt pour la production.

### 🔍 2. Détecter les balises SEO manquantes

Vous pouvez vérifier les balises manquantes comme ceci :

```js
const missingTags = [];
if (!document.querySelector('meta[name="description"]')) missingTags.push("description");
if (!document.querySelector('meta[property="og:title"]')) missingTags.push("og:title");
```

### 🖼️ 3. Ajouter l'exportation de captures d'écran ou de rapports

Utilisez l'API `chrome.tabs.captureVisibleTab()` pour prendre une capture d'écran, ou générez un rapport HTML/JSON téléchargeable.

## 🧭 Étape 9 : Publier sur le Chrome Web Store

Une fois que vous avez testé votre extension, visitez [chrome.google.com/webstore/devconsole](https://chrome.google.com/webstore/devconsole). Vous devrez payer des frais d'inscription de développeur uniques de 5 $, puis vous pourrez télécharger votre extension sous forme de fichier ZIP. Assurez-vous d'écrire une description claire et utile avant de soumettre votre extension pour examen.

## ✅ Dernières réflexions

Dans ce tutoriel, vous avez appris :

* Comment les extensions Chrome communiquent entre les scripts et les pages Web
    
* Comment extraire en toute sécurité les données du DOM
    
* Comment afficher des informations structurées dans une interface utilisateur de popup
    
* Comment étendre les outils du navigateur avec l'IA pour une analyse plus intelligente
    

Les extensions de navigateur sont un moyen incroyable d'apporter l'automatisation Web, l'analyse et la créativité directement dans votre flux de travail. Que vous analysiez des pages, amélioriez l'accessibilité ou expérimentiez avec l'IA, vous avez maintenant les bases pour construire tout ce que vous imaginez.