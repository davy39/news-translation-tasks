---
title: Une tentative TypeScript de Clean Architecture
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T20:56:12.000Z'
originalURL: https://freecodecamp.org/news/a-typescript-stab-at-clean-architecture-b51fbb16a304
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zizBT5zxwmm5mibeF55bow.png
tags:
- name: Clean Architecture
  slug: clean-architecture
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: TypeScript
  slug: typescript
seo_title: Une tentative TypeScript de Clean Architecture
seo_desc: "By Warren Bell\n# \nClean Architecture\nThere are many videos and articles\
  \ explaining clean architecture. Most of these go over the concepts from a 20,000\
  \ foot view. I don’t know about you, but I don’t learn things very well at that\
  \ elevation. Not a lot..."
---

Par Warren Bell

# 

### Clean Architecture

Il existe de nombreuses vidéos et articles expliquant l'architecture propre. La plupart de ces ressources abordent les concepts d'un point de vue très général. Je ne sais pas pour vous, mais je n'apprends pas très bien les choses à cette altitude. Il n'y a pas beaucoup d'oxygène là-haut. J'apprends en plongeant tête la première et en codant. Cet article et le code qui l'accompagne sont le résultat d'un tel plongeon.

### Bob est ton oncle

Le terme « Clean Architecture » a été popularisé par Robert Martin (Uncle Bob) et son livre « Clean Architecture: A Craftsman’s Guide to Software Structure and Design ». Je ne prétends pas être un expert dans ce domaine et je n'ai pas lu son livre, bien que je compte le faire. Mais je peux tout à fait me reconnaître dans les problèmes qu'il tente de résoudre.

Comment écrire un système logiciel qui ne dépend de rien d'autre qu'un langage principal ? On nous avait promis cela dans le passé avec les interfaces et autres principes OO, mais je n'avais jamais vu auparavant une explication « propre », jeu de mots intentionnel, sur la manière de faire cela concernant l'ensemble du système. Et oui, je suis un peu en retard à cette fête, étant donné qu'Uncle Bob a commencé à parler de ces concepts en 2012, ce qui est un siècle en années logicielles.

### Le diagramme qui m'a déconcerté

Voici le diagramme original qu'Uncle Bob et d'autres ont utilisé dans leurs présentations pour expliquer la Clean Architecture. Ce simple petit diagramme est devenu une obsession pour moi. J'avais depuis longtemps purgé ma mémoire de tout ce qui était lié à UML et je luttais avec les relations has-a et uses-a indiquées par les têtes de flèches ouvertes et fermées. La seule façon de comprendre cela était d'écrire du code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Amv74nfUdirQYlRmSyEMDA.png)
_Crédit Image : Uncle Bob_

### Connaître vos oignons

Une façon de voir la Clean Architecture est comme un oignon avec des couches. Toutes les couches ne peuvent dépendre que d'une couche plus proche du centre. C'est-à-dire que toutes les dépendances pointent vers l'intérieur et non vers l'extérieur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nEATDe5dRLIWN3MSxSjG0A.png)
_[Crédit Image](https://android.jlelse.eu/thoughts-on-clean-architecture-b8449d9d02df" rel="noopener" target="_blank" title=")_

### Un de ces jours, je vais m'organiser

Dans notre exemple, il y a 4 modules qui correspondent à chaque couche de cet oignon. Finalement, ceux-ci pourraient être des modules npm séparés. Pour des raisons de lisibilité, j'ai essayé de nommer les choses selon le diagramme original de Clean Architecture d'Uncle Bob en haut de cet article. Dans le monde réel, vous préfixeriez probablement tous les noms avec le cas d'utilisation qu'ils représentent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xfnLsbxyTy4s-AEQY7vi2A.png)
_Crédit Image : Moi-même_

La couche infrastructure (bleue) est l'endroit où vivent tous nos systèmes externes pluggables. Ces systèmes externes tels que les appareils, le web et les interfaces utilisateur, représentés dans le diagramme de l'oignon, utiliseront nos interfaces IRequest et IViewModel pour communiquer avec notre Controller et Presenter tandis que la base de données et les interfaces externes, représentées dans le diagramme de l'oignon, utiliseront l'interface IEntityGateway pour communiquer avec notre Interactor.

