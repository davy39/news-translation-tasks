---
title: Notation Crow's Foot – Symboles de relation et comment lire les diagrammes
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-06T15:11:31.000Z'
originalURL: https://freecodecamp.org/news/crows-foot-notation-relationship-symbols-and-how-to-read-diagrams
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/hanna-morris-_XXNjSziZuA-unsplash.jpg
tags:
- name: database
  slug: database
seo_title: Notation Crow's Foot – Symboles de relation et comment lire les diagrammes
seo_desc: "Entity relationship diagrams (ERD) help us understand the connection between\
  \ various \"entities\" that make up a system. \nIn software development, ERDs are\
  \ mostly used in database design. This lets us create graphical representations\
  \ of the entities th..."
---

Les diagrammes de relation entre entités (ERD) nous aident à comprendre la connexion entre diverses "entités" qui composent un système. 

En développement logiciel, les ERD sont principalement utilisés dans la conception de bases de données. Cela nous permet de créer des représentations graphiques des entités qui composent des systèmes tels qu'une base de données (vous comprendrez mieux cela avec les exemples de ce tutoriel). 

Afin de comprendre la relation entre les entités dans un ERD, nous utilisons des symboles et des notations spécifiques. 

Bien qu'il existe diverses notations pour comprendre les ERD, nous nous concentrerons sur la notation Crow's Foot, qui est l'une des plus couramment utilisées lors de la création/conception d'ERD. 

Ce tutoriel vous aidera à comprendre ce que sont les entités et leurs attributs dans les diagrammes de relation entre entités, les différents symboles de la notation Crow's Foot que vous pouvez utiliser pour définir la relation entre les entités, et comment lire et comprendre les diagrammes. 

À la fin du tutoriel, vous devriez être capable de comprendre et de lire les diagrammes, et de créer vos propres diagrammes de relation entre entités en utilisant la notation Crow's Foot pour définir vos relations entre entités. 

Vous verrez les mots : notation, indicateurs et symboles utilisés de manière interchangeable. 

## Qu'est-ce qu'une entité dans les ERD ? 

Avant de regarder quelques exemples, parlons de certains des termes clés/composants qui composeront les diagrammes de relation entre entités avec lesquels nous travaillerons. 

Le premier est l'**entité**. Une entité représente simplement un objet dans notre base de données. Cela pourrait être un objet pour les utilisateurs, les cours, les produits, et ainsi de suite. 

Notez que le nom de chaque entité doit être au singulier (user) et non au pluriel (users). 

Voici à quoi ressemble une entité : 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/entity.png) 

Le diagramme ci-dessus montre une entité appelée user. Cette entité contiendra des informations sur les différents utilisateurs inscrits sur une plateforme. 

Dans la section suivante, nous parlerons des attributs. 

## Qu'est-ce que les attributs dans les ERD ? 

Nous avons parlé des entités et nous savons qu'elles stockent une sorte d'information sur l'objet qu'elles représentent. 

L'information sur un objet est constituée des attributs. Nous pouvons donc dire que les propriétés d'une entité sont les attributs. 

Représentons cela à l'aide d'un diagramme. 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/attributes-2.png) 

L'entité dans le diagramme ci-dessus a trois attributs – username, age et email. 

Maintenant, vous avez une image plus claire de ce qu'est une entité et de ses attributs. 

Si cela vous semble encore confus, l'entité ci-dessus s'appelle "User". L'entité a trois propriétés (username, age et email) qui sont appelées les attributs de l'entité. 

## Relation entre les entités dans les ERD 

Dans les sections précédentes, nous avons parlé des entités et de leurs attributs. Dans la plupart des cas, les bases de données sont composées de plus d'une entité. 

Pour comprendre la relation entre une entité et une autre, nous utilisons des lignes pour les connecter. Mais ces lignes ont des notations (indicateurs) qui spécifient le type de relation qui existe entre deux entités. 

