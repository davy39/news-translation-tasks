---
title: Comment maîtriser les défis de codage en entretien d'embauche
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-17T03:33:34.000Z'
originalURL: https://freecodecamp.org/news/conquering-job-interview-code-challenges-v1-0
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/le-tan-nsexDkLGC-c-unsplash.jpg
tags:
- name: challenge
  slug: challenge
- name: code
  slug: code
- name: code challenge
  slug: code-challenge
- name: coding
  slug: coding
- name: coding interview
  slug: coding-interview
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: interview
  slug: interview
- name: Interviewing
  slug: interviewing
- name: JavaScript
  slug: javascript
- name: job
  slug: job
- name: Job Hunting
  slug: job-hunting
- name: Job Interview
  slug: job-interview
- name: learn to code
  slug: learn-to-code
- name: learning to code
  slug: learning-to-code
seo_title: Comment maîtriser les défis de codage en entretien d'embauche
seo_desc: 'By Jonathan Sexton

  As many of you know, I have been applying for a job in web development for a few
  weeks and I thought it would be a good idea to share some of the coding challenges
  I''ve encountered.

  Not only that but I''ll share the ways I went abou...'
---

Par Jonathan Sexton

Comme beaucoup d'entre vous le savent, je postule pour un emploi en développement web depuis quelques semaines et j'ai pensé qu'il serait bon de partager certains des défis de codage que j'ai rencontrés.

Non seulement cela, mais je vais aussi partager les méthodes que j'ai utilisées pour résoudre ces défis. Bien sûr, il existe de nombreuses façons de résoudre ces défis, mais ce sont celles que j'ai choisies. Si vous avez des méthodes différentes, c'est génial et j'adorerais que vous les partagiez avec moi !

Je ne partagerai aucune information identifiable sur les entreprises ou les détails spécifiques du processus d'entretien pour préserver l'intégrité du processus.

Trêve de bavardages, passons à l'action.

## Le Défi

Voici un défi que j'ai reçu récemment et que j'ai réussi à résoudre avec succès :

_**Tâche : Retourner une liste stylisée de base de posts depuis un endpoint en ordre chronologique inverse**_

