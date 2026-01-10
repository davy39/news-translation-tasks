---
title: Le Manuel de Bootstrap — Tout ce que vous devez savoir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-23T03:44:33.000Z'
originalURL: https://freecodecamp.org/news/bootstrap-4-everything-you-need-to-know-c750991f6784
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XJhVE27AcycpeaWMhoqZ9w.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: technology
  slug: technology
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Le Manuel de Bootstrap — Tout ce que vous devez savoir
seo_desc: 'By Emmanuel Ohans

  A deep dive into solving common responsive web design problem

  This article will cover the practical fundamentals you need to start building responsive
  websites with the latest version of Bootstrap, version 4.

  You may be wondering — ...'
---

Par Emmanuel Ohans

#### Une immersion profonde dans la résolution des problèmes courants de conception web adaptative

Cet article couvrira les bases pratiques dont vous avez besoin pour commencer à créer des sites web adaptatifs (responsive) avec la dernière version de Bootstrap, la version 4.

Vous vous demandez peut-être — pourquoi Ohans a-t-il écrit ce guide de 17 000 mots sur Bootstrap ? Après tout, le support des navigateurs pour Flexbox et Grid est en hausse.

Eh bien, j'ai de bonnes nouvelles pour vous — je suis bien conscient de ces tendances. J'ai écrit [une introduction complète à Flexbox](https://medium.freecodecamp.org/understanding-flexbox-everything-you-need-to-know-b4013d4dc9af) il y a quelque temps, et j'ai écrit [plus d'articles sur Medium sur Flexbox et Grid](https://medium.com/flexbox-and-grids) que n'importe quel autre développeur.

Cela dit, je pense qu'il existe encore de nombreuses situations où la connaissance de la dernière version de Bootstrap vous aidera.

Il n'y a pas un seul outil pour chaque cas d'utilisation.

Au fait, si vous ne connaissez pas bien le CSS, je vous recommande de l'apprendre sérieusement d'abord. Au lieu de cela, obtenez une véritable [éducation CSS](http://bit.ly/learn_css). Comprenez [Flexbox](https://medium.freecodecamp.org/understanding-flexbox-everything-you-need-to-know-b4013d4dc9af), et apprenez peut-être aussi comment fonctionne la mise en page [CSS Grid](https://medium.com/flexbox-and-grids/how-to-efficiently-master-the-css-grid-in-a-jiffy-585d0c213577). Ensuite, attaquez-vous à Bootstrap 4.

Mais si vous vous sentez prêt, procédons. ?

### Une note rapide sur Bootstrap 4

Bootstrap 4 est la dernière version du framework front-end très populaire, [Bootstrap](http://getbootstrap.com).

Bootstrap 4 possède de nombreuses nouvelles fonctionnalités et capacités passionnantes qui rendent la création de designs adaptatifs encore plus facile qu'auparavant. Le plus gros ajout est qu'il est fortement construit sur Flexbox.

### Dois-je encore apprendre Bootstrap en 2019 ?

Il y a des années, la principale raison pour laquelle j'ai appris Bootstrap était la facilité de créer des designs adaptatifs. Cependant, avant la sortie de la nouvelle version de Bootstrap, j'ai arrêté d'utiliser le Framework. Pourquoi ?

Avec l'avènement de Flexbox et CSS Grid, j'ai trouvé plus facile de construire des modules adaptatifs en utilisant le support CSS natif.

Parmi les développeurs expérimentés, je suppose que Bootstrap est moins populaire. C'est une opinion personnelle, pas un fait vérifié. Mais, que vous soyez un vieux de la vieille ou un nouveau dans le monde du design adaptatif, il y a toujours de bonnes raisons d'apprendre Bootstrap :

#### 1. Prototypage rapide

Il existe de nombreux autres outils et frameworks qui permettent un prototypage rapide. Par exemple, vous avez peut-être entendu parler de [Bulma](https://bulma.io/) et [Materialize](http://materializecss.com/).

Bootstrap est un concurrent de taille ici. Beaucoup soutiendraient qu'ils n'ont pas besoin de certaines des autres fonctionnalités du framework. Pourtant, Bootstrap vous permet de personnaliser et de choisir les modules qui vous concernent.

#### 2. Conception Web Adaptative (Responsive Web Design)

Pour les débutants, le design web adaptatif est un enjeu majeur. Il est facile d'en rire quand on est un développeur expérimenté, mais repensez à vos débuts. C'était sacrément difficile à réaliser. Bootstrap rend cela relativement facile.

#### 3. Ancienne base de code (Codebase)

Quand j'ai arrêté d'utiliser Bootstrap pour mes projets personnels et nouveaux, je devais encore refactoriser et maintenir une ancienne base de code au travail. Que vous le vouliez ou non, beaucoup d'anciennes bases de code sont écrites avec Bootstrap. Vous ne voulez pas avoir l'air perdu juste parce que vous êtes « pro » et que vous n'aimez pas Bootstrap.

#### 4. La dernière version est plus intelligente et meilleure

La nouvelle version 4 de Bootstrap est beaucoup plus intelligente. Elle est construite sur Flexbox et est livrée avec beaucoup de saveurs que nous explorerons dans les sections suivantes de cet article.

#### 5. Plus grande facilité de personnalisation

Le nouveau Bootstrap 4 est beaucoup plus facile à personnaliser.

Je détestais Bootstrap parce qu'il fallait utiliser Less ou Sass pour toute personnalisation significative. Bien que cela reste en partie vrai, la version 4 est beaucoup plus personnalisable que les versions précédentes.

Bootstrap ne va pas disparaître de sitôt. Vous pouvez en savoir plus sur l'opportunité de l'apprendre ou non dans cette [discussion de forum](https://forum.freecodecamp.org/t/will-bootstrap-be-dropped/73378/21) freeCodeCamp :

[**Bootstrap sera-t-il abandonné ?**](https://forum.freecodecamp.org/t/will-bootstrap-be-dropped/73378/21)  
[_"Chaque site web bootstrap de l'histoire !" - c'est encore plus FACILE que ça, pourquoi apprendre le front-end/gui du tout ? Tapez simplement Monster..._forum.freecodecamp.org](https://forum.freecodecamp.org/t/will-bootstrap-be-dropped/73378/21)

### Ce que vous allez apprendre

1. Je vais vous enseigner les fondamentaux du fonctionnement de Bootstrap.
2. Je vous guiderai à travers ce qui est différent dans cette nouvelle version de Bootstrap. Si vous êtes un développeur plus expérimenté, cette section vous intéressera.
3. J'ai passé de nombreuses heures à étudier le Framework Bootstrap. Je vais vous montrer quelques-uns des conseils utiles que j'ai trouvés en chemin. Cela facilitera votre travail avec le framework.
4. Apprendre les fondamentaux, c'est cool. Ce qui est encore plus cool, c'est d'appliquer ces fondamentaux pour construire des applications réelles.
5. Je vous guiderai dans la construction de beaucoup de « petites choses ». Ensuite, je terminerai par cette [page d'accueil de startup](https://codepen.io/ohansemmanuel/full/zEKrxP/) entièrement construite avec Bootstrap 4.

![Image](https://cdn-media-1.freecodecamp.org/images/lTbErHVtsOVqOyWeG8kycn3RHrBIPwSjB8cA)

![Image](https://cdn-media-1.freecodecamp.org/images/HChwKqzlRXQOO48hgg-aBlNJrMe-EE4vXZeH)

![Image](https://cdn-media-1.freecodecamp.org/images/ZSc5KmKERgLGTh6qWTUimdIUvjMNi1gXxHfy)

![Image](https://cdn-media-1.freecodecamp.org/images/O1Wxnybkc7bpuixPSRlCMBrH7Gcz8juqOhtj)
_Quelques écrans de la [démo](https://codepen.io/ohansemmanuel/full/zEKrxP/" rel="noopener" target="_blank" title=") que nous allons construire._

Ne sont-ils pas jolis ?

La plupart des gens disent : « tous les sites Bootstrap se ressemblent ». Je ne suis pas d'accord. La phrase devrait être : « tous les sites Bootstrap **mal conçus** se ressemblent ».

Je suis ravi de vous montrer comment construire de beaux sites en utilisant Bootstrap. J'espère que vous l'êtes aussi.

![Image](https://cdn-media-1.freecodecamp.org/images/cz99qCqD-sSaMyAP9EW1CTncBBnwi5dagikk)
_Excité !!!!! Gif par [Tony Babel](https://dribbble.com/TonyBabel" rel="noopener" target="_blank" title=")_

### Ce que vous devriez savoir

* Je suppose que vous avez une bonne compréhension du fonctionnement de `HTML` et `CSS`. Si vous ne connaissez pas très bien le CSS, je vous recommande de suivre mon cours [Introduction complète au CSS](https://bit.ly/learn_css) (cours payant avec plus de 70 leçons).
* Vous devriez avoir une connaissance décente du fonctionnement de Flexbox. Veuillez lire ce [guide détaillé sur Flexbox](https://medium.freecodecamp.org/understanding-flexbox-everything-you-need-to-know-b4013d4dc9af), ou ce [guide axé sur les exemples](https://medium.freecodecamp.org/the-ultimate-guide-to-flexbox-learning-through-examples-8c90248d4676) pour un rappel sur Flexbox.

### **_Quoi de neuf dans la version 4 de Bootstrap ?_**

Cette section s'adresse aux développeurs plus expérimentés. Si vous êtes nouveau dans le domaine du front-end, ignorez ceci et revenez-y après avoir lu les autres sections de l'article.

La dernière version de Bootstrap, la version 4, regorge de quelques changements vitaux.

#### 1. La valeur par défaut de border-box a été modifiée

Les versions précédentes du framework Bootstrap réglaient la valeur `border-box` sur `content-box`. La plupart des gens, comme moi, trouvaient cela ennuyeux la plupart du temps.

Maintenant, l'équipe Bootstrap a basculé la valeur sur `border-box`. Je trouve cela plus facile à comprendre.

#### 2. Resets CSS opinionnés

Les [Resets CSS](https://meyerweb.com/eric/tools/css/reset/) ont parcouru un long chemin. Dans cette version de Bootstrap, la feuille de style de Reset CSS s'appelle Reboot.

Reboot fait quelques choses différemment. Il est basé sur Normalize. Il évite `margin-top`, adopte la valeur CSS `inherit`, utilise massivement l'unité `rem`, et adopte l'utilisation de la pile de polices natives pour un rendu de texte optimal.

Je vous conseille de prendre 10 minutes pour lire sur Reboot dans la [documentation officielle](https://getbootstrap.com/docs/4.0/content/reboot/). C'est une lecture assez intéressante.

![Image](https://cdn-media-1.freecodecamp.org/images/vR-qsq519vhC0WD4T4hGCRtLicy2KF9IuJKP)

### Introduction au fonctionnement de Bootstrap

Cette section est destinée à ceux qui ne sont pas familiers avec le fonctionnement de Bootstrap. Vous pouvez l'ignorer si vous êtes un développeur plus expérimenté.

Commençons.

Le flux habituel pour créer une page web basique ressemble à ceci :

1. Écrire un document de balisage de base (HTML)
2. Styler la page en utilisant CSS

Prétendons un instant que nous faisons exactement cela.

Considérez le balisage de base ci-dessous :

```
<h1>Hello World</h1><h2>Salut. Bonjour encore</h2><a href="example.com">Lien vers mon site web</a>
```

Le balisage possède deux éléments d'en-tête et une balise d'ancrage. Voici le résultat affiché dans un navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/-qAKb3JJXYvqSXnacRVp1hFAgUG2yHNPtmCk)
_Le résultat du balisage de base_

C'est exactement ce que vous auriez pu espérer, mais le résultat montre une vérité fondamentale. Voyons pourquoi c'est important.

Regardez le résultat ci-dessus. L'élément `h1` est affiché plus grand que l'élément `h2`, et la balise `a` est bleue — par défaut.

Avez-vous remarqué que nous obtenons ces styles sans écrire de CSS ?

Pourquoi ?

C'est le résultat des styles par défaut du navigateur.

La leçon à retenir est que les navigateurs ont des feuilles de style par défaut qui affectent l'apparence des pages web.

Comment pouvons-nous empêcher ce comportement par défaut ?

La solution est assez simple. Vous pouvez écraser les styles par défaut du navigateur avec vos propres styles via CSS.

Par exemple :

```
h1 {  color: blue}
```

```
a {  color: black}
```

Cette fois, j'ai inversé les couleurs. Le lien est `black` (noir) et le `h1` est bleu.

![Image](https://cdn-media-1.freecodecamp.org/images/LPNwPJyHfOnoyQe0ToQgKrmulcZNOWjDSFam)
_Les styles par défaut du navigateur ont maintenant été écrasés. Le lien apparaît maintenant en `black` et le h1 est bleu._

C'était facile.

### Où Bootstrap s'insère-t-il dans tout cela ?

Le navigateur a affecté l'affichage de la page sans votre intervention. L'utilisation de frameworks comme Bootstrap peut modifier considérablement l'affichage de vos pages web — avec peu ou pas d'intervention de votre part.

Ainsi, cela fonctionne comme ceci :

Le style général de chaque page web est influencé par les styles par défaut du navigateur, les styles de frameworks tels que Bootstrap et votre propre CSS écrit.

![Image](https://cdn-media-1.freecodecamp.org/images/mBMF65xuVfhEFgvw9ofwRWunNxFe1QAEX8Qt)
_Un coup d'œil rapide aux styles qui influencent l'apparence de chaque page web._

Ne vous inquiétez pas si vous ne comprenez pas tout de suite, je vais vous expliquer avec un exemple.

Supposons que j'ai écrit une bibliothèque CSS appelée `**cowbell**`. `**Cowbell**` ne fait qu'une seule chose. J'ai inclus la bibliothèque, peut-être via un lien CDN. Elle a donné à ma page une couleur d'arrière-plan qui ressemble à une « cloche de vache » (cowbell).

Quelque part dans la bibliothèque `**cowbell**`, j'aurais écrit ceci :

```
.cowbell {   background-color: cowbell}
```

Notez que tout ce que j'ai fait est d'inclure une classe `.cowbell` avec une `background-color` équivalente.

Pour information, il n'existe pas de couleur appelée « cowbell ».

Lorsque vous incluez la bibliothèque cowbell dans votre page, comment l'utilisez-vous ?

Simple.

Vous ajoutez simplement la classe `.cowbell` à n'importe quel élément auquel vous voulez donner une couleur `cowbell`.

Quelque chose comme ça :

```
<!--- ceci est mon superbe document HTML --><body class="cowbell">  Ceci est mon superbe site</body>
```

Puisque j'ai déjà défini la classe `cowbell` dans la bibliothèque, vous n'avez pas à vous soucier de l'écriture de la fonctionnalité.

Comme dans l'exemple ci-dessus, l'ajout de la classe `cowbell` au `body` donnera à l'ensemble du document une couleur **cowbell**.

Maintenant, vous avez utilisé une bibliothèque CSS !

Sous le capot, c'est de la même manière que Bootstrap fonctionne. De la même manière, il existe un ensemble de classes CSS Bootstrap qui ont été stylisées au sein de la bibliothèque.

Tout ce que vous avez à faire est d'apprendre les noms des classes et de les appliquer à votre balisage `html`. Elles feront ce pour quoi elles ont été conçues.

Dans le cas de la bibliothèque `**cowbell**`, le nom de la classe requis est `.cowbell`.

Que fait-elle ? Elle donne à l'élément une couleur « cowbell ».

Comment ça marche ? Vous allez simplement ajouter le nom de la classe, `.cowbell`, à n'importe quel élément.

De même, la bibliothèque Bootstrap possède un fichier CSS géant avec de nombreuses classes utilitaires, des modules adaptatifs et des joyaux CSS généraux.

Commençons à décortiquer les couches de Bootstrap dans la section suivante.

### Installer Bootstrap

Vous ne pouvez pas faire faire quoi que ce soit à Bootstrap s'il n'est pas installé ou inclus dans votre page web.

Il existe plusieurs façons de le faire et les utilisateurs plus avancés peuvent explorer les [options disponibles](https://v4-alpha.getbootstrap.com/getting-started/download/#package-managers).

Par souci de simplicité, j'utiliserai un `cdn`.

Désolé pour le jargon. Un CDN est l'abréviation de Content Delivery Network (Réseau de diffusion de contenu).

Une façon simple de décrire ce qu'est un CDN est d'imaginer que vous commandez un short sur un site web fictif appelé Anazon. Votre commande a été reçue et traitée avec succès par Anazon. Malheureusement, Anazon remarque que vous vivez en Antarctique — un endroit vraiment éloigné de leur entrepôt principal.

Mauvaise nouvelle.

Heureusement, Anazon dispose d'un large réseau d'entrepôts distribués dans le monde entier. Incroyable.

Maintenant, Anazon décide quel entrepôt est le plus proche de votre maison en Antarctique, et livre votre short depuis cet entrepôt. De plus, la prochaine fois que vous passerez une commande, Anazon vérifiera le même entrepôt et livrera vos marchandises en moins de 24 heures.

Comme c'est agréable.

C'est un peu comme cela qu'un réseau de diffusion de contenu fonctionne. Un CDN est comme un entrepôt qui héberge des bibliothèques courantes comme Bootstrap.

Si vous visitez un site web qui possède un lien vers une ressource CDN, le navigateur chargera une version en cache de la bibliothèque. C'est une version « stockée » dans la mémoire de votre navigateur. S'il n'en trouve aucune, il fera une requête pour récupérer la ressource demandée.

Charger une ressource à partir d'un CDN présente l'avantage de recevoir la ressource plus rapidement. Comme ce short !

Voici le lien vers le CDN de Bootstrap.

```
https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous"
```

Incluez cela dans votre page, et vous êtes prêt à partir.

Par exemple, ajoutez ceci à n'importe quel balisage HTML :

```
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
```

### Quelle différence Bootstrap fait-il ?

Dans cette section, nous allons mettre en place une page de démonstration de base avec Bootstrap. Pour ces démos, j'utiliserai [codepen.io](http://www.codepen.io).

Ajouter Bootstrap v4 à un projet est simple. Cliquez sur le paramètre CSS du pen, et incluez Bootstrap à partir des options.

![Image](https://cdn-media-1.freecodecamp.org/images/8Xak2MK5OPNCAEokXoqlg6nAuO7RGjAGKnlS)

Une fois cela fait, nous sommes tous prêts pour les démos qui arrivent dans les sections suivantes.

Alors, quelle différence Bootstrap fait-il ?

![Image](https://cdn-media-1.freecodecamp.org/images/EqC1JaOi4QqbXPfiIP6R8vk1zt6spw2Xl8MZ)

![Image](https://cdn-media-1.freecodecamp.org/images/PXJ6CsFKeLIInx4H5rIhkR72l8wA-3Kn9zuS)
_Les images montrent les résultats sans Bootstrap (à gauche), et avec Bootstrap (à droite)_

J'ai continué avec l'exemple « Hello World » dont nous avons parlé plus tôt. Regardez les résultats ci-dessus.

La différence est très subtile. À partir des images, vous pouvez voir que certains des styles de page par défaut de Bootstrap ont écrasé ceux du navigateur.

La police est maintenant différente, l'espacement entre chaque bloc de texte est modifié, et le lien a un style différent.

Bootstrap à l'œuvre !

Maintenant que je suis sûr que vous comprenez comment les bibliothèques CSS fonctionnent en général, apprenons quelques-uns des styles de base de Bootstrap ou des noms de classes que vous devriez connaître.

![Image](https://cdn-media-1.freecodecamp.org/images/5oh-0ra19Xn73R6fjvwIIGBrln14wg7TALcD)

### Les styles de base de Bootstrap que tout le monde devrait connaître

Des personnes très intelligentes ont fourni beaucoup de travail pour construire la bibliothèque Bootstrap. Ils ont fait une grande partie du travail « ingrat » pour vous. Tout ce que vous avez à faire est de vous brancher sur ce qu'ils ont fait et d'en récolter les fruits !

J'utiliserai une méthode de questions-réponses pour expliquer l'utilisation de ces styles Bootstrap.

Commençons.

Pour pratiquer les concepts de cette section, nous commencerons par le balisage suivant. C'est un poème peu intelligent sur les lapins.

```
<h1> Poèmes de lapins </h1><p> Ce qui suit est un poème pour la plupart inintelligent sur les lapins. Ne réfléchissez pas trop à leur sujet. <br /> Profitez-en !</p>
```

```
<h2> Le lapin qui n'avait pas d'oreilles </h2>
```

```
<p> M. Lapin. Quelle taille avaient les oreilles de vos ancêtres </p><p> Quelle fierté duveteuse pour votre famille </p><p> Mais, attendez... </p><p> Comment se fait-il que vous n'ayez pas d'oreilles </p><p> Avec vos yeux vous entendez, et avec votre nez vous voyez ? </p><p> Comme c'est triste, M. Lapin </p><p> Voyez-le sauter, sauter, sauter sur des pattes si fortes.</p><p> Mais des oreilles, il n'en a aucune <p><p> Vivez longtemps, et rendez vos ancêtres fiers </p>
```

Le résultat du balisage est visible ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Bhu58m-X521YhNrkcSkUfzb6ff-iNv36-Ow3)
_Le résultat initial avant l'inclusion de Bootstrap._

Le résultat est largement influencé par le style du navigateur. C'est ce qu'on appelle la feuille de style de l'agent utilisateur (user agent stylesheet).

La première étape consiste à inclure Bootstrap. Veuillez inclure Bootstrap comme discuté dans une section précédente, et vous devriez avoir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/4igS5eSWHGSIBw6HJrykrBBHtTWbvBCwRdjN)
_Le résultat après l'ajout de Bootstrap._

Sans aucun style écrit pour l'instant, nous avons une page d'apparence décente. Elle est bien espacée et la famille de polices a changé. Vous voyez les changements ?

Les styles par défaut de Bootstrap ont écrasé ceux du navigateur. Sans aucun effort, nous avons une page d'apparence correcte.

#### Pourquoi la famille de polices a-t-elle changé quand j'ai ajouté Bootstrap ?

Vous avez peut-être remarqué que le texte est maintenant affiché dans une police complètement différente.

Bootstrap 4 adopte l'idée des piles de polices natives (native font stacks). C'est assez simple. Différents systèmes d'exploitation — y compris Android, MacOS, Windows et Linux — ont tous des polices par défaut installées.

Cette version de Bootstrap met en place une pile de polices qui utilise la police sans-serif par défaut disponible sur l'appareil actuel.

![Image](https://cdn-media-1.freecodecamp.org/images/lebjxaSP54ENAd2d6mOskNAAxop8oUM2o5Rh)
_illustration de la pile de polices tirée de [complete practical introduction to css](http://bit.ly/learn_css" rel="noopener" target="_blank" title=")_

C'est une chose beaucoup plus intelligente à faire, sans pour autant enlever la flexibilité du changement. Vous pouvez écraser ce comportement et utiliser vos propres polices.

Je prévoyais d'expliquer en détail comment fonctionne la configuration des piles de polices natives en CSS, mais [Marcin Wichary](https://www.freecodecamp.org/news/bootstrap-4-everything-you-need-to-know-c750991f6784/undefined) m'a devancé. Dans cet [article](https://www.smashingmagazine.com/2015/11/using-system-ui-fonts-practical-guide/), il a fait un excellent travail en l'expliquant mieux que je ne pourrais jamais le faire.

Ainsi, en ajoutant Bootstrap, nous avons de belles polices sur toutes les plateformes — quel que soit le système d'exploitation de l'appareil.

#### Comment créer des en-têtes plus grands que ceux par défaut ?

Parfois, vous avez besoin d'en-têtes vraiment grands. Par exemple, en haut d'un site web.

Regardez l'exemple de base que nous avons mis en place plus tôt. Il existe un `h1` et un `h2` dans leurs tailles par défaut. Si pour une raison quelconque vous avez besoin que ces en-têtes soient plus grands, Bootstrap 4 a ce qu'il vous faut.

Ajoutez n'importe laquelle des classes `display-1`, `display-2`, `display-3` ou `display-4`.

Par exemple :

```
<h2 class="display-4"> Le lapin qui n'avait pas d'oreilles </h2>
```

J'ai ajouté la classe `display-4` à l'élément `h2`. Comme on le voit ci-dessous, il a l'air beaucoup plus grand maintenant. Plus grand que l'élément `h1` !

![Image](https://cdn-media-1.freecodecamp.org/images/8H3oKKH4SwfBMzLXXTlfoTltiDsjdenLtSsr)
_« Le lapin qui n'avait pas d'oreilles » apparaît plus grand que l'élément h1. Merci au nom de classe « display-4 »._

#### Les classes de taille d'affichage de texte sont-elles limitées aux seuls éléments d'en-tête ?

Les classes d'affichage ne sont pas limitées aux seuls éléments d'en-tête, de `h1` à `h6`. En fait, elles peuvent être ajoutées à n'importe quel élément.

Dans l'exemple ci-dessous, j'ai ajouté `display-3` à l'un des éléments de paragraphe.

```
<p class="display-2"> Mais, attendez... </p>
```

![Image](https://cdn-media-1.freecodecamp.org/images/xTVTCy30eOdCj1gJFX4rCv-lFFP7nonoyOxr)
_Les classes d'affichage peuvent être utilisées sur n'importe quel élément de texte — pas seulement les éléments d'en-tête (h1 — h6)_

#### Quelle est la différence entre les noms de classes `display-1` et `display-4` ?

La différence vient de la taille résultante des éléments. `display-1` produira des tailles plus grandes que `display-4`. Vous pouvez voir la différence de tailles dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/s1xywMJHNJmilrdmnJTPPfzY3TH2mFYSLQy9)
_Lequel produit les textes les plus grands ? « display-1 » ou « display-4 » ?_

#### Comment centrer et justifier du texte avec Bootstrap ?

C'est assez simple. Ajoutez la classe `text-center` à l'élément souhaité pour centrer le bloc de texte.

```
<p class="text-center">Comment se fait-il que vous n'ayez pas d'oreilles </p>
```

![Image](https://cdn-media-1.freecodecamp.org/images/FG3XhkBXRJoFdNQmu0EecoYdtcRFbgFY8Akk)

Pour justifier le texte, et styliser le texte pour qu'il s'adapte à gauche et à droite, utilisez la classe `text-justify` comme ceci :

```
<p class="text-justify">Comment se fait-il que vous n'ayez pas d'oreilles </p>
```

#### Comment mettre les textes en majuscules dans Bootstrap 4 ?

Il existe trois classes spécifiquement conçues pour cela : `.text-lowercase`, `.text-uppercase` et `.text-capitalize`.

Si vous appliquez la classe `text-lowercase` sur un texte déjà en majuscules, il apparaîtra en minuscules.

```
<p class="text-lowercase">NOUS CROYONS EN TOI LAPIN</p>
```

Cela produira un texte en minuscules malgré le texte _« NOUS CROYONS EN TOI LAPIN »_ écrit en majuscules.

![Image](https://cdn-media-1.freecodecamp.org/images/1naiXm7QpHHULmPpX72mXdwGlxfB2fxEsh5Q)
_« nous croyons en toi lapin » apparaît en minuscules bien qu'il soit écrit en majuscules dans le HTML_

`text-capitalize` mettra en majuscule la première lettre de chaque mot, et `text-uppercase` mettra chaque lettre d'un mot en majuscule.

#### Comment déplacer des textes vers la gauche ou la droite ?

Comme pour les autres classes utilitaires de texte, ajoutez l'une des classes `text-left` et `text-right` pour l'effet désiré.

#### Comment mettre un texte en gras, normal ou italique avec Bootstrap 4 ?

L'ajout des classes `.font-weight-bold`, `.font-weight-normal` et `.font-italic` rendra le texte gras, normal ou italique. Si vous venez de Bootstrap 3, vous remarquerez que ces noms de classes sont différents.

Voici un exemple :

```
<p class="font-weight-bold"> Comme c'est triste, M. Lapin </p><p class="font-italic">Voyez-le sauter, sauter, sauter sur des pattes si fortes.</p><strong class="font-weight-normal"> Mais des oreilles, il n'en a aucune </strong>
```

![Image](https://cdn-media-1.freecodecamp.org/images/MjAbpDLwMCKWMMk88FSngRv7QWSvlEtHqH39)
_`font-weight-bold`, `font-weight-normal` et `font-italic` en action._

Notez que l'exemple utilise `font-weight-normal` sur une balise `strong`. Par défaut, `<strong></strong>` devrait produire des textes en gras. Ce comportement est « normalisé » lorsque vous ajoutez la classe `font-weight-normal`.

Notez que le nom de la classe pour mettre un texte en italique ne dit PAS `font-weight-italic` MAIS `font-italic`.

#### Comment puis-je styliser des citations (block quotes) avec Bootstrap ?

Bootstrap dispose du nom de classe `blockquote` disponible pour styliser la balise de citation, `<blockquote>` ou tout autre bloc de texte tel que l'élément de paragraphe.

Par exemple :

```
<blockquote class="blockquote">  Les hommes ont des oreilles. Les hommes ont des nez. Les hommes ont des bouches. Nous aussi. Nous sommes des lapins</blockquote>
```

Cela donnera au texte « Les hommes ont des oreilles. Les hommes ont des nez. Les hommes ont des bouches. Nous aussi. Nous sommes des lapins », un style Bootstrap unique pour les citations.

#### Comment puis-je styliser l'auteur d'une citation différemment dans Bootstrap ?

Il est assez courant d'inclure un auteur après une citation. Il en va de même pour citer la source de n'importe quel bloc de texte. Pour ce faire, utilisez la classe `blockquote-footer` comme ceci :

```
<blockquote class="blockquote">  Les hommes ont des oreilles. Les hommes ont des nez. Les hommes ont des bouches. Nous aussi. Nous sommes des lapins  <div class="blockquote-footer">Ohans Lapin </div></blockquote>
```

Pour cet exemple, j'ai utilisé `blockquote-footer` à l'intérieur d'une balise `blockquote`. Ce n'est pas obligatoire. Vous pouvez utiliser le nom de classe `blockquote-footer` sur n'importe quel bloc de texte tel que l'élément de paragraphe, `p`.

Voici le résultat de ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0AdPSAwPR6ULPugPSFuDiLXJD3S3Bft64I6q)
_Les noms de classes blockquote de Bootstrap ajoutés à la citation et à l'auteur._

#### Comment supprimer le padding, la marge et le style par défaut sur une liste non ordonnée ?

Il semble que j'aie toujours besoin de faire cela lorsque je crée n'importe quel type de liste `html`. Encore une fois, c'est trivialement simple avec Bootstrap. Utilisez le nom de classe `list-unstyled`, comme ceci :

```
<ul class="list-unstyled">  <li>Merci</li>  <li>Muchas Gracias</li>  <li>Merci</li></ul>
```

![Image](https://cdn-media-1.freecodecamp.org/images/XYVsfPkvOo0QBfFz-jghumXfRcuHKHKRl5m2)
_Le style par défaut pour les listes — avec un style de liste à puces et un certain padding._

![Image](https://cdn-media-1.freecodecamp.org/images/Xd3d2-MfA7KN-GvHOF4hhPv7jnyHHestPb9C)
_La vue par défaut pour la liste a été modifiée. Pas de style de liste à puces, et pas de padding._

#### Comment créer des éléments de liste disposés côte à côte ?

Parfois, vous pouvez avoir besoin que vos éléments de liste soient disposés horizontalement, ou côte à côte, par opposition à la vue verticale par défaut. Utilisez le nom de classe `list-inline` sur la liste non ordonnée, et `list-inline-item` sur les éléments de liste.

Par exemple :

```
<ul class="list-inline">  <li class="list-inline-item">Merci</li>  <li class="list-inline-item">Muchas Gracias</li>  <li class="list-inline-item">Merci</li></ul>
```

Cela créera des éléments de liste alignés côte à côte, horizontalement.

![Image](https://cdn-media-1.freecodecamp.org/images/EB62J3FdZiq7cQfUS6SgbgBof6jNsQE5s3UK)
_La liste apparaît maintenant côte à côte, horizontalement — exactement comme prévu._

#### Quelles options de couleur sont disponibles dans Bootstrap ?

Les couleurs sont le langage visuel que la plupart des gens traitent avant même d'en prendre conscience.

Dans le design et Bootstrap en général, les couleurs peuvent être appliquées à une large gamme d'éléments. Textes, arrière-plans, bordures, et plus encore.

Demandez à un enfant de 5 ans de nommer des couleurs et il partira avec « rouge, bleu, vert... »

Il existe bien plus de 100 noms de couleurs en CSS, ce qui rend difficile de représenter tout cela avec des noms de classes. Il serait bizarre d'avoir des noms de classes `color-blue`, `color-red`, et ainsi de suite pour plus de 100 couleurs.

Par conséquent, les couleurs sont traitées un peu différemment dans Bootstrap. Il existe certains mots-clés ou noms de couleurs spéciaux qui sont mappés à certaines couleurs.

Par exemple, le mot-clé `primary` est souvent associé à une couleur bleue. `success` à une couleur verte, et `danger` à une couleur rouge, et ainsi de suite.

![Image](https://cdn-media-1.freecodecamp.org/images/l6DyABHOo2TP89kJkC0mx7Ra3E2Vg0DaRZr7)
_Les couleurs de [Bootstrap](https://getbootstrap.com/docs/4.0/utilities/colors/" rel="noopener" target="_blank" title=")._

#### Comment afficher un texte coloré dans Bootstrap ?

Pour afficher un texte dans une certaine couleur, vous devez utiliser les noms de classes `.text-*`, où « * » peut être n'importe lequel de `primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light` ou `dark`.

Par exemple :

```
<p class="text-primary">Hello World</p><p class="text-secondary">Hello World</p><p class="text-success">Hello World</p><p class="text-danger">Hello World</p><p class="text-warning">Hello World</p><p class="text-info">Hello World</p><p class="text-light">Hello World</p><p class="text-dark">Hello World</p>
```

Le bloc de code ci-dessus produira le résultat illustré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/ztoZoRK9CVd6rubni9JWAsMc7MCWrHfBhymJ)
_Différentes couleurs de texte fournies par Bootstrap_

Il est important de noter que l'application de la classe `text-light` produit un texte de couleur claire. Il est plus approprié d'appliquer cette classe à des textes sur un fond sombre.

Par exemple, j'ai utilisé la classe `text-light` sur un texte à l'intérieur d'un fond bleu. Il s'affiche joliment.

![Image](https://cdn-media-1.freecodecamp.org/images/UdTUxLGTWuvfyybTH2kOokwMdFMvzZI3FCr8)
_Utilisez text-light sur des fonds plus sombres. De cette façon, vous obtiendrez de beaux résultats — des textes lisibles._

#### Comment créer des images adaptatives (Responsive Images) dans Bootstrap ?

Tout le monde aime les images. Si vous ne les aimez pas, alors vous faites partie des très rares exceptions. Par expérience, vous devez savoir que le stylisme des images peut devenir incontrôlable très rapidement.

Pour créer des images adaptatives quel que soit l'appareil utilisé, ajoutez la classe `.img-fluid` à l'élément image.

Par exemple :

Dans l'exemple du poème sur le lapin, j'ai ajouté l'image d'un chaton mignon :

```
<img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg"/>
```

Par défaut, les limites de l'image ne sont pas visibles à cause de sa taille. Ajoutez la classe `.img-fluid` pour une image entièrement adaptative.

```
<img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="img-fluid"/>
```

![Image](https://cdn-media-1.freecodecamp.org/images/MeA8iXRqDGA6Qe99aC62a-UlK5CPvYg9-uGj)

![Image](https://cdn-media-1.freecodecamp.org/images/dosXoI2XdiwRHqij28gIFG92pV-FWwlFoPBZ)
_Image entièrement adaptative d'un chaton mignon. L'image s'affiche joliment sur mobile (à gauche) et même sur de plus grands appareils (à droite)_

#### Comment créer des images avec des bords subtilement arrondis dans Bootstrap ?

Parfois, vous voulez quelque chose de différent. Ainsi, Bootstrap permet d'avoir des images avec des bordures subtilement arrondies. Ajoutez simplement la classe `rounded` comme ceci :

```
<img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="img-fluid rounded"/>
```

Notez que le balisage ci-dessus possède plus d'un nom de classe appliqué. C'est un bon exemple de la façon d'utiliser plusieurs noms de classes sur un seul élément.

Regardez de près le résultat ci-dessous. Vous trouverez l'image avec des bordures légèrement arrondies. Je trouve souvent cela plus esthétique que d'avoir des bords carrés.

![Image](https://cdn-media-1.freecodecamp.org/images/6eKqd8sP6SSPuv77cpfHYIAfcwozm6iMeeoI)
_Le chaton mignon a reçu des bords subtilement arrondis pour l'esthétique._

#### Puis-je créer des images avec un seul côté ayant une bordure arrondie ?

Dans l'exemple précédent, les coins arrondis ont été appliqués à tous les côtés de l'image. Il est également possible d'avoir des bordures arrondies dans une seule direction. Par exemple, l'application de la classe `rounded-top` créera une image avec seulement les coins supérieurs arrondis. `.rounded-bottom` fait exactement le contraire.

```
<img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="img-fluid rounded-top"/>
```

Au cas où vous vous poseriez la question, vous pouvez également utiliser les classes `rounded-left` et `rounded-right` pour les bordures gauche et droite respectivement.

#### Existe-t-il des options pour créer des images avec un arrière-plan entièrement circulaire ?

Oui. Bootstrap permet de créer une image circulaire en utilisant le nom de classe `rounded-circle`.

Par exemple :

```
<img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="img-fluid rounded-circle"/>
```

Cela donnera un chaton tout rond et mignon.

![Image](https://cdn-media-1.freecodecamp.org/images/aqxzbeoeYlELQ3hFf8lAMeVeUoFf08PcMxlD)
_Chaton mignon arrondi avec une bordure entièrement ronde._

#### Puis-je manipuler les bords arrondis que Bootstrap donne ?

Autant que possible, Bootstrap 4 essaie de ne pas vous enlever votre liberté. Donc oui, les bords arrondis que Bootstrap donne peuvent être peaufinés avec vos propres styles. Laissez-moi vous montrer un exemple.

Si pour une raison quelconque vous avez stylisé une image pour avoir des bordures arrondies, vous pouvez supprimer les bordures arrondies avec Bootstrap en ajoutant la classe `rounded-0`.

Par exemple :
J'ai ajouté un border-radius de `50px` à l'image du chat :

```
img {  border-radius: 50px}
```

Voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/HBvfCyu1d3GWhxhy5fc7Y9JUVItkJgAkEpXY)
_Le chaton mignon avec un border-radius de 50px._

C'est une image de chat de forme bizarre. Voyons ce qui se passe sous le capot.

Dans le balisage `html`, nous avons ceci :

```
<img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="img-fluid rounded-bottom"/>
```

Comme vous pouvez le voir dans le balisage, il y a déjà une classe `rounded-bottom` appliquée à l'image. Ainsi, Bootstrap aura le contrôle total sur les bords inférieurs. Les bords que vous ajoutez en utilisant la propriété `border-radius` n'affecteront que les bordures supérieures, ou les bordures que vous n'avez pas stylisées à l'aide de Bootstrap.

Est-ce que cela a du sens ? Je suppose que oui.

Si vous enleviez la classe `rounded-bottom` ou toute autre classe `rounded` sur l'image, votre style s'appliquerait désormais à tous les côtés de la bordure. Voir le résultat ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/VCWg7VhovP3P9RENKdOzyFjbypm2--hTMA2m)
_Le chaton mignon a maintenant tous ses côtés obéissant à la règle CSS que nous venons d'écrire._

Dans l'exemple ci-dessus, la classe `rounded-bottom` a été supprimée du balisage, laissant les bordures faire votre volonté.

Selon vos besoins spécifiques, vous pouvez retirer toutes les classes `.rounded` fournies par Bootstrap de votre balisage et styliser l'image vous-même à l'aide de la propriété `border-radius`.

Si vous souhaitez que certains bords conservent le comportement Bootstrap par défaut, vous pouvez laisser la classe de côté arrondi spécifique dans votre balisage, telle que `.rounded-top`, tout en stylisant également les images à l'aide de `border-radius`.

#### Comment aligner des images à droite ou à gauche ?

L'alignement est une partie vitale du design. La plupart du temps, vous continuerez à déplacer des éléments jusqu'à ce que cela vous semble correct.

Pour aligner des images à gauche ou à droite, utilisez l'une des classes `float-right` ou `float-left`.

Par exemple :

```
<img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="rounded-circle float-left"/>
```

![Image](https://cdn-media-1.freecodecamp.org/images/b94BJ9THInAurmuDi155PIfEbNigbn2rXcq2)
_Le lapin a été flotté vers la gauche. Il se trouve maintenant côte à côte avec le texte._

Pour que l'image flotte dans la direction souhaitée, vous devez supprimer la classe `img-fluid` sur l'image, et donner à l'image une largeur fixe comme ceci :

```
img {  width: 150px}
```

La raison en est que `img-fluid` fait en sorte que l'image remplisse la largeur disponible de l'appareil. Elle ne peut pas se déplacer vers la gauche ou la droite de l'écran car elle occupe déjà tout l'espace. Vous devez réduire la largeur de l'image dans votre propre feuille de style CSS comme je l'ai fait dans l'exemple ci-dessus.

#### Quelle est la meilleure façon de styliser des images avec des descriptions textuelles ?

Il n'est pas impossible d'avoir des images avec des descriptions textuelles. C'est utile dans les galeries et d'autres cas où vous essayez de transmettre plus d'informations sur l'image en utilisant un bloc de texte.

La façon correcte de le faire est de contenir les images dans une balise `figure` et d'avoir le bloc de texte dans un bloc `figcaption`.

Voici un exemple :

```
<figure>  <img src="https://static.pexels.com/photos/126407/pexels-photo-126407.jpeg" class="img-fluid rounded"/>  <figcaption>    Je m'appelle Katey et j'ai seulement 2 mois et demi.  </figcaption></figure>
```

```
<figure>  <img src="https://static.pexels.com/photos/416160/pexels-photo-416160.jpeg" class="img-fluid rounded"/>  <figcaption>    Je m'appelle Jando et j'ai seulement 3 mois. Clairement, j'adore m'amuser !  </figcaption></figure>
```

Et voici le résultat de cela :

![Image](https://cdn-media-1.freecodecamp.org/images/zzBXh9xqUnXBc1KcK1ogAYB0WqneLLs3KkPe)

Rien de magique pour l'instant. Maintenant, stylisons cela.

Bootstrap permet l'utilisation de deux noms de classes, `figure-img` et `figure-caption`. Comme vous l'avez peut-être deviné, ils sont tous deux utilisés respectivement sur l'image et le bloc de texte.

Laissez-moi vous montrer un exemple.

Allez-y et ajoutez les noms de classes `figure-img` et `figure-caption` comme ceci :

```
<figure>  <img src="https://static.pexels.com/photos/126407/pexels-photo-126407.jpeg" class="img-fluid figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Katey et j'ai seulement 2 mois et demi.  </figcaption></figure>
```

```
<figure>  <img src="https://static.pexels.com/photos/416160/pexels-photo-416160.jpeg" class="img-fluid figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Jando et j'ai seulement 3 mois. Clairement, j'adore m'amuser !  </figcaption></figure>
```

Cela créera un certain espacement entre l'image et la légende, et la légende textuelle recevra une couleur légèrement calme.

Voir le résultat ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/0pDgDiUmQKSxPb4HBvb1i8BytB5YQi9JqhET)

Notez que pour créer l'effet montré dans le résultat ci-dessus, j'ai ajouté les noms de classes `img-fluid` et `rounded` aux images de figure. Cela garantira que les images sont adaptatives et ont des bords légèrement arrondis.

#### Comment centrer des images avec Bootstrap ?

Centrer des images peut devenir un peu délicat avec Bootstrap. La première chose est de s'assurer que l'image que vous essayez de centrer n'a pas été stylisée pour s'adapter à la largeur disponible ou à `100%`. Vous devriez supprimer la classe `img-fluid` sur l'image si elle existe.

Voyons un exemple.

Voici un balisage d'un exemple précédent :

```
<img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="rounded img-fluid"/>
```

Je vais enlever la classe `img-fluid` :

```
<img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="rounded"/>
```

Et je vais styliser l'image avec ma propre classe qui limitera la largeur de l'image à peut-être `200px` :

```
.img-restricted {  width: 200px}
```

Cela produira l'image de largeur fixe que vous voyez ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/l2kj5bUM-k4sZDPY-yL5VG0C-6jVJ5Y7qm0f)
_Image limitée à une largeur de 200px. Par défaut, elle est alignée horizontalement au début de la page et NON au centre._

Maintenant, pour centrer l'image.

Il existe deux façons différentes de centrer des images dans Bootstrap.

1. utiliser le nom de classe `text-center`
2. utiliser le nom de classe `mx-auto`

Ces options fonctionnent un peu différemment.

Pour la classe `text-center`, l'image à centrer doit conserver sa valeur `display` par défaut de `inline-block` ou `inline`. De plus, le nom de la classe doit être ajouté au bloc parent de l'image tel qu'un `div` et NON à l'image elle-même.

Désolé si cela semble déroutant. Voyons un exemple.

```
<div class="text-center">  <img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="rounded img-restricted"/></div>
```

Notez que le nom de la classe, `text-center`, a été ajouté au `div` parent et NON à l'élément `img`.

Et voilà, nous avons une image centrée !

![Image](https://cdn-media-1.freecodecamp.org/images/IQcJDjxSQIoyDmzeSDlNN6k-ZT5eXlb289i1)
_Image centrée en appliquant text-center sur l'élément parent de l'image et NON sur l'image elle-même._

Juste pour que vous voyiez à quoi ressemblerait un mauvais balisage, ceci est faux :

```
<div>  <img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="text-center rounded img-restricted"/></div>
```

Le balisage est faux car `text-center` a été appliqué à l'élément `img`. Cela ne centrera PAS l'élément image.

Pourquoi la classe `text-center` fonctionne-t-elle ? Les images sont des éléments `inline-block` par défaut, elles honoreront donc le style `text-center` appliqué sur un élément parent.

Voyons la deuxième façon de centrer des images en utilisant la classe `**mx-auto**`.

Si pour une raison quelconque vous avez modifié la propriété `display` par défaut de l'image et l'avez rendue `block`, la classe `text-center` ne fonctionnera plus.

Par exemple :

```
.img-restricted {   display: block}
```

Une fois que vous avez défini la propriété `display` sur `block`, l'image n'honore plus le style `text-center` — car elle n'est plus un élément `inline`.

![Image](https://cdn-media-1.freecodecamp.org/images/vy6FtIodODDa1Ju1WtpPUGM7GK9lFALauAMQ)
_Une fois que la propriété display est définie sur block, l'image revient à sa position par défaut et n'est donc PAS centrée._

Dans ce cas, vous devez centrer l'image comme tout autre élément de bloc. Appliquez le nom de classe `mx-auto` à l'élément `img` comme ceci :

```
<img src="https://static.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg" class="mx-auto rounded img-restricted"/>
```

Et l'image redevient centrée.

![Image](https://cdn-media-1.freecodecamp.org/images/sFyleAUCGBBzLINTkhDfA1aa65-Zjo3605OZ)
_Et l'image redevient centrée. Ouf !_

Maintenant, vous pouvez aller de l'avant et centrer n'importe quelle image que vous désirez.

#### Comment ajouter de l'espacement sur tous les côtés d'un élément ?

C'est nouveau dans Bootstrap 4, et j'ai trouvé cela super utile. Souvent, vous avez besoin d'ajouter un `padding` ou une `margin` supplémentaire à un élément. Dans les versions précédentes, vous deviez le faire en écrivant vos propres styles. Parfois, cela ne fonctionnait pas en raison de problèmes de spécificité. Tout cela a été pris en charge dans la dernière version de Bootstrap.

L'espacement que Bootstrap donne va de `.25rem` à `3rem`. Pour la plupart des cas d'utilisation, cela devrait suffire.

Supposons que les marges soient représentées par la lettre `m` et le padding par la lettre `p`. De plus, laissons les différentes plages être représentées de `0 à 5`.

Cela étant dit, vous pouvez ajouter de l'espacement sur tous les côtés d'un élément en utilisant l'une des classes `**m-***` pour les marges et `**p-***` pour le padding.

Par exemple `**m-0**`, `m-1`, `m-2`, `m-3`, `m-4` et `m-5` sont tous des noms de classes valides pour ajouter des marges. On peut dire la même chose pour l'ajout de padding en utilisant l'un des noms de classes suivants `**p-0**`, `p-1`, `p-2`, `p-3`, `p-4` et `**p-5.**`

Voyons un exemple pratique en utilisant un exemple précédent. Ajoutons un peu d'espacement aux images de figure et à la légende textuelle que nous avons créées plus tôt.

J'appliquerai un peu de padding à l'élément `figure`, comme ceci :

```
<figure class="p-5">  <img src="https://static.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg" class="img-fluid rounded figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Flerri et j'ai seulement 2 mois.  </figcaption></figure>
```

Qu'est-ce qui a changé ?

J'ai ajouté la classe `p-5`, c'est tout ce qui a changé. Et le résultat ?

Voir ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/zv3srpns3cM5JqOsXq82I6-ds0xujA-Und26)
_Un padding de 3rem a été ajouté au premier élément de figure. Cela a été réalisé en utilisant la classe Bootstrap 4 : p-5._

Contrairement aux autres figures, vous pouvez voir que la première a un padding ajouté comme espacement interne sur tous les côtés. Plutôt cool !

Allons un peu plus loin et ajoutons la classe de padding `p-5` à toutes les figures :

```
<figure class="p-5">  <img src="https://static.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg" class="img-fluid rounded figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Flerri et j'ai seulement 2 mois.  </figcaption></figure>
```

```
<figure class="p-5">  <img src="https://static.pexels.com/photos/126407/pexels-photo-126407.jpeg" class="img-fluid rounded figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Katey et j'ai seulement 2 mois et demi.  </figcaption></figure>
```

```
<figure class="p-5">  <img src="https://static.pexels.com/photos/416160/pexels-photo-416160.jpeg" class="img-fluid rounded figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Jando et j'ai seulement 3 mois. Clairement, j'adore m'amuser !  </figcaption></figure>
```

Maintenant, toutes les figures ont un espacement supplémentaire.

![Image](https://cdn-media-1.freecodecamp.org/images/Qmv2m4Qi5ANVgj7UgWNUfb8THn0-1Kfy1U1f)
_Un padding de 3rem a été ajouté à toutes les figures. Le nom de classe p-5 a été utilisé pour y parvenir._

Résultat assez impressionnant pour peu de code supplémentaire.

#### Comment réduire ou augmenter l'espacement ajouté sur tous les côtés d'un élément ?

Dans l'exemple précédent, j'ai mentionné que les plages de classes étaient représentées de `**0 à 5.**`

Zéro, `0`, supprimera tout espacement sur un élément, tandis que l'espacement augmente au fur et à mesure que vous passez de `1` à `5`.

![Image](https://cdn-media-1.freecodecamp.org/images/Ch1dWGaAqc8ocWQvqc3hWfuAWmt7UIoR7q5y)
_Illustration de la plage de tailles pour les noms de classes d'espacement_

Par exemple, la marge créée par `**m-2**` sera plus petite que celle créée par `**m-5**`. De même, le padding créé par `**p-1**` sera plus petit que celui créé par `**p-3.**`

Pour les curieux, `1` ajoute un espacement de `0.25rem`, `2` ajoute un espacement de `0.5rem`, `3` ajoute un espacement de `1rem`, `4` ajoute un espacement de `1.5rem` et `5` ajoute un espacement de `3rem`.

![Image](https://cdn-media-1.freecodecamp.org/images/Pf9IlWOWh83I6ZhFKLUxhm3cYOZ62i8Wfrhg)
_Espacement de chaque classe_

Pour illustrer cela, je vais ajouter différents noms de classes d'espacement sur les différentes figures comme ceci :

```
<figure class="p-3">  <img src="https://static.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg" class="img-fluid rounded figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Flerri et j'ai seulement 2 mois.  </figcaption></figure>
```

```
<figure class="p-4">  <img src="https://static.pexels.com/photos/126407/pexels-photo-126407.jpeg" class="img-fluid rounded figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Katey et j'ai seulement 2 mois et demi.  </figcaption></figure>
```

```
<figure class="p-5">  <img src="https://static.pexels.com/photos/416160/pexels-photo-416160.jpeg" class="img-fluid rounded figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Jando et j'ai seulement 3 mois. Clairement, j'adore m'amuser !  </figcaption></figure>
```

Voici le résultat de cela.

![Image](https://cdn-media-1.freecodecamp.org/images/9L4aWJPI7ljh9OdS-IIOfYfIFqsctNDFjDbS)
_Les figures ont un espacement interne différent. Cela est dû aux différents noms de classes d'espacement ajoutés au balisage._

Dans le résultat ci-dessus, vous pouvez voir le padding augmenter de la première figure à la troisième.

#### Comment ajouter de l'espacement à UN SEUL côté d'un élément ?

Il y a des moments où vous ne voulez pas d'espacement sur tous les côtés d'un élément. Vous pouvez n'avoir besoin d'espacement qu'en `top` (haut), `bottom` (bas), `left` (gauche) ou `right` (droite) de l'élément.

Bootstrap a toutes les options ! Cela m'enthousiasme. Vous seriez surpris de voir à quel point c'est utile lorsque vous commencez à construire des choses.

Au lieu d'utiliser les noms de classes `m-*`, ajoutez un `t`, `b`, `l` ou `r` pour une marge `top`, `bottom`, `left` ou `right`.

Par exemple, `mt-1`, `mb-1`, `ml-1` et `mr-1` sont tous des noms de classes valides. La plage de `**0**` à `**5**` reste la même qu'auparavant.

![Image](https://cdn-media-1.freecodecamp.org/images/4Dpr0pOhjUsebR0fxd66JYFPYGtIVvJ9b7WZ)
_t est top. b est bottom. r est right. l est left._

La convention `t`, `b`, `r` et `l` est également la même pour le padding.

![Image](https://cdn-media-1.freecodecamp.org/images/qpqR49YESkxz66idYmQ7TPcaurHWNJxmMksD)
_t est top. b est bottom. r est right. l est left. même pour le padding._

Je vais modifier l'espacement que nous avons sur toutes les figures pour représenter uniquement le padding `bottom`.

```
<figure class="pb-3">  <img src="https://static.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg" class="img-fluid rounded figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Flerri et j'ai seulement 2 mois.  </figcaption></figure>
```

```
<figure class="pb-3">  <img src="https://static.pexels.com/photos/126407/pexels-photo-126407.jpeg" class="img-fluid rounded figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Katey et j'ai seulement 2 mois et demi.  </figcaption></figure>
```

```
<figure class="pb-3">  <img src="https://static.pexels.com/photos/416160/pexels-photo-416160.jpeg" class="img-fluid rounded figure-img"/>  <figcaption class="figure-caption">    Je m'appelle Jando et j'ai seulement 3 mois. Clairement, j'adore m'amuser !  </figcaption></figure>
```

Comme vous pouvez le voir, j'ai utilisé le nom de classe `**pb-3**`. Cela ajoutera des paddings inférieurs de `1rem` chacun.

![Image](https://cdn-media-1.freecodecamp.org/images/GA34uCd4kZsWiYr9Wzj7KPMbZO2HppdYmrgj)

#### Comment ajouter le même espacement aux côtés opposés d'un élément ?

Assez parlé d'espacement. C'est le dernier exemple — je le promets.

Il est également possible d'ajouter l'espacement aux côtés `top` et `bottom` d'un élément par exemple. De la même manière, vous pouvez ajouter le même espacement à la `left` et à la `right` d'un élément également.

Alors, comment fait-on cela ?

Laissez `x` représenter les valeurs `left` et `right`, tandis que `y` représente les valeurs `top` et `bottom`.

Pour ajouter le même espacement aux côtés `left` et `right` d'un élément, utilisez la classe `mx-*`, et la classe `my-*` pour les valeurs `top` et `bottom`.

Par exemple, `mx-1` ajoutera une marge de `0.25rem` sur les côtés `left` et `right` de l'élément. `my-1` ajoutera `0.25rem` sur les côtés `top` et `bottom` de l'élément.

![Image](https://cdn-media-1.freecodecamp.org/images/W0L3Ad3WWN2Zrfd45lt3ACaYV9ak4J9DcBWk)
_Si vous n'avez pas séché les cours de mathématiques à l'école, la convention de nommage « x » et « y » ne devrait pas vous sembler si étrange._

Et c'est tout pour l'espacement ! Croyez-moi, c'est un sujet important.

#### Comment styliser un paragraphe d'introduction (Lead Paragraph) ?

Le paragraphe d'introduction est généralement le premier paragraphe d'un essai ou d'un article. Le but est d'accrocher l'attention du lecteur.

Pour styliser un paragraphe d'introduction, ajoutez la classe `.lead` au paragraphe. Par exemple, je vais ajouter la classe `.lead` au premier paragraphe du poème sur le lapin comme ceci :

```
<p class="lead"> Ce qui suit est un poème pour la plupart inintelligent sur les lapins. Ne réfléchissez pas trop à leur sujet. <br /> Profitez-en !</p>
```

Et le résultat est un paragraphe légèrement plus grand comme on le voit ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/M-e3KjPnMiPZ20zpx3Pv13qjzwY9PyjhQDLq)
_un paragraphe légèrement plus grand — paragraphe d'introduction (lead)._

Pour les technophiles, la classe `.lead` augmente la taille de la police de `25%` et règle le `font-weight` à `300`, ce qui donne un ton de texte plus grand et beaucoup plus léger.

![Image](https://cdn-media-1.freecodecamp.org/images/itRikZSixM7RX2GP3hYfZAvp3B4uN9gnpWKO)

### Les bases de la conception adaptative (Responsive Design) avec Bootstrap

Avez-vous déjà utilisé Flexbox ? Si la réponse est oui, c'est génial. Avec Flexbox, le contexte de formatage flexbox n'est PAS initié tant qu'un `flex-container` n'est pas créé.

Que vous ayez une certaine expérience avec Flexbox ou non, avec Bootstrap, un élément `container` doit être défini pour récolter les bénéfices du design adaptatif offert par Bootstrap.

#### Alors, qu'est-ce qu'un conteneur (container) Bootstrap ?

Un conteneur est simplement un élément avec la classe `.container` appliquée. Par exemple :

```
<div class="container"></div>
```

Plutôt simple, non ?

Pour un balisage simple, il est probable que vous enveloppiez chaque élément dans un conteneur Bootstrap.

Par exemple, je vais refactoriser le poème sur le lapin pour utiliser le conteneur Bootstrap.

```
<div class="container">    <h1> Poèmes de lapins </h1>  <p class="lead"> Ce qui suit est un poème pour la plupart inintelligent sur les lapins. Ne réfléchissez pas trop à leur sujet. <br /> Profitez-en !  </p>
```

```
<h2 class="display-5"> Le lapin qui n'avait pas d'oreilles </h2>  <p> M. Lapin. Quelle taille avaient les oreilles de vos ancêtres </p>  <p> Quelle fierté duveteuse pour votre famille </p>  <p class="display-4"> Mais, attendez... </p>  <p class="text-center">Comment se fait-il que vous n'ayez pas d'oreilles </p>  <p> Avec vos yeux vous entendez, et avec votre nez vous voyez ? </p>  <p class="font-weight-bold"> Comme c'est triste, M. Lapin </p>  <p class="font-italic">Voyez-le sauter, sauter, sauter sur des pattes si fortes.</p>  <strong class="font-weight-normal"> Mais des oreilles, il n'en a aucune </strong>  <p> Vivez longtemps, et rendez vos ancêtres fiers </p>  <p class="text-capitalize">Nous croyons en vous</p>  <blockquote class="blockquote">    Les hommes ont des oreilles. Les hommes ont des nez. Les hommes ont des bouches. Nous aussi. Nous sommes des lapins    <div class="blockquote-footer">Ohans Lapin </div>  </blockquote>  ...</div>
```

Comme vous pouvez le voir dans l'échantillon de code ci-dessus, j'ai maintenant enveloppé CHAQUE élément dans un div avec la classe container.

```
<div class="container">    <!--tous les autres éléments vont ici --></div>
```

#### Quelle est la différence entre container et container-fluid ?

Dans l'exemple ci-dessus, j'ai fait ceci :

```
<div class="container">    <!--tous les autres éléments vont ici --></div>
```

Bien que cela soit correct, il existe une autre classe de conteneur que Bootstrap met à disposition, et c'est `.container-fluid`.

L'usage est le même, comme ceci :

```
<div class="container-fluid">    <!--tous les autres éléments vont ici --></div>
```

Alors, quelle est la différence ?

Voyons des exemples visuels.

Je me suis toujours demandé pourquoi je ne comprenais pas la différence entre ces deux-là quand j'ai commencé à apprendre le framework Bootstrap, il y a des années. Vous avez de la chance car je le comprends maintenant. Laissez-moi vous expliquer :)

Pour un retour visuel, je vais donner au `body` une couleur d'arrière-plan `red` (rouge). Je vais également donner aux classes `container` et `container-fluid` des couleurs d'arrière-plan `white` (blanc). Juste pour qu'elles n'héritent pas de la couleur d'arrière-plan `red` du `body`.

Voici le code :

```
body {  background: red}.container,.container-fluid {  background: white}
```

Maintenant, voyons quelle différence cela fait lorsque vous enveloppez tout le contenu du poème sur le lapin dans un div `.container`.

Avec tout le contenu du poème sur le lapin enveloppé dans un div `.container`, essayez de redimensionner votre navigateur.

Que remarquez-vous ?

![Image](https://cdn-media-1.freecodecamp.org/images/fzRhz2EySBFzxw-EfttIBPAIlJ2kG2xPANpB)
_Le comportement attendu lors du redimensionnement du navigateur._

Vous remarquerez que la largeur du `.container` change à différents viewports. Il laisse un espace de respiration entre lui-même et l'élément `body` — cela explique pourquoi vous voyez l'arrière-plan `red` dans le gif ci-dessus. N'oubliez pas que l'élément `body` a un arrière-plan `red`.

Aussi simple que cela puisse paraître, c'est un comportement très important à noter.

Au contraire, si vous utilisiez `.container-fluid`, le div remplit tout le viewport disponible. Vous ne voyez pas l'arrière-plan rouge car il n'y a pas d'espace de respiration entre l'élément `container-fluid` et le `body`. Tout l'espace disponible a été occupé.

![Image](https://cdn-media-1.freecodecamp.org/images/JGYFcK7sWcDFdVBEgL1UAVgQkhRSypi4nxAo)
_Le comportement attendu lors du redimensionnement du navigateur._

Comme vous pouvez le voir, avec la classe `.container-fluid`, vous n'avez pas le luxe de l'espace. Le conteneur occupe `100%` de la largeur disponible. Il y a toujours un petit padding appliqué à l'élément `.container-fluid`, mais la largeur ne s'agrandit pas et ne change pas avec le viewport de l'utilisateur. C'est la différence entre les noms de classes `.container` et `.container-fluid`.

#### Que sont les Media Queries ?

Puisque cette section est axée sur le design adaptatif, je pense qu'il est important d'avoir un rappel sur ce que sont les media queries — surtout pour les débutants. Cette section est également vitale pour comprendre comment fonctionnent les modules adaptatifs dans Bootstrap.

Considérez le bloc de code ci-dessous :

```
@media screen and (min-width: 768px) {     .bg {         background-color: blue     }}
```

Si vous avez l'habitude d'écrire des modules adaptatifs à la main, alors le bloc de code ci-dessus devrait vous être familier.

Le bloc de code représente l'utilisation des media queries CSS. Si vous n'avez aucune idée de la façon dont cela fonctionne, veuillez lire la suite.

Les media queries sont au cœur du design adaptatif. Elles vous permettent de cibler des tailles d'écran spécifiques et de spécifier des codes à exécuter uniquement sur les appareils spécifiés.

La forme la plus populaire sous laquelle les media queries sont utilisées est ce qu'on appelle la règle `**@media**`.

Elle ressemble à ceci :

```
@media screen and (min-width: 300px) {  /*écrivez votre CSS dans ce bloc de code*/}
```

En la regardant, vous pouvez presque deviner ce qu'elle fait.  
« Pour un appareil à écran avec une largeur minimale de 300px... faites ceci et cela »

Tous les styles à l'intérieur du bloc de code ne s'appliqueront qu'aux appareils qui correspondent à l'expression, « `screen and (min-width: 300px)` ». Dans l'exemple ci-dessus, la largeur de l'appareil `300px` est connue sous le nom de point d'arrêt (breakpoint).

Je suppose que cela a aidé à éclaircir une certaine confusion.

#### Qu'est-ce que le système de grille (Grid System) de Bootstrap ?

Avec Bootstrap ou n'importe quel design bien pensé, rien ne se trouve simplement sur la page. Chaque élément repose sur une structure de grille bien définie.

![Image](https://cdn-media-1.freecodecamp.org/images/3VwGM3hSmDRYV4Q0JSC-jZMDcE4gHpfbwwjG)
_Exemple de grille_

Dans ce contexte, une grille est une série de lignes de guidage verticales et horizontales sécantes utilisées pour structurer le contenu d'une page web.

Personne ne se contente de plaquer du contenu n'importe comment sur une page.

![Image](https://cdn-media-1.freecodecamp.org/images/1RdjnoFZXTBPbz7R7PUuHXZpIrwHQdW7E775)
_contenu web mal disposé sur une grille._

Regardez l'exemple ci-dessus. Avez-vous déjà vu un contenu sur un site web disposé comme cela ? Je parie que « non ».

La plupart du temps, vous aurez une grille qui contient un contenu bien structuré. Quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Qt9TgYy6OzyfAzoxY0uXK8OC5DaK6vdZXX8-)
_Contenu judicieusement disposé le long d'une grille_

Bootstrap a un moyen de définir des grilles et d'y placer correctement le contenu. C'est ce qu'on appelle le système de grille de Bootstrap.

Pour les utilisateurs plus avancés, il est important de noter que vous n'avez pas besoin de lignes de grille horizontales ou verticales. Avec le [CSS Grid](https://medium.com/flexbox-and-grids/how-to-efficiently-master-the-css-grid-in-a-jiffy-585d0c213577) saupoudré d'un peu de magie CSS, vous pouvez facilement construire une mise en page non conventionnelle.

#### Comment utiliser la grille Bootstrap ?

La grille de Bootstrap 4 est construite avec Flexbox — ce qui la rend encore plus puissante que jamais.

Avertissement : cette partie de Bootstrap a tendance à être pénible quand on l'apprend pour la première fois. Mais, si vous prenez le temps de maîtriser le système de grille de Bootstrap, vous découvrirez que c'est l'une des connaissances les plus importantes que vous ayez sur Bootstrap.

Laissez-moi vous expliquer comment cela fonctionne.

Ainsi, votre amie Chloé vous appelle à minuit et vous dit : « Je vais me marier ! ..haha »

Vous êtes tous les deux excités par la nouvelle et discutez plus longtemps que prévu. Juste au moment où vous alliez mettre fin à l'appel, vous décidez d'agir comme un super développeur providentiel. « Hé, Chloé. Je vais construire ton site de mariage pour toi ! » Et vous discutez pendant encore 30 minutes...

Eh bien, belle histoire.

La bonne nouvelle est que vous venez de ravir Chloé. Elle sera super excitée. La mauvaise nouvelle, ou (pas si mauvaise nouvelle), est que vous allez passer du temps et de l'énergie (et du café) pour construire le site du mariage.

Ainsi, vous obtenez une maquette comme celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/Fk5B9eB270DPqqsVC92YTvzsDHg9mpws366d)
_J'ai conçu cela à la hâte pour les besoins de cet article. Alors, ne commencez pas à le critiquer :)_

Vous n'avez pas beaucoup de temps pour construire ce site, alors vous recourez à l'utilisation de Bootstrap. Quelle est la première chose à faire ? Configurer la grille Bootstrap.

Il y a des règles assez strictes à suivre lors de l'utilisation du système de grille Bootstrap.

Tout d'abord, dans votre esprit, remontez jusqu'à la maquette ci-dessus et essayez de décomposer chaque ligne de contenu en rangées séparées. Cette ligne de contenu doit aller de l'horizontal au vertical.

Pouvez-vous faire cela ?

Je l'ai fait pour vous, et voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/k7tPEApuxaRgBYsOet1hqT1aq0YBybpIZHN0)

Ce que j'ai fait, c'est dessiner des boîtes horizontales s'étendant de gauche à droite autour du contenu groupé le long d'une ligne. Même pour des mises en page plus complexes, ce type de décomposition est très important.

Ces boîtes horizontales sont appelées **rows** (rangées). Dénotées par la classe `.row`.

Cela ne s'arrête pas là. À l'intérieur de chaque rangée, il y a des boîtes de contenu individuelles. Regardez l'image précédente et essayez d'identifier ces boîtes de contenu individuelles.

Encore une fois, j'ai fait la même chose. Voir les résultats ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/rgG-6vF4zP10NLCUQjy2RN2TZsnANVtKfkjR)

Ces boîtes de contenu individuelles qui vivent à l'intérieur des rangées sont appelées **columns** (colonnes).

C'est logique ?

Les colonnes sont dénotées par la classe `.col`.

Puisque les rangées et les colonnes sont de grands amis, une colonne ne doit pas exister en dehors d'une rangée. C'est une règle importante à retenir.

De plus, chaque rangée doit être placée à l'intérieur d'un conteneur. Soit `.container`, soit `.container-fluid` fera l'affaire. Une rangée ne peut pas exister en dehors d'un conteneur. Elle doit vivre à l'intérieur d'un conteneur.

En pratique, vous pouvez avoir un conteneur global qui abrite tout le groupe de rangées, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/bRVin1Wx59n2baldHk1itJNXZnb1VQ3cfQiQ)
_un seul conteneur (en rouge) qui abrite toutes les rangées._

Ou vous pouvez avoir un conteneur qui enveloppe chaque rangée individuelle, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1JS2aTcxVWfwd9bxM3YOade48UWoDRRH9aRM)
_Plusieurs conteneurs qui abritent chaque rangée de contenu._

Je semble préférer cette dernière solution. Je la trouve plus flexible — dans certains cas d'utilisation.

Un résumé rapide : Chaque rangée doit être placée à l'intérieur d'un conteneur. Les rangées sont spécifiées avec le nom de classe `.row`, les colonnes avec `.col` et les conteneurs avec `.container` ou `.container-fluid`.

C'est la base du fonctionnement du système de grille de Bootstrap. Je discuterai de quelques cas d'utilisation plus pratiques dans les sections suivantes.

#### Qu'en est-il des colonnes de différentes tailles ?

Au fur et à mesure que vous construisez des applications web, il est très probable que vous ayez besoin de colonnes de différentes largeurs. Presque à chaque fois, il y aura des colonnes de largeurs variables à l'intérieur des rangées.

Voici un exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/RefRm678n0l2alGoQrXSX3iY21od-o4NzQJl)

Une colonne peut occuper `60%` de la largeur de la rangée, et l'autre `40%`. Comment gérez-vous cela en utilisant la grille Bootstrap ?

La grille Bootstrap suppose une grille de 12 colonnes. Elle suppose qu'à l'intérieur de chaque rangée, il existe 12 colonnes disponibles. Avec ces 12 colonnes, il devient de votre devoir de distribuer la largeur des colonnes de la manière que vous jugez appropriée.

Laissez-moi vous expliquer.

Comme montré précédemment, considérez la rangée de contenu ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/fFjCzSff-eQhyyfgB9WiU-wQnU8C8A39DfDT)

La rangée contient deux colonnes de tailles différentes.

À l'intérieur de cette rangée, la grille bootstrap suppose 12 colonnes à l'intérieur de cette rangée, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/vJdJJRerVBxAGqgnnJm-EWMUA1SGdhasuwHm)
_L'illustration de la grille de 12 colonnes de bootstrap._

Selon Bootstrap, il y a 12 colonnes à l'intérieur de chaque rangée. La façon dont vous distribuez l'espace dépend de vous.

Puisque vous n'avez que 2 colonnes définies par l'utilisateur (la plus grande et la plus petite colonne) à l'intérieur de la rangée, vous devez distribuer l'espace des colonnes, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/BWFoCBxRCSlM3EURKCddFmdaPEXiDN4YVadi)
_Distribuez les 12 colonnes Bootstrap parmi vos colonnes définies par l'utilisateur._

C'est assez simple, et en un rien de temps, vous vous y habituerez. Vous assignez 8 des colonnes à la plus grande colonne, et les 4 restantes à la plus petite. Notez que la somme de cela est égale à 12.

La somme de la largeur des colonnes distribuées à l'intérieur d'une rangée ne doit pas être supérieure à 12. Dans l'exemple ci-dessus, nous avons utilisé `col-8` et `col-4`. Le `col-8` représente la plus grande colonne qui occupe 8 colonnes de la grille bootstrap, et `col-4` représente la plus petite colonne avec 4 colonnes de la grille bootstrap.

Dans ce cas, vous aurez deux colonnes, l'une faisant `2x` la largeur de l'autre. Rappelez-vous, `8 / 4 = 2`.

Si vous vouliez des colonnes de largeur égale, vous utiliseriez `col-6` et `col-6`. Cela créera des colonnes égales qui occupent chacune la moitié des `12` colonnes de la grille Bootstrap.

Si vous vouliez un ratio plus important entre les deux colonnes, vous pourriez utiliser `col-10` et `col-2`.

Je suis presque sûr que vous comprenez maintenant.

#### Que se passe-t-il si je dépasse 12 colonnes ?

Dans le cas où vous avez un nombre total de colonnes qui dépasse 12, elles passeront à la ligne suivante. Tout comme l'utilisation de `flex-wrap`.

Par exemple :

```
<section>  <div class="container">    <div class="row">      <div class="col-3">      </div>      <div class="col-3">      </div>      <div class="col-3">      </div>      <div class="col-3">      </div>    </div>  </div></section>
```

Avec le balisage ci-dessus, le nombre total est de 12. Vous obtenez le résultat attendu ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/ty2EfpHNYj8sTSUEvd3BRh3ExEwQdSF5CNpp)
_4 colonnes à l'intérieur d'une rangée_

Si à l'intérieur de la même rangée vous ajoutez 2 colonnes supplémentaires, que se passe-t-il ?

```
<section>  <div class="container">    <div class="row">      <div class="col-3">      </div>      <div class="col-3">      </div>      <div class="col-3">      </div>      <div class="col-3">      </div>      <div class="col-3">      </div>      <div class="col-3">      </div>    </div>  </div></section>
```

L'ensemble de colonnes suivant après 12 passe à la ligne suivante, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/ZwXRJMYzU2jj6JXIbNFPLDKKqxCAgqMD6yTn)
_L'ensemble de colonnes suivant passe à la ligne suivante._

#### C'est bien, mais qu'en est-il des grilles adaptatives (Responsive Grids) ?

Dans les exemples ci-dessus, les tailles de colonnes définies resteront les mêmes quel que soit l'appareil de l'utilisateur.

Par exemple, `col-8` et `col-4` créeront 2 colonnes à l'intérieur de la rangée. Ce sera le cas sur les appareils mobiles et sur les appareils plus grands.

Pour les besoins du design adaptatif, ce sera rarement le cas. Si vous avez une grille à 2 colonnes sur les tablettes, vous voudrez peut-être que les colonnes s'empilent sur mobile.

![Image](https://cdn-media-1.freecodecamp.org/images/FDrBl010owMFRmhmfK9wTbww6zs22zIDfCgE)
_Deux colonnes côte à côte affichées sur de grands appareils. Chacune des colonnes occupe la moitié de la largeur disponible._

![Image](https://cdn-media-1.freecodecamp.org/images/fsGYYvnON70jNbLviS0v9ExwseqR3qgDr7Kl)
_Les deux colonnes s'empilent maintenant verticalement sur mobile. Chacune des colonnes occupe également 100% de la largeur disponible._

Vous pouvez également avoir une grille à 3 colonnes sur les ordinateurs de bureau, mais 2 sur les tablettes ou seulement 1 colonne sur les appareils mobiles. Dans ce cas, il doit y avoir un moyen de masquer les colonnes supplémentaires que nous ne voulons pas sur les petits appareils.

Heureusement, bootstrap a prévu ces cas d'utilisation !

Les colonnes Bootstrap peuvent être modifiées à l'aide de certains modificateurs.
Par exemple :

`col-**sm**` fait référence à une colonne sur les petits appareils (téléphones) et plus

`col-**md**` fait référence à une colonne sur les appareils moyens (tablettes) et plus

`col-**lg**` fait référence à une colonne sur les grands appareils (ordinateurs de bureau) et plus

`col-**xl**` fait référence à une colonne sur les appareils extra larges (écrans larges)

![Image](https://cdn-media-1.freecodecamp.org/images/yJPsT6-IxkYagtQn3a8DNjlLc0WcHsmRvINF)
_Capture d'écran de getbootstrap.com_

Revenons à l'exemple d'une largeur de 2 colonnes. Nous avons besoin que les colonnes apparaissent comme 2 colonnes sur les appareils moyens (et plus grands), mais qu'elles s'empilent horizontalement sur les plus petits appareils (téléphones).

Comment faites-vous cela ?

Commencez par un balisage comme celui-ci :

```
<div class="row">    <div></div>    <div></div></div>
```

J'ai supposé que cette `row` sera placée à l'intérieur d'un conteneur. N'oubliez pas que chaque `row` doit être placée à l'intérieur d'un `container`.

Bootstrap emploie une philosophie mobile first. Par défaut, vous devriez construire le design pour les appareils mobiles, puis passer aux appareils plus grands à partir de là.

Dans ce cas, nous allons d'abord nous occuper de l'affichage sur les appareils mobiles.

```
<div class="row">    <div class="col-12"></div>    <div class="col-12"></div></div>
```

Le balisage ci-dessus créera des colonnes qui occupent toute la largeur disponible à l'intérieur de la rangée. Les colonnes s'empileront verticalement avec une largeur de 100%.

Ce n'est pas le comportement que nous voulons pour les appareils moyens, nous ajoutons donc les classes de modificateurs, comme ceci :

```
<div class="row">    <div class="col-12 col-md-6"></div>    <div class="col-12 col-md-6"></div></div>
```

Vous voyez ça ?

Notez que pour les plus petits appareils, il n'y a pas besoin de classe de modificateur.

Maintenant, pour les appareils moyens et plus grands, la rangée assumera une largeur de 2 colonnes. L'une occupant 6 colonnes et l'autre 6 colonnes, avec la grille de 12 colonnes de Bootstrap.

Dans la section pratique, je discuterai de la façon de masquer les colonnes sur les petits appareils.

#### Comment cela a-t-il fonctionné ?

Bootstrap a implémenté des media queries avec certains points d'arrêt (breakpoints) pour répondre à chaque besoin adaptatif. Allant des téléphones extra petits aux petits téléphones, tablettes, ordinateurs portables et même des ordinateurs de bureau plus grands — Bootstrap vous couvre.

Comme les classes de marge et de padding que nous avons étudiées plus tôt, il existe une convention de nommage spécifique pour appliquer des styles basés sur la taille d'écran spécifique de l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/EBEJwIxAXlM4KHNDndFiQrOPzbUntVwxiHko)
_Capture d'écran de getbootstrap.com_

Comme on le voit dans l'image ci-dessus, `xs` fait référence aux téléphones extra petits, `sm` fait référence aux petits téléphones, `md` fait référence aux appareils moyens tels que les tablettes, `lg` fait référence aux grands appareils tels que les ordinateurs portables, et `xl` fait référence aux écrans extra larges tels que les grands écrans d'ordinateur de bureau.

Pour les curieux, voici à quoi ressemblent les media queries de Bootstrap :

```
// Appareils extra petits (téléphones en portrait, moins de 576px)// Pas de media query car c'est le réglage par défaut dans Bootstrap// Appareils petits (téléphones en paysage, 576px et plus)@media (min-width: 576px) { ... }// Appareils moyens (tablettes, 768px et plus)@media (min-width: 768px) { ... }// Grands appareils (ordinateurs de bureau, 992px et plus)@media (min-width: 992px) { ... }// Appareils extra grands (grands ordinateurs de bureau, 1200px et plus)@media (min-width: 1200px) { ... }
```

Si vous êtes un utilisateur avancé, jetez un œil à la documentation pour la [version 4](https://getbootstrap.com/docs/4.0/layout/grid/) et la [version 3](https://getbootstrap.com/docs/3.3/css/#grid). Notez la différence dans les points d'arrêt de la grille. J'ai passé du temps à comprendre cela moi-même. Alors, faites de même.

#### Quel est le problème avec `min-width` ?

Vous remarquerez que les media queries de Bootstrap utilisent `min-width`. Vous remarquerez également que dans les exemples précédents, je n'arrêtais pas de dire « appareils moyens et plus grands ».

Par exemple, `col-md` cible les appareils moyens et plus grands. Ainsi, si vous spécifiez une colonne pour occuper 8 colonnes sur les appareils moyens, `col-md-8`, les autres appareils plus grands que les moyens occuperont également la même définition de largeur. Il n'est pas nécessaire d'écrire `col-lg-8` ou `col-xl-8`.

Ce comportement est dû à l'utilisation de `min-width` dans les media queries de Bootstrap.

```
// Appareils moyens (tablettes, 768px et plus)@media (min-width: 768px) { ... }
```

Le bloc de code ci-dessus dit : « pour les appareils qui ont une largeur minimale de `768px`... ». Cela englobe également tous les appareils plus grands que `768px`.

#### Puis-je personnaliser les classes Bootstrap en fonction de tailles d'écran spécifiques ?

Oui, cela peut être fait, mais pas pour chaque classe Bootstrap. Prenons l'exemple du stylisme des textes. Si vous vouliez qu'un morceau de texte apparaisse au centre uniquement sur les téléphones mobiles, comment feriez-vous cela ?

Utilisez la classe `text-sm-center` sur le bloc de texte :

```
<p class="text-sm-center">Comment se fait-il que vous n'ayez pas d'oreilles </p>
```

Le texte, « Comment se fait-il que vous n'ayez pas d'oreilles » apparaîtra normalement dans le flux du document, sauf lorsqu'il est visualisé par un petit téléphone. À ce stade, il sera centré sur l'écran.

### Résumé

Cela a été une section assez enrichissante. Si vous êtes nouveau sur Bootstrap, vous devriez être beaucoup plus à l'aise avec le fonctionnement du framework maintenant. Si vous êtes un habitué, vous avez probablement vu de nouvelles façons dont cette version de Bootstrap diffère de la précédente.

Dans la section suivante, nous passerons à la pratique. Nous afficherons toutes les autres techniques, astuces et nouvelles pépites du framework avec des exemples pratiques.

Comme discuté dans la section « Ce que vous allez apprendre », nous allons commencer à construire la Page d'Accueil de Startup.

![Image](https://cdn-media-1.freecodecamp.org/images/m59-a6E95aRsbD1JMAP5N8VvAZ8aLLPviX8g)

### **Passer à la pratique avec Bootstrap 4**

Haha ! C'est la partie de l'article qui m'excite vraiment. Dans les sections précédentes, j'ai essayé de vous familiariser avec le framework Bootstrap 4, maintenant construisons des projets vraiment cool.

Lorsque nous aurons terminé avec [ce projet](https://codepen.io/ohansemmanuel/full/zEKrxP/), vous devriez avoir réussi à construire une Page de Startup d'une seule page.

#### Ce que vous allez apprendre

En plus d'être la première application réelle des concepts enseignés dans cet article, la construction de ce projet présente certains avantages.

Si vous êtes nouveau sur Bootstrap, je me suis assuré d'aborder les concepts fondamentaux dont vous avez besoin. Pour les développeurs plus expérimentés, cet exemple met en évidence certaines des nouvelles fonctionnalités de Bootstrap 4.

L'exemple montre également comment Flexbox est utilisé dans Bootstrap 4. De plus, certaines choses apparemment simples comme le décalage des colonnes (offsetting) et l'alignement des éléments de bloc au centre sont gérées différemment dans cette version du framework.

Ce sont quelques-unes des choses que nous allons examiner dans cet exemple.

#### Ce dont vous avez besoin pour suivre

Pour une configuration de développement rapide, j'utiliserai [CodePen](https://codepen.io) pour cette démo. C'est tout ce dont vous avez besoin pour suivre.

Pour commencer, nous nous concentrerons sur le viewport initial de la Page d'Accueil de Startup. Il remplit l'écran avec une image d'arrière-plan décente, un bloc de texte et un bouton CTA (Call To Action).

![Image](https://cdn-media-1.freecodecamp.org/images/D-hkyZg6uOvdCHv5bvYvcMdgX1MUf4fT3Nfd)
_viewport initial_

De plus, puisque nous nous concentrerons sur une approche mobile first, il est important de voir comment le design s'affiche sur les appareils mobiles.

Voici la maquette mobile :

![Image](https://cdn-media-1.freecodecamp.org/images/JE9s-5YaJTz05YBf5XwWqaT8tk7S4hTaDXJC)

Comme on le voit dans l'image ci-dessus, tout est à peu près pareil. Le CTA et le paragraphe d'ouverture restent alignés horizontalement au début de la page.

Maintenant que nous comprenons les exigences de conception, commençons par le balisage initial requis.

#### Le balisage initial

Si vous travaillez localement, le balisage initial dont vous avez besoin pour un projet bootstrap décent est celui-ci :

```
<!DOCTYPE html><html lang="fr">  <head>    <!-- Balises meta requises -->    <meta charset="utf-8">    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">    <!-- CSS de Bootstrap -->    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">  </head>
```

```
  <body>     <div class="container"></div>  </body></html>
```

Ne laissez pas le code apparemment complexe vous décourager. Le balisage est assez basique.

Tout d'abord, considérez la balise `meta` :

```
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
```

La balise `meta` existe pour garantir que les pages développées s'affichent correctement sur les appareils mobiles. Si vous définissez des media queries sans cette balise `meta`, vous risquez de ne pas obtenir l'apparence que vous espériez sur les appareils mobiles. Il est important que vous l'incluiez. La balise garantit également que le zoom tactile est pris en compte sur les appareils mobiles.

Curieux de savoir ce que font les attributs `content` et `initial-scale` ? Voir cette [réponse stackoverflow](https://stackoverflow.com/questions/33767533/what-does-the-shrink-to-fit-viewport-meta-attribute-do) bien expliquée.

Deuxièmement, considérez la balise `link` :

```
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
```

La balise `link` ci-dessus est la même que toutes les autres balises `link` que vous avez utilisées dans le passé. Elle inclut l'attribut `href` qui pointe vers le `cdn` de bootstrap.

D'accord, je sais ce que vous pensez. Quels sont les attributs html `integrity` et `crossorigin` ?

![Image](https://cdn-media-1.freecodecamp.org/images/k95U4VtPVvv4Ebk8gc697VLb1DKbxHpb1jUs)

L'attribut `integrity` vérifie la source à partir de laquelle le `cdn` est chargé et garantit que le fichier n'a pas été manipulé. C'est une mesure de sécurité pour s'assurer que vous obtenez ce que vous avez « commandé ». Cela peut sembler trivial, mais pendant longtemps, un inconvénient majeur de l'utilisation d'un CDN était que vous n'aviez aucun contrôle direct sur ce qui se trouvait dans le contenu fourni. Cela pouvait conduire à avoir un code importé non fiable ou altéré.

L'attribut `crossorigin` est présent lorsqu'une requête est chargée à l'aide de « CORS ».

Ne réfléchissez pas trop à ce que sont ces attributs. Continuons.

À ce stade, il est sûr de supposer que vous avez configuré le balisage de base. Notez également que le balisage ci-dessus ne contient aucun lien vers un fichier JavaScript. C'est intentionnel. Plus loin dans cet article, nous pourrons examiner l'ajout d'interactivité à l'aide de JavaScript beaucoup plus tard.

#### Configuration de Codepen

J'utiliserai codepen pour une configuration plus facile. Dans codepen, vous pouvez ajouter les balises meta dans la fenêtre contextuelle des paramètres `html`. Veuillez vous référer à la capture d'écran ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/pwr47w1I6ulGp96U6tK-qwkRq89-glak2ied)
_ajoutez les balises meta et link dans la section « Stuff for <head> »_

Dans votre `html`, allez-y et commencez les choses avec ceci :

```
<h1>Hello World</h1>
```

Si vous avez « Hello World » affiché à l'écran, alors vous êtes prêt à suivre sans aucun problème.

#### Structure initiale du document

L'un des avantages d'une nouvelle API est qu'il n'y a pas vraiment de meilleures pratiques dans ses premières étapes de couverture. On peut dire la même chose pour Bootstrap 4.

Si vous avez travaillé avec Bootstrap dans le passé, vous savez que le balisage de votre projet peut devenir difficile à gérer en un rien de temps. Pour cette raison, j'ai quelques modèles qui fonctionnent bien pour moi. Vous n'avez pas besoin de les adopter, mais ils peuvent certainement faciliter votre travail. Essayez-les.

Lorsque vous regardez le [design final](https://codepen.io/ohansemmanuel/full/zEKrxP/), vous réaliserez qu'il y a des sections de contenu catégorisées.

Il y a une section initiale avec un appel à l'action, une section avec la maquette de l'application, une section qui met en évidence certaines des caractéristiques de l'entreprise, une section de témoignages, et plus encore. Vous avez compris l'idée. En tout, vous devriez avoir 8 sections.

La première règle d'or est d'avoir des couches de contenu séparées à l'aide d'une balise `section` ou de toute autre balise sémantique `html5`. Pourquoi ? Par conception, l'utilisation de Bootstrap signifie que vous aurez beaucoup de `div` dans votre balisage. L'utilisation de la balise `section` rend le balisage un peu plus gérable.

```
<section></section><section></section><section></section><section></section><section></section><section></section><section></section><section></section>
```

Vous devriez commencer par 8 balises comme indiqué ci-dessus.

Maintenant, donnez à chaque balise un `id` unique.

La raison pour laquelle je choisis `id` plutôt que des classes a à voir avec la spécificité et le fait d'avoir un identifiant unique. Vous verrez pourquoi c'est important plus tard.

Je vais nommer les éléments `section` avec des ID pertinents :

```
<section id="introduction"></section><section id="info--1"></section><section id="info--2"></section><section id="info--3"></section><section id="featured-on"></section><section id="feature-rundown"></section><section id="pricing"></section><section id="footer"></section>
```

Maintenant, nous avons 8 balises `section` prêtes à être utilisées à bon escient.

#### Construction du viewport initial

Analysons et construisons la section initiale `section#introduction`.

![Image](https://cdn-media-1.freecodecamp.org/images/rPVxLN3MjTlyeGthatE-TDMbwJKwHL2uU1iA)

Ce que nous avons est une `section` qui remplit le viewport initial de l'utilisateur, avec un message et un appel à l'action (CTA) centrés verticalement et alignés horizontalement au début de la `section`.

Maintenant, appliquons la connaissance des grilles au projet en cours de construction.

![Image](https://cdn-media-1.freecodecamp.org/images/RzE56lgrt60MutLGUOTlGcBybA30FbgAaoP8)
_La section initiale telle qu'elle est vue sur plusieurs appareils_

Le viewport initial aura son balisage interne structuré comme ceci :

```
<section id="introduction">   <div class="container">    <div class="row fill-viewport">       <div class="col-12"></div>    </div>   </div></section>
```

Maintenant, nous avons une structure de base en place.

Notez l'utilisation de la classe de colonne, `.col-12`. Cela garantit que le `div` remplit l'intégralité des 12 colonnes disponibles. L'ajout de la classe `.col-12` signifie qu'à chaque taille d'écran, grande ou petite, le `div` remplira toujours toute la grille de 12 colonnes. Il sera en pleine largeur sur la grille.

Le balisage nécessaire à l'intérieur du `div.col-12` est celui-ci :

```
<h1>Coder sous stéroïdes</h1><p>Arrêtez d'embaucher des ingénieurs pour écrire votre code. Utilisez simplement le script de 1 ko qui résout magiquement tous vos problèmes et algorithmes.</p><a href="#" role="button">Essayez-le hier</a>
```

Ce que vous devriez avoir maintenant est une page nue qui n'a pas l'air très bien.

![Image](https://cdn-media-1.freecodecamp.org/images/iOdSTKs9rCosn2nvByqwtsxFItTmv2wVmEDZ)

#### Rendons cela joli

Il y a quelques choses dont nous avons besoin pour rendre cette interface utilisateur superbe.

(i) Styler `section#introduction`  
`section#introduction` a besoin d'une image d'arrière-plan et doit remplir le viewport de l'utilisateur.

(ii) Positionner correctement le bloc de contenu  
Le bloc de contenu, les blocs de texte, `h1` et `p` contenant « Coder sous stéroïdes... » doivent être parfaitement alignés verticalement au centre.

(iii) Styler l'en-tête et le paragraphe d'introduction (Lead)  
Les éléments `h1` et `p` ont besoin d'un peu de style — aussi basique soit-il.

(iv) Styler le CTA  
Les appels à l'action doivent être lisibles et distincts. L'élément `button` doit également être stylé.

(iv) S'étendre au-delà de la vue mobile  
Enfin, sur les écrans plus grands, le bloc de contenu ne doit PAS remplir toute la largeur disponible mais occuper `50%` de la largeur disponible.

Avec ces points à l'esprit, nous résoudrons ces problèmes avec le moins de styles personnalisés possible, en profitant des styles Bootstrap par défaut là où c'est possible.

Commençons.

#### Solutions

Pour styler `section#introduction` avec une image d'arrière-plan, vous devez écrire un style personnalisé, comme ceci :

```
#introduction {  background: linear-gradient(rgba(100,181,246 ,1), rgba(0,0,0,0.8)), url('http://bit.ly/2fBj6OJ') 0% 0%/cover }
```

Cela donnera à `section#introduction` une image d'arrière-plan subtile surmontée d'un léger dégradé linéaire.

Si vous n'êtes pas sûr de ce que fait le code ci-dessus, l'illustration suivante peut vous aider :

![Image](https://cdn-media-1.freecodecamp.org/images/iMi4vCVjMxjCF4HeF3Ll45lAqIKKcG8EnXGv)
_Un exemple de réglage d'un dégradé et d'une image d'arrière-plan sur un élément._

Il est nécessaire que `section#introduction` remplisse le viewport de l'utilisateur. Bootstrap n'a pas de classe utilitaire à cet effet, nous devons donc écrire la nôtre. La voici :

```
.fill-viewport {  min-height: 100vh }
```

Maintenant, ajoutez cette classe à `section#introduction` comme ceci :

```
<section id="introduction"> <div class="container">   <div class="row fill-viewport">       ...   </div> </div></section>
```

Qu'ai-je fait ici ?

Vous remarquerez que j'ai ajouté `.fill-viewport` au `div.row` et NON au conteneur global, `div.container` ou à `section#introduction`.

C'est très intentionnel. En règle générale, chaque classe utilitaire dont vous avez besoin sur un corps de contenu contenant doit aller dans le `.row`, sauf dans certaines occasions spéciales. C'est ainsi que j'aime travailler. Une autre raison pour laquelle je suis cette règle est qu'elle rend le balisage propre, sans avoir des noms de classes qui sautent partout. Vous avez besoin d'un peu de structure pour écrire du bon code.

Avec cela, vous devriez avoir une `section` qui a l'air plutôt bien.

![Image](https://cdn-media-1.freecodecamp.org/images/onjY0aos-OUrlCi1vxnBlTSlrnnwFRkfhFpE)

Vous avez dû remarquer que le bloc de contenu n'est pas bien positionné. Mettons-le au centre vertical de la page.

C'est le moment idéal pour souligner ceci. Chaque `.row` de Bootstrap 4 est par défaut un `flex-container`.

Je ne saurais trop insister sur l'importance de ce point.

Chaque `.row` de Bootstrap 4 est par défaut un `flex-container`.

Cela ouvre des opportunités qui n'étaient pas disponibles dans les versions précédentes du framework.

Puisque `.row` est un `flex-container`, nous pouvons ajouter la classe utilitaire Bootstrap `align-items-center`. Cela alignera le contenu de chaque `flex-container` au centre.

Appliquez-le comme ceci :

```
<section id="introduction"> <div class="container">   <div class="row fill-viewport align-items-center">       ...   </div> </div></section>
```

Encore une fois, j'ai ajouté cette classe au `.row`.

Voici le résultat de cela :

![Image](https://cdn-media-1.freecodecamp.org/images/QdJXdbYSq6UcF4-p4JzwrGQjtOaFglEKVRxu)

À ce stade, nous faisons des progrès décents.

Bootstrap 4 possède de nombreuses autres classes [utilitaires Flexbox](https://getbootstrap.com/docs/4.0/utilities/flex/). Elles n'ont pratiquement pas besoin de beaucoup d'explications. Les noms de classes sont très descriptifs.

Stylisons les éléments `h1` et `p`.

J'avais pris le temps de discuter des classes utilitaires de texte au début de cet article. Pour styliser ces éléments de texte, faites ceci :

```
<h1 class="text-white">Coder sous stéroïdes</h1><p class="lead">Arrêtez d'embaucher des ingénieurs pour écrire votre code. Utilisez simplement le script de 1 ko qui résout magiquement tous vos problèmes et algorithmes.</p>
```

Comme vous le savez déjà, `text-white` donnera au `h1` une couleur blanche, `.lead` stylisera le paragraphe un peu différemment des autres paragraphes.

![Image](https://cdn-media-1.freecodecamp.org/images/170grQ2mWBkJiX8xwUSFT9OiSiTOLIBs8q3d)

Cela a l'air bien, mais je veux que le paragraphe ait une couleur légèrement plus pâle. À cet effet, nous allons écrire une autre classe utilitaire :

```
.text-white-70 {  color: rgba(255,255,255,0.7)}
```

Cela donnera au texte une couleur blanche légèrement transparente.

Allez-y et utilisez cette classe sur le paragraphe d'introduction comme ceci :

```
<p class="lead text-white-70">Arrêtez d'embaucher des ingénieurs pour écrire votre code. Utilisez simplement le script de 1 ko qui résout magiquement tous vos problèmes et algorithmes.</p>
```

Et maintenant vous devriez avoir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/WViFBQQXiJ2-hP0Kv4QPXMqu0xZeTgjawACt)

Notez comment nous extrayons de minuscules fonctionnalités dans des classes CSS réutilisables. C'est vraiment important pour la réutilisabilité.

Le bouton n'est toujours pas stylé. Nous devons corriger cela.

Les boutons dans Bootstrap sont stylés à l'aide de la classe `.btn`. Il existe quelques variations en ce qui concerne la couleur. Par exemple `.btn-primary` et `.btn-secondary` donneront respectivement un bouton bleu et un bouton gris.

![Image](https://cdn-media-1.freecodecamp.org/images/KgRZDhT9YVjZkI3YxkeVOM4zL2dwF8lCefR6)
_[https://getbootstrap.com/docs/4.0/components/buttons/](https://getbootstrap.com/docs/4.0/components/buttons/" rel="noopener" target="_blank" title=")_

Pour styler le lien, faites ceci :

```
<a class="btn btn-primary" href="#" role="button">Essayez-le hier</a>
```

![Image](https://cdn-media-1.freecodecamp.org/images/l4GqM-94xG9NJ9gyCGKNSVKJg-JXOVeDOauY)

À ce stade, nous avons une `section` qui a l'air bien sur mobile, mais pas si géniale sur les appareils plus grands. Réparons cela.

Bootstrap suit l'approche de développement mobile first largement acceptée. Cela signifie que vous construisez d'abord pour les appareils mobiles, puis vous adaptez le design à des tailles d'écran encore plus grandes. C'est ce que nous allons faire maintenant.

Lors de la définition de la grille contenante dans la `section#introduction`, nous avons fait exactement cela.

```
<div class="col-12">   ....</div>
```

En écrivant cela, nous avons dit : « Oh Bootstrap, laisse ce `div` remplir toute la largeur de 12 colonnes sur toutes les tailles d'écran ». C'est bien — dans l'esprit de la conception à partir d'une perspective mobile first.

Maintenant, faisons en sorte que la colonne occupe la moitié de la largeur sur les appareils plus grands. Vous faites cela comme ceci :

```
<div class="col-12 col-md-6">     ...</div>
```

Maintenant, ce que nous avons dit est ceci : « Oh Bootstrap, par défaut, laisse ce div remplir toute la largeur de 12 colonnes, MAIS laisse le div occuper 6 colonnes sur les appareils plus grands ».

12 divisé par deux, égale 6. Par conséquent, la colonne occupera la moitié de l'espace disponible sur les appareils plus grands.

![Image](https://cdn-media-1.freecodecamp.org/images/aqGYJRDcy5tMiGUoMIYBxiNDZjpcNiSk6dEc)

Cela conclut le développement du viewport initial.

Passons à la section suivante.

#### Construction de la section des détails de la startup

La section suivante est assez intéressante. Voici comment elle s'affiche sur les grands, moyens et petits appareils :

![Image](https://cdn-media-1.freecodecamp.org/images/dz6h9AbOpqJsVR3r6Ee8AxMyvqoURj0IVrt6)

Sur les appareils mobiles, l'utilisateur voit une colonne en pleine largeur avec des morceaux de textes importants. Sur les tablettes, plus de texte est affiché, ainsi qu'un aperçu de l'application sur le côté. Cela donne 2 colonnes de largeur égale.

Sur les appareils plus grands, encore plus de texte est affiché, et l'aperçu de l'application mobile reste également.

Maintenant, construisons cela.

Par convention, nous adopterons un design mobile first. Concevez d'abord pour les appareils mobiles.

Remplissez la `section#info--1` avec le balisage suivant :

```
<section id="info--1">  <div class="container">    <div class="row pt-5 align-items-center">      <div class="col-12">        <h6 class="text-uppercase text-black-40">          info à un million de dollars        </h6>        <h2>Nous faisons ce que nos concurrents font, mais avec 500 % de plus</h2>        <p>Sed ut perspiciatis unde omnis iste natus error        sit voluptatem accusantium doloremque laudantium,        totam rem aperiam..</p>     </div>    </div>  </div></section>
```

Vous remarquerez que j'ai glissé beaucoup plus de choses ici. Laissez-moi vous expliquer.

Considérez le `.row` :

```
<div class="row pt-5 align-items-center"></div>
```

À l'intérieur de la `row`, il y a une colonne représentée par :

```
<div class="col-12">...</div>
```

`col-12` garantit que le `div` s'étend sur toute la largeur, 12 colonnes par défaut.

Il y a deux classes supplémentaires dans le `.row` avec lesquelles vous devriez être familier. `pt-5` ajoute un padding top au `div` et `align-items-center` garantit que les flex-items sont centrés verticalement.

N'oubliez pas que dans Bootstrap 4, chaque `row` est un `flex-container`.

Le bloc de code suivant représente les blocs de texte :

```
<h6 class="text-uppercase text-black-40">info à un million de dollars</h6><h2>Nous faisons ce que nos concurrents font, mais avec 500 % de plus</h2> <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem  accusantium doloremque laudantium,totam rem aperiam..</p>
```

`text-uppercase` est une classe utilitaire bootstrap pour faire apparaître le texte en majuscules.

`text-black-40` est une autre petite classe qui donne au texte une couleur noire avec une opacité de `40 %`.

```
.text-black-40 {  color: rgba(0,0,0,0.4)}
```

Et avec cela, vous devriez avoir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/BKtjqaA9lhfl6iL5nkWpIaYPMSN2QHne2qfz)

Cela a l'air bien sur mobile. Maintenant, corrigeons l'affichage sur les appareils plus grands.

Pour les appareils moyens, nous avons besoin de deux colonnes. L'une pour abriter la maquette de l'application, et l'autre pour le bloc de texte.

Le bloc de code ci-dessous met en évidence la solution. Allez-y et ajoutez l'image dans une nouvelle colonne juste à l'intérieur du `.row` mais au-dessus du bloc de texte.

```
<section id="info--1">  <div class="container">    <div class="row pt-5 align-items-center">       <div class="col d-none d-md-block align-self-end">         <img src="http://bit.ly/2fyUtlS" class="img-fluid"/>       </div>       <div class="col">        <h6 class="text-uppercase text-black-40">          info à un million de dollars        </h6>        <h2>Nous faisons ce que nos concurrents font, mais avec 500 % de plus</h2>        <p>Sed ut perspiciatis unde omnis iste natus error        sit voluptatem accusantium doloremque laudantium,        totam rem aperiam..</p>     </div>    </div>  </div></section>
```

Le nouveau bloc de code qui inclut l'image est celui-ci :

```
<div class="col d-none d-md-block align-self-end">    <img src="http://bit.ly/2fyUtlS" class="img-fluid"/></div>
```

Il y a quelques nouvelles classes utilitaires Bootstrap là-dedans. Jetons un coup d'œil.

Les noms de classes commençant par `d-` représentent des classes d'affichage (display).

`d-none` masquera tout élément auquel il est appliqué, tandis que `d-block` affichera l'élément en lui donnant un `display: block`. Ainsi, l'application des classes `d-none` et `d-md-block` dit : « Hé Bootstrap, masque cet élément par défaut, mais affiche l'élément sur les appareils moyens `md` ».

De plus, `align-self-end` s'assurera que l'élément est aligné au bas du conteneur flex verticalement. Quelques pépites Flexbox ici !

Il y a un autre changement que vous n'avez peut-être pas remarqué.

Nous avons maintenant 2 colonnes chacune avec le nom de classe `.col`. Au lieu d'avoir les deux colonnes avec le nom de classe `col-12`, changez cela en juste `.col`.

```
<section id="info--1">  <div class="container">    <div class="row pt-5 align-items-center">       <div class="col d-none d-md-block align-self-end">         <img src="http://bit.ly/2fyUtlS" class="img-fluid"/>       </div>       <div class="col">        <h6 class="text-uppercase text-black-40">          info à un million de dollars        </h6>        <h2>Nous faisons ce que nos concurrents font, mais avec 500 % de plus</h2>        <p>Sed ut perspiciatis unde omnis iste natus error        sit voluptatem accusantium doloremque laudantium,        totam rem aperiam..</p>     </div>    </div>  </div></section>
```

Lorsque vous avez un nombre quelconque d'éléments ayant la classe `.col`, ils occuperont la largeur disponible dans des dimensions égales.

Dans ce cas, le bloc d'image et la zone de contenu occuperont `50 %` de la largeur disponible. Si vous aviez trois éléments à l'intérieur d'un `.row` avec chacun ayant la classe `.col`, ils prendraient chacun `30 %` de la largeur disponible. Je suis sûr que vous comprenez maintenant.

Voici le résultat que vous devriez avoir à ce stade :

![Image](https://cdn-media-1.freecodecamp.org/images/lxD-9chjTFNHKuyngaReglg5h62xfyPDmxW3)

Nous en avons presque fini avec cette `section` à l'exception des blocs de texte supplémentaires sur les appareils plus grands. Réparons cela.

Puisque les colonnes peuvent être imbriquées, nous pouvons inclure une autre colonne pour abriter le bloc de texte côte à côte sur les grands appareils.

Cela devrait aller à l'intérieur de la deuxième colonne, et sous le dernier bloc de texte :

```
<!-- les colonnes peuvent être imbriquées --> <div class="row">   <div class="d-none d-md-block col">      <h5>fonctionnalité tueuse</h5>       <p>veritatis et quasi architecto beatae vitae       dicta sunt explicabo.</p>       <a href="#" class="d-block">en savoir plus</a>    </div>    <div class="d-none d-lg-block col">       <h5>deuxième fonctionnalité tueuse</h5>        <p>veritatis et quasi architecto beatae vitae        dicta sunt explicabo.</p>        <a href="#" class="d-block">en savoir plus</a>    </div> </div>
```

Vous remarquerez à nouveau l'utilisation des classes utilitaires d'affichage. Par défaut, les deux `div` à l'intérieur de la `row` sont masqués avec `d-none`. Par conséquent, ils ne s'afficheront pas sur les appareils mobiles. Le nom de classe `col` garantit qu'ils prennent tous deux des espaces égaux. Cependant, le deuxième bloc de texte ne sera affiché que sur les appareils plus grands avec `.d-lg-block`.

Puisque Bootstrap emploie une approche mobile first par conception, le premier bloc de texte avec la classe de `d-md-block` sera également visible sur les grands appareils.

« afficher sur mobile » est synonyme de « afficher sur tous les appareils ».
« afficher sur les appareils moyens » signifie également « afficher sur les appareils moyens et tout ce qui est plus grand ».

J'espère vraiment que vous avez compris cela.

Voici le résultat jusqu'à présent :

![Image](https://cdn-media-1.freecodecamp.org/images/5-mbvJwziITFrIuEktkHitXNdXDjkuSPZYDY)

Passons à la section suivante !

#### Construction de la section à propos

La troisième section a à peu près la même ambiance que la deuxième section dont j'ai discuté ci-dessus. Il y a quelques différences subtiles :

1. L'utilisation des balises `pre`
2. Un changement dans l'ordre des colonnes lors de l'affichage sur les appareils mobiles.

![Image](https://cdn-media-1.freecodecamp.org/images/UppceStd-DIWXre2JSQsix9kCkZfOiaeNtKJ)
_Le bloc de code apparaît en premier lorsqu'il est visualisé sur mobile. Sur les appareils plus grands, l'affichage est permuté avec le bloc de code apparaissant en dernier._

Voici le code complet qui compose la section :

```
<section id="info-2" class="bg-dark"> <div class="container">   <div class="row align-items-center fill-80-viewport">     <div class="col-12 col-md-6 my-5 order-2 order-md-1">       <p class="text-uppercase text-white-40"><strong>développement plus rapide</strong></p>       <h2 class="text-white">Coder n'a jamais été aussi rapide. C'est presque magique</h2>       <p class="lead text-white-70">Arrêtez d'embaucher des ingénieurs pour écrire votre code. Installez simplement un script qui résout magiquement tous vos problèmes.</p>       <a class="btn btn-light d-block d-md-inline-block py-3" href="#" role="button">Lire la documentation</a>     </div>     <pre class="col-12 col-md-6 my-5 order-1 order-md-2 py-4 border border-info rounded text-info">      <span>1</span> <span> //codingSteroids.js</span>       <span>2</span>      <span>3</span>   const data = {      <span>4</span>        "purpose": {      <span>5</span>        "getId": "#element",      <span>6</span>        "companyName": "coolStartup",      <span>7</span>      }      <span>8</span>    }      <span>9</span>           <span>10</span>   function codingSteroids(        <span>11</span>       data,      <span>12</span>       getSteroidsType      <span>13</span>   )       <span>14</span>           <span>15</span>   function getSteroidsType() {      <span>16</span>     return "codeHellish!"      <span>17</span>   }      </pre>   </div> </div></section>
```

Vous pourriez être tenté de penser que le bloc de code représenté ci-dessus est complexe. Pourtant, après un examen attentif, il ne l'est pas vraiment.

Comme toujours, la section commence par un balisage familier :

```
<section id="info-2" class="bg-dark"> <div class="container">   <div class="row align-items-center fill-80-viewport">     ...   </div> </div></section>
```

Je donne toujours un `Id` aux sections. De plus, à l'intérieur de la `row` se trouvent deux colonnes :

```
<section id="info-2" class="bg-dark"> <div class="container">   <div class="row align-items-center fill-80-viewport">     <div class="col-12">     </div>     <pre class="col-12">     </pre>   </div> </div></section>
```

Par défaut, les deux colonnes ont été configurées pour occuper les 12 colonnes disponibles. Par conséquent, elles s'empileront verticalement l'une sur l'autre.

Sur les appareils moyens et plus grands, les colonnes occupent une largeur de colonne égale :

```
<section id="info-2" class="bg-dark"> <div class="container">   <div class="row align-items-center fill-80-viewport">     <div class="col-12 col-md-6">     </div>     <pre class="col-12 col-md-6">     </pre>   </div> </div></section>
```

Vous devriez y être habitué maintenant :)  
`.bg-dark` donne à la section un arrière-plan sombre. Contenu dans la section se trouve un `container` et une `row` imbriquée.

`align-items-center` est une classe utilitaire Flexbox qui aligne le contenu de la `row` au centre vertical. N'oubliez pas que chaque `row` est par défaut un `flex-container`.

`fill-80-viewport` est une petite classe que j'ai écrite comme ceci :

```
.fill-80-viewport {  min-height: 80vh}
```

La classe `.fill-80-viewport` garantit que la section occupe `80 %` de la hauteur du viewport de l'utilisateur.

Alors, voici les nouvelles choses dont nous n'avons pas discuté :

```
<section id="info-2" class="bg-dark"> <div class="container">   <div class="row align-items-center fill-80-viewport">     <div class="col-12 order-2 order-md-1">     </div>     <pre class="col-12 order-1 order-md-2">     </pre>   </div> </div></section>
```

En supposant que vous soyez familier avec le fonctionnement de Flexbox, la propriété `order` détermine l'ordre visuel dans lequel les `flex-items` sont affichés. L'élément avec la valeur `order` la plus basse est affiché en premier et la plus `haute` en dernier. Essentiellement, les éléments sont affichés en termes de valeurs `order` croissantes — de la plus basse à la plus haute.

Les noms de classes `order-` sont une tentative de recréer ce même comportement. Ce sont des classes utilitaires Flexbox de Bootstrap qui permettent toutes les valeurs entières telles que `order-5` et `order-10`.

Un élément avec la classe `order-2` a une valeur d'ordre plus élevée qu'un élément avec `order-1`. Vous l'avez deviné. Plus la valeur entière est élevée, plus la valeur `order` est élevée.

Les noms de classes d'ordre ont également des variations adaptatives. Ainsi `order-md-1` aura une valeur d'ordre de 1 lorsqu'il est visualisé sur un appareil de taille moyenne ou plus grande. Par conséquent, `order-md-2` aura une valeur `order` de `2` lorsqu'il est visualisé sur un appareil de taille moyenne ou plus grande.

À la lumière de cela, vous devriez être en mesure de comprendre ceci :

```
<div class="col-12 order-2 order-md-1"></div><pre class="col-12 order-1 order-md-2"></pre>
```

Par défaut, la balise `pre` sera affichée en premier, puis le `div`. C'est parce que `order-1` est affiché en premier, puis `order-2` en termes de valeurs `order` croissantes. Lorsqu'il est visualisé sur des appareils plus grands, le contenu à l'intérieur du `div` sera affiché en premier, suivi du contenu à l'intérieur des balises `pre`.

![Image](https://cdn-media-1.freecodecamp.org/images/gA8Zh41UhbS907ZNxCv8I8rVzErRI9QFzM8U)
_Lorsqu'il est visualisé sur des appareils plus grands, le contenu à l'intérieur du `div` sera affiché en premier, suivi du contenu à l'intérieur des balises `pre`._

Le reste du balisage qui compose la section n'est pas difficile à comprendre. Il est largement basé sur les classes utilitaires de texte et d'espacement que nous avons déjà passé tant de temps à examiner.

Passons à la section de contenu suivante.

#### Construction de la section de témoignages

![Image](https://cdn-media-1.freecodecamp.org/images/dd1KwRS6BfpUipnw7n5r2oK4PYFJeYMiR6Xl)
_La section de témoignages telle qu'elle est affichée sur mobile et sur les appareils plus grands._

Si vous avez suivi, il devrait être évident que celle-ci est très similaire à la première section de contenu.

Elle est composée d'une colonne. La colonne se trouve sur le côté droit sur les appareils plus grands, mais reste alignée au début sur les plus petits appareils. Voici le balisage qui alimente cette section :

```
<section id="info-3">  <div class="container">    <div class="row fill-80-viewport align-items-center justify-content-end text-white">      <div class="col-12 basis-md-50">        <h6 class="text-white-40">          ce que les autres pensent        </h6>        <h3>« Coding on Steroids est époustouflant. Je me concentre moins sur l'écriture de code tout en prenant des photos de mode à travers le monde. »</h3>        <p class="text-uppercase text-white-70">Fondateur, La Startup Ocumpious</p>      </div>  </div>  </div></section>
```

Plutôt simple, non ?

`align-items-center` et `justify-content-end` font exactement ce qu'ils disent. La colonne unique qui représente le `flex-item` sera alignée au centre vertical et à la fin horizontale.

Par défaut, cette colonne remplit tout l'espace disponible avec `.col-12`. Cependant, sur les appareils moyens et plus grands, elle n'occupe que `50 %` de la largeur disponible.

`basis-md-50` est une petite classe que j'ai écrite comme ceci :

```
@media screen and (min-width: 768px ){  .basis-md-50 {    flex-basis: 50%  }  }
```

Lorsque la colonne occupe `100 %` de la largeur disponible, elle ne peut pas vraiment être forcée vers la fin. Vous n'obtenez aucun retour visuel à ce sujet. Cependant, lorsque la largeur de la colonne est réduite à `50 %`, cela devient évident.

C'est l'astuce pour déplacer la colonne vers la droite — sur les appareils plus grands.

Passons à la section suivante.

#### Construction de la section en vedette

![Image](https://cdn-media-1.freecodecamp.org/images/DHsfphtJHtuCoMSN483pg2pVTGsCzFbNtkKG)
_Cette section contient une liste d'icônes, centrées horizontalement dans la section._

Celle-ci ressemble à un jeu d'enfant. C'est vraiment simple.

Le balisage consiste en une liste d'icônes font-awesome.

```
<section id="featured-on" class="bg-primary">  <div class="container">    <div class="row py-5 text-center text-white">      <div class="col-12">          <i class="fa fa-3x fa-free-code-camp my-3 mx-5"              aria-hidden="true"></i>          <i class="fa fa-3x fa-twitter my-3 mx-4"              aria-hidden="true"></i>          <i class="fa fa-3x fa-facebook my-3 mx-4"              aria-hidden="true"></i>          <i class="fa fa-3x fa-quora my-3 mx-4"              aria-hidden="true"></i>          <i class="fa fa-3x fa-reddit my-3 mx-4"              aria-hidden="true"></i>          <i class="fa fa-3x fa-pied-piper my-3 mx-4"              aria-hidden="true"></i>          <i class="fa fa-3x fa-paypal my-3 mx-4"              aria-hidden="true"></i>          <i class="fa fa-3x fa-product-hunt my-3 mx-4"              aria-hidden="true"></i>      </div>    </div>  </div></section>
```

La classe `.text-center` garantit que ces icônes sont toujours centrées horizontalement. Cette section utilise une grande quantité de classes d'espacement. Voyez-vous `my-3`, `mx-4` et `py-5` dans le balisage ci-dessus ?

Ce sont des noms de classes avec lesquels vous êtes déjà familier, n'est-ce pas ?

Oui !

Passons à la section de contenu suivante.

#### Construction de la section des fonctionnalités du produit

![Image](https://cdn-media-1.freecodecamp.org/images/wzc8fBOzq7IRB3FWMdffT3jHKq5KjNjxzNm8)
_Une section contenant un en-tête et quelques fonctionnalités alignées dans plusieurs colonnes._

Le balisage complet de cette section est visible ci-dessous :

```
<section id="feature-rundown">  <div class="container">    <div class="row mt-5">      <div class="col-12 col-md-6 mx-auto mt-5 text-center">        <h6 class="text-black-40 text-uppercase">          La vérité amère        </h6>        <h3 class="text-black-70">Sur une échelle de 1 à 10, nous vous facilitons la vie à 10/10, point final.</h3>      </div>    </div>    <div class="row mb-5">        <div class="col-12 col-md-4 text-center">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Support 24/7</strong> Pour            votre bien, nous ne dormons pas.          </p>        </div>        <div class="col-12 col-md-4 text-center">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Rapide</strong> Comme l'éclair.          </p>        </div>        <div class="col-12 col-md-4 text-center">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Fiable</strong> Nous n'avons jamais d'interruption de serveur.          </p>        </div>        <div class="col-12 col-md-4 text-center">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Analyse computationnelle</strong> comme aucune autre.          </p>        </div>        <div class="col-12 col-md-4 text-center">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Analytique</strong> comme aucune autre.          </p>        </div>        <div class="col-12 col-md-4 text-center mb-5">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Abordable</strong> comme un café.          </p>        </div>    </div>  </div></section>
```

Bien que cela puisse paraître complexe, c'est vraiment simple quand on l'examine de près.

Comme les autres sections, celle-ci commence par donner à la section un `id` et par y imbriquer un `container`.

```
<section id="feature-rundown">  <div class="container">    ...  </div></section>
```

Contrairement aux autres sections, celle-ci contient 2 rangées imbriquées.

```
<section id="feature-rundown">  <div class="container">    <div class="row">    </div>    <div class="row">    </div>  </div></section>
```

La première rangée contient le titre de la section :

![Image](https://cdn-media-1.freecodecamp.org/images/K5tCfp3ZnbUQ6MPCiJoTIZPyxhJ51jlglJBC)
_Le titre mis en évidence._

La deuxième rangée contient la liste des icônes d'image :

![Image](https://cdn-media-1.freecodecamp.org/images/iW-DJY-TLFvnxwjPoID-aAGaVCQT-xOVAyUz)
_La liste d'icônes mise en évidence._

Voici le contenu de la première rangée :

```
<div class="col-12 col-md-6 mx-auto mt-5 text-center">        <h6 class="text-black-40 text-uppercase">          La vérité amère        </h6>        <h3 class="text-black-70">Sur une échelle de 1 à 10, nous vous facilitons la vie à 10/10, point final.</h3></div>
```

Par défaut, elle occupe toute la largeur disponible de la rangée `col-12`. Sur les appareils moyens, elle occupe la moitié de la largeur `col-md-6` et elle est centrée horizontalement `mx-auto`.

Les autres noms de classes sont des choses que vous connaissez déjà.

Pour plus de clarté, `text-black-40` et `text-black-70` sont de petites classes que j'ai écrites comme ceci :

```
.text-black-70 {   color: rgba(0,0,0,0.7) } .text-black-40 {   color: rgba(0,0,0,0.4) }
```

D'autre part, la deuxième `row` contient une liste d'images et de textes associés :

```
<div class="col-12 col-md-4 text-center">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Support 24/7</strong> Pour            votre bien, nous ne dormons pas.          </p>        </div>        <div class="col-12 col-md-4 text-center">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Rapide</strong> Comme l'éclair.          </p>        </div>        <div class="col-12 col-md-4 text-center">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Fiable</strong> Nous n'avons jamais d'interruption de serveur.          </p>        </div>        <div class="col-12 col-md-4 text-center">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Analyse computationnelle</strong> comme aucune autre.          </p>        </div>        <div class="col-12 col-md-4 text-center">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Analytique</strong> comme aucune autre.          </p>        </div>        <div class="col-12 col-md-4 text-center mb-5">          <img src="http://bit.ly/2yE6Z8h" class="mt-4"/>          <p>            <strong class="text-info">Abordable</strong> comme un café.          </p>        </div>
```

Par défaut, les colonnes remplissent l'espace disponible, occupent un tiers de l'espace disponible sur les appareils moyens ou plus grands, et le texte et les images sont alignés au centre, `col-12 col-md-4 text-center`.

La classe `text-info` sur la balise `<strong>` donne au texte une couleur de type bleu sarcelle.

C'est à peu près tout ce qu'il y a à dire sur cette section.

Passons à la suivante.

#### Construction de la section des tarifs

![Image](https://cdn-media-1.freecodecamp.org/images/xssqpQU2E2wttWxOOrcoiyQA9p-TKCHejk0i)
_Cette section contient une grille de tarifs._

Les tableaux de tarifs sont très importants — si vous voulez que votre entreprise gagne de l'argent. Voyons comment en construire un.

Le balisage complet de cette section est ci-dessous :

```
<section id="pricing" class="bg-light">    <div class="container fill-80-viewport">        <div class="row">          <div class="col-12 col-md-6 mx-auto text-center my-5">              <h6 class="text-black-40 text-uppercase">                tarifs              </h6>              <h3 class="text-black-70">nous sommes très abordables</h3>            </div>        </div>   
```

```
<div class="row pb-5">        <div class="col-12 col-md-4 px-2 my-4 text-center">        <h6 class="text-black-40 text-uppercase">            Personnel          </h6>        <img src="http://bit.ly/2y9EpP2" alt="9 $ par mois" class="my-4"/>        <p>Puissance suffisante</p>        <ul class="list-unstyled list-border-black-20 list-border-y text-left text-black-70">               <li class="py-2"><strong>10k</strong> requêtes mensuelles</li>          <li class="py-2"><strong>9h-17h</strong> support technique</li>          <li class="py-2">Accès API <strong>Public</strong></li>        </ul>        <a class="btn btn-block btn-primary border-0 text-white py-3" href="#">Démarrer</a>        </div>                   <div class="col-12 col-md-4 px-2 my-4 text-center">          <h6 class="text-black-40 text-uppercase">              Entreprise            </h6>          <img src="http://bit.ly/2xKjVeS" alt="49 $ par mois" class="my-4">          <p>Parfait pour les petites entreprises.</p>          <ul class="list-unstyled  list-border-black-20 list-border-y text-left text-black-70">                 <li class="py-2"><strong>100k</strong> requêtes mensuelles</li>            <li class="py-2"><strong>9h-17h</strong> support technique</li>            <li class="py-2">Accès API <strong>Public et Privé</strong></li>          </ul>          <a class="btn btn-block btn-primary border-0 text-white py-3" href="#">Démarrer</a>        </div>                  <div class="col-12 col-md-4 px-2 my-4 text-center">          <h6 class="text-black-40 text-uppercase">              Corporatif            </h6>          <img src="http://bit.ly/2wjsVEl" alt="119 $ par mois" class="my-4"/>          <p>Super pouvoirs illimités</p>          <ul class="list-unstyled list-border-black-20 list-border-y text-left text-black-70">                 <li class="py-2"><strong>10 000k</strong> requêtes mensuelles</li>            <li class="py-2"><strong>9h-17h</strong> support technique</li>            <li class="py-2">Accès API <strong>Public et Privé</strong></li>          </ul>          <a class="btn btn-block btn-primary border-0 text-white py-3" href="#">Démarrer</a>        </div>      </div>      </div>  </section>
```

Cela a l'air complexe ?

Ne vous inquiétez pas. Laissez-moi vous expliquer.

La section commence par un conteneur imbriqué et deux rangées :

```
<section id="pricing" class="bg-light">    <div class="container fill-80-viewport">        <div class="row">        </div>        <div class="row">        </div>    </div></section> 
```

Comme toujours, la `section` a un `id`. La classe `bg-light` donne à la section une couleur d'arrière-plan claire.

Le conteneur a été configuré pour remplir au moins `80 %` de la hauteur du viewport disponible. J'ai fait cela plusieurs fois, cela ne devrait pas être étrange :

```
.fill-80-viewport {  min-height: 80vh}
```

À l'intérieur de la première rangée se trouve le titre de la section :

```
<div class="col-12 col-md-6 mx-auto text-center my-5">     <h6 class="text-black-40 text-uppercase">         tarifs     </h6>     <h3 class="text-black-70">nous sommes très abordables</h3></div>
```

Les en-têtes sont imbriqués dans une colonne qui remplit l'espace disponible sur les appareils mobiles tout en occupant la moitié de la largeur disponible pour les appareils moyens ou plus `col-12 col-md-6`. La colonne est également stylisée pour centrer son contenu textuel `text-center` et elle se trouve au centre de la largeur disponible `mx-auto`.

Les noms de classes `text-black-40` et `text-black-70` sont de petites classes que j'ai écrites comme ceci :

```
.text-white-40 {  color: rgba(255,255,255,0.4)}.text-white-70 {  color: rgba(255,255,255,0.7)}
```

À l'intérieur de la deuxième `row` se trouvent les tableaux de tarifs.

Chaque tableau de tarifs est composé de ceci :

```
<div class="col-12 col-md-4 px-2 my-4 text-center">        <h6 class="text-black-40 text-uppercase">            Personnel          </h6>        <img src="http://bit.ly/2y9EpP2" class="my-4"/>        <p>Puissance suffisante</p>        <ul class="list-unstyled list-border-black-20 list-border-y text-left text-black-70">               <li class="py-2"><strong>10k</strong> requêtes mensuelles</li>          <li class="py-2"><strong>9h-17h</strong> support technique</li>          <li class="py-2">Accès API <strong>Public</strong></li>        </ul>        <a class="btn btn-block btn-primary border-0 text-white py-3" href="#">Démarrer</a></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/hPOrAhEde0h43LP0A3PH8YStoSdyz5dbOsOp)
_Une décomposition des composants de la grille de tarifs._

C'est essentiellement un en-tête, une image, une liste non ordonnée de fonctionnalités avec un bouton CTA.

Dupliquez cela à trois endroits et vous avez la grille de tarifs à 3 colonnes. Vous voyez comment le balisage est devenu gérable ?

La plupart des noms de classes devraient vous être familiers. Mais regardez ceci :

```
...<ul class="list-unstyled list-border-black-20 list-border-y text-left text-black-70">    ... </ul>
```

`list-unstyled` est une classe bootstrap qui supprime le padding et le style de liste qui viennent par défaut avec les listes non ordonnées `ul`.

Et ceux-ci :

```
list-border-black-20,  list-border-y
```

`list-border-y` est une petite classe que j'ai écrite pour ajouter des bordures uniquement en haut et en bas d'un élément de liste.

```
.list-border-y li {  border-top: 1px solid}.list-border-y li:last-child {  border-bottom: 1px solid}
```

C'est ce qui donne aux listes à l'intérieur du tableau de tarifs les bordures de `1px`.

![Image](https://cdn-media-1.freecodecamp.org/images/Bupr9weqP1vm0tlhQeMP4yC7Q8ha4RMOxIac)
_Les bordures de 1px autour des éléments de la liste._

`list-border-black-20` est une autre petite classe qui donne aux bordures une couleur noire transparente.

Ces classes ne sont pas fournies avec bootstrap, nous devons donc écrire les nôtres.

```
.list-border-black-20 li,.list-border-black-20 li:last-child{  border-color: rgba(0,0,0,0.2)}
```

Maintenant, cela fait apparaître la couleur des bordures comme un noir transparent subtil.

C'est à peu près tout ce qu'il y a à dire sur cette section de contenu. Voyons la suivante.

#### Construction du pied de page (footer)

![Image](https://cdn-media-1.freecodecamp.org/images/s5Tvf24syhAkrRQ9TXRhyYMWSa439iwLpv-E)
_La section du pied de page._

C'est la dernière section de contenu pour cette page, et elle représente le pied de page de la page.

Le code complet de cette section est présenté ci-dessous :

```
<section id="footer" class="bg-dark">  <div class="container">    <div class="row fill-40-viewport py-5 text-white-70 align-items-center">        <div class="col-12 col-md-6">          <ul class="list-unstyled">            <li><h6 class="text-white">À PROPOS</h6></li>            <li>Nous travaillons sur Coding on Steroids               toute notre vie.               Une technologie révolutionnaire mérite un tel dévouement, n'est-ce pas ?               Si vous souhaitez en savoir plus, ou si vous êtes intéressé par un emploi,               contactez-nous à tout moment sur               <a class="text-white" href="https://twitter.com/OhansEmmanuel" target="_blank">@ohansemmanuel</a></li>          </ul>        </div>        <div class="col-12 col-md-2">          <ul class="list-unstyled">            <li><h6 class="text-white">PRODUIT</h6></li>            <li>Fonctionnalités</li>            <li>Exemples</li>            <li>Tour</li>            <li>Galerie</li>          </ul>        </div>        <div class="col-12 col-md-2">          <ul class="list-unstyled">            <li><h6 class="text-white">APIS</h6></li>            <li>Données riches</li>            <li>Simple</li>            <li>Temps réel</li>            <li>Social</li>          </ul>        </div>        <div class="col-12 col-md-2">        <ul class="list-unstyled">          <li><h6 class="text-white">LÉGAL</h6></li>          <li>Conditions</li>          <li>Juridique</li>          <li>Confidentialité</li>          <li>Licence</li>        </ul>      </div>       </div>  </div> </section>
```

Maintenant, analysons-le.

Tout est simple lorsqu'on le décompose en petits morceaux.

La `section` commence par un `container` et une rangée imbriqués.

```
<section id="footer" class="bg-dark">  <div class="container">    <div class="row">    </div>  </div></section>
```

Comme toujours, j'ai donné un `id` à la section. La classe `bg-dark` donnera au pied de page un arrière-plan sombre.

À l'intérieur de cette colonne se trouvent quatre colonnes.

![Image](https://cdn-media-1.freecodecamp.org/images/IubwF14ksU0SrdIVKYOAREYIVpTU7IAB5mzm)
_Les quatre colonnes qui composent le pied de page._

```
<div class="col-12 col-md-6"></div><div class="col-12 col-md-2"></div><div class="col-12 col-md-2"></div><div class="col-12 col-md-2"></div>
```

Chaque colonne occupera l'espace disponible lorsqu'elle sera visualisée sur des appareils mobiles `col-12`.

La première colonne occupe la moitié de la largeur disponible sur les appareils moyens et plus grands `col-md-6`, tandis que les autres colonnes occupent un tiers de l'espace restant divisé par deux disponible `col-md-2`. La grille totalise finalement 12. `6 + 2 + 2 + 2 = 12`.

À l'intérieur de la première colonne se trouve une liste non ordonnée et un tas d'éléments de liste. `list-unstyled` garantit que l'espacement par défaut et le style de liste sont supprimés de l' `ul`.

```
<ul class="list-unstyled">   <li><h6 class="text-white">À PROPOS</h6></li>   <li>Nous travaillons sur Coding on Steroids        toute notre vie.        Une technologie révolutionnaire mérite un tel dévouement, n'est-ce pas ?         Si vous souhaitez en savoir plus, ou si vous êtes intéressé par un emploi,        contactez-nous à tout moment sur        <a class="text-white" href="https://twitter.com/OhansEmmanuel" target="_blank">@ohansemmanuel</a></li></ul>
```

Les autres colonnes contiennent également une liste non ordonnée avec un tas d'éléments de liste :

```
<ul class="list-unstyled">    <li><h6 class="text-white">PRODUIT</h6></li>    <li>Fonctionnalités</li>    <li>Exemples</li>    <li>Tour</li>    <li>Galerie</li> </ul>
```

Et c'est tout !

Plutôt cool, non ?

Merci beaucoup d'avoir suivi !

### Conclusion et plus d'informations

Il y a quelques mois, quand j'ai commencé à écrire cet article, je prévoyais d'écrire tout ce que je savais sur Bootstrap. Cependant, cela s'est avéré être beaucoup ?.

L'article sur Medium aurait été si long que j'avais peur que personne ne prenne la peine de le lire ?.

Les sujets que j'ai ignorés incluent :

1. Introduction à Sass/SCSS
2. Comment personnaliser Bootstrap à l'aide de Sass
3. Comment utiliser l'outil Bootstrap CLI pour une configuration plus rapide
4. Comment créer votre propre processus de construction (Build Process) à l'aide de Gulp et Webpack
5. Comment construire des thèmes Bootstrap professionnels, par exemple des thèmes de tableau de bord d'administration
6. Comment utiliser Bootstrap 4 avec ReactJS
7. Plus d'exemples pratiques, comme la construction d'un clone de Twitter et de Medium avec Bootstrap. Ces exemples utilisent JavaScript et plus de composants Bootstrap

Il y a une bonne nouvelle !

Je suis en train de les écrire, mais je les ai distillés dans un livre complet. Vous voudrez peut-être rester en contact et [être informé](https://goo.gl/forms/vD49zKW03LqKH7sv1) de la sortie du livre.

Si vous cherchez à devenir un développeur senior, vous ne devriez pas hésiter à avoir un large éventail d'expériences avec diverses technologies.

Santé,

_Ohans Emmanuel_ 