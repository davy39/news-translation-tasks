---
title: L'astuce d'optimisation Web que vous avez peut-être manquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T14:16:27.000Z'
originalURL: https://freecodecamp.org/news/web-optimization-a-secret-world-to-unleash-5fbdf1065945
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GpMnxERgXwdHlsW4B4R8pA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: optimization
  slug: optimization
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: L'astuce d'optimisation Web que vous avez peut-être manquée
seo_desc: 'By Harnoor Bandesh

  Have you ever wondered why the Google search pages or Amazon site loads really fast?
  Well stay with me while I take you through the concept, which drastically improves
  page performance. But firstly, let us go through some concepts ...'
---

Par Harnoor Bandesh

Vous êtes-vous déjà demandé pourquoi les pages de recherche Google ou le site Amazon se chargent si rapidement ? Eh bien, restez avec moi pendant que je vous explique le concept qui améliore considérablement les performances des pages. Mais d'abord, passons en revue quelques concepts qui mènent à cette idée.

### Analyser le Chemin de Rendement Critique (CRP)

Tout d'abord, définissons le vocabulaire que nous allons utiliser :

1. **Ressource Critique** : Ressource qui pourrait bloquer le rendu initial de la page
2. **Time To First Byte (TTFB)** : Mesure la durée entre la requête HTTP du navigateur et la réception du premier octet de la page par le navigateur

Optimiser les performances Web consiste à comprendre ce qui se passe dans les étapes intermédiaires entre la réception des fichiers HTML, CSS et JavaScript et le traitement nécessaire pour les transformer en pixels rendus — c'est le chemin de rendu critique (CRP).

Avant que les pages ne soient rendues, le navigateur doit passer par toutes les étapes suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/WQe1LRl6yEYWqRRCvl4EZQ62h1J-MWalcjsQ)

Lorsque le navigateur atteint la page pour la première fois, il télécharge le fichier HTML. Il commence ensuite à construire l'arbre DOM (Document Object Model). Chaque balise en HTML représente un nœud à l'intérieur de l'arbre DOM qui contient toutes les informations à son sujet. Prenons un exemple pour comprendre cela.

Supposons que le navigateur reçoive le HTML suivant du serveur :

```html
<html>
 <head>
   <meta name="viewport" content="width=device-width,initial-scale=1">
   <link href="style.css" rel="stylesheet">
   <title>Chemin Critique</title>
 </head>
 <body>
    <p>Bonjour <span>étudiants en performance web</span> !</p>
     <div><img src="awesome-photo.jpg"></div>
 </body>
```