Pour protéger l'entreprise et leurs informations, je ne partagerai pas l'URL depuis laquelle j'ai récupéré les informations, mais j'utiliserai plutôt un lien générique de [JSONPlaceholder](https://jsonplaceholder.typicode.com/) (une API gratuite et open source pour les développeurs lorsque vous avez besoin de données externes génériques) dans le code ci-dessous.

Voici le HTML avec lequel j'ai commencé pour afficher nos résultats :

![un exemple de code montrant du HTML](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-3.png)
_Modèle HTML de base_

La balise _<ul>_ a un id pour que nous puissions la styliser plus tard dans le processus.

## Récupération des données depuis l'endpoint

D'accord, plongeons dans la partie **JavaScript** de ce défi. D'abord, j'aime définir mes variables de sortie et d'affichage :

![Code JavaScript montrant deux variables déclarées](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-4.png)
_Nos variables utilisées lors de l'affichage du code retourné_

J'utilise _let_ pour la variable _output_ et je la définis à _null_ car nous changerons sa valeur plus tard dans le code. La variable _list_ est déclarée avec _const_ car sa valeur ne changera pas.

![code javascript montrant une fonction fetch](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-12.png)
_Récupération des données depuis l'endpoint_

Dans l'exemple ci-dessus, nous déclarons une [fonction fléchée](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) nommée _getData_ enveloppée dans un bloc [try...catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) (il s'agit d'une syntaxe plus propre et plus facile à utiliser/lire qui _essaie_ du code et _attrape_ les erreurs si elles se produisent — vous verrez également la partie _catch_ ci-dessous). Comme nous récupérons des données de manière asynchrone, nous devons également utiliser [_async/await_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) pour récupérer les données. Il s'agit de la méthode avec laquelle je suis le plus à l'aise, mais je sais qu'il existe de nombreuses autres façons d'obtenir des données depuis un endpoint, alors n'hésitez pas à partager les vôtres :D

Une fois que nous avons déclaré notre variable _data_, la prochaine étape consiste à définir une variable pour convertir les données retournées en un objet JSON afin de les obtenir sous une forme utilisable. Nous faisons cela avec la méthode _[.json()](https://developer.mozilla.org/en-US/docs/Web/API/Body/json)_. Nous attendons également les données car si nous omettions le mot-clé _await_, JavaScript essaierait de convertir la variable _data_ en JSON, mais les données ne seraient pas encore là car elles proviennent d'une API asynchrone.

![un log de console d'un tableau javascript](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-9.png)
_Nos données glorieuses !_

En tant que toute dernière ligne de cette section, nous utilisons _console.log_ pour afficher nos données que nous recevons de l'endpoint de l'API, juste pour nous assurer que nous obtenons tout ce que nous voulions. Nous avons un tableau rempli d'objets. Vous remarquerez également que la clé _published_at_ contient nos dates et qu'elles ne sont pas dans un ordre particulier. Leur format n'est pas non plus un simple nombre à quatre chiffres représentant l'année, ce qui faciliterait leur filtrage en **ordre chronologique inverse**. Nous devons nous en occuper.

## Manipulation de nos données

![code javascript qui copie une variable](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-7.png)
_Création d'une copie de notre variable de données_

Ici, nous déclarons la variable _dataCopy_ qui pointe vers la variable _dataJSON_ mutée en un tableau via l'_[opérateur de décomposition (...)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)_. Essentiellement, nous copions nos données JSON retournées afin de ne pas manipuler l'original (mauvaise pratique) tout en les transformant en un tableau afin de pouvoir itérer dessus.

Ensuite, nous _[trions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)_ le tableau. La méthode de tri est une méthode de tableau extrêmement utile qui placera nos indices de tableau dans l'ordre de notre choix en fonction de la fonction que nous passons à _sort_.

Typiquement, nous pourrions vouloir trier les données en fonction de la valeur (de la plus grande à la plus petite), donc nous soustrayons le paramètre _**a**_ du paramètre _**b**_. Mais comme nous devons afficher nos résultats en **ordre chronologique inverse**, j'ai décidé de produire une nouvelle date (réalisée avec l'opérateur _[new](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)_ et la méthode intégrée de JavaScript _[Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)_ qui crée une nouvelle instance formatée indépendante de la plateforme d'une date. Maintenant, comme _**a**_ et _**b**_ représentent nos objets situés à l'intérieur de nos indices de tableau, nous pouvons accéder aux paires clé/valeur contenues dans ces objets. Ainsi, nous soustrayons _b.published_at_ de _a.published_at_ et cela devrait nous donner nos dates en **ordre chronologique inverse**.

## Affichage des fruits de notre travail

Vous vous souvenez de la variable _output_ que nous avons définie à _null_ tout en haut de notre programme ? Eh bien, c'est maintenant son heure de gloire !

![code javascript montrant une variable de sortie en train de changer](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-10.png)
_Cette variable de sortie mérite maintenant son salaire !_

Plusieurs choses se passent ici. Tout d'abord, nous définissons notre variable _output_ à une nouvelle valeur en mappant sur notre variable _dataCopy_ en utilisant la méthode _[map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)_. Cette méthode retourne un nouveau tableau avec les résultats de l'appel de la fonction fournie une fois pour chaque indice. Le paramètre _item_ représente nos objets à l'intérieur de notre tableau qui a été retourné depuis l'endpoint et a donc accès à toutes leurs propriétés telles que _title_ et _published_at_.

Nous retournons deux éléments de liste avec un _<span>_ à l'intérieur de chacun (à des fins de style), ainsi qu'une chaîne pour les en-têtes **Titre** et **Date de publication**. À l'intérieur de ceux-ci, nous avons nos variables qui utilisent des [littéraux de gabarit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) pour définir le titre et la date pour chaque post.

Ensuite, nous définissons le _[innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)_ de notre variable _list_ égal à celui de notre variable _output_.

Enfin, nous avons l'accolade de fermeture et la gestion des erreurs de notre bloc _try...catch_ ainsi que notre appel de fonction :

![code javascript montrant la gestion des erreurs pour une requête fetch](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-11.png)
_Ce code gérera toute erreur et les affichera dans la console_

## Code final

Voici à quoi ressemble notre code complet maintenant :

![code javascript](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-13.png)
_L'intégralité de notre base de code_

Et voici notre style CSS de base :

![code css montrant le style de base d'un élément](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-14.png)
_Ai-je dit style de base ? Je voulais dire basique :D_

Et voici le résultat de notre travail avec son style très basique :

![une liste de posts en ordre chronologique inverse](https://jonathansexton.me/blog/wp-content/uploads/2019/05/image-15.png)
_N'est-ce pas magnifique ?_

Comme vous pouvez le voir, nous avons accompli ce que nous nous étions fixé et en fait, la liste est en **ordre chronologique inverse**. Hourra !

---

J'espère que vous avez apprécié cette visite guidée de mon processus de réflexion et de la façon dont j'ai résolu ce défi. Bien sûr, il existe de nombreuses façons de compléter cela, alors n'hésitez pas à partager les vôtres avec moi ! Je suis ravi de continuer cette série et publierai un autre article après avoir traversé un autre défi !

De plus, je publie la plupart de mes articles sur de grandes plateformes comme [Dev.to](https://dev.to/jsgoose) et [Medium](https://medium.com/@joncsexton), donc vous pouvez aussi trouver mon travail là-bas. Cet article a été initialement publié sur mon [blog](https://jonathansexton.me/blog) le 27 mai 2019.

Pendant que vous êtes ici, pourquoi ne pas [vous inscrire à ma **Newsletter**](https://jonathansexton.me/blog/). Je promets de ne jamais spammer votre boîte de réception et vos informations ne seront pas partagées avec qui que ce soit/site. J'aime occasionnellement envoyer des ressources intéressantes que je trouve, des articles sur le développement web et une liste de mes nouveaux posts.

Passez une journée formidable remplie d'amour, de joie et de codage !