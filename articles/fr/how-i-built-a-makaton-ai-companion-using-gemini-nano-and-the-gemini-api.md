---
title: Comment j'ai conçu un compagnon IA Makaton avec Gemini Nano et l'API Gemini
subtitle: ''
author: OMOTAYO OMOYEMI
co_authors: []
series: null
date: '2025-11-07T16:33:07.595Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-makaton-ai-companion-using-gemini-nano-and-the-gemini-api
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762533154134/e2209ade-6971-464b-aeef-f05abd0a30d7.png
tags:
- name: geminiAPI
  slug: geminiapi
- name: Computer Vision
  slug: computer-vision
- name: nlp
  slug: nlp
- name: gemini-nano
  slug: gemini-nano
seo_title: Comment j'ai conçu un compagnon IA Makaton avec Gemini Nano et l'API Gemini
seo_desc: 'When I started my research on AI systems that could translate Makaton (a
  sign and symbol language designed to support speech and communication), I wanted
  to bridge a gap in accessibility for learners with speech or language difficulties.

  Over time, t...'
---

Lorsque j'ai commencé mes recherches sur les systèmes d'IA capables de traduire le Makaton (un langage de signes et de symboles conçu pour soutenir la parole et la communication), je voulais combler un manque d'accessibilité pour les apprenants ayant des difficultés d'élocution ou de langage.

Au fil du temps, cet intérêt académique a évolué vers un prototype fonctionnel qui combine l'IA sur l'appareil et l'IA dans le cloud pour décrire des images et les traduire en significations anglaises. L'idée était simple : je voulais construire une application web légère qui reconnaisse les gestes ou les symboles Makaton et fournisse instantanément une interprétation en anglais.

