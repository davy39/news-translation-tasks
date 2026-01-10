---
title: Comment rendre les applications React optimisées pour le SEO – Un manuel pour
  débutants
subtitle: ''
author: Okosa Leonard
co_authors: []
series: null
date: '2024-01-09T15:25:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-seo-friendly-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/How-to-Make-React-Apps-SEO-Friendly-Cover--1-.png
tags:
- name: handbook
  slug: handbook
- name: React
  slug: react
- name: SEO
  slug: seo
- name: Web Development
  slug: web-development
seo_title: Comment rendre les applications React optimisées pour le SEO – Un manuel
  pour débutants
seo_desc: 'When developing your web applications, you should always consider search
  engine optimization (SEO) techniques. Many things come into play when you''re making
  sure your web application operates as intended and has an online presence.

  Search engines suc...'
---

Lors du développement de vos applications web, vous devriez toujours envisager des techniques d'optimisation pour les moteurs de recherche (SEO). De nombreux facteurs entrent en jeu pour s'assurer que votre application web fonctionne comme prévu et dispose d'une présence en ligne.

Les moteurs de recherche tels que Google, Bing et Yahoo servent de média principal pour les utilisateurs cherchant des informations, des services et des produits sur internet. Une application web optimisée pour le SEO est stratégiquement conçue pour s'aligner sur les algorithmes et les critères de classement des moteurs de recherche les plus populaires au monde.

L'objectif est clair : maximiser la visibilité de l'application sur internet, améliorer sa découvrabilité et, à terme, attirer une base d'utilisateurs plus large et plus ciblée.

Il y a de nombreux avantages à optimiser les applications web pour les moteurs de recherche. Cela garantit une exposition accrue dans les résultats de recherche, ce qui place l'application devant des personnes qui recherchent activement du contenu pertinent. Plus d'exposition entraîne plus de trafic organique, ce qui est un moyen plus économique et durable d'attirer des visiteurs que de dépendre de la publicité payante.

Plongeons plus profondément dans les raisons pour lesquelles le SEO est important pour vos applications web.

## Prérequis

Pour suivre cet article, vous devriez avoir une connaissance de niveau intermédiaire de React. Vous devriez également avoir des connaissances de base en Express.js et être à l'aise pour naviguer sur le web.

Vous devrez avoir un éditeur de code installé – par exemple VS Code – et créer une application React en utilisant Vite. Pour ce faire, vous pouvez saisir la ligne suivante dans votre terminal : `npm create vite@latest`, puis suivre les instructions. Ou vous pouvez utiliser cette commande dans votre terminal : `npx-create-react-app` (ou avec yarn) pour les utilisateurs de MacOS.

## Table des matières

