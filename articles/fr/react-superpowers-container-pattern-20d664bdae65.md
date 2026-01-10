---
title: Comment développer vos superpouvoirs React avec le Container Pattern
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-28T17:19:21.000Z'
originalURL: https://freecodecamp.org/news/react-superpowers-container-pattern-20d664bdae65
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OmLZDzZ_WRGIaLdv
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment développer vos superpouvoirs React avec le Container Pattern
seo_desc: 'By Eduardo Vedes

  Hello everyone! ?

  This time I’m going to tell you about this very useful pattern in React called the
  container pattern or container component pattern.

  This is one of the first patterns I learned. It helped me a lot to separate proble...'
---

Par Eduardo Vedes

Bonjour à tous ! ?

Cette fois, je vais vous parler de ce modèle très utile en React appelé le **container pattern** ou **container component pattern**.

C'est l'un des premiers modèles que j'ai appris. Il m'a beaucoup aidé à séparer les problèmes en plus petits et à les résoudre un à la fois.

De plus, il a définitivement aidé à rendre mon code beaucoup plus réutilisable et autonome en même temps.

Cela peut sembler un paradoxe ! Comment rendre votre code à la fois réutilisable et autonome ?

Eh bien, réutilisable car vous apprenez à faire de petits composants dummy (présentationnels) que vous pouvez réutiliser beaucoup.

Autonome car le container, la vue, ou ce que vous utilisez pour garder toute votre logique peut facilement être détaché d'un endroit et attaché à un autre sans grands changements/refactoring dans votre application principale.

#### **C'est donc un gagnant-gagnant et une superpuissance secrète que vous devez acquérir dès que possible !**

La vérité est que lorsque vous voulez faire une fonctionnalité, vous commencez toujours simple et propre.

Les jours passent et vous ajoutez une petite fonctionnalité ici, une autre là. Vous faites un patch ici, un patch là, et tout votre code devient désordonné et ingérable.

Croyez-moi, j'ai été là. **Et je suis encore là aujourd'hui !** Nous y sommes tous, à un certain point, car la programmation est un artisanat. Mais nous pouvons minimiser cela beaucoup avec la pratique et avec ce modèle de conception incroyable.

Mais, qu'est-ce qu'un modèle de conception ?

### 01. Qu'est-ce qu'un Software Design Pattern ?

