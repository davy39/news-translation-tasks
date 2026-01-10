---
title: Comment créer une extension Chrome de générateur de conseils avec Manifest
  V3
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2025-08-25T20:19:19.961Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-advice-generator-chrome-extension-with-manifest-v3
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756152220137/8717b809-1186-4a15-92f8-ea926177ef76.png
tags:
- name: Web Development
  slug: web-development
- name: JavaScript
  slug: javascript
- name: chrome extension
  slug: chrome-extension
seo_title: Comment créer une extension Chrome de générateur de conseils avec Manifest
  V3
seo_desc: 'In 2025, using Chrome without extensions is like using a smartphone without
  apps. It’s possible, but you’re missing out on a lot.

  And despite how essential extensions are, creating one is very simple – it’s just
  HTML, CSS, and JavaScript with browser...'
---

En 2025, utiliser Chrome sans extensions, c'est comme utiliser un smartphone sans applications. C'est possible, mais vous passez à côté de beaucoup de choses.

Et malgré l'aspect essentiel des extensions, en créer une est très simple : il s'agit simplement de HTML, CSS et JavaScript avec des API de navigateur.

Dans ce tutoriel, nous allons découvrir les extensions Chrome en construisant une extension de générateur de conseils avec Manifest V3 (MV3), l'architecture la plus récente et la plus sécurisée pour les extensions Chrome. Vous pouvez passer directement à [ce que nous allons construire ici](#heading-ce-que-nous-allons-construire).

### Table des matières

