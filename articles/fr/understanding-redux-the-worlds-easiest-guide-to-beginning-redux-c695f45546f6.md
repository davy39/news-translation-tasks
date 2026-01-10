---
title: Le Livre Redux – Le Guide le Plus Simple au Monde pour Débuter avec Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-01T14:36:35.000Z'
originalURL: https://freecodecamp.org/news/understanding-redux-the-worlds-easiest-guide-to-beginning-redux-c695f45546f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8cpJBanzu5koQqzkBirvsQ.png
tags:
- name: book
  slug: book
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: technology
  slug: technology
seo_title: Le Livre Redux – Le Guide le Plus Simple au Monde pour Débuter avec Redux
seo_desc: 'By Emmanuel Ohans

  This is a comprehensive (but simplified) guide for absolute Redux beginners, or
  any who wants to re-evaluate their understanding of the fundamental Redux concepts.

  For an expanded Table of Contents please visit this link, & for more...'
---

Par Emmanuel Ohans

Ce guide est une ressource complète (mais simplifiée) pour les débutants absolus en Redux, ou pour quiconque souhaite réévaluer sa compréhension des concepts fondamentaux de Redux.

Pour un **Table des Matières** détaillé, veuillez [visiter ce lien](https://medium.com/@ohansemmanuel/table-of-contents-for-understanding-redux-ea0667e1453d), et pour des concepts **Redux avancés**, consultez mes [livres sur Redux](https://thereduxjsbooks.com).

### Introduction

![Image](https://cdn-media-1.freecodecamp.org/images/1*hNbxQCWNME17dVX4cdSugw.png)

Cet article (qui est en réalité un livre) est la pièce manquante si vous avez longtemps cherché comment maîtriser Redux.

Avant de commencer, je devrais vous dire que ce livre parle avant tout de moi. Oui, de moi. Mes luttes pour apprendre Redux, et la recherche d'une meilleure façon de l'enseigner.

Il y a quelques années, j'avais tout juste appris React. J'étais enthousiaste à ce sujet, mais encore une fois, tout le monde semblait parler de quelque chose d'autre appelé Redux.

### Mon Dieu ! La série d'apprentissage ne finit-elle jamais ?

En tant qu'ingénieur engagé dans mon développement personnel, je voulais être au courant. Je ne voulais pas être laissé de côté. Alors, j'ai commencé à apprendre Redux.

J'ai vérifié la documentation de Redux. Elle était assez bonne, en fait ! Pour une raison quelconque, cela n'a tout simplement pas tout à fait cliqué pour moi. J'ai également regardé une série de vidéos YouTube. Celles que j'ai trouvées semblaient précipitées et pas détaillées. Pauvre de moi.

Honêtement, je ne pense pas que les tutoriels vidéo que j'ai regardés étaient mauvais. Il manquait juste quelque chose. Un guide facile qui soit bien pensé et écrit pour une personne saine d'esprit comme moi, et non pour un humanoïde imaginaire.

Il semblait que je n'étais pas seul.

Un bon ami à moi, quelqu'un que je mentorais à l'époque, venait de terminer un cours de certification de développeur React où il avait payé une somme importante (plus de 300 $) pour obtenir un certificat.

Quand je lui ai demandé son avis honnête sur le programme, ses mots étaient du genre :

> Le cours était assez bon, mais je ne pense toujours pas que Redux ait été bien expliqué à un débutant comme moi. Ce n'était pas expliqué si bien.

Vous voyez, il y en a beaucoup d'autres comme mon ami, tous en difficulté pour comprendre Redux. Ils utilisent peut-être Redux, mais ils ne peuvent pas dire qu'ils comprennent vraiment comment cela fonctionne.

J'ai décidé de trouver une solution. J'allais comprendre Redux en profondeur, et trouver une manière plus claire de l'enseigner.

Ce que vous êtes sur le point de lire a pris des mois d'étude, puis un peu plus de temps pour écrire et construire les projets d'exemple, tout en gardant un emploi quotidien et d'autres engagements sérieux.

Mais vous savez quoi ?

Je suis super excité de partager cela avec vous !

Si vous avez cherché un guide Redux qui ne vous parlera pas par-dessus la tête, c'est celui-ci. Ne cherchez pas plus loin.

J'ai pris en considération mes luttes et celles de beaucoup d'autres que je connais. Je m'assurerai de vous enseigner les choses importantes — et de le faire sans vous confondre.

Maintenant, c'est une promesse.

### Mon Approche pour Enseigner Redux

Le vrai problème avec l'enseignement de Redux — surtout pour les débutants — n'est pas la complexité de la bibliothèque Redux elle-même.

Non. Je ne pense pas que ce soit cela. Ce n'est qu'une petite bibliothèque de 2 ko — dépendances incluses.

Jetez un œil à la communauté Redux en tant que débutant, et vous allez perdre la tête rapidement. Il n'y a pas **seulement** Redux, mais aussi toute une série d'autres bibliothèques "associées" supposées nécessaires pour construire des applications réelles.

Si vous avez passé un peu de temps à faire des recherches, alors vous les avez déjà rencontrées. Il y a Redux, React-Redux, Redux-thunk, Redux-saga, Redux-promise, Reselect, Recompose et bien d'autres encore !

Comme si cela ne suffisait pas, il y a aussi le routage, l'authentification, le rendu côté serveur, les tests et le bundling qui s'ajoutent — tout en même temps.

Mon Dieu ! C'est écrasant.

Le "tutoriel Redux" n'est souvent pas tant sur Redux, mais sur toutes les autres choses qui l'accompagnent.

Il doit y avoir une approche plus saine adaptée aux débutants. Si vous êtes un développeur humanoïde, vous n'aurez certainement pas de problèmes avec cela. Devinez quoi ? La plupart d'entre nous sont en fait des humains.

**Alors, voici mon approche pour enseigner Redux.**

Oubliez toutes les choses supplémentaires pour l'instant, et faisons simplement Redux. Oui !

Je n'introduirai que le strict minimum dont vous avez besoin pour l'instant. Il n'y aura pas de React-router, Redux-form, Reselect, Ajax, Webpack, Authentification, Tests, rien de tout cela — pour l'instant !

Et devinez quoi ? C'est ainsi que vous avez appris à faire certaines des compétences "importantes" de la vie que vous avez acquises.

Comment avez-vous appris à marcher ?

Avez-vous commencé à courir en un jour ? Non !

Laissez-moi vous guider à travers une approche saine pour apprendre Redux — sans les tracas.

Restez bien assis.

#### _"Une marée montante soulève tous les bateaux"_

Une fois que vous aurez compris le fonctionnement des bases de Redux (la marée montante), tout le reste sera plus facile à comprendre (cela soulève tous les bateaux).

### Une Note sur la Courbe d'Apprentissage de Redux

![Image](https://cdn-media-1.freecodecamp.org/images/1*9S5urNy3YlK3LbxFfKefdQ.png)
_Un tweet sur la courbe d'apprentissage de Redux d'Eric Elliot._

Redux a une courbe d'apprentissage. Je ne dis pas le contraire.

Apprendre à marcher avait aussi une courbe d'apprentissage. Cependant, avec une approche systématique de l'apprentissage, vous l'avez surmontée.

Vous êtes tombé quelques fois, mais c'était acceptable. Quelqu'un était toujours là pour vous soutenir et vous aider à vous remettre sur pied.

Eh bien, j'espère être cette personne pour vous — pendant que vous apprenez Redux avec moi.

### Ce que Vous Allez Apprendre

Après tout ce qui a été dit et fait, vous allez voir que Redux n'est pas aussi effrayant qu'il en a l'air de l'extérieur.

Les principes sous-jacents sont si simples !

Tout d'abord, je vais vous enseigner les fondamentaux de Redux dans un langage simple et facile à aborder.

Ensuite, nous allons construire quelques applications simples. En commençant par une application basique Hello World.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FrKpOqcpaxYoOK3Xh2XELw.png)
_Une application Redux Hello World basique._

Mais cela ne suffira pas.

J'inclurai également des exercices et des problèmes que je pense que vous devriez aborder.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BReMx28eoEflxz9qJGLRgA.png)
_Applications d'exercice que nous allons travailler ensemble._

L'apprentissage efficace ne consiste pas seulement à lire et à écouter. L'apprentissage efficace consiste surtout à pratiquer !

Considérez cela comme des devoirs, mais sans le professeur en colère. En pratiquant les exercices, vous pouvez me [Tweeter](https://twitter.com/OhansEmmanuel) avec le hashtag #UnderstandingRedux et je jetterai définitivement un coup d'œil !

Pas de professeurs en colère, hein ?

Les exercices sont bons, mais vous devez aussi me regarder construire une application plus grande. C'est là que nous concluons en construisant **Skypey**, une application de messagerie sympa, un peu comme un clone de Skype.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3VVJuwBx5J-A4A4n5FhKcg.gif)
_Skypey : Le clone de Skype que nous allons construire ensemble._

Skypey a des fonctionnalités telles que l'édition de messages, la suppression de messages et l'envoi de messages à plusieurs contacts.

Hourra !

Si cela ne vous a pas excité, je ne sais pas ce qui le fera. Je suis super excité de vous montrer tout cela !

![Image](https://cdn-media-1.freecodecamp.org/images/1*LGGCJPkm_P-dpjlTKlFymw.gif)
_Gif par Jona Dinges_

### Prérequis

Le seul prérequis est que vous connaissiez déjà React. Si ce n'est pas le cas, [Dave Ceddia](https://www.freecodecamp.org/news/understanding-redux-the-worlds-easiest-guide-to-beginning-redux-c695f45546f6/undefined) [Pure React](https://daveceddia.com/pure-react/) est ma recommandation personnelle si vous avez quelques dollars à dépenser. Je ne suis pas affilié. C'est juste une bonne ressource.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4K9z2UW0LJlrLoRCrKagPg.png)

### Télécharger le PDF et l'Epub pour la Lecture Hors Ligne

La vidéo ci-dessous met en évidence le processus impliqué dans l'obtention de vos versions PDF et Epub du livre.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yHOPFYwlVvI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Le point crucial est le suivant :

1. Visitez la [page de vente du livre](https://gumroad.com/l/Ocgbb).
2. Utilisez le coupon **FREECODECAMP** pour obtenir 100 % de réduction sur le prix afin d'obtenir un livre de 29 $ pour 0 $.
3. Si vous voulez dire merci, veuillez recommander cet article en le partageant sur les réseaux sociaux.

Maintenant, commençons.

### Chapitre 1 : Découvrir Redux

![Image](https://cdn-media-1.freecodecamp.org/images/1*s6ZQPdkn-5ho3mPLrqKsJg.png)

Il y a quelques années, le développement d'applications front-end semblait être une plaisanterie pour beaucoup. De nos jours, la complexité croissante de la construction d'applications front-end décentes est presque écrasante.

Il semble que pour répondre aux exigences pressantes de l'utilisateur toujours plus exigeant, le chaton mignon et gentil a dépassé les limites d'une maison. Il est devenu un lion sans peur avec des griffes de 3 pouces et une bouche qui s'ouvre assez large pour contenir une tête humaine.

Oui, c'est à cela que ressemble le développement front-end moderne de nos jours.

Les frameworks modernes comme Angular, React et Vue ont fait un excellent travail pour dompter cette "bête". De même, les philosophies modernes telles que celles imposées par Redux existent également pour donner à cette "bête" une pilule de calme.

Suivez-moi pendant que nous examinons ces philosophies.

### Qu'est-ce que Redux ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*1dMEMg7Z1a7PIU4YWA7JXw.png)
_Qu'est-ce que Redux ? Comme vu dans la Documentation Redux_

La documentation officielle de Redux indique :

> Redux est un conteneur d'état prévisible pour les applications JavaScript.

Ces 9 mots semblaient être 90 phrases incomplètes lorsque je les ai lus pour la première fois. Je n'ai tout simplement pas compris. Vous ne comprenez probablement pas non plus.

Ne vous en faites pas. Je vais passer en revue cela dans un instant, et à mesure que vous utiliserez Redux davantage, cette phrase deviendra plus claire.

Du bon côté, si vous lisez la documentation un peu plus longtemps, vous trouverez les éléments plus explicatifs quelque part là-dedans.

Elle indique :

> Il vous aide à écrire des applications qui se comportent de manière cohérente...

Vous voyez cela ?

En termes profanes, cela signifie : "il vous aide à dompter la bête". Métaphoriquement.

Redux élimine certains des tracas liés à la gestion de l'état dans les grandes applications. Il vous offre une excellente expérience de développement et s'assure que la testabilité de votre application n'est pas sacrifiée pour cela.

Alors que vous développez des applications React, vous pouvez constater que le fait de conserver tout votre état dans un composant de niveau supérieur n'est plus suffisant pour vous.

Vous pouvez également avoir beaucoup de données qui changent dans votre application au fil du temps.

Redux aide à résoudre ces types de problèmes. Notez bien qu'il n'est pas la seule solution disponible.

### Pourquoi utiliser Redux ?

Comme vous le savez déjà, des questions comme "Pourquoi devriez-vous utiliser A plutôt que B ?" se résument à vos préférences personnelles.

J'ai construit des applications en production qui n'utilisent pas Redux. Je suis sûr que beaucoup ont fait de même.

Pour ma part, je m'inquiétais d'introduire une couche supplémentaire de complexité pour mes membres d'équipe. Au cas où vous vous poseriez la question, je ne regrette pas du tout cette décision.

L'auteur de Redux, [Dan Abamov](https://twitter.com/dan_abramov), met également en garde contre le danger d'introduire Redux [trop tôt](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367) dans votre application. Vous n'aimerez peut-être pas Redux, et c'est tout à fait compréhensible. J'ai des amis qui ne l'aiment pas.

Cela dit, il existe encore de très bonnes raisons d'apprendre Redux.

Par exemple, dans les applications plus grandes avec beaucoup de pièces mobiles, la gestion de l'état devient une préoccupation majeure. Redux résout cela assez bien sans problèmes de performance ou de compromis sur la testabilité.

Une autre raison pour laquelle de nombreux développeurs aiment Redux est l'expérience de développement qui l'accompagne. Beaucoup d'autres outils ont commencé à faire des choses similaires, mais un grand crédit à Redux.

Certaines des choses sympas que vous obtenez en utilisant Redux incluent la journalisation, le rechargement à chaud, le voyage dans le temps, les applications universelles, l'enregistrement et la relecture — tout cela sans avoir à faire grand-chose de votre côté en tant que développeur. Ces choses sonneront probablement de manière fantaisiste jusqu'à ce que vous les utilisiez et que vous voyiez par vous-même.

La conférence de Dan appelée [Hot Reloading with Time Travel](https://youtu.be/xsSnOQynTHs) vous donnera une bonne idée de leur fonctionnement.

De plus, [Mark Ericsson](https://twitter.com/acemarke?lang=en), l'un des mainteneurs de Redux, dit que [plus de 60 %](http://blog.isquaredsoftware.com/2018/03/redux-not-dead-yet/) des applications React en production utilisent Redux. C'est beaucoup !

Par conséquent, et ce n'est que mon avis, de nombreux ingénieurs aiment montrer aux employeurs potentiels qu'ils peuvent maintenir de grandes bases de code de production construites en React et Redux, donc ils apprennent Redux.

Si vous voulez d'autres raisons d'utiliser Redux, Dan, le créateur de Redux, a quelques autres raisons mises en avant dans [son article](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367) sur Medium.

Si vous ne vous considérez pas comme un ingénieur senior, je vous conseille d'apprendre Redux — largement à cause de certains des principes qu'il enseigne. Vous apprendrez de nouvelles façons de faire des choses courantes, et cela vous rendra probablement un meilleur ingénieur.

Chacun a des raisons différentes de choisir différentes technologies. À la fin, le choix vous appartient. Mais cela ne fait certainement pas de mal d'ajouter Redux à votre ensemble de compétences.

### Expliquer Redux à un enfant de 5 ans

Cette section du livre est vraiment importante. L'explication ici sera référencée tout au long du livre. Alors, préparez-vous.

Puisqu'un enfant de 5 ans n'a pas le temps pour le jargon technique, je vais garder cela très simple mais pertinent pour notre objectif d'apprendre Redux.

Alors, c'est parti !

Considérons un événement auquel vous êtes probablement familier — aller à la banque pour retirer de l'argent. Même si vous ne faites pas cela souvent, vous êtes probablement conscient de ce à quoi ressemble le processus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rRbT3p4vI6FQOvwppdMuzA.png)
_Le jeune Joe se rend à la banque._

Vous vous réveillez un matin et vous vous rendez à la banque aussi vite que possible. En allant à la banque, il n'y a qu'une seule **intention/action** que vous avez en tête : `RETIRER_DE_L'ARGENT`.

Vous voulez retirer de l'argent de la banque.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wgMTYZNauE-xrHlcPEiOnA.png)
_Le jeune Joe se rend à la banque avec l'intention de retirer de l'argent._

Voici où les choses deviennent intéressantes.

Lorsque vous entrez dans la banque, vous allez directement au Caissier pour faire connaître votre demande.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yy1NfkM5n7E-97hyH2qYsA.png)
_Le jeune Joe est à la banque ! Il va directement voir le Caissier et fait connaître sa demande._

Attendez, vous êtes allé voir le Caissier ?

Pourquoi n'êtes-vous pas simplement entré dans le coffre-fort de la banque pour récupérer votre argent ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ca5dfoZcpdfmVCAaxlkliw.png)
_Si seulement le jeune Joe entrait dans le Coffre. Il partirait avec autant qu'il trouve._

Après tout, c'est votre argent durement gagné.

Eh bien, comme vous le savez déjà, les choses ne fonctionnent pas de cette manière. Oui, la banque a de l'argent dans le coffre, mais vous devez parler au Caissier pour vous aider à suivre un processus dû pour retirer votre propre argent.

Le Caissier, depuis leur ordinateur, entre ensuite quelques commandes et vous remet votre argent. Facile comme bonjour.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9wklChnNZx8Cpt4Sa7vb7Q.png)
_Voici comment vous obtenez de l'argent. Pas du Coffre, désolé._

Maintenant, comment Redux s'intègre-t-il dans cette histoire ?

Nous allons entrer dans plus de détails bientôt, mais d'abord, la terminologie.

1. Le Coffre de la Banque est à la banque ce que le `Store Redux` est à Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*y60iqwOOfQmzPcQhzU8WFA.png)
_Le coffre de la banque peut être comparé au Store Redux !_

Le coffre de la banque garde l'argent dans la banque, n'est-ce pas ?

Eh bien, dans votre application, vous ne dépensez pas d'argent. Au lieu de cela, l'`état` de votre application est comme l'argent que vous dépensez. L'ensemble de l'interface utilisateur de votre application est une fonction de votre état.

Tout comme le coffre de la banque garde votre argent en sécurité dans la banque, l'état de votre application est gardé en sécurité par quelque chose appelé un `store`. Donc, le `store` garde votre "argent" ou `état` intact.

Euh, vous devez vous en souvenir, d'accord ?

**Le Store Redux peut être comparé au Coffre de la Banque. Il contient l'état de votre application — et le garde en sécurité.**

Cela conduit au premier principe de Redux :

> Avoir une seule source de vérité : L'état de votre application entière est stocké dans un arbre d'objets au sein d'un seul store Redux.

Ne laissez pas les mots vous confondre.

En termes simples, avec Redux, il est conseillé de stocker l'état de votre application dans un seul objet géré par le `store` Redux. C'est comme avoir `un seul coffre` au lieu de disperser de l'argent partout dans le hall de la banque.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aG_sU6CyVDRW9iy4SfuKRg.png)
_Le premier principe de Redux_

2. Allez à la banque avec une `action` en tête.

Si vous voulez obtenir de l'argent de la banque, vous devrez y aller avec une certaine intention ou action de retirer de l'argent.

Si vous entrez simplement dans la banque et vous promenez, personne ne vous donnera simplement de l'argent. Vous pourriez même finir par être jeté dehors par la sécurité. Triste histoire.

On pourrait en dire autant pour Redux.

Écrivez autant de code que vous voulez, mais si vous voulez mettre à jour l'état de votre application Redux (comme vous le faites avec `setState` dans React), vous devez informer Redux de cela avec une `action`.

De la même manière que vous suivez un processus dû pour retirer votre propre argent de la banque, Redux tient également compte d'un processus dû pour changer/mettre à jour l'état de votre application.

Cela nous amène au principe Redux #2.

> L'état est en lecture seule :

> La seule façon de changer l'état est d'émettre une action, un objet décrivant ce qui s'est passé.

Qu'est-ce que cela signifie en langage clair ?

Lorsque vous marchez vers la banque, vous y allez avec une action claire en tête. Dans cet exemple, vous voulez retirer de l'argent.

Si nous choisissons de représenter ce processus dans une simple application Redux, votre action à la banque peut être représentée par un objet.

Un objet qui ressemble à ceci :

```js
{ 
  type: "RETIRER_DE_L'ARGENT",
  montant: "10 000 $"
}
```

Dans le contexte d'une application Redux, cet objet est appelé une `action` ! Il a toujours un champ `type` qui décrit l'action que vous souhaitez effectuer. Dans ce cas, il s'agit de `RETIRER_DE_L'ARGENT`.

Chaque fois que vous devez changer/mettre à jour l'état de votre application Redux, vous devez envoyer une action.

![Image](https://cdn-media-1.freecodecamp.org/images/1*niOOiE8U1EzTmDSNdCUwaQ.png)
_Le deuxième principe de Redux._

Ne vous stressez pas sur la façon de faire cela pour l'instant. Je pose simplement les bases ici. Nous approfondirons de nombreux exemples bientôt.

3. Le Caissier est à la banque ce que le `réducteur` est à Redux.

D'accord, faites un pas en arrière.

Souvenez-vous que dans l'histoire ci-dessus, vous ne pouviez pas simplement aller directement dans le coffre de la banque pour récupérer votre argent de la banque. Non. Vous deviez d'abord voir le Caissier.

Eh bien, vous aviez une action en tête, mais vous deviez transmettre cette action à quelqu'un — le Caissier — qui à son tour communiquait (de la manière qu'ils faisaient) avec le coffre qui contient tout l'argent de la banque.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9U0ntjx6hpWKc7deAFYsdQ.png)
_La communication entre le Caissier et le Coffre !_

On pourrait en dire autant pour Redux.

Comme vous avez fait connaître votre action au Caissier, vous devez faire de même dans votre application Redux. Si vous voulez mettre à jour l'état de votre application, vous transmettez votre `action` au `réducteur` — notre propre Caissier.

Ce processus est principalement appelé l'envoi d'une `action`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pl0DYUFRdhGkIdvX9jEX1g.png)

Dispatch est juste un mot anglais. Dans cet exemple, et dans le monde Redux, il est utilisé pour signifier l'envoi de l'action aux réducteurs.

Le `réducteur` sait quoi faire. Dans cet exemple, il prendra votre action pour `RETIRER_DE_L'ARGENT` et s'assurera que vous obtenez votre argent.

En termes Redux, l'argent que vous dépensez est votre `état`. Donc, votre réducteur sait quoi faire, et il retourne toujours votre `nouvel état`.

Hmmm. Ce n'était pas si difficile à comprendre, n'est-ce pas ?

Et cela nous amène au dernier principe de Redux :

> Pour spécifier comment l'arbre d'état est transformé par les actions, vous écrivez des réducteurs purs.

Alors que nous avançons, j'expliquerai ce qu'est un réducteur "pur". Pour l'instant, ce qui est important est de comprendre que, pour mettre à jour l'état de votre application (comme vous le faites avec `setState` dans React), vos actions doivent toujours être envoyées (dispatched) aux réducteurs pour obtenir votre `nouvel état`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xa5F3FkCXNVquJVGh13JWg.png)
_Le troisième principe de Redux_

Avec cette analogie, vous devriez maintenant avoir une idée de ce que sont les acteurs Redux les plus importants : le `store`, le `réducteur` et une `action`.

Ces trois acteurs sont essentiels à toute application Redux. Une fois que vous comprenez comment ils fonctionnent, la majeure partie du travail est faite.

### Chapitre 2 : Votre Première Application Redux

![Image](https://cdn-media-1.freecodecamp.org/images/1*pk7qqBNInfhHljVqxT_Ffg.png)

> Nous apprenons par l'exemple et par l'expérience directe car il y a des limites réelles à l'adéquation de l'instruction verbale.  
>   
> Malcom Gladwell

Même si j'ai passé beaucoup de temps à expliquer les principes de Redux d'une manière que vous n'oublierez pas, les instructions verbales ont leurs limites.

Pour approfondir votre compréhension des principes, je vais vous montrer un exemple. Votre première application Redux, si vous voulez l'appeler ainsi.

Mon approche de l'enseignement est d'introduire des exemples de difficulté croissante. Donc, pour commencer, cet exemple est axé sur la refactorisation d'une simple application pure React pour utiliser Redux.

L'objectif ici est de comprendre comment introduire Redux dans un simple projet React, et d'approfondir votre compréhension des concepts fondamentaux de Redux également.

Prêt ?

Voici l'application "Hello World" triviale avec laquelle nous allons travailler.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JtIWaDLn7cCkOy_BBItC7w.png)
_L'application basique Hello World._

Ne riez pas.

Vous apprendrez à faire vos premiers pas avec Redux à partir d'un concept "connu" comme React, vers l'"inconnu" Redux.

### La Structure de l'Application React Hello World

L'application React avec laquelle nous allons travailler a été initialisée avec `create-react-app`. Ainsi, la structure de l'application est celle à laquelle vous êtes déjà habitué.

Vous pouvez récupérer le dépôt depuis [Github](https://github.com/ohansemmanuel/hello-redux) si vous souhaitez suivre — ce que je recommande.

Il y a un fichier d'entrée `index.js` qui rend un composant `<App />` dans le `DOM`.

Le composant principal `App` est composé d'un certain composant `<HelloWorld />`.

Ce composant `<HelloWorld />` prend une prop `tech`, et cette prop est responsable de la technologie particulière affichée à l'utilisateur.

Par exemple, `<HelloWorld tech="React" />` donnera le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*88RahoLYBGZ_RM_Betiolw.png)
_L'application basique Hello World avec l'état par défaut, "React"_

De plus, un `<HelloWorld tech="Redux" />` donnera le résultat suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dm-ckGv0Do49-k0HOR2gSQ.png)
_L'application basique Hello World avec la prop tech changée en "Redux"_

Maintenant, vous comprenez l'idée.

Voici à quoi ressemble le composant `App` :

`**src/App.js**`

```js
import React, { Component } from "react";
import HelloWorld from "./HelloWorld";

class App extends Component {
 state = { 
  tech : "React"
}
render() {
  return <HelloWorld tech={this.state.tech}/>
}
}

export default App;
```

Jetez un bon coup d'œil à l'objet `state`.

Il n'y a qu'un seul champ, `tech`, dans l'objet `state` et il est passé en tant que `prop` dans le composant `HelloWorld` comme montré ci-dessous :

```
<HelloWorld tech={this.state.tech}/>
```

Ne vous inquiétez pas de l'implémentation du composant `HelloWorld` — pour l'instant. Il prend simplement une prop `tech` et applique un peu de CSS fantaisiste. C'est tout.

Puisque cela est principalement axé sur Redux, je vais sauter les détails du style.

Donc, voici le défi.

Comment pouvons-nous refactoriser notre `App` pour utiliser `Redux` ?

Comment pouvons-nous supprimer l'objet state et le faire gérer entièrement par Redux ? Rappelez-vous que Redux est le **gestionnaire d'état** de votre application.

Commençons à répondre à ces questions dans la section suivante.

### Revisiter vos Connaissances de Redux

Vous vous souvenez de la citation de la documentation officielle ?

> Redux est un conteneur d'état prévisible pour les applications JavaScript.

Une phrase clé dans la phrase ci-dessus est **conteneur d'état**.

Techniquement, vous voulez que l'`état` de votre application soit géré par Redux.

C'est ce qui fait de Redux un **conteneur d'état**_._

L'état de votre composant React existe toujours. Redux ne le supprime pas.

Cependant, Redux gérera efficacement l'état **global** de votre application. Comme un coffre de banque, il a un `store` pour cela.

Pour le simple composant `<App/>` que nous avons ici, l'objet state est simple.

Le voici :

```
{
 tech: "React"
}
```

Nous devons le retirer du state du composant `<App />`, et le faire gérer par Redux.

D'après mon explication précédente, vous devriez vous souvenir de l'analogie entre le Coffre de la Banque et le Store Redux. Le Coffre de la Banque garde l'argent, le `store` Redux garde l'objet state de l'application.

Alors, quelle est la première étape pour refactoriser le composant `<App />` pour utiliser Redux ?

Oui, vous avez raison.

Supprimer le state du composant de `<App />`.

Le `store` Redux sera responsable de la gestion de l'`état` de l'App. Cela dit, nous devons supprimer l'objet state actuel de `App/>`.

```js
import React, { Component } from "react";
import HelloWorld from "./HelloWorld";

class App extends Component {
 // l'objet state a été supprimé. 
render() {
  return <HelloWorld tech={this.state.tech}/>
}
}

export default App;
```

La solution ci-dessus est incomplète, mais pour l'instant, `<App/>` n'a pas d'état.

Veuillez installer Redux en exécutant `yarn add redux` depuis l'interface de ligne de commande (CLI). Nous avons besoin du package `redux` pour faire quoi que ce soit de bien.

### Création d'un Store Redux

Si `<App />` ne gérera pas son état, alors nous devons créer un Store Redux pour gérer l'état de notre application.

Pour un Coffre de Banque, quelques ingénieurs mécaniciens ont probablement été embauchés pour créer une installation sécurisée de conservation de l'argent.

Pour créer une installation de conservation d'état gérable pour notre application, nous n'avons pas besoin d'ingénieurs mécaniciens. Nous le ferons de manière programmatique en utilisant certaines des API que Redux met à notre disposition.

Voici à quoi ressemble le code pour créer un `store` Redux :

```js
import { createStore } from "redux"; // une importation de la bibliothèque redux
const store = createStore();  // une solution incomplète - pour l'instant.
```

Tout d'abord, nous importons la fonction de fabrique `createStore` de Redux. Ensuite, nous invoquons la fonction, `createStore()` pour créer le store.

Maintenant, la fonction `createStore` prend quelques arguments. Le premier est un `reducer`.

Ainsi, une création de store plus complète serait représentée comme ceci : `createStore(reducer)`

Maintenant, laissez-moi expliquer pourquoi nous avons un `reducer` là-dedans.

### La Relation entre le Store et le Reducer

Retour à l'analogie de la banque.

Lorsque vous allez à la banque pour faire un retrait, vous rencontrez le Caissier. Après avoir fait connaître votre intention/action `RETIRER_DE_L'ARGENT` au Caissier, ils ne vous remettent pas simplement l'argent demandé.

Non.

Le Caissier vérifie d'abord que vous avez assez d'argent sur votre compte pour effectuer la transaction de retrait que vous souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*URl1s4Dd6zgdh_8LuOaAfQ.png)
_Vous avez combien vous voulez même retirer ?_

Le Caissier vérifie d'abord que vous avez l'argent que vous dites avoir.

Depuis l'ordinateur, ils peuvent tout voir — en quelque sorte en communiquant avec le Coffre, puisque le Coffre contient tout l'argent de la banque.

En résumé, le Caissier et le Coffre sont toujours synchronisés. De grands amis !

![Image](https://cdn-media-1.freecodecamp.org/images/1*9U0ntjx6hpWKc7deAFYsdQ.png)
_Le Caissier et le Coffre en synchronisation !_

On pourrait en dire autant pour un `STORE` Redux (notre propre Coffre), et le `REDUCER` Redux (notre propre Caissier).

Le Store et le Reducer sont de grands amis. Toujours en synchronisation.

Pourquoi ?

Le `REDUCER` "parle" toujours au `STORE`. Tout comme le Caissier reste en synchronisation avec le Coffre.

Cela explique pourquoi la création du store doit être invoquée avec un `Reducer`, et cela est obligatoire. Le `Reducer` est le seul argument obligatoire passé à `createStore()`

![Image](https://cdn-media-1.freecodecamp.org/images/1*nuhu4cIhARGmLctYXthPAw.png)
_Le reducer est un argument obligatoire passé à « createStore »_

Dans la section suivante, nous allons jeter un bref coup d'œil aux Reducers, puis créer un `STORE` en passant le `REDUCER` dans la fonction de fabrique `createStore`.

### Le Reducer

Nous allons entrer dans les détails plus tard, mais je vais garder cela court pour l'instant.

Lorsque vous entendez le mot, reducer, qu'est-ce qui vous vient à l'esprit ?

Réduire ?

Oui, c'est ce que je pensais.

Cela ressemble à réduire.

Eh bien, selon la documentation officielle de Redux :

> Les reducers sont le concept le plus important dans Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZfzLq5UcqweCssO8ulgHHw.png)
_Les reducers sont le concept le plus important dans Redux. Un ingénieur plus expérimenté pourrait argumenter en faveur des middlewares._

Notre Caissier est une personne assez importante, hein ?

Alors, quel est le problème avec le Reducer. Que fait-il ?

En termes plus techniques, un reducer est également appelé une fonction de réduction. Vous ne l'avez peut-être pas remarqué, mais vous utilisez probablement déjà un reducer — si vous êtes familier avec la méthode `[Array.reduce()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)`.

Voici un petit rappel.

Considérez le code ci-dessous.

C'est une façon populaire d'obtenir la somme des valeurs dans un tableau JavaScript :

```js
let arr = [1,2,3,4,5]
let sum = arr.reduce((x,y) => x + y)
console.log(sum)  //15
```

Sous le capot, la fonction passée à `arr.reduce` est appelée un `reducer`.

Dans cet exemple, le reducer prend deux valeurs, un `accumulateur` et une `valeurActuelle`, où `x` est l'`accumulateur` et `y` est la `valeurActuelle`.

De la même manière, le Redux Reducer est simplement une fonction. Une fonction qui prend **deux** paramètres. Le premier étant l'`ÉTAT` de l'application, et l'autre l'`ACTION`.

Oh mon Dieu ! Mais d'où viennent l'`ÉTAT` et l'`ACTION` passés dans le `REDUCER` ?

Lorsque j'apprenais Redux, je me suis posé cette question plusieurs fois.

Tout d'abord, jetez un œil à l'exemple `Array.reduce()` à nouveau :

```js
let arr = [1,2,3,4,5]
let sum = arr.reduce((x,y) => x + y)
console.log(sum)  //15
```

La méthode `Array.reduce` est responsable de la transmission des arguments nécessaires, `x` et `y` dans l'argument de la fonction, le `reducer`. Donc, les arguments ne sont pas sortis de nulle part.

On pourrait en dire autant pour Redux.

Le reducer Redux est également passé dans une certaine méthode. Devinez ce que c'est ?

Le voici !

```js
createStore(reducer)
```

La fonction de fabrique `createStore`. Il y a un peu plus impliqué dans le processus comme vous le verrez bientôt.

Comme `Array.reduce()`, `createStore()` est responsable de la transmission des arguments dans le reducer.

Si vous n'avez pas peur des trucs techniques, voici la version épurée de l'implémentation de `createStore` dans le code source de Redux.

```js
function createStore(reducer) {
    var state;
    var listeners = []

    function getState() {
        return state
    }
    
    function subscribe(listener) {
        listeners.push(listener)
        return unsubscribe() {
            var index = listeners.indexOf(listener)
            listeners.splice(index, 1)
        }
    }
    
    function dispatch(action) {
        state = reducer(state, action)
        listeners.forEach(listener => listener())
    }

    dispatch({})

    return { dispatch, subscribe, getState }
}
```

Ne vous en voulez pas si vous ne comprenez pas le code ci-dessus. Ce que je veux vraiment souligner est dans la fonction `dispatch`.

Remarquez comment le `reducer` est appelé avec `state` et `action`

Cela dit, le code minimal pour créer un `store` Redux est le suivant :

```js
import { createStore } from "redux";  
const store = createStore(reducer);   //ci a été mis à jour pour inclure le reducer créé.
```

### Retour au Processus de Refactorisation

Revenons à la refactorisation de l'application React "Hello World" pour utiliser Redux.

Si je vous ai perdu à un moment donné dans la section précédente, veuillez relire la section une fois de plus et je suis sûr que cela s'imprégnera. Mieux encore, vous pouvez [me poser une question](https://twitter.com/OhansEmmanuel).

D'accord, voici tout le code que nous avons à ce stade :

```js
import React, { Component } from "react";
import HelloWorld from "./HelloWorld";

 import { createStore } from "redux";  
 const store = createStore(reducer);  

 class App extends Component {
 render() {
   return <HelloWorld tech={this.state.tech}/>
 }
}

export default App;
```

Cela a du sens ?

Vous avez peut-être remarqué un problème avec ce code. Voir la ligne 4.

La fonction `reducer` passée à `createStore` n'existe pas encore.

Maintenant, nous devons en écrire une. Le reducer est juste une fonction, vous vous souvenez ?

Créez un nouveau répertoire appelé `**reducers**` et créez un fichier `**index.js**` dedans. Essentiellement, notre fonction reducer sera dans le chemin `**src/reducers/index.js**`.

Tout d'abord, exportez une fonction simple dans ce fichier :

```js
export default () => {
}
```

Souvenez-vous que le `reducer` prend deux arguments — comme établi précédemment. Pour l'instant, nous allons nous préoccuper du premier argument, `STATE`

Mettez cela dans la fonction, et nous avons ceci :

```js
export default (state) => {
}
```

Pas mal.

Un reducer retourne toujours quelque chose. Dans l'exemple initial du reducer `Array.reduce()`, nous avons retourné la **somme** de l'accumulateur et de la valeur actuelle.

Pour un reducer Redux, vous retournez toujours le `nouvel état` de votre application.

Laissez-moi expliquer.

Après être entré dans la banque et avoir effectué un retrait réussi, le montant actuel d'argent détenu dans le coffre de la banque pour vous n'est plus le même. Maintenant, si vous avez retiré 200 $, vous êtes maintenant à court de 200 $. Votre solde de compte est réduit de 200 $.

Encore une fois, le Caissier et le Coffre restent synchronisés sur le montant que vous avez maintenant.

C'est exactement ainsi que fonctionne le `reducer`.

Comme le Caissier, le `reducer` retourne toujours le `nouvel état` de votre application. Au cas où quelque chose aurait changé. Nous ne voulons pas émettre le même solde bancaire même si une action de retrait a été effectuée.

Nous aborderons les détails internes de la manière de changer/mettre à jour l'état plus tard. Pour l'instant, la confiance aveugle devra suffire.

Maintenant, revenons au problème en main.

Puisque nous ne nous préoccupons pas de changer/mettre à jour l'état à ce stade, nous allons garder le `nouvel état` retourné comme étant le même `état` passé en entrée.

Voici la représentation de ceci dans le `reducer` :

```js
export default (state) => {
	    return state	
}
```

Si vous allez à la banque sans effectuer d'action, votre solde bancaire reste le même, n'est-ce pas ?

Puisque nous n'effectuons aucune `ACTION` ou même ne la passons pas encore au reducer, nous allons simplement `retourner` le même `état`.

### Le Deuxième Argument de `createStore`

Lorsque vous rendez visite au Caissier à la banque, si vous lui demandiez votre solde de compte, il le consulterait et vous le dirait.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7Z2A1be7Q5o1La-H5RUs3w.png)
_Combien ?_

Mais comment ?

Lorsque vous avez créé un compte pour la première fois avec votre banque, vous l'avez fait soit avec un certain montant de dépôt, soit sans.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HoWXgJi3r-hTAwNk46AnHA.png)
_Euh, j'ai besoin d'un nouveau compte avec un dépôt initial de 500 $_

Appelons cela le Dépôt Initial sur votre compte.

Retour à Redux.

De la même manière, lorsque vous créez un `STORE` Redux (notre propre coffre de conservation d'argent), il y a l'option de le faire avec un dépôt initial.

En termes Redux, cela s'appelle l'`initialState` de l'application.

En pensant en code, `initialState` est le deuxième argument passé dans l'appel de la fonction `createStore`.

```js
const store = createStore(reducer, initialState);
```

Avant de faire toute action monétaire, si vous demandiez votre solde bancaire, le Dépôt Initial vous serait toujours retourné.

Par la suite, chaque fois que vous effectuez une action monétaire, ce dépôt initial sera également mis à jour.

Maintenant, il en va de même pour Redux.

L'objet passé en tant que `initialState` est comme le dépôt initial au Coffre. Cet `initialState` sera toujours retourné en tant qu'`état` de l'application à moins que vous ne mettiez à jour l'état en effectuant une `action`.

Nous allons maintenant mettre à jour l'application pour passer un `état initial` :

```js
const initialState = { tech: "React " };
const store = createStore(reducer, initialState);
```

Notez comment `initialState` est juste un objet, et c'est exactement ce que nous avions comme état par défaut dans l'application React avant de commencer la refactorisation.

Maintenant, voici tout le code que nous avons à ce stade — avec le `reducer` également importé dans `App.`

`**App.js**`

```js
import React, { Component } from "react";
import HelloWorld from "./HelloWorld";
import reducer from "./reducers";
import { createStore } from "redux";  

const initialState = { tech: "React " };
const store = createStore(reducer, initialState);

class App extends Component {
 render() {
   return <HelloWorld tech={this.state.tech}/>
 }
 }

export default App;
```

`**reducers/index.js**`

```js
export default state  => {
	    return state	
}
```

Si vous codez et essayez d'exécuter l'application maintenant, vous obtiendrez une erreur. Pourquoi ?

Jetez un coup d'œil à la prop `tech` passée dans `<HelloWorld />`. Elle indique toujours `this.state.tech`.

Il n'y a plus d'objet state attaché à `<App />`, donc cela sera `undefined`.

Corrigeons cela.

La solution est assez simple. Puisque le `store` gère maintenant l'état de notre application, cela signifie que l'objet `STATE` de l'application doit être récupéré depuis le `store`. Mais comment ?

Chaque fois que vous créez un store avec `createStore()`, le store créé a trois méthodes exposées.

L'une d'entre elles est `getState()`.

À tout moment, l'appel de la méthode `getState` sur le `store` créé retournera l'état actuel de votre application.

Dans notre cas, `store.getState()` retournera l'objet `{ tech: "React"}` puisque c'est l'`ÉTAT INITIAL` que nous avons passé dans la méthode `createStore()` lorsque nous avons créé le `STORE`.

Vous voyez comment tout cela s'assemble maintenant ?

Ainsi, la prop `tech` sera passée dans `<HelloWorld />` comme montré ci-dessous :

`**App.js**`

```js
import React, { Component } from "react";
import HelloWorld from "./HelloWorld";
import { createStore } from "redux";  

const initialState = { tech: "React " };
const store = createStore(reducer, initialState);  

class App extends Component {
 render() {
   return <HelloWorld tech={store.getState().tech}/>
 }
 }
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*d0zGDexx_UwReri6DLVPEg.png)
_Remplacer « this.state » par « store.getState() »_

`**Reducers/Reducer.js**`

```js
export default state => {
	    return state	
}
```

Et c'est tout ! Vous venez d'apprendre les bases de Redux et avez réussi à refactoriser une simple application React pour utiliser Redux.

L'application React a maintenant son état géré par Redux. Tout ce qui doit être obtenu de l'objet `state` sera récupéré du `store` comme montré ci-dessus.

Espérons que vous avez compris tout ce processus de refactorisation.

Pour un aperçu plus rapide, jetez un coup d'œil à cette [différence GitHub](https://github.com/ohansemmanuel/hello-redux/compare/solution?expand=1).

Avec le projet "Hello World", nous avons examiné certains concepts essentiels de Redux. Même s'il s'agit d'un projet si petit, il fournit une base décente sur laquelle construire !

### Piège Possible

Dans l'exemple **Hello World** que nous venons de conclure, une solution possible que vous auriez pu trouver pour récupérer l'`état` du `store` pourrait ressembler à ceci :

```js
class App extends Component {
  state = store.getState();
  render() {
    return <HelloWorld tech={this.state.tech} />;
  }
}
```

Qu'en pensez-vous ? Cela fonctionnera-t-il ?

Juste pour rappel, les deux façons suivantes sont des façons correctes d'initialiser l'état d'un composant React.

(a)

```js
class App extends Component {
 constructor(props) {
   super(props);
   this.state = {}
  }
}
```

(b)

```js
class App extends Component {
  state = {}
}
```

Alors, en revenant à la réponse à la question, oui, la solution fonctionnera très bien.

`store.getState()` récupérera l'état actuel du `STORE` Redux.

Cependant, l'affectation, `state = store.getState()` affectera l'état obtenu de Redux à celui du composant `<App />`.

Par implication, l'instruction de retour de `render` telle que `<HelloWorld tech={this.state.tech} />` sera valide.

Notez que cela lit `this.state.tech` **et non** `store.getState().tech`.

Même si cela fonctionne, cela va à l'encontre de la philosophie idéale de Redux.

Si, dans l'application, vous exécutez maintenant `this.setState()`, l'état de l'application sera mis à jour sans l'aide de Redux.

C'est le mécanisme React par défaut, et ce n'est pas ce que vous voulez. Vous voulez que l'`état` géré par le `STORE` Redux soit la seule source de vérité.

Que vous récupériez l'état, comme dans `store.getState()` ou que vous mettiez à jour/modifiiez l'`état` (comme nous le verrons plus tard), vous voulez que cela soit entièrement géré par Redux, et non par `setState()`.

Puisque Redux gère l'`état` de l'application, tout ce que vous avez à faire est de fournir l'`état` du `STORE` Redux en tant que props à tout composant requis.

Une autre grande question que vous vous posez probablement est "Pourquoi ai-je dû subir tout ce stress juste pour que l'état de mon App soit géré par Redux ?"

Reducer, Store, createStore blah, blah, blah …

Oui, je comprends.

Je me sentais de la même manière.

Cependant, considérez le fait que vous ne vous rendez pas simplement à la banque et que vous **ne** suivez **pas** un processus dû pour retirer votre propre argent. C'est votre argent, mais vous devez suivre un processus dû.

On pourrait en dire autant pour Redux.

Redux a son propre "processus" pour faire les choses. Nous devons apprendre comment cela fonctionne — et hé, vous ne vous en sortez pas mal !

### Conclusion et Résumé

Ce chapitre a été passionnant. Nous nous sommes principalement concentrés sur l'établissement d'une base décente pour les choses plus intéressantes à venir.

Voici quelques choses que vous avez apprises dans ce chapitre :

* Redux est un conteneur d'état **prévisible** pour les applications JavaScript.
* La fonction de fabrique `createStore` de Redux est utilisée pour créer un `STORE` Redux.
* Le `Reducer` est le seul argument obligatoire passé à `createStore()`
* Un `REDUCER` est simplement une fonction. Une fonction qui prend **deux** paramètres. Le premier est l'`ÉTAT` de l'application, et l'autre est une `ACTION`.
* Un `Reducer` retourne toujours le `nouvel état` de votre application.
* L'État Initial de votre application, `initialState` est le deuxième argument passé dans l'appel de la fonction `createStore`.
* `Store.getState()` retournera l'état actuel de votre application. Où `Store` est un `STORE` Redux valide.

### Introduction aux Exercices

S'il vous plaît, s'il vous plaît, s'il vous plaît, ne sautez pas les exercices. Surtout si vous n'êtes pas confiant quant à vos compétences Redux et que vous voulez vraiment tirer le meilleur parti de ce guide.

Alors, prenez vos chapeaux de développeur, et écrivez du code :)

De plus, si vous voulez que je vous donne des commentaires sur vos solutions à tout moment, tweetez-moi avec le hashtag **#UnderstandingRedux** et je serai ravi de jeter un coup d'œil. Je ne promets pas de répondre à chaque tweet, mais je vais définitivement essayer !

Une fois que vous avez trié les exercices, je vous verrai dans la section suivante.

N'oubliez pas qu'une bonne façon de lire du contenu long est de le diviser en morceaux plus courts et digestes. Ces exercices vous aident à faire exactement cela. Vous prenez un peu de temps, essayez de résoudre les exercices, puis vous revenez pour continuer à lire. C'est une manière efficace d'étudier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*utZ-bm-mOxuDVIERBCp0Nw.png)

Vous voulez voir mes solutions à ces exercices ? J'ai inclus les solutions aux exercices dans le package du livre. Vous trouverez des instructions sur la façon d'obtenir le code et les solutions des exercices accompagnants une fois que vous aurez téléchargé l'Ebook (PDF & Epub) (gratuit).

Alors, voici l'exercice pour cette section.

### Exercice

**(a) Refactoriser l'application de carte utilisateur pour utiliser Redux**

Dans les fichiers de code accompagnant le livre, vous trouverez une application de carte utilisateur écrite uniquement en React. L'état de l'application est géré via React. Votre tâche est de déplacer l'état pour qu'il soit géré uniquement par Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bS7K67iPR13f0yF2lO-anA.png)
_L'exercice : Application de carte utilisateur construite avec React. Refactoriser pour utiliser Redux._

### Chapitre 3 : Comprendre les Mises à Jour d'État avec les Actions

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lj-Vnna9wFACtnKKrr8eDA.png)

Maintenant que nous avons discuté des concepts fondamentaux de Redux, nous allons commencer à faire des choses plus intéressantes.

Dans ce chapitre, nous allons continuer à apprendre en faisant, car je vais vous guider à travers un autre projet — tout en expliquant chaque processus en détail.

Alors, quel projet allons-nous travailler cette fois-ci ?

J'ai celui qui est parfait.

Veuillez considérer la maquette ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FrKpOqcpaxYoOK3Xh2XELw.png)
_Design mis à jour de l'application Hello world._

Oh, cela ressemble exactement à l'exemple précédent — mais avec quelques changements. Cette fois-ci, nous allons prendre en compte les actions de l'utilisateur. Lorsque nous cliquons sur l'un des boutons, nous voulons mettre à jour l'état de l'application comme le montre le GIF ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cflSm-KpyU2S1Qt4px9BHQ.gif)
_Le GIF !_

Voici en quoi cela diffère de l'exemple précédent. Dans ce scénario, l'utilisateur effectue certaines actions qui influencent l'état de l'application. Dans l'exemple précédent, tout ce que nous avons fait était d'afficher l'état initial de l'application sans prendre en compte les actions de l'utilisateur.

### Qu'est-ce qu'une Action Redux ?

Lorsque vous entrez dans une banque, le Caissier reçoit votre action, c'est-à-dire votre intention de venir à la banque. Dans notre exemple précédent, il s'agissait de `RETRAIT_D'ARGENT`. La seule façon pour que l'argent quitte le Coffre de la banque est que vous fassiez connaître votre action ou intention au Caissier.

Maintenant, il en va de même pour le Reducer Redux.

Contrairement à `setState()` dans React pur, la seule façon de mettre à jour l'état d'une application Redux est de faire connaître votre intention au REDUCER.

Mais comment ?

En dispatchant des actions !

Dans le monde réel, vous savez exactement quelle action vous voulez effectuer. Vous pourriez probablement l'écrire sur un papier et le remettre au Caissier.

Cela fonctionne presque de la même manière avec Redux. Le seul défi est, comment décrire une action dans une application Redux ? Certainement pas en parlant par-dessus le comptoir ou en l'écrivant sur un papier.

Eh bien, il y a de bonnes nouvelles.

Une action est précisément décrite avec un objet JavaScript simple. Rien de plus.

Il y a juste une chose à savoir. Une action **doit** avoir un champ `type`. Ce champ décrit l'intention de l'action.

Dans l'histoire de la banque, si nous devions décrire votre action à la banque, cela ressemblerait à ceci :

```js
{
  type: "retirer_de_l'argent"
}
```

C'est tout, vraiment.

Une action Redux est décrite comme un objet simple.

Veuillez jeter un coup d'œil à l'action ci-dessus.

Pensez-vous que seul le champ `type` décrit avec précision votre action supposée de faire un retrait à une banque ?

Hmmm. Je ne pense pas. Et le montant d'argent que vous voulez retirer ?

De nombreuses fois, votre action aura besoin de données supplémentaires pour une description complète. Considérez l'action ci-dessous. Je soutiens que cela fait une action mieux décrite.

```js
{
  type: "retirer_de_l'argent",
  montant: "4000 $"
}
```

Maintenant, il y a suffisamment d'informations décrivant l'action. Pour l'exemple, ignorez tous les autres détails que l'action peut inclure, comme votre numéro de compte bancaire.

Autre que le champ `type`, la structure de votre Action Redux vous appartient vraiment.

Cependant, une approche courante consiste à avoir un champ `type` et un champ `payload` comme montré ci-dessous :

```js
{
  type: " ",
  payload: {}
}
```

Le champ `type` décrit l'action, et toutes les autres données/informations requises qui décrivent l'action sont mises dans l'objet `payload`.

Par exemple :

```js
{
  type: "retirer_de_l'argent",
  payload: {
     montant: "4000 $"
  }
}
```

Alors, oui ! C'est ce qu'est une action.

### Gestion des Réponses aux Actions dans le Reducer

Maintenant que vous comprenez avec succès ce qu'est une action, il est important de voir comment elles deviennent utiles dans un sens pratique.

Plus tôt, j'ai dit qu'un reducer prend **deux** arguments. Un `state`, l'autre `action`.

Voici à quoi ressemble un simple Reducer :

```js
function reducer(state, action) {
  //retourner un nouvel état
}
```

L'`action` est passée en tant que deuxième paramètre au Reducer. Mais nous n'avons rien fait avec elle dans la fonction elle-même.

Pour gérer les actions passées dans le reducer, vous écrivez généralement une instruction `switch` dans votre reducer, comme ceci :

```js
function reducer (state, action) {
	switch (action.type) {
		 case "retirer_de_l'argent":
			//faire quelque chose
			break;
		case "déposer-de-l'argent":
			 //faire quelque chose
			break;
		default:
			return state;
			 }
}
```

Certaines personnes semblent ne pas aimer l'instruction `switch`, mais c'est essentiellement un `if/else` pour les valeurs possibles sur un seul champ.

Le code ci-dessus va `switch` sur le `type` de l'action et faire quelque chose en fonction du type d'action passé. Techniquement, le bit _faire quelque chose_ est requis pour retourner un nouvel état.

Laissez-moi expliquer davantage.

Supposons que vous aviez deux boutons hypothétiques, le bouton #1 et le bouton #2, sur une certaine page web, et que votre objet state ressemblait à ceci :

```js
{
	 isOpen: true,
	 isClicked: false,
  }
```

Lorsque le bouton #1 est cliqué, vous voulez basculer le champ `isOpen`. Dans le contexte d'une application React, la solution est simple. Dès que le bouton est cliqué, vous feriez ceci :

```js
this.setState({isOpen: !this.state.isOpen})
```

De plus, supposons que lorsque le bouton #2 est cliqué, vous voulez mettre à jour le champ `isClicked`. Encore une fois, la solution est simple, et ressemble à ceci :

```js
this.setState({isClicked: !this.state.isClicked})
```

Bien.

Avec une application Redux, vous ne pouvez pas utiliser `setState()` pour mettre à jour l'objet state géré par Redux.

Vous devez d'abord dispatcher une action.

Supposons que les actions soient les suivantes :

**#1 :**

```js
{
	type: "is_open"
}
```

**#2 :**

```js
{
	type: "is_clicked"
}
```

Dans une application Redux, chaque action passe par le reducer.

Toutes. Donc, dans cet exemple, l'action #1 et l'action #2 passeront par le même reducer.

Dans ce cas, comment le reducer différencie-t-il chacune d'elles ?

Oui, vous avez deviné juste.

En basculant sur le `action.type`, nous pouvons gérer les deux actions sans problème.

Voici ce que je veux dire :

```js
function reducer (state, action) {
	switch (action.type) {
		case "is_open":
			return;  //retourner un nouvel état
		case "is_clicked":
			return; //retourner un nouvel état
		default:
		return state;
	}
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*CwuzXvAoX_OrADV7J8jY6w.png)

Maintenant, vous voyez pourquoi l'instruction `switch` est utile. Toutes les actions passeront par le reducer. Ainsi, il est important de gérer chaque type d'action séparément.

Dans la section suivante, nous allons continuer avec la tâche de construire la mini application ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cflSm-KpyU2S1Qt4px9BHQ.gif)

### Examen des Actions dans l'Application

Comme je l'ai expliqué précédemment, chaque fois qu'il y a une intention de mettre à jour l'état de l'application, une `action` doit être dispatchée.

Que cette intention soit initiée par un clic de l'utilisateur, un événement de timeout, ou même une requête Ajax, la règle reste la même. Vous devez dispatcher une action.

Il en va de même pour cette application.

Puisque nous avons l'intention de mettre à jour l'état de l'application, chaque fois que l'un des boutons est cliqué, nous devons dispatcher une action.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GRL5DOFenKGm3sTzYtWhFg.png)

Tout d'abord, décrivons les actions.

Essayez et voyez si vous y arrivez.

Voici ce que j'ai trouvé :

Pour le bouton React :

```js
{
    type: "SET_TECHNOLOGY",
    text: "React"
  }
```

Pour le bouton React-Redux :

```js
{
     type: "SET_TECHNOLOGY",
     text: "React-redux"
   }
```

Et enfin :

```js
{
   type: "SET_TECHNOLOGY",
  text: "Elm"
}
```

Facile, n'est-ce pas ?

Notez que les trois actions ont le même champ `type`. C'est parce que les trois boutons font tous la même chose. S'ils étaient des clients dans une banque, alors ils déposeraient tous de l'argent, mais des montants différents. Le `type` d'action serait alors `DEPOSER_DE_L'ARGENT` mais avec des champs `montant` différents.

De plus, vous remarquerez que le type d'action est écrit en majuscules. C'était intentionnel. Ce n'est pas obligatoire, mais c'est un style assez populaire dans la communauté Redux.

Espérons que vous comprenez maintenant comment j'ai créé les actions.

#### Introduction aux Créateurs d'Actions

Jetez un coup d'œil aux actions que nous avons créées ci-dessus. Vous remarquerez que nous répétons quelques choses.

Pour commencer, elles ont toutes le même champ `type`. Si nous devions dispatcher ces actions à plusieurs endroits, nous devrions les dupliquer partout. Ce n'est pas très bon. Surtout parce que c'est une bonne idée de garder votre code DRY.

Pouvons-nous faire quelque chose à ce sujet ?

Bien sûr !

Bienvenue, Créateurs d'Actions.

Redux a tous ces noms fantaisistes, hein ? Reducers, Actions, et maintenant, Créateurs d'Actions :)

Laissez-moi vous expliquer ce que sont ces derniers.

Les Créateurs d'Actions sont simplement des fonctions qui vous aident à créer des actions. C'est tout. Ce sont des fonctions qui retournent des objets d'action.

Dans notre exemple particulier, nous pourrions créer une fonction qui prendra un paramètre `text` et retournera une action, comme ceci :

```js
export function setTechnology (text) {
  return {
     type: "SET_TECHNOLOGY",
     tech: text
   }
}
```

Maintenant, nous n'avons plus à nous soucier de dupliquer du code partout. Nous pouvons simplement appeler le créateur d'action `setTechnology` à tout moment, et nous obtiendrons une action en retour !

Quelle bonne utilisation des fonctions.

En utilisant ES6, le créateur d'action que nous avons créé ci-dessus pourrait être simplifié en ceci :

```js
const setTechnology = text => ({ type: "SET_TECHNOLOGY", text });
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*I9y06GVVAKfCrSJ_-TvBcw.png)

Maintenant, c'est fait.

### Tout Rassembler

J'ai discuté de tous les composants importants nécessaires pour construire l'application Hello World plus avancée de manière isolée dans les sections précédentes.

Maintenant, mettons tout ensemble et construisons l'application. Excité ?

Tout d'abord, parlons de la structure des dossiers.

Lorsque vous arrivez à la banque, le Caissier est probablement assis dans son propre box/bureau. Le Coffre est également gardé en sécurité dans une pièce sécurisée. Pour de bonnes raisons, les choses semblent un peu plus organisées de cette manière. Chacun dans son propre espace.

On pourrait en dire autant pour Redux.

Il est courant que les principaux acteurs d'une application redux vivent dans leur propre dossier/répertoire.

Par acteurs, je veux dire, le `reducer`, les `actions`, et le `store`.

Il est courant de créer trois dossiers différents dans votre répertoire d'application, et de nommer chacun d'après ces acteurs.

Ce n'est pas une obligation — et inévitablement, vous décidez de la manière dont vous souhaitez structurer votre projet. Pour les grandes applications, cependant, c'est certainement une pratique assez décente.

Nous allons maintenant refactoriser les répertoires actuels de l'application que nous avons. Créez quelques nouveaux répertoires/dossiers. Un appelé `reducers`, un autre, `store`, et le dernier, `actions`

Vous devriez maintenant avoir une structure de composants qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KGLLK6HyMyeE0k73x8HLvQ.png)

Dans chacun des dossiers, créez un fichier `index.js`. Ce sera le point d'entrée pour chacun des acteurs Redux (reducers, store, et actions). Je les appelle acteurs, comme des acteurs de cinéma. Ils sont les principaux composants d'un système Redux.

Maintenant, nous allons refactoriser l'application précédente du **Chapitre 2 : Votre Première Application Redux**, pour utiliser cette nouvelle structure de répertoire.

`**store/index.js**`

```js
import { createStore } from "redux";
import reducer from "../reducers";

const initialState = { tech: "React " };
export const store = createStore(reducer, initialState);
```

C'est exactement comme nous avions avant. La seule différence est que le store est maintenant créé dans son propre fichier `index.js`, comme avoir des cubicles/bureaux séparés pour les différents acteurs Redux.

Maintenant, si nous avons besoin du store n'importe où dans notre application, nous pouvons l'importer en toute sécurité, comme dans `import store from "./store";`

Cela dit, le fichier `App.js` pour cet exemple particulier est légèrement différent de l'ancien.

`**App.js**`

```js
import React, { Component } from "react";
import HelloWorld from "./HelloWorld";
import ButtonGroup from "./ButtonGroup";
import { store } from "./store";

class App extends Component {
  render() {
    return [
      <HelloWorld key={1} tech={store.getState().tech} />,
      <ButtonGroup key={2} technologies={["React", "Elm", "React-redux"]} />
    ];
  }
}

export default App;
```

Qu'est-ce qui est différent ?

À la ligne 4, le store est importé depuis son propre 'cubicle'. De plus, il y a maintenant un composant `<ButtonGroup />` qui prend un tableau de technologies et génère des boutons. Le composant `ButtonGroup` gère le rendu des trois boutons sous le texte "Hello World".

![Image](https://cdn-media-1.freecodecamp.org/images/1*VCqQQuHPD5EVKGuLvwJ31Q.png)

De plus, vous pouvez remarquer que le composant `App` retourne un tableau. C'est une nouveauté de `React 16`. Avec React 16, vous n'avez pas à envelopper les éléments `JSX` adjacents dans une `div`. Vous pouvez utiliser un tableau si vous le souhaitez — mais passez une prop `key` à chaque élément du tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KLyFCPIyUBYPLcZ0JaAQTQ.png)

C'est tout pour le composant `App.js`.

L'implémentation du composant `ButtonGroup` est assez simple. La voici :

`**ButtonGroup.js**`

```js
import React from "react";

const ButtonGroup = ({ technologies }) => (
  <div>
    {technologies.map((tech, i) => (
      <button
        data-tech={tech}
        key={`btn-${i}`}
        className="hello-btn"
      >
        {tech}
      </button>
    ))}
  </div>
);

export default ButtonGroup;
```

`ButtonGroup` est un composant sans état qui prend un tableau de technologies, désigné par `technologies`.

Il parcourt ce tableau en utilisant `map` et rend un `<button></button` pour chaque technologie dans le tableau.

Dans cet exemple, le tableau de boutons passé est `["React", "Elm", "React-redux"]`

Les boutons générés ont quelques attributs. Il y a l'évident `className` pour des raisons de style. Il y a `key` pour éviter l'avertissement ennuyeux de React concernant le rendu de plusieurs éléments sans une prop key. Mon Dieu, cette erreur me hante à chaque fois :(

Enfin, il y a un attribut `data-tech` sur chaque `button` aussi. Cela s'appelle un [attribut de données](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes). C'est une façon de stocker quelques informations supplémentaires qui n'ont aucune représentation visuelle. Cela rend légèrement plus facile la récupération de certaines valeurs d'un élément.

Un bouton complètement rendu ressemblera à ceci :

```js
<button 
  data-tech="React" 
  key="btn-1" 
  className="hello-btn"> React </button>
```

Pour l'instant, tout se rend correctement, mais lorsque l'on clique sur le bouton, rien ne se passe encore.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CDsM2ZMgAVYiBfdfeHXg1A.gif)

Eh bien, c'est parce que nous n'avons pas encore fourni de gestionnaires de clics. Faisons cela maintenant.

Dans la fonction `render`, mettons en place un gestionnaire `onClick` :

```js
<div>
    {technologies.map((tech, i) => (
      <button
        data-tech={tech}
        key={`btn-${i}`}
        className="hello-btn"
        onClick={dispatchBtnAction}
      >
        {tech}
      </button>
    ))}
  </div>
```

Bien. Écrivons maintenant le `dispatchBtnAction`.

N'oubliez pas que le seul but de ce gestionnaire est de dispatcher une action lorsqu'un clic s'est produit.

Par exemple, si vous cliquez sur le bouton React, dispatch l'action :

```js
{
    type: "SET_TECHNOLOGY",
    tech: "React"
  }
```

Si vous cliquez sur le bouton React-Redux, dispatch cette action :

```js
{
     type: "SET_TECHNOLOGY",
     tech: "React-redux"
   }
```

Alors, voici la fonction `dispatchBtnAction`.

```js
function dispatchBtnAction(e) {
  const tech = e.target.dataset.tech;
  store.dispatch(setTechnology(tech));
}
```

Hmmm. Le code ci-dessus a-t-il du sens pour vous ?

`e.target.dataset.tech` obtiendra l'attribut de données défini sur le bouton, `data-tech`. Ainsi, `tech` contiendra la valeur du texte.

`store.dispatch()` est la manière dont vous dispatch une action dans Redux, et `setTechnology()` est le créateur d'action que nous avons écrit plus tôt !

```js
function setTechnology (text) {
  return {
     type: "SET_TECHNOLOGY",
     text: text
   }
}
```

J'ai ajouté quelques commentaires dans l'illustration ci-dessous, juste pour que vous compreniez le code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DKChwIKGbICadjllMPelLg.png)

Comme vous le savez déjà, `store.dispatch` attend un objet d'action, et rien d'autre. N'oubliez pas le créateur d'action `setTechnology`. Il prend le texte du bouton et retourne l'action requise.

De plus, la `tech` du bouton est récupérée à partir du jeu de données du bouton. Vous voyez, c'est exactement pourquoi j'avais un attribut `data-tech` sur chaque bouton. Pour que nous puissions facilement récupérer la tech de chacun des boutons.

Maintenant, nous dispatchons les bonnes actions. Peut-on dire si cela fonctionne comme prévu maintenant ?

### Actions Dispatchées. Cela Fonctionne-t-il ?

Tout d'abord, voici une courte question de quiz. Après avoir cliqué sur un `button` et par conséquent dispatché une action, que se passe-t-il ensuite dans Redux ? Quels sont les acteurs Redux qui entrent en jeu ?

Simple. Lorsque vous allez à la banque avec une action `RETIRER_DE_L'ARGENT`, à qui allez-vous ? Au Caissier, oui.

Même chose ici. Les actions, lorsqu'elles sont dispatchées, passent par le reducer.

Pour le prouver, je vais logger toute action qui arrive dans le reducer.

`**reducers/index.js**`

```js
export default (state, action) => {
  console.log(action);
  return state;
};
```

Le reducer retourne ensuite le nouvel état de l'application. Dans notre cas particulier, nous retournons simplement le même `état` initial.

Avec le `console.log()` dans le reducer, voyons ce qui se passe lorsque nous cliquons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wz3mgvrjStRarPhrh04Dpw.gif)

Oh, oui !

Les actions sont loggées lorsque les boutons sont cliqués. Ce qui prouve que les actions passent effectivement par le Reducer. Incroyable !

Il y a une chose de plus cependant. Dès que l'application démarre, une action étrange est également loggée. Elle ressemble à ceci :

```js
{type: "@@redux/INITu.r.5.b.c"}
```

Qu'est-ce que c'est ?

Eh bien, ne vous inquiétez pas trop de cela. C'est une action passée par Redux lui-même lors de la configuration de votre application. Elle est généralement appelée l'action `init` de Redux, et elle est passée au reducer lorsque Redux initialise votre application avec l'état initial de l'application.

Maintenant, nous sommes sûrs que les actions passent effectivement par le Reducer. Super !

Bien que ce soit excitant, la seule raison pour laquelle vous allez voir le Caissier avec une demande de retrait est parce que vous voulez de l'argent. Si le Reducer ne prend pas l'action que nous passons et ne fait rien avec notre action, quelle est sa valeur ?

### Faire Compter le Reducer

Jusqu'à présent, le reducer sur lequel nous avons travaillé n'a rien fait de particulièrement intelligent. C'est comme un Caissier qui est nouveau dans le travail et ne fait rien avec notre intention de `RETIRER_DE_L'ARGENT`.

Qu'attendons-nous exactement du reducer ?

Pour l'instant, voici l'`initialState` que nous avons passé à `createStore` lorsque le `STORE` a été créé.

```js
const initialState = { tech: "React" };
export const store = createStore(reducer, initialState);
```

Lorsque l'utilisateur clique sur l'un des boutons, passant ainsi une action au reducer, le nouvel état que nous attendons du reducer doit contenir le texte de l'action !

Voici ce que je veux dire.

L'état actuel est `{ tech: "React"}`

Étant donné une nouvelle action de type `SET_TECHNOLOGY`, et le texte, `React-Redux` :

```js
{
	    type: "SET_TECHNOLOGY",
	    text: "React-Redux"
}
```

À quoi vous attendez-vous que le nouvel état soit ?

Oui, `{tech: "React-Redux"}`

La seule raison pour laquelle nous avons dispatché une action est parce que nous voulons un nouvel état d'application !

Comme je l'ai mentionné précédemment, la manière courante de gérer différents types d'actions dans un reducer est d'utiliser l'instruction JavaScript `switch` comme montré ci-dessous :

```js
export default (state, action) => {
  switch (action.type) {
    case "SET_TECHNOLOGY":
      //faire quelque chose.

    default:
      return state;
  }
};
```

Maintenant, nous faisons un `switch` sur le `type` de l'action. Mais pourquoi ?

Eh bien, si vous alliez voir un Caissier, vous pourriez avoir de nombreuses actions différentes en tête.

Vous pourriez vouloir `RETIRER_DE_L'ARGENT`, ou `DEPOSER_DE_L'ARGENT` ou peut-être juste `DIRE_BONJOUR`.

Le Caissier est intelligent, donc il prend votre action et répond en fonction de votre intention.

C'est exactement ce que nous faisons avec le Reducer.

L'instruction `switch` vérifie le `type` de l'action.

Que voulez-vous faire ? Retirer, déposer, peu importe...

Après cela, nous gérons les `cases` connues que nous attendons. Pour l'instant, il n'y a qu'un seul `case` qui est `SET_TECHNOLOGY`.

Et par défaut, assurez-vous de simplement retourner l'`état` de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JcmpiTNT-StwOpmnrK-Sww.png)

Jusqu'à présent, tout va bien.

Le Caissier (`Reducer`) comprend maintenant notre action. Cependant, ils ne nous donnent pas encore d'argent (`état`).

Faisons quelque chose dans le `case`.

Voici la version mise à jour du reducer. Celui qui nous donne effectivement de l'argent :)

```js
export default (state, action) => {
  switch (action.type) {
    case "SET_TECHNOLOGY":
      return {
        ...state,
        tech: action.text
      };

    default:
      return state;
  }
};
```

Ah, oui !

Vous voyez ce que je fais là ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*huM6oRFU4eTpsCW6JQwRCQ.png)

Je vais expliquer ce qui se passe dans la section suivante.

### Ne Mutatez Jamais l'État Dans les Reducers

Lorsque vous retournez `state` depuis les reducers, il y a quelque chose qui peut vous dérouter au début. Cependant, si vous écrivez déjà du bon code React, alors vous devriez être familier avec cela.

Vous ne devriez pas muter le `state` reçu dans votre Reducer. Au lieu de cela, vous devriez toujours retourner une nouvelle copie de l'état.

Techniquement, vous ne devriez jamais faire ceci :

```js
export default (state, action) => {
  switch (action.type) {
    case "SET_TECHNOLOGY":
      state.tech = action.text; 
      return state;

    default:
      return state;
  }
};
```

C'est exactement pourquoi le reducer que j'ai écrit a retourné ceci :

```js
return {
        ...state,
        tech: action.text
  };
```

Au lieu de muter (ou changer) l'état reçu du reducer, je retourne un **nouvel** objet. Cet objet a toutes les propriétés de l'objet d'état précédent. Grâce à l'opérateur de propagation ES6, `...state`. Cependant, le champ `tech` est mis à jour avec ce qui provient de l'action, `action.text.`

De plus, chaque Reducer que vous écrivez devrait être une fonction pure sans effets secondaires — pas d'appels API ou de mise à jour d'une valeur en dehors de la portée de la fonction.

Vous avez compris ?

Espérons que oui.

Maintenant, le Caissier n'ignore plus nos actions. Ils nous donnent en fait de l'argent maintenant !

Après avoir fait cela, cliquez sur les boutons. Est-ce que cela fonctionne maintenant ?

Mon Dieu, cela ne fonctionne toujours pas. Le texte ne se met pas à jour.

Qu'est-ce qui ne va pas cette fois-ci ?

### S'abonner aux Mises à Jour du Store

Lorsque vous vous rendez à la banque, faites connaître votre action de `RETRAIT` au Caissier, et recevez avec succès votre argent — alors, quelle est la suite ?

Très probablement, vous recevrez une alerte par e-mail/texte ou une autre notification mobile disant que vous avez effectué une transaction, et que votre nouveau solde de compte est tel et tel.

Si vous ne recevez pas de notifications mobiles, vous recevrez définitivement une sorte de "reçu personnel" pour montrer qu'une transaction réussie a été effectuée sur votre compte.

D'accord, notez le flux. Une action a été initiée, vous avez reçu votre argent, vous avez obtenu une alerte pour une transaction réussie.

Nous semblons avoir un problème avec notre code Redux.

Une action a été initiée avec succès, nous avons reçu de l'argent (état), mais hé, où est l'alerte pour une mise à jour réussie de l'état ?

Nous n'en avons aucune.

Eh bien, il y a une solution. Là d'où je viens, vous vous abonnez pour recevoir des notifications de transaction de la banque soit par e-mail/texte.

Il en va de même pour Redux. Si vous voulez les mises à jour, vous devez vous y abonner.

Mais comment ?

Le store Redux, quel que soit le store que vous créez, a une méthode appelée `subscribe` comme ceci : `store.subscribe()`.

Une fonction bien nommée, si vous me demandez !

L'argument passé à `store.subscribe()` est une fonction, et elle sera invoquée chaque fois qu'il y a une mise à jour de l'état.

Pour ce qu'elle vaut, veuillez vous souvenir que l'**argument** passé à `store.subscribe()` doit être une **fonction**. D'accord ?

Maintenant, profitons de cela.

Réfléchissez-y. Après que l'état est mis à jour, que voulons-nous ou attendons-nous ? Nous attendons un re-rendu, n'est-ce pas ?

Alors, l'état a été mis à jour. Redux, s'il vous plaît, re-rendez l'application avec les nouvelles valeurs d'état.

Jetons un coup d'œil à l'endroit où l'application est rendue dans `index.js`

Voici ce que nous avons.

```js
ReactDOM.render(<App />, document.getElementById("root")
```

C'est la ligne qui rend l'application entière. Elle prend le composant `App/>` et le rend dans le DOM. L'ID `root` pour être précis.

Tout d'abord, abstrayons cela dans une fonction.

Voyez ceci :

```js
const render = function() {
  ReactDOM.render(<App />, document.getElementById("root")
}
```

Puisque cela est maintenant dans une fonction, nous devons invoquer la fonction pour `render` l'application.

```js
const render = function() {
   ReactDOM.render(<App />, document.getElementById("root")
}
render()
```

Maintenant, le `<App />` sera rendu comme avant.

En utilisant quelques fonctionnalités ES6, la fonction peut être simplifiée.

```js
const render = () => ReactDOM.render(<App />, document.getElementById("root"));

render();
```

Le fait que le rendu du `<App/>` soit encapsulé dans une fonction signifie que nous pouvons maintenant nous abonner aux mises à jour du store comme ceci :

```js
store.subscribe(render);
```

Où `render` est toute la logique de rendu pour le `<App />` — celle que nous venons de refactoriser.

Vous comprenez ce qui se passe ici, n'est-ce pas ?

À chaque fois qu'il y a une mise à jour réussie du store, le `<App/>` sera maintenant re-rendu avec les nouvelles valeurs d'état.

Pour plus de clarté, voici le composant `<App/>` :

```js
class App extends Component {
  render() {
    return [
      <HelloWorld key={1} tech={store.getState().tech} />,
      <ButtonGroup key={2} technologies={["React", "Elm", "React-redux"]} />
    ];
  }
}
```

Chaque fois qu'un re-rendu se produit, `store.getState()` à la ligne 4 récupérera maintenant l'état mis à jour.

Voyons si l'application fonctionne maintenant comme prévu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cflSm-KpyU2S1Qt4px9BHQ.gif)

Oui ! Cela fonctionne, et je savais que nous pouvions le faire !

Nous dispatchons avec succès une action, recevons de l'argent du Caissier, puis nous abonnons pour recevoir des notifications. Parfait !

### Note Importante sur l'Utilisation de store.subscribe()

Il y a quelques mises en garde à l'utilisation de `store.subscribe()` comme nous l'avons fait ici. C'est une API Redux de bas niveau.

En production, et largement pour des raisons de performance, vous utiliserez probablement des liaisons telles que `react-redux` lorsque vous traiterez avec des applications plus grandes. Pour l'instant, il est sûr de continuer à utiliser `store.subscribe()` à des fins d'apprentissage.

Dans l'un des [commentaires de PR](https://github.com/reduxjs/redux/pull/1289) les plus beaux que j'ai vus depuis longtemps, Dan Abramov, dans l'un des exemples d'application Redux, a dit :

> Le nouvel exemple Counter Vanilla vise à dissiper le mythe selon lequel Redux nécessite Webpack, React, le rechargement à chaud, les sagas, les créateurs d'actions, les constantes, Babel, npm, les modules CSS, les décorateurs, un abonnement Egghead, un doctorat, ou un niveau O.W.L. Exceeds Expectations.

Je crois la même chose.

Lorsque vous apprenez Redux, surtout si vous débutez, vous pouvez vous passer de tant d'"extras" que possible.

Apprenez à **marcher** d'abord, puis vous pourrez **courir** autant que vous le souhaitez.

### D'accord, Avons-nous Fini ?

Oui, nous avons techniquement fini. Cependant, il y a une chose de plus que j'aimerais vous montrer. Je vais ouvrir les outils de développement de mon navigateur et activer le paint-flashing.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jr9Cew3Wn5zYRo9rVkblQg.png)

Maintenant, lorsque nous cliquons et mettons à jour l'état de l'application, notez les flashes verts qui apparaissent à l'écran. Les flashes verts représentent les parties de l'application qui sont repeintes ou re-rendues par le moteur du navigateur.

Jetez un coup d'œil :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ij_Zo6lOfrKpWsX2z5J7EA.gif)

Comme vous pouvez le voir, même si cela semble que la fonction `render` est invoquée chaque fois qu'une mise à jour d'état est effectuée, ce n'est pas toute l'application qui est re-rendue. Seule la composante avec une nouvelle valeur d'état est re-rendue. Dans ce cas, le composant `<HelloWorld/>`.

Une chose de plus.

Si l'état actuel de l'application rend, `Hello World React`, cliquer à nouveau sur le bouton `React` ne re-rend pas puisque la valeur de l'état est la même.

Bien !

C'est l'algorithme de `Diff` du DOM virtuel React qui fonctionne ici. Si vous connaissez un peu React, vous devez avoir entendu cela auparavant.

Alors, oui. Nous avons terminé avec cette section ! Je m'amuse tellement à expliquer cela. J'espère que vous appréciez aussi la lecture.

### Conclusion et Résumé

Pour une application supposément simple, ce chapitre était plus long que vous ne l'aviez probablement anticipé. Mais c'est bien. Vous êtes maintenant équipé de connaissances encore plus grandes sur le fonctionnement de Redux.

Voici quelques choses que vous avez apprises dans ce chapitre :

* Contrairement à `setState()` dans React pur, la seule façon de mettre à jour l'état d'une application Redux est de dispatcher une action.
* Une action est précisément décrite avec un objet JavaScript simple, mais elle doit avoir un champ `type`.
* Dans une application Redux, chaque action passe par le reducer. Toutes.
* En utilisant une instruction `switch`, vous pouvez gérer différents types d'actions dans votre Reducer.
* Les Action Creators sont simplement des fonctions qui retournent des objets d'action.
* Il est courant de faire vivre les principaux acteurs d'une application redux dans leur propre dossier/répertoire.
* Vous ne devriez pas muter le `state` reçu dans votre Reducer. Au lieu de cela, vous devriez toujours retourner une nouvelle copie de l'état.
* Pour vous abonner aux mises à jour du store, utilisez la méthode `store.subscribe()`.

### Exercices

D'accord, maintenant c'est à vous de faire quelque chose de cool.

1. Dans les fichiers d'exercice, j'ai mis en place une simple application React qui modélise une application bancaire d'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2nNVTPKo4JiP8giwvOAxIg.png)

Jetez un bon coup d'œil à la maquette ci-dessus. En plus de permettre à l'utilisateur de voir son solde total, il peut également effectuer des actions de retrait.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GjQU6EInejsQqv9MggQL7g.png)

Le `nom` et le `solde` de l'utilisateur sont stockés dans l'état de l'application.

```js
{
  name: "Ohans Emmanuel",
  balance: 1559.30
}
```

Il y a deux choses que vous devez faire.

(i) Refactoriser l'état de l'application pour qu'il soit géré uniquement par Redux.

(ii) Gérer les actions de retrait pour effectivement réduire le solde de l'utilisateur (c'est-à-dire, en cliquant sur les boutons, le solde diminue).

Vous devez le faire uniquement via Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*utZ-bm-mOxuDVIERBCp0Nw.png)

Pour rappel, après avoir téléchargé l'Ebook, vous trouverez des instructions sur la façon d'obtenir les fichiers de code accompagnants, les fichiers d'exercice et les solutions des exercices également.

2. L'image suivante est celle d'un compteur de temps créé en tant qu'application React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pcRuv8kL7TzQErA7V2p8kg.png)

L'objet state ressemble à ceci :

```js
{
  days: 11,
  hours: 31,
  minutes: 27,
  seconds: 11,
  activeSession: "minutes"
}
```

Selon la session active, cliquer sur l'un des boutons "augmenter" ou "diminuer" doit mettre à jour la valeur affichée dans le compteur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l6KyblB5d-1j2JSIH4ETdw.png)

Il y a deux choses que vous devez faire.

(i) Refactoriser l'état de l'application pour qu'il soit géré uniquement par Redux.

(ii) Gérer les actions d'augmentation et de diminution pour affecter réellement le temps affiché sur le compteur.

### Chapitre 4 : Construire Skypey : Un Exemple Plus Avancé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*itX4GQXZ8hrq5Fr7t3zQyg.png)

Nous avons parcouru un long chemin, et je vous salue pour avoir suivi.

Dans cette section, je vais vous guider à travers le processus de construction d'un exemple plus avancé.

Même si nous avons couvert beaucoup de terrain sur les bases de Redux, je pense vraiment que cet exemple vous donnera une perspective plus profonde sur la façon dont certains des concepts que vous avez appris fonctionnent à plus grande échelle.

Nous parlerons de la planification de votre application, de la conception et de la normalisation de l'objet d'état, et bien plus encore. Les applications réelles nécessitent bien plus que Redux. Vous aurez encore besoin de CSS et de React.

Attachez vos ceintures, car ce sera un long voyage qui en vaut la peine !

### Planification de l'Application

D'accord. Voici la grande question. Que faites-vous généralement en premier lorsque vous commencez une nouvelle application React ?

Eh bien, nous avons tous nos préférences.

Décomposez-vous toute l'application en composants et construisez-vous de bas en haut ?

Commencez-vous par la disposition générale de l'application d'abord ?

Et l'objet d'état de votre application ? Passez-vous également du temps à y réfléchir ?

Il y a effectivement beaucoup de choses à prendre en considération. Je vous laisse avec votre manière préférée de faire les choses.

En construisant **Skypey**, je vais adopter une approche de haut en bas. Nous allons discuter de la disposition générale de l'application, puis de la conception de l'objet d'état de l'application, puis nous allons construire les plus petits composants.

Encore une fois, il n'y a pas de manière parfaite de faire cela. Pour un projet plus complexe, peut-être qu'une approche de bas en haut conviendrait mieux.

Une fois de plus, voici le résultat final que nous visons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3VVJuwBx5J-A4A4n5FhKcg.gif)
_L'application Skypey_

### Résolution de la Disposition Initiale de l'Application

À partir de l'interface de ligne de commande, créez une nouvelle application React avec `create-react-app`, et appelez-la `Skypey`.

```bash
create-react-app Skypey
```

La disposition de Skypey est une simple disposition à 2 colonnes. Une barre latérale de largeur fixe à gauche, et à droite une section principale qui prend le reste de la largeur de la fenêtre.

Voici une note rapide sur la façon dont cette application est stylisée.

Si vous êtes un ingénieur plus expérimenté, assurez-vous d'utiliser la solution CSS dans JavaScript qui fonctionne pour vous. Pour simplifier, je vais styliser l'application _Skypey_ avec du bon vieux CSS — rien de plus.

Commençons.

Créez deux nouveaux fichiers, `Sidebar.js` et `Main.js` dans le répertoire racine.

Comme vous l'avez peut-être deviné, lorsque nous aurons construit les composants `Sidebar` et `Main`, nous les rendrons dans le composant `App` comme ceci :

`**App.js**`

```js
const App = () => {
  return (
    <div className="App">
      <Sidebar />
      <Main />
    </div>
  );
};
```

Je suppose que vous êtes familier avec la structure d'un projet `create-react-app`. Il y a le point d'entrée de l'application, `index.js` qui rend un composant `App`.

Avant de passer à la construction des composants Sidebar et Main, d'abord un peu de ménage CSS. Assurez-vous que le nœud DOM où l'application est rendue, `#root`, prend toute la hauteur de la fenêtre.

`**index.css**`

```css
#root {
  height: 100vh;
}
```

Pendant que vous y êtes, vous devriez également supprimer tout espacement indésirable du `body` :

```css
body {
  margin: 0;
  padding: 0;
  font-family:  sans-serif;
}
```

Bien !

La disposition de l'application sera structurée en utilisant **Flexbox**.

Faites fonctionner le jus de Flexbox en faisant de `.App` un `flex-container` et en vous assurant qu'il prend 100 % de la hauteur disponible.

`**App.css**`

```css
.App {
  height: 100%;
  display: flex;
  color: rgba(189, 189, 192, 1);
}
```

Maintenant, nous pouvons nous mettre à l'aise pour construire les composants `Sidebar` et `Main`.

Gardons cela simple pour l'instant.

`**Sidebar.js**`

```css
import React from "react";
import "./Sidebar.css";

const Sidebar = () => {
  return <aside className="Sidebar">Sidebar</aside>;
};

export default Sidebar;
```

Tout ce qui est rendu est le texte `Sidebar` dans un élément `<aside>`. Notez également qu'une feuille de style correspondante, `Sidebar.css`, a été importée.

Dans `Sidebar.css`, nous devons restreindre la largeur de la Sidebar, plus quelques autres styles simples.

`**Sidebar.css**`

```css
.Sidebar {
  width: 80px;
  background-color: rgba(32, 32, 35, 1);
  height: 100%;
  border-right: 1px solid rgba(189, 189, 192, 0.1);
  transition: width 0.3s;
}

/* pas de petits appareils  */
@media (min-width: 576px) {
  .Sidebar {
    width: 320px;
  }
}
```

En adoptant une approche mobile-first, la `width` de la Sidebar sera de `80px` et de `320px` sur les appareils plus grands.

D'accord, passons maintenant au composant `Main`.

Comme avant, nous allons garder cela simple.

Rendez simplement un texte simple dans un élément `<main>`.

Lors du développement d'applications, vous voulez être sûr de construire de manière progressive. En d'autres termes, construisez par morceaux, et assurez-vous que l'application fonctionne.

Voici le composant `<Main>` :

```css
import React from "react";
import "./Main.css";

const Main = () => {
  return <main className="Main">Main Stuff</main>;
};

export default Main;
```

Encore une fois, une feuille de style correspondante, `Main.css`, a été importée.

Avec les éléments rendus des deux `<Main />` et `<Sidebar />`, il existe les noms de classe CSS, `.Main` et `.Sidebar`.

Puisque les composants sont tous deux rendus dans `<App />`, les classes `.Sidebar` et `.Main` sont des enfants de la classe parente, `.App`.

N'oubliez pas que `.App` est un conteneur flex. Par conséquent, `.Main` peut être fait pour remplir l'espace restant dans la fenêtre comme ceci :

```css
.Main {
 flex: 1 1 0;
}
```

Maintenant, voici le code complet :

```css
.Main {
  flex: 1 1 0;
  background-color: rgba(25, 25, 27, 1);
  height: 100%;
}
```

C'était facile :)

Et voici le résultat de tout le code que nous avons écrit jusqu'à présent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V28qpoICjKfTnP_sk-XQ3w.png)
_Le résultat modeste avec les sections Sidebar et Main disposées._

Pas si excitant. Patience. Nous y arriverons.

Pour l'instant, la disposition de base de l'application est définie. Bien joué !

### Conception de l'Objet d'État

La manière dont les applications React sont créées est que votre application entière est principalement une fonction de l'objet `state`.

Que vous créiez une application sophistiquée ou quelque chose de simple, beaucoup de réflexion devrait être mise dans la manière dont vous allez structurer l'objet d'état de votre application.

Particulièrement lorsque vous travaillez avec Redux, vous pouvez réduire beaucoup de complexité en concevant correctement l'objet d'état.

Alors, comment faire cela correctement ?

Tout d'abord, considérons l'application Skypey.

Un utilisateur de l'application a plusieurs contacts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1eqg-bUg5VKpYj46wgKWLA.png)
_Les multiples contacts qu'un utilisateur peut avoir._

Chaque contact a à son tour un certain nombre de messages, constituant leur conversation avec l'utilisateur principal de l'application. Cette vue est activée lorsque vous cliquez sur l'un des contacts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZV5TFQLIirXkK2kDtipRA.png)
_Cliquer sur un contact affiche son message dans le panneau principal._

Par association, vous n'auriez pas tort d'avoir une image comme celle-ci dans votre esprit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FPioi1H_8bq2mtnmnHzTbQ.png)
_Hmmm… Une grande boîte utilisateur avec des contacts imbriqués_

Vous pourriez alors décrire l'état de l'application comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z5QQRJAbdM26JGSkEyFBew.png)
_Un grand tableau utilisateur avec des contacts imbriqués_

D'accord, en JavaScript simple, voici ce que vous auriez probablement :

```js
const state = {
  user: [
    {
      contact1: 'Alex',
      messages: [
        'msg1',
        'msg2',
        'msg3'
      ]
    },
    {
      contact2: 'john',
      messages: [
        'msg1',
        'msg2',
        'msg3'
      ]
    }
  ]
```

Dans l'objet `state` ci-dessus, il y a un champ `user` représenté par un grand tableau. Puisque l'utilisateur a un certain nombre de contacts, ceux-ci sont représentés par des objets dans le tableau. Oh, puisque il pourrait y avoir de nombreux messages différents, ceux-ci sont également stockés dans un tableau.

À première vue, cela peut sembler être une solution décente.

Mais est-ce le cas ?

Si vous deviez recevoir des données d'un backend, la structure pourrait ressembler exactement à cela !

Bien, n'est-ce pas ?

Non, mon ami. Pas si bien.

C'est une assez bonne représentation des données. Il semble qu'elle montre la relation entre chaque entité, mais en termes d'état de votre application front-end, c'est une mauvaise idée. Mauvais est un mot fort. Disons simplement qu'il y a une meilleure façon de faire cela.

Voici comment je le vois.

Si vous deviez gérer une équipe de football, un bon plan serait de choisir les meilleurs buteurs de l'équipe et de les placer à l'avant pour vous marquer des buts.

Vous pouvez argumenter que les bons joueurs peuvent marquer de n'importe où — oui. Je parie qu'ils seront plus efficaces lorsqu'ils seront bien positionnés devant le but de l'opposition.

Il en va de même pour l'objet d'état.

Choisissez les leaders de l'objet d'état et placez-les "à l'avant".

Lorsque je dis "leaders", je veux dire les champs de l'objet d'état sur lesquels vous effectuerez plus d'actions CRUD. Les parties de l'état que vous créerez, lirez, mettrez à jour et supprimerez plus souvent que d'autres. Les parties de l'état qui sont essentielles à l'application.

Ce n'est pas une règle immuable, mais c'est une bonne métrique à suivre.

En regardant l'objet d'état actuel et les besoins de notre application, nous pouvons choisir les "leaders" ensemble.

Pour commencer, nous allons lire le champ "Messages" assez souvent — pour chaque contact de l'utilisateur. Il y a aussi le besoin d'éditer et de supprimer un message de l'utilisateur.

Maintenant, c'est un leader.

Il en va de même pour les "Contacts" également.

Maintenant, plaçons-les "à l'avant".

Voici comment.

Au lieu d'avoir les champs "Messages" et "Contacts" imbriqués, choisissez-les et faites-en des clés primaires dans l'objet d'état. Comme ceci :

```js
const state = {
    user: [],
    messages: [
      'msg1',
      'msg2'
    ],
    contacts: ['Contact1', 'Contact2']
  }
```

C'est encore une représentation incomplète, mais nous avons grandement amélioré la représentation de l'objet d'état de l'application.

Maintenant, continuons.

Souvenez-vous qu'un utilisateur peut envoyer des messages à l'un de ses contacts. Pour l'instant, les champs `messages` et `contact` dans l'objet d'état sont indépendants.

Après avoir fait de ces champs des clés primaires dans l'objet d'état, il n'y a rien qui montre la relation entre un certain message et le contact associé. Ils sont indépendants, et ce n'est pas bien car nous devons savoir à qui appartient quelle liste de messages. Sans le savoir, comment affichons-nous les messages corrects lorsqu'un contact est cliqué ?

Aucune façon. Nous ne pouvons pas.

Voici une façon de gérer cela :

```js
const state = {
    user: [],
    messages: [
      {
        messageTo: 'contact1',
        text: "Hello"
      },
      {
        messageTo: 'contact2',
        text: "Hey!"
      }
    ],
    contacts: ['Contact1', 'Contact2']
  }
```

Donc, tout ce que j'ai fait est de faire du champ `messages` un tableau d'objets de messages. Des objets avec une clé `messageTo`. Cette clé montre à quel contact appartient un message particulier.

Nous nous rapprochons. Juste un peu de refactorisation, et nous avons terminé.

Au lieu d'un simple tableau, un utilisateur pourrait être mieux décrit par un objet — un objet `user`.

```js
user:  {
    name,
    email,
    profile_pic,
    status:,
    user_id
  }
```

Un utilisateur aura un nom, un email, une photo de profil, un statut de texte fantaisiste et un identifiant utilisateur unique. L'identifiant utilisateur est important — et doit être unique pour chaque utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NeUt-4ctfePHyEotEHtJyA.png)
_Un affichage visuel de certaines propriétés de l'utilisateur._

Réfléchissez-y. Les contacts d'une personne peuvent également être représentés par un objet utilisateur similaire.

Ainsi, le champ `contacts` dans l'objet d'état peut être représenté par une liste d'objets utilisateur.

```js
contacts: [
  {
    name,
    email,
    profile_pic,
    status,
    user_id
  },
  {
    name,
    email,
    profile_pic,
    status,
    user_id_2
  }
]
```

D'accord. Jusqu'à présent, tout va bien.

Le champ `contacts` est maintenant représenté par un grand tableau d'objets `user`.

Cependant, au lieu d'utiliser un tableau, nous pouvons avoir les `contacts` représentés par un objet également. Voici ce que je veux dire.

Au lieu d'envelopper tous les contacts utilisateur dans un grand tableau, ils pourraient également être placés dans un objet.

Voyez ci-dessous :

```js
contacts: {
  user_id: {
    name,
    email,
    profile_pic,
    status,
    user_id
  },
  user_id_2: {
    name,
    email,
    profile_pic,
    status,
    user_id_2
  }
}
```

Puisque les objets doivent avoir une paire clé-valeur, les identifiants uniques des contacts sont utilisés comme clés pour leurs objets utilisateur respectifs.

Cela a du sens ?

Il y a certains avantages à utiliser des [objets plutôt que des tableaux](https://youtu.be/aJxcVidE0I0). Il y a aussi des inconvénients.

Dans cette application, je vais principalement utiliser des objets pour décrire les champs de l'objet d'état.

Si vous n'êtes pas habitué à cette approche, [cette vidéo](https://youtu.be/aJxcVidE0I0) explique certains des avantages.

Comme je l'ai dit plus tôt, il y a quelques inconvénients à cette approche, mais je vais vous montrer comment les surmonter.

Nous avons résolu comment le champ `contacts` sera conçu dans l'objet d'état de l'application. Maintenant, passons au champ `messages`.

Nous avons actuellement les `messages` sous forme de tableau avec des objets de messages.

```js
messages: [
      {
        messageTo: 'contact1',
        text: "Hello"
      },
      {
        messageTo: 'contact2',
        text: "Hey!"
      }
    ]
```

Nous allons maintenant définir une forme plus appropriée pour les objets de messages. Un objet de message sera représenté par l'objet de message ci-dessous :

```js
{
    text,
    is_user_msg 
};
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ocz7zH5TCDvYtKAEppU7kw.png)
_Remarquez comment certains messages sont positionnés à gauche, et d'autres à droite._

Le `text` est le texte affiché dans la bulle de chat. Cependant, `is_user_msg` sera un booléen — vrai ou faux. Cela est important pour différencier si un message provient d'un contact ou de l'utilisateur de l'application par défaut.

En regardant le graphique ci-dessus, vous remarquerez que les messages de l'utilisateur et ceux d'un contact sont stylisés différemment dans la fenêtre de chat. Les messages de l'utilisateur restent à droite, et le contact, à gauche. L'un est bleu, l'autre est sombre.

Vous voyez maintenant pourquoi le booléen, `is_user_msg` est important. Nous en avons besoin pour rendre les messages de manière appropriée.

Par exemple, l'objet de message peut ressembler à ceci :

```js
{
  text: "Hello there. U good?",
  is_user_msg: false
}
```

Maintenant, en représentant le champ `messages` dans l'état avec un objet, nous devrions avoir quelque chose comme ceci :

```js
messages: {
    user_id: {
       text,
       is_user_msg
    },
    user_id_2: {
     text,
     is_user_msg
   }
 }
```

Remarquez comment j'utilise également un objet au lieu d'un tableau. De plus, nous allons mapper chaque message à la clé unique, `user_id` du contact.

C'est parce qu'un utilisateur peut avoir différentes conversations avec différents contacts, et il est important de montrer cette représentation dans l'objet d'état. Par exemple, lorsque un contact est cliqué, nous devons savoir lequel a été cliqué !

Comment faisons-nous cela ? Oui, avec leur `user_id`.

La représentation ci-dessus est incomplète mais nous avons fait beaucoup de progrès ! Le champ `messages` que nous avons représenté ici suppose que chaque contact (représenté par son identifiant utilisateur unique) n'a qu'un seul message.

Mais, ce n'est pas toujours le cas. Un utilisateur peut avoir de nombreux messages envoyés dans les deux sens au sein d'une conversation.

Alors, comment faisons-nous cela ?

La manière la plus simple est d'avoir un tableau de messages, mais au lieu de cela, je vais représenter cela avec des objets :

```js
messages: {
  user_id: {
     0: {
        text,
        is_user_msg
     },
     1: {
       text,
       is_user_msg
     }
  },
  user_id_2: {
    0: {
       text,
       is_user_msg
    }
 }  
}
```

Maintenant, nous prenons en considération la quantité de messages envoyés au sein d'une conversation. Un message, deux messages, ou plus, ils sont maintenant représentés dans la représentation `messages` ci-dessus.

Vous vous demandez peut-être pourquoi j'ai utilisé des nombres, `0`, `1` et ainsi de suite pour créer un mappage pour chaque message de contact.

Je vais expliquer cela ensuite.

Pour ce qu'il vaut, le processus de suppression des entités imbriquées de votre objet d'état et de le concevoir comme nous l'avons fait ici s'appelle "Normaliser l'Objet d'État". Je ne veux pas que vous soyez confus au cas où vous verriez cela ailleurs.

### Le Principal Problème avec l'Utilisation d'Objets au Lieu de Tableaux

J'aime l'idée d'utiliser des objets plutôt que des tableaux — pour la plupart des cas d'utilisation. Il y a cependant quelques mises en garde à connaître.

#### **Mise en garde #1** : Il est beaucoup plus facile d'itérer sur les Tableaux dans votre logique de vue

Une situation courante dans laquelle vous vous trouverez est le besoin de rendre une liste de composants.

Par exemple, pour rendre une liste d'utilisateurs donnée une prop `users`, votre logique ressemblerait à ceci :

```js
const users = this.props.users; 

users.map(user => {
	  return <User />
})
```

Cependant, si `users` étaient stockés dans l'état en tant qu'objet, lorsqu'ils sont récupérés et passés en tant que `props`, `users` resteront un objet. Vous ne pouvez pas utiliser `map` sur les objets — et il est beaucoup plus difficile d'itérer sur eux.

Alors, comment résolvons-nous cela ?

#### **Solution #1a** :

Utilisez `Lodash` pour itérer sur les objets.

Pour les non-initiés, `Lodash` est une bibliothèque utilitaire JavaScript robuste. Même pour itérer sur les tableaux, beaucoup soutiendraient que vous utilisez toujours `Lodash` car il aide à gérer les valeurs fausses.

La syntaxe pour utiliser `Lodash` pour itérer sur les objets n'est pas difficile à comprendre. Elle ressemble à ceci :

```js
//importer la bibliothèque
import _ from "lodash"

//l'utiliser
_.map(users, (user) => {
		return <User />
})
```

Vous appelez la méthode `map` sur l'objet `Lodash`, `_.map()`. Vous passez l'objet à itérer, puis vous passez une fonction de rappel comme vous le feriez avec la fonction `map` JavaScript par défaut.

#### **Solution #1b** :

Considérez la manière habituelle dont vous mapperiez sur un tableau pour créer une liste rendue d'utilisateurs :

```js
const users = this.props.users;

users.map(user => {
	  return <User />
})
```

Maintenant, supposons que `users` était un objet. Cela signifie que nous ne pouvons pas `map` dessus. Et si nous pouvions facilement convertir `users` en un tableau sans trop de tracas ?

`Lodash` à la rescousse à nouveau.

Voici à quoi cela ressemblerait :

```js
const users = this.props.users; //ci est un objet. 

_.values(users).map(user => {
	  return <User />
})
```

Vous voyez cela ?

`_.values()` convertira l'objet en un tableau. Cela rend `map` possible !

Voici comment cela fonctionne.

Si vous aviez un objet `users` comme ceci :

```js
{
 user_id_1: {user_1_object},
 user_id_2 {user_2_object},
 user_id_3: {user_3_object},
 user_id_4: {user_4_object},
}
```

`_.values(users)` convertira cela en ceci :

```js
[
 {user_1_object},
 {user_2_object},
 {user_3_object},
 {user_4_object},
]
```

Oui ! Un tableau avec les valeurs de l'objet. Exactement ce dont vous avez besoin pour itérer. Problème résolu.

Il y a encore une autre mise en garde. C'est peut-être une plus grande.

#### **Mise en garde #2** : Préservation de l'Ordre

C'est peut-être la raison numéro un pour laquelle les gens utilisent des tableaux. Les tableaux préservent l'ordre de leurs valeurs.

Vous devez voir un exemple pour comprendre cela.

```js
const numbers = [0,3,1,6,89,5,7,9]
```

Quoi que vous fassiez, la récupération de la valeur de `numbers` retournera toujours le même tableau, avec l'ordre des entrées inchangé.

Et un objet ?

```js
const numbers = {
 0: "Zero",
 3: "Three",
 1: "One",
 6: "Six",
 89: "Eighty-nine",
 5: "Five",
 7: "Seven",
 9: "Nine"
}
```

L'ordre des nombres est le même que dans le tableau avant.

Maintenant, regardez-moi copier et coller ceci dans la console du navigateur, puis essayez de récupérer les valeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9Em-4BPYl8Up0yND4v5pRg.gif)
_Le problème avec les objets._

Ok, vous avez peut-être manqué cela. Regardez ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qep8JRg8q99S-z1-ngJ-1A.png)
_Le problème avec les objets et l'ordre non préservé._

Voyez les surlignages dans l'image ci-dessus. L'ordre des valeurs de l'objet n'est pas retourné de la même manière !

Maintenant, selon le type d'application que vous construisez, cela peut causer des problèmes très sérieux. Surtout dans les applications où l'ordre est primordial.

Vous connaissez des exemples de telles applications ?

Eh bien, moi oui. Une application de chat !

Si vous représentez les conversations des utilisateurs sous forme d'objet, vous vous souciez certainement de l'ordre dans lequel les messages sont affichés !

Vous ne voulez pas qu'un message envoyé hier apparaisse comme s'il avait été envoyé aujourd'hui. L'ordre compte.

Alors, comment résoudre ce problème ?

#### **Solution #2** :

Gardez un tableau séparé d'IDs pour indiquer l'ordre.

Vous devez avoir vu cela auparavant, mais vous n'y avez peut-être pas prêté attention.

Par exemple, si vous aviez l'objet suivant :

```js
const numbers = {
  0: "Zero",
  3: "Three",
  1: "One",
  6: "Six",
  89: "Eighty-nine",
  5: "Five",
  7: "Seven",
  9: "Nine"
 }
```

Vous pourriez garder un autre tableau pour indiquer l'ordre des valeurs.

```js
numbersOrderIDs: [0, 3, 1, 6, 89, 5, 7, 9]
```

De cette façon, vous pouvez toujours garder une trace de l'ordre des valeurs — indépendamment du comportement de l'objet. Si vous devez ajouter des valeurs à l'objet, vous le faites, mais vous poussez également l'ID associé dans le `numbersOrderIDs`.

Il est important d'être conscient de ces choses car vous n'aurez pas toujours le contrôle sur certaines choses. Vous pourriez reprendre des applications avec un état modélisé de cette manière. Et même si vous n'aimez pas l'idée, vous devriez définitivement être au courant.

Pour simplifier, les IDs des messages pour l'application Skypey seront toujours dans l'ordre — car ils sont numérotés avec des valeurs croissantes à partir de zéro.

Cela peut ne pas être le cas dans une vraie application. Vous pourriez avoir des IDs auto-générés bizarres qui ressemblent à du charabia comme `y68fnd0a9wyb`.

Dans de tels cas, vous voulez garder un tableau séparé pour suivre l'ordre des valeurs.

C'est tout !

Il est utile de souligner que l'ensemble du processus de **normalisation** de l'objet d'état peut être résumé comme suit :

• Chaque type de données doit avoir sa propre clé dans l'objet d'état.

• Chaque clé doit stocker les éléments individuels dans un objet, avec les IDs des éléments comme clés et les éléments eux-mêmes comme valeurs.

• Toute référence à des éléments individuels doit être faite en stockant l'ID de l'élément.

• Idéalement, gardez un tableau d'IDs pour indiquer l'ordre.

### Récapitulatif sur la Conception de l'Objet d'État

Maintenant, je sais que cela a été un long discours sur la structure de l'objet d'état.

Cela peut ne pas sembler important pour vous maintenant, mais à mesure que vous construisez des projets, vous en viendrez à voir à quel point il est inestimable de mettre un peu de réflexion dans la conception de votre état. Cela vous aidera à effectuer des opérations CRUD beaucoup plus facilement, réduira beaucoup de logique trop complexe dans vos reducers, et vous aidera également à tirer parti de la Composition de Reducers, un terme que je décrirai plus tard dans ce livre.

Je voulais que vous compreniez la raison derrière mes décisions, et que vous soyez en mesure de prendre des décisions éclairées à mesure que vous construisez vos propres applications. Je crois que vous êtes maintenant doté des bonnes informations.

Avec tout ce qui a été dit et fait, voici une représentation visuelle de l'objet d'état de Skypey :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FWFzkdKwxIVln7PQFsLKxQ.png)
_Exemple d'objet d'état pour 2 contacts utilisateurs. Dans l'application que nous allons construire, il y aura 10 contacts avec 10 messages initiaux._

L'image suppose seulement deux contacts utilisateurs. Veuillez bien la regarder.

### Construction de la Liste des Utilisateurs

Ensuite, il est temps d'écrire du code. Voici l'objectif de cette section. Construire la liste des utilisateurs montrée ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mhwwe-U2SLWB8O80Of6sXA.gif)
_Nous devrions avoir quelque chose comme ceci lorsque nous aurons construit avec succès la liste des utilisateurs._

Qu'est-ce qui est nécessaire pour construire cela ?

D'un niveau élevé, il devrait être assez clair que dans le composant `Sidebar`, il est nécessaire de rendre une liste des contacts d'un utilisateur.

Présumément, dans `Sidebar`, vous pourriez avoir quelque chose comme ceci :

```js
contacts.map(contact => <User />)
```

Vous avez compris ?

Vous mappez sur certaines données `contacts` de l'état, et pour chaque `contact`, vous rendez un composant `User`.

Mais d'où viennent les données pour cela ?

Idéalement, et dans un scénario réel, vous allez récupérer ces données depuis le serveur avec un appel Ajax. À des fins d'apprentissage, cela apporte une couche de complexité que nous pouvons éviter — pour l'instant.

Ainsi, au lieu de récupérer des données à distance depuis un serveur, j'ai créé quelques [fonctions](https://gist.github.com/ohansemmanuel/d940d45c541ae8bc49e16b2fe0a55a2d) qui vont gérer la création de données pour l'application. Nous allons utiliser ces données statiques pour construire l'application.

Par exemple, il y a une variable `contacts` déjà créée dans [static-data.js](https://gist.github.com/ohansemmanuel/d940d45c541ae8bc49e16b2fe0a55a2d), qui va toujours retourner une liste de contacts générée aléatoirement. Tout ce que vous avez à faire est d'importer cela dans l'application. Pas d'appels Ajax.

Ainsi, créez un nouveau fichier dans le répertoire racine du projet et appelez-le `static-data.js`

Copiez le contenu de [la gist ici](https://gist.github.com/ohansemmanuel/d940d45c541ae8bc49e16b2fe0a55a2d) dans ce fichier. Nous allons l'utiliser très bientôt.

### Configuration du Store

Passons rapidement en revue le processus de configuration du store de l'application afin que nous puissions récupérer les données nécessaires pour construire la liste des utilisateurs dans la barre latérale.

L'une des premières étapes lors de la création d'une application Redux est la configuration du store Redux. Puisque c'est là que les données seront lues, il devient impératif de résoudre cela.

Alors, veuillez installer `redux` depuis le `cli` avec :

```bash
yarn add redux
```

Une fois l'installation terminée, créez un nouveau dossier appelé `store` et dans le répertoire, créez un nouveau fichier `index.js`.

N'oubliez pas l'analogie d'avoir les principaux acteurs Redux dans leurs propres répertoires.

Comme vous le savez déjà, le store sera créé via la fonction de fabrique `createStore` de `redux` comme ceci :

`**store/index.js**`

```js
import { createStore } from "redux";

const store = createStore(someReducer, initialState); 

export default store;
```

Le `createStore` de Redux doit être conscient du reducer (souvenez-vous de la relation entre le store et le reducer que j'ai expliquée plus tôt).

Maintenant, modifiez la deuxième ligne pour qu'elle ressemble à ceci :

```js
const store = createStore(reducer, {contacts});
```

Maintenant, importez le `reducer`, et `contacts` depuis les données statiques :

```js
import reducer from "../reducers";
import { contacts } from "../static-data";
```

Puisque nous n'avons pas encore créé de répertoire `reducers`, veuillez le faire maintenant. Créez également un fichier `index.js` dans ce répertoire `reducers`.

Maintenant, créez le reducer.

`**reducers/index.js**`

```js
export default (state, action) => {
    return state;
};
```

Un reducer est simplement une fonction qui prend `state` et `action`, et retourne un nouveau `state`.

Si je vous ai perdu dans la création du store, `const store = createStore(reducer, {contacts});` vous devriez vous souvenir que le deuxième argument dans `createStore` est l'état initial de l'application.

Je l'ai défini comme l'objet `{contacts}`.

C'est une syntaxe ES6, similaire à ceci : `{contacts: contacts}` avec une clé `contacts` et une valeur `contacts` de `static-data`.

Il n'y a aucun moyen de savoir que ce que nous avons fait est correct. Essayons de corriger cela.

Dans `Index.js`, voici ce que vous devriez avoir maintenant :

`**Index.js**`

```js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import registerServiceWorker from "./registerServiceWorker";


ReactDOM.render(<App />, document.getElementById("root"));
registerServiceWorker();
```

Comme nous l'avons fait avec le premier exemple, refactorisons l'appel `ReactDOM.render` pour qu'il se trouve dans une fonction `render`.

```js
const render = () => {
  return ReactDOM.render(<App />, document.getElementById("root"));
};
```

Ensuite, invoquez la fonction render pour que l'application se rende correctement.

```js
render()
```

Maintenant, importez le `store` que vous avez créé plus tôt...

```js
import store from "./store";
```

Et assurez-vous que chaque fois que le store est mis à jour, la fonction `render` est invoquée.

```js
store.subscribe(render);
```

Bien !

Maintenant, profitons de cette configuration.

Chaque fois que le store est mis à jour et invoque `render`, logguons l'`état` du store.

Voici comment :

```js
const render = () => {
  fancyLog();
  return ReactDOM.render(<App />, document.getElementById("root"));
};
```

Il suffit d'appeler une nouvelle fonction, `fancyLog()`, que vous allez bientôt écrire.

Voici la fonction `fancyLog` :

```js
function fancyLog() {
  console.log("%c Rendered with ? ??", "background: purple; color: #FFF");
  console.log(store.getState());
}
```

Hmmm. Qu'ai-je fait ?

`console.log(store.getState())` est la partie que vous connaissez. Cela va logger l'état récupéré du store.

La première ligne, `console.log("%c Rendered with ? ??", "background: purple; color: #fff");` va logger le texte, "Rendered with …", plus quelques emojis, et un peu de style CSS pour le rendre distinguable. Le `%c` écrit avant le texte "Rendered with …" permet d'utiliser le style CSS.

Assez parlé. Voici le code complet :

`**index.js**`

```js
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import registerServiceWorker from "./registerServiceWorker";
import store from "./store";

const render = () => {
  fancyLog();
  return ReactDOM.render(<App />, document.getElementById("root"));
};

render();
store.subscribe(render);
registerServiceWorker();

function fancyLog() {
  console.log("%c Rendered with ? ??", "background: purple; color: #fff");
  console.log(store.getState());
}
```

Voici l'objet d'état qui est loggé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vNkkF2fYJFuNAnSSy4UkJQ.gif)
_Notre logger de base en action._

Comme vous pouvez le voir, dans l'objet d'état se trouve un champ `contacts` qui contient les contacts disponibles pour l'utilisateur particulier. La structure des données est telle que nous l'avons discutée précédemment. Chaque contact est mappé avec son `user_id`

Nous avons fait des progrès décents.

#### Passage des Données de la Barre Latérale via les Props

Si vous jetez un coup d'œil à l'ensemble du code maintenant, vous serez d'accord pour dire que le point d'entrée de l'application reste `index.js`.

`Index.js` rend ensuite le composant `App`. Le composant `App` est alors responsable du rendu des composants `Main` et `Sidebar`.

Pour que `Sidebar` ait accès aux données de contacts requises, nous allons passer les données via les props.

Dans `App.js`, récupérez `contacts` du store, et passez-le à `Sidebar` comme ceci :

`**App.js**`

```js
const App = () => {
  const { contacts } = store.getState();

  return (
    <div className="App">
      <Sidebar contacts={contacts} />
      <Main />
    </div>
  );
};
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*8ORuVSEdkT2gYAO03noqlQ.png)
_L'objet contacts passé avec succès en tant que props à Sidebar_

Comme je l'ai fait dans la capture d'écran ci-dessus, inspectez le composant Sidebar et vous trouverez les `contacts` passés en tant que prop. Les contacts sont un objet avec des IDs mappés à des objets utilisateur.

Maintenant, nous pouvons procéder au rendu des contacts.

Tout d'abord, installez `Lodash` depuis le `cli` :

```bash
yarn add lodash
```

Importez `lodash` dans `App.js`

```js
import  _ from lodash
```

Je sais. Le soulignement semble drôle, mais c'est une belle convention. Vous allez l'aimer :)

Maintenant, pour utiliser l'une des méthodes utilitaires que `lodash` nous offre, appelez les méthodes sur le soulignement importé, comme `.fakeMethod()`.

Maintenant, mettez `Lodash` à bonne utilisation. En utilisant l'une des fonctions utilitaires de `Lodash`, l'objet `contacts` peut être facilement converti en un tableau lorsqu'il est passé en tant que props.

Voici comment :

```js
<Sidebar contacts={_.values(contacts)} />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*IX54ufF4ZWhXYUnn7wOzvw.png)
_Notez que la prop contacts est maintenant un tableau._

Vous pouvez lire plus sur la méthode [.values de Lodash](https://lodash.com/docs/4.17.10#values) si vous le souhaitez. En résumé, elle crée un tableau à partir de toutes les valeurs clés de l'objet passé.

Maintenant, rendons vraiment quelque chose dans la Sidebar.

`**Sidebar.js**`

```js
import React from "react";
import User from "./User"; 
import "./Sidebar.css";

const Sidebar = ({ contacts }) => {
  return (
    <aside className="Sidebar">
      {contacts.map(contact => <User user={contact} key={contact.user_id} />)}
    </aside>
  );
};

export default Sidebar;
```

Dans le bloc de code ci-dessus, nous mappons sur la prop contacts et rendons un composant `User` pour chaque `contact`.

Pour éviter l'avertissement React key, l'`user_id` du contact est utilisé comme clé. De plus, chaque contact est passé en tant que prop `user` au composant `User`.

### Construction du Composant User

Nous rendons un composant `User` dans la `Sidebar`, mais ce composant n'existe pas encore.

Veuillez créer un fichier `User.js` et `User.css` dans le répertoire racine.

Fait ?

Maintenant, voici le contenu du fichier `User.js` :

`**User.js**`

```js
import React from "react";
import "./User.css";

const User = ({ user }) => {
  const { name, profile_pic, status } = user;

  return (
    <div className="User">
      <img src={profile_pic} alt={name} className="User__pic" />
      <div className="User__details">
        <p className="User__details-name">{name}</p>
        <p className="User__details-status">{status}</p>
      </div>
    </div>
  );
};

export default User;
```

Ne laissez pas le gros morceau de code vous tromper. Il est en fait très facile à lire et à comprendre. Jetez un deuxième coup d'œil.

Le `name`, l'URL `profile_pic` et le `status` de l'utilisateur sont obtenus des props via la déstructuration : `const { name, profile_pic, status } = user;`

Ces valeurs sont ensuite utilisées dans l'instruction return pour un rendu approprié, et voici le résultat de cela :

![Image](https://cdn-media-1.freecodecamp.org/images/1*y-ryoC5V9nh89kf18a0Mkw.gif)
_La barre latérale rendue avec des contacts non stylisés._

Le résultat ci-dessus est super laid, mais c'est une indication que cela fonctionne !

Maintenant, stylisons cela.

Tout d'abord, empêchez la liste des utilisateurs de déborder du conteneur Sidebar.

`**Sidebar.css**`

```css
.Sidebar {
... 
overflow-y: scroll;
}
```

De plus, la police est laide. Changeons cela.

`**Index.css**`

```css
@import url("https://fonts.googleapis.com/css?family=Nunito+Sans:400,700");

body {
 ... 
  font-weight: 400;
  font-family: "Nunito Sans", sans-serif;
}
```

Enfin, gérez l'affichage global du composant `User`.

`**User.css**`

```css
.User {
  display: flex;
  align-items: flex-start;
  padding: 1rem;
}
.User:hover {
  background: rgba(0, 0, 0, 0.2);
  cursor: pointer;
}
.User__pic {
  width: 50px;
  border-radius: 50%;
}
.User__details {
  display: none;
}

/* pas de petits appareils  */
@media (min-width: 576px) {
  .User__details {
    display: block;
    padding: 0 0 0 1rem;
  }
  .User__details-name {
    margin: 0;
    color: rgba(255, 255, 255, 0.8);
    font-size: 1rem;
  }
}
```

Puisque ceci n'est pas un livre sur CSS, je saute certaines des explications de style. Cependant, si quelque chose vous confond, demandez-moi simplement [sur Twitter](https://twitter.com/ohansemmanuel), et je serai ravi de vous aider.

Voilà !

Voici le bel affichage que nous avons maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*XgNDuwcP9wDgzLrZoN76_Q.gif)
_Les contacts de la barre latérale bien stylisés !_

Incroyable !

Nous sommes passés de rien à avoir une belle liste d'utilisateurs rendue à l'écran.

Si vous codez, redimensionnez le navigateur pour voir la belle vue sur mobile également.

Tenez bon !

### Des questions ?

Il est tout à fait normal d'avoir des questions.

Le moyen le plus rapide de me joindre sera de tweeter votre question [via Twitter](https://twitter.com/ohansemmanuel), avec le hashtag, **#UnderstandingRedux**. De cette façon, je peux facilement trouver et répondre à votre question.

### Vous n'avez pas à Passer les Props

Jetez un coup d'œil à la structure de haut niveau de l'interface utilisateur de Skypey ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qsEjU76UDKvJ5pvWoYK32A.png)
_Une structure de haut niveau de la disposition de Skypey_

Dans les applications React traditionnelles (sans utiliser l'API de contexte), vous êtes tenu de passer les props de `<App />` à `<Sidebar />` et `<Main />`

![Image](https://cdn-media-1.freecodecamp.org/images/1*weaeYex3hH1vnvEyEc9elA.png)
_Passer les props depuis App, comme dans les applications React normales._

Avec Redux, cependant, vous n'êtes **pas** lié par cette règle.

Si un certain composant a besoin d'accéder à une valeur de l'objet d'état, vous pouvez simplement atteindre le store et récupérer l'état actuel.

Par exemple, `<Sidebar />` et `<Main />` peuvent accéder au store Redux sans avoir besoin de dépendre de `<App />`

![Image](https://cdn-media-1.freecodecamp.org/images/1*_lkAqTmg0NvU_wa5YVM_LA.png)
_Avec Redux, vous n'avez pas à passer les props. Obtenez simplement les valeurs requises directement depuis le store_

La seule raison pour laquelle je ne l'ai pas fait ici est que `<App />` est un parent direct, avec `<Sidebar />` et `<Main />` NON plus d'un niveau profond dans la hiérarchie des composants.

Comme vous le verrez dans les sections suivantes, pour les composants qui sont imbriqués plus profondément dans la hiérarchie des composants, nous atteindrons directement le store Redux pour récupérer l'état actuel.

Il n'est pas nécessaire de passer les props.

Vous allez adorer le graphique ci-dessous. Il va encore plus loin pour décrire le besoin de ne pas passer les props lors de l'utilisation de Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ahRv99qU-soyV-_QR7BgzA.png)

### Structure de Dossiers Conteneurs et Composants

Il y a un peu de refactorisation que vous devez faire avant que nous passions au codage de l'application Skypey.

Dans les applications Redux, il est courant de diviser vos composants en deux répertoires différents.

Tout composant qui parle directement à Redux, que ce soit pour récupérer l'état du store ou pour dispatcher une action, doit être déplacé dans un répertoire `containers`.

Les autres composants, ceux qui ne **parlent pas** à Redux, doivent être déplacés dans un répertoire `components`.

Eh bien, eh bien, eh bien. Pourquoi se donner tout ce mal ?

Pour une chose, votre base de code devient un peu plus propre. Il devient également plus facile de trouver certains composants tant que vous savez s'ils parlent à Redux ou non.

Alors, allez-y.

Jetez un coup d'œil aux composants dans l'état actuel de l'application, et réorganisez-les en conséquence.

Pour que vous ne gâchiez pas les choses, n'oubliez pas de déplacer le fichier CSS associé aux composants.

Voici ma solution :

1. Créez deux dossiers : `containers` et `components`.
2. `App.js` tente de récupérer `contacts` du store. Donc, déplacez `App.js` et `App.css` dans le dossier `containers`.
3. Déplacez `Sidebar.js`, `Sidebar.css`, `Main.js` et `Main.css` dans le dossier `components`. Ils ne parlent pas directement à Redux pour quoi que ce soit.
4. Veuillez ne pas déplacer `Index.js` et `Index.css`. Ce sont les points d'entrée de l'application. Laissez-les simplement à la racine du répertoire du projet.
5. Veuillez déplacer `User.js` et `User.css` dans le répertoire `containers`. Le composant `User` ne parle pas encore à Redux **mais il le fera**. Souvenez-vous que lorsque l'application est terminée, lors du **clic** sur un utilisateur de la barre latérale, leurs messages seront affichés. Par implication, une action sera dispatchée. Dans les sections à venir, nous allons construire cela.
6. À ce stade, beaucoup de vos URLs d'importation seront cassées, c'est-à-dire les composants qui ont importé ces composants déplacés. Vous devez changer leur URL d'importation. Je vous laisse faire cela. C'est une correction facile :)

Voici une solution d'exemple pour le point #6 ci-dessus : Dans `App.js`, changez les imports `Sidebar` et `Main` en ceci :

```js
import Sidebar from "../components/Sidebar";
import Main from "../components/Main";
```

Contrairement à l'ancien :

```js
import Sidebar from "./Sidebar";
import Main from "./Main";
```

Vous avez compris ?

Voici quelques conseils pour résoudre le défi vous-même :

1. Vérifiez l'instruction d'importation de `Sidebar.js` pour le composant `User`.
2. Vérifiez l'instruction d'importation de `Index.js` pour le composant `App`.
3. Vérifiez l'instruction d'importation de `App.js` pour le `store`

Une fois cela fait, vous aurez Skypey fonctionnant comme prévu !

### Refactorisation pour Définir l'État Initial à partir du Reducer

Tout d'abord, veuillez jeter un coup d'œil à la création du `store` dans _store/index.js_. En particulier, considérons cette ligne de code :

```js
const store = createStore(reducer, { contacts });
```

L'objet d'état initial est passé directement dans `createStore`. Souvenez-vous que le store est créé avec la signature, `createStore(reducer, initialState)`. Dans ce cas, l'état initial a été défini comme l'objet, `{contacts: contacts}`

Même si cette approche fonctionne, elle est typiquement utilisée pour le rendu côté serveur (ne vous en souciez pas si vous ne savez pas ce que cela signifie). Pour l'instant, comprenez que cette approche de définition d'un état initial dans `createStore` est plus utilisée dans le monde réel pour le rendu côté serveur.

Pour l'instant, supprimez l'état initial dans la méthode `createStore`.

Nous allons faire en sorte que l'état initial de l'application soit défini uniquement par le reducer.

Faites-moi confiance, vous allez comprendre cela.

Voici à quoi ressemblera le fichier `store/index.js` une fois que vous aurez supprimé l'état initial de `createStore`.

```js
import { createStore } from "redux";
import reducer from "../reducers";

const store = createStore(reducer);

export default store;
```

Et voici le contenu actuel du fichier `reducer/index.js` :

```js
export default (state, action) => {
  return state;
};
```

Veuillez le changer en ceci :

```js
import { contacts } from "../static-data";

export default (state = { contacts }, action) => {
  return state;
};
```

Ainsi, qu'est-ce qui se passe ici ?

En utilisant les paramètres par défaut ES6, nous avons défini le paramètre state à une valeur initiale de `{contacts}`.

C'est essentiellement la même chose que `{contacts: contacts}`.

Ainsi, l'instruction `return state` dans le reducer retournera cette valeur, `{contacts: contacts}` comme état initial de l'application.

À ce stade, l'application fonctionne maintenant — tout comme avant. La seule différence ici est que l'état initial de l'application est maintenant géré par le Reducer.

Continuons à refactoriser.

### Composition de Reducers

Dans toutes les applications que nous avons créées jusqu'à présent, nous avons utilisé un seul reducer pour gérer l'ensemble de l'état des applications.

Quelle est l'implication de cela ?

C'est comme avoir un seul Caissier dans tout le hall de la banque. À quel point cela est-il évolutif ?

Même si le Caissier peut faire tout le travail efficacement, il peut être plus gérable — et peut-être une meilleure expérience client — d'avoir plus d'un Caissier dans le hall de la banque.

Quelqu'un doit s'occuper de tout le monde, et c'est beaucoup de travail pour une seule personne !

Il en va de même pour vos applications Redux.

Il est courant d'avoir plusieurs reducers dans votre application plutôt qu'un seul reducer gérant toutes les opérations de l'état. Ces reducers sont ensuite combinés en un seul.

Par exemple, il pourrait y avoir 5 ou 10 Caissiers dans le hall de la banque, mais tous combinés servent un seul but. C'est ainsi que cela fonctionne également.

Considérez l'objet d'état de l'application Hello World que nous avons construite précédemment.

```js
{ 
  tech: "React"
}
```

Assez simple.

Tout ce que nous avons fait, c'est avoir **un** reducer gérer toutes les mises à jour de l'état.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZDW08Z4ry2Cn9S66F4kR5Q.png)

Cependant, considérons l'objet d'état de l'application Skypey plus complexe :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FWFzkdKwxIVln7PQFsLKxQ.png)

Avoir un seul reducer gérer l'ensemble de l'objet d'état est faisable — mais ce n'est pas la meilleure approche.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aD_wEZMqWfAOBtZpcWmE3g.png)

Au lieu d'avoir l'ensemble de l'objet géré par un seul reducer, que se passerait-il si nous avions un reducer gérer un seul champ dans l'objet d'état ?

Comme une correspondance un à un ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*M-l-Wn_CJzQCgB7KND-1aw.png)

Vous voyez ce que nous faisons là ? Introduire plus de Caissiers !

La composition de reducers nécessite qu'un seul reducer gère la mise à jour de l'état pour un seul champ dans l'objet d'état.

Par exemple, pour le champ `messages`, vous avez un `messagesReducer`. Pour un champ `contacts`, vous avez également un `contactsReducer` et ainsi de suite.

Une autre chose importante à souligner est que la valeur retournée par chacun des reducers est uniquement pour le champ qu'ils représentent.

Ainsi, si j'avais `messagesReducer` écrit comme ceci :

```js
export const function messagesReducer (state={}, action) {
  return state 
}
```

L'`état` retourné ici n'est pas l'état de toute l'application.

Non.

C'est seulement la valeur du champ `messages`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yL6a7ysCWCT1URK9xVv5YA.png)

Il en va de même pour les autres reducers.

Vous avez compris ?

Voyons cela en pratique, et comment exactement ces reducers sont combinés pour un seul but.

### Refactorisation de _Skypey_ pour Utiliser Plusieurs Reducers

Vous vous souvenez comment j'ai parlé de plusieurs reducers gérant chaque champ dans l'objet d'état ?

Maintenant, vous pouvez dire que nous aurons les reducers multiples suivants comme le montre la figure ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*M-l-Wn_CJzQCgB7KND-1aw.png)

Maintenant, pour chaque champ dans l'objet d'état, nous allons créer un reducer correspondant. Les actuels à ce stade sont, `contacts` et `user`.

Passons en revue comment cela affecte notre code d'abord. Ensuite, je vais faire un pas en arrière pour expliquer comment cela fonctionne à nouveau.

Jetez un coup d'œil à `reducer/index.js` :

```js
import { contacts } from "../static-data";

export default (state = contacts, action) => {
  return state;
};
```

Renommez ce fichier en `contacts.js`.

Ceci deviendra le reducer des contacts.

Créez un fichier `user.js` dans le répertoire `reducers`.

Ceci sera le reducer de l'utilisateur.

Voici le contenu du reducer de l'utilisateur.

`**reducers/user.js**`

```js
import { generateUser } from "../static-data";
export default function user(state = generateUser(), action) {
  return state;
}
```

Encore une fois, j'ai créé une fonction `generateUser` pour générer quelques informations utilisateur statiques.

En utilisant les paramètres par défaut ES6, l'état initial est défini comme le résultat de l'invocation de cette fonction. Par conséquent, `return state` retournera maintenant un objet utilisateur.

Maintenant, nous avons deux reducers différents. Combinons-les pour le bien commun :)

* Créez un fichier `index.js` dans le répertoire reducers

Tout d'abord, importez les deux reducers, `user` et `contacts` :

```js
import user from "./user";
import contacts from "./contacts";
```

Pour combiner ces reducers, nous avons besoin de la fonction d'assistance `combineReducers` de `redux`

Importez-la comme ceci :

```js
import { combineReducers } from "redux";
```

Maintenant, `index.js` exportera la combinaison des deux reducers comme ceci :

```js
export default combineReducers({
  user,
  contacts,
});
```

Remarquez que la fonction `combineReducers` prend un objet. Un objet dont la forme est exactement comme l'objet d'état de l'application.

Le bloc de code est le même que ceci :

```js
export default combineReducers({
  user: user,
  contacts: contacts
})
```

L'objet a des clés `user` et `contacts`, tout comme l'objet d'état que nous avons en tête.

Et les valeurs de ces clés ?

Les valeurs proviennent des reducers !

![Image](https://cdn-media-1.freecodecamp.org/images/1*I1oXITmnlaO33g1wSw_bcw.png)

Il est important de comprendre cela. D'accord ?

### Je suis perdu. Comment cela fonctionne-t-il à nouveau ?

Laissez-moi faire un pas en arrière et expliquer comment fonctionne la composition des reducers à nouveau. Cette fois, d'une perspective différente.

Considérez l'objet JavaScript ci-dessous :

```js
const state = {
  user: "me",
  messages: "hello",
  contacts: ["no one", "khalid"],
  activeUserId: 1234
}
```

Maintenant, supposons qu'au lieu d'avoir les valeurs des clés codées en dur, nous voulions qu'elles soient représentées par des appels de fonction. Cela pourrait ressembler à ceci :

```js
const state = {
   user:  getUser(),
   messages: getMsg(),
   contacts: getContacts(),
   activeUserId: getID()
}
```

Cela suppose que `getUser()` retournera également la valeur précédente, "me". Il en va de même pour les autres fonctions remplacées.

Vous suivez toujours ?

Maintenant, renommons ces fonctions.

```js
const state = {
   user:  user(),
   messages: messages(),
   contacts: contacts(),
   activeUserId: activeUserId()
}
```

Maintenant, les fonctions ont des noms identiques à leurs clés d'objet correspondantes. Au lieu de `getUser()`, nous avons maintenant `user()`.

Soyons imaginatifs.

Imaginez qu'il existait une certaine fonction utilitaire importée depuis une bibliothèque. Appelons cette fonction, `killerFunction`.

Maintenant, `killerFunction` permet de faire ceci :

```js
const state = killerFunction({
   user: user,
   messages: messages, 
   contacts: contacts,
   activeUserId: activeUserId
})
```

Qu'est-ce qui a changé ?

Au lieu d'invoquer chacune des fonctions, vous écrivez simplement les noms des fonctions. `killerFunction` se chargera d'invoquer les fonctions.

Maintenant, en utilisant ES6, nous pouvons simplifier le code davantage :

```js
const state = killerFunction({
   user,
   messages, 
   contacts,
   activeUserId
})
```

C'est la même chose que le bloc de code précédent. En supposant que les fonctions sont dans la portée et ont le même nom (identifiant) que la clé de l'objet.

Vous avez compris ?

Maintenant, c'est un peu comme ça que fonctionne `combineReducer` de `Redux`.

Les valeurs de chaque clé dans votre objet d'état seront obtenues à partir du `reducer`. N'oubliez pas qu'un reducer est simplement une fonction.

Tout comme `killerFunction`, `combineReducers` est capable de s'assurer que les valeurs sont obtenues en invoquant les fonctions passées.

Toutes les clés et valeurs mises ensemble donneront alors l'objet d'état de l'application.

C'est tout !

Un point important à toujours retenir est que lors de l'utilisation de `combineReducers`, la valeur retournée par chaque reducer n'est pas l'état de l'application.

C'est seulement la `valeur` de la clé particulière qu'ils représentent dans l'objet d'état !

Par exemple, le reducer `user` retourne la valeur pour la clé `user` dans l'état. De même, le reducer `messages` retourne la valeur pour la clé `messages` dans l'état.

Maintenant, voici le contenu complet de `reducers/index.js` :

```js
import { combineReducers } from "redux";
import user from "./user";
import contacts from "./contacts";

export default combineReducers({
  user,
  contacts
});
```

Maintenant, si vous inspectez les logs, vous trouverez `user` et `contacts` là dans l'objet d'état.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QQZQgphCtK43Qz5UT0My4Q.gif)
_"user" et "contacts" existent maintenant dans l'objet d'état._

### Construction de l'Écran Vide

Pour l'instant, le composant `Main` affiche simplement le texte, `main stuff`. Ce n'est pas ce que nous voulons.

L'objectif final est de montrer un écran vide, mais d'afficher les messages de l'utilisateur lorsqu'un contact est cliqué.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fu7NzjfZYDjeG9d78L3xsg.png)

Construisons l'écran vide.

Pour cela, nous aurons besoin d'un nouveau composant appelé, `Empty.js`. Pendant que vous y êtes, créez également un fichier CSS correspondant, `Empty.css`.

Veuillez créer ceux-ci dans le répertoire `components`.

`<Empty />` rendra le balisage pour l'écran vide. Pour ce faire, il nécessitera une certaine prop `user`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tM6z4Ef8LJ4hUO2j6t-7nw.png)

Définiment, le `user` doit être passé depuis l'état de l'application. N'oubliez pas la structure globale de l'objet d'état que nous avons résolu plus tôt :

Donc, voici le contenu actuel du composant `<Main />` :

```js
import React from "react";
import "./Main.css";

const Main = () => {
  return <main className="Main">Main Stuff</main>;
};

export default Main;
```

Il retourne simplement le texte, `Main Stuff`.

Le composant `<Main />` est responsable de l'affichage du composant `<Empty />` lorsqu'aucun utilisateur n'est actif. Dès qu'un utilisateur est cliqué, `<Main />` rend les conversations de l'utilisateur cliqué. Cela pourrait être représenté par un composant, `<ChatWindow />`.

Pour que cette bascule de rendu fonctionne et que `<Main />` rende soit `<Empty />` soit `<ChatWindow />`, nous devons suivre un certain `activeUserId`.

Par exemple, par défaut `activeUserId` sera null, puis `<Empty />` sera affiché.

Cependant, dès qu'un utilisateur est cliqué, l'`activeUserId` devient l'`user_id` du contact cliqué. Maintenant, `<Main />` rendra le composant `<ChatWindow />`.

Cool, hein ?

Pour que cela fonctionne, nous allons garder un nouveau champ dans l'objet d'état, `activeUserId`

À ce stade, vous devriez déjà connaître la procédure. Pour ajouter un nouveau champ à l'objet d'état, nous allons le configurer dans les reducers.

Créez un nouveau fichier, `activeUserId.js` dans le dossier `reducers`.

Et voici le contenu du fichier :

`**reducers/activeUserId.js**`

```js
export default function activeUserId(state = null, action) {
  return state;
}
```

Par défaut, il retourne `null`.

Maintenant, connectez ce reducer nouvellement créé à l'appel de la méthode `combineReducer` comme ceci :

```js
...
 import activeUserId from "./activeUserId";
 
export default combineReducers({
  user,
  contacts,
  activeUserId
});
```

Maintenant, si vous inspectez les logs, vous trouverez `activeUserId` là dans l'objet d'état.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mZvpJ_IyZw_ZzDhPQ4bYxQ.gif)

Continuons.

Dans `**App.js**`, récupérez le `user` et `activeUserId` du store, comme ceci :

```js
const { contacts, user, activeUserId  } = store.getState();
```

Ce que nous avions précédemment était ceci :

```js
const { contacts } = store.getState();
```

Maintenant, passez ces valeurs en tant que props au composant `<Main />`.

```js
<Main user={user} activeUserId={activeUserId} />
```

Ce que nous avions précédemment était ceci :

```js
<Main  />
```

Maintenant, développons la logique de rendu dans `<Main />`

**avant :**

```js
import React from "react";
import "./Main.css";

const Main = () => {
  return <main className="Main">Main Stuff</main>;
};

export default Main;
```

**maintenant :**

```js
import React from "react";
import "./Main.css";
import Empty from "../components/Empty";
import ChatWindow from "../components/ChatWindow";

const Main = ({ user, activeUserId }) => {
  const renderMainContent = () => {
    if (!activeUserId) {
      return <Empty user={user} activeUserId={activeUserId} />;
    } else {
      return <ChatWindow activeUserId={activeUserId} />;
    }
  };
  return <main className="Main">{renderMainContent()}</main>;
};

export default Main;
```

Ce qui a changé n'est pas difficile à comprendre. `user` et `activeUserId` sont reçus en tant que props. L'instruction return dans le composant a la fonction `renderMainContent` invoquée.

Tout ce que fait `renderMainContent` est de vérifier si `activeUserId` n'existe pas. Si ce n'est pas le cas, il rend l'écran vide. Si ce n'est pas le cas, alors le `ChatWIndow` est rendu.

Super !

Nous n'avons pas encore construit les composants `Empty` et `ChatWindow`.

Pardonnez-moi, je vais coller beaucoup de code à la fois.

Modifiez le fichier `Empty.js` pour qu'il contienne ceci :

```js
import React from "react";
import "./Empty.css";

const Empty = ({ user }) => {
  const { name, profile_pic, status } = user;
  const first_name = name.split(" ")[0];

  return (
    <div className="Empty">
      <h1 className="Empty__name">Welcome, {first_name} </h1>
      <img src={profile_pic} alt={name} className="Empty__img" />
      <p className="Empty__status">
        <b>Status:</b> {status}
      </p>
      <button className="Empty__btn">Start a conversation</button>
      <p className="Empty__info">
        Search for someone to start chatting with or go to Contacts to see who
        is available
      </p>
    </div>
  );
};

export default Empty;
```

Oups. Qu'est-ce que tout ce code ???

Prenez du recul, ce n'est pas aussi complexe qu'il y paraît.

Le composant `<Empty />` prend une prop `user`. Cette prop user est un objet qui a la forme suivante :

```js
{ 
name,
email,
profile_pic,
status,
user_id:
}
```

En utilisant la syntaxe de déstructuration ES6, récupérez le `name`, `profile_pic` et `status` de l'objet user :

```js
const { name, profile_pic, status } = user;
```

Pour la plupart des utilisateurs, le `name` contient deux mots comme `Ohans Emmanuel`. Récupérez le premier mot et attribuez-le à la variable `first_name` comme ceci :

```js
const first_name = name.split(" ")[0];
```

L'instruction return ne fait que générer un morceau de balisage.

Vous verrez le résultat de cela très bientôt.

Avant d'aller plus loin, n'oublions pas de créer un composant `ChatWindow` dans le répertoire `containers`.

`ChatWindow` sera responsable de l'affichage des conversations pour un contact utilisateur actif, et il va beaucoup parler directement à Redux !

Dans `ChatWIndow.js`, écrivez ce qui suit :

```js
import React from "react";

const ChatWindow = ({ activeUserId }) => {
  return (
    <div className="ChatWindow">Conversation for user id: {activeUserId}</div>
  );
};

export default ChatWindow;
```

Nous reviendrons pour développer cela. Pour l'instant, c'est assez bon.

Enregistrez toutes les modifications que nous avons apportées jusqu'à présent, et voici ce que j'ai obtenu !

![Image](https://cdn-media-1.freecodecamp.org/images/1*ie5XT_f-aIP6yqBqKP2g_g.png)
_L'écran vide non stylisé étant affiché._

Vous devriez avoir quelque chose de très similaire aussi.

L'écran vide fonctionne, mais il est laid, et personne n'aime les applications laides.

J'ai écrit le CSS pour le composant `<Empty />`.

`**Empty.css**`

```css
.Empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.Empty__name {
  color: #fff;
}
.Empty__status,
.Empty__info {
  padding: 1rem;
}
.Empty__status {
  color: rgba(255, 255, 255, 0.9);
  border-bottom: 1px solid rgba(255, 255, 255, 0.7);
}
.Empty__img {
  border-radius: 50%;
  margin: 2rem 0;
}
.Empty__btn {
  padding: 1rem;
  margin: 1rem 0;
  font-weight: bold;
  font-size: 1.2rem;
  border-radius: 30px;
  outline: 0;
}
.Empty__btn:hover {
  background: rgba(255, 255, 255, 0.7);
  cursor: pointer;
}
```

Juste du bon vieux CSS. Je parie que vous pouvez comprendre les styles.

Maintenant, voici le résultat de cela :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lkMhgMt15B3tDBePYzkREA.png)
_Avec un peu de CSS, l'écran vide prend rapidement vie._

Voici le résultat avec les outils de développement ancrés :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6Bbqw6YS3C9Nmj0k2mWh_A.png)
_Cela a l'air bien ? Le résultat jusqu'à présent !_

Maintenant, cela a définitivement l'air bien !

### Construction de la Fenêtre de Chat

![Image](https://cdn-media-1.freecodecamp.org/images/1*aeHtPLMsGT6hV84tzTir7w.png)
_Voici toute la fenêtre de chat._

Jetez un coup d'œil à la logique dans le composant `<Main />`. `<ChatWindow />` ne sera affiché que lorsque `activeUserId` est présent.

Pour l'instant, `activeUserId` est défini sur `null`.

Nous devons nous assurer que l'`activeUserId` est défini chaque fois qu'un contact est cliqué.

Qu'en pensez-vous ?

Nous devons dispatcher une action, n'est-ce pas ?

Oui !

Définissons la forme de l'action.

Souvenez-vous qu'une action est simplement un objet avec un champ `type` et un `payload`.

Le champ `type` est obligatoire, tandis que vous pouvez appeler `payload` comme vous le souhaitez. `payload` est un bon nom. Très courant aussi.

Ainsi, voici une représentation de l'action :

```js
{
  type: "SET_ACTION_ID",
  payload: user_id
}
```

Le type ou le nom de l'action sera appelé `SET_ACTION_ID`.

Au cas où vous vous poseriez la question, il est assez courant d'utiliser le snake case avec des lettres majuscules dans les types d'action tels que `SET_ACTION_ID` et non `setactionid` ou `set-action-id`.

De plus, le payload de l'action sera le `user_id` de l'utilisateur à définir comme actif.

Définissons maintenant les actions lors de l'interaction de l'utilisateur.

Puisque c'est la première fois que nous dispatchons des actions dans cette application, créez un nouveau répertoire `actions`. Pendant que vous y êtes, créez également un dossier `constants`.

Dans le dossier `constants`, créez un nouveau fichier, `action-types.js`.

Ce fichier a pour seule responsabilité de conserver les constantes de type d'action. Je vais expliquer pourquoi cela est important, sous peu.

Écrivez ce qui suit dans `action-types.js`.

`**constants/action-types.js**`

```js
export const SET_ACTIVE_USER_ID = "SET_ACTIVE_USER_ID";
```

Alors, pourquoi est-ce important ?

Pour comprendre cela, nous devons examiner où les types d'action sont utilisés dans une application Redux.

Dans la plupart des applications Redux, ils apparaîtront à deux endroits.

1. Le Reducer

Lorsque vous faites un `switch` sur le type d'action dans vos reducers :

```js
switch(action.type)  {
  case "RETIRER_DE_L'ARGENT":
     faireQuelqueChose();
     break;
}
```

2. Le Créateur d'Action

Dans le créateur d'action, vous écrivez également un code qui ressemble à ceci :

```js
export const seRetirerMontant = montant => ({
  type: "RETIRER_DE_L'ARGENT,
  payload: montant
})
```

Maintenant, jetez un coup d'œil à la logique du reducer et du créateur d'action ci-dessus. Qu'est-ce qui est commun aux deux ?

La chaîne de caractères `"RETIRER_DE_L'ARGENT"` !

À mesure que votre application grandit et que vous avez beaucoup de ces chaînes qui traînent, vous (ou quelqu'un d'autre) pourriez un jour faire l'erreur d'écrire `"RETIRER_DE_L'ARGENT"` ou `"RETIRER_DE_L'ARGENT_"` au lieu de `"RETIRER_DE_L'ARGENT_"`

Le point que j'essaie de faire est que l'utilisation de chaînes brutes comme celle-ci facilite les fautes de frappe. D'expérience, les bugs qui proviennent de fautes de frappe sont super énervants. Vous pourriez finir par chercher pendant si longtemps, pour vous rendre compte que le problème était causé par une toute petite erreur de votre part.

Évitez de devoir gérer ce tracas.

Une bonne façon de faire est de stocker les chaînes en tant que constantes dans un fichier séparé. De cette façon, au lieu d'écrire les chaînes brutes à plusieurs endroits, vous importez simplement la chaîne de la constante déclarée.

Vous déclarez les constantes à un seul endroit, mais vous pouvez les utiliser dans autant d'endroits que possible. Pas de fautes de frappe !

C'est exactement pourquoi nous avons créé le fichier `constants/action-types.js`.

Maintenant, créons le créateur d'action.

`**action/index.js**`

```js
import { SET_ACTIVE_USER_ID} from "../constants/action-types";

export const setActiveUserId = id => ({
  type: SET_ACTIVE_USER_ID,
  payload: id
});
```

Comme vous pouvez le voir, j'ai importé la chaîne de type d'action depuis le dossier des constantes. Tout comme je l'ai expliqué plus tôt.

Encore une fois, le créateur d'action est simplement une fonction. J'ai appelé cette fonction `setActiveUserId`. Elle prendra un `id` d'utilisateur et retournera l'action (c'est-à-dire l'objet) avec le type et le payload correctement définis.

Avec cela en place, ce qui reste est de dispatcher cette action lorsqu'un utilisateur clique sur un utilisateur, et de faire quelque chose avec l'action dispatchée dans nos reducers.

Continuons.

Jetez un coup d'œil au composant `User.js`.

La première ligne de l'instruction `return` est une `div` avec le nom de classe, `User` :

```js
<div className="User">
```

C'est le bon endroit pour configurer le gestionnaire de clics. Dès que cette `div` est cliquée, nous allons dispatcher l'action que nous venons de créer.

Donc, voici le changement :

```js
<div className="User" onClick={handleUserClick.bind(null, user)}>
```

Et la fonction `handleUserClick` est juste ici :

```js
function handleUserClick({ user_id }) {
  store.dispatch(setActiveUserId(user_id));
}
```

Où `setActiveUserId` a été importé d'où ? Le créateur d'action !

```js
import { setActiveUserId } from "../actions";
```

Maintenant, voici tout le code `User.js` que vous devriez avoir à ce stade :

`**containers/User.js**`

```js
import React from "react";
import "./User.css";
import store from "../store";
import { setActiveUserId } from "../actions";

const User = ({ user }) => {
  const { name, profile_pic, status } = user;

  return (
    <div className="User" onClick={handleUserClick.bind(null, user)}>
      <img src={profile_pic} alt={name} className="User__pic" />
      <div className="User__details">
        <p className="User__details-name">{name}</p>
        <p className="User__details-status">{status}</p>
      </div>
    </div>
  );
};

function handleUserClick({ user_id }) {
  store.dispatch(setActiveUserId(user_id));
}

export default User;
```

Pour dispatcher l'action, j'ai également dû importer le `store` et appelé la méthode, `store.dispatch()`.

Notez également que j'ai utilisé la syntaxe de déstructuration ES6 pour récupérer le `user_id` de l'argument `user` dans `handleUserClick`.

Si vous codez, comme je le recommande, cliquez sur l'un des contacts utilisateur et inspectez les logs. Vous pouvez ajouter une console log à `handleUserClick` comme ceci :

```js
function handleUserClick({ user_id }) {
  console.log(user_id);
  store.dispatch(setActiveUserId(user_id));
}
```

Vous trouverez l'ID utilisateur logué du contact utilisateur.

Comme vous l'avez peut-être déjà remarqué, l'action est dispatchée, mais rien ne change à l'écran. L'`activeUserId` n'est pas défini dans l'objet d'état. C'est parce que pour l'instant, les reducers ne savent rien de l'action dispatchée.

Corrigeons cela, mais n'oubliez pas de supprimer le `console.log(user_id)` après avoir inspecté les logs.

Jetez un coup d'œil au reducer `activeUserId` :

```js
export default function activeUserId(state = null, action) {
  return state;
}
```

**reducer/activeUserId.js**

```js
import { SET_ACTIVE_USER_ID } from "../constants/action-types";
export default function activeUserId(state = null, action) {
  switch (action.type) {
    case SET_ACTIVE_USER_ID:
      return action.payload;
    default:
      return state;
  }
}
```

Vous devriez comprendre ce qui se passe ici.

La première ligne importe la chaîne, `SET_ACTIVE_USER_ID`.

Nous vérifions ensuite si l'action passée est de `type` `SET_ACTIVE_USER_ID`. Si oui, alors la nouvelle valeur de `activeUserId` est définie sur `action.payload`.

N'oubliez pas que le payload de l'action contient le `user_id` du contact utilisateur.

Voyons cela en action. Est-ce que cela fonctionne comme prévu ?

Oui !

![Image](https://cdn-media-1.freecodecamp.org/images/1*uUnt0X7O7xHjoZedOhpv_w.gif)
_Hourra ! Nous avons réussi pour l'instant ;)_

Maintenant, le composant `ChatWindow` est rendu avec le bon `activeUserId` défini.

Pour rappel, il est important de se souvenir que avec la composition de reducers, la valeur retournée par chaque reducer est la valeur du champ d'état qu'ils représentent, et non l'objet d'état entier.

### Décomposition de la Fenêtre de Chat en Composants Plus Petits

Jetez un coup d'œil à ce à quoi ressemble la fenêtre de chat complète :

![Image](https://cdn-media-1.freecodecamp.org/images/1*aeHtPLMsGT6hV84tzTir7w.png)
_Voici toute la fenêtre de chat._

Pour une approche de développement plus saine, je l'ai décomposée en trois sous-composants, `Header`, `Chats` et `MessageInput` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*eeT_vo5kurzpUj42cKn4qQ.png)
_Les sous-composants, Header, Chats et MessageInput_

Ainsi, afin de compléter le composant `chatWindow`, nous allons construire ces trois sous-composants. Nous allons ensuite les composer pour former le composant `chatWindow`.

Prêt ?

Commençons par le composant Header.

Le contenu actuel du composant `chatWindow` est le suivant :

```js
import React from "react";

const ChatWindow = ({ activeUserId }) => {
  return (
    <div className="ChatWindow">Conversation for user id: {activeUserId}</div>
  );
};

export default ChatWindow;
```

Pas très utile.

Mettez à jour le code comme suit :

```js
import React from "react";
import store from "../store";
import Header from "../components/Header";

const ChatWindow = ({ activeUserId }) => {
  const state = store.getState();
  const activeUser = state.contacts[activeUserId];

  return (
    <div className="ChatWindow">
      <Header user={activeUser} />
    </div>
  );
};

export default ChatWindow;
```

Qu'est-ce qui a changé ?

Souvenez-vous que l'`activeUserId` est passé en tant que props dans le composant `ChatWindow`.

Maintenant, au lieu de rendre le texte, _Conversation pour l'ID utilisateur : …_, rendez le composant `Header`.

Le composant Header ne peut pas être rendu correctement sans avoir connaissance de l'utilisateur cliqué. Pourquoi ?

Le `name` et `status` rendus dans le `Header` sont ceux de l'utilisateur cliqué.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m3yYXHGTvw45jRg4bxXn_A.png)
_Les informations dans l'en-tête sont celles du contact cliqué._

Pour garder une trace de l'utilisateur actif, une nouvelle variable, `activeUser` est créée, et la valeur est récupérée de l'objet d'état comme ceci : `const activeUser = state.contacts[activeUserId]`.

Comment cela fonctionne-t-il ?

Tout d'abord, nous récupérons l'état du store Redux : `const state = store.getState()`.

Maintenant, souvenez-vous que chaque contact de l'utilisateur de l'application est stocké dans le champ `contacts`. De plus, chaque utilisateur est mappé par son `user_id`.

Ainsi, l'utilisateur actif peut être récupéré en récupérant l'utilisateur avec le champ id correspondant de l'objet `contacts` : `state.contacts[activeUserId]`.

Tout est compris ?

À ce stade, nous devons construire le composant `Header` rendu.

Créez les fichiers, `Header.js` et `Header.css` dans le répertoire `components`.

Le contenu de `Header.js` est simple. Le voici :

```js
import React from "react";
import "./Header.css";

function Header({ user }) {
  const { name, status } = user;
  return (
    <header className="Header">
      <h1 className="Header__name">{name}</h1>
      <p className="Header__status">{status}</p>
    </header>
  );
}

export default Header;
```

C'est un composant fonctionnel sans état qui rend un élément `header` et des balises `h1` et `p` pour contenir le _name_ et le _status_ de l'utilisateur actif.

N'oubliez pas que l'utilisateur actif est l'utilisateur cliqué dans la barre latérale.

Les styles pour le composant `<Header />` sont également simples. Les voici :

```css
.Header {
  padding: 1rem 2rem;
  border-bottom: 1px solid rgba(189, 189, 192, 0.2);
}
.Header__name {
  color: #fff;
}
```

Maintenant, nous avons ce bébé qui fonctionne !

![Image](https://cdn-media-1.freecodecamp.org/images/1*xRdtESErP36hhmVyHXDDKQ.gif)
_Cela a l'air bien !_

Incroyable. Si vous êtes encore là, vous vous en sortez vraiment bien !

Passons à la construction du composant `<Chats />`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AwvWSDCdk-b8fmol-JfLrA.png)
_Le composant Chats à construire_

Le composant `<Chats />` est essentiellement une liste rendue des conversations d'un utilisateur.

Alors, d'où viennent ces conversations ?

Oui, de l'état de l'application.

Comme je l'ai expliqué précédemment, une application réelle récupérera ces conversations depuis un serveur. Cependant, mon approche pour apprendre Redux est que vous éliminiez autant de complexités que possible lorsque vous apprenez les fondamentaux.

À cette fin, il n'y aura pas de ressource de récupération de serveur ici. Nous allons connecter les données en utilisant quelques fonctions d'assistance que j'ai créées pour la génération de données utilisateur aléatoires.

Commençons par connecter les données requises à l'état de l'application.

Le processus est le même que nous l'avons fait plusieurs fois déjà.

1. Créez un Reducer
2. En utilisant ES6, ajoutez une valeur de paramètre par défaut au reducer
3. Incluez le reducer dans l'appel de la fonction `combineReducers`.

Allez-vous essayer cela avant de passer à ma solution ?

Voici ma solution, de toute façon.

Créez un nouveau fichier, `messages.js` dans le répertoire `reducers`. Ce sera le reducer des messages.

Voici le contenu du reducer des messages.

`**reducers/messages.js**`

```js
import { getMessages } from "../static-data";

export default function messages(state = getMessages(10), action) {
  return state;
}
```

Pour générer des messages aléatoires, j'ai importé la fonction `getMessages` de `static-data`

Cette fonction prend une quantité, représentée par un nombre. La fonction `getMessages` générera alors cette quantité de messages pour chaque contact utilisateur.

Par exemple, `getMessages(10)` générera 10 messages par contact utilisateur.

Maintenant, incluez le reducer dans l'appel de la fonction `combineReducers` dans `reducers/index.js`

`**reducers/index.js**`

```js
import messages from "./messages";

export default combineReducers({
  user,
  messages,
  contacts,
  activeUserId
});
```

Faire cela inclura un champ `messages` dans l'objet d'état.

Voici un aperçu des logs. Vous trouverez maintenant `messages` comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*9IhFBz5uRrwih4Z0fkDzcA.png)
_Les messages existent maintenant dans l'objet d'état._

Avec cela en place, nous pouvons reprendre en toute sécurité la construction du composant `Chats`.

Si vous ne l'avez pas déjà fait, créez les fichiers, `Chats.js` et `Chats.css` dans le répertoire des composants.

Maintenant, importez `Chats` et rendez-le sous le composant `<Header />` dans `ChatWindow`.

`**containers/ChatWindow.js**`

```js
... 
import Chats from "../components/Chats"; 
... 
return (
    <div className="ChatWindow">
      <Header user={activeUser} />
      <Chats />
    </div>
  );
```

Le composant `<Chats/>` prendra la liste des messages de l'objet d'état, mappée sur ces messages, puis les rendra joliment.

N'oubliez pas que les messages passés à `Chats` sont spécifiquement les messages de l'utilisateur actif !

Alors que `state.messages` contient tous les messages de chaque contact utilisateur, `state.messages[activeUserId]` récupérera les messages de l'utilisateur actif.

C'est pourquoi chaque conversation est mappée à l'ID utilisateur du contact — pour une récupération facile comme nous l'avons fait.

Récupérez les messages de l'utilisateur actif et passez-les en tant que props dans `Chats`.

`**containers/ChatWindow.js**`

```js
... 
import Chats from "../components/Chats"; 
... 
const activeMsgs = state.messages[activeUserId];

return (
    <div className="ChatWindow">
      <Header user={activeUser} />
      <Chats messages={activeMsgs} />
    </div>
  );
```

Maintenant, souvenez-vous que les messages de chaque utilisateur sont un grand objet avec chaque message ayant un champ de nombre :

![Image](https://cdn-media-1.freecodecamp.org/images/1*9Ee2u0S5l_SnOew-qLIFKw.png)
_Jetez un autre coup d'œil au champ des messages_

Pour une itération et un rendu plus faciles, nous allons convertir cela en un tableau. Tout comme nous l'avons fait avec la liste des utilisateurs dans la Sidebar.

Pour cela, nous aurons besoin de `Lodash`.

`**containers/ChatWindow.js**`

```js
... 
import _ from "lodash";
import Chats from "../components/Chats"; 
... 
const activeMsgs = state.messages[activeUserId];

return (
    <div className="ChatWindow">
      <Header user={activeUser} />
      <Chats messages={_.values(activeMsgs)} />
    </div>
  );
```

Maintenant, au lieu de passer `activeMsgs`, nous passons `_.values(activeMsgs)`.

Il y a une étape importante avant de voir les résultats.

Le composant `Chats` n'a pas encore été créé.

Dans `Chats.js`, écrivez ce qui suit. Je vais expliquer ensuite.

`**containers/Chat.js**`

```js
import React, { Component } from "react";
import "./Chats.css";

const Chat = ({ message }) => {
  const { text, is_user_msg } = message;
  return (
    <span className={`Chat ${is_user_msg ? "is-user-msg" : ""}`}>{text}</span>
  );
};

class Chats extends Component {
  render() {
    return (
      <div className="Chats">
        {this.props.messages.map(message => (
          <Chat message={message} key={message.number} />
        ))}
      </div>
    );
  }
}

export default Chats;
```

Ce n'est pas trop difficile à comprendre, mais je vais expliquer ce qui se passe.

Tout d'abord, jetez un coup d'œil au composant `Chats`. Vous remarquerez que j'ai utilisé un composant basé sur une classe ici. Vous verrez pourquoi plus tard.

Dans la fonction render, nous mappons sur les props `messages` et pour chaque `message`, nous retournons un composant `Chat`.

Le composant `Chat` est super simple :

```js
const Chat = ({ message }) => {
  const { text, is_user_msg } = message;
  return (
    <span className={`Chat ${is_user_msg ? "is-user-msg" : ""}`}>{text}</span>
  );
};
```

Pour chaque message qui est passé, le contenu `text` du message et le drapeau `is_user_msg` sont tous deux récupérés en utilisant la syntaxe de déstructuration ES6, `const { text, is_user_msg } = message;`

L'instruction return est plus intéressante.

Une simple balise `span` est rendue.

Retirez un peu de la magie `JSX`, et voici la forme simple de ce qui est rendu :

```js
<span> {text} </span>
```

Le contenu textuel du message est enveloppé dans un élément `span`. Simple.

Cependant, nous devons différencier le message de l'utilisateur de l'application et le message du contact.

N'oubliez pas qu'une conversation se fait avec au moins deux personnes qui s'envoient des messages.

Si le message rendu est celui de l'utilisateur, nous voulons que le balisage rendu soit le suivant :

```
<span className="Chat  is-user-msg"> {text} &lt;/span>
```

Et si ce n'est pas le cas, nous voulons ceci :

```js
<span className="Chat  is-user-msg"> {text} </span>
```

Remarquez que ce qui a changé est la classe `is-user-msg` qui est basculée.

De cette façon, nous pouvons spécifiquement styliser le message de l'utilisateur en utilisant le sélecteur css montré ci-dessous :

```js
.Chat.is-user-msg {

}
```

Alors, c'est pourquoi nous avons un peu de `JSX` fantaisiste pour rendre les noms de classe en fonction de la présence ou de l'absence du drapeau `is_user_msg`.

```js
<span className={`Chat ${is_user_msg ? "is-user-msg" : ""}`}>{text}</span>
```

La vraie sauce est ici :

`${is_user_msg ? "is-user-msg" : `

C'est l'opérateur ternaire !

Vous pouvez comprendre tout le code dans `containers/Chats.js` maintenant, hein ?

Voici le résultat jusqu'à présent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VIdMgEfqJllrqEP0us1DCg.gif)
_Le résultat actuel de nos itérations. Il a encore besoin de travail._

Les messages sont rendus mais cela ne ressemble pas à grand-chose. C'est parce que tous les messages sont rendus dans des balises `span`.

Puisque les balises `span` sont des éléments en ligne, tous les messages se rendent simplement en une ligne continue, ayant l'air écrasés.

C'est là que mon pote CSS brille.

Ajoutons un peu de magie CSS et commençons la fête :)

En commençant par la Fenêtre de Chat, créez un nouveau fichier, `ChatWindow.css` dans le répertoire `containers`.

N'oubliez pas de l'importer dans `ChatWindow.js` comme ceci : `import "./ChatWindow.css"`

Écrivez ceci dedans :

```css
.ChatWindow {
    display: flex;
    flex-direction: column;
    height: 100vh;
}
```

Cela s'assurera que le `ChatWindow` prend toute la hauteur disponible, `100vh`. J'ai également fait de lui un conteneur flex pour que je puisse utiliser quelques fonctionnalités flex tout en alignant ses éléments, à savoir, `Header`, `Chats` et `Message`.

Vous pouvez voir le `ChatWindow` avec une bordure rouge ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kESXliVu5zdPLItobZUBjw.png)
_ChatWindow — pas encore le meilleur des looks._

Passons maintenant au style des Messages de Chat.

`**components/Chats.css**`

```css
.Chats {
  flex: 1 1 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 85%;
  margin: 0 auto;
  overflow-y: scroll;
}
.Chat {
  margin: 1rem 0;
  color: #fff;
  padding: 1rem;
  background: linear-gradient(90deg, #1986d8, #7b9cc2);
  max-width: 90%;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}
.Chat.is-user-msg {
  margin-left: auto;
  background: #2b2c33;
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}

@media (min-width: 576px) {
  .Chat {
    max-width: 60%;
  }
}
```

Mon Dieu ! Cela a déjà l'air si bien !

![Image](https://cdn-media-1.freecodecamp.org/images/1*GmCRmgEOsLRVpBpUqaD_Kg.gif)
_À quel point c'est beau :)_

Laissez-moi expliquer certaines des déclarations de style importantes.

Avec `flex: 1 1 0`, `.Chats` est fait pour grandir (prendre l'espace disponible) et se réduire en conséquence dans `ChatWindow`.

`.Chats` est également fait d'un conteneur flex avec `display: flex`. En définissant `flex-direction: column`, tous les messages de chat sont alignés verticalement. Ils ne sont plus des éléments en ligne mais des éléments flex !

Les chats qui ne sont pas ceux de l'utilisateur sont donnés un dégradé de fond bleuâtre avec `background: linear-gradient(90deg, #1986d8, #7b9cc2);`

Cela est remplacé si le message est celui de l'utilisateur :

```css
.Chat.is-user-msg {
  background: #2b2c33;
}
```

Je crois que vous pouvez comprendre tout le reste.

Jusqu'à présent, tout va bien !

Je suis vraiment excité de voir jusqu'où nous sommes allés. Une dernière étape, et la fenêtre de chat est complètement construite !

Construisons le composant Message Input.

Nous avons dû construire des composants plus difficiles. Celui-ci ne sera pas difficile à construire.

Cependant, il y a un point à considérer.

Le composant Input sera un composant contrôlé. Par conséquent, nous allons stocker la valeur de l'input dans l'objet d'état de l'application.

Pour cela, nous aurons besoin d'un nouveau champ appelé `typing` dans l'objet d'état.

Mettons cela en place.

Pour nos considérations, chaque fois qu'un utilisateur tape, nous allons dispatcher une action de type `SET_TYPING_VALUE`.

Assurez-vous d'ajouter cette constante dans le fichier `**constants/action-types.js**` :

```js
export const SET_TYPING_VALUE = "SET_TYPING_VALUE";
```

De plus, la forme de l'action dispatchée ressemblera à ceci :

```js
{
   type: SET_TYPING_VALUE,
   payload: "input value"
}
```

Où le `payload` de l'action est la valeur tapée dans l'input. Créons un créateur d'action pour gérer la création de cette action :

`**actions/index.js**`

```js
import {
  ...
  SEND_MESSAGE
} from "../constants/action-types";

export const sendMessage = (message, userId) => ({
  type: SEND_MESSAGE,
  payload: {
    message,
    userId
  }
})
```

Cela signifie également que la constante de type d'action `SEND_MESSAGE` doit être créée dans `**constants/action-types.js**`.

```js
export const SEND_MESSAGE = "SEND_MESSAGE";
```

Avant de tester le code, vous ne devez pas oublier de mettre à jour les imports des créateurs d'action dans `**MessageInput.js**` pour inclure `sendMessage`.

```js
import { setTypingValue, sendMessage } from "../actions";
```

Alors, essayez-le. Est-ce que le code fonctionne ?

Euh, non, ça ne fonctionne pas.

Le formulaire est soumis, la page ne se recharge pas grâce à la soumission du formulaire, l'action est dispatchée, mais toujours pas de mises à jour.

Nous n'avons rien fait de mal, sauf que le type d'action n'a pas été pris en compte dans l'un des reducers.

Les reducers ne savent rien de cette nouvelle action de type, `SEND_MESSAGE`.

Corrigeons cela ensuite.

### Mise à Jour de l'État des Messages

Voici une liste de tous les reducers que nous avons à ce stade :

```
activeUserId.js
contacts.js
messages.js
typing.js
user.js
```

Lequel de ceux-ci pensez-vous devrait être concerné par la mise à jour des messages dans une conversation utilisateur ?

Oui, le reducer `messages`.

Voici le contenu actuel du reducer `messages` :

```js
import { getMessages } from "../static-data";

export default function messages(state = getMessages(10), action) {
  return state;
}
```

Pas grand-chose à faire là-dedans.

Importez le type d'action `SEND_MESSAGE`, et commençons à le gérer dans ce reducer `messages`.

```js
import { getMessages } from "../static-data";
import { SEND_MESSAGE } from "../constants/action-types";

export default function messages(state = getMessages(10), action) {
  switch (action.type) {
    case SEND_MESSAGE:
      return "";
    default:
      return state;
  }
}
```

Maintenant, nous gérons le type d'action, `SEND_MESSAGE` mais une chaîne vide est retournée.

Ce n'est pas ce que nous voulons, mais nous allons construire cela à partir de là. En attendant, quelle est, selon vous, la conséquence de retourner une chaîne vide ici ?

Laissez-moi vous montrer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2T20DwKd8UrlKX454QWZjw.gif)

Tous les messages disparaissent ! Mais pourquoi ? C'est parce que dès que nous appuyons sur Entrée, l'action `SEND_MESSAGE` est dispatchée. Dès que cette action atteint le reducer, le reducer retourne une chaîne vide ``.

Ainsi, il n'y a plus de messages dans l'objet d'état. Tout est parti !

C'est définitivement inacceptable.

Ce que nous voulons, c'est conserver tous les messages qui sont dans l'état. Cependant, nous voulons ajouter un nouveau message **uniquement** aux messages de l'utilisateur actif.

D'accord. Mais comment ?

Souvenez-vous que chaque utilisateur a ses messages mappés à son ID. Tout ce que nous avons à faire est de cibler cet ID et de mettre à jour **uniquement** les messages qui s'y trouvent.

Voici à quoi cela ressemble graphiquement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pMUn2YaNncGFepMCegGdsQ.png)
_un aperçu de ce qui doit être fait._

Veuillez regarder la console dans le graphique ci-dessus. Le graphique suppose qu'un utilisateur a soumis le formulaire d'entrée trois fois avec le texte, `Hi`.

Comme prévu, le texte, `Hi` apparaît trois fois dans les conversations de chat pour le contact particulier.

Maintenant, jetez un coup d'œil à la console. Cela vous donnera une idée de ce que nous visons dans la solution de code à venir.

Dans cette application, chaque utilisateur a 10 messages. Chacun des messages a un numéro qui va de `0` à `9`.

Ainsi, chaque fois qu'un utilisateur soumet un nouveau message, nous voulons ajouter un nouvel objet `message` mais avec des numéros croissants !

Dans la console dans le graphique ci-dessus, vous remarquerez que le numéro augmente. `10`, `11` et `12`.

De plus, la forme du message reste la même, ayant les champs `number`, `text` et `is_user_msg`.

```js
{ 
  number: 10,
  text: "the text typed",
  is_user_msg: true
}
```

`is_user_msg` sera toujours vrai pour ces messages. Ils viennent de l'utilisateur !

Maintenant, représentons cela avec un peu de code.

Je vais bien expliquer cela, car le code peut sembler complexe au premier abord.

En tout cas, voici la représentation dans le bloc `switch` du reducer `messages` :

```js
switch (action.type) {
    case SEND_MESSAGE:
      const { message, userId } = action.payload;
      const allUserMsgs = state[userId];
      const number = +_.keys(allUserMsgs).pop() + 1;

      return {
        ...state,
        [userId]: {
          ...allUserMsgs,
          [number]: {
            number,
            text: message,
            is_user_msg: true
          }
        }
      };

    default:
      return state;
  }
```

Passons en revue cela ligne par ligne.

Juste après le `case SEND_MESSAGE:`, nous gardons une référence au `message` et `userId` passés dans le payload.

```js
const {message, userId } = action.payload
```

Pour continuer, il est également important de récupérer les messages de l'utilisateur actif. Cela est fait à la ligne suivante avec :

```js
const allUserMsgs = state[userId];
```

Comme vous le savez peut-être déjà, `state` ici n'est pas l'objet d'état global de l'application. Non. C'est l'état géré par le reducer pour le champ `messages`.

Puisque chaque message d'un contact est mappé avec son user ID, le code ci-dessus récupère les messages pour l'ID utilisateur spécifique passé dans le payload.

Maintenant, chaque message a un `number`. Cela agit comme une sorte d'identifiant unique. Pour que les messages entrants aient un identifiant unique, `_.keys(allUserMsgs)` retournera un tableau de toutes les clés des messages de l'utilisateur.

D'accord, laissez-moi expliquer.

`_.keys` est comme `Object.keys()`. La seule différence ici est que j'utilise l'assistant de `Lodash`. Vous pouvez utiliser `Object.keys()` si vous le souhaitez.

De plus, `allUserMsgs` est un objet qui contient tous les messages de l'utilisateur. Il ressemblera à quelque chose comme ceci :

```js
{
  0: {
    number: 0,
    text: "first message"
    is_user_msg: false
  },
  1: {
     number: 0,
     text: "first message"
     is_user_msg: false
  }
}
```

Cela continuera jusqu'au 10ème message !

Lorsque nous faisons `_.keys(allUserMsgs)` ou `Object.keys(allUserMsgs)`, cela retournera un tableau de toutes les clés. Quelque chose comme ceci :

```js
[ 0, 1, 2, 3, 4, 5]
```

La fonction `Array.pop()` est utilisée pour récupérer le dernier élément du tableau. C'est le plus grand nombre déjà existant pour les messages du contact. Un peu comme le dernier ID de message du contact.

Une fois que cela est récupéré, nous ajoutons `+ 1` à celui-ci. En nous assurant que le nouveau message obtient `+ 1` du plus grand nombre des messages disponibles.

Voici tout le code responsable de cela à nouveau :

```js
const number = +_.keys(allUserMsgs).pop() + 1;
```

Si vous vous demandez pourquoi il y a un `+` avant le `_.keys(allUserMsgs).pop() + 1`, c'est pour s'assurer que le résultat est converti en un Nombre au lieu d'une Chaîne.

C'est tout !

Passons à la partie principale du bloc de code :

```js
return {
        ...state,
        [userId]: {
          ...allUserMsgs,
          [number]: {
            number,
            text: message,
            is_user_msg: true
          }
        }
      };
```

Regardez de près, et je suis sûr que vous comprendrez.

`...state` s'assurera que nous ne touchons pas aux messages précédents dans l'application.

Parce que nous utilisons des notations d'objet, nous pouvons facilement récupérer le message avec l'ID utilisateur particulier avec `[userID]`

Dans l'objet, nous nous assurons que tous les messages de l'utilisateur ne sont pas touchés : `...allUserMsgs`

Enfin, nous ajoutons le nouvel objet message avec le nombre précédemment calculé !

```js
[number]: {
  number,
  text: message,
  is_user_msg: true
}
```

Cela peut sembler complexe, mais ce n'est pas le cas. Espérons que vous avez de l'expérience avec ce type de calculs d'état non mutants de votre développement React.

Toujours confus ?

Jetez un autre coup d'œil à l'instruction return. Cette fois, avec quelques couleurs de code. Cela peut aider à donner vie au code :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YihT3MVX88qxIFJLPx-Jbw.png)
_jetez un autre coup d'œil à l'instruction return. Pouvez-vous comprendre cela maintenant ?_

Et cela, mon ami, est la fin de la mise à jour de la conversation lorsqu'une entrée est saisie !

Nous avons juste quelques ajustements à faire.

### Ajustements pour Rendre l'Expérience de Chat Naturelle

Voici à quoi ressemble l'état actuel des choses lorsque j'écris `Hello!` et que je soumets trois fois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zKHWIzPY7WntUxJs7T1hfA.gif)
_DÉMO jusqu'à présent._

Vous remarquerez rapidement deux problèmes.

1. Même si les entrées sont soumises et les messages correctement ajoutés aux conversations, je dois faire défiler vers le bas pour voir les messages. Ce n'est pas ainsi que fonctionnent les applications de chat. La fenêtre de chat devrait faire défiler automatiquement vers le bas.
2. Il serait bien de vider la valeur de l'input lorsqu'elle est soumise. De cette façon, l'utilisateur obtient un retour immédiat que son input a été soumis.

Le deuxième est une correction beaucoup plus facile. Commençons par cela.

Nous dispatchons déjà une action `SEND_MESSAGE`. Nous pouvons écouter cette action et vider la valeur de l'input dans le reducer `typing.js`.

Faisons exactement cela.

Ajoutez ceci dans le bloc switch du reducer `typing.js` :

```js
case SEND_MESSAGE:
      return "";
```

Ce qui porte tout le code à ceci :

`**reducer/typing.js**`

```js
import { SET_TYPING_VALUE, SEND_MESSAGE } from "../constants/action-types";

export default function typing(state = "", action) {
  switch (action.type) {
    case SET_TYPING_VALUE:
      return action.payload;
    case SEND_MESSAGE:
      return "";
    default:
      return state;
  }
}
```

Maintenant, dès que l'action arrive ici, la valeur `typing` sera effacée et une chaîne vide sera retournée.

Voici cela en action :

![Image](https://cdn-media-1.freecodecamp.org/images/1*iXXkDrUboFW8pqKquzThYQ.gif)

Cela fonctionne !

Comme prévu, la valeur de l'input est maintenant effacée.

D'accord, assurons-nous que la fenêtre de chat fait défiler lorsque elle est mise à jour.

Pour ce faire, nous aurons besoin d'un peu de manipulation du DOM. C'est la raison pour laquelle j'ai insisté pour faire de `<Chats />` un composant de classe.

D'accord, parlons code.

Tout d'abord, nous devons créer une `Ref` pour contenir le nœud DOM de Chats.

```js
constructor(props) {
    super(props);
    this.chatsRef = React.createRef();
  }
```

Si vous n'êtes pas familier avec `React.createRef()`, c'est parfaitement normal. C'est parce que React 16 a introduit une [nouvelle façon de créer des Refs](https://reactjs.org/docs/refs-and-the-dom.html).

Nous gardons une référence à cette `Ref` via `this.chatsRef`.

Dans le DOM rendu, nous mettons ensuite à jour la ref comme ceci :

```js
<div className="Chats" ref={this.chatsRef}>
```

Nous avons maintenant une référence à la `div` qui contient toutes les conversations de chat.

Assurons-nous que cela est toujours défilé vers le bas lorsqu'il est mis à jour.

Dites bonjour aux méthodes de cycle de vie !

```js
componentDidMount() {
    this.scrollToBottom();
  }
  componentDidUpdate() {
    this.scrollToBottom();
  }
```

Ainsi, dès que le composant est monté, nous invoquons une fonction `scrollToBottom`. Nous faisons de même chaque fois que l'application est mise à jour, aussi !

Maintenant, voici la fonction `scrollToBottom` :

```js
scrollToBottom = () => {
    this.chatsRef.current.scrollTop = this.chatsRef.current.scrollHeight;
  };
```

Tout ce que nous faisons est de mettre à jour la propriété `scrollTop` pour qu'elle corresponde à la `scrollHeight`

Pas si difficile. Le `this.chatsRef.current` fait référence au nœud DOM en question.

Voici tout le code pour `Chats.js` à ce stade.

```js
...

class Chats extends Component {
  constructor(props) {
    super(props);
    this.chatsRef = React.createRef();
  }
  componentDidMount() {
    this.scrollToBottom();
  }
  componentDidUpdate() {
    this.scrollToBottom();
  }
  scrollToBottom = () => {
    this.chatsRef.current.scrollTop = this.chatsRef.current.scrollHeight;
  };

  render() {
    return (
      <div className="Chats" ref={this.chatsRef}>
        {this.props.messages.map(message => (
          <Chat message={message} key={message.number} />
        ))}
      </div>
    );
  }
}

export default Chats;
```

Hé ! Avec cela, nous avons Skypey fonctionnant comme prévu !

Voici une démonstration. Remarquez comment la position de défilement est mise à jour dès que le composant est monté, et lorsqu'un message est tapé, le composant est également mis à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZXbfiqJl3KFHPFUTKisMYg.gif)
_Les résultats finaux ont l'air bien ! Magnifique !_

Des trucs géniaux !

Si excité !

Nous sommes allés si loin :)

### Conclusion et Résumé

Oh mon ! Cela a été une expérience incroyable pour moi. Construire Skypey a été très amusant.

Avez-vous aimé cela ? J'adorerais voir votre propre version de Skypey. Changez les couleurs, modifiez le design, et construisez quelque chose de mieux !

Lorsque vous aurez terminé, [envoyez-moi un tweet](https://twitter.com/OhansEmmanuel) et je serai ravi de vous encourager.

Voici un résumé de certaines des choses que nous avons apprises jusqu'à présent :

* Il est bon de toujours planifier votre processus de développement d'application avant de vous lancer dans le code.
* Dans votre objet d'état, évitez les entités imbriquées à tout prix. Gardez l'objet d'état normalisé.
* Stocker vos champs d'état sous forme d'objets a certains avantages. Soyez également conscient des problèmes liés à l'utilisation d'objets, principalement le manque d'ordre.
* La bibliothèque utilitaire `lodash` est très pratique si vous choisissez d'utiliser des objets plutôt que des tableaux dans votre objet d'état.
* Peu importe la quantité, prenez toujours un peu de temps pour concevoir l'objet d'état de votre application.
* Avec Redux, vous n'avez pas toujours à passer des props. Vous pouvez accéder directement aux valeurs d'état depuis le store.
* Gardez toujours une structure de dossier propre dans vos applications Redux, comme avoir tous les acteurs majeurs de Redux dans leurs propres dossiers. En plus de la structure de code globale propre, cela facilite la collaboration avec d'autres personnes sur votre projet car elles sont probablement familières avec la même structure de dossier.
* La composition de reducers est vraiment géniale surtout à mesure que votre application grandit. Cela augmente la testabilité et réduit la tendance aux erreurs difficiles à suivre.
* Pour la composition de reducers, utilisez `combineReducers` de la bibliothèque `redux`.
* L'objet passé dans la fonction `combineReducers` est conçu pour ressembler à l'état de votre application, chaque valeur étant obtenue à partir des reducers associés.
* Décomposez toujours les composants plus grands en morceaux plus petits et gérables. C'est beaucoup plus facile de construire de cette manière.

À plus tard !

### Exercices

L'application Skypey que nous avons construite ici n'est pas tout ce qu'il y a dans l'application. Il y a deux autres tâches pour vous.

* Étendez l'application Skypey que nous avons construite pour gérer l'édition d'un message utilisateur comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZTThoHF2J7-XGGv_GnWzw.gif)
_Incluez la fonctionnalité d'édition de message montrée ici._

* Étendez l'application Skypey que nous avons construite pour gérer également la suppression d'un message utilisateur. Comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iOmQWbzt4sh1_HeE3enTjA.gif)
_Incluez la fonctionnalité de suppression de message montrée ici._

Cela devrait être amusant à implémenter !

### Chapitre 5 : Et Ensuite ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*6cQLUZREZeokTDCuYJxxPg.png)
_La suite de ce livre actuel_

Le livre que vous lisez actuellement est l'un des trois de la suite Redux Trio.

Dans le deuxième livre, Understanding Redux 2, j'explique en détail les concepts avancés de Redux tels que les Middlewares, les Composants d'Ordre Supérieur, les Appels Ajax, et plus encore.

Cela ne s'arrête pas là.

Je vais également vous montrer quelques-unes des bibliothèques Redux les plus aimées de la communauté pour résoudre des problèmes courants. Reselect, Redux-form, Redux-thunk, Recompose, et bien d'autres.

La section suivante est un extrait de, [Understanding Redux 2](http://thereduxjsbooks.com/).

> _Introduction à React-Redux_  
>   
> _Aller à la banque chaque fois que vous avez besoin de faire un retrait de votre compte est une telle corvée. Eh bien, ne vous en faites pas. Nous sommes en 2018. Nous avons la banque en ligne, n'est-ce pas ?_  
>   
> _Retour à Redux._  
>   
> _Configurer le Reducer, s'abonner au Store, écouter et re-rendre lors des changements d'état … nous pouvons réduire certains des tracas._  
>   
> _Comme la banque en ligne apporte un souffle d'air frais au processus de retrait d'argent de votre compte, les 'bindings' comme react-redux facilitent également l'utilisation de Redux avec React — sans problèmes de performance._

Comme c'est doux.

Prêt ?

Je couvre cela en profondeur dans le livre suivant, [Understanding Redux 2](http://thereduxjsbooks.com/).

Et bien plus encore !

En attendant, je vous retrouve plus tard !

Hey, continuez à coder !

Beaucoup d'amour ??