Un [design pattern](https://en.wikipedia.org/wiki/Software_design_pattern) n'est rien de plus qu'une solution générale et réutilisable à un problème courant dans un contexte donné en conception logicielle. Ce n'est pas une conception finale qui peut être transformée directement en code source ou en code machine. C'est une description ou un modèle pour résoudre un problème qui peut être utilisé dans de nombreuses situations différentes.

**Les design patterns sont des meilleures pratiques formalisées que le programmeur peut utiliser pour résoudre des problèmes courants lors de la conception d'une application ou d'un système.**

Vous connaissez le [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) software design pattern ?

### 02. Qu'est-ce que le MVC Design Pattern ?

Eh bien, MVC signifie [Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller). C'est un modèle architectural utilisé pour développer des interfaces utilisateur. Il divise l'application en trois parties interconnectées.

Traditionnellement, il était utilisé pour les interfaces graphiques de bureau (GUI). Cette architecture est devenue populaire pour la conception d'applications web et même mobiles.

Imaginez que vous avez un triangle avec trois sommets : **View**, **Controller** et **Model**.

La Vue est ce que l'utilisateur voit à l'écran (côté client).

L'utilisateur voyant la vue peut produire des changements, peut appuyer sur un bouton, remplir un formulaire, appuyer sur play pour voir une vidéo, déclencher une panoplie de choses ensemble.

Le Contrôleur gère les changements que l'utilisateur a promus et toute la logique derrière. (Il fonctionne comme un relais, il fait des requêtes et gère tout entre la Vue et le Modèle.)

Le Modèle est le gestionnaire. Il contient ce qu'on appelle la logique métier, les données. Le modèle reçoit des informations du contrôleur et procède aux changements nécessaires. Il donne les mises à jour au Contrôleur et à la Vue.

React est « une bibliothèque JavaScript pour construire des interfaces utilisateur » (par définition ?). La plupart du temps, vous mélangez et gérez la V et une partie de la C.

Et c'est cette V et cette C que nous voulons séparer distinctement du container pattern.

### 03. Qu'est-ce que le Container Pattern ?

Le Container Pattern est une solution pour bien séparer la V de la C. Au lieu de faire un seul **<Component** /> avec la logique et la vue, vous le séparez en **deux : <ComponentContainer /> et <Component />. Le premier effectuera toutes les opérations logiques nécessaires et promouvra la communication avec la logique métier tandis que le second sera un composant de présentation dummy qui rendra ce que son parent Container demande.

Les composants de présentation se préoccupent de **l'apparence des choses**. Tandis que les composants Container se préoccupent de **la façon dont les choses fonctionnent**.

### 04. Mettons les mains dans le cambouis

Imaginez que nous voulons faire un composant Superhero List qui affiche certaines données à leur sujet. Nous allons récupérer les données d'une API et nous voulons les afficher à l'écran.

D'accord, pour simuler notre Modèle (base de données), j'ai créé un objet de données factice. Cet objet contient les informations des super-héros. Il a également une fonction fetchFarAwayAPI() qui retournera cet objet.

![Image](https://cdn-media-1.freecodecamp.org/images/6oM0C4bT-PSw0dDWZvxBgoAszEDh3g7DjuUe)
_simulation backend, base de données_

Ensuite, j'ai créé un composant stateful pour récupérer l'API, sauvegarder la réponse dans l'état de notre composant et rendre les données dans un tableau bootstrap à l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/PQ0-Zo7UZQZ9XBxF71WiYRLKe6kQMGKWqGUH)
_définition du composant SuperHeroList_

![Image](https://cdn-media-1.freecodecamp.org/images/V4TdLd9nlB-u3RAzkREv54vySgm-ajYZNJbf)
_méthode de rendu SuperHeroList_

D'accord, nous avons totalement séparé le Contrôleur de la vue. C'est ?l'idée principale que vous devriez garder à l'esprit concernant le container pattern.

Si vous regardez attentivement, nous avons fait un composant où nous récupérons des données, les sauvegardons dans l'état et les rendons à l'écran. Nous avons mélangé le C et le V. D'accord ?

D'accord, comment résolvons-nous cela ? Oui ! **Container Pattern !**

Suivez-moi !

La première étape consiste à créer un composant de présentation pour rendre la vue. Ce composant recevra des props et les rendra. Il est complètement dummy. Jetez un œil :

![Image](https://cdn-media-1.freecodecamp.org/images/NjvKR1zu5hRBiM36hBidB5HkiB-6ZZJxJIhy)
_Composant de présentation SuperHeroList_

Pour gérer la logique du Contrôleur, j'ai refactorisé notre ancien SuperHeroList en le renommant SuperHeroListContainer.

![Image](https://cdn-media-1.freecodecamp.org/images/iIyrhzvGMjr2RzRAgwAQ-A6Ks3MffQCkExVw)
_Composant SuperHeroListContainer_

D'accord, nous avons totalement séparé le Contrôleur de la vue et c'est ?l'idée principale que vous devriez garder à l'esprit concernant le container pattern.

Mais...

Nous pouvons aller plus loin et extraire la complexité des lignes du nouveau composant SuperHeroList. Comment faisons-nous cela ? Créons un nouveau composant SuperHeroRow :

![Image](https://cdn-media-1.freecodecamp.org/images/ycgvvXOcy1cByqk23d15vT9mShVn-YYo9I9J)
_Composant SuperHeroRow_

![Image](https://cdn-media-1.freecodecamp.org/images/OpesZFFBU08yhgqUi9cxtnncjNzLcUXyIPH7)
_Composant SuperHeroList_

Qu'avons-nous fait ici ? Nous avons découplé la complexité du rendu des lignes en dehors du composant SuperHeroList. Nous avons laissé le premier rendre uniquement le tableau et invoquer le SuperHeroRow pour rendre chacune des lignes seule.

Nous avons extrait la complexité des lignes vers un autre composant. N'oubliez pas, le container pattern est là (à l'intérieur de SuperHeroListContainer). Nous avons simplement réparti le rendu en deux composants parent/enfant qui sont complètement dummy et présentationnels en utilisant la méthode de travail préférée de React : la composition !

Vous avez la liberté d'extraire les responsabilités/complexités dans des composants plus petits. C'est ainsi que vous devriez travailler avec React ! Vous devez l'ajuster à ce qui est le mieux pour l'application, pour l'équipe, pour le contexte dans lequel vous vous trouvez.

![Image](https://cdn-media-1.freecodecamp.org/images/rlgOQMQjvzfepYufQD0khYiQe6R6pqZ76tmD)
_Vue navigateur de la liste des super-héros_

Parfois, nous pouvons abstraire un peu la chose ! Je pense que pour l'instant nous allons bien, mais... allons un peu plus loin...

Créons une deuxième SuperHeroList cette fois en utilisant un HOC (Higher Order Component).

Un composant d'ordre supérieur (HOC) est une technique avancée dans React pour réutiliser la logique des composants. Les HOC ne font pas partie de l'API React, à proprement parler. Ils sont un modèle qui émerge de la nature compositionnelle de React.

Concrètement, **un composant d'ordre supérieur est une fonction qui prend un composant et retourne un nouveau composant.**

Le but ici est de refactoriser notre SuperHeroListContainer en une fonction JavaScript vanilla. Cette fonction prend un composant (communément appelé le WrappedComponent) et retourne un nouveau composant.

Vérifiez simplement comment je l'ai fait ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/kDPOzrmiYp88pMEFwVIiMZ9MiRMPgCoJCCAL)
_HOC withContainer_

Nous avons refactorisé le <SuperHeroListContainer /> en cette fonction appelée withContainer. Elle reçoit n'importe quel composant que vous voulez passer à travers et retourne un composant de classe avec toute la logique à l'intérieur !

Dans ce cas, l'abstraction nous permet d'exporter plusieurs types de tableaux ou de réutiliser toute la logique que nous avions dans le container pour invoquer plusieurs/différents composants de présentation/dummy.

C'est ainsi que nous obtenons l'autonomie et la réutilisabilité ensemble ?

![Image](https://cdn-media-1.freecodecamp.org/images/Ur3mNoy-cQ7ff6-6DspQgf2aIGXdabRygkiE)
_SuperHeroList 1 et 2 rendus à l'écran_

### Dernier point mais non des moindres

Ne vous inquiétez pas si, au début, vous avez eu du mal à déterminer comment appliquer le container pattern. C'est un processus itératif. Avec la pratique, vous y arriverez sans trop réfléchir. Cela deviendra intuitif et semblera à première vue la meilleure approche pour presque (90%) tout ce que vous faites en React.

React a un modèle de composition puissant. [Ils recommandent](https://reactjs.org/docs/composition-vs-inheritance.html) d'utiliser la composition plutôt que l'héritage pour réutiliser le code entre les composants.

NOTE : Pour cet article, j'ai utilisé Create React App 2.0 avec Bootstrap. Vous pouvez toujours tirer mon repo [ici](https://github.com/evedes/container-pattern) et faire quelques expérimentations plus tard. Vous trouverez les deux SuperHeroLists et les deux exemples que nous avons faits tout au long de l'article.

Continuez à lire mes articles et n'oubliez pas : toujours **Soyez Fort et Codez !**

### Bibliographie

1. [Documentation React](https://reactjs.org/docs/getting-started.html)
2. [Container Components](https://medium.com/@learnreact/container-components-c0e67432e005) de _Learn React with chantastic_;
3. [Software design pattern](https://en.wikipedia.org/wiki/Software_design_pattern), de wikipedia, l'encyclopédie libre;
4. [Model-view-controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller), de wikipedia, l'encyclopédie libre;
5. [Presentational and Container Patterns](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0), par Dan Abramov;

Merci beaucoup !

evedes, Oct 2018