---
title: Comment utiliser Chrome DevTools – Stratégies simples pour un développement
  web plus intelligent
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2024-02-15T16:12:02.000Z'
originalURL: https://freecodecamp.org/news/chrome-devtools
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/ChromeDevTools-1.png
tags:
- name: Google Chrome
  slug: chrome
- name: clean code
  slug: clean-code
- name: debugging
  slug: debugging
- name: devtools
  slug: devtools
- name: Problem Solving
  slug: problem-solving
seo_title: Comment utiliser Chrome DevTools – Stratégies simples pour un développement
  web plus intelligent
seo_desc: "As a web developer, there are many tools out there – in addition to your\
  \ code editor – that can make you more efficient. \nIt doesn't matter if you're\
  \ just starting out or have been coding for years. Knowing how to effectively use\
  \ Developer Tools (Dev..."
---

En tant que développeur web, il existe de nombreux outils – en plus de votre éditeur de code – qui peuvent vous rendre plus efficace.

Peu importe que vous débutiez ou que vous codiez depuis des années. Savoir utiliser efficacement les outils de développement (DevTools en abrégé) peut considérablement améliorer votre processus de développement. Vous pouvez modifier des pages à la volée, repérer rapidement des problèmes et comprendre en profondeur les performances de votre site.

Tous les navigateurs majeurs disposent de leurs propres DevTools qui vous permettent d'examiner le code d'une page web, d'évaluer ses métriques et d'exécuter certains tests en parallèle. Cet article discutera des DevTools de Chrome, car c'est la norme de l'industrie.

## Table des matières :

