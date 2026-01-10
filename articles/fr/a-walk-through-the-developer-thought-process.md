---
title: 'Comment les développeurs pensent : Un guide pas à pas de la planification
  et de la conception derrière une application web simple'
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2019-08-29T15:01:34.000Z'
originalURL: https://freecodecamp.org/news/a-walk-through-the-developer-thought-process
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/alvaro-reyes-qWwpHwip31M-unsplash.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: code newbie
  slug: code-newbie
- name: coding
  slug: coding
- name: 'Junior developer '
  slug: junior-developer
- name: programing
  slug: programing
- name: Web Development
  slug: web-development
seo_title: 'Comment les développeurs pensent : Un guide pas à pas de la planification
  et de la conception derrière une application web simple'
seo_desc: "I love the number of awesome tutorials there are on how to make different\
  \ web apps. As great as these are, though, I often felt stuck when it came to starting\
  \ my own web apps. \nSo I wrote this article to walk you through my thought process.\
  \ This is h..."
---

J'adore le nombre de tutoriels géniaux qui existent sur la façon de créer différentes applications web. Malgré leur qualité, j'ai souvent eu l'impression d'être bloqué lorsque je devais commencer mes propres applications web. 

J'ai donc écrit cet article pour vous guider à travers mon processus de réflexion. Voici comment je planifie et développe mes propres projets.

Une petite note avant de commencer : cet article n'est pas un guide "miracle" sur la façon de créer N'IMPORTE QUEL projet. C'est simplement la manière dont j'aborde personnellement mes projets. Cela peut fonctionner pour vous, ou non.

Il n'existe pas de "bonne" façon de créer une application. Rappelez-vous : il existe de nombreuses routes qui vous mèneront à la fin de votre voyage. (Sauf si vous portez un anneau brillant à Mordor, auquel cas il n'y a qu'une seule route, malheureusement).

