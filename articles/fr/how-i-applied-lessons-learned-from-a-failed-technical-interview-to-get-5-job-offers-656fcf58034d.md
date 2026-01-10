---
title: Comment j'ai appliqué les leçons tirées d'un entretien technique raté pour
  obtenir 5 offres d'emploi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-16T08:25:26.000Z'
originalURL: https://freecodecamp.org/news/how-i-applied-lessons-learned-from-a-failed-technical-interview-to-get-5-job-offers-656fcf58034d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4_aEIqKHhYy0FF3b2RuB6g.jpeg
tags:
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment j'ai appliqué les leçons tirées d'un entretien technique raté pour
  obtenir 5 offres d'emploi
seo_desc: 'By Fredrik Strand Oseberg

  It was almost like a dream. I had taken 6 months off to go all in on coding and
  moving to Australia with my girlfriend, when I finally returned to Norway — and
  a job.

  It almost went without a hitch. I had it all. I’ll start ...'
---

Par Fredrik Strand Oseberg

C'était presque comme un rêve. J'avais pris 6 mois de congé pour me consacrer entièrement au codage et déménager en Australie avec ma petite amie, quand je suis finalement retourné en Norvège — et à un emploi.

Tout s'est presque passé sans accroc. J'avais tout. Je vais commencer par vous donner un peu de mon background entrepreneurial.