Le navigateur le convertit en un objet arborescent appelé le DOM comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/AqH7doxr-cbo5R-32GKdvZ5xYaCvGwwlMj4u)
_Source : [https://developers.google.com/web/fundamentals/performance/critical-rendering-path/constructing-the-object-model](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/constructing-the-object-model" rel="noopener" target="_blank" title=")_

**Note** : Le processus de construction du DOM est incrémental. C'est la base de l'idée pour laquelle j'écris cet article.

Pendant que le navigateur construisait le DOM, il a rencontré une balise `link` dans la section `head` référençant une feuille de style CSS externe.

Anticipant qu'il a besoin de cette ressource pour rendre la page, il envoie une requête pour la même, qui revient avec le contenu suivant :

```css
body { font-size: 16px }
p { font-weight: bold } 
span { color: red } 
p span { display: none } 
img { float: right }
```

Le navigateur crée ensuite le CSSOM (CSS Object Model) :

![Image](https://cdn-media-1.freecodecamp.org/images/GwlK2gSYqVlvagMKeEE8c0I7zRYFPAP9bL0H)
_Source : [https://developers.google.com/web/fundamentals/performance/critical-rendering-path/constructing-the-object-model](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/constructing-the-object-model" rel="noopener" target="_blank" title=")_

Les arbres CSSOM et DOM sont combinés pour former un arbre de rendu. L'arbre de rendu est ensuite utilisé pour calculer la mise en page de chaque élément visible.

Voici à quoi ressemble un arbre de rendu :

![Image](https://cdn-media-1.freecodecamp.org/images/qKI-Nmv3BuUQLW-9bG2u-fUxR3UMznJ-63wC)
_Source : [https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction" rel="noopener" target="_blank" title=")_

Certains nœuds ne sont pas visibles — comme les balises de script et les balises meta — et sont omis puisqu'ils ne sont pas reflétés dans la sortie rendue. Certains nœuds sont cachés via CSS et sont également omis de l'arbre de rendu.

Maintenant que l'arbre de rendu est en place, nous pouvons passer à l'étape de mise en page. Le résultat du processus de mise en page est un « modèle de boîte » dans lequel la position et la taille exactes de chaque élément sont capturées. Toutes les mesures relatives sont converties en pixels absolus à l'écran.

Enfin, maintenant que nous savons quels nœuds sont visibles, et leurs styles et géométrie calculés, nous pouvons transmettre ces informations à l'étape finale. Cette étape convertit chaque nœud de l'arbre de rendu en pixels réels à l'écran. Cette étape est souvent appelée « peinture ».

**Note** : le CSS est bloquant pour le rendu. Jusqu'à ce que le CSSOM soit construit, le navigateur ne peut pas passer à l'étape de l'arbre de rendu. Par conséquent, nous devons servir le fichier CSS au navigateur dès que possible, c'est pourquoi nous gardons toutes les balises `link` dans la section `head`.

Maintenant, ajoutons JavaScript à notre exemple :

```html
<html>
 <head>
   <meta name="viewport" content="width=device-width,initial-scale=1">
   <link href="style.css" rel="stylesheet">
   <title>Chemin Critique</title>
 </head>
 <body>
    <p>Bonjour <span>étudiants en performance web</span> !</p>
    <div><img src="awesome-photo.jpg"></div>
    <script src="app.js"></script>
 </body>
```

Par défaut, l'exécution de JavaScript est « bloquante pour l'analyseur ». Lorsque le navigateur rencontre une balise `script` dans le document, il effectue les étapes suivantes :

1. Pause de la construction du DOM

2. Téléchargement du fichier

3. Transfert du contrôle à l'environnement d'exécution JavaScript

4. Laisse le script s'exécuter avant de poursuivre la construction du DOM

Le navigateur ne sait pas ce que le script prévoit de faire sur la page, il suppose donc le pire scénario et bloque l'analyseur.

Attendez !!! Ce n'est pas le pire cas qui peut se produire pendant l'analyse du DOM. Dans le dernier exemple, nous pouvons voir que nous avons à la fois des fichiers CSS et JavaScript externes que le navigateur doit télécharger.

Maintenant, supposons que les fichiers CSS prennent un certain temps à télécharger, et entre-temps le fichier JavaScript est téléchargé. Maintenant, le navigateur supposera le pire scénario que JavaScript pourrait interroger le CSSOM, c'est pourquoi il ne commence pas à analyser le fichier JavaScript jusqu'à ce que le fichier CSS soit téléchargé et que le CSSOM soit prêt !

Regardons un diagramme qui pourrait nous aider à mieux comprendre ce que j'essaie de dire :

![Image](https://cdn-media-1.freecodecamp.org/images/SKjeC1Cwz5n179CwODwHkG8K0XWnfrRdLSyy)
_Source : [https://developers.google.com/web/fundamentals/performance/critical-rendering-path/analyzing-crp](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/analyzing-crp" rel="noopener" target="_blank" title=")_

Le CSS est un **démon** pour toute page web ! Il est bloquant pour le rendu et l'analyse. Nous devons être très prudents dans sa gestion.

Examinons quelques moyens d'optimiser le CRP.

### Optimiser le CRP

À ce stade, nous savons que le CSS peut être un démon. Obtenez-le pour le client dès que possible pour optimiser le temps jusqu'au premier rendu. Que faire si nous avons certains styles CSS qui ne sont utilisés que sous certaines conditions ? Par exemple, lorsque la page est imprimée ou projetée sur un grand écran ?

Il serait bien de ne pas avoir à bloquer le rendu sur ces ressources. Les « types de média » CSS et les « requêtes de média » nous permettent de traiter ces cas d'utilisation :

```html
<link href="style.css" rel="stylesheet">
<link href="print.css" rel="stylesheet" media="print">
<link href="other.css" rel="stylesheet" media="(min-width: 40em)">
```

Une [requête de média](https://developers.google.com/web/fundamentals/design-and-ux/responsive/#use-css-media-queries-for-responsiveness) se compose d'un type de média qui vérifie les conditions de certaines fonctionnalités de média. Par exemple, notre première déclaration de feuille de style ne fournit pas de type de média ou de requête, elle s'applique donc dans tous les cas. C'est-à-dire qu'elle est toujours bloquante pour le rendu.

D'autre part, la deuxième déclaration de feuille de style s'applique uniquement lorsque le contenu est imprimé. Par conséquent, cette déclaration de feuille de style n'a pas besoin de bloquer le rendu de la page lorsqu'elle est chargée pour la première fois.

Enfin, la dernière feuille de style sera exécutée par le navigateur si la condition est remplie. Si la condition n'est pas remplie, le navigateur ne bloquera pas le rendu.

Lorsque vous déclarez vos ressources de feuille de style, portez une attention particulière au type de média et aux requêtes. Ils ont un grand impact sur les performances du chemin de rendu critique.

Par défaut, tout JavaScript est bloquant pour l'analyseur. Un signal au navigateur que le script n'a pas besoin d'être exécuté au point où il est référencé permet au navigateur de continuer à construire le DOM et laisse le script s'exécuter lorsqu'il est prêt. Par exemple, après que le fichier a été récupéré du cache ou d'un serveur distant.

Pour y parvenir, nous marquons notre `script` comme `async` :  
`<script src="app.js" async></script>`

Ajouter le mot-clé `async` à la balise `script` indique au navigateur de ne pas bloquer la construction du DOM pendant qu'il attend que le script devienne disponible, ce qui peut améliorer considérablement les performances.

Un autre point positif de l'attribut `async` est que le `script` n'est pas bloqué en attendant que le CSSOM soit prêt.

Le script d'analyse est un excellent exemple pour l'attribut `async` car le `script` ne modifie pas le DOM de quelque manière que ce soit. Il existe un autre attribut pour les balises `script`, qui est `defer`. Vous pouvez en apprendre davantage sur `defer` en visitant [ici](https://hacks.mozilla.org/2009/06/defer/).

Et enfin — l'apogée de l'article arrive, où je vais vous révéler le principal secret — en plus des optimisations mentionnées ci-dessus — que les grandes entreprises appliquent et font des merveilles...

### Envoyer le HTML par morceaux depuis le serveur

Regardez les images suivantes et décidez : de quelle manière souhaitez-vous que vos sites web se rendent ?

![Image](https://cdn-media-1.freecodecamp.org/images/L0hvfXMCOkYqMTg1sMS9B8iSMgKSdOTYZv6n)
_Source : [https://developers.google.com/web/fundamentals/performance/critical-rendering-path/](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/" rel="noopener" target="_blank" title=")_

Vous avez une réponse ? C'est bien sûr la première ! Personne n'aime vraiment voir la page blanche pendant si longtemps. Il est beaucoup mieux de rendre le HTML par morceaux sur la page web, ce que font les pages de recherche Google, Amazon et autres géants.

Maintenant, lorsque vous accédez pour la première fois à l'URL d'un site web, le HTML complet de la page est construit sur le serveur. Jusqu'à ce moment, le navigateur reste inactif sans rien faire.

Après que le HTML est construit sur le serveur, il est transmis au navigateur. Le navigateur commence alors à construire le DOM et passe par toutes les étapes du CRP comme mentionné précédemment.

Le diagramme suivant nous aidera à clarifier cela :

![Image](https://cdn-media-1.freecodecamp.org/images/d6sq4uTavOf-X92c6UNvjssaPnANjwZdZVtj)

Alors pourquoi ne pas optimiser le temps d'inactivité du navigateur et le faire commencer à construire le DOM en envoyant le morceau de HTML qui est prêt au serveur ? En d'autres termes, nous pouvons envoyer le HTML par morceaux dès qu'ils sont prêts, au lieu d'attendre que tout le HTML soit préparé. Cela fera commencer la construction de l'arbre DOM/CSSOM par le navigateur au lieu d'attendre inactif. N'est-ce pas une idée merveilleuse !

J'espère que le diagramme suivant pourra clarifier cette idée davantage :

![Image](https://cdn-media-1.freecodecamp.org/images/tBQsjnYmgHkzdtbRxgjfhJPKe9p2pbXvOeJd)

La page est divisée en morceaux de HTML sur le serveur. Maintenant, le serveur, au lieu d'attendre que tout le HTML soit prêt puis de le servir au navigateur, enverra les morceaux de HTML dès qu'ils sont prêts sur le serveur. Cela signifie que les premiers morceaux n'attendront pas que les deux autres soient prêts — ils seront servis au navigateur dès qu'ils seront prêts sur le serveur.

Prenons un exemple pour comprendre cette idée encore mieux. Voici la page de recherche Google :

![Image](https://cdn-media-1.freecodecamp.org/images/ZDbrdlHDORbGDPNNwunuhJcOPaDWzUjRXf0x)

Maintenant, supposons que nous accédons à cette URL, et le navigateur envoie une requête au serveur pour servir cette page. Le serveur commence à construire cette page et a terminé le HTML de la Partie A, mais pour la Partie B, il doit récupérer les données d'une source qui prendra un peu plus de temps.

Maintenant, au lieu d'attendre que la partie B soit terminée, le serveur envoie le HTML terminé de la partie A au navigateur afin qu'il commence à construire le DOM.

Entre-temps, le serveur prépare le HTML de la partie B avec les données requises. De cette manière, l'utilisateur pourra voir la page web se charger progressivement dans le navigateur. Envoyer le HTML par morceaux réduit également le Time To First Byte et améliore les performances et l'indice de vitesse de la page.

C'est ce que Google fait réellement dans ses pages de recherche ! Même Amazon envoie d'abord son en-tête tandis que le reste de la page est préparé sur le serveur.

Envoyer le HTML par morceaux sert également un autre objectif d'optimisation. Comme votre balise `head` atteint le client en premier, le navigateur initie les requêtes CSS et autres dans la balise. Cela aide le navigateur à télécharger d'autres ressources critiques tandis que le reste du HTML est préparé par le serveur.

Le temps typique pour récupérer une page du serveur est d'environ 500 ms. Mais un temps typique pour obtenir le premier morceau du serveur est d'environ 20-30 ms. L'appel CSS qui devait être initié après 500 ms sera maintenant initié après 20-30 ms, donnant un coup de pouce de 470-480 ms à la page web. Vous pouvez même `pré-charger` les images lourdes dans la balise `head` qui seront utilisées par le HTML qui doit encore venir du serveur, améliorant ainsi le temps de chargement de la page !

Maintenant, la question est : comment envoyer le HTML par morceaux depuis le serveur.

Eh bien, nous avons différentes méthodes dans différents langages. Nous avons une méthode appelée `flush` en Java, .NET et PHP. En Node.js, nous devons utiliser `res.write()` chaque fois que notre morceau de HTML est prêt.

Note : Le navigateur ne fait pas d'appels répétitifs au serveur pour obtenir tous les morceaux. Tous les morceaux de HTML sont servis via un seul appel au serveur.

#### Ma POC

J'ai fait une POC avec Node.js, Express et React, où les composants React sont rendus sur Node.js et chaque composant est envoyé au navigateur dès que son HTML est préparé. Vous pouvez trouver le code source [ici](https://github.com/HBandesh/TTFB-Optimization-React).

Vous pouvez voir la démonstration en direct [ici](http://www.harnoorbandesh.co.in/).

Dans la démonstration, vous pouvez voir des liens. Le lien **Aller à la page sans découpage** vous mènera à la page dans laquelle le concept de découpage n'a pas été appliqué. Le lien **Aller à la page avec découpage** vous mènera à la page dans laquelle le concept de découpage a été appliqué. Voici des captures d'écran de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/frsNGUpRgNiCxnmLLHq2EtqHqU0-CdIxYG-r)

![Image](https://cdn-media-1.freecodecamp.org/images/7wZFlc1VlwjTUXF9U-LtCIXKPCcDR3UV6-G0)

![Image](https://cdn-media-1.freecodecamp.org/images/2DAhtWjA4TUtSb3vWDU4pPUfOgdQZjGJ9MeG)

La page est divisée en 4 parties. Dès que la Partie A est préparée sur le serveur, elle est envoyée au navigateur afin que le navigateur puisse commencer à construire le DOM.

La Partie B est construite à l'aide des données d'une API qui prendra un certain temps. Jusqu'à ce moment, le navigateur crée le HTML de la Partie A comme une construction de DOM dans un processus incrémental.

Dès que le HTML de la Partie B est préparé sur le serveur, il est servi au navigateur. L'histoire continue pour la Partie C et la Partie D.

Mais voici un piège : même avant d'envoyer la Partie A, j'envoie un autre morceau au navigateur qui est la balise `head` du HTML. Dans la balise `head`, j'ai pré-chargé toutes les images lourdes de la bannière dans l'en-tête et le pied de page, et j'ai fait un pré-connexion et un pré-récupération DNS de toutes les images restantes. En savoir plus sur le pré-chargement, le pré-récupération et la pré-connexion [ici](https://developer.mozilla.org/en-US/docs/Web/HTML/Preloading_content).

La balise `head` contient également les liens vers les fichiers CSS. Maintenant, dès que la Partie A est préparée sur le serveur, le navigateur envoie la requête de toutes les ressources dans la section `head` afin que la page se remplisse plus rapidement lorsque le HTML arrive.

Le test de performance sur les deux pages a été effectué à l'aide de l'extension Lighthouse dans Chrome. Et les résultats sont vraiment encourageants.

Le test a été effectué 10 fois sur les deux pages et la moyenne de toutes les valeurs est affichée ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/fgPue6pGUhWo3BkX1d4Cv5POoxS59l3J8M9Y)

En savoir plus sur [Time to Interactivity](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive), [Speed Index](https://developers.google.com/web/tools/lighthouse/audits/speed-index), [first meaningful paint](https://developers.google.com/web/tools/lighthouse/audits/first-meaningful-paint).

Cette implémentation de l'idée de base peut améliorer considérablement les performances d'une page web. J'espère avoir réussi à expliquer le concept.

Si vous souhaitez contribuer à l'idée, ou si vous pensez que quelque chose de mieux peut être fait, alors n'hésitez pas, fork le repo, créez une nouvelle branche et faites une pull request. Veuillez trouver ci-dessous les étapes pour activer l'application en local :

1. Clonez depuis [ici](https://github.com/HBandesh/TTFB-Optimization)
2. Installez Node sur votre système
3. Exécutez `npm install` dans le dossier où vous avez cloné le code
4. Exécutez `npm run dev` pour créer le fichier `bundle.js`
5. Terminez le processus et exécutez `npm start`
6. L'application démarrera sur le port `8080`

N'hésitez pas à partager cet article avec vos amis si vous le trouvez intéressant. :)