* [Qu'est-ce que Chrome DevTools ?](#heading-quest-ce-que-chrome-devtools)
* [Comment ouvrir Chrome DevTools](#heading-comment-ouvrir-chrome-devtools)
* [Raccourcis clavier pour une navigation facile](#heading-raccourcis-clavier-pour-une-navigation-facile)
* [Fonctionnalités clés de Chrome DevTools](#heading-fonctionnalites-cles-de-chrome-devtools)
* [Cas d'utilisation pratiques de DevTools](#heading-cas-dutilisation-pratiques-de-devtools)
* [Conclusion](#heading-conclusion)

# Qu'est-ce que Chrome DevTools ?

Chrome DevTools est un ensemble d'outils essentiels pour diagnostiquer et résoudre les défis du développement web, directement dans le navigateur Google Chrome.

Il vous donne un accès direct au fonctionnement interne d'un site web - pour inspecter le HTML et le CSS, déboguer JavaScript, analyser les performances et voir l'impact immédiat de votre code, le tout en temps réel.

Cet accès direct au fonctionnement interne d'un site web est crucial pour diagnostiquer rapidement et efficacement les problèmes, garantissant que vos applications web sont à la fois performantes et sans bogues.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/DevToolsScreenshots-1.png)
_Une grille d'éléments, de la console, des panneaux de performances et de réseau_

# Comment ouvrir Chrome DevTools

Pour ouvrir DevTools dans votre navigateur Chrome, vous pouvez soit :

1. Faire un clic droit sur n'importe quelle page web et sélectionner "Inspecter" dans la liste des options.
2. Utiliser le raccourci (commande + option + I sur Mac ou contrôle + maj + I sur Windows).
3. Cliquer sur l'icône des trois points à côté de votre photo de profil sur votre navigateur Chrome, choisir "Plus d'outils" et "Outils de développement" dans la deuxième boîte d'options.

Il s'ouvre généralement dans une interface en écran divisé, soit en dessous de votre page web actuelle, soit à côté. Une fois ouvert, ses fonctionnalités s'alignent sous forme d'onglets en haut de la fenêtre DevTools. Ces onglets incluent : Éléments, Console, Source, Réseau, Application, Sécurité, Mémoire, Performance, Audits.

## Raccourcis clavier pour une navigation facile

1. Utilisez Cmd ou Ctrl + Shift + C pour ouvrir le panneau Éléments
2. Utilisez Cmd ou Ctrl + Shift + J pour ouvrir le panneau Console
3. Utilisez Cmd ou Ctrl + ] pour passer à l'onglet suivant
4. Utilisez Cmd ou Ctrl + [ pour revenir à l'onglet précédent

# Fonctionnalités clés de Chrome DevTools

DevTools est rempli de fonctionnalités essentielles pour les développeurs web afin de rationaliser divers aspects de leur flux de travail. Examinons-en quelques-unes en détail maintenant.

## Panneau Éléments

Ce panneau est utilisé pour inspecter et modifier le HTML et le CSS d'une page web en temps réel, ce qui est idéal pour déboguer les problèmes de mise en page ou expérimenter de nouveaux styles avant de les appliquer dans votre code réel. Vous pouvez également voir comment le DOM (Document Object Model) est structuré.

Imaginez ajuster l'apparence du pied de page de votre site web (couleur de fond, taille de police) directement dans votre navigateur et voir les résultats instantanément.

Avec DevTools ouvert, cliquez sur l'onglet Éléments pour y accéder.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/elpanel-1.png)
_Une capture d'écran du panneau Éléments de Chrome DevTools_

## Panneau Console

Ce panneau sert de terrain de jeu interactif pour JavaScript dans le navigateur. Que vous traquiez un bug insaisissable avec un rapide `console.log()` ou que vous expérimentiez avec des éléments DOM, dans le panneau Console, vous pouvez tester des extraits de JavaScript et voir les journaux ou les erreurs dans la page web actuellement chargée.

Pour l'utiliser, ouvrez simplement DevTools et sélectionnez l'onglet "Console" ou utilisez le raccourci (option + commande + J sur Mac ou contrôle + maj + J sur Windows).

![Image](https://www.freecodecamp.org/news/content/images/2024/02/clpanel-1.png)
_Une capture d'écran du panneau Console de Chrome DevTools_

## Panneau Réseau

Ce panneau vous donne un aperçu de toute l'activité réseau sur votre page web – du suivi de chaque ressource chargée à la manière dont votre site communique avec les serveurs.

Si vous vous êtes déjà demandé pourquoi votre site web met une éternité à se charger ou pourquoi certaines requêtes API semblent disparaître dans la nature, le panneau Réseau est votre solution, car il fournit des informations sur la réussite ou l'échec des appels API.

Pour y accéder, ouvrez DevTools et accédez à l'onglet "Réseau".

![Image](https://www.freecodecamp.org/news/content/images/2024/02/netpanel-2.png)
_Une capture d'écran du panneau Réseau de Chrome DevTools_

## Panneau Performance

Ce panneau est utilisé pour capturer et analyser les métriques de performance d'un site web. Il montre toutes les activités qui se produisent lors de l'interaction avec une page.

Lorsque votre application web commence à ralentir sous une utilisation intensive, le panneau Performance peut identifier où se situent les goulots d'étranglement de performance afin que vous puissiez résoudre ces problèmes, garantissant que votre application fonctionne sans problème.

Avec DevTools ouvert, cliquez sur l'onglet "Performance" pour l'utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/perfpanel-1.png)
_Une capture d'écran du panneau Performance de Chrome DevTools_

Les panneaux ci-dessus ne sont qu'une poignée de ceux disponibles, mais ils sont de loin les plus populaires et les plus essentiels. Les utiliser correctement rendra vos processus de développement plus intuitifs et gratifiants.

# Cas d'utilisation pratiques de DevTools

Dans les exemples interactifs suivants, j'ai intentionnellement créé le mini-projet dans Codepen **avec des problèmes** pour simuler des scénarios de débogage du monde réel en utilisant Chrome DevTools.

J'ai pensé que ce serait un excellent moyen de mettre en évidence les utilisations pratiques de certains panneaux et fonctionnalités de DevTools pour identifier les bugs et résoudre les problèmes directement dans le navigateur.

### Prérequis

* Navigateur Chrome ([Cliquez sur ce lien pour télécharger](https://support.google.com/chrome/answer/95346?hl=en&co=GENIE.Platform%3DDesktop))
* Une compréhension de base du HTML, du CSS et de JavaScript
* [Codepen](https://codepen.io/ophyboamah/full/rNpZZwo)

<p class="codepen" data-height="300" data-default-tab="html,result" data-slug-hash="rNpZZwo" data-user="ophyboamah" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>Voir le stylo <a href="https://codepen.io/ophyboamah/pen/rNpZZwo">
  Fenêtre modale</a> par Ophy Boamah (<a href="https://codepen.io/ophyboamah">@ophyboamah</a>)
  sur <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

## Comment déboguer le HTML et le CSS avec le panneau Éléments

Notre mini-projet contient une modale qui, lors du clic, devrait afficher une fenêtre modale avec des informations importantes. Mais il y a un bug qui empêche cela de se produire.

Cette situation prépare le terrain pour une démonstration pratique de la manière dont vous pouvez utiliser le panneau Éléments pour résoudre les problèmes de style et de structure.

```
<body>
  <button class="show-modal">Cliquez ici pour découvrir un secret 🤫</button>

  <div class="modal hidden">
    <button class="close-modal">&times;</button>
    <h1>Salut, c'est Ophy ici 👋🏾</h1>
    <p>
      Je dirige Women Who Code Frontend, une communauté mondiale à distance de 3 000+ femmes développeuses frontend et passionnées. Retrouvez-nous sur beacons.ai/wwcodefrontend
    </p>
  </div>
  <div class="overlay hidden"></div>

  <script src="script.js"></script>
</body>
```

```css
.hidden {
  display: none;
}

.modal {
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  width: 70%;

  background-color: white;
  padding: 6rem;
  border-radius: 5px;
  box-shadow: 0 3rem 5rem rgba(0, 0, 0, 0.3);
  z-index: 10;
}
```

Dans le code HTML de notre modale ci-dessus, nous avons ajouté le nom de classe 'modal hidden' qui a un style correspondant avec la propriété CSS `display:none` qui est définie pour masquer la modale lorsque la page est chargée initialement et ne l'afficher que lorsque le bouton est cliqué.

### ✅ Étape 1 - Inspection initiale :

Essayez de déclencher la modale en cliquant sur le bouton 'Cliquez ici pour découvrir un secret'. Comme nous avons configuré cela pour ne pas fonctionner, faites un clic droit sur la zone où la modale devrait apparaître et choisissez "Inspecter" pour ouvrir le panneau Éléments de DevTools.

### ✅ Étape 2 - Diagnostiquer les problèmes de visibilité :

Dans le panneau Éléments, localisez la modale dans le DOM pour voir que la modale est présente mais non visible. Cela confirme que le bug est causé par notre code CSS `display: hidden`.

Dès que vous cliquez sur la modale dans le DOM, toutes les classes CSS correspondantes seront affichées dans la section Styles en bas du panneau Éléments. Vous pouvez activer ou désactiver certaines propriétés ou en taper d'autres pour voir les effets en temps réel.

Modifiez manuellement le nom de la classe de `modal hidden` à `modal block` pour déclencher les bonnes propriétés qui feront apparaître la modale.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/modalblock.png)
_Une capture d'écran du débogage du HTML, CSS de la modale dans le panneau Éléments_

### ✅ Étape 3 - Centrer la modale :

Maintenant, la modale est visible, mais elle est affichée en haut – ce qui est différent de l'endroit où nous aimerions qu'elle soit (c'est-à-dire au centre de la page).

Pour changer cela, modifiez la propriété `transform` en `translate(-50%, -50%)` en ajoutant le deuxième `-50%` et assurez-vous que `top: 50%` et `left: 50%` sont correctement définis pour centrer la modale sur l'écran.

### ✅ Étape 4 - Améliorer l'apparence :

Vous pouvez aller plus loin pour affiner l'apparence de la modale en ajustant sa `background-color`, `padding`, ou d'autres propriétés stylistiques directement dans les Styles pour obtenir le look et la sensation souhaités.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/ChromeDevTools.gif)
_Un GIF corrigeant la modale dans le panneau Éléments de Chrome DevTools_

## Déboguer JavaScript avec le panneau Sources

J'ai ajouté un bug dans le code JavaScript de notre mini-projet de modale pour l'empêcher de s'ouvrir lorsque le bouton est cliqué.

Dans le monde réel, cela empêcherait les commandes d'ouverture et de fermeture de déclencher une action, ce qui laisserait les utilisateurs incapables d'interagir avec le contenu et frustrés. Résolvons et déboguons ce problème dans le panneau Sources.

Dans le code ci-dessous, la fonction openModal est configurée pour supprimer les classes indiquées. Cependant, cela ne fonctionne pas parce que nous avons délibérément mal orthographié `hidden`.

```javascript
// Introduction d'un bug : orthographe incorrecte de 'hidden' en 'hiddn'
const openModal = function () {
  modal.classList.remove("hiddn"); // Bug intentionnel
  overlay.classList.remove("hidden");

  // Récupérer des données d'une vraie API et les afficher dans la modale
};
```

### ✅ Étape 1 - Configurer les points d'arrêt :

Ouvrez Chrome DevTools et accédez au panneau Sources. Ici, trouvez le fichier JavaScript qui inclut la fonctionnalité de la modale (dans notre exemple, c'est pen.js).

La fonction openModal contient la logique pour afficher la modale à l'écran. Cette fonction inclura une ligne où la classe de l'élément modale est manipulée pour supprimer une classe "hidden".

Cliquez sur le numéro à côté de cette ligne de code dans DevTools. Une icône bleue (ou parfois rouge, selon le thème) apparaît à côté du numéro de ligne, indiquant qu'un point d'arrêt a été défini. Ce point d'arrêt mettra en pause l'exécution de notre code JavaScript dès qu'il atteindra cette ligne.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/soscreenshot.png)
_Une capture d'écran de la configuration des points d'arrêt dans le JS de la modale dans le panneau Sources_

Les points d'arrêt mettent en pause l'exécution du code à des points critiques, vous permettant d'inspecter l'état actuel des variables et de comprendre le flux d'exécution. Cette étape est cruciale pour identifier où le code s'écarte du comportement attendu.

### ✅ Étape 2 - Examiner le flux d'exécution du code :

Avec notre point d'arrêt en place, essayez d'ouvrir la modale en cliquant sur son bouton. L'exécution de notre code JavaScript s'arrête maintenant à notre point d'arrêt, ce qui nous permet de parcourir le code ligne par ligne.

C'est l'occasion d'observer les variables, les appels de fonction, de rechercher des anomalies telles que des fonctions mal nommées, une logique incorrecte ou des exceptions non capturées qui pourraient expliquer pourquoi la modale ne fonctionne pas.

Dans notre cas, c'est parce que nous avons intentionnellement mal orthographié le nom de la classe `hidden` en `hiddn`. Corrigons cela dans le code pour que la modale fonctionne à nouveau.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/ChromeDevTools--2-.gif)
_Un GIF de dépannage du bug de la modale dans le panneau Éléments de Chrome DevTools_

## Optimiser les performances avec le panneau Réseau

Ici, j'ai ajouté une fonction fetch qui fait un appel API à un endpoint en direct ([`https://jsonplaceholder.typicode.com/posts/1`](https://jsonplaceholder.typicode.com/posts/1)). C'est une excellente opportunité d'explorer les capacités du panneau Réseau pour diagnostiquer et comprendre les problèmes liés au réseau.

D'après le code ci-dessous, vous pouvez voir que la fonction openModal ne se contente pas d'ouvrir la modale, mais fait également un appel API à l'endpoint `jsonplaceholder` pour récupérer des données.

```javascript
const openModal = function () {
  fetch('https://jsonplaceholder.typicode.com/posts/1')
    .then(response => response.json())
    .then(json => document.getElementById('modal-content').innerText = json.title)
    .catch(error => console.error('Erreur de chargement du contenu :', error));
};
```

### ✅ Étape 1 - Initier l'appel API :

Sur l'interface utilisateur du projet de modale, cliquez sur le bouton 'Cliquez ici pour découvrir un secret'. Bien que la modale ne s'active pas visiblement, en raison de la logique de fetch dans la fonction openModal, un appel API sera effectué.

### ✅ Étape 2 - Inspection du panneau Réseau :

Idéalement, votre panneau Réseau devrait être ouvert avant de cliquer sur le bouton, mais vous pouvez également inverser les étapes. Des informations détaillées sur votre requête API telles que la méthode de la requête, le code de statut, la réponse et le temps qu'elle a pris pour se compléter, seront disponibles sous les onglets headers, preview, response, initiator et timing respectivement.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/netscreenshot.png)
_Une capture d'écran donnant un aperçu de la requête API dans le panneau Réseau_

### ✅ Étape 3 - Simulation des conditions réseau :

Utilisez la fonction de limitation du panneau Réseau pour imiter diverses vitesses de réseau comme hors ligne ou 3G lent pour voir comment la requête API se comporte dans des conditions contraignantes.

De cette manière, vous pouvez comparer comment différentes vitesses de réseau peuvent affecter les performances de l'application. Cela vous apprendra l'importance d'optimiser les stratégies de chargement des données pour améliorer l'expérience utilisateur, surtout sur des connexions plus lentes.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/ChromeDevTools--1-.gif)
_Un GIF observant les requêtes et réponses API dans le panneau Réseau de Chrome DevTools_

# Conclusion

Intégrer Chrome DevTools dans votre routine de développement web ne consiste pas seulement à corriger des bugs. Il s'agit de rationaliser votre flux de travail, de rendre vos sites plus accessibles et d'améliorer leurs performances.

À travers notre mini-projet de fenêtre modale, nous avons vu de première main comment DevTools peut répondre à une large gamme de défis de développement, mais ce n'est là qu'effleurer la surface de ce qu'il peut faire.

Alors que vous continuez à explorer ses capacités et à vous familiariser avec ses fonctionnalités, vous découvrirez qu'il s'agit d'un compagnon inestimable dans votre parcours de développement web – conçu pour rendre votre processus de développement non seulement plus rapide, mais aussi plus gratifiant.

* [La documentation officielle de Chrome DevTools](https://developer.chrome.com/docs/devtools)
* [Comment utiliser les Chrome DevTools pour dépanner les sites web](https://www.freecodecamp.org/news/learn-how-to-use-the-chrome-devtools-to-troubleshoot-websites/)