---
title: Le Guide Ultime pour les Débutants en Développement de Jeux avec Unity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-21T20:27:47.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-beginners-guide-to-game-development-in-unity-f9bfe972c2b5
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca41d740569d1a4ca6043.jpg
tags:
- name: Game Development
  slug: game-development
- name: gaming
  slug: gaming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: unity
  slug: unity
seo_title: Le Guide Ultime pour les Débutants en Développement de Jeux avec Unity
seo_desc: 'By Hugo Dolan

  Unity is a great tool for prototyping everything from games, to interactive visualisations.
  In this article, we run through all you need to know to get started using Unity.

  First, a little bit about me: I’m a hobbyist unity developer, 3...'
---

Par Hugo Dolan

Unity est un excellent outil pour prototyper tout, des jeux aux visualisations interactives. Dans cet article, nous passons en revue tout ce que vous devez savoir pour commencer à utiliser Unity.

D'abord, un peu à propos de moi : Je suis un développeur Unity amateur, un modeleur 3D et un graphiste qui travaille avec Unity et Blender depuis plus de 5 ans. Je suis maintenant étudiant en mathématiques financières à l'Université College Dublin, et occasionnellement, je fais du design graphique freelance, du prototypage web et du prototypage de jeux.

![Image](https://cdn-media-1.freecodecamp.org/images/Q-bD3OdyDZX2X2cmqgyyRIFwRpy9mngdYAtC)
_L'art conceptuel est l'une des premières phases du processus de développement de jeux, au cours des 5 dernières années, j'ai été exposé à tous les domaines de la conception de jeux. Consultez mon [Portfolio](http://hugodolan.com/portfolio" rel="noopener" target="_blank" title=") de design graphique, UX, art conceptuel, développement de jeux, etc._

### Introduction

Cet article s'adresse à toute personne n'ayant jamais utilisé Unity auparavant, mais ayant une certaine expérience en programmation ou en design/développement web. À la fin de cet article, vous devriez avoir une bonne vue d'ensemble du moteur ainsi que toutes les fonctions et le code nécessaires pour commencer à créer un jeu de base.

### Pourquoi Unity ?

#### Si vous voulez créer des jeux

Il y a vraiment très peu d'options lorsqu'il s'agit de développement de jeux indépendants. Les trois principaux choix si vous voulez créer des jeux sont Unreal, Unity ou GameMaker.

Unity est probablement la plateforme la moins restrictive des trois. Il vous offre un produit très brut dès la sortie de la boîte, mais il est très flexible, bien documenté et hautement extensible pour construire pratiquement n'importe quel genre de jeu auquel vous pouvez penser.

Il existe de nombreux jeux très réussis tels que Escape from Tarkov (FPS), Monument Valley (Puzzle), et This War of Mine (Stratégie/Survie), tous construits avec Unity.

En réalité, le moteur sur lequel vous construisez votre premier jeu n'est probablement pas critique, donc mon conseil est de simplement en choisir un et de vous y tenir.

#### Si vous voulez prototyper des expériences utilisateur

Puisque Unity est simplement un moteur avec un ensemble de physique, d'animation et de rendu 3D en temps réel, c'est aussi un excellent espace pour créer des prototypes interactifs complets pour des études UX.

Unity prend entièrement en charge la VR et la RA et pourrait donc être un excellent outil pour explorer l'architecture, les automatisations et les simulations avec des clients.

### **Sections de cet article**

* **Pourquoi Unity ?**
* **Fenêtre de l'éditeur Unity**
* **Objets de jeu Unity**
* **Composants intégrés de Unity**
* **Création de composants personnalisés**
* **Structure d'un MonoBehaviour**
* **Manipulation des GameObjects**
* **Raycasting**
* **Détection des collisions**
* **Fonctionnalités avancées**
* **Conseils pour les nouveaux venus**
* **Belles ressources et communautés**
* **Conclusion**

### **Fenêtre de l'éditeur Unity**

La fenêtre de l'éditeur est divisée en plusieurs sections. Nous allons couvrir cela très brièvement car nous allons nous y référer constamment tout au long de l'article. Si vous êtes déjà familier avec cela, passez simplement à la suite !

![Image](https://cdn-media-1.freecodecamp.org/images/hOKvEBDHVZj2N1udUtho7ksnzXmcdbMTWAWh)

> **Vue de la scène** : Permet le placement et le mouvement des GameObjects dans la scène

> **Vue du jeu** : Aperçu de la manière dont le joueur verra la scène depuis la caméra

> **Inspecteur** : Fournit des détails sur le GameObject sélectionné dans la scène.

> **Actifs / Projet** : Tous les préfabriqués, textures, modèles, scripts, etc. sont stockés ici

> **Hiérarchie** : Permet l'imbrication et la structuration des GameObjects dans la scène

Maintenant, nous sommes prêts à commencer !

### Objets de jeu Unity

#### Qu'est-ce que les GameObjects

Les GameObjects sont les éléments de base de tout dans le moteur de jeux Unity. Le nom le suggère presque :

> Tout ce que vous placez dans une scène dans Unity doit être enveloppé dans un « game object ».

Si vous avez un background en design web, vous pouvez penser aux GameObjects comme étant très similaires aux éléments <div> ! Des conteneurs extrêmement ennuyeux, mais hautement extensibles pour créer des fonctionnalités ou des visuels complexes.

![Image](https://cdn-media-1.freecodecamp.org/images/vlXNfFyr4lsQgC-DL05daoOtSWT35ZFUcA1l)
_Je l'ai pris directement depuis la fenêtre de l'éditeur Unity juste pour illustrer ce point._

Littéralement tout, des effets de particules, caméras, joueurs, éléments d'interface utilisateur, ... (la liste est longue) est un GameObject.

#### Création de hiérarchie

Comme un <div> en développement web, un GameObject est également un conteneur. Tout comme vous imbriquez des <div> pour créer des mises en page variées et souhaitables ou des abstractions que vous pourriez vouloir faire de même avec les objets de jeu.

> La logique derrière l'imbrication des objets de jeu est très similaire au développement web, je vais donner quelques exemples...

**Encombrement et efficacité**

> **_Analogie Web_** : _Vous avez de nombreux éléments similaires qui peuvent être générés dynamiquement à la volée en réponse à l'interaction de l'utilisateur et vous voulez les garder organisés._

> **_Traduction Unity_** : _Vous construisez un clone de Minecraft et vous avez des tonnes de blocs dans la scène, vous devez ajouter et supprimer des « chunks » de blocs de la scène pour des raisons de performance. Ainsi, les avoir parentés à un GameObject vide pour chaque chunk a du sens, car supprimer le parent du chunk supprime tous les blocs enfants._

**Positionnement**

> **_Analogie Web_** : _Vous voulez garder la position du contenu contenu « relative » au conteneur et non à la page web._

> **_Traduction Unity_** : _Vous avez créé un tas de drones d'assistance qui flottent autour du joueur. Vous ne voulez vraiment pas écrire de code pour leur dire de poursuivre le joueur, alors vous les instanciez comme enfants de l'objet de jeu du joueur._

### Composants intégrés de Unity

#### Le modèle de composant d'acteur

Les GameObjects seuls sont assez inutiles — comme nous l'avons vu, ils sont presque juste des conteneurs. Pour leur ajouter des fonctionnalités, nous devons ajouter des composants, qui sont essentiellement des scripts écrits en C# ou en Javascript.

Unity fonctionne selon un modèle de composant d'acteur, en résumé, les GameObjects sont les acteurs et les composants sont vos scripts.

Si vous avez déjà écrit des applications web, vous serez familier avec l'idée de créer de petits composants réutilisables tels que des boutons, des éléments de formulaire, des mises en page flexibles qui ont diverses directives et propriétés personnalisables. Ensuite, assembler ces petits composants en pages web plus grandes.

Le grand avantage de cette approche est le niveau de réutilisabilité et les canaux de communication clairement définis entre les éléments. De même, en développement de jeux, nous voulons minimiser le risque d'effets secondaires non intentionnels. Les petits bugs ont tendance à s'aggraver si vous n'êtes pas prudent, et sont extrêmement difficiles à déboguer. Ainsi, créer de petits composants robustes et réutilisables est crucial.

#### Composants intégrés clés

Je pense qu'il est temps de donner quelques exemples des composants intégrés fournis par le moteur de jeux Unity.

* **MeshFilter** : Permet d'assigner des matériaux à un maillage 3D à un GameObject
* **MeshRender** : Permet d'assigner des matériaux à un maillage 3D
* **[Box | Mesh]Collider** : Active la détection du GameObject lors des collisions
* **Rigidbody** : Active la simulation physique réaliste pour agir sur les GameObjects avec des maillages 3D et déclenchera des événements de détection sur les colliders de boîte
* **Light** : Illumine des portions de votre scène
* **Camera** : Définit le viewport du joueur à attacher à un GameObject
* Divers composants de canevas UI pour afficher les interfaces graphiques

Il y en a beaucoup d'autres, mais ce sont les principaux avec lesquels vous devez vous familiariser. Un conseil est que vous pouvez accéder à toute la documentation pour ceux-ci via le manuel Unity et la référence de script hors ligne où que vous soyez :

![Image](https://cdn-media-1.freecodecamp.org/images/CNB5Rb4DWImRiHh04xThXYtZnojyCj5OJJ1f)
_Il suffit de cliquer sur la section d'aide, les docs en général sont assez bonnes_

### Création de composants personnalisés

Les composants intégrés contrôlent principalement la physique et les visuels, mais pour vraiment créer un jeu, vous devrez accepter les entrées de l'utilisateur et manipuler ces composants standard ainsi que les GameObjects eux-mêmes.

> Pour commencer à créer des composants, allez dans le GameObject souhaité > Ajouter un composant > tapez le nom de votre nouveau composant dans la barre de recherche > nouveau script (c#).

En général, je déconseille d'utiliser JavaScript dans Unity. Il n'a pas été mis à jour avec toutes les grandes fonctionnalités qui sont venues avec ES6, et la plupart des choses plus avancées reposent sur des éléments C# portés vers JavaScript... Cela devient simplement un énorme contournement selon mon expérience.

### Structure d'un MonoBehaviour

#### Fonctions clés

Tous les composants héritent de la classe MonoBehaviour. Elle inclut plusieurs méthodes standard, les plus importantes étant :

* **void Start()** qui est appelée chaque fois qu'un objet contenant le script est instancié dans la scène. Cela est utile chaque fois que nous voulons exécuter un code d'initialisation, par exemple, définir l'équipement d'un joueur après qu'il ait été généré dans une partie.
* **void Update()** qui est appelée à chaque frame. C'est ici que la majorité du code impliquant les entrées de l'utilisateur sera placée, mettant à jour diverses propriétés telles que le mouvement du joueur dans la scène.

#### Variables de l'inspecteur

Souvent, nous voulons rendre les composants aussi flexibles que possible. Par exemple, toutes les armes peuvent avoir des dégâts différents, une cadence de tir, un has_sight, etc. Bien que toutes les armes soient essentiellement la même chose, nous pouvons vouloir créer différentes variations rapidement via l'éditeur Unity.

Un autre exemple où nous pouvons vouloir faire cela est lors de la création d'un composant UI qui suit les mouvements de la souris de l'utilisateur et place un curseur dans le viewport. Ici, nous pouvons vouloir contrôler la sensibilité du curseur aux mouvements (si l'utilisateur utilise un joystick ou une manette de jeu par rapport à une souris d'ordinateur). Ainsi, il serait logique d'avoir ces variables faciles à changer à la fois en mode édition et aussi expérimenter avec elles pendant l'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/ARiWcy5AEsVyRicp7demoZnzQR0MjPQnFzXJ)
_Les variables dans la fenêtre de l'inspecteur peuvent être modifiées à tout moment pendant l'exécution ou le mode édition. Remarque : Les modifications apportées pendant l'exécution ne seront pas permanentes._

Nous pouvons faire cela facilement en les déclarant simplement comme des variables publiques dans le corps du composant.

![Image](https://cdn-media-1.freecodecamp.org/images/dMqFuop796E9p2Y4urYkJtsuM3Rh6oM07cIJ)
_Remarquez comment nous pouvons faire en sorte que les variables aient différents niveaux d'accès, privé, public, ou public mais non affiché dans la fenêtre de l'inspecteur._

#### Accepter les entrées de l'utilisateur

Bien sûr, nous voulons que notre jeu réponde aux entrées de l'utilisateur. Les méthodes les plus courantes pour le faire sont les suivantes dans la fonction Update() d'un composant (ou ailleurs si vous le souhaitez) :

* Input.GetKey(KeyCode.W) Retourne True si la touche W est maintenue enfoncée
* Input.GetKeyDown(KeyCode.W) Retourne True lorsque la touche W est pressée pour la première fois
* Input.GetAxis("Vertical"), Input.GetAxis("Horizontal") Retourne entre -1,1 le mouvement de la souris

### Manipulation des GameObjects

Une fois que nous avons les entrées de l'utilisateur, nous voulons que les GameObjects dans notre scène répondent. Il existe plusieurs types de réponses que nous pouvons considérer :

* Translation, Rotation, Mise à l'échelle
* Créer de nouveaux GameObjects
* Envoyer des messages à des GameObjects / composants existants

#### Transformations

Les GameObjects ont tous une propriété de transformation qui permet d'effectuer diverses manipulations utiles sur l'objet de jeu actuel.

![Image](https://cdn-media-1.freecodecamp.org/images/cqutjhXkSZxKNCywMSjGbxewqeDo5GCp0R-d)

Les méthodes ci-dessus sont assez explicites, notez simplement que nous utilisons _gameObject_ en minuscules pour faire référence au GameObject qui possède cette instance spécifique du composant.

En général, il est bon de pratiquer l'utilisation de _local[Position,Rotation]_ plutôt que la position/rotation globale d'un objet. Cela rend généralement plus facile le déplacement des objets de manière logique, car l'axe de l'espace local sera orienté et centré sur l'objet parent plutôt que sur l'origine du monde et les directions x, y, z.

![Image](https://cdn-media-1.freecodecamp.org/images/sgr4nHfYLQYqjEEPSxlxPA0BhCrNjgzzvOmW)
_Les avantages de l'espace local deviennent un peu plus évidents avec un diagramme !_

Si vous devez convertir entre l'espace local et l'espace mondial (ce qui est souvent le cas), vous pouvez utiliser ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/vNEw9xUc-B2vZOaeAqXcQn5W-lxfmJbLiEZw)

Comme vous pouvez l'imaginer, il y a un peu d'algèbre linéaire assez simple derrière cela, suggéré par le mot « Inverse » dans le nom de la méthode.

#### Création de nouveaux GameObjects

Puisque les GameObjects sont essentiellement tout dans votre scène, vous pourriez vouloir les générer à la volée. Par exemple, si votre joueur a un lanceur de projectiles, vous pourriez vouloir créer des projectiles à la volée qui ont leur propre logique encapsulée pour le vol, infliger des dégâts, etc.

Tout d'abord, nous devons introduire la notion de _Prefab_. Nous pouvons créer ceux-ci simplement en faisant glisser n'importe quel GameObject de la hiérarchie de la scène dans le dossier des actifs.

![Image](https://cdn-media-1.freecodecamp.org/images/BEBGqpePGsVgtEY5y89WrnLAbdZjPHZiagjZ)
_À quoi ressemble un prefab dans l'onglet Actifs_

Cela stocke essentiellement un modèle de l'objet que nous avions dans notre scène avec toutes les mêmes configurations.

![Image](https://cdn-media-1.freecodecamp.org/images/wFLWTKOYgxfMEAEzUjgMsTCETSmTA3JIPLGp)
_Un exemple d'objet de brique personnalisé qui est utilisé pour générer dynamiquement des briques Lego dans une scène, il a un tas de composants attachés avec diverses valeurs par défaut._

Une fois que nous avons ces composants prefab, nous pouvons les assigner à des variables d'inspecteur (comme nous en avons parlé plus tôt) sur n'importe quel composant dans la scène, afin que nous puissions créer de nouveaux GameObjects comme spécifié par le prefab à tout moment.

Nous pouvons ensuite effectuer l'« instanciation » du prefab et le manipuler à l'emplacement souhaité dans la scène et établir les relations parent nécessaires.

![Image](https://cdn-media-1.freecodecamp.org/images/xAzUlbgEAIkyS8bsX8W0xlVI0YiSTiVyMljj)

### Accéder à d'autres GameObjects et composants

Souvent, nous devons communiquer avec d'autres GameObjects ainsi qu'avec leurs composants associés. Une fois que vous avez une référence à un objet de jeu, cela est assez simple.

> ComponentName comp = some_game_object.GetComponent<ComponentName>();

Après cela, vous pouvez accéder à toutes les méthodes/variables publiques du composant afin de manipuler le GameObject. C'est la partie simple, cependant, obtenir la référence au GameObject peut être fait de plusieurs manières...

#### Accès via une variable d'inspecteur

C'est la méthode la plus simple. Il suffit de créer une variable publique pour le GameObject, comme nous l'avons démontré plus tôt avec les prefabs, et de le faire glisser et déposer manuellement sur le composant via l'inspecteur. Ensuite, accédez à la variable comme ci-dessus.

#### Accès via l'étiquetage

Nous pouvons étiqueter les GameObjects ou les prefabs via l'inspecteur, puis utiliser les fonctions de recherche de GameObject pour localiser les références à ceux-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/9Ur13zYuVV3r17CGo9hDMnyCoG44jTXCwv4g)

Cela se fait simplement comme ci-dessous.

> GameObject some_game_object = GameObject.FindGameObjectWithTag("Brick");

#### Accès via la transformation

Si nous souhaitons accéder aux composants dans un objet parent, nous pouvons facilement le faire via l'attribut de transformation.

> ComponentName comp = gameObject.transform.parent.GetComponent<ComponentName>();

#### Accès via SendMessage

Alternativement, si nous voulons envoyer un message à de nombreux autres composants ou souhaitons envoyer un message à un objet qui est loin dans une hiérarchie imbriquée, nous pouvons utiliser les fonctions d'envoi de message, qui acceptent le nom de la fonction suivi des arguments.

> gameObject.SendMessage("MethodName",params); // Diffuser le message

> gameObject.SendMessageUpwards("MethodName", params); // Reçu uniquement par les composants qui sont imbriqués au-dessus.

### Raycasting

Vous avez peut-être déjà entendu parler de cela lorsque les gens comparent les jeux FPS qui sont « basés sur la physique » ou « basés sur les rayons ». Le raycasting est essentiellement comme avoir un pointeur laser qui, lorsqu'il entre en contact avec un « collider » ou un « rigidbody », retourne un « hit » et renvoie les détails de l'objet.

Il y a deux scénarios où cela s'avère utile (il y en a probablement beaucoup d'autres) :

1. Si vous conceviez un système d'armes pour un jeu, vous pourriez utiliser le raycasting pour la détection des impacts, et même personnaliser la longueur du rayon de sorte que les objets de mêlée « frappent » uniquement à courte portée.
2. Créer un rayon à partir du pointeur de la souris vers un point dans l'espace 3D, c'est-à-dire si vous souhaitez que l'utilisateur puisse sélectionner des unités avec sa souris dans un jeu de stratégie.

![Image](https://cdn-media-1.freecodecamp.org/images/GcxZnE2hbosbWwoDp94ecEd1g8aVlwrFKOhB)
_Exemple 2 détaillé ci-dessus_

Comme vous pouvez le voir, le code pour cela est un peu plus impliqué. La chose clé à comprendre est que pour lancer un rayon vers l'endroit où la souris pointe dans l'espace 3D nécessite la transformation ScreenPointToRay. La raison en est que la caméra rend un espace 3D comme un viewport 2D sur l'écran de votre ordinateur portable, donc naturellement il y a une projection impliquée pour revenir en 3D.

### Détection des collisions

Plus tôt, nous avons mentionné les composants Collider et Rigidbody qui peuvent être ajoutés à un objet. La règle pour les collisions est qu'un objet dans la collision doit avoir un rigidbody et l'autre un collider (ou les deux ont les deux composants). Notez que lors de l'utilisation du raycasting, les rayons n'interagiront qu'avec les objets ayant des composants collider attachés.

Une fois configuré dans n'importe quel composant personnalisé attaché à l'objet, nous pouvons utiliser les méthodes OnCollisionEnter, OnCollisionStay et OnCollisionExit pour répondre aux collisions. Une fois que nous avons les informations de collision, nous pouvons obtenir le GameObject responsable et utiliser ce que nous avons appris précédemment pour interagir avec les composants qui y sont attachés.

![Image](https://cdn-media-1.freecodecamp.org/images/ppKZgvdAjKDqbW80Nin2wG9izk08UjyuaqAt)

Une chose à noter est que les rigid-bodies fournissent une physique telle que la gravité pour les objets, donc si vous voulez désactiver cela, vous devrez cocher _is_kinematic_.

![Image](https://cdn-media-1.freecodecamp.org/images/I9UU3oy-UoVWOwjhXUy9PRiGDT5eFO4O9-IB)
_Cochez is kinematic pour désactiver la physique indésirable mais conserver une belle détection des collisions._

### Fonctionnalités avancées

Nous n'allons pas approfondir cela maintenant, mais peut-être dans un futur article — juste pour vous faire savoir qu'elles existent.

#### Création d'interfaces graphiques

Unity dispose d'un moteur UI complet pour organiser l'interface graphique de votre jeu. En général, ces composants fonctionnent de manière assez similaire au reste du moteur.

#### Extension de l'éditeur Unity

Unity vous permet d'ajouter des boutons personnalisés à vos inspecteurs afin que vous puissiez affecter le monde en mode édition. Par exemple, pour aider à la construction du monde, vous pourriez développer une fenêtre d'outil personnalisée pour construire des maisons modulaires.

#### Animation

Unity dispose d'un système d'animation basé sur des graphes qui vous permet de mélanger et de contrôler les animations sur divers objets tels que les joueurs mettant en œuvre un système d'animation basé sur les os.

#### Matériaux et PBR

Unity fonctionne avec un moteur de rendu basé sur la physique qui permet un éclairage en temps réel et des matériaux réalistes. La réalité est que vous devrez soit apprendre la modélisation 3D d'abord, soit utiliser des modèles faits et optimisés par quelqu'un d'autre avant d'en arriver là, afin de créer des choses qui ont vraiment l'air bien.

### Conseils pour les nouveaux venus

Si vous prévoyez d'écrire votre premier jeu, ne sous-estimez pas la complexité et le temps qu'il faut pour écrire même les jeux les plus triviaux. N'oubliez pas que la plupart des jeux qui sortent sur Steam ont des équipes qui travaillent dessus à temps plein pendant des années !

Choisissez un concept simple et décomposez-le en petites étapes réalisables. Il est fortement recommandé de séparer votre jeu en composants indépendants aussi petits que possible, car vous avez beaucoup moins de chances de rencontrer des bugs si vous gardez les composants simples plutôt que des blocs de code monolithiques.

Avant d'écrire du code pour une partie quelconque de votre jeu, allez faire des recherches sur ce que quelqu'un d'autre a fait auparavant pour résoudre le même problème — il y a de fortes chances qu'ils aient une solution beaucoup plus élégante.

### Ressources et communautés utiles

La conception de jeux possède l'une des meilleures communautés qui soit, et il y a de nombreux professionnels hautement qualifiés dans l'industrie qui mettent du contenu en ligne gratuitement ou pour presque rien. C'est un domaine qui nécessite des modeleurs 3D, des artistes conceptuels, des concepteurs de jeux, des programmeurs, etc. J'ai lié quelques excellentes ressources générales que j'ai rencontrées pour chacun de ces domaines ci-dessous :

**Art conceptuel**

* [Feng Zhu Design School](https://www.youtube.com/channel/UCbdyjrrJAjDIACjCsjAGFAA) (Plus de 90 heures de tutoriels d'art conceptuel)
* [Tyler Edlin Art](https://www.youtube.com/channel/UCm9pCim4dDN4KJZUILGizgA) (Excellente communauté d'art BST avec des retours de pros sur les défis mensuels)
* [Art Cafe](https://www.youtube.com/channel/UCyGGrJ-wQlvcWujLKHzB42w) (Interviews et ateliers avec des artistes conceptuels célèbres)
* [Trent Kaniuga](https://www.youtube.com/channel/UCmRm1xtLIpBhuWjTyD411pA) (Illustrateur et artiste 2D qui crée aussi son propre jeu)

**Modélisation 3D**

* [CG Cookie](https://cgcookie.com/course/mesh-modeling-bootcamp/?utm_source=youtube&utm_medium=social&utm_campaign=course&utm_term=description&utm_content=modeling-bootcamp-lessons) (Meilleurs bases de modélisation de maillage dans Blender, ils ont beaucoup d'autres excellents contenus pour Blender)
* [Tor Frick](https://www.youtube.com/channel/UCDmOobbSOonY66M6fsJO7GQ) (Modeleurs de surface dure et sculpteurs dans Blender)
* [Gleb Alexandrov](https://www.youtube.com/channel/UCVA3cYOgsTN4hs3v7pjne7w) (Tutoriels de rendu puissants et courts dans Blender)

**Conception de jeux**

* [DoubleFine Amnesia Fortnight](https://www.youtube.com/watch?v=juJikoClDxw&list=PLIhLvue17Sd7riA8vb8h1kP3jCFS_qtTM) (Développeurs de jeux qui font un hackathon de 2 semaines et enregistrent leur processus de conception entier)
* [GameMakers Toolkit](https://www.youtube.com/channel/UCqJ-Xo29CKyLTjn6z2XwYAw) (Examine les principes de conception de jeux)

**Programmation**

* [Handmade Hero](https://www.youtube.com/channel/UCaTznQhurW5AaiYPbhEA-KA) (Écrire un jeu et un moteur à partir de zéro en C)
* [Jonathan Blow](https://www.youtube.com/channel/UCCuoqzrsHlwv1YyPKLuMDUQ) (Développeur indépendant qui diffuse en direct son développement de jeu)
* [Brackeys](https://www.youtube.com/channel/UCYbK_tjZ2OrIZFBvU6CCMiA) (Bons tutoriels Unity)

### Conclusion

J'espère que vous avez aimé ce tutoriel ! Je fais aussi un peu de design graphique ainsi que des prototypes de jeux et d'interfaces utilisateur, alors consultez [mon portfolio](http://hugodolan.com/portfolio) ! Je suis aussi sur LinkedIn.

[**Portfolio**](https://hugodolandesigns.portfoliobox.net) | [**LinkedIn**](https://www.linkedin.com/in/hugo-dolan-62971a174/)

![Image](https://cdn-media-1.freecodecamp.org/images/NwkVR7XrAVlrJUTy9x0Cc30JmbmpAayM69HK)
_[http://eepurl.com/gkV7ov](http://eepurl.com/gkV7ov)_