![Image](https://www.freecodecamp.org/news/content/images/2019/09/39rblx.jpg)

Je vais utiliser React.js pour coder l'application exemple. J'ai inclus un Code Sandbox avec l'application terminée à la fin de cet article. 

Vous devrez donc également avoir une familiarité de base avec la configuration d'un projet React. Ne vous inquiétez pas, les principes de cet article s'appliquent encore, quel que soit le langage que vous utilisez pour coder l'application.

D'accord, commençons. Aujourd'hui, nous allons concevoir une... TODO-LIST !

Je plaisante. Nous allons créer une calculatrice simple.

## "Qu'est-ce qu'elle fait ?"

C'est la première question que je me pose avant de commencer un projet personnel. Je veux que ma calculatrice puisse :

* Additionner, soustraire, diviser et multiplier des nombres
* Afficher le résultat du calcul 
* Réinitialiser l'affichage

Cela devrait suffire pour l'instant. Planifier les fonctionnalités de cette manière vous donne une idée de ce que votre application fera et commence à vous mettre "dans la zone", pour ainsi dire. 

Cette approche vous donne également un objectif solide à atteindre. Une fois que vous avez implémenté toutes les fonctionnalités, vous avez terminé et vous pouvez commencer à penser à votre prochain projet personnel - Hourra ! 

Sinon, vous risquez de vous retrouver à essayer d'ajouter trop de fonctionnalités et de voir des calculatrices dans vos rêves. Bien sûr, vous pouvez continuer à ajouter des fonctionnalités si vous le souhaitez. Mais assurez-vous d'avoir un objectif final à atteindre.

Dans le monde réel - selon votre rôle - il peut y avoir un client ou un propriétaire de produit qui définit la partie "qu'est-ce qu'elle fait" pour vous. Votre travail en tant que développeur sera de décomposer ces exigences en tâches plus détaillées, ce que nous aborderons plus tard.

## "À quoi ressemble-t-elle ?"

Maintenant que j'ai une idée des fonctionnalités, je vais commencer à réfléchir à son apparence. 

Si vous avez du mal à trouver des designs, il existe plusieurs façons de procéder :

* regarder des exemples d'applications similaires
* parcourir des frameworks CSS pour des éléments que vous pouvez utiliser
* ou utiliser votre imagination. (Tous les projets personnels que vous faites n'ont pas besoin de paraître "incroyables".)

Je me sens particulièrement artistique aujourd'hui, alors je vais faire un rapide wireframe de ce à quoi je veux que ma calculatrice ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-17-at-20.39.55.png)

Ah ! Magnifique ! Je devrais devenir artiste. 

J'ai donc mes fonctionnalités et mon croquis dont Van Gogh lui-même serait fier.

Dans le monde réel, lorsque vous travaillez au sein d'une équipe, un designer peut créer quelque chose comme cela pour vous. Ou, encore mieux, on peut vous donner un prototype fonctionnel avec lequel vous pouvez jouer.

## "Comment positionner et styliser les éléments ?"

Je commence à avoir une bonne idée de ce que mon application devrait faire et de son apparence. Il est maintenant temps de devenir un peu plus technique.

À ce stade, je me dis : "D'accord, j'ai quelques boutons et un grand affichage. Comment vais-je positionner tout cela ?"

J'aime penser que la mise en œuvre d'un design est un peu comme la construction d'une maison. Posez les fondations (**la mise en page**), construisez la structure extérieure (**boutons, entrées**), et ajoutez les touches finales plus tard (**couleurs, icônes, styles**). 

En parlant de mise en page, les premières choses qui me viennent à l'esprit sont **CSS Grid, Flexbox**, ou un framework (comme **Bootstrap**). Je vais utiliser Flexbox, car il est réactif, rend super facile l'arrangement des éléments dans une rangée, et bien, parce que j'en ai envie. Cela m'évite d'avoir à installer des dépendances supplémentaires dont nous n'avons pas besoin.

## "Comment se comporte-t-elle ?"

Il est maintenant temps de réfléchir à la manière dont l'application se comportera. Cela revient essentiellement à décomposer nos fonctionnalités en plus de détails pour aider à **concevoir le code**. 

Lorsque je me pose cette question, je pense à des choses comme :

* À quoi ressemble l'application lorsqu'elle se charge ?
* Que se passe-t-il lorsque l'utilisateur clique sur un bouton ? Le style change-t-il ? 
* Comment l'interface utilisateur réagit-elle aux différentes actions de l'utilisateur ?

Une autre façon de répondre à cette question est de jouer avec un exemple existant. 

Une petite tâche pour vous : essayez d'ouvrir la calculatrice sur votre ordinateur et commencez à faire quelques opérations. Addition, multiplication, peu importe. 

Lorsque vous effectuez une action, essayez de **capturer autant de détails que possible** sur ce qui se passe.

Voici ce que j'ai trouvé :

* Lorsque l'application se charge, l'affichage est défini sur "0" et tous les boutons sont dans un état "inactif"
* Lorsque l'utilisateur clique sur un nombre, l'affichage se met à jour avec la nouvelle valeur. Le bouton cliqué changera de style pour indiquer à l'utilisateur que le clic a réussi.
* Lorsque l'utilisateur clique sur un opérateur, l'opérateur sélectionné indiquera d'une certaine manière qu'il a été sélectionné.
* Si un bouton opérateur a été cliqué et que l'utilisateur clique ensuite sur un bouton nombre, l'affichage se réinitialisera d'abord à zéro avant d'afficher les prochains nombres que l'utilisateur clique.
* Lorsque le bouton égal est cliqué, un calcul est effectué en utilisant le nombre initial, l'opérateur sélectionné et le nombre suivant qui a été entré.
* Lorsque l'utilisateur clique sur le bouton de réinitialisation, l'affichage se réinitialise à zéro et l'application se réinitialise.

Dans le monde réel, nous n'aurons pas toujours le luxe d'avoir un exemple ou un prototype avec lequel jouer. Mais à mesure que votre expérience grandit, il devient plus facile de le faire sur la base d'un wireframe ou d'une maquette. C'est pourquoi je suggère aux débutants de **répliquer des applications existantes**, car cela vous donne un exemple pour pratiquer cette pensée critique et cette analyse.

Mais pourquoi devons-nous entrer dans des détails aussi minutieux ? Bonne question. Et la réponse est que les ordinateurs sont incroyablement intelligents, mais aussi incroyablement stupides. (Vous ne me croyez pas ? Essayez de supprimer une accolade aléatoire de votre code et regardez tout s'effondrer.)

Les instructions que nous donnons aux ordinateurs doivent être **extrêmement spécifiques**. Par exemple, en revenant à nos comportements ci-dessus, cliquer sur un nombre agira différemment selon qu'un opérateur a été cliqué ou non. 

Nous, en tant qu'humains, savons comment fonctionne une calculatrice, mais un ordinateur ne le sait pas jusqu'à ce que nous le lui disions.

## "À quoi ressemblera mon code ?" 

Tout comme j'ai passé du temps à concevoir l'interface utilisateur, j'aime faire de même avec le code. Cela présente de nombreux avantages :

* Cela me fait réfléchir en détail aux composants dont j'ai besoin
* Cela me fait réfléchir aux flux de travail
* Cela signifie que l'écriture du code sera plus facile/plus rapide, puisque j'ai un plan 
* Cela permet de détecter les problèmes et les zones à problèmes tôt 

J'ai mentionné précédemment que pour ce projet, je vais essayer de garder les choses simples, donc je vais m'en tenir à cette approche. Au début, je vais tout garder dans un seul composant. Cependant, je vais commencer à refactoriser et à diviser en composants lorsque :

* Le code devient trop difficile à gérer ou à comprendre
* Il y a beaucoup de code dupliqué
* Un seul élément sur la page nécessite ses propres fonctions et état

Avez-vous déjà été vers la fin d'un projet et pensé "mince ! J'ai oublié quelque chose, maintenant je dois tout redessiner ?" En planifiant à l'avance, vous éviterez ce piège. Avec cela à l'esprit, voici les éléments dont je pense avoir besoin. Ne passez pas toute la journée à y réfléchir, trouvez un équilibre entre la planification et le fait de simplement commencer. Décomposons notre maquette d'interface utilisateur en ses parties individuelles et réfléchissons au code nécessaire.

### L'affichage

Mon affichage montre à l'utilisateur le nombre actuel, donc je vais avoir besoin d'une sorte de **valeur d'état** pour cela. Rien ne se passe lorsque je clique dessus, donc je n'ai besoin de rien là.

### Les boutons numériques

Puisque les boutons numériques affectent le nombre affiché dans l'affichage, je vais avoir besoin d'une **fonction** qui est appelée par un événement **onClick** pour gérer cela. Pas besoin de stocker le nombre sélectionné dans l'état pour l'instant.

### Les boutons opérateurs

Le bouton opérateur est intéressant - car différentes choses se passent (vous vous souvenez de nos notes "comment se comporte-t-elle ?" ci-dessus ?). Puisque _je dois savoir quel opérateur est actuellement sélectionné_, je vais stocker cela comme une **valeur d'état** également.

### Le bouton égal

Le bouton égal doit prendre la valeur de l'affichage, l'opérateur, la valeur précédemment entrée et calculer le résultat. Facile !

Pas tout à fait, nous avons rencontré notre premier problème ! Reprenons nos comportements

> Si un bouton opérateur a été cliqué et que l'utilisateur clique ensuite sur un bouton nombre, l'affichage se réinitialisera d'abord avant d'afficher les nombres que l'utilisateur a cliqués

Le premier nombre que l'utilisateur entre dans l'affichage est **réinitialisé** lorsqu'il clique sur un opérateur et commence à entrer le nombre suivant - ce qui signifie que notre application ne sait pas quel était le premier nombre lorsque l'utilisateur clique sur égal (je vous avais dit que les ordinateurs étaient stupides) ! Réfléchissons à cela :

Lorsque le bouton opérateur est cliqué, c'est à ce moment que l'affichage se réinitialise et se met à jour avec le nombre suivant que l'utilisateur entre. Logiquement alors, _il est logique de stocker la valeur précédente de l'affichage lorsqu'un opérateur est cliqué._ Pour que cela fonctionne, j'aurai besoin d'une **fonction** et d'une **valeur d'état** qui stocke la valeur de l'affichage lorsqu'un opérateur est cliqué.

### Le bouton de réinitialisation

Celui-ci est facile - réinitialiser nos **valeurs d'état à zéro**, permettant à l'utilisateur de recommencer. J'aurai besoin d'une simple **fonction onClick** attachée au bouton pour gérer cela.

## "Qu'est-ce que je dois tester ? Et qu'est-ce qui peut mal tourner ?"

Selon à qui vous parlez, il peut y avoir différentes façons d'aborder les tests. Certains aiment faire du TDD (qui consiste à écrire les tests en premier) et d'autres les écrivent à la fin. Je fais les deux selon le projet. **Mais l'important est de les écrire à un moment donné.** 

Lorsque je pense à mes tests, je regarde les exigences. La première exigence (ou fonctionnalité) est :

* Additionner, soustraire, diviser et multiplier des nombres

Je devrais donc tester que l'application peut faire ces choses. Je ne vais pas entrer dans les détails sur la façon d'écrire des tests, mais une bonne suite de tests devrait couvrir :

* Les exigences et les cas d'utilisation courants
* Les cas limites (par exemple, l'utilisateur entre 99999999999999999999 + 9999999999999999999999) 
* Les cas d'erreur et les points de rupture (par exemple, l'utilisateur essaie de diviser par zéro)

"Combien de tests dois-je écrire ?" est probablement votre prochaine question. Malheureusement, il n'y a pas de nombre fixe pour cela. Il existe une infinité d'entrées possibles. Si vous suivez les points ci-dessus, vous aurez une suite de tests solide pour tout projet.

Penser à vos tests tôt vous aidera à réfléchir aux endroits où des erreurs peuvent survenir dans votre code et vous permettra de les anticiper plus tôt dans vos conceptions.

## Regardons le code

Ce n'est pas un tutoriel de codage à proprement parler, donc je ne vais pas entrer dans les détails de chaque étape dans cet article. **Voir le code sandbox à la fin pour voir un exemple fonctionnel, incluant le code/guide pas à pas pour chaque étape décrite ci-dessous.** N'hésitez pas à forker le code et à jouer, détruire et expérimenter à votre guise ! 

Lors de l'écriture de code, nous allons nous en tenir au plan :

* Concentrez-vous d'abord sur la mise en place de la mise en page de l'interface utilisateur et des éléments, en utilisant notre wireframe comme référence
* Implémentez la logique (JS, gestionnaires d'événements, etc.) 
* Touches finales  
* N'oubliez pas de faire la chose la plus simple pour que tout fonctionne - pas besoin de vous soucier de la refactorisation et des performances au début !

### Étape 1 - Mise en page et éléments de base de l'interface utilisateur

(Dans le Code Sandbox lié ci-dessous, cliquez sur le bouton `Étape 1` pour voir l'exemple fonctionnel, voir `app-etape-1.js` pour consulter le code !)

Rappelez-vous, nous allons commencer par la mise en page et rassembler la "structure" de notre application. Cela inclura l'ajout du HTML et l'utilisation de Flexbox pour positionner notre affichage et nos boutons. Ils ne feront rien pour l'instant, mais ils auront une belle apparence. En quelque sorte.

### Étape 2 - Ajout de la logique

(Dans le Code Sandbox lié ci-dessous, cliquez sur le bouton `Étape 2` pour voir l'exemple fonctionnel, voir `app-etape-2.js` pour consulter le code !)

Nous avons fait notre planification pour cette partie, alors faisons référence à cela. Dans nos notes "À quoi ressemblera mon code", nous devons créer un ensemble de différents objets d'état et fonctions pour gérer les événements. 

Pour cela, je prends un élément de notre liste "À quoi ressemblera mon code ?" à la fois et je fais référence à nos notes "Comment se comporte-t-elle ?" pour assembler tout cela. J'implémente la fonctionnalité et je teste qu'elle fonctionne (généralement automatiquement, mais manuellement fera l'affaire). Exemple :

Le premier élément de la liste est l'**affichage**. Je vais donc ajouter les variables d'état et la logique pour cela. Tester que cela fonctionne et passer aux **boutons numériques**, et répéter. C'est là que l'écriture de vos tests tôt est utile - vous pouvez exécuter la suite de temps en temps pour vous assurer que rien n'est cassé.

### Étape 3 - Ajout des clochettes et des sifflets

(Dans le Code Sandbox lié ci-dessous, cliquez sur le bouton `Étape 3` pour voir l'exemple fonctionnel, voir `app-etape-3.js` pour consulter le code !)

Super, nous avons presque terminé ! Maintenant que la logique fonctionne, nous allons ajouter quelques touches finales (boutons arrondis, bordures, affichage plus grand, etc.) à l'application, et c'est terminé ! Notre calculatrice très basique fonctionne maintenant ! 

### Étape 4 - À vous de jouer !

J'ai délibérément laissé de côté certaines choses que vous pouvez essayer si vous en avez envie. Utilisez les approches que nous avons apprises jusqu'à présent - en réfléchissant aux comportements, aux fonctions/objets d'état dont vous aurez besoin, etc.

* Notre calculatrice ne correspond pas _tout à fait_ au wireframe - pouvez-vous ajouter de la couleur aux boutons ? Et changer la couleur d'un bouton sélectionné lorsqu'il est cliqué ?
* Pas de tests ! Oh là là ! Voyez si vous pouvez en ajouter quelques-uns 
* Il existe du code dupliqué - pouvez-vous trouver un moyen de rendre les boutons pour que nous n'ayons pas besoin de coder en dur 16 éléments `button` ?
* Gestion des erreurs - il n'y en a aucune ! Ce n'est pas bon. Que se passe-t-il si vous essayez de diviser par zéro ? Ou si vous avez un nombre plus large que l'affichage ?
* Lorsque l'utilisateur commence à entrer des nombres, tous les zéros précédents sont ajoutés à l'affichage, par exemple `000003`, ce n'est pas une bonne UX, pouvez-vous le corriger ?

---

### Merci d'avoir lu ! Vous voulez plus d'articles comme celui-ci ?

Espérons que cela vous a donné un aperçu d'une approche de codage des applications. Si vous souhaitez être informé lorsque je publierai d'autres articles comme celui-ci, n'hésitez pas à rejoindre la liste de diffusion sur [chrisblakely.dev](https://www.chrisblakely.dev#sign-up) ! Ou contactez-moi sur [Twitter](https://twitter.com/chrisblakely01) si vous avez envie de discuter :)

---

## CodeSandbox - Exemple terminé



%[https://codesandbox.io/s/code-thought-process-2imft]