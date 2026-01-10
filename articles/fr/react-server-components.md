---
title: React Server Components Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-29T20:56:01.000Z'
originalURL: https://freecodecamp.org/news/react-server-components
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/Untitled-design--1-.png
tags:
- name: React
  slug: react
seo_title: React Server Components Expliqués
seo_desc: 'By Mehul Mohan

  Last week, the React team released a new feature called React Server Components
  (RSC). In this article, I would like to give you my perspective on a few aspects
  of RSC.

  Can''t I run React on servers already?

  Yes you can. React has suppo...'
---

Par Mehul Mohan

La semaine dernière, l'équipe React a publié une nouvelle fonctionnalité appelée React Server Components (RSC). Dans cet article, je souhaite vous donner ma perspective sur quelques aspects des RSC.

## Ne puis-je pas déjà exécuter React sur des serveurs ?

Oui, vous pouvez. React prend en charge le rendu côté serveur depuis longtemps en utilisant le package `react-dom/server`, qui est un moteur de rendu React pour le HTML statique à partir de composants React.

Cependant, notez que `react-dom/server` a un travail simple : il prend l'arborescence React et la convertit en balisage HTML statique.

Vous devez réhydrater l'état (en utilisant `ReactDOM.hydrate`), ajouter toute interactivité en utilisant JavaScript côté client, et vous occuper de la navigation, de la mise en cache, et d'un million d'autres choses vous-même.

Des frameworks comme Next.js font déjà beaucoup de travail pour vous, mais c'est une autre histoire.

## En quoi les React Server Components diffèrent-ils du rendu côté serveur ?

Les composants serveur ne sont pas un SSR _complet_. Imaginez un site web React comme une hiérarchie de composants comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/tree.png)

Prenons Next.js comme exemple pour le SSR car c'est le framework SSR le plus courant pour React. Next.js (SSR) vous donne la possibilité de faire ce qui suit :

1. Export statique complet du site sans JS
2. Export statique partiel par page (fonctionnalité expérimentale de Next.js)
3. SSR complet de l'arborescence (puis réhydratation, etc.)
4. Division des composants en utilisant l'import dynamique rendu sur le client en tant que module React.
5. Division des composants en utilisant l'import dynamique rendu sur le serveur en tant que module React.

Pouvez-vous deviner ce qui manque (ou plutôt _ne_ manque _pas_) ici ? Dans les exports statiques de Next, vous ne pouvez pas exporter statiquement un composant à moins de créer une page pour celui-ci.

Et même si vous le faites, vous perdez la capacité d'avoir des mises à jour de données dynamiques déclenchées par une action de l'utilisateur (sauf si vous utilisez un autre serveur d'API backend avec le client, rendant l'UI non-SSR).

Il peut être difficile de le voir maintenant, mais les React Server Components comblent cette lacune. Considérez à nouveau le graphique ci-dessus et les 5 points ci-dessus :

1. L'export statique complet signifie que tous les nœuds dans le graphique ci-dessus sont des documents HTML complets sans JS. Pour l'instant, considérons le nœud `1` comme une seule page, et en supposant qu'il y a plusieurs racines de ce type, toutes les pages sont entièrement basées sur HTML.
2. L'export statique partiel signifie que seule la racine unique (page unique) serait un HTML statique (`1` dans ce cas)
3. Le SSR complet signifie que l'ensemble du site web (ou de la page) est rendu à chaque fois à la demande. Cela implique de rendre la page de haut en bas puis de réhydrater la page avec React (ajoutez une touche de mise en cache aux endroits _coûteux_ si vous le souhaitez)
4. La division des composants en utilisant l'import dynamique rendu sur le client en tant que module React - cela signifie que certains nœuds (par exemple `4` et `7`) ne seront pas rendus sur le serveur et que le code JS brut pour leurs composants sera envoyé sur le réseau, et s'exécutera comme un composant React côté client régulier. Parce que `4` et `7` ne sont pas rendus sur le serveur, cela s'applique automatiquement à leurs enfants également (8, 9, 14).
5. La division des composants en utilisant l'import dynamique rendu sur le serveur en tant que module React - c'est l'approche la plus proche des RSC. Ici, nous divisons le code du composant en différents bundles (chunks), le rendons sur le serveur, et l'envoyons sur le réseau uniquement lorsque le client le demande (par exemple - en tapant dans un champ de recherche ou en cliquant sur un bouton).

La question maintenant est, en quoi les RSC diffèrent-ils de l'import dynamique rendu sur le serveur de Next.js ?

## RSC vs Import Dynamique Rendu sur le Serveur

Jusqu'à présent, l'import dynamique rendu sur les serveurs serait toujours téléchargé et utilisé comme des composants React réguliers. Cela signifie que vous devez dépenser quelques cycles CPU sur le chunk dynamique que vous avez obtenu et l'intégrer dans le DOM React côté client.

Les React Server Components pour les clients, eh bien, ne sont pas des composants du tout. Ce sont _autre chose_.

Tout d'abord, vos React Server Components peuvent mettre à jour uniquement une petite partie de l'UI (le composant). Ils diffèrent du SSR typique en ce sens qu'ils n'envoient jamais de HTML statique au premier chargement.

Si vous utilisez React sans SSR mais avec RSC, votre premier chargement ressemblera beaucoup à un React côté client régulier (sans contenu HTML).

Considérons une application qui utilise une barre de recherche pour rechercher des films, liée à une base de données sur votre backend. Supposons que les résultats de recherche sont en fait un React Server Component, et non un composant régulier. Dans le cas d'un composant régulier, voici ce qui pourrait se passer :

1. Dès que vous tapez, une requête `fetch` est faite à une API distante pour une charge utile JSON.
2. Dès que vous obtenez les données, vous les analysez en JSON et les donnez à React.
3. React rend le composant des résultats à partir des données JSON et affiche les informations sur les films.

Assez simple. Avec RSC, voici ce qui se passera :

1. Une requête réseau est faite à un backend que vous possédez et qui est capable de rendre des RSC.
2. Le composant est rendu sur le serveur lui-même (étapes 2 et 3 ci-dessus), et vous recevez une construction de balisage statique des données _dans un format non-JSON/non-HTML pour l'instant_ (cela pourrait changer à l'avenir)
3. Le frontend rend ce balisage en tant qu'_UI statique_ (important : pas en tant que composant React). Cela économise un traitement supplémentaire du composant sur le frontend.

Avec l'import dynamique rendu sur le serveur, eh bien, cela n'a pas beaucoup de sens car votre client ne peut pas dire à votre chunk "d'import dynamique" de rendre une UI dépendante de l'état. Cela est dû au fait que les imports dynamiques ne sont là que pour des raisons de performance.

Lorsque vous utilisez RSC, il y a plusieurs autres choses à noter :

1. Vous ne pouvez pas rendre vos composants serveur interactifs (car ils ne sont que des chunks de mises à jour de l'UI)
2. Vous pouvez, cependant, inclure des composants côté client à l'intérieur de vos composants côté serveur qui pourraient être interactifs et se rendraient comme vous vous y attendez.
3. Votre UI du serveur est automatiquement synchronisée avec l'état côté client car vous ne "détruisez et ne créez" jamais de composants lors de la mise à jour de parties de l'UI vous-même - React le fait pour vous.

## Conclusion

C'est tout ! J'espère que cet article vous aide à comprendre les RSC plus clairement. La technologie est nouvelle et peut être intégrée avec des frameworks comme Next.js. Voyons ce que l'avenir nous réserve.

Vous voulez en savoir plus ? Il y a une très bonne vidéo officielle de 57 minutes de l'équipe React qui plonge en profondeur dans les RSC, démonstration incluse. Vous pouvez la consulter [ici](https://www.youtube.com/watch?v=TQQPAU21ZUw).

Si vous avez aimé l'article, vous pouvez me suivre sur [twitter](https://twitter.com/mehulmpt) pour plus de contenu de ce type :)