Nous utiliserons la notation Crow's Foot pour spécifier nos relations entre entités. 

### Symboles de la notation Crow's Foot et leur signification 

Avant de voir les diagrammes des symboles associés à la notation Crow's Foot, nous devons discuter d'un terme clé dans la notation Crow's Foot. 

L'un des termes les plus importants à connaître lors de l'utilisation de la notation Crow's Foot est la **cardinalité**. 

La **cardinalité** agit comme un paramètre pour la relation entre les entités. Pour une entité, il existe un nombre minimum et maximum qui aide à définir sa relation avec une autre entité. 

Ne vous inquiétez pas si ces explications semblent confuses. Au fur et à mesure que nous avancerons, vous les comprendrez parfaitement. 

Voici les symboles associés à la notation Crow's Foot : 

#### Zéro 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/zero-crow.png) 

Le symbole/diagramme ci-dessus désigne zéro dans la notation Crow's Foot. Nous le savons grâce à l'indicateur zéro/cerle du côté droit de la ligne horizontale. 

#### Un 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/one-crow.png) 

Le diagramme ci-dessus montre une ligne horizontale avec une courte ligne verticale la croisant. La ligne verticale agit comme l'indicateur – elle désigne un. 

#### Plusieurs 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/crows-crows-foot.png) 

Le diagramme ci-dessus désigne plusieurs. Vous pouvez facilement vous souvenir de ce symbole car il ressemble à un pied de corbeau. 

Les trois diagrammes ci-dessus sont la représentation de base des indicateurs dans la notation Crow's Foot. Mais dans la plupart des cas, ces indicateurs sont combinés pour comprendre pleinement la relation entre les entités. 

Au moment où nous commencerons à regarder quelques exemples pratiques, vous comprendrez mieux la signification de ces symboles. 

Avant cela, jetons un coup d'œil à d'autres diagrammes et à leur signification. Nous n'introduirons rien de nouveau – juste une combinaison des diagrammes ci-dessus. 

#### Zéro ou plusieurs 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/zero-and-many-crow.png) 

Comme on peut le voir ci-dessus, le symbole/indicateur **zéro ou plusieurs** dans la notation Crow's Foot est une combinaison des indicateurs zéro et plusieurs. 

#### Un ou plusieurs 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/one-and-many-crow.png) 

Comme prévu, l'indicateur **un ou plusieurs** est une combinaison de deux indicateurs – un et plusieurs. 

#### Un et un seul 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/one-and-one-crow.png) 

L'indicateur **un et un seul** a deux indicateurs "un". Dans nos exemples dans la section suivante, vous comprendrez mieux son utilisation. 

## Comment utiliser la notation Crow's Foot dans les diagrammes de relation entre entités 

Dans la dernière section, nous nous sommes concentrés sur les diagrammes de notation Crow's Foot et leur signification. Ils servent d'indicateurs qui expliquent la relation entre une entité et une autre. 

Dans cette section, nous allons plonger et regarder quelques exemples pratiques – cela vous aidera à comprendre pleinement comment utiliser la notation Crow's Foot. 

Si vous avez suivi depuis les sections précédentes, alors certains aspects des diagrammes que nous utiliserons dans cette section devraient être clairs pour vous. 

### Exemple de notation Crow's Foot #1 

Dans cet exemple, nous commencerons par une hypothèse, créerons des entités et désignerons leur relation en utilisant la notation Crow's Foot. 

Nous allons diviser cet exemple en étapes avec des diagrammes menant à l'esquisse finale. 

##### Étape #1 - Notre hypothèse et les entités 

Supposons que nous avons deux entités dans notre base de données. Une entité enseignant et une entité cours. Voici une représentation de cela : 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/teacher-course-crow.png) 

##### Étape #2 - Relation de l'entité Enseignant et de l'entité Cours 