* [Quels sont les composants clés d'une extension Chrome ?](#heading-quels-sont-les-composants-cles-d-une-extension-chrome)
    
* [Comment créer une extension Chrome de générateur de conseils](#heading-comment-creer-une-extension-chrome-de-generateur-de-conseils)
    
* [Les avantages de Manifest V3](#heading-les-avantages-de-manifest-v3)
    
* [Comment déboguer votre extension Chrome](#heading-comment-deboguer-votre-extension-chrome)
    
* [Conclusion](#heading-conclusion)
    

## Quels sont les composants clés d'une extension Chrome ?

Les extensions Chrome sont des outils incroyablement puissants qui peuvent ajouter des fonctionnalités personnalisées directement dans votre expérience de navigation pour transformer la façon dont vous utilisez le Web.

Avant d'écrire du code, comprenons certains composants clés :

* Chaque extension commence par un fichier **manifest**. Ce fichier JSON indique à Chrome tout ce qu'il doit savoir sur une extension : nom, version, autorisations et fichiers.
    
* L'**interface utilisateur** est construite avec HTML, CSS et JavaScript. Il s'agit essentiellement d'une mini-page Web qui vit à l'intérieur de votre navigateur.
    
* Enfin, il y a le **service worker** qui s'exécute en arrière-plan et récupère des données à partir d'API externes. Dans Manifest V3, les service workers ont remplacé les pages d'arrière-plan (background pages).
    

## Comment créer une extension Chrome de générateur de conseils

<span id="heading-ce-que-nous-allons-construire">Voici un aperçu de ce que nous allons construire :</span>

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1755718930961/381f422d-f83c-49a9-a007-051ddea6e8da.png align="center")

Ce design est réalisé par [Frontend Mentor](https://www.frontendmentor.io/?via=ophyboamah).

**Prérequis :**

Pour suivre ce tutoriel, vous avez besoin de :

* Une compréhension de base du HTML, du CSS et du JavaScript.
    
* Un navigateur Chrome.
    
* Un éditeur de texte.
    

Lors de la structuration d'un projet d'extension, le seul prérequis est de placer le fichier `manifest.json` dans le répertoire racine de l'extension.

### **Tester votre extension Chrome (Charger l'extension décompressée)**

Avant de commencer la construction, vous voudrez voir vos progrès après chaque fichier pour détecter tout problème rapidement. Voici comment charger votre extension dans Chrome pour la tester :

1. Allez sur `chrome://extensions` pour ouvrir la page des extensions Chrome.
    
2. Dans le coin supérieur droit de la page des extensions, activez le **Mode développeur**.
    
3. Cliquez sur le bouton **Charger l'extension décompressée** qui apparaît.
    
4. Dans la boîte de dialogue, allez dans le **dossier racine de l'extension** et cliquez sur **Sélectionner le dossier**.
    

Votre extension devrait apparaître. Si son icône n'apparaît pas immédiatement dans la barre d'outils de votre navigateur, cliquez sur l'icône **puzzle** dans votre barre d'outils et épinglez-la.

![Une capture d'écran montrant comment épingler une extension Chrome depuis la barre d'outils d'un navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1755711497449/6c3f056c-322d-45a2-b1b3-15a62b7fad44.png align="center")

Commençons maintenant par définir l'identité de notre extension dans le fichier `manifest.json`.

### Les avantages de Manifest V3

Le fichier `manifest.json` est le cœur d'une extension Chrome. Écrit en JSON (JavaScript Object Notation), il fournit à Chrome tout ce dont il a besoin pour connaître votre extension.

Considérez-le comme un passeport avec des visas et Chrome comme l'officier d'immigration vérifiant l'identité et l'accès.

![Une image illustrant l'analogie du fichier Manifest comme un passeport et un visa et Chrome comme l'officier d'immigration qui assure les bonnes autorisations.](https://cdn.hashnode.com/res/hashnode/image/upload/v1755715844005/b1742fbf-fafa-4c36-b08c-1637d00d625d.png align="center")

Manifest V3 (MV3) apporte de meilleures performances, une sécurité accrue et une plus grande fiabilité aux extensions. MV3 utilise des service workers qui ne s'activent qu'au besoin, ce qui améliore la durée de vie de la batterie et empêche les extensions de ralentir votre navigateur.

Détaillons chaque champ important :

* `manifest_version` est la ligne la plus critique. Donnez-lui la valeur 3 pour indiquer à Chrome que vous utilisez Manifest V3.
    
* `name`**,** `version`**,** `description` définissent l'identité de base de votre extension.
    
* `action` est un champ Manifest V3 qui contrôle ce qui se passe quand quelqu'un clique sur le `default_icon` de votre extension dans la barre d'outils. Le `default_popup` pointe vers votre fichier HTML, de sorte que cliquer sur l'icône ouvre cette page dans une petite fenêtre contextuelle.
    
* `permissions` indique à Chrome ce à quoi votre extension a besoin d'accéder. Nous utilisons l'autorisation d'hôte [https://api.adviceslip.com/\\*](https://api.adviceslip.com/) pour que notre extension puisse récupérer des conseils de cette API. Sans cela, l'extension serait empêchée de faire ces requêtes. Cela peut sembler excessivement prudent, mais c'est une mesure de sécurité qui protège les utilisateurs.
    
* `background` pointe vers votre script de service worker. Le champ `service_worker` indique à Chrome que `service-worker.js` doit s'exécuter en arrière-plan.
    

### Étape 1 : Créer un fichier Manifest V3

En suivant les explications des différentes parties du fichier ci-dessus, voici à quoi ressemblerait notre fichier `manifest.json` :

```json
{
  "name": "Générateur de conseils",
  "description": "Obtenez un nouveau conseil chaque fois que vous en avez besoin !",
  "version": "1.0",
  "manifest_version": 3,
  "action": {
    "default_popup": "index.html",
    "default_icon": "/icons/icon-dice.png"
  },
  "permissions": [
    "activeTab"
  ],
  "host_permissions": [
    "https://api.adviceslip.com/*"
  ],
  "background": {
    "service_worker": "service-worker.js"
  }
}
```

Vous pourriez voir `activeTab` dans d'autres exemples d'extensions. Bien que nous n'en ayons pas strictement besoin ici, il est utile de le connaître. Il donne un accès temporaire à l'onglet sur lequel l'utilisateur se trouve, mais seulement lorsqu'il clique sur l'icône de l'extension.

L'image ci-dessous sera le résultat de l'exécution de notre code de manifest ci-dessus :

![Une capture d'écran montrant l'extension Chrome Advice Generator après l'exécution du Manifest.json](https://cdn.hashnode.com/res/hashnode/image/upload/v1755711701772/49fa40e5-1c5b-4cd3-a6f2-a9100db8efcb.png align="center")

### Étape 2 : Créer les pages HTML et CSS

Maintenant que l'identité et les autorisations de notre extension sont définies, passons à la construction de l'interface utilisateur en commençant par une page `index.html`.

```xml
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Générateur de conseils</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;800&display=swap" rel="stylesheet">
</head>
<body>
    <main class="advice-card">
        <h1 class="advice-id">CONSEIL #<span id="advice-id-number"></span></h1>
        <p class="advice-quote" id="advice-quote">
            « Il est facile de s'asseoir et de prêter attention, le plus difficile est de se lever et de passer à l'action. »
        </p>
        <div class="divider">
            <img src="icons/pattern-divider.png" alt="Séparateur">
        </div>
        <button class="dice-button" id="generate-advice-btn">
            <img src="icons/icon-dice.png" alt="Icône de dé">
        </button>
    </main>
    <script src="index.js"></script>
</body>
</html>
```

Maintenant, donnons vie au design avec un fichier `style.css` dans votre répertoire racine. Nous allons configurer les styles généraux du corps, positionner la carte et styliser tous les éléments qu'elle contient.

```css
:root {
    /* Couleurs du guide de style Frontend Mentor */
    --clr-light-cyan: hsl(193, 38%, 86%);
    --clr-neon-green: hsl(150, 100%, 66%);
    --clr-grayish-blue: hsl(217, 19%, 35%);
    --clr-dark-grayish-blue: hsl(217, 19%, 25%);
    --clr-dark-blue: hsl(218, 23%, 16%); 
    /* Typographie */
    --ff-manrope: 'Manrope', sans-serif;
    --fw-regular: 400;
    --fw-bold: 700;
}
body {
    margin: 0;
    padding: 0;
    font-family: var(--ff-manrope);
    background-color: var(--clr-dark-blue);
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    min-width: 30rem;
    box-sizing: border-box;
}
.advice-card {
    background-color: var(--clr-dark-grayish-blue);
    border-radius: 0.5rem;
    padding: 1.5rem 1.5rem;
    width: 60%; 
    text-align: center;
    position: relative;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
    margin-bottom: 70px; 
}
.advice-id {
    color: var(--clr-neon-green);
    font-size: 0.8em;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 20px;
}
.advice-quote {
    color: var(--clr-light-cyan);
    font-size: 1.75em; 
    font-weight: var(--fw-bold);
    line-height: 1.4;
    margin-bottom: 1.2rem;
    padding: 0 15px;
}
.divider {
    margin-bottom: 35px;
}
.divider img {
    max-width: 90%;
    height: auto;
}
.dice-button {
    background-color: var(--clr-neon-green);
    border: none;
    border-radius: 50%;
    width: 2rem;
    height: 2rem;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    position: absolute;
    bottom: -1rem; 
    left: 50%;
    padding: 1rem;
    transform: translateX(-50%);
    transition: box-shadow 0.3s ease-in-out;
}
.dice-button:hover {
    box-shadow: 0 0 40px var(--clr-neon-green);
}
.dice-button img {
    width: 2rem;
    height: 2rem;
}
```

L'image ci-dessous sera le résultat de l'exécution de notre code HTML et CSS ci-dessus plus le manifest initial :

![Une image du design de l'extension Chrome Advice Generator](https://cdn.hashnode.com/res/hashnode/image/upload/v1755711748813/c641535b-5bdf-4adc-a11c-6115b1f1a284.png align="center")

Une fois le HTML et le CSS terminés, l'aspect visuel de notre extension est complet. Ensuite, donnons-lui vie en écrivant le JavaScript qui gère la récupération de nouveaux conseils et la mise à jour de l'affichage.

### Étape 3 : Ajouter un Service Worker

Dans Manifest V3, la logique d'arrière-plan principale d'une extension réside dans son Service Worker. Contrairement aux pages d'arrière-plan persistantes de Manifest V2, les Service Workers de la V3 ne s'exécutent qu'au besoin, par exemple en réponse à un message d'`index.js` ou à un événement du navigateur.

Notre `service-worker.js` aura les rôles suivants :

* Écouter une requête provenant d'`index.js` (quand l'utilisateur clique sur le dé).
    
* Récupérer un nouveau conseil depuis l'API Advice Slip.
    
* Renvoyer ce conseil à `index.js` pour qu'il soit affiché.
    

Créez un fichier nommé `service-worker.js` dans le répertoire racine de votre extension.

```javascript
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "fetchAdvice") {
    fetchAdvice().then(adviceData => {
      sendResponse({ advice: adviceData });
    }).catch(error => {
      console.error("Erreur lors de la récupération du conseil :", error);
      sendResponse({ error: "Impossible de récupérer le conseil" });
    });
    return true;
  }
});

// Fonction pour récupérer le conseil depuis l'API Advice Slip
async function fetchAdvice() {
  try {
    const response = await fetch("https://api.adviceslip.com/advice");
    if (!response.ok) {
      throw new Error(`Erreur HTTP ! statut : ${response.status}`);
    }
    const data = await response.json();
    return data.slip; 
  } catch (error) {
    console.error("Impossible de récupérer le conseil :", error);
    throw error; 
  }
}
```

#### Gestion des messages dans les Service Workers

Comme les Service Workers n'ont pas d'accès direct au DOM de votre page `index.html` (et vice versa), ils communiquent par passage de messages. Comme vous pouvez le voir dans le code ci-dessus, l'utilisateur clique sur le dé dans `index.html`, et `index.js` envoie un message à `service-worker.js` demandant un nouveau conseil. Le Service Worker récupère alors le conseil et le renvoie dans un autre message.

`chrome.runtime.onMessage.addListener` écoute les messages entrants et `sendResponse` y répond.

Notre Service Worker est maintenant prêt à récupérer des conseils. L'étape suivante consiste à faire interagir notre `index.js` avec lui.

### Étape 4 : Ajouter la fonctionnalité de l'application

Tout d'abord, nous allons créer notre fichier `index.js`. Ce script est responsable de toute la logique orientée utilisateur. Il gérera l'interaction de l'utilisateur (clic sur le dé), enverra un message à notre `service-worker.js` pour obtenir un nouveau conseil, puis mettra à jour l'`index.html` avec le conseil récupéré.

Notre `index.js` effectuera les étapes suivantes :

1. Référencer les éléments HTML où nous afficherons l'ID du conseil, la citation et le dé.
    
2. Mettre en place un écouteur d'événements pour le clic sur le dé.
    
3. Envoyer un message au `service-worker.js` pour demander un nouveau conseil.
    
4. Recevoir le conseil du `service-worker.js` et mettre à jour le contenu sur la page `index.html`.
    

```javascript
// Récupérer les références de nos éléments HTML
const adviceIdElement = document.getElementById('advice-id-number');
const adviceQuoteElement = document.getElementById('advice-quote');
const generateAdviceBtn = document.getElementById('generate-advice-btn');

// Fonction pour demander un conseil au Service Worker
function requestNewAdvice() {
  chrome.runtime.sendMessage({ action: "fetchAdvice" }, (response) => {
    if (chrome.runtime.lastError) {
      console.error("Erreur lors de l'envoi du message :", chrome.runtime.lastError);
      adviceQuoteElement.textContent = "Erreur : Impossible d'obtenir le conseil.";
      adviceIdElement.textContent = "---";
      return;
    }
    if (response && response.advice) {
      adviceIdElement.textContent = response.advice.id;
      adviceQuoteElement.textContent = `« ${response.advice.advice} »`;
    } else if (response && response.error) {
      console.error("Erreur du Service Worker :", response.error);
      adviceQuoteElement.textContent = `Erreur : ${response.error}`;
      adviceIdElement.textContent = "---";
    }
  });
}

if (generateAdviceBtn) {
  generateAdviceBtn.addEventListener('click', requestNewAdvice);
} else {
  console.error("Bouton de génération de conseil non trouvé !");
}

document.addEventListener('DOMContentLoaded', requestNewAdvice);
```

Avec `index.js` en place, notre générateur de conseils est maintenant prêt, comme vous pouvez le voir dans le GIF ci-dessous :

![Un GIF montrant l'extension Chrome Advice Generator terminée](https://cdn.hashnode.com/res/hashnode/image/upload/v1755717163786/326dc332-bf3b-4a8a-ba3a-25bdc829cf68.gif align="center")

La prochaine étape cruciale est de savoir comment déboguer votre extension si quelque chose ne va pas.

## Comment déboguer votre extension Chrome

Chrome fournit d'excellents outils de débogage pour aider à résoudre les problèmes des extensions. Suivez toujours ces étapes essentielles :

* Rechargez votre extension après avoir effectué des changements (surtout dans `manifest.json` ou `service-worker.js`) en cliquant sur l'icône de rafraîchissement sur `chrome://extensions`.
    
* Vérifiez votre `manifest.json` pour les fautes de frappe – des virgules ou des crochets manquants casseront tout.
    
* Vérifiez l'URL de votre API et assurez-vous d'avoir les bonnes autorisations listées dans `manifest.json`.
    

### Débogage des pages HTML et JS principales

C'est probablement ici que vous rencontrerez la plupart de vos problèmes JavaScript ou HTML/CSS initiaux.

1. Ouvrez l'extension et faites un clic droit n'importe où dans la fenêtre contextuelle (popup) pour **Inspecter**.
    
2. Vérifiez l'onglet **Console** pour les erreurs JavaScript de votre fichier `index.js`.
    
3. Utilisez l'onglet **Éléments** pour inspecter votre HTML et ajuster les styles CSS en temps réel.
    

![Un GIF montrant comment inspecter les onglets Éléments et Console d'une extension Chrome](https://cdn.hashnode.com/res/hashnode/image/upload/v1755714931805/f03dc46c-b78b-44b6-bc67-bb7fe02499a9.gif align="center")

### **Débogage du Service Worker – Crucial pour MV3**

Le Service Worker s'exécute en arrière-plan et possède ses propres DevTools séparés.

1. Allez sur `chrome://extensions`.
    
2. Cliquez sur le lien **Service worker** sous votre extension ou sur le bouton **Erreurs**.
    
3. Vérifiez les onglets **Console** et **Network** (Réseau) pour les erreurs de service worker et d'API respectivement.
    

![Une capture d'écran montrant une extension Chrome avec le lien du service worker et le bouton d'erreurs](https://cdn.hashnode.com/res/hashnode/image/upload/v1755715410580/2c03c56c-affe-4a0a-939f-72ca866eecd3.png align="center")

## **Conclusion**

Félicitations, vous venez de créer une extension Chrome en utilisant Manifest V3. Vous avez créé une interface utilisateur, implémenté un traitement en arrière-plan avec un service worker et établi une communication entre les différentes parties de votre extension. Ces compétences sont les piliers de toute extension Chrome, qu'elle soit simple ou complexe.

Voici quelques ressources utiles :

* [MDN sur les extensions de navigateur](https://developer.mozilla.org/fr/docs/Mozilla/Add-ons/WebExtensions/What_are_WebExtensions)
    
* [Chrome Devs sur les extensions Chrome](https://developer.chrome.com/docs/extensions/get-started?hl=en)