Dans cet article, je vais vous expliquer comment j'ai construit mon compagnon IA Makaton, une application web d'une seule page alimentée par Gemini Nano (sur l'appareil) et l'API Gemini (cloud). Vous verrez comment cela fonctionne, comment j'ai résolu des problèmes courants comme le CORS et les erreurs de modèle d'API, et comment ce petit projet est devenu une étape de mon parcours vers l'IA pour l'accessibilité.

À la fin de cet article, vous serez capable de :

* Comprendre le concept de base du Makaton et pourquoi il est important pour l'accessibilité et l'éducation inclusive.
    
* Apprendre à combiner l'IA sur l'appareil (Gemini Nano) et l'IA basée sur le cloud (API Gemini) dans un seul projet web.
    
* Construire une application web fonctionnelle alimentée par l'IA capable de décrire des images et de les mapper à des significations anglaises prédéfinies.
    
* Découvrir comment gérer les erreurs courantes telles que les problèmes d'endpoint de modèle, les clés API manquantes et les restrictions CORS lors de l'utilisation d'API d'IA générative.
    
* Apprendre à stocker les clés API localement pour la confidentialité des utilisateurs à l'aide de `localStorage`.
    
* Utiliser la synthèse vocale du navigateur pour convertir les significations anglaises générées par l'IA en sortie vocale.
    

## Table des matières

* [Outils et Stack technique](#heading-outils-et-stack-technique)
    
* [Construire l'application étape par étape](#heading-construire-l-application-etape-par-etape)
    
* [Comment résoudre les problèmes courants](#heading-comment-resoudre-les-problemes-courants)
    
* [Démo : Le compagnon IA Makaton en action](#heading-demo-le-compagnon-ia-makaton-en-action)
    
* [Réflexions plus larges](#heading-reflexions-plus-larges)
    
* [Conclusion](#heading-conclusion)
    

## Outils et Stack technique

Pour construire le compagnon IA Makaton, je voulais quelque chose de léger, rapide à prototyper et facile à exécuter pour n'importe qui sans dépendances compliquées. J'ai choisi une Stack technique web classique en mettant l'accent sur l'accessibilité et la transparence.

Voici ce que j'ai utilisé :

### Frontend

* **HTML + CSS + JavaScript (Vanilla) :** Pas de Frameworks, juste du code propre et compréhensible que tout débutant peut suivre.
    
* Une seule page `index.html` gère l'interface de téléchargement, l'affichage des résultats et la logique d'IA.
    

### Composants d'IA

* **Gemini Nano** s'exécute localement dans Chrome Canary. Ce modèle sur l'appareil permet aux utilisateurs de générer du texte court sans appeler l'API cloud.
    
* **API Gemini (Cloud)** utilisée comme solution de repli lorsque l'IA sur l'appareil n'est pas disponible ou lorsqu'une analyse d'image est requise.
    
    * Modèles testés : `gemini-1.5-flash` et `gemini-pro-vision`.
        
    * La logique de repli garantit que l'application vérifie plusieurs endpoints de modèle si l'un d'eux renvoie une erreur 404.
        

### Stockage local

* La clé API Gemini est stockée en toute sécurité dans le `localStorage` du navigateur, de sorte qu'elle ne quitte jamais l'ordinateur de l'utilisateur.
    

### API SpeechSynthesis du navigateur

* Convertit la signification anglaise traduite en audio parlé en un clic.
    

### Logique de mapping

* Un petit dictionnaire personnalisé (`mapping.js`) lie les descriptions générées par l'IA aux significations Makaton probables. Par exemple : `{ keywords: ["open hand", "raised hand", "wave"], meaning: "Hello / Stop" }`.
    

### Serveur local

* L'application est servie localement à l'aide du serveur HTTP intégré de Python pour éviter les problèmes de CORS :
    
    `python -m http.server 8080`
    

Ouvrez ensuite `http://localhost:8080` dans Chrome Canary.

## Construire l'application étape par étape

Plongeons maintenant dans le fonctionnement interne du compagnon IA Makaton. Ce projet suit un flux simple mais efficace : Télécharger une image → Décrire (IA) → Mapper à la signification → Parler ou Copier le résultat.

Nous allons passer en revue chaque partie étape par étape.

### 1\. Configuration du dossier du projet

Vous n'avez pas besoin d'une configuration complexe. Créez simplement un nouveau dossier et ajoutez ces fichiers :

```plaintext
makaton-ai-companion/
│
├── index.html
├── styles.css
├── app.js
└── lib/
    ├── mapping.js
    └── ai.js
```

Si vous préférez une version prête à l'emploi, vous pouvez tout servir à partir d'un fichier zip (je partagerai un lien GitHub à la fin).

### 2\. Création de la structure HTML de base

Votre fichier `index.html` définit l'interface où les utilisateurs téléchargent une image, cliquent sur *Describe* et visualisent les résultats.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Makaton AI Companion</title>
  <link rel="stylesheet" href="styles.css"/>
</head>
<body>
  <header class="app-header">
    <h1>🧩 Makaton AI Companion</h1>
    <button id="btnSettings" class="btn secondary">Settings</button>
  </header>

  <main class="container">
    <section class="card">
      <h2>1) Upload an image (Makaton sign/symbol)</h2>
      <label for="file">
        Choose an image file
        <input id="file" type="file" accept="image/*" title="Select an image file"/>
      </label>
      <div id="preview" class="preview hidden"></div>
      <p id="status" class="status"></p>
      <div class="actions">
        <button id="btnDescribe" class="btn">Describe (Cloud or Nano)</button>
        <button id="btnType" class="btn ghost">Type a description instead</button>
      </div>
      <div id="typedBox" class="typed hidden">
        <textarea id="typed" rows="3" placeholder="Describe what you see..."></textarea>
        <button id="btnUseTyped" class="btn">Use this description</button>
      </div>
    </section>

    <section class="card">
      <h2>2) AI Output</h2>
      <div class="grid">
        <div>
          <h3>Image Description</h3>
          <div id="output" class="output"></div>
        </div>
        <div>
          <h3>English Meaning (Mapped)</h3>
          <div id="meaning" class="meaning"></div>
          <div class="actions">
            <button id="btnSpeak" class="btn ghost" disabled>🔊 Speak</button>
            <button id="btnCopy" class="btn ghost" disabled>📋 Copy</button>
          </div>
        </div>
      </div>
    </section>
  </main>

  <dialog id="settings">
    <form method="dialog" class="settings-form">
      <h2>Settings</h2>
      <label>Gemini API key (optional)<input id="apiKey" type="password" placeholder="AIza..."/></label>
      <div class="settings-actions">
        <button id="btnSaveKey" type="submit" class="btn">Save</button>
        <button id="btnCloseSettings" type="button" class="btn secondary">Close</button>
      </div>
      <div id="apiStatus" class="api-status"></div>
    </form>
  </dialog>

  <script type="module" src="lib/mapping.js"></script>
  <script type="module" src="lib/ai.js"></script>
  <script type="module" src="app.js"></script>
</body>
</html>
```

Cette interface est intentionnellement minimale : pas de Frameworks, pas d'outils de build, juste du HTML clair.

### 3\. Mapping des descriptions aux significations Makaton

Le fichier `mapping.js` contient un dictionnaire simple basé sur des mots-clés. Lorsque l'IA décrit une image (comme *"a raised open hand"*), l'application recherche des mots-clés qui correspondent à des signes Makaton connus.

```javascript
// lib/mapping.js

export const MAKATON_GLOSSES = [
  { keywords: ["open hand", "raised hand", "wave", "hand up"], meaning: "Hello / Stop" },
  { keywords: ["eat", "food", "spoon", "hand to mouth"], meaning: "Eat" },
  { keywords: ["drink", "cup", "glass", "bottle"], meaning: "Drink" },
  { keywords: ["home", "house", "roof"], meaning: "Home" },
  { keywords: ["sleep", "bed", "eyes closed"], meaning: "Sleep" },
  { keywords: ["book", "reading", "pages"], meaning: "Book / Read" },
  // Added so your current screenshot maps correctly:
  { keywords: ["help", "assist", "thumb on palm", "hand over hand", "assisting"], meaning: "Help" },
];

export function mapDescriptionToMeaning(desc) {
  if (!desc) return "";
  const d = desc.toLowerCase();
  for (const entry of MAKATON_GLOSSES) {
    if (entry.keywords.some(k => d.includes(k))) return entry.meaning;
  }
  if (d.includes("hand")) return "Gesture / Hand sign (clarify)";
  return "No direct mapping found.";
}
```

C'est simple mais suffisamment efficace pour simuler une véritable traduction de symbole en langage à des fins de démonstration.

### 4\. Ajout de la logique d'IA Gemini

Le fichier `ai.js` se connecte à Gemini Nano (sur l'appareil) ou à l'API Gemini (cloud). Si Nano n'est pas disponible, l'application se replie sur le modèle cloud. Et si cela échoue, elle permet aux utilisateurs de saisir manuellement une description.

```javascript
// lib/ai.js — dynamic model discovery (try-all version)

// --- On-device availability (Gemini Nano) ---
export async function checkAvailability() {
  const res = { nanoTextPossible: false };
  try {
    const canCreate = self.ai?.canCreateTextSession || self.ai?.languageModel?.canCreate;
    if (typeof canCreate === "function") {
      const ok = await (self.ai.canCreateTextSession?.() || self.ai.languageModel.canCreate?.());
      res.nanoTextPossible = ok === "readily" || ok === "after-download" || ok === true;
    }
  } catch {}
  return res;
}

export async function createNanoTextSession() {
  if (self.ai?.createTextSession) return await self.ai.createTextSession();
  if (self.ai?.languageModel?.create) return await self.ai.languageModel.create();
  throw new Error("Gemini Nano text session not available");
}

// --- Cloud: dynamically discover models for this key ---
async function listModels(key) {
  const url = "https://generativelanguage.googleapis.com/v1/models?key=" + encodeURIComponent(key);
  const r = await fetch(url);
  if (!r.ok) throw new Error("ListModels failed: " + (await r.text()));
  const j = await r.json();
  return (j.models || []).map(m => m.name).filter(Boolean);
}

function rankModels(names) {
  // Prefer Gemini 1.5 (multimodal), then flash variants, then anything with vision/pro.
  return names
    .filter(n => n.startsWith("models/"))              // ignore tunedModels, etc.
    .filter(n => !n.includes("experimental"))          // skip experimental
    .sort((a, b) => score(b) - score(a));

  function score(n) {
    let s = 0;
    if (n.includes("1.5")) s += 10;
    if (n.includes("flash")) s += 8;
    if (n.includes("pro-vision")) s += 7;
    if (n.includes("pro")) s += 6;
    if (n.includes("vision")) s += 5;
    if (n.includes("latest")) s += 2;
    return s;
  }
}

async function tryGenerateForModels(imageDataUrl, key, models, mimeType) {
  const base64 = imageDataUrl.split(",")[1];
  const body = {
    contents: [{
      parts: [
        { text: "Describe this image briefly in one sentence focusing on the main gesture or symbol." },
        { inline_data: { mime_type: mimeType || "image/png", data: base64 } }
      ]
    }]
  };
  let lastErr = "";
  for (const model of models) {
    const endpoint = "https://generativelanguage.googleapis.com/v1/" + model + ":generateContent?key=" + encodeURIComponent(key);
    try {
      const r = await fetch(endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body)});
      if (!r.ok) { lastErr = await r.text().catch(()=>String(r.status)); continue; }
      const j = await r.json();
      const text = j?.candidates?.[0]?.content?.parts?.map(p=>p.text).join(" ").trim();
      if (text) return text;
      lastErr = "Empty response from " + model;
    } catch (e) {
      lastErr = String(e?.message || e);
    }
  }
  throw new Error("All discovered models failed. Last error: " + lastErr);
}

export async function describeImageWithGemini(imageDataUrl, apiKey, mimeType = "image/png") {
  if (!apiKey) throw new Error("No API key provided");

  const models = await listModels(apiKey);
  if (!models.length) throw new Error("No models returned for this key. Ensure Generative Language API is enabled and T&Cs accepted in AI Studio.");

  const ranked = rankModels(models);
  if (!ranked.length) throw new Error("No usable model names returned (models/*).");

  return await tryGenerateForModels(imageDataUrl, apiKey, ranked, mimeType);
}

// --- Key storage (local only) ---
const KEY = "makaton_demo_gemini_key";
export function saveApiKey(k) { localStorage.setItem(KEY, k || ""); }
export function loadApiKey() { return localStorage.getItem(KEY) || ""; }
```

Remarque : Ce système de tentative est essentiel car de nombreux utilisateurs rencontrent des erreurs de modèle 404 en raison de l'indisponibilité de certaines versions de Gemini dans chaque compte.

### 5\. La logique principale (app.js)

Ce script lie tout ensemble : téléchargement de fichier, appel à l'IA, mapping de signification et affichage des résultats.

```javascript

import { mapDescriptionToMeaning } from './lib/mapping.js';
import { checkAvailability, createNanoTextSession, describeImageWithGemini, saveApiKey, loadApiKey } from './lib/ai.js';

document.addEventListener('DOMContentLoaded', () => {
  console.log('[Makaton] DOM ready');

  const $ = (s) => document.querySelector(s);

  // Elements
  const fileInput   = $('#file');
  const preview     = $('#preview');
  const meaningEl   = $('#meaning');
  const outputEl    = $('#output');
  const btnDescribe = $('#btnDescribe');
  const btnType     = $('#btnType');
  const typedBox    = $('#typedBox');
  const typed       = $('#typed');
  const btnUseTyped = $('#btnUseTyped');
  const btnSpeak    = $('#btnSpeak');
  const btnCopy     = $('#btnCopy');
  const statusEl    = $('#status');

  const settings        = $('#settings');
  const btnSettings     = $('#btnSettings');
  const btnCloseSettings= $('#btnCloseSettings');
  const btnSaveKey      = $('#btnSaveKey');
  const apiKeyInput     = $('#apiKey');
  const apiStatus       = $('#apiStatus');

  let currentImageDataUrl = null;
  let currentImageMime    = "image/png";

  // Sanity logs
  console.log('[Makaton] Elements:', {
    fileInput: !!fileInput, preview: !!preview, outputEl: !!outputEl,
    meaningEl: !!meaningEl, btnDescribe: !!btnDescribe, statusEl: !!statusEl
  });

  // Init API key
  if (apiKeyInput) apiKeyInput.value = loadApiKey() || "";

  // --- Helpers ---
  function setStatus(text) {
    if (statusEl) statusEl.textContent = text || '';
    console.log('[Makaton][Status]', text);
  }
  function clearOutputs() {
    if (outputEl) outputEl.textContent = '';
    if (meaningEl) meaningEl.textContent = '';
    if (btnSpeak) btnSpeak.disabled = true;
    if (btnCopy)  btnCopy.disabled  = true;
  }
  function setOutput(desc) {
    if (outputEl) outputEl.textContent = desc || '';
    const meaning = mapDescriptionToMeaning(desc || '');
    if (meaningEl) meaningEl.textContent = meaning;
    if (btnSpeak) btnSpeak.disabled = !meaning || meaning.includes('No direct mapping');
    if (btnCopy)  btnCopy.disabled  = !meaning;
    setStatus('Done.');
  }
  function fileToDataURL(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload  = () => resolve(reader.result);
      reader.onerror = (e) => reject(e);
      reader.readAsDataURL(file);
    });
  }
  function handleFiles(files) {
    const file = files?.[0];
    if (!file) { setStatus('No file selected.'); return; }
    currentImageMime = file.type || "image/png";
    fileToDataURL(file)
      .then((dataUrl) => {
        currentImageDataUrl = dataUrl;
        if (preview) {
          preview.innerHTML = `<img alt="preview" src="${dataUrl}" />`;
          preview.classList.remove('hidden');
        }
        setStatus('Image loaded. Click "Describe" to continue.');
      })
      .catch((err) => {
        console.error('[Makaton] fileToDataURL error', err);
        setStatus('Could not read the image.');
      });
  }

  // --- File input change ---
  if (fileInput) {
    fileInput.addEventListener('change', (e) => {
      console.log('[Makaton] file input change');
      handleFiles(e.target.files);
    });
  } else {
    console.warn('[Makaton] #file input not found in DOM.');
  }

  // --- Drag & drop support on preview area ---
  if (preview) {
    preview.addEventListener('dragover', (e) => { e.preventDefault(); preview.classList.add('drag'); });
    preview.addEventListener('dragleave', () => preview.classList.remove('drag'));
    preview.addEventListener('drop', (e) => {
      e.preventDefault();
      preview.classList.remove('drag');
      console.log('[Makaton] drop');
      handleFiles(e.dataTransfer?.files);
    });
  }

  // --- Describe click ---
  if (btnDescribe) {
    btnDescribe.addEventListener('click', async () => {
      console.log('[Makaton] Describe clicked');
      if (!currentImageDataUrl) { setStatus('Please upload an image first.'); return; }
      clearOutputs();
      setStatus('Checking on-device AI availability…');

      const avail = await checkAvailability().catch(() => ({ nanoTextPossible: false }));
      try {
        const apiKey = loadApiKey();
        if (apiKey) {
          setStatus('Using Gemini cloud for image description…');
          const desc = await describeImageWithGemini(currentImageDataUrl, apiKey, currentImageMime);
          setOutput(desc);
          return;
        }
        if (avail.nanoTextPossible) {
          setStatus('No API key found. Using on-device AI (text) for best guess…');
          const session = await createNanoTextSession();
          const desc = await session.prompt('Given an image is uploaded by the user (not directly visible to you), infer a likely one-sentence description of a common Makaton sign or symbol a teacher might upload. Keep it generic and safe.');
          setOutput(desc);
          return;
        }
        setStatus('No AI available. Please type a brief description.');
        if (typedBox) typedBox.classList.remove('hidden');
      } catch (err) {
        console.error('[Makaton] Describe error', err);
        setStatus('Description failed: ' + (err?.message || err));
        if (typedBox) typedBox.classList.remove('hidden');
      }
    });
  } else {
    console.warn('[Makaton] Describe button not found.');
  }

  // --- Manual typing flow ---
  if (btnType) {
    btnType.addEventListener('click', () => {
      if (typedBox) typedBox.classList.remove('hidden');
      if (typed) typed.focus();
    });
  }
  if (btnUseTyped) {
    btnUseTyped.addEventListener('click', () => {
      const text = (typed?.value || '').trim();
      if (!text) { setStatus('Type a description first.'); return; }
      setOutput(text);
    });
  }

  // --- Utilities ---
  if (btnSpeak) {
    btnSpeak.addEventListener('click', () => {
      const text = meaningEl?.textContent?.trim();
      if (!text) return;
      const u = new SpeechSynthesisUtterance(text);
      speechSynthesis.cancel();
      speechSynthesis.speak(u);
    });
  }
  if (btnCopy) {
    btnCopy.addEventListener('click', async () => {
      const text = meaningEl?.textContent?.trim();
      if (!text) return;
      try {
        await navigator.clipboard.writeText(text);
        setStatus('Copied meaning to clipboard.');
      } catch {
        setStatus('Copy failed.');
      }
    });
  }

  // --- Settings modal ---
  if (btnSettings && settings) btnSettings.addEventListener('click', () => settings.showModal());
  if (btnCloseSettings && settings) btnCloseSettings.addEventListener('click', () => settings.close());
  if (btnSaveKey) {
    btnSaveKey.addEventListener('click', (e) => {
      e.preventDefault();
      const k = apiKeyInput?.value?.trim() || "";
      saveApiKey(k);
      if (apiStatus) apiStatus.textContent = k ? "API key saved locally. Try Describe again." : "Cleared API key. You can still use on-device or typed mode.";
    });
  }

  // First status
  setStatus('Ready. Upload an image to begin.');
});
```

Décomposons les sections principales du script `app.js` pour le compagnon IA Makaton, car il s'y passe beaucoup de choses :

1. **Importations et configuration initiale :**
    
    * Le script importe des fonctions de `mapping.js` et `ai.js` pour gérer le mapping des descriptions aux significations et les interactions avec l'IA.
        
    * Il configure des écouteurs d'événements pour le moment où le contenu du DOM est entièrement chargé, garantissant que tous les éléments sont prêts pour l'interaction.
        
2. **Sélection des éléments :**
    
    * Il utilise une fonction utilitaire `$` pour sélectionner les éléments du DOM par leurs sélecteurs CSS. Cela inclut les entrées de fichiers, les boutons et les zones d'affichage pour les aperçus d'images et les résultats.
        
3. **Sanity logs :**
    
    * Il enregistre la présence des éléments clés dans la console à des fins de débogage, s'assurant que tous les éléments nécessaires sont trouvés dans le DOM.
        
4. **Initialisation de la clé API :**
    
    * Il charge toute clé API enregistrée depuis le stockage local et la définit dans le champ de saisie pour le confort de l'utilisateur.
        
5. **Fonctions utilitaires :**
    
    * `setStatus` : Met à jour le message de statut affiché à l'utilisateur.
        
    * `clearOutputs` : Efface les zones d'affichage des résultats et des significations et désactive les boutons pour parler et copier.
        
    * `setOutput` : Affiche la description générée par l'IA et la mappe à une signification Makaton, en activant les boutons si une signification valide est trouvée.
        
    * `fileToDataURL` : Convertit un fichier téléchargé en une Data URL pour l'aperçu et le traitement de l'image.
        
    * `handleFiles` : Gère la sélection de fichiers, la mise à jour de l'aperçu et la définition de la Data URL de l'image actuelle.
        
6. **Gestion du changement d'entrée de fichier :**
    
    * Il écoute les changements dans l'entrée de fichier, traite le fichier sélectionné et met à jour la zone d'aperçu.
        
7. **Support du Drag & Drop :**
    
    * Il ajoute une fonctionnalité de glisser-déposer à la zone d'aperçu, permettant aux utilisateurs de faire glisser des fichiers directement sur l'application pour traitement.
        
8. **Clic sur le bouton Describe :**
    
    * Il gère l'événement de clic sur le bouton "Describe", vérifiant la présence d'une image téléchargée et tentant de la décrire à l'aide de l'API Gemini ou de l'IA sur l'appareil.
        
    * Si aucune IA n'est disponible, il invite l'utilisateur à saisir manuellement une description.
        
9. **Flux de saisie manuelle :**
    
    * Il permet aux utilisateurs de saisir manuellement une description si le traitement par l'IA est indisponible ou échoue, mettant à jour le résultat avec le texte saisi.
        
10. **Utilitaires :**
    
    * `btnSpeak` : Utilise l'API SpeechSynthesis du navigateur pour lire à haute voix la signification mappée.
        
    * `btnCopy` : Copie la signification mappée dans le presse-papiers pour un partage facile.
        
11. **Modal de paramètres :**
    
    * Il gère le modal de paramètres pour saisir et enregistrer la clé API, fournissant un retour sur le statut de la clé.
        
12. **Statut initial :**
    
    * Il définit le message de statut initial pour guider l'utilisateur à télécharger une image pour commencer le processus.
        

Ce script lie efficacement l'interface utilisateur, la gestion des fichiers, le traitement de l'IA et l'affichage des résultats, offrant une expérience fluide pour traduire les signes Makaton en significations anglaises.

#### Comment la vision et le langage collaborent ici

En travaillant sur ce projet, j'ai commencé à apprécier comment la vision par ordinateur et la compréhension du langage se complètent dans des systèmes multimodaux comme celui-ci.

* Le modèle de vision (Gemini ou Nano) interprète *ce qu'il voit* comme les formes de mains, les gestes ou la disposition et transforme ce contexte visuel en langage descriptif.
    
* La logique de mapping du langage interprète ensuite ces mots, déduit l'intention et trouve la correspondance sémantique la plus proche (par exemple, « help », « friend », « eat »).
    
* C'est une collaboration entre deux formes de compréhension (*perceptive* et *sémantique*) qui permettent ensemble à l'IA de combler le fossé entre le geste et la signification.
    

Cette prise de conscience a remodelé ma façon de penser l'accessibilité : les meilleures technologies d'assistance émergent souvent non pas de modèles plus intelligents seuls, mais de l'interaction entre des modalités comme voir, décrire et raisonner en contexte.

### 6\. Optionnel — Parler et Copier

Pour rendre l'application plus accessible, j'ai ajouté une sortie vocale et un bouton de copie rapide :

```javascript
btnSpeak.addEventListener('click', () => {
  const text = meaningEl.textContent.trim();
  if (text) speechSynthesis.speak(new SpeechSynthesisUtterance(text));
});

btnCopy.addEventListener('click', async () => {
  const text = meaningEl.textContent.trim();
  if (text) await navigator.clipboard.writeText(text);
});
```

Cela donne aux utilisateurs un retour à la fois visuel et auditif, particulièrement utile pour les apprenants ou les éducateurs.

## Comment résoudre les problèmes courants

Aucun projet d'IA ou d'intégration web ne se déroule sans accroc la première fois – et c'est normal. Voici une analyse des principaux problèmes auxquels j'ai été confronté lors de la construction du compagnon IA Makaton, comment je les ai diagnostiqués et comment j'ai résolu chacun d'eux.

Ces leçons aideront quiconque tente d'intégrer les API Gemini, l'IA sur l'appareil ou des applications web locales sans backend complet.

### 1\. L'erreur “CORS” lors de l'exécution avec `file://`

Lorsque j'ai ouvert mon `index.html` directement depuis mon explorateur de fichiers, Chrome a renvoyé plusieurs erreurs de politique CORS :

```python
Access to script at 'file:///lib/ai.js' from origin 'null' has been blocked by CORS policy.
```

Au début, cela semblait déroutant, mais la raison est simple : les navigateurs modernes bloquent les modules JavaScript (`import/export`) lors de l'exécution à partir de chemins `file://` pour des raisons de sécurité.

✅ **Solution :** J'ai réalisé que je devais servir les fichiers via **HTTP**, et non depuis le système de fichiers. J'ai donc lancé un serveur web local rapide à l'aide de Python :

```python
python -m http.server 8080
```

Puis j'ai ouvert :

```python
http://localhost:8080/index.html
```

Cette seule étape a corrigé toutes les erreurs CORS et a permis à mes modules de se charger correctement.

### 2\. “Model Not Found” (404) de l'API Gemini

Le défi suivant est venu de l'API Gemini. Même si j'avais une clé API valide, ma console affichait cette erreur :

```python
"models/gemini-1.5-flash" is not found for API version v1beta, or is not supported for generateContent.
```

Il s'avère que les endpoints d'API de Google peuvent varier légèrement en fonction de la configuration de votre projet et des autorisations de votre clé.

✅ **Solution :** J'ai réécrit mon script `lib/ai.js` pour essayer automatiquement **plusieurs endpoints de modèle Gemini** jusqu'à ce qu'il en trouve un qui fonctionne. Quelque chose comme ceci :

```python
const GEMINI_IMAGE_ENDPOINTS = [
  "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent",
  "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent",
  "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash-latest:generateContent",
];
```

Et je l'ai enveloppé dans une boucle qui s'arrête dès qu'un endpoint réussit.

Plus tard, je l'ai encore amélioré en listant dynamiquement les modèles disponibles à l'aide de  
`https://generativelanguage.googleapis.com/v1/models?key=VOTRE_CLE` et en essayant automatiquement ceux qui supportent la génération d'images.

Cette approche de découverte dynamique a corrigé les erreurs 404 de manière permanente.

### **3\. Empaqueter une version locale à fichier unique**

Une fois que tout a fonctionné, je voulais une version que d'autres pourraient tester facilement sans installer Node.js ou exécuter des outils de build.

✅ **Solution :** J'ai regroupé le projet dans un simple fichier zip contenant :

```python
index.html
app.js
lib/ai.js
lib/mapping.js
styles.css
```

De cette façon, n'importe qui peut simplement dézipper et exécuter :

```python
python -m http.server 8080
```

et ouvrir `localhost:8080`.

Tout s'exécute localement dans le navigateur, aucun code côté serveur n'est requis. Cela le rend également parfait pour les démos, les salles de classe, etc.

### 4\. Débogage des erreurs d'importation de script dans la console

Un autre problème subtil est apparu lorsque j'ai remarqué ce message rouge :

```python
The requested module './lib/mapping.js' does not provide an export named 'mapDescriptionToMeaning'
```

Cette ligne m'a dit exactement ce qui n'allait pas : mes noms de fonctions d'importation et d'exportation ne correspondaient pas. La correction a été simple :

```python
// app.js
import { mapDescriptionToMeaning } from './lib/mapping.js';
```

Et ensuite s'assurer que le fichier de mapping l'exportait :

```python
// mapping.js
export function mapDescriptionToMeaning(desc) { ... }
```

Après cela, toutes les pièces se sont connectées sans problème.

L'utilisation de la console du navigateur **comme tableau de bord de débogage** s'est avérée être l'outil le plus puissant de tous. Chaque correction a commencé par la lecture et le raisonnement sur ces lignes d'erreur rouges.

## Démo : Le compagnon IA Makaton en action

Voyons le compagnon IA Makaton en action et comprenons ce qui se passe sous le capot.

### Étape 1 : Exécuter l'application localement

Une fois que vous avez téléchargé ou cloné le dossier du projet, ouvrez votre terminal dans ce répertoire et démarrez un serveur de développement local : `python -m http.server 8080`. Ouvrez ensuite votre navigateur et visitez : `http://localhost:8080/index.html`

Vous devriez voir l'interface du compagnon IA Makaton :

![Interface principale de l'application compagnon IA Makaton](https://github.com/tayo4christ/makaton-ai-companion/blob/9cc834fa75f6dcd39866c538ed42255f9006bb51/assets/app-interface.jpg?raw=true align="left")

### Étape 2 : Obtenir votre clé API Gemini

Pour activer la description d'image basée sur le cloud, vous aurez besoin d'une [**clé API Gemini**](https://aistudio.google.com/welcome?utm_source=PMAX&utm_medium=display&utm_campaign=FY25-global-DR-pmax-1710442&utm_content=pmax&gclsrc=aw.ds&gad_source=1&gad_campaignid=21521981511&gbraid=0AAAAACn9t66nbeHlpP_VYvpWIrX7IJGEW&gclid=EAIaIQobChMIqf-KiIHbkAMV1ZFQBh0KHA8wEAAYASAAEgKLA_D_BwE) de Google AI Studio.

**Voici comment en générer une :**

1. Visitez : `https://aistudio.google.com/welcome`
    
2. Cliquez sur **“Create API key”** et liez-la à votre projet Google Cloud (ou créez-en un nouveau).
    
3. Copiez la clé, elle ressemblera à ceci : `AIzaSyA...XXXXXXXXXXXX`
    
4. Ouvrez le compagnon IA Makaton dans votre navigateur et cliquez sur le bouton **Settings** (en haut à gauche).
    
5. Collez votre clé dans la zone de saisie et cliquez sur **Save**.
    

![Configuration de la clé API OpenAI dans l'interface de l'application](https://github.com/tayo4christ/makaton-ai-companion/blob/9cc834fa75f6dcd39866c538ed42255f9006bb51/assets/api-key-setting.jpg?raw=true align="left")

Vous verrez un message de confirmation comme celui-ci :

> *“API key saved locally. Try Describe again.”*

Cela signifie que votre clé est stockée en toute sécurité dans le localStorage et n'est accessible que depuis votre navigateur.

### Étape 3 : Activer Gemini Nano pour l'IA sur l'appareil

Si vous utilisez [**Chrome Canary**,](https://www.google.com/intl/en_uk/chrome/canary/) vous pouvez exécuter Gemini Nano localement sans accès à Internet. Cela permet au compagnon IA Makaton de générer du texte même lorsque la clé API n'est pas définie.

#### Télécharger et installer Chrome Canary :

Visitez la page de téléchargement officielle de Chrome Canary et installez-le sur votre système Windows ou macOS. Chrome Canary est une version spéciale de Chrome conçue pour les développeurs et les premiers adoptants, offrant les dernières fonctionnalités et mises à jour.

#### Activer Gemini Nano :

Ouvrez Chrome Canary et tapez `chrome://flags/#prompt-api-for-gemini-nano` dans la barre d'adresse.

Localisez le flag "Prompt API for Gemini Nano" dans la liste. Réglez ce flag sur **Enabled**. Cette action permet à Chrome Canary de prendre en charge le modèle Gemini Nano pour le traitement de l'IA sur l'appareil.

Après avoir activé le flag, relancez Chrome Canary pour appliquer les modifications.

#### Télécharger le modèle Gemini Nano :

Ouvrez un nouvel onglet dans Chrome Canary et entrez `chrome://components` dans la barre d'adresse.

Faites défiler vers le bas pour trouver le composant **“Optimization Guide”**. Cliquez sur **Check for update**. Cette action lancera le téléchargement du modèle Gemini Nano, nécessaire pour exécuter des tâches d'IA localement sans connexion Internet.

#### Vérifier l'installation :

Une fois le modèle Gemini Nano installé, l'application compagnon IA Makaton le détectera automatiquement. Vous devriez voir un message indiquant que l'application utilise l'IA sur l'appareil : *“No API key found. Using on-device AI (text) for best guess…”*

Cette confirmation signifie que l'application peut désormais générer des descriptions textuelles à l'aide du modèle Gemini Nano sans avoir besoin d'une clé API ou d'un accès Internet.

En suivant ces étapes détaillées, vous vous assurez que le modèle Gemini Nano est correctement configuré et prêt à être utilisé pour le traitement de l'IA sur l'appareil dans le compagnon IA Makaton.

### Étape 4 : Télécharger un signe ou un symbole Makaton

Cliquez sur **Choose File** pour télécharger n'importe quelle image Makaton (par exemple, le signe « help »), puis appuyez sur **Describe (Cloud or Nano)**. Vous verrez immédiatement des logs de console confirmant que l'application fonctionne correctement et se connecte à l'API Gemini :

![Sortie de la console montrant les logs de traduction en temps réel](https://github.com/tayo4christ/makaton-ai-companion/blob/9cc834fa75f6dcd39866c538ed42255f9006bb51/assets/console.jpg?raw=true align="left")

### Étape 5 : Description par l'IA et mapping

Voici ce qui se passe ensuite :

1. L'image est lue et encodée en Base64.
    
2. L'API Gemini (cloud ou sur l'appareil) génère une courte description visuelle.
    
3. La description est transmise à la fonction `mapDescriptionToMeaning()`.
    
4. Si les mots-clés correspondent à une entrée dans le dictionnaire `MAKATON_GLOSSES`, l'application affiche la signification anglaise correspondante.
    
5. Enfin, les utilisateurs peuvent cliquer sur **Speak** ou **Copy** pour entendre ou réutiliser la traduction.
    

Exemples de résultats :

**Lorsqu'aucun mapping n'est trouvé :**  
La description de l'IA est précise mais ne correspond pas encore à un mot-clé Makaton connu.

![Démonstration incorrecte montrant le modèle interprétant mal un signe](https://github.com/tayo4christ/makaton-ai-companion/blob/9cc834fa75f6dcd39866c538ed42255f9006bb51/assets/Incorrect-demonstration.jpg?raw=true align="left")

**Après la mise à jour de la liste de mapping :**  
L'ajout de nouveaux mots-clés comme `"help"`, `"assist"` ou `"hand over hand"` permet une traduction correcte.

![Démonstration correcte où l'IA reconnaît avec précision le signe Makaton](https://github.com/tayo4christ/makaton-ai-companion/blob/9cc834fa75f6dcd39866c538ed42255f9006bb51/assets/correct-demonstration.jpg?raw=true align="left")

### Pourquoi c'est important

Cela démontre comment des outils accessibles, assistés par l'IA, peuvent soutenir la communication pour les personnes qui dépendent du Makaton. Même lorsqu'un geste n'est pas reconnu, le système fournit une sortie structurée et permet aux utilisateurs ou aux éducateurs d'élargir la liste de mapping, rendant l'outil plus intelligent au fil du temps.

## Réflexions plus larges

La construction de ce projet s'est avérée être bien plus qu'un simple exercice de codage pour moi.  
C'était une expérience significative combinant l'accessibilité, le traitement du langage naturel (NLP) et la vision par ordinateur. Ces trois domaines, lorsqu'ils sont réunis, peuvent créer un véritable impact social.

En y travaillant, j'ai commencé à comprendre comment la vision par ordinateur et la compréhension du langage se complètent en pratique. Le modèle de vision perçoit le monde en identifiant des formes, des gestes et des motifs spatiaux, tandis que le modèle de langage interprète ce que ces visuels signifient en termes humains.  
Dans ce projet, le système d'intelligence artificielle voit d'abord le signe Makaton, puis le décrit, et enfin le mappe à un mot anglais qui porte une intention et une signification.

Cette interaction entre perception et sémantique est ce qui rend l'intelligence artificielle multimodale si puissante. Il ne s'agit pas seulement de reconnaître une image ou de générer du texte ; il s'agit de construire des systèmes qui connectent la compréhension à travers différentes formes d'information pour rendre la technologie plus inclusive et centrée sur l'humain.

Cette prise de conscience a changé ma façon de concevoir la technologie d'accessibilité. La véritable innovation ne passe pas seulement par des modèles plus intelligents, mais par l'harmonie entre voir et comprendre, entre ce qu'un système d'intelligence artificielle observe et comment il communique cette observation pour aider les gens.

### L'accessibilité rencontre l'IA

Travailler sur ce projet m'a rappelé que l'accessibilité n'est pas seulement une question de conformité ou de dispositifs d'assistance. C'est aussi une question d'inclusion. Un système d'IA simple capable de décrire un geste de la main ou un symbole en temps réel peut autonomiser les enseignants, les parents et les élèves qui communiquent à l'aide du Makaton ou de systèmes similaires.

En mappant les descriptions générées par l'IA à des phrases significatives, l'application démontre comment l'IA peut soutenir l'éducation inclusive, même à petite échelle. Elle comble le fossé de communication entre les apprenants verbaux et non verbaux, ce que les systèmes de traduction traditionnels négligent souvent.

### Intégration du NLP et de la vision par ordinateur

Sur le plan technique, ce projet m'a montré à quel point la vision par ordinateur et la compréhension du langage se complètent naturellement. Les modèles multimodaux de l'API Gemini ont pu analyser une image et produire des phrases cohérentes en langage naturel, ce que les anciennes API ne pouvaient pas faire sans enchaîner plusieurs outils.

En injectant ce résultat dans une fonction de mapping NLP légère, j'ai pu simuler un traducteur de symbole en langage à un stade très précoce, ce qui est au cœur de mon intérêt de recherche plus large pour la traduction automatique du Makaton vers l'anglais.

### Pourquoi l'IA locale (Gemini Nano) est importante

Bien que les modèles cloud soient puissants, l'expérimentation de Gemini Nano a révélé quelque chose de passionnant :  
l'IA sur l'appareil peut rendre les outils d'accessibilité plus rapides, plus sûrs et plus privés.

Dans les salles de classe ou les séances de thérapie, on ne peut souvent pas compter sur des connexions Internet stables ou partager des données sensibles sur les élèves. L'exécution de l'inférence localement signifie que les gestes ou les images de symboles des apprenants ne quittent jamais l'appareil, une étape cruciale vers une IA d'accessibilité préservant la confidentialité.

Et comme Nano s'exécute directement dans Chrome Canary, cela montre comment l'IA s'intègre au niveau du navigateur, abaissant les barrières pour les enseignants et les développeurs afin de construire des solutions inclusives sans avoir besoin d'une infrastructure massive.

### Perspectives d'avenir

Ce prototype n'est qu'un point de départ. Les futures itérations pourraient intégrer la reconnaissance des gestes directement à partir de l'entrée de la caméra, prendre en charge plusieurs ensembles de symboles, ou même apprendre des retours des utilisateurs pour enrichir automatiquement le dictionnaire.

Plus important encore, cela renforce une conviction centrale dans mon parcours de recherche et d'enseignement :

**L'innovation en matière d'accessibilité ne nécessite pas de systèmes massifs. Elle commence par la curiosité, l'empathie et quelques lignes de code ciblées.**

## Conclusion

La construction du compagnon IA Makaton a été l'un des projets les plus gratifiants de mon parcours dans l'IA – pas seulement parce qu'il a fonctionné, mais parce qu'il a prouvé à quel point l'innovation peut être accessible.

Avec juste un navigateur, quelques lignes de JavaScript et la bonne API, j'ai pu combiner la vision par ordinateur, la compréhension du langage et la conception de l'accessibilité dans un système fonctionnel qui traduit les symboles en significations. C'est un petit pas vers un avenir où n'importe qui, indépendamment de ses capacités d'élocution ou de langage, peut être compris grâce à la technologie.

Le projet a également renforcé quelque chose de profondément personnel pour moi en tant que chercheur et éducateur : l'IA pour l'accessibilité n'a pas besoin d'être complexe, coûteuse ou centralisée. Elle peut être légère, ouverte et construite avec empathie par quiconque est prêt à apprendre et à expérimenter.

### Rejoignez la conversation

Si ce projet vous inspire, j'aimerais voir vos propres expériences et améliorations. Pouvez-vous le rendre compatible avec les gestes en direct via webcam ? Pourriez-vous l'adapter à d'autres systèmes de symboles, comme le PECS ou la BSL ?

Partagez vos idées dans les commentaires ou taguez-moi si vous publiez votre propre version. Ensemble, nous pouvons transformer un petit prototype en un outil d'accessibilité piloté par la communauté et continuer à explorer comment l'IA peut donner une voix à plus de personnes.

Code source complet sur GitHub : [Makaton-ai-companion](https://github.com/tayo4christ/makaton-ai-companion)