* [Importance du SEO dans vos applications React.](#heading-importance-du-seo-dans-vos-applications-react)
    
* [Défis SEO dans les applications React.](#heading-defis-seo-dans-les-applications-react)
    
* [Solutions aux défis SEO des SPA.](#heading-solutions-aux-defis-seo-des-spa)
    
* [Qu'est-ce que le rendu côté client ?](#heading-quest-ce-que-le-rendu-cote-client)
    
* [Qu'est-ce que le rendu côté serveur ?](#heading-quest-ce-que-le-rendu-cote-serveur)
    
* [Comment implémenter le rendu côté serveur dans React.](#heading-comment-implementer-le-rendu-cote-serveur-dans-react)
    
* [Comment implémenter le Lazy Loading dans React.](#heading-comment-implementer-le-lazy-loading-dans-react)
    
* [Comment la vitesse de chargement des pages affecte-t-elle le classement SEO ?](#heading-comment-la-vitesse-de-chargement-des-pages-affecte-t-elle-le-classement-seo)
    
* [Comment optimiser les images dans React.](#heading-comment-optimiser-les-images-dans-react)
    
* [Outils pour mesurer la performance des images.](#heading-outils-pour-mesurer-la-performance-des-images)
    
* [Comment incorporer des métadonnées pour le SEO dans votre application React.](#heading-comment-incorporer-des-metadonnees-pour-le-seo-dans-votre-application-react)
    
* [Bonnes pratiques pour les métadonnées dans React.](#heading-bonnes-pratiques-pour-les-metadonnees-dans-react)
    
* [Comment optimiser les métadonnées avec le Schema Markup.](#heading-comment-optimiser-les-metadonnees-avec-le-schema-markup)
    
* [Tester votre application React à l'aide d'outils SEO](#heading-tester-votre-application-react-a-laide-doutils-seo)
    
* [Conclusion](#heading-conclusion)
    

## Importance du SEO dans vos applications React

Pour s'assurer que les personnes qui ont besoin de votre site web ou de votre application web le découvrent, l'optimisation pour les moteurs de recherche (SEO) est cruciale.

Voici quelques raisons pour lesquelles le SEO est vital pour les applications web :

### Visibilité et trafic accrus

Les meilleures pratiques de SEO aident à garantir que vos applications sont optimisées pour les moteurs de recherche, ce qui permet aux consommateurs de les localiser plus facilement en recherchant des termes pertinents. Des résultats de moteur de recherche améliorés entraînent des taux de clics plus élevés, ce qui attire à son tour plus d'utilisateurs organiques vers l'application web.

### Amélioration de l'expérience utilisateur

Les techniques de SEO se concentrent fréquemment sur l'amélioration du contenu, de la navigation et de la structure du site web pour améliorer l'expérience utilisateur globale. La satisfaction des utilisateurs est considérablement impactée par des applications en ligne bien optimisées, qui présentent souvent des temps de chargement plus rapides, une réactivité sur les appareils mobiles et une navigation facile.

### Marketing ciblé

Les applications web peuvent cibler des segments d'audience et des mots-clés particuliers grâce au SEO. Les applications web peuvent attirer des clients qui recherchent activement des produits, des services ou des informations qu'elles fournissent en optimisant les requêtes de recherche spécifiques utilisées par ces audiences.

### Crédibilité et fiabilité

La crédibilité et la fiabilité vont souvent de pair avec des classements élevés dans les moteurs de recherche. Les applications web qui se classent bien dans les résultats de recherche sont souvent plus dignes de confiance pour les utilisateurs. Donc, si vous avez un site web qui traite des données sensibles et propose des services dépendant de la confidentialité des utilisateurs, assurez-vous de mettre en œuvre des mesures de sécurité et des fonctionnalités d'interface utilisateur qui favorisent la confiance.

Ce ne sont là que quelques-unes des nombreuses raisons pour lesquelles vous devriez essayer de rendre vos sites web optimisés pour le SEO. Passons maintenant à la compréhension du SEO dans les applications basées sur React.

## Défis SEO dans les applications React

Il peut être un peu difficile de rendre les applications à page unique (SPA) optimisées pour le SEO. Pourquoi en est-il ainsi ?

Les Single Page Applications (SPA) peuvent aider à offrir une expérience utilisateur dynamique et fluide, car elles chargent le contenu de manière asynchrone sans nécessiter de rechargements complets de la page.

L'obstacle principal au SEO est que le matériel dynamique est rendu à l'aide de JavaScript, ce qui peut être difficile à comprendre et à indexer pour les robots d'exploration des moteurs de recherche conventionnels.

Le premier obstacle consiste à s'assurer que les moteurs de recherche peuvent explorer et indexer efficacement le contenu de la SPA. Les robots des moteurs de recherche peuvent éprouver plus de difficultés à indexer correctement le contenu des SPA car elles chargent souvent le contenu de manière asynchrone et s'appuient sur des frameworks JavaScript comme Angular ou React.

Pour fournir des instantanés HTML que les moteurs de recherche peuvent comprendre et améliorer la visibilité de la SPA dans les résultats de recherche, une mise en œuvre appropriée du rendu côté serveur (SSR) ou du pré-rendu devient essentielle.

### Solutions aux défis SEO des SPA

Il existe plusieurs façons de gérer les défis de SEO qui accompagnent les SPA.

La solution numéro un consiste à utiliser le rendu côté serveur (SSR) ou le pré-rendu pour créer des instantanés HTML pour les moteurs de recherche.

La solution numéro deux consiste à gérer des structures d'URL complexes pour garantir une indexation et une interprétation appropriées du contenu.

Ainsi, discutons maintenant de la manière dont le rendu côté serveur et le rendu côté client fonctionnent et des avantages qu'ils apportent à vos applications React.

## Qu'est-ce que le rendu côté client ?

Dans le développement web, le rendu côté client (ou CSR) est une technique qui utilise JavaScript pour rendre les pages web principalement du côté du client.

Dans cette architecture, le navigateur exécute JavaScript pour construire et rendre le contenu sur l'appareil du client dynamiquement après avoir reçu un minimum de HTML, CSS et JavaScript du serveur.

Dans le contexte des Single Page Applications (SPA), le rendu côté client est courant. Au sein d'une SPA, l'application actualise dynamiquement le contenu sans nécessiter de rechargement de page lorsqu'un utilisateur se déplace entre diverses sections ou pages. Parce que seules les données requises sont récupérées du serveur et que le rendu a lieu du côté client, cette méthode offre une expérience utilisateur plus fluide et réactive.

### Problèmes avec le rendu côté client

L'incapacité des robots d'exploration des moteurs de recherche à digérer et comprendre correctement le contenu est un inconvénient du rendu côté client, particulièrement en ce qui concerne le SEO. Les moteurs de recherche peuvent ne pas voir le contenu complètement rendu car le premier HTML envoyé par le serveur est souvent limité, ce qui pourrait affecter la visibilité de la SPA dans les résultats de recherche.

## Qu'est-ce que le rendu côté serveur ?

Dans le développement web, le rendu côté serveur (SSR) est une technique qui permet au navigateur du client de recevoir la page complètement rendue après que le contenu HTML a été généré par le serveur.

C'est différent du rendu côté client où l'appareil client rend le contenu en utilisant JavaScript et reçoit un HTML de base minimal du navigateur.

### Comment le rendu côté serveur aide-t-il avec le SEO ?

Le SSR est essentiel pour résoudre les problèmes liés au CSR dans le contexte du SEO, en particulier pour les Single Page Applications (SPA). Contrairement au CSR, le SSR profite au SEO de la manière suivante :

#### Exploration par les moteurs de recherche :

Habituellement, les robots d'exploration des moteurs de recherche utilisent l'analyse HTML pour indexer le contenu. Les moteurs de recherche peuvent éprouver des difficultés à comprendre et indexer le contenu lors de l'utilisation du CSR, car une grande partie du processus de rendu du contenu a lieu du côté client.

Le SSR aide à s'assurer que le moteur de recherche reçoit une page HTML complètement rendue du serveur, ce qui facilite l'indexation correcte du contenu par les robots.

#### Chargement initial de la page :

Contrairement au CSR, le SSR offre un chargement de page initial plus rapide. Des retards peuvent survenir dans le CSR car l'appareil client doit télécharger le minimum de HTML, exécuter JavaScript, puis rendre le contenu.

En pré-rendant le HTML, le SSR améliore l'expérience utilisateur en réduisant le temps nécessaire aux consommateurs pour voir le contenu initial.

#### Efficacité SEO

Le contenu indexable et facilement disponible est souvent privilégié par les moteurs de recherche. En garantissant que le serveur livre une page HTML complète au client, le SSR améliore les performances SEO et se conforme aux normes des moteurs de recherche.

Le rendu côté serveur améliore de façon astronomique les performances SEO. En donnant aux moteurs de recherche un contenu HTML entièrement rendu, en améliorant les capacités d'exploration et d'indexation, et en améliorant finalement la visibilité dans les résultats des moteurs de recherche, il surmonte les inconvénients du rendu côté client.

Maintenant, parlons de la façon d'utiliser le rendu côté serveur dans React.

## Comment implémenter le rendu côté serveur dans React

Si vous êtes un ingénieur ou développeur front-end, nous allons sortir un peu des sentiers battus ici. Le cas d'utilisation que je vais présenter implique un peu de connaissances en backend avec `express.js` et `node.js`, mais je vais vous guider.

En configurant votre application pour créer le HTML initial côté serveur au lieu de dépendre uniquement du rendu côté client, vous pouvez implémenter le Server-Side Rendering (SSR) dans React.

Le rendu côté serveur est facilité par React avec le package ReactDOMServer. Passons en revue le processus général pour activer le SSR dans une application React.

### Étape 1 : Configuration du serveur.

Pour gérer les requêtes entrantes et rendre les composants React du côté serveur, vous devrez configurer un serveur en utilisant `Node.js` et `Express.js`.

Ensuite, installez tous les packages requis, y compris `react`, `express`, `react-dom`, et toute autre dépendance. Vous devrez créer tous les fichiers nécessaires pour héberger différents composants et fonctionnalités comme vos fichiers `app.js` et `server.js`. Et enfin, assurez-vous que Node est installé sur votre système.

### Étape 2 : Établir un point d'accès côté serveur.

Maintenant, vous devrez créer un fichier nommé `server.js` ou un autre point d'entrée similaire pour le serveur.

Importez les modules requis, tels que le module `ReactDOMServer` et vos composants React. Voici les commandes pour faire cela :

```javascript
import express from 'express';
import React from 'react';
import ReactDOMServer from 'react-dom/server';
import App from './App'; // Importez votre composant React principal
```

### Étape 3 : Configurez votre port pour votre projet.

Établissez un port pour accéder à votre projet dans votre `server.js` en saisissant le code suivant :

```javascript
const PORT = process.env.PORT || 3000;
app.listen(PORT)
```

Maintenant, vous pourrez accéder à ce projet sur `localhost:3000` dans votre navigateur web si Node est installé sur votre système.

### Étape 4 : Établir des routes.

Comme je l'ai mentionné plus haut, si vous n'êtes pas un développeur full-stack, certains de ces concepts peuvent être un peu difficiles à saisir. Pour vous aider, je vais expliquer ce que sont les routes avant de continuer :

#### Que sont les routes ?

Les chemins ou URLs auxquels les utilisateurs peuvent accéder au sein d'une application sont appelés des routes. C'est un concept clé dans le développement d'applications web, car ils aident à spécifier comment le programme réagit aux diverses demandes des utilisateurs. Ils sont également importants pour décider quelle vue ou quel matériel afficher en fonction de l'URL ou du chemin particulier demandé.

Les routes sont fréquemment liées à certains chemins d'URL. Par exemple, dans une application de blog, la route "/posts" peut pointer vers une page avec une liste d'articles de blog, tandis que la route "/about" peut pointer vers une page contenant des informations sur le blog.

Maintenant que vous comprenez un peu mieux ce que sont les routes, continuons avec notre exemple de rendu côté serveur dans React.

Dans votre fichier `server.js`, définissez les routes et indiquez quels composants React doivent être rendus pour chacune d'elles :

```javascript
const app = express();

app.get('/', (req, res) => {
  const html = ReactDOMServer.renderToString(<App />);
  res.send(html);
});

// Ajoutez autant de routes que nécessaire
```

### Étape 5 : Gestion des ressources statiques.

Servir des fichiers statiques comme le HTML, le CSS, les images et le JavaScript côté client directement aux clients sans nécessiter de traitement par le serveur est connu sous le nom de "gestion de fichiers statiques" dans Express.js. Sans cela, le serveur ne pourra pas servir correctement vos fichiers au navigateur.

Maintenant, pour garantir que les ressources statiques telles que le CSS, les fichiers d'images, les fichiers de polices, et ainsi de suite, sont servies correctement, vous devrez configurer votre serveur pour gérer ces fichiers.

Pour ce faire, assurez-vous de créer un dossier avec vos préférences de nommage et d'y ajouter les fichiers. Ensuite, utilisez le code ci-dessous pour faire savoir à Express.js que les fichiers statiques sont situés dans ce dossier spécifique.

Donc, dans `server.js`, écrivez le code suivant :

```javascript
app.use(express.static('public')); // Remplacez 'public' par votre répertoire de ressources statiques
```

### Étape 6 : Lancez votre serveur.

Démarrez votre serveur pour voir le SSR en action en exécutant `node server.js` dans le terminal.

Allez sur [http://localhost:3000](http://localhost:3000) (ou le port que vous avez défini) pour voir votre application React rendue côté serveur.

Note : Selon les exigences et la structure de votre projet, l'implémentation peut différer de ce schéma de base. Pour des applications plus complexes, Next.js et d'autres frameworks similaires offrent une abstraction de plus haut niveau pour le rendu côté serveur avec React.

Maintenant, regardons d'autres fonctionnalités qui aident au SEO lors de l'utilisation de React.

## Comment implémenter le Lazy Loading dans React

### Qu'est-ce que le Lazy Loading ?

Dans React, le lazy loading est la pratique consistant à attendre pour charger des composants ou des ressources spécifiques jusqu'à ce qu'ils soient réellement nécessaires. Lors de travaux sur des applications volumineuses et complexes, où le chargement de tous les composants en même temps peut ralentir le chargement initial de la page, cela peut grandement améliorer la vitesse d'une application React.

Le lazy loading dans un contexte React est fréquemment connecté au composant `Suspense` et à la méthode `React.lazy`. À l'aide de cette fonctionnalité, vous pouvez charger des composants de manière asynchrone, ce qui signifie qu'ils ne sont récupérés et affichés que lorsque l'écran est prêt à les afficher.

J'ai écrit un article complet sur l'utilisation de React Suspense et du lazy loading, vous pouvez le [consulter ici](https://www.freecodecamp.org/news/react-suspense/) – mais nous allons tout de même parler un peu de ces concepts clés ici.

### Étape 1 : Comment utiliser `React.lazy`

`React.lazy` rend possible le code splitting. Le code splitting consiste à diviser votre code JavaScript en plusieurs fichiers afin qu'ils puissent être chargés séparément par le navigateur. Cela permet des imports de composants efficaces, ce qui réduit la taille initiale du bundle en ne chargeant les composants que lorsqu'ils sont nécessaires.

La récupération et le rendu asynchrones des composants améliorent l'efficacité. C'est également particulièrement utile dans les grandes applications aux interfaces utilisateur complexes pour réduire les temps de chargement initiaux.

Vous pouvez charger un composant en différé en utilisant la méthode `React.lazy`. Une fonction qui renvoie une instruction `import()` dynamique est requise. Voici le code :

```jsx
const MyLazyComponent = React.lazy(() => import('./LeoComponent'));
```

### Étape 2 : Comment utiliser `Suspense`

`Suspense` est un composant React utilisé pour gérer les opérations asynchrones dans les composants. Il vous permet de "suspendre" le rendu jusqu'à ce qu'une ressource, telle que des données ou un composant, soit prête. Cela améliore l'expérience utilisateur et simplifie la gestion des tâches asynchrones dans les applications React.

Le composant chargé en différé est enveloppé dans le composant `Suspense`. Il vous permet de fournir un contenu de secours (comme un indicateur de chargement) qui apparaît pendant que le composant en lazy loading se charge. Voici le code pour cela :

```jsx
import { Suspense } from 'react';

const MyLazyComponent = React.lazy(() => import('./LeoComponent'));

function MyLazyComponentWrapper() {
  return (
    <Suspense fallback={<div>Chargement...</div>}>
      <MyLazyComponent />
    </Suspense>
  );
}
```

Combiner le lazy loading avec le code splitting est une méthode qui divise un énorme bundle JavaScript en morceaux plus petits et plus faciles à gérer. Le code splitting accélère le temps de chargement initial d'une application en garantissant que seul le code requis pour la vue actuelle est chargé.

Lorsqu'il s'agit de booster la vitesse des applications avec plusieurs routes ou vues, le lazy loading est particulièrement utile. Vous pouvez minimiser la charge utile initiale et améliorer l'expérience utilisateur globale—particulièrement pour les utilisateurs ayant des connexions réseau plus lentes—en chargeant les composants uniquement lorsque cela est nécessaire.

Il est important de noter que seules les versions de React 16.6 et ultérieures permettent le lazy loading. Le lazy loading améliore considérablement le temps de chargement initial de la page, alors parlons maintenant de la façon dont la vitesse de chargement de la page affecte les classements SEO.

### Comment la vitesse de chargement des pages affecte-t-elle le classement SEO ?

Google, en particulier, prend en compte la vitesse et la fonctionnalité d'un site web lors de la détermination de son classement.

Parlons de quelques manières dont la vitesse de chargement des pages affecte les classements des moteurs de recherche :

#### UX, ou expérience utilisateur

Offrir aux gens une excellente expérience est quelque chose que Google prend très au sérieux. Les pages qui se chargent lentement pourraient offrir aux utilisateurs une mauvaise expérience, ce qui augmente les taux de rebond et diminue la satisfaction des utilisateurs.

Des chargements de pages plus rapides mènent à une meilleure expérience utilisateur (UX), ce qui peut à son tour booster les résultats SEO puisque les moteurs de recherche récompensent les sites web qui satisfont les utilisateurs.

#### Taux de rebond

Les pages qui se chargent lentement ont fréquemment des taux de rebond plus élevés (c'est-à-dire le nombre de fois où les visiteurs quittent un site web rapidement). Les moteurs de recherche sont alertés par des taux de rebond élevés lorsque les utilisateurs ne sont pas satisfaits de l'expérience ou du contenu.

Des taux de rebond réduits peuvent être interprétés par les moteurs de recherche comme un signe de contenu intéressant et pertinent, ce qui pourrait améliorer les classements SEO.

#### Budget d'exploration (Crawl budget)

Chaque site web possède un budget d'exploration que les robots des moteurs de recherche utilisent pour décider de la fréquence et du nombre de pages à explorer. Les pages qui se chargent lentement consomment plus de budget d'exploration, ce qui pourrait entraîner une indexation incomplète du site web.

Une visibilité accrue du site web dans les résultats de recherche est le résultat de chargements de pages plus rapides, qui permettent aux robots des moteurs de recherche d'explorer et d'indexer efficacement plus de pages dans le budget d'exploration alloué.

#### Réactivité mobile

Google utilise désormais la version mobile d'un site web pour le classement, ce que l'on appelle l'"indexation mobile-first". L'un des aspects les plus cruciaux de l'indexation mobile-first est la vitesse de chargement des pages sur les appareils mobiles.

Les sites web adaptés aux mobiles ou responsives sont plus susceptibles de bien se classer dans les résultats de recherche globaux et ont un chargement plus rapide sur les pages mobiles.

#### Signaux Web essentiels (Core Web Vitals)

Google a publié une collection d'indicateurs de performance appelés Core Web Vitals, qui incluent le First Input Delay (FID), le Cumulative Layout Shift (CLS) et le Largest Contentful Paint (LCP). Ces mesures se concentrent sur les éléments liés à l'interaction et à la vitesse de chargement des pages.

Google accorde une priorité plus élevée aux sites web qui respectent ou dépassent les exigences des Core Web Vitals, et ces sites peuvent voir une augmentation de leurs classements de recherche.

Voici les manières dont la vitesse de chargement des pages affecte le classement de recherche. Parlons d'autres moyens d'améliorer le SEO dans votre application React.

## Comment optimiser les images dans React

Un composant essentiel du SEO est l'optimisation des images, qui améliore considérablement l'expérience utilisateur et booste les classements dans les moteurs de recherche.

Des chargements de site web plus rapides sont le résultat d'images optimisées, et les algorithmes de SEO en tiennent compte. Les sites web avec des pages à chargement rapide sont privilégiés par les moteurs de recherche comme Google car ils améliorent l'expérience utilisateur et abaissent les taux de rebond.

Vous devrez spécifier les dimensions des images, choisir des formats de fichiers appropriés (WebP offre une compression supérieure) et compresser les images sans sacrifier la qualité. Ces techniques réduisent la taille des fichiers d'images, ce qui accélère les téléchargements et améliore les performances globales des sites web.

### Techniques d'optimisation des images dans React

#### Compresser les images

Vous pouvez utiliser des méthodes de compression d'images pour réduire les fichiers sans perdre beaucoup de qualité. Cela accélère le chargement des pages, ce qui est important pour le SEO. La compression est facilitée par plusieurs ressources en ligne et programmes d'édition d'images.

Il existe plusieurs ressources sur le web que vous pouvez utiliser pour compresser des images pour votre application React, mais je recommande d'utiliser [TinyPNG](https://tinypng.com/). C'est une ressource gratuite pour compresser les WebP, PNG et JPEG – vous pouvez donc simplement vous rendre sur leur site web pour l'essayer.

#### Choisir les formats de fichiers appropriés

Sélectionnez le bon format de fichier en fonction du contenu et du cas d'utilisation. Le JPEG convient aux photographies, tandis que le PNG est idéal pour les images avec transparence. Le WebP est un format émergent connu pour son excellente compression et sa qualité.

#### Rendre les images responsives

Implémentez des techniques d'images responsives, en fournissant différentes tailles d'images en fonction de l'appareil et de la taille d'écran de l'utilisateur. Cela empêche le chargement inutile de grandes images sur de petits écrans, améliorant ainsi les performances mobiles.

Une technique pour rendre les images responsives consiste à mettre la propriété CSS `max-width` à 100 % et à s'assurer que les images se redimensionnent proportionnellement en fonction de la largeur de leur conteneur. Donnons un exemple :

```javascript
const ResponsiveImg = () => {
  return (
    <div>
      <h1>Composant React de Leo</h1>
      <div className="Img-container">
        <img
          src="/images/Leo-image.jpg"
          alt="Mon Image"
          className="responsive-image"
        />
      </div>
    </div>
  );
};

export default ResponsiveImage;
```

Ensuite, dans votre CSS, vous pouvez définir les styles pour l'image responsive :

```css
.Img-container {
  max-width: 100%;
  margin: 0 auto; /* Centrer l'image */
}

.responsive-image {
  width: 100%;
  height: auto;
  display: block; /* Supprimer l'espace supplémentaire sous les images inline */
}
```

#### Utiliser le lazy loading

Essayez de charger les images uniquement lorsque le viewport de l'utilisateur va les inclure en utilisant le lazy loading. En chargeant progressivement les graphiques au fur et à mesure que l'utilisateur fait défiler la page, cette méthode économise de la bande passante et accélère les chargements initiaux de page.

Donnons un exemple d'utilisation du lazy loading pour les images. Regardez le code ci-dessous :

```jsx
import { lazy, Suspense } from 'react';

// Créer un composant chargé en différé pour l'image
const LazyImg = lazy(() => import('./LennyImage'));

// Espace réservé pendant que l'image est en cours de chargement
const LoadingPlaceholder = () => <div>Chargement...</div>;

const App = () => {
  return (
    <div>
      <h1>Votre application React</h1>
      {/* Utiliser Suspense pour gérer le composant chargé en différé */}
      <Suspense fallback={<LoadingPlaceholder />}>
        {/* Rendre le composant d'image chargé en différé */}
        <LazyImg src="path/to/your/image.jpg" alt="Image chargée en différé" />
      </Suspense>
    </div>
  );
};

export default App;
```

Dans ce cas d'utilisation :

1. D'abord, nous avons créé un composant chargé en différé `LazyImg` en utilisant la fonction `lazy`, qui importe dynamiquement le composant quand il est nécessaire.
    
2. Nous avons défini un composant `LoadingPlaceholder` à rendre pendant le chargement de l'image. Autrement dit, si l'image n'est pas prête à être affichée, ce composant est montré à sa place. Ceci est affiché en utilisant la prop `fallback` du composant `Suspense`.
    
3. À l'intérieur du composant `App`, nous avons utilisé le composant `Suspense` pour envelopper le composant `LazyImg` chargé en différé. La prop `fallback` spécifie quoi rendre pendant que l'image est en cours de chargement.
    
4. Les props `src` et `alt` sont transmises au composant d'image chargé en différé. Le chargement réel de l'image est géré par le composant `LazyImg`.
    

#### Employer des images sprites

C'est une technique de développement web où plusieurs images sont fusionnées en un seul fichier image. Ce fichier image unique est connu sous le nom de feuille de sprite (sprite sheet) et peut ensuite être utilisé pour afficher différentes parties de l'image à différents moments, réduisant ainsi le nombre de requêtes au serveur et améliorant les performances.

Dans votre application React, vous pouvez regrouper plusieurs petites images, telles que des boutons ou des icônes, dans un seul sprite d'image. En conséquence, il y a moins de requêtes serveur, ce qui raccourcit les temps de chargement et améliore la fonctionnalité du site web.

#### Activer la mise en cache du navigateur

Configurez la mise en cache des images dans votre navigateur afin que les utilisateurs puissent enregistrer des copies mises en cache localement. Lorsqu'un navigateur obtient des images de son cache local au lieu du serveur, les visites ultérieures sur la même page se chargent rapidement.

Passons en revue les étapes à suivre pour implémenter la mise en cache du navigateur dans React.

Tout d'abord, vous devrez utiliser Express une fois de plus. Pour ce faire, vous devez configurer le serveur pour inclure les en-têtes de cache appropriés.

**Étape 1 :** Assurez-vous d'avoir Express.js installé dans votre projet. Si ce n'est pas le cas, installez-le en ouvrant votre terminal avec Ctrl + backtick (`) et en saisissant la commande `npm install express`.

**Étape 2 :** Créez un fichier serveur Express.js (par exemple, `server.js`) pour servir votre application React, servir les fichiers statiques et gérer les routes.

```javascript
const express = require('express');
const path = require('path');
const app = express();

// Servir les fichiers statiques, y compris les images, depuis le répertoire 'public'
app.use(express.static(path.join(__dirname, 'public'), { maxAge: '30d' }));

// Gérer les autres routes (ex: routes React)
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Démarrer le serveur
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Le serveur tourne sur http://localhost:${PORT}`);
});
```

En utilisant l'option `maxAge` réglée sur `'30d'`, cela indique que le navigateur doit mettre en cache les images pendant 30 jours. Ajustez cette valeur en fonction de vos besoins spécifiques.

**Étape 3 :** Placez vos images dans le répertoire 'public'. Par exemple, si vous avez une image nommée `Leo-Image.jpg`, mettez-la dans le répertoire 'public/images'.

**Étape 4 :** Incluez l'image dans votre composant React et référencez-la avec des chemins relatifs en vous assurant d'avoir rendu l'image correctement.

```jsx
import React from 'react';

const LeosComponent = () => {
  return (
    <div>
      <h1>Composant React de Leo</h1>
      <img src="/images/Leo-Image.jpg" alt="Image de Leo" />
    </div>
  );
};

export default LeosComponent;
```

**Étape 5 :** Examinez les requêtes réseau à l'aide des outils de développement du navigateur pour vous assurer que les en-têtes de mise en cache sont définis de manière appropriée. Recherchez les en-têtes HTTP qui indiquent la stratégie de cache, tels que Expires et Cache-Control.

Cette configuration devrait garantir que les photos sont stockées dans le cache du navigateur pour la durée allouée, améliorant l'efficacité en réduisant le nombre de téléchargements d'images inutiles lors des visites ultérieures. Adaptez les autres variables et la durée du cache aux besoins de votre application.

L'incorporation de ces techniques d'optimisation d'images booste non seulement les performances du site web, mais impacte également positivement les classements SEO. En priorisant une livraison d'images efficace et en améliorant l'expérience utilisateur, les sites web peuvent atteindre des temps de chargement plus rapides, des taux de rebond réduits et une meilleure visibilité dans les résultats des moteurs de recherche.

Maintenant, discutons des outils que nous pouvons utiliser pour mesurer la performance des images.

### Outils pour mesurer la performance des images

Il existe plusieurs outils pour mesurer la performance des images sur vos applications web. Nous allons discuter de six de ces outils qui aident les développeurs web à comprendre comment les images affectent le temps de chargement et l'expérience utilisateur :

1. Google [PageSpeed insights](https://developers.google.com/speed/docs/insights/v5/about) : Avec un outil appelé PageSpeed Insights, Google évalue le contenu d'une page web et propose des suggestions d'amélioration. Il offre des conseils complets sur l'optimisation des images et crée un score de performance en évaluant plusieurs facteurs. Vous pouvez en apprendre beaucoup sur l'impact de vos images sur le temps de chargement à l'aide de cet outil. Pour utiliser Google PageSpeed Insights, cliquez sur ce lien [https://pagespeed.web.dev/](https://pagespeed.web.dev/) et saisissez le nom de votre site web ; c'est aussi simple que cela. Une fois cela fait, un groupe de nombreuses métriques s'affichera pour vous permettre d'analyser les performances de votre site.
    
2. [Lighthouse](https://github.com/GoogleChrome/lighthouse) : Lighthouse est un outil automatique et open-source pour améliorer la qualité des pages web. Grâce à son intégration dans les outils de développement Chrome, il propose des audits approfondis qui intègrent des métriques liées à la vitesse des images. Lighthouse fournit des informations sur la manière d'améliorer les performances globales de la page et d'optimiser les images.
    
3. [WebPageTest](https://www.webpagetest.org/) : WebPageTest vous donne des aperçus détaillés sur une gamme de mesures de performance, y compris l'optimisation des images, et vous permet de tester la fonctionnalité d'un site web depuis plusieurs emplacements. Il fournit des graphiques en cascade (waterfall) qui illustrent l'ordre de chargement des ressources et indiquent les zones nécessitant des améliorations. Pour utiliser WebPageTest, rendez-vous sur [https://www.webpagetest.org/](https://www.webpagetest.org/) et saisissez l'URL de votre site web.
    
4. [Pingdom tools](https://tools.pingdom.com/) : Le test de vitesse de site web fourni par Pingdom Tools met en lumière plusieurs indicateurs de performance, y compris le temps nécessaire au chargement des images. Il offre une note de performance et indique les domaines qui pourraient nécessiter un travail d'optimisation. Pingdom tools propose également des tests depuis différents emplacements. Pour utiliser Pingdom tools, rendez-vous sur [https://tools.pingdom.com/](https://tools.pingdom.com/) et insérez l'URL de votre site web.
    
5. [ImageOptim](https://imageoptim.com/mac) : ImageOptim est une application de bureau macOS qui vous permet de redimensionner et d'optimiser les photos manuellement. Elle utilise de nombreux algorithmes d'optimisation et prend en charge une gamme de formats d'images sans sacrifier la qualité. Pour utiliser ImageOptim, rendez-vous sur [https://imageoptim.com/mac](https://imageoptim.com/mac) et téléchargez l'application.
    
6. [TinyPNG](https://tinypng.com/) et [TinyJPG](https://tinyjpg.com/) : Nous avons déjà parlé de TinyPNG. Vous pouvez optimiser et réduire la taille des photos PNG et JPEG avec TinyPNG et TinyJPG, deux applications web. Ces programmes minimisent la taille des fichiers sans sacrifier la qualité visuelle en utilisant des algorithmes de compression de pointe.
    

#### Comment exécuter Lighthouse sur les outils de développement Chrome :

1. Assurez-vous d'avoir Google Chrome installé.
    
2. Une fois Chrome installé, ouvrez-le et exécutez la commande `Ctrl+shift+i`.
    
3. Les outils de développement Chrome devraient s'ouvrir. Naviguez jusqu'à la section Lighthouse ; si vous ne la voyez pas immédiatement, reportez-vous à l'image ci-dessous pour naviguer jusqu'à l'outil Lighthouse. Analysez l'URL que vous avez insérée dans votre barre de recherche pour générer un rapport Lighthouse.
    

![Navigation dans les outils de développement Chrome](https://www.freecodecamp.org/news/content/images/2024/01/chrome-dev-tools-navigation-image.png align="left")

4. Vous y verrez tous les problèmes associés à votre page web, y compris la performance des images.
    

Avec ces métriques, vous pouvez comprendre et apprendre les problèmes de SEO auxquels votre application React pourrait être confrontée et les résoudre.

Continuons notre voyage pour améliorer le SEO dans votre application React en parlant de la façon d'utiliser les métadonnées dans votre application React.

## Comment incorporer des métadonnées pour le SEO dans votre application React

### Que sont les métadonnées dans React et comment affectent-elles le SEO ?

Les métadonnées dans React désignent les informations et les contextes supplémentaires qui sont transmis à une page web concernant le contenu.

Les métadonnées donnent aux moteurs de recherche des informations sur le contenu d'un site web ou d'une application web et améliorent la manière dont les pages sont indexées et affichées dans les résultats de recherche. C'est crucial pour améliorer l'optimisation des moteurs de recherche (SEO).

Dans les applications React, les types de métadonnées courants incluent :

1. Balises de titre (Title Tags) : Dans un document HTML, l'élément `<title>` donne le titre de la page, qui est affiché sur l'onglet du navigateur et dans les résultats des moteurs de recherche. Les balises de titre dans les applications React peuvent être mises à jour dynamiquement en fonction du contenu présenté.
    
2. Méta descriptions : La propriété description de l'élément `<meta>` offre un bref aperçu du contenu de la page. Des méta descriptions bien écrites peuvent améliorer les taux de clics dans les résultats de recherche et donner aux moteurs de recherche une meilleure idée de la pertinence de la page.
    

En HTML, les méta descriptions sont incluses dans la section `<head>` d'une page web. Voyons quelques exemples de la manière dont les méta descriptions peuvent être implémentées en utilisant HTML :

1. Méta description basique :
    

```html
<head>
    <meta name="description" content="Votre description brève et convaincante va ici.">
</head>
```

2. Utilisation de React Helmet dans React.js :
    

```javascript
import { Helmet } from 'react-helmet';

const LeoComponent = () => {
    return (
        <div>
            <Helmet>
                <meta name="description" content="Votre méta description va ici." />
            </Helmet>
            {/* Reste de votre composant */}
        </div>
    );
};

export default LeoComponent;
```

3. Balises Open Graph (OG) : Les balises Open Graph, largement utilisées sur des sites comme Facebook, permettent aux développeurs React de gérer l'apparence du matériel lorsqu'il est partagé sur les réseaux sociaux. Elles contiennent des informations telles que le titre, la description, l'image et le type de contenu.
    

Voici un exemple d'utilisation des balises Open Graph dans React :

```javascript
import { Helmet } from 'react-helmet';

const LeoComponent = () => {
    // Données pour les balises Open Graph
    const ogData = {
        title: 'Le titre de votre page',
        description: 'Description du contenu de votre page.',
        url: 'https://www.votre-site-web.com',
        image: 'https://www.votre-site-web.com/og-image.jpg',
        siteName: 'Le nom de votre site web',
    };

    return (
        <div>
            <Helmet>
                {/* Balises méta Open Graph */}
                <meta property="og:title" content={ogData.title} />
                <meta property="og:description" content={ogData.description} />
                <meta property="og:url" content={ogData.url} />
                <meta property="og:image" content={ogData.image} />
                <meta property="og:site_name" content={ogData.siteName} />
                {/* Vous pouvez ajouter d'autres balises Open Graph si nécessaire */}

                {/* Autres balises méta standard */}
                <meta name="description" content={ogData.description} />
                {/* Autres balises méta si nécessaire */}
            </Helmet>
            {/* Reste de votre composant */}
        </div>
    );
};

export default LeoComponent;
```

Dans cet exemple :

* `og:title` : Spécifie le titre de votre page.
    
* `og:description` : Spécifie la description du contenu de votre page.
    
* `og:url` : Spécifie l'URL canonique de votre page.
    
* `og:image` : Spécifie l'URL d'une image représentant votre page. Elle est souvent utilisée comme image d'aperçu lors d'un partage sur les réseaux sociaux.
    
* `og:site_name` : Spécifie le nom de votre site web.
    

N'hésitez pas à personnaliser les valeurs de l'objet `ogData` selon le contenu de votre page et vos besoins spécifiques. De plus, vous pouvez inclure d'autres balises Open Graph si nécessaire pour votre cas d'utilisation particulier.

4. Balises canoniques (Canonical Tags) : Lorsque plusieurs URL pointent vers des informations similaires ou identiques, les balises `<link>` avec la propriété `rel="canonical"` aident à prévenir les problèmes de contenu dupliqué en désignant l'URL préférée. En termes simples, les balises canoniques sont des balises HTML qui aident les moteurs de recherche à comprendre la version préférée d'une page web lorsque plusieurs versions avec un contenu similaire existent.
    

Voici un exemple de balise canonique dans React.js utilisant React Helmet :

```javascript
import { Helmet } from 'react-helmet';

const LeoComponent = () => {
    // URL canonique pour la page
    const canonicalUrl = 'https://www.votre-site-web.com/votre-page';

    return (
        <div>
            <Helmet>
                {/* Balise canonique */}
                <link rel="canonical" href={canonicalUrl} />

                {/* Autres balises méta standard */}
                <meta name="description" content="Description du contenu de votre page." />
                {/* Autres balises méta si nécessaire */}
            </Helmet>
            {/* Reste de votre composant */}
        </div>
    );
};

export default LeoComponent;
```

Dans cet exemple, la balise `link` avec l'attribut `rel="canonical"` est utilisée pour spécifier l'URL canonique de la page. L'attribut `href` contient l'URL préférée que les moteurs de recherche doivent considérer comme la version faisant autorité.

Il est crucial de définir la balise canonique sur toutes les versions d'une page ayant un contenu similaire pour indiquer la version préférée. Cela aide les moteurs de recherche à consolider la valeur SEO et à éviter toute confusion sur la version à indexer. Ajustez la variable `canonicalUrl` en fonction des URL spécifiques de vos pages.

Ainsi, les métadonnées ont un impact sur le SEO en raison de leur capacité à influencer les classements dans les moteurs de recherche, les taux de clics et l'engagement des utilisateurs.

Des métadonnées bien optimisées donnent une description claire et succincte du contenu de la page, augmentant la probabilité qu'elle soit révélée lors de recherches pertinentes. De plus, des informations correctes et intéressantes encouragent les visiteurs à cliquer sur les résultats de recherche, ce qui améliore les performances SEO globales d'une application React.

### Bonnes pratiques pour les métadonnées dans React

Construire des métadonnées solides et efficaces dans React, incorporer des données structurées et utiliser un schema markup sont toutes des procédures très importantes dans l'optimisation pour les moteurs de recherche.

Ces actions améliorent considérablement la façon dont le contenu est présenté et localisé dans les pages de résultats des moteurs de recherche (SERP). Elles aident également les moteurs de recherche à comprendre le contexte d'une page web.

Voici quelques façons d'améliorer les métadonnées dans votre application React :

#### Définir dynamiquement les balises de titre

Utilisez la capacité de React à définir dynamiquement les balises de titre en réponse au contenu présenté. Écrivez des titres clairs et pertinents qui résument de manière appropriée les informations de la page.

#### Méta descriptions optimisées

Écrivez des méta descriptions qui, en pas plus de 150–160 caractères recommandés, résument succinctement le contenu de la page. Incorporez des mots-clés pertinents pour renforcer votre présence dans les résultats de recherche.

#### Utilisation de mots-clés stratégiques

Incluez des mots-clés cruciaux dans les métadonnées d'une manière qui fait sens pour le contenu de la page. Évitez le bourrage de mots-clés (keyword stuffing) et assurez-vous que les métadonnées résument de manière appropriée le contenu de la page.

#### Balises méta responsives

Utilisez des balises méta responsives pour vous assurer que le contenu s'affiche de manière optimale et cohérente sur différents types d'appareils. C'est privilégié par les moteurs de recherche et essentiel pour une expérience utilisateur fluide.

#### Utiliser les balises OG

Utilisez les balises OG pour gérer la façon dont le matériel s'affiche lorsqu'il est partagé sur les réseaux sociaux. Cela améliore la manière dont les liens sont affichés visuellement sur des sites de réseaux sociaux comme Facebook, Twitter et LinkedIn.

### Comment optimiser les métadonnées avec le Schema Markup

#### Qu'est-ce que le Schema Markup ?

Le schema markup peut également être appelé données structurées. C'est un code que vous ajoutez à vos pages web pour aider les moteurs de recherche tels que Google, Bing, Yahoo, etc., à mieux comprendre le contenu de votre page web. C'est un moyen de fournir des informations supplémentaires sur votre contenu afin que les moteurs de recherche puissent l'afficher plus efficacement dans les résultats de recherche.

Par exemple, si vous avez une recette sur votre site web, l'utilisation du schema markup vous permet de spécifier des détails tels que les ingrédients, le temps de cuisson et les informations nutritionnelles. Quand quelqu'un cherche une recette, les moteurs de recherche peuvent utiliser ces informations balisées pour afficher des extraits enrichis (rich snippets), montrant non seulement le titre et la méta description mais aussi des détails clés directement dans les résultats de recherche.

Regardons quelques exemples d'utilisation du schema markup dans nos applications React.

#### Employer le format JSON-LD

JSON-LD signifie JavaScript Object Notation for Linked Data. C'est un format d'échange de données léger conçu pour être facile à lire et à écrire pour les humains, et facile à analyser et générer pour les machines.

JSON-LD est également un moyen de structurer les données pour les rendre compréhensibles pour les moteurs de recherche, les robots d'exploration web et d'autres applications.

Dans le cas de notre exemple de site web de recettes ci-dessus, regardons comment nous pouvons implémenter JSON-LD dans React.

```javascript

const RecipePage = () => {
  // Définir les détails de la recette
  const recipe = {
    name: 'Délicieux Gâteau au Chocolat',
    description: 'Une recette de gâteau au chocolat appétissante.',
    recipeIngredient: [
      '2 tasses de farine tout usage',
      '1 tasse de poudre de cacao',
      '1 tasse de sucre',
      '1 tasse de beurre',
      '4 œufs',
    ],
    cookTime: 'PT45M',
    nutrition: {
      '@type': 'NutritionInformation',
      calories: '350 calories par portion',
      servingSize: '1 part',
    },
  };

  return (
    <div>
      <h1>{recipe.name}</h1>
      <p>{recipe.description}</p>
      {/* Rendre d'autre contenu de recette ici */}

      {/* Ajouter le script JSON-LD pour le schema markup */}
      <script type="application/ld+json">
        {JSON.stringify({
          '@context': 'https://schema.org',
          '@type': 'Recipe',
          ...recipe,
        })}
      </script>
    </div>
  );
};

export default RecipePage;
```

Nous avons développé un composant RecipePage dans cet exemple React, qui affiche les données de la recette. À l'intérieur du composant, nous utilisons un