Notre exemple aura une entité appelée Widget avec trois propriétés. Il utilise également un cas d'utilisation « créer un widget » qui prend un widget de l'interface utilisateur, sauvegarde le widget dans un système de stockage et retourne à l'interface utilisateur un widget nouvellement créé avec un identifiant et un numéro de révision.

### Plus d'aides visuelles

Voici la structure du répertoire. Tout est connecté dans le fichier index.ts de chaque module. Le point d'entrée est démontré dans un test situé dans infrastructure/test/TestEntryPoint.spec.ts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LRbWuQzcmLh9LOJL5P2HYA.png)
_Crédit Image : Shift Command 4_

### Dans quelle direction est-il parti ?

L'un de mes blocages initiaux était de comprendre comment la couche la plus externe communique avec les couches internes. Je pensais qu'il suffisait d'appeler une fonction createWidget(), par exemple, sur un Controller et que vous obtiendriez un nouveau widget tout neuf. Faux.

Ce que vous voulez faire, c'est envoyer le widget à créer vers le cas d'utilisation (Interactor) sur un certain chemin et faire en sorte que le cas d'utilisation (Interactor) envoie le nouveau widget en retour sur un chemin différent. Cela ressemble à une fonction de rappel ou une Promesse. J'ai trouvé un bon diagramme illustrant cela dans un article intitulé « Implementing Clean Architecture — Of controllers and presenters » (lien ci-dessous). Dans notre exemple, je n'ai pas implémenté de RequestModel ou de ResponseModel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KMgKFitjUr7K0MaNxuLZGA.png)
_[Crédit Image](https://plainionist.github.io/Implementing-Clean-Architecture-Controller-Presenter/" rel="noopener" target="_blank" title=")_

### Entrer, Sauter et Sortir, à la manière OO

Alors, créons d'abord un widget avec des classes et des interfaces.

### Étape OO 1

C'est le point d'entrée. Ce code serait situé dans la couche infrastructure (bleue). Cette couche est l'endroit où vivent votre application mobile, votre application web, votre API, votre CLI, etc. Tous vos systèmes externes comme les API externes, les frameworks, les bibliothèques et les bases de données vivent également ici. Tout est pluggable dans cette couche et communique avec notre système via les interfaces que nous fournissons.

Tout d'abord, vous créez votre implémentation de ViewModel de l'interface IViewModel où un nouveau widget apparaîtra et vous pourrez mettre à jour votre interface utilisateur dans la fonction implémentée presentWidget(widget).

Vous créez ensuite un Controller qui implémente l'interface IRequest en passant l'EntityGateway et le ViewModel que vous avez créés ci-dessus à un constructeur. Enfin, votre interface utilisateur appelle createWidget(widget) sur le Controller où votre nouveau widget commence son voyage vers l'Interactor.

#### Qu'est-ce qu'un EntityGateway ?

Un EntityGateway implémente l'interface IEntityGateway et est l'endroit où vous implémentez un code spécifique qui persiste votre widget. Il vit dans la couche infrastructure (bleue). Cela pourrait être n'importe quel type d'API externe existante ou future ou un système de persistance tel qu'une base de données.

Pour changer de système, vous n'auriez qu'à connecter la nouvelle implémentation de l'EntityGateway avec l'interface IEntityGateway. Dans cet exemple, j'utilise une Promesse pour simuler une sorte d'opération de persistance.

#### Connecter quoi ?

Le fichier infrastructure/src/index.ts dans le module infrastructure est l'endroit où vous pouvez connecter vos différentes implémentations de votre interface IEntityGateway. Le chemin « from » de l'instruction d'importation pointe vers l'implémentation correcte. Dans ce cas, il s'agit d'un système de persistance nommé AnyDB.

Uncle Bob parle également de l'utilisation d'une classe Main où vous pouvez faire ce type de connexion ou faire d'autres codes d'initialisation. La classe Main vivrait également dans le module infrastructure et serait pluggable. Elle communiquerait également de la même manière que les autres systèmes du module infrastructure. Par exemple, vous initierez cette classe dans le code d'initialisation de votre interface utilisateur et la passerez dans vos couches plus internes pour être utilisée via une sorte d'interface de configuration.

Notre exemple n'utilise pas de classe Main et passe plutôt le système de persistance dans l'interactor via la fonction createWidget(). Ce n'est probablement pas la manière « pure » de faire cela, mais cela a été fait pour rendre notre exemple plus facile à lire.

### Étape OO 2

Le Controller est un endroit très occupé. Tout d'abord, l'EntityGateway passe inchangé à notre constructeur Interactor. Ensuite, notre ViewModel est passé au constructeur de notre Presenter qui, à son tour, est également passé à notre constructeur Interactor. Tout cela se passe dans la fonction createWidget(widget) du Controller qui a été appelée par notre interface utilisateur dans l'étape 1 via l'interface IRequest. Nous parlerons de notre Presenter dans l'étape 4 lorsque le widget nouvellement créé remonte vers l'interface utilisateur.

### Étape OO 3

Enfin, nous sommes à la couche la plus interne de notre voyage, la couche de cas d'utilisation où vit notre Interactor. Ou mieux connu comme notre maison pour toute la logique des cas d'utilisation de notre application. Il y a une couche encore plus interne, le domaine. C'est là que vivent toutes nos entités métier et la logique spécifique au métier. Dans cet exemple, nous n'avons vraiment pas besoin d'y aller sauf pour emprunter les interfaces WidgetType et IEntityGateway.

#### Avancer

Ici, dans notre Interactor, nous prenons l'EntityGateway qui a été passé du Controller et appelons sa fonction saveWidget(widget) via l'interface IEntityGateway. Cette fonction retourne une Promesse de l'EntityGateway qui se résout dans .then() avec un widget nouvellement créé. Nous appelons ensuite la fonction presentWidget(widget) du Presenter via l'interface IOutputBoundary qui commence le widget nouvellement créé à remonter vers l'interface utilisateur. Tout cela se passe dans la fonction createWidget(widget) de l'Interactor qui a été appelée par notre Controller via l'interface IInputBoundary dans l'étape 2.

### Étape OO 4

Ici, dans notre Presenter, nous passons simplement le widget à la fonction presentWidget(widget) de notre ViewModel que nous avons créée dans notre interface utilisateur. Tout cela se passe dans la fonction presentWidget(widget) du Presenter via l'interface IOutputBoundary qui a été appelée dans la fonction createWidget(widget) de l'Interactor dans l'étape 3. Plus de choses peuvent se passer ici, mais pas dans notre exemple.

### Étape OO 5

Enfin, notre widget nouvellement créé est de retour à la maison, prêt à être affiché dans notre interface utilisateur. C'est l'endroit exact (code) où nous avons commencé dans l'étape 1. La mise à jour de l'interface utilisateur se fait dans la fonction presentWidget(widget) du ViewModel via l'interface IViewModel qui a été appelée dans la fonction presentWidget(widget) du Presenter dans l'étape 4.

#### Membres du casting de soutien OO

Voici toutes les interfaces et définitions de types restantes regroupées dans un seul fichier.

#### 2 hommes entrent, 1 homme sort

J'ai écrit la version classe et interface de ce projet en premier. Je voulais essayer de la faire correspondre au diagramme original d'Uncle Bob aussi près que possible. Lorsque j'ai terminé ce projet, j'ai réalisé que j'aurais pu faire la même chose avec des fonctions et des définitions de types. J'ai donc créé un projet identique et remplacé les Classes par des Fonctions et les Interfaces par des définitions de Type.

Et voici la différence entre une classe Controller et une fonction Controller.

### Entrer, Sauter et Sortir, à la manière Fonction

Maintenant, essayons de créer des widgets avec des fonctions et des définitions de types.

#### Différences générales

WidgetType est identique à la version OO ci-dessus et IEntityGateway, IRequest, IViewModel, IInputBoundary et IOutputBoundary sont maintenant des définitions de types au lieu d'interfaces.

### Étape Fonction 1

Tout est identique à l'étape OO 1 ci-dessus, sauf que nous importons maintenant une fonction nommée « controllerConstructor » au lieu d'une classe nommée « Controller ». Et nous importons une fonction nommée « entityGateway » au lieu d'une classe nommée EntityGateway. Enfin, le ViewModel que nous avons créé est maintenant un objet avec une fonction presentWidget() au lieu d'une classe avec une fonction presentWidget().

#### EntityGateway encore ?

L'EntityGateway effectue la même tâche que la version OO ci-dessus. C'est maintenant une fonction au lieu d'une classe. Elle retourne une fonction saveWidget() enveloppée dans un objet.

#### Plus de connexion

Identique à la version OO ci-dessus sauf que nous exportons maintenant une fonction au lieu d'une classe.

### Étape Fonction 2

Notre Controller est toujours un endroit occupé et effectue les mêmes tâches que la version OO. Nous importons maintenant une fonction nommée interactorConstructor au lieu d'une classe nommée Interactor. Nous exportons une fonction nommée « controllerConstructor » au lieu d'une classe nommée « Controller ». Elle retourne une fonction nommée « createWidget » enveloppée dans un objet.

### Étape Fonction 3

De retour dans l'Interactor dans notre module usecase, nous exécutons les mêmes tâches que la version OO ci-dessus. Nous exportons maintenant une fonction nommée « interactorConstructor » au lieu d'une classe nommée « Interactor ». Elle retourne une fonction nommée « createWidget » enveloppée dans un objet.

### Étape Fonction 4

Nous passons maintenant le widget nouvellement créé en remontant dans notre Presenter où nous exécutons les mêmes tâches que la version OO ci-dessus. Nous exportons une fonction nommée « presenterConstructor » au lieu d'une classe nommée « Presenter ». Elle retourne une fonction nommée « presentWidget » enveloppée dans un objet.

### Étape Fonction 5

Nous avons encore fait le tour complet et nous sommes de retour à l'endroit exact (code) où nous avons commencé dans l'étape 1. Notre interface utilisateur est mise à jour avec notre widget nouvellement créé dans la fonction presentWidget() du ViewModel.

#### Membres du casting de soutien Fonction

Voici toutes les définitions de types restantes regroupées dans un seul fichier. Ce sont nos interfaces.

### Tout ça pour un fichu Widget ?

Oui, mais vous obtenez également la promesse d'un système complètement découplé où vous pouvez brancher différentes implémentations de vos systèmes externes (couche infrastructure bleue), y compris différents types d'interfaces utilisateur, d'API externes, de bases de données, de bibliothèques, de frameworks et plus encore.

### Nous n'avons pas besoin de profiler

Mon intuition initiale était que la version classe et interface serait plus lente que la version fonction. J'ai donc exécuté les deux projets à travers mes outils de profilage avancés en tapant « npm test » et en appuyant sur entrer jusqu'à ce que mon doigt se crampe.

Ma première observation était que la version fonction était environ deux fois plus rapide, WOW. Ensuite, j'ai décidé de refactoriser la version fonction pour retourner toutes les fonctions importantes enveloppées dans des objets afin de pouvoir imposer les noms des fonctions. J'ai ensuite exécuté les deux versions à travers mes profileurs avancés et elles étaient à peu près à la même vitesse.

Je n'ai aucune idée de pourquoi envelopper une fonction dans un objet la ralentirait autant. Peut-être que je n'ai pas complètement désinstallé Adobe Flash de mon ordinateur portable et qu'il a décidé d'interférer. Quoi qu'il en soit, il serait intéressant d'obtenir une mesure plus précise de la vitesse en utilisant les outils corrects contre le JavaScript compilé.

### Le Take Away

La version OO a plus de code mais peut être plus facile à lire et à suivre. La version fonction a moins de code mais peut être plus difficile à lire et à suivre.

Personnellement, je préfère la version fonction, ayant fait beaucoup de programmation en Java et étant fatigué d'écrire autant de classes. L'une des choses que j'aime le plus dans TypeScript/JavaScript est la capacité à utiliser des littéraux d'objet. Et avec les définitions de types TypeScript, vous pouvez maintenant appliquer une certaine sécurité à l'utilisation des littéraux d'objet.

Un autre point à retenir est que vous n'avez pas besoin de vous conformer rigidement à l'architecture propre telle que diagramée ci-dessus pour obtenir un système découplé. Par exemple, vous pourriez tout aussi facilement faire en sorte que votre interface utilisateur communique directement avec votre couche de cas d'utilisation en contournant la couche de livraison si elle n'est pas nécessaire. Toutes ces couches peuvent physiquement vivre dans différents endroits et avoir différentes façons de communiquer entre elles.

### Essayez-le

Voici quelques-unes des choses que je compte appliquer dans mon prochain projet.

1. Les dépendances doivent toujours aller dans un sens.
2. Les dépendances doivent toujours pointer de vos systèmes externes (interface utilisateur, base de données, etc.) vers vos entités métier et votre logique métier.
3. Vos couches internes (livraison, cas d'utilisation et entités métier) doivent exposer des interfaces pour que les couches plus externes puissent les utiliser.
4. Vous devez toujours commencer à développer à partir de la couche la plus interne. Commencez par les entités métier et la logique, puis testez. Créez les interfaces qui seront utilisées, puis testez ces interfaces. Je suis coupable de travailler dans l'autre sens. Je pense que nous aimons tous commencer par l'interface utilisateur, car elle nous permet immédiatement de voir visuellement à quoi ressemblera notre système pour un utilisateur. De plus, l'interface utilisateur est l'endroit où vivent beaucoup de technologies « cool ».
5. Utilisez le TDD (Test Driven Development). La clean architecture vous permet de faire cela beaucoup plus facilement. Tout est plus compartimenté et plus facile à simuler. L'implémentation de l'IEntityGateway ci-dessus est essentiellement une simulation d'une base de données.
6. Enfin, soyez flexible. Ne vous épuisez pas à essayer de vous conformer à la clean architecture lorsque la bibliothèque ou le framework que vous souhaitez utiliser ne fonctionne tout simplement pas avec. Mais soyez averti que cela est probablement une bonne indication que vous aurez éventuellement des problèmes concernant cette bibliothèque ou ce framework, surtout s'il vous demande d'étendre leurs classes. Le découplage doit être votre objectif.

### Mais, mais, qu'en est-il de...

Veuillez poser des questions et donner des commentaires, il n'y a pas de meilleure façon d'apprendre que de recevoir des critiques constructives de vos pairs. Et il est fortement probable que j'ai manqué quelque chose quelque part.

### Ressources :

#### Le code de la version OO se trouve à l'adresse suivante :

[https://github.com/warrenbell/cleanarch-tsoo](https://github.com/warrenbell/cleanarch-tsoo)

#### Le code de la version fonction se trouve à l'adresse suivante :

[https://github.com/warrenbell/cleanarch-ts](https://github.com/warrenbell/cleanarch-tsoo)fun

#### ts-node

Outil pratique pour TypeScript.

[https://github.com/TypeStrong/ts-node](https://github.com/TypeStrong/ts-node)

#### La Clean Architecture par Uncle Bob

[https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)

#### Le Livre

[https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)

#### L'une des nombreuses vidéos

Elles sont toutes essentiellement les mêmes sauf pour les cinq premières minutes où Uncle Bob aime disserter sur quelque chose de vaguement lié et fait ensuite une transition brutale vers la clean architecture.

[https://www.youtube.com/watch?v=Nltqi7ODZTM](https://www.youtube.com/watch?v=Nltqi7ODZTM)

#### Implémentation de la Clean Architecture — Des contrôleurs et des présentateurs

[https://plainionist.github.io/Implementing-Clean-Architecture-Controller-Presenter/](https://plainionist.github.io/Implementing-Clean-Architecture-Controller-Presenter/)

#### Clean Architecture : Se tenir sur les épaules des géants

[https://herbertograca.com/2017/09/28/clean-architecture-standing-on-the-shoulders-of-giants/](https://herbertograca.com/2017/09/28/clean-architecture-standing-on-the-shoulders-of-giants/)

#### Clean Architecture : Cas d'utilisation contenant le présentateur ou retournant des données ?

[https://softwareengineering.stackexchange.com/questions/357052/clean-architecture-use-case-containing-the-presenter-or-returning-data](https://softwareengineering.stackexchange.com/questions/357052/clean-architecture-use-case-containing-the-presenter-or-returning-data)

#### Clean architecture. Quels sont les rôles du présentateur ?

[https://stackoverflow.com/questions/46510550/clean-architecture-what-are-the-jobs-of-presenter](https://stackoverflow.com/questions/46510550/clean-architecture-what-are-the-jobs-of-presenter)