J'ai passé les 6 derniers mois à travailler sans relâche sur mon portfolio et mes projets personnels. Notamment, j'ai créé [CryptoDasher](https://cryptodasher.com/), un outil pour suivre les cryptomonnaies et les valeurs de portefeuille en temps réel. J'ai également soumis une entrée à un [concours de design web](https://fredrikoseberg.github.io/loopringv2/) pour une entreprise chinoise de blockchain appelée [Loopring](https://loopring.org/).

Je me sentais prêt. J'ai postulé pour un emploi de développeur frontend dans une grande entreprise de conseil en Norvège, et j'ai attiré leur attention — ou du moins, je le pensais.

Après avoir réussi une mission à domicile et un premier entretien, j'ai été invité pour l'entretien technique.

L'événement principal.

J'étais nerveux.

Comment se préparer pour l'entretien technique ? Je me suis demandé. J'ai demandé autour de moi et j'ai fouillé internet comme un fou. J'ai regardé des entretiens simulés sur YouTube. Voici quelques-unes des ressources que j'ai utilisées :

* [Cracking the front-end interview](https://medium.freecodecamp.org/cracking-the-front-end-interview-9a34cd46237) (Article Medium de freeCodeCamp)
* L'avis de David Shariff sur [Preparing for a Front-End Web Development Interview in 2017](http://davidshariff.com/blog/preparing-for-a-front-end-web-development-interview-in-2017/)
* [10 Interview Questions Every JavaScript Developer Should Know](https://medium.com/javascript-scene/10-interview-questions-every-javascript-developer-should-know-6fa6bdf5ad95)
* [Liste de questions d'entretien JavaScript de Toptal](https://www.toptal.com/javascript/interview-questions)
* [Mozilla Developer Network (MDN)](https://developer.mozilla.org/en-US/)
* [Pramp - un outil pour les entretiens simulés avec d'autres](https://www.pramp.com/)
* [Collection de questions pour développeur frontend sur Github](https://github.com/h5bp/Front-end-Developer-Interview-Questions)
* [YouTube JS mock interview #1](https://www.youtube.com/watch?v=UdiXLzBie9g)
* [YouTube JS mock interview #2](https://www.youtube.com/watch?v=057Rs6CgJnY&t=3142s)

J'ai passé des heures et des heures à potasser ce matériel, essayant de me préparer au mieux. Je ne me sentirais pas bien si je ne faisais pas tout ce que je pouvais avant l'entretien, comme je suis sûr que vous comprenez.

Le jour de l'entretien est arrivé.

J'étais rentré chez moi depuis 4 jours. Après un vol de 36 heures depuis l'Australie, je me réveillais encore à 5 heures du matin chaque jour.

Ce jour-là, je me suis réveillé à 4 heures.

Toujours effrayé, mais curieusement, aussi excité.

J'ai rencontré l'interviewer dans le hall de l'entreprise, et nous sommes montés à leurs bureaux.

Nous avons eu une bonne discussion et avons commencé à nous connecter immédiatement. Je suis bon en compétences sociales, alors j'espérais démontrer cette force tôt. Nous avons rencontré un autre interviewer peu après et nous sommes dirigés vers la salle de réunion.

Le début de l'entretien s'est très bien passé. Nous nous sommes présentés, et ils ont commencé à me poser des questions sur mon background. On m'a demandé ce que je pensais être la partie la plus difficile pour commencer à coder, quel type de technologie j'aimerais apprendre, quel type de technologie j'aimerais enseigner aux autres, et ce que je trouve excitant à ce sujet.

À ce stade, je sentais que l'entretien se passait bien. J'étais curieux d'en apprendre davantage sur l'entreprise et je sentais que je m'entendais bien avec mes interviewers.

Puis la partie technique a commencé.

Tout d'abord, on m'a demandé d'expliquer mon code de la mission à domicile. La mission était de créer une pagination pour un ensemble de données et de l'afficher dans une liste. Je l'avais écrit en utilisant React, et j'ai commencé à parcourir le code. Alors que nous parcourions le code, mes interviewers me posaient des questions à ce sujet. Je vais essayer de décrire les questions ci-dessous et ce que je pense que les interviewers recherchaient.

**Sais-tu ce qu'est le test unitaire ? Quelle partie du code pourrait être testée unitairement ?**

En toute honnêteté, je pense que j'ai mal répondu à cette question. Un test unitaire est un morceau de code qui vérifie qu'une unité ou une partie spécifique du code source remplit son objectif sans effets secondaires indésirables. Je ne me souviens pas de ce que j'ai répondu, mais j'ai peut-être confondu avec le test d'intégration. J'avais quelques connaissances sur les tests unitaires et le TDD avant l'entretien, mais dans le feu de l'action, cela a pu m'échapper.

Après quelques discussions, j'ai conclu que je pouvais tester la fonction de pagination, car elle était responsable de la plupart de la logique du programme.

**Comment améliorerais-tu le programme ?**

J'ai trouvé cette question légèrement déconcertante. Lorsque j'ai rendu la mission à domicile (il y a des semaines), on m'avait demandé d'inclure une liste de choses que je pourrais améliorer dans le programme. En supposant que l'interviewer connaissait déjà ces points, j'ai eu du mal à trouver d'autres domaines d'amélioration que ceux que j'avais déjà inclus.

Il est rapidement devenu clair pour moi que l'interviewer était intéressé par les choses que j'avais déjà mentionnées dans mon email, alors j'ai commencé à mentionner tous ces points - la gestion des erreurs, l'optimisation mobile, le retour utilisateur pendant l'appel Ajax, et la gestion des pages en cas de grand ensemble de données.

**Sais-tu ce qu'est BEM ? Est-ce que c'est BEM que tu utilises dans ton code ?**

J'ai répondu que je savais ce qu'est BEM. C'est une convention de nommage pour travailler sur des projets CSS et signifie Block, Element, Modifier. J'ai également répondu que je m'étais inspiré de BEM dans le nommage de mes classes CSS, mais que ce n'était pas exactement BEM, car cela ne suivait pas toutes les règles de BEM.

**Comment rendrais-tu ce site mobile friendly ?**

Les requêtes média CSS. C'est le principal ici. Ils voulaient savoir que je savais comment travailler avec les requêtes média pour rendre les sites réactifs.

Jusqu'à présent, tout va bien. Je sentais que j'avais répondu aux questions de manière assez compétente, bien que j'aie dû discuter des questions un peu avant de comprendre exactement ce que l'interviewer cherchait.

### Le défi de codage

Ensuite, ils m'ont demandé d'étendre la fonctionnalité. On m'a demandé d'implémenter un mécanisme de tri qui prendrait l'ensemble de données paginé et les réorganiserait par nom et par nombres. On m'a donné quelques minutes pour réfléchir au problème.

J'ai posé quelques questions de clarification, comme si je devais utiliser la fonction de tri JavaScript intégrée ou construire la mienne (comme nous le verrons plus tard, ce fut une grosse erreur). Les données paginées existent sous forme de tableau d'objets où chaque objet a un tableau de données avec 20 objets qui représentent chaque élément de la liste. J'ai imaginé l'algorithme suivant :

1. Combiner chaque tableau de données des objets de pagination dans un nouveau tableau.
2. Trier le nouveau tableau
3. Paginator le tableau trié et définir l'état du composant sur le nouveau tableau trié.

C'était un bon algorithme. Et j'ai rapidement compris ce qu'il fallait faire. Le seul problème maintenant était de l'implémenter. Voici où j'ai fait des erreurs.

Tout d'abord, j'ai passé beaucoup trop de temps à trouver comment combiner les tableaux. Je l'admets, je pense que la pression de la situation m'a atteint ici. Parce que j'ai fait toutes sortes de choses bizarres alors que j'aurais pu le résoudre avec un simple reduce. À ma décharge, je n'étais pas aussi à l'aise avec reduce à l'époque que je le suis maintenant.

```js
// Ce que j'aurais dû faire
const pageData = pages.reduce((startingValue, page) => startingValue.concat(page.data), [])
// Ce que j'ai fini par faire
const pages = this.state.pages;
const pageData = [];
pages.forEach(page => pageData = pageData.concat(page.data));
```

Maintenant que j'avais un tableau avec toutes les données, je devais écrire la logique pour les trier. Comme mon expérience en programmation a été largement basée sur la construction de mes propres projets, cela faisait longtemps que je n'avais rien à voir avec la fonction de tri JavaScript. J'ai dû la chercher, et j'ai passé un peu de temps à vérifier MDN et des exemples sur stack overflow pour vraiment la comprendre avant de l'implémenter.

J'ai réussi à faire fonctionner le tri, partiellement. Je suis resté bloqué ici pendant un moment. La plupart des noms dans le tableau étaient triés correctement, cependant en haut il y avait quelques noms qui n'étaient pas dans l'ordre. À ce stade, j'essayais de rester calme, mais dans mon esprit, je paniquais. J'essayais de comprendre pourquoi cela ne triait pas correctement. Et je suis resté bloqué ici plus longtemps que je ne l'aurais voulu.

Après quelques discussions et encouragements des interviewers, je me suis finalement souvenu que les chaînes sont triées par leurs valeurs ASCII. Les lettres majuscules sont valorisées de 65 à 90 et les lettres minuscules de 97 à 122. Les résultats en haut qui n'étaient pas triés correctement avaient une première lettre majuscule, ce qui avait pour effet de les trier en premier, puisque leur valeur ASCII est inférieure à celle des lettres minuscules. **C'est une erreur que je ne referai plus jamais.**

Lorsque le problème a été identifié, je l'ai immédiatement résolu en utilisant .toLowerCase() sur les noms triés.

Il ne restait plus qu'une chose.

Passer les données triées dans la fonction de pagination.

Ici aussi, j'ai rencontré un obstacle.

La fonction de pagination attendait une réponse Ajax et passait chaque élément à une fonction formatData qui décomposait les morceaux pertinents et retournait un nouvel objet. Cependant, lorsque j'ai essayé de passer le nouveau tableau d'objets triés dans cette fonction, il n'avait plus les noms de propriétés originaux et la fonction lançait une erreur.

J'ai passé un peu de temps à travailler sur ce problème avant de comprendre que je devais déplacer formatData hors de la fonction de pagination et l'exécuter sur les données de réponse avant que les données ne soient passées à la fonction de pagination.

Une fois cela et quelques autres modifications mineures effectuées, le code fonctionnait enfin. Cela avait pris un peu de temps, mais finalement, j'ai résolu le problème.

À ce stade, la partie codage de l'entretien technique était terminée.

Et je me sentais épuisé.

Nous avons conclu l'entretien avec un peu plus de discussion. Ils m'ont parlé davantage de leur entreprise, et j'ai posé quelques questions avant de nous séparer.

Cependant, l'entretien ne s'est pas arrêté là.

J'ai contemplé l'entretien, réfléchi à ce que j'avais fait de mal, je suis allé dormir puis je suis allé travailler.

Le lendemain, j'ai passé trois heures à améliorer la solution, puis j'ai envoyé cet email :

> _Bonjour interviewer X et interviewer Y._

> _Je voudrais vous remercier d'avoir accepté de parler avec moi hier. J'ai beaucoup réfléchi à la solution et j'ai décidé de travailler un peu à son amélioration aujourd'hui. J'ai fourni le code d'une version améliorée de ce sur quoi nous avons travaillé hier. Voici ce que j'ai fait :_

> _J'ai étendu la fonctionnalité de tri pour pouvoir inverser le résultat si elle est pressée une seconde fois._

> _J'ai étendu la fonctionnalité de tri à tous les titres._

> _J'ai ajouté des icônes aux en-têtes de tri._

> _J'ai refactorisé la fonction de pagination, appris les bases des tests unitaires, et utilisé Jest pour tester sa fonctionnalité._

> _J'ai ajouté la prise en charge des chaînes de requête pour la pagination afin que le rechargement et le lien montrent les données correctes lors de la visite d'une page différente._

> _J'ai ajouté un style de requête média pour rendre le composant mobile friendly._

> _J'ai ajouté un chargeur à afficher pendant que l'appel API est en cours_

> _J'ai ajouté une gestion des erreurs, avec une opportunité pour l'utilisateur de réinitialiser l'appel API._

> _J'ai changé la fonction de tri sur mobile pour qu'elle fonctionne avec une boîte de sélection._

> _J'ai corrigé l'erreur où une balise d'ancrage enfermait une balise li._

> _Cela aurait peut-être été légèrement excessif, mais j'étais inspiré et je voulais améliorer la solution._

> _Cordialement,_

> _Fredrik Strand Oseberg_

Ce n'était pas suffisant. Mais au moins j'ai fait tout ce que je pouvais. Quelque temps plus tard, j'ai reçu cet email :

> _Bonjour !_

> _Nous aimerions vous remercier pour quelques beaux tours d'entretien, mais nous devons conclure que nous ne vous offrons pas le poste, car vous n'avez pas aspiré à nos attentes dans la partie technique._

> _Nous aimons votre background et croyons que vous pouvez bien vous intégrer dans notre communauté, alors nous vous donnons un retour détaillé sur votre entretien technique, espérant que vous postulerez à nouveau une fois que vous aurez acquis plus d'expérience en programmation._

### Où ai-je fait faux ?

Eh bien, heureusement, j'ai reçu un rapport de feedback détaillé. Alors examinons-le et je vais en discuter avec vous.

#### Morceau de Feedback #1 : « Passe trop de temps à trouver comment combiner des tableaux. Cherche d'abord sur internet au lieu de vérifier la documentation pour JavaScript (par exemple : « js array doc » donnerait w3schools ou mdn, où les fonctions sont listées), et utilise les exemples de manière incorrecte (array.concat retourne un nouveau tableau). Personne ne se souvient de tout dans les APIs, donc être à l'aise avec l'utilisation de la documentation pour JS ou une bibliothèque est important. »

**À retenir :** Les interviewers veulent vous voir atteindre MDN (ou une autre documentation pertinente) en premier. Ils veulent voir que vous pouvez trouver et lire la documentation et l'implémenter en fonction des informations trouvées.

#### Morceau de Feedback #2 : « Dans l'assignation de tri, le candidat suggère d'abord un algorithme manuel bizarre. Heureusement, il choisit d'utiliser la fonction de tri intégrée en JavaScript, mais il n'est pas sûr de son fonctionnement et doit vérifier la documentation à plusieurs reprises. »

**À retenir :** Soyez absolument clair dans votre communication. Dans ce cas, j'ai demandé aux interviewers si je devais utiliser la fonction de tri intégrée en JavaScript ou non, pour clarifier les limites/limites de la tâche à accomplir, et pour démontrer que je ne me suis pas lancé dans le codage sans connaître les termes sous lesquels je fonctionnais. Malheureusement, je pense que cela a été mal interprété comme si je suggérais d'utiliser mon propre algorithme de tri, alors que je n'avais pas l'intention de le faire à moins que ce ne soit spécifiquement ce qu'ils voulaient de la tâche.

Cela a fini par avoir l'effet inverse de ce que je voulais transmettre. Assurez-vous de communiquer clairement ce que vos questions visent à découvrir. Parce qu'elles peuvent avoir un sens parfait pour vous, mais peuvent être perçues différemment par vos interviewers.

#### Morceau de Feedback #3 : « Lorsque le code fonctionne, le texte est trié « sensible à la casse », un scénario classique. »

Malheureusement, le candidat passe beaucoup de temps avant que le problème ne soit compris, mais une fois identifié, il est corrigé immédiatement.

**À retenir :** La vitesse est de l'essence. Les bugs apparaîtront toujours lors de l'écriture de programmes, mais essayez de les résoudre aussi rapidement que possible. Trouvez l'essence du problème et tournez-vous rapidement vers la documentation si vous ne pouvez pas le comprendre.

#### Morceau de Feedback 4 : « A passé du temps à comprendre pourquoi formatData devait être déplacé hors de la pagination lors du refactor. »

**À retenir :** Encore une fois, la vitesse est de l'essence.

#### Morceau de Feedback #5 : « Beaucoup de boucles foreach, où array.map ou array.reduce auraient pu être utilisées. Il serait bénéfique d'en apprendre davantage sur la programmation fonctionnelle. »

**À retenir :** Apprenez array.map, array.filter et array.reduce, et apprenez-les bien. Je me suis plongé dans la programmation fonctionnelle à la suite de cela, et c'est une tâche intimidante. Mais vous n'avez pas besoin de tout apprendre maintenant, assurez-vous simplement de maîtriser les bases.

#### Morceau de Feedback #6 : « J'aurais aimé que le candidat ait plus de connaissances sur les tests unitaires. »

**À retenir :** Cela semble assez évident, mais écrivons-le quelques fois pour bonne mesure : Les tests sont importants. Les tests sont importants. Les tests sont importants. Apprenez-les. Incorporez-les. Utilisez-les.

Le reste du document est élogieux. Je ne vais pas entrer dans autant de détails, car ce n'est pas si important. Mais voici l'essentiel :

* Il utilise bien son éditeur
* Il utilise le débogueur dans Chrome (connaître des outils de débogage avancés est important)
* Il vérifie que les choses fonctionnent avant de passer à autre chose (en utilisant console.log)
* Il essaie de diviser le code en parties logiques plus petites
* Il utilise des variables avec des noms au lieu de commentaires, ce qui rend le code plus lisible.
* Il connaît bien React
* Les projets précédents sont impressionnants
* Possède d'autres qualités positives que la programmation (design/visuel)

### Qu'aurais-je pu faire différemment en préparation ?

Le recul est toujours 20/20. Mais quand on reçoit un non, on passe inévitablement du temps à réfléchir à ce qu'on aurait pu faire différemment.

#### Passer en revue le code de la mission à domicile plus minutieusement.

J'ai passé trop de temps à travailler sur mes connaissances en JavaScript. J'aurais dû passer en revue mon propre code encore plus que je ne l'ai fait. Même si je l'ai écrit, quand quelques semaines passent entre le moment de l'écriture et l'entretien, il faut revenir en arrière et rafraîchir sa mémoire. J'aurais souhaité avoir passé plus de temps sur cela que sur des questions obscures de JavaScript.

#### Faire plus de missions pratiques en JavaScript.

J'ai fait beaucoup de travail théorique en préparation de l'entretien. Maintenant, je souhaite avoir passé plus de temps, ou au moins mélangé, des missions pratiques. Résoudre des algorithmes sur [Hackerrank](https://www.hackerrank.com/) ou [Code Wars](https://www.codewars.com/). Ou construire des composants frontend courants comme une liste triée, des menus déroulants, une pagination, et ainsi de suite.

### Conclusion de l'entretien

Comment me sens-je après mon premier entretien technique ? Honnêtement, ce fut une grande expérience. Je suis très reconnaissant envers les interviewers avec qui j'ai parlé de m'avoir donné un feedback si détaillé, et de m'avoir permis de corriger mes erreurs avant mon prochain entretien. Et même si je n'ai pas obtenu ce travail, je suis un pas de plus vers l'obtention de mon premier emploi de développeur frontend.

J'ai aussi appris que les entretiens sont une chose capricieuse. Peut-être que si j'avais construit un mécanisme de tri dans mes propres projets, ou si j'avais obtenu une mission différente plus proche de quelque chose que j'avais fait auparavant, cela aurait été différent.

Ma plus grande force est que j'ai passé beaucoup de temps à apprendre JavaScript au cours de la dernière année, et je suis maintenant capable d'apprendre et d'adopter de nouvelles idées rapidement. Malheureusement, je ne pense pas avoir pu démontrer cette connaissance cette fois-ci. Je n'ai pas eu l'occasion de :

* Leur montrer ma connaissance de la chaîne de prototypes JavaScript, et comment elle permet un partage de méthodes sans effort et efficace en mémoire entre les objets.
* Parler des fermetures et comment les fonctions internes de JavaScript ont la capacité de fermer sur les variables dans la portée externe et d'y accéder à un moment ultérieur après que la fonction externe a retourné - et comment cela empêche la collecte des déchets.
* Partager ma connaissance de la portée JavaScript, et comment JavaScript vérifie chaque niveau de sa portée locale jusqu'à la portée globale pour trouver des variables.
* Partager ma connaissance de la conversion et comment === vérifie l'égalité sans conversion de type et == vérifie l'égalité et la conversion de type.
* Parler du hissing et comment les déclarations de fonctions et les variables (sauf let et const) sont hissées en haut en JavaScript, permettant au code précédent de les utiliser.
* Parler du mot-clé this, et comment la valeur de this dépend entièrement de l'invocation (site d'appel) de la fonction.

J'aurais **voulu** **(jeu de mots intentionnel)** que je l'aie fait.

### La route vers le succès

Maintenant, il aurait été facile pour moi de me dire : « Je ne suis pas assez bon. J'ai besoin de passer 3 - 4 mois à apprendre davantage, puis essayer à nouveau. »

Je ne l'ai pas fait.

J'ai décidé de postuler à autant d'emplois que possible en deux semaines. J'ai postulé aux plus grandes entreprises informatiques de Norvège.

J'ai visé la lune.

Deux semaines plus tard, j'avais terminé les entretiens avec plusieurs entreprises, et j'avais un autre entretien technique.

### Deuxième round de préparation

Si il y a une chose que j'ai apprise de mon premier entretien technique, c'est que la préparation est la clé. Cela aide à penser à l'entretien technique comme un examen, et à prendre les mesures nécessaires pour s'assurer de le réussir.

Les examens, comme les entretiens, sont défectueux en ce sens qu'ils ne parviennent pas à englober le spectre complet des connaissances du candidat. Alors que pouvez-vous faire ?

**Élargissez votre spectre de connaissances.**

Soyez à toute épreuve. Soyez Neo.

Pour moi, j'ai utilisé des techniques de mémoire avancées pour mémoriser les réponses à plus de 100 questions d'entretien frontend en 8 heures. [Les questions peuvent être trouvées dans ce dépôt](https://github.com/h5bp/Front-end-Developer-Interview-Questions).

Comment j'ai fait cela dépasse le cadre de cet article, mais si vous êtes curieux de savoir comment cela fonctionne, laissez un commentaire ci-dessous et j'écrirai un autre article à ce sujet.

De plus, j'ai passé du temps sur des exemples pratiques sur [Code Wars](https://www.codewars.com/) et [Hackerrank](http://hackerrank.com/). Ainsi que du temps à construire des choses.

### Entretien Technique #2

Riche des leçons de mon dernier entretien raté, j'avais fait mes devoirs.

Cet entretien était plus axé sur une discussion des concepts frontend. C'était un entretien complet, et j'ai senti que les interviewers voulaient vraiment cartographier mes connaissances et apprendre mes forces et mes faiblesses.

L'entretien a duré environ deux heures cette fois, et j'ai vraiment apprécié que les interviewers aient fait leurs devoirs aussi minutieusement.

Voici une liste de tous les sujets que nous avons abordés :

* JS, CSS et HTML en larges traits
* Structure du document
* Structure du projet
* Git
* Performance
* Sécurité
* Accessibilité
* SEO
* Conception web réactive

Le défi de codage était basé sur du Javascript vanilla. On m'a demandé d'ajouter une simple classe à une div en utilisant du Javascript vanilla. Maintenant, si vous avez passé du temps en JS en utilisant principalement des frameworks, vous ne serez peut-être pas familier avec l'API classList. Heureusement, j'avais passé la plupart de mon temps à faire tous les projets freeCodeCamp avec du JS vanilla. Voici à quoi cela ressemble :

```js
const btn = document.querySelector('.btn');
const menu = document.querySelector('.menu');
function addClassNameToDiv() {
 if (!menu.classList.contains('new-class')) {
     menu.classList.add('new-class');
 } else {
     menu.classList.remove('new-class');
 }
}
btn.addEventListener('click', addClassNameToDiv)
```

Alternativement, vous pourriez utiliser classList.toggle('new-class') pour en faire une ligne. On m'a également demandé de l'étendre pour fermer le menu si vous cliquez en dehors du menu déroulant :

```
window.addEventListener('click', () => menu.classList.remove('new-class'));
```

**Leçons tirées du défi de codage :**

* Plus court est mieux, tant que c'est toujours lisible.
* En termes de performance, il est préférable de placer les sélecteurs de requête en dehors de la fonction de rappel d'un écouteur d'événement (appelé une seule fois au lieu de chaque fois que l'écouteur se déclenche).
* En termes de performance, getElementById et getElementByClassName sont plus performants que querySelector

Le lendemain, le manager m'a appelé. J'avais réussi l'entretien, et ils voulaient me faire une offre.

J'aurais pu m'arrêter là. J'aurais pu dire : « J'ai réussi un entretien technique, c'est suffisant. »

J'ai fait le contraire.

J'ai appelé chaque entreprise avec laquelle je parlais à ce moment-là et je leur ai dit que j'avais une offre sur la table, et je leur ai demandé si nous pouvions accélérer le processus, car j'avais maintenant des contraintes de temps à considérer.

Les entretiens, et surtout les entretiens techniques, sont des épreuves mentales difficiles. Vous êtes toujours en train de performer, toujours attendu pour performer et dépasser les attentes. C'est difficile. Alors pourquoi ai-je fait cela ?

**Quatre raisons.**

1. Je voulais me prouver à moi-même que ce n'était pas de la chance.
2. Je voulais être respectueux envers tout le monde avec qui j'avais eu des entretiens et leur donner une chance équitable.
3. Je voulais m'assurer de trouver la bonne adéquation et la meilleure communauté pour moi afin de grandir en tant que développeur.
4. Vous, les gars. Cette communauté m'a tellement aidé, et je voulais aider à recueillir autant d'informations que possible de l'entretien technique, afin que vous puissiez apprendre de mes erreurs et vous préparer en conséquence.

Je suis humble face à l'aide et au soutien que j'ai reçus de freeCodeCamp, et je voulais rendre la pareille.

### Entretien Technique #3

Après avoir contacté les autres entreprises et expliqué que j'avais une offre sur la table d'une entreprise de premier plan, beaucoup d'entreprises étaient pressées de me faire passer rapidement. En une semaine, j'ai mené plusieurs entretiens, et j'avais plus d'entretiens techniques à passer.

Voici un résumé de certaines des questions d'entretien de mon troisième entretien technique :

* Comment es-tu entré dans React ? Pourquoi es-tu entré dedans ? Qu'est-ce qui est bien dedans ?
* Comment fonctionne Redux ? De quoi se compose l'API ? Qu'est-ce que l'immuabilité ? Qu'est-ce qui est bien dans l'immuabilité ?
* Comment redessinerais-tu notre page web ?
* Comment te sens-tu à l'idée de travailler avec des couches plus profondes de l'application ? Par exemple, le backend ?
* Fais-tu tes propres tests ? Qu'est-ce qu'un test unitaire ?
* Qu'est-ce qu'une bonne expérience utilisateur pour toi ?
* Comment testes-tu l'expérience utilisateur ?

Le défi de codage dans cet entretien était basé sur CSS. On m'a donné une feuille de papier avec quelques règles CSS qui ressemblaient à ceci :

```js
<div id="menu" class="dropdown-menu"></div> // Élément HTML
// Règles CSS
#menu {
   color: black;
}
.dropdown-menu {
   color: green;
}
div {
   color: blue;
}
```

Ma tâche était d'expliquer ce que je voyais. J'ai immédiatement identifié l'élément HTML et j'ai dit aux interviewers que l'id et la classe sur l'élément pouvaient être utilisés en CSS pour sélectionner l'élément HTML. De là, j'ai expliqué que CSS est en cascade, ce qui signifie que normalement la dernière règle sera appliquée. Cependant, dans ce cas, les sélecteurs ont des pondérations différentes. L'ordre de pondération est le suivant : id > classe > élément.

Ce qui signifie, dans l'exemple ci-dessus, que la couleur noire sera appliquée à l'élément HTML.

### **Entretien Technique #4**

C'est le dernier entretien technique que j'ai eu. Et bien que ce soit toujours stressant, à ce stade, j'y étais habitué. Voici un résumé de ce dont nous avons parlé :

* Dessiner un site web de base. Identifier les composants.
* Comment le rendrais-tu réactif ?
* Comment centrerais-tu le texte verticalement et horizontalement ?
* Qu'est-ce que le modèle de boîte CSS ? Quelle est la différence entre la boîte de contenu et la boîte de bordure ?
* Quelle est la différence entre double et triple égal ?
* Qu'est-ce qui est bien dans React ?
* Quel est l'avantage de array.forEach par rapport à une boucle for ? Y a-t-il des cas où tu pourrais avoir besoin d'utiliser une boucle for ?

Le défi de codage était de construire une fonction de retour à la ligne de degrés de difficulté variables. Imaginez que vous ne pouvez faire tenir que 20 caractères sur un écran, et si vous dépassez, vous devez commencer sur une nouvelle ligne.

Ma solution initiale à cette question impliquait de diviser la chaîne, d'utiliser un compteur et l'opérateur modulo pour déterminer si le compte était de 20, puis d'insérer un caractère de nouvelle ligne dans le tableau et de joindre la chaîne.

La tâche a ensuite été augmentée en difficulté pour ne permettre que des mots complets sur une seule ligne. Ce qui signifie que si un mot faisait que le compte total dépassait 20, vous deviez insérer un caractère de nouvelle ligne avant ce mot.

Je n'ai pas résolu cela complètement pendant l'entretien, mais j'étais sur la bonne voie. J'ai utilisé MDN lorsque j'étais incertain, et je faisais de bons progrès.

Et cela a suffi.

Je n'ai pas pu m'en empêcher, alors si vous êtes intéressé, voici la version résolue :

```js
function wordWrap(str) {
 let totalCount = 0;
 const arr = str.split(' '), formattedStr = [];
 
 arr.forEach((word, index) => {
  totalCount += word.length;
  if (totalCount >= 20) {
     formattedStr.push('\n', word, ' ');
     totalCount = word.length;
  } else {
     formattedStr.push(word, ' ');
  }
 });
 return formattedStr.join('');
}
```

### **Conclusion**

Si vous êtes arrivé jusqu'ici, félicitations. C'était long. J'ai fait de mon mieux pour le rendre aussi informatif que possible, espérant que cela puisse aider quelqu'un comme vous.

Le résultat final de cela m'a placé dans une situation que je n'aurais jamais imaginée. À la fin, j'avais 5 offres sur la table à choisir. Une grande entreprise m'a même fait une offre « à l'aveugle », basée sur le fait que j'avais une offre d'un concurrent. J'ai fini par choisir l'entreprise où j'ai d'abord réussi l'entretien technique, car je croyais que ce serait le meilleur choix pour moi.

L'entretien technique peut être une épreuve mentale difficile. Vous allez être mis au défi, vous allez être sorti de votre zone de confort, et c'est une bonne chose. Cela vous aide à grandir. Cela vous rend meilleur.

Et si vous vous préparez, vous serez prêt pour cela.

Alors, d'après ma propre expérience, ne vous éloignez pas de l'entretien technique. Ne le repoussez pas parce que vous en avez raté un. Ne pensez pas que c'est la mesure ultime de vous en tant que développeur. Ce n'est pas le cas. Ce n'est que l'outil le moins cassé que les entreprises ont pour mesurer votre productivité.

Postulez pour des emplois. Préparez-vous bien. Passez des entretiens techniques. Apprenez de vos erreurs. Répétez.

Si vous faites cela, je vous le garantis, vous réussirez.

Je vous soutiens.