Puisque nous sommes ceux qui créons ce modèle de la base de données, nous établissons les règles ! Donc pour chaque enseignant, ils ne peuvent enseigner qu'un seul cours. 

Nous supposerons que cela est une plateforme où les utilisateurs sont enseignés des langages de programmation. Chaque enseignant ne peut enseigner qu'un seul langage de programmation. 

La notation ici sera **un et un seul**. La notation sera placée du côté droit de la ligne horizontale. 

Voici un diagramme de relation entre entités pour cela : 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/teacher-course-crow2.png) 

Vous vous souvenez quand nous avons parlé de **cardinalité** ? Eh bien, c'est l'endroit parfait pour la voir en pratique. Le nombre minimum de cours qu'un enseignant peut prendre est un, et le maximum est également un. 

##### Étape #3 - Relation de l'entité Cours et de l'entité Enseignant 

Pour chaque cours, nous voulons avoir un ou plusieurs enseignants parmi lesquels choisir – ce qui signifie qu'un cours peut être enseigné par un ou plusieurs enseignants. Le minimum ici sera un tandis que le maximum sera plusieurs. 

Ainsi, l'utilisateur peut avoir un ou plusieurs enseignants de JavaScript parmi lesquels apprendre, un ou plusieurs enseignants de Python parmi lesquels apprendre, et ainsi de suite. 

La notation à utiliser est **un ou plusieurs**. La notation sera placée du côté gauche de la ligne horizontale. 

Voici l'ERD : 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/teacher-course-crow3.png) 

### Exemple de notation Crow's Foot #2 

Les notations n'ont pas toujours à être différentes. Ce qui compte, c'est la logique derrière la relation entre les entités. Cela dépend entièrement de ceux qui créent ou conçoivent la base de données. 

Jetez un coup d'œil au diagramme ci-dessous. 

![Image](https://www.freecodecamp.org/news/content/images/2022/06/crows-foot-example.png) 

Nous avons deux entités – Client et Pizza. Ces entités sont liées ensemble par une ligne horizontale avec des symboles/indicateurs/notations. 

Commençons par la notation à gauche. Elle a la notation **zéro ou plusieurs**. Cela implique qu'une pizza peut être commandée par aucun (optionnel) ou plusieurs clients. 

De même, la notation du côté droit implique qu'un client peut commander **zéro ou plusieurs** pizzas. 

La **cardinalité** ici est la même pour les deux entités. Zéro est le minimum tandis que plusieurs est le maximum. 

Les cas d'utilisation pour les autres diagrammes de notation Crow's Foot sont les mêmes que ceux de nos exemples. Tout dépend de la logique et de ce que vous concevez. 

## Conclusion 

Ce tutoriel sert d'introduction à la compréhension des diagrammes de relation entre entités et de la notation Crow's Foot pour la conception de bases de données. 

Nous pouvons utiliser les diagrammes de relation entre entités pour créer un modèle de base de données, ou créer une représentation graphique d'une base de données avec les diverses entités qui composent la base de données. Cela facilite la compréhension de la manière dont chaque entité s'associe à une autre. 

La notation facilite la compréhension des relations entre les entités. Dans notre cas, nous avons utilisé la notation Crow's Foot. 

Nous avons commencé par expliquer quelques terminologies clés associées aux diagrammes de relation entre entités et à la notation Crow's Foot comme les entités, les attributs, la cardinalité et la signification des différents diagrammes de notation Crow's Foot. 

Nous avons ensuite vu quelques exemples pour aider à comprendre l'application des diagrammes de notation Crow's Foot dans la définition de la relation entre les entités dans un diagramme de relation entre entités. 

Les exemples utilisés sont très basiques, mais ce n'est pas toujours le cas lors de la travail sur une base de données réelle. Avoir une bonne compréhension des diagrammes de base et de leur signification vous aidera à comprendre des conceptions beaucoup plus complexes. 

Merci d'avoir lu !