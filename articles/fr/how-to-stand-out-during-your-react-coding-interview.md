---
title: Entretien de codage React – Comment se démarquer et réussir les défis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-20T18:20:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-stand-out-during-your-react-coding-interview
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/reactinterview.png
tags:
- name: coding interview
  slug: coding-interview
- name: Interview tips
  slug: interview-tips
- name: Job Interview
  slug: job-interview
- name: React
  slug: react
seo_title: Entretien de codage React – Comment se démarquer et réussir les défis
seo_desc: 'By Iva Kop

  As a React developer, I have gone through my fair share of front-end coding interviews.
  Recently, I had the opportunity to experience the process from the other side –
  as an interviewer. Here is what I''ve learned.

  Coding interview usually ...'
---

Par Iva Kop

En tant que développeur React, j'ai passé ma part d'entretiens de codage front-end. Récemmment, j'ai eu l'opportunité de vivre le processus de l'autre côté – en tant qu'interviewer. Voici ce que j'ai appris.

Les entretiens de codage impliquent généralement un processus en plusieurs étapes où les interviewers évaluent tout, des connaissances techniques de base à l'adéquation culturelle. Chaque étape de ce processus est importante et ne doit pas être sous-estimée. Préparez-vous pour tout cela et préparez-vous bien.

Mais il y a une chose qui est au cœur de (presque) chaque entretien React.

Inévitablement, à un moment donné, vous devez construire une application React.

# L'assignation de l'application

Voici une courte liste d'assignations d'applications réelles que j'ai dû compléter pour mes propres entretiens React au fil des ans :

* **Application de support** – une application pour afficher une liste d'employés du support et leurs informations de contact.
* **Application vidéo** – une application où, étant donné une URL de vidéo YouTube, elle l'affiche sur la page. Les utilisateurs peuvent commenter.
* **Application de projets** – une application pour afficher une liste de projets en cours auxquels les utilisateurs peuvent s'abonner et suivre.
* **Application d'articles** – une application pour afficher une liste d'articles où les utilisateurs peuvent laisser des commentaires imbriqués pour chacun.

Ces assignments sont, à bien des égards, très similaires les unes aux autres. La raison est qu'elles évaluent le même ensemble de compétences de base en React. Quelles sont ces compétences ? Décomposons-les.

## Compétence d'entretien #1 – Comment construire des interfaces utilisateur avec React

Le travail principal d'un développeur React est de construire et structurer des composants React de manière significative.

Les assignments ci-dessus sont destinées à tester votre capacité à écrire du code de manière modulaire et réutilisable tout en créant des abstractions au bon niveau.

L'objectif principal est que votre application fonctionne bien. Mais, en tant que développeur front-end, on s'attend également à ce que vous construisiez des interfaces utilisateur qui aient également une belle apparence.

La plupart du temps, l'assignment sera accompagné d'un design concret que vous devrez suivre. Si c'est le cas, il est important de s'y tenir de près.

Mais si vous pensez qu'il y a une bonne raison de vous écarter, n'hésitez pas à le faire. Soyez simplement prêt à expliquer pourquoi votre solution est meilleure.

Si aucun design n'est disponible, l'interviewer est probablement intéressé à comprendre si vous pouvez créer des interfaces utilisateur sensées par vous-même. Bien que cela puisse être plus difficile, cela vous donne également l'opportunité de montrer que vous êtes capable de faire des choix conscients en matière de front-end.

**Astuce :** Il est facile de supposer que l'attente est que vous devez construire tous les composants à partir de zéro. Utiliser une bibliothèque de composants tierce peut sembler tricher dans un contexte d'entretien. Mais ce n'est pas le cas !

Assurez-vous de demander à l'avance ce qui est attendu. Tirer parti de bibliothèques de composants comme [MaterialUI](https://material-ui.com/) ou [ChakraUI](https://chakra-ui.com/) est un gain de temps énorme pendant les assignments d'entretien et vous permettra de vous concentrer sur des parties plus intéressantes de l'application.

## Compétence d'entretien #2 – Gestion d'état dans React

Un autre défi important lors de la construction d'applications React est la gestion d'état. Il existe une myriade de façons de procéder en fonction de votre cas d'utilisation concret et de vos objectifs. Consultez [mon article](https://blog.whereisthemouse.com/how-to-think-about-react-state-management) sur le sujet si vous êtes curieux d'en savoir plus.

Quelle que soit l'approche que vous choisissez, ce qui est important lors d'une assignment d'entretien est de montrer à l'interviewer que vous comprenez et êtes capable de raisonner sur la gestion d'état.

Votre solution doit avoir du sens sans être excessivement complexe ou alambiquée. Soyez prêt à expliquer et défendre vos choix.

**Astuce :** Il est bon de faire correspondre votre solution de gestion d'état à celle utilisée par l'entreprise pour laquelle vous passez l'entretien.

Utilisent-ils Redux ? Alors n'hésitez pas à inclure Redux dans votre projet. S'intéressent-ils aux machines à états ? Alors xState est votre ami, et ainsi de suite. Assurez-vous de demander à l'interviewer à l'avance ce qu'ils aimeraient voir implémenté dans votre projet.

## Compétence d'entretien #3 – Récupération de données dans React

En tant que développeur front-end, on ne s'attend généralement pas à ce que vous construisiez votre propre back-end. Mais l'assignment qui vous est donné impliquera probablement une forme de récupération de données – probablement soit via une API simulée de quelque sorte, soit simplement un fichier JSON avec les données nécessaires.

Cette partie de l'assignment est destinée à tester si vous, en tant que développeur front-end, savez comment communiquer avec le back-end. Pouvez-vous obtenir, afficher et mettre à jour les données que vous recevez du back-end correctement ? Comprenez-vous comment fonctionnent les requêtes API ?

Dans un cadre plus avancé, il pourrait y avoir une conversation sur l'architecture de récupération de données, la gestion de l'état des données et la mise en cache front-end.

**Astuce :** Faites un effort pour implémenter un mécanisme de récupération de données semi-réaliste dans votre application. Si vous recevez un fichier JSON, n'importez pas directement les données dans vos composants. Utilisez plutôt `fetch` ou une autre approche plus avancée (de préférence asynchrone) pour l'obtenir afin de pouvoir démontrer votre compréhension plus approfondie.

## Compétence d'entretien #4 – Routage dans React

La plupart du temps, créer un projet React est synonyme d'application à page unique. Il est donc possible que l'assignment implique la mise en œuvre d'une solution de routage.

Ici, l'objectif est de démontrer que vous comprenez les bases du routage côté client et êtes capable de structurer votre application autour de celui-ci.

**Astuce :** Évitez de créer votre propre implémentation de routage côté client, sauf si cela est explicitement requis. Opter pour [React Router](https://reactrouter.com/) ou [Reach Router](https://reach.tech/router/) est un choix parfaitement acceptable.

# Comment se démarquer lors d'un entretien React

Avoir une bonne maîtrise des bases discutées ci-dessus est un must et c'est un bon début pour marquer des points lors d'une assignment d'entretien. Mais pour vraiment se démarquer, vous devez aller plus loin.

Voici comment.

## Comprendre votre installation

La plupart du temps, vous pouvez vous en sortir en utilisant des chaînes d'outils comme Create React App (ou similaires) lors de la construction d'un projet React pour un entretien. Cela vous aidera à démarrer et à gagner du temps.

En fait, il est important d'utiliser ces outils afin de consacrer votre temps au développement significatif plutôt qu'à la configuration.

Mais il est également important de comprendre et d'être capable d'expliquer les outils de base que vous utilisez. Lors d'un entretien React, attendez-vous à ce qu'on vous pose des questions sur [Webpack](https://webpack.js.org/) et [Babel](https://babeljs.io/), par exemple.

Mais ce qui peut vraiment vous donner un avantage, c'est si vous ne comprenez pas seulement mais êtes capable d'améliorer votre configuration existante. Une idée serait d'ajouter un linter ([eslint](https://eslint.org/)) et un formateur ([prettier](https://prettier.io/)) à votre application. Cela montre que vous vous souciez vraiment de la qualité et de la cohérence du code.

Une autre idée serait d'aller encore plus loin et de configurer des hooks pré-commit ([husky](https://github.com/typicode/husky)) qui lintent et formatent votre code à chaque commit. Fou, je sais !

Ces outils prennent quelques minutes à configurer mais peuvent sembler une étape supplémentaire impressionnante aux yeux d'un interviewer.

## Testez votre code

Très peu d'assignments indiqueront explicitement que des tests sont requis. Pour cette raison, de nombreux développeurs supposent que les tests ne font pas partie de la tâche et les ignorent complètement. C'est faux !

La plupart du temps, un interviewer sera impressionné de voir que vous comprenez l'importance de tester votre code. C'est un moyen très facile mais puissant de vous démarquer.

Il n'est pas nécessaire d'avoir un test pour chaque ligne de code dans votre projet. Plusieurs tests stratégiquement sélectionnés couvrant la logique plus compliquée devraient faire l'affaire.

## Ne négligez pas la réactivité

Voici un autre aspect de votre assignment React qui n'est pas explicitement mentionné la plupart du temps – la réactivité.

Même si vous recevez un design au début de la tâche, presque toujours il ne sera pas réactif. C'est à vous de vous soucier suffisamment de la réactivité pour la comprendre par vous-même.

Comme pour les tests, la plupart des développeurs ignoreront simplement la réactivité. Ce qui est une bonne nouvelle pour vous – cela vous donne l'opportunité de briller !

Il n'est pas nécessaire que l'implémentation soit parfaite et fonctionne sans faille sur chaque écran et appareil. Le simple fait que ce soit quelque chose auquel vous avez pensé dans votre processus de développement devrait suffire à vous rapporter des points majeurs.

## Améliorez l'accessibilité

L'accessibilité est une préoccupation majeure pour la plupart des produits web modernes. Prendre même de petites mesures pour améliorer l'accessibilité de votre projet, comme ajouter du texte `alt` à vos images, par exemple, peut laisser une très bonne impression.

L'accessibilité est également une autre raison pour laquelle vous pourriez vouloir choisir une bibliothèque de composants tierce lors de la construction de votre assignment. La plupart des composants de ces bibliothèques sont accessibles dès la sortie de la boîte.

Rendre votre projet aussi accessible que possible peut vraiment vous démarquer lors d'un entretien. Mais ce qui est plus important, l'accessibilité devrait être (et devient) la norme dans le développement web. Assurez-vous que votre futur employeur sache que vous comprenez cela.

## Les détails comptent

Tout dans votre code devrait dire à l'interviewer que vous êtes un développeur compétent – des bases comme la façon dont vous nommez et structurez votre code aux petits détails comme les messages de commit.

Étant donné que ces assignments sont généralement réalisées sous des contraintes de temps, il est tentant d'ignorer simplement ces aspects apparemment sans importance. Mais les faire correctement peut vous démarquer de manière significative.

J'espère que cet article est utile pour votre prochain entretien React. Faites-moi savoir comment cela se passe !

[Suivez-moi](https://twitter.com/iva_kop) sur Twitter pour plus de contenu tech.