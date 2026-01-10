---
title: Comment construire un tableau de bord pour votre grill en utilisant Arduino
  et React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-17T03:23:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-dashboard-for-your-grill-using-arduino-and-react-425fb8d57ffe
coverImage: https://cdn-media-1.freecodecamp.org/images/0*KEM-bv3KNV0n6l2H.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment construire un tableau de bord pour votre grill en utilisant Arduino
  et React
seo_desc: 'By Chris Aquino

  “When should I use React?” My students at DigitalCrafts have been asking me this
  question a lot lately.

  We’re three months into the bootcamp and two days into React. Several students have
  commented that React has a weird mix that comb...'
---

Par Chris Aquino

« Quand devrais-je utiliser React ? » Mes étudiants à [DigitalCrafts](http://www.digitalcrafts.com/) me posent beaucoup cette question dernièrement.

Nous en sommes à trois mois dans le bootcamp et à deux jours dans React. Plusieurs étudiants ont commenté que React a un mélange étrange qui combine le familier avec l'étranger.

Et naturellement. Cela ressemble à un mélange bizarre de JavaScript et de HTML, tout en ayant les sensibilités de rendu unidirectionnel d'Express et de Handlebars.

Ma réponse favorite est les tableaux de bord. React est idéal pour créer des panneaux qui mettent à jour indépendamment les informations. C'est le genre d'interfaces utilisateur qui est un cauchemar à construire avec jQuery.

Ensuite, ils demandent : « Ok, comme quoi ? »

Et puis je leur montre... PitMaster.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Q-zIUhFXWgp8SZeS.png)
_PitMaster ! Regardez-le dans toute sa majesté._

D'abord, une confession : j'ai un amour démesuré pour le barbecue. Si je ne mange pas de barbecue, je prépare un barbecue. (Dans le sud des États-Unis, le barbecue est un nom, pas un verbe. C'est le processus d'exposition de la viande à une fumée à basse température pendant des heures.)

Le dernier Thanksgiving, en prévision d'être extrêmement paresseux, j'ai construit un dispositif qui surveille la progression de la cuisson de la dinde dans un fumoir. Les résultats étaient affichés en temps réel sur une page web. Certes, une dinde ne prend pas longtemps à cuire par rapport à d'autres types de viande. Et je ne suis vraiment pas _si_ paresseux, mais j'avais une vision plus grande en tête.

Imaginez ceci : vous êtes à 12 heures d'un fumage de 18 heures, et vous préféreriez vraiment ne pas quitter le canapé pour vérifier la température encore une fois. De plus, vous ne devriez pas ouvrir le fumoir pendant la cuisson, ce qui provoquerait une fluctuation massive de la température.

Les détails du matériel pourraient remplir un autre article de blog, mais voici un croquis approximatif.

![Image](https://cdn-media-1.freecodecamp.org/images/0*VszihuplAb_5KpqT.png)

Enfoncez une résistance thermique (thermistor) à haute température et sûre pour les aliments dans la nourriture juste avant de la placer dans le fumoir. Un thermistor est un morceau de matériel qui change sa conductivité électrique lorsque sa température change. Un long fil relie le thermistor à un Arduino.

L'Arduino exécute un programme qui convertit la lecture analogique du thermistor en une valeur numérique. Un Raspberry Pi interroge l'Arduino pour cette valeur toutes les quelques 100 millisecondes, la journalise dans un fichier, puis la pousse à tout client connecté via WebSocket.

Cela peut sembler sophistiqué, mais voici à quoi ressemble réellement le dispositif.

![Image](https://cdn-media-1.freecodecamp.org/images/0*KEM-bv3KNV0n6l2H.png)
_Voyez la diode électroluminescente (LED) rouge ? Ma femme a surnommé le dispositif « Roxanne »._

À l'origine, l'interface utilisateur pour afficher la température actuelle était, pour le dire simplement, vraiment laide. C'était précisément ce que vous verriez dans un tutoriel « Hello World », consistant en un seul `h1` non stylisé dans toute sa gloire Times New Roman.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_HG8JHAq9_T6e327.png)
_Ce design n'est pas susceptible de remporter des rubans bleus._

J'ai donc construit `PitMaster`, un tableau de bord qui surveille la progression des fumoirs. Vous pouvez obtenir une copie du code [ici](https://github.com/radishmouse/react-pit-master).

Dans cet article, je vais passer en revue quelques concepts clés qui m'ont échappé lorsque j'ai commencé à apprendre React.

### Aperçu

Malgré tout le battage autour des « interfaces utilisateur fonctionnelles et déclaratives » et de la « différenciation du DOM virtuel », je me concentre sur ces trois directives lors de la construction avec React :

* Données en entrée, interface utilisateur en sortie
* Construisez vos composants de bas en haut et passez les données de haut en bas
* Rendez vos composants aussi simples que possible, mais pas plus simples

Avec ces directives en tête, examinons l'interface utilisateur.

### Esquisse de PitMaster

Voici un fil de fer de base de l'interface utilisateur de PitMaster :

![Image](https://cdn-media-1.freecodecamp.org/images/0*2cuU0_cHzoSkkD2a.png)

Comme recommandé dans l'excellente page [Thinking in React](https://facebook.github.io/react/docs/thinking-in-react.html), la meilleure façon de commencer est de faire une décomposition visuelle de votre interface utilisateur.

PitMaster est une application divisée en deux parties : un formulaire qui peut être utilisé pour ajouter des commandes et un panneau qui affiche l'état actuel de chaque commande.

![Image](https://cdn-media-1.freecodecamp.org/images/0*WlY3_yLVxx6bSGKZ.png)

Le formulaire peut être divisé en trois parties :

* Menu déroulant avec les différents types d'aliments
* Champ de texte pour entrer le nom de la personne qui commande la nourriture
* Bouton de soumission pour soumettre le formulaire

![Image](https://cdn-media-1.freecodecamp.org/images/0*qKdwJRgF4LF6goiU.png)

Le panneau ne contient qu'un « moniteur » individuel pour une commande de nourriture. Ceux-ci semblent plus complexes, mais ils ne font pas grand-chose d'autre qu'afficher du texte et des nombres. Nous commencerons par ceux-ci, car ils démontrent l'idée la plus fondamentale de React : transformer les données en une interface utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*0Vtds2qpGzQr9b0v.png)

### Utilisation de fonctions pour transformer les données en composants d'interface utilisateur

React se prête parfaitement aux principes de conception atomique. Cela n'a rien à voir avec la physique nucléaire et tout à voir avec un mouvement récent dans la conception d'interfaces utilisateur. Dans la [conception atomique](http://bradfrost.com/blog/post/atomic-web-design/), vous commencez par concevoir les plus petits composants visuels, puis vous les composez en composants de plus en plus grands. Cela vous donne l'opportunité de réutiliser des composants dans d'autres parties de votre interface utilisateur. En fin de compte, c'est moins de travail et cela crée une cohérence dans toute votre interface utilisateur.

Dans PitMaster, vous pouvez voir que la lecture de la température est la plus petite, donc je vais commencer par là. Un autre bon candidat est le NameLabel, mais la lecture est réutilisée plus souvent.

### Construction du composant Readout

Un `Composant` dans React est quelque chose qui accepte des données et retourne une description de l'interface utilisateur qui affiche ces données. Les fonctions sont exactement l'outil qu'il faut pour le travail. Le composant `Readout` ne sera rien de plus qu'une fonction qui accepte du texte, des nombres comme arguments, et retourne un `<span>` avec ces valeurs à l'intérieur.

Voici la version la plus simple de cela :

Il y a deux choses à noter à ce sujet.

Premièrement, toute donnée passée à un composant est regroupée dans un objet appelé `props`. Par conséquent, `label` et `value` doivent être accessibles en tant que propriétés de l'objet `props`.

Deuxièmement, vous ne créez pas réellement des éléments DOM, vous créez des éléments React, qui sont des **descriptions** d'éléments DOM. Cela va sembler très différent si vous êtes habitué à construire des interfaces utilisateur avec jQuery, où vous créez soit des éléments DOM, soit vous référencez des éléments DOM existants. Les raisons de cela deviendront plus apparentes bientôt.

La description `React.createElement('span', null, props.label, props.value)` signifie que le type d'élément DOM est un `span`.

Nous ne lui passons aucun `props`, et imbriqués à l'intérieur de `span` se trouvent les valeurs `props.label` et `props.value`.

Les valeurs qui sont imbriquées à l'intérieur d'un élément React sont appelées **enfants**.

#### Fonctions fléchées et déstructuration

Il existe une syntaxe alternative pour les fonctions qui est largement utilisée dans de nombreuses bases de code React. Les **fonctions fléchées** ES6 sont les mêmes que les fonctions anonymes, mais avec une syntaxe plus courte. (Parce que les programmeurs détestent appuyer sur plus de touches que nécessaire !)

Dans le prochain extrait de code, une valeur de fonction fléchée est assignée à la variable `Readout`, qui est déclarée en utilisant `const`, et non `var`.

Une `const` est une variable qui ne peut pas être réassignée.

Mais attendez, il y a plus !

Nous pouvons utiliser la syntaxe de déstructuration ES6 pour extraire des valeurs spécifiques de l'argument `props` et les assigner à des variables locales, le tout en une seule étape.

React exige que vos composants retournent un seul élément. Avec les fonctions fléchées, si le corps ne contient qu'une seule instruction et qu'il s'agit d'une instruction `return`, alors vous pouvez omettre les accolades et le mot-clé `return`. La valeur à droite de la flèche est implicitement `return`ée.

Parce que la valeur de `return` peut devenir longue, vous verrez du code qui ressemble à ceci, où des parenthèses ont été ajoutées autour de la valeur de retour implicite :

C'est la même chose, mais cela permet au programmeur de faire ce qu'il veut avec les espaces blancs.

### JSX ou « Pourquoi y a-t-il du HTML dans mon JavaScript ? »

Il y a une autre abstraction à ajouter. Peut-être devrons-nous mettre `span` à l'intérieur d'un `div` à des fins de style :

Pour ce faire, nous devons écrire le code suivant en JavaScript :

Comme vous pouvez l'imaginer, lorsque nous essayons de décrire des structures DOM plus complexes, les appels imbriqués `React.createElement` peuvent rapidement devenir ingérables. Heureusement, React vous permet d'utiliser une syntaxe optionnelle pour `React.createElement` qui ressemble beaucoup au HTML. Voici ce composant réécrit en utilisant cette syntaxe :

Cette syntaxe est JSX, qui est du XML intégré dans notre JavaScript. Avant que le navigateur n'exécute le JavaScript, le XML est transformé en appels de fonction `React.createElement` imbriqués. De plus, les accolades, ainsi que toutes les variables ou expressions JavaScript à l'intérieur des accolades, sont évaluées et les valeurs résultantes sont substituées.

L'avantage ici est que toute personne familiarisée avec le HTML peut jeter un coup d'œil au JSX et savoir quels éléments DOM seront produits.

### Composants personnalisés

Ce qui est pratique avec `React.createElement`, c'est que vous n'êtes pas limité à la description des éléments HTML. Une fois que vous avez créé un composant comme `Readout`, vous pouvez l'utiliser avec `React.createElement` ou avec JSX.

Voici la liste complète du code pour le composant qui affiche trois températures récentes à partir de trois intervalles de temps différents (1 minute, 5 minutes et 10 minutes).

Vous pouvez mélanger vos composants personnalisés avec les composants HTML natifs. N'oubliez pas que vos composants `Readout` produisent des éléments qui sont un `span` à l'intérieur d'un `div`.

Et pour passer des arguments, par exemple `props`, à un composant personnalisé, vous pouvez utiliser une syntaxe qui ressemble à des attributs HTML :

Si vous regardez `Monitor.js`, vous pouvez voir qu'il s'agit d'une combinaison de `Readout`, `TemperatureHistory`, `NameLabel` et de composants HTML :

À ce stade, il devrait être clair que les composants ne sont rien de plus qu'un raccourci pour les appels imbriqués à `React.createElement`. Chaque composant reçoit des données (`props`) de son parent et transmet des données à ses enfants. Toutes les données affichées dans une application React ont été initialement transmises à l'élément racine, le plus haut.

Mais la question devient alors, quel est le résultat de tous ces appels de fonction ?

### Démystifier le DOM virtuel

La réponse est que tous ces appels imbriqués `React.createElement` résultent en un grand objet JavaScript, également connu sous le nom d'arbre d'éléments. Voici l'arbre d'éléments produit à partir de `<TemperatureHistory valueArray=[154, 132, 126]` /> :

React utilise l'arbre d'éléments pour créer des éléments DOM réels et les rendre sur la page. C'est ce que signifie le terme **DOM virtuel**. L'arbre d'éléments sert de plan pour le DOM, et React peut s'y référer au besoin pour mettre à jour la page.

### Mise à jour du DOM

D'accord, un certain temps passe et le barbecue progresse vers une délicieuse bonté. À mesure que les lectures de température changent, l'interface utilisateur change également. Supposons que seule la première valeur de l'historique des températures a changé (de 154 à 156) :

`<TemperatureHistory valueArray=[156, 132, 126]` />

Lorsque les données changent, les nouvelles valeurs sont transmises au composant racine, et les données se propagent dans l'arbre des composants. Cela entraîne un nouvel arbre d'éléments.

Voici l'arbre d'éléments résultant :

React fait ensuite quelque chose de très intelligent. Il compare cet nouvel arbre d'éléments au précédent. Il détermine ensuite le nombre minimal d'endroits dans le DOM qu'il doit mettre à jour. Il calcule littéralement la différence entre les deux arbres afin de faire le _moins de travail possible_ pour s'assurer que le DOM reflète la version la plus récente des données. (Vous devriez être en train de paniquer maintenant parce que c'est vraiment incroyable.)

La question suivante est, si tout dans l'arbre d'éléments est une valeur statique, comment et où suivons-nous les données de l'application ?

Un bon exemple de composant qui doit suivre les données de l'application est le `FoodChooserForm`. À mesure que l'utilisateur entre des informations dans le formulaire, les données du formulaire changent, et cela provoque techniquement le rendu des éléments du formulaire. Mais nous devons nous assurer que tout ce que l'utilisateur a entré jusqu'à présent est conservé.

### Ajout de composants de classe

Jusqu'à présent, nous n'avons examiné que des composants qui sont des fonctions. Plus précisément, ceux-ci sont connus sous le nom de [**composants fonctionnels sans état**](https://facebook.github.io/react/docs/components-and-props.html#functional-and-class-components). La plupart de vos composants seront de cette variété. Il existe un autre type de composant qui possède quelques capacités supplémentaires. Pour les créer, nous devrons utiliser la syntaxe de classe ES6.

Voici `FoodChooserForm`, montrant tout sauf l'arbre d'éléments qu'il produit.

Les classes en JavaScript ne sont vraiment que du [sucre syntaxique](https://en.wikipedia.org/wiki/Syntactic_sugar) pour les fonctions et les [prototypes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain). En général, les classes sont utilisées pour créer des versions spécialisées de types d'objets existants. Lorsqu'elles sont utilisées avec React, elles créent principalement des composants qui peuvent conserver l'état des données de l'application entre les rendus. `FoodChooserForm` est un exemple de **composant de classe avec état**.

Il hérite de `React.Component` et invoque `super(props)` dans son `constructeur`. De plus, notez qu'il initialise la variable d'instance `this.state`. La variable `state` est l'endroit où un composant de classe stocke ses données d'application. Il a deux autres méthodes `_updateOrderName` et `_updateFoodChoice`. Chacune de ces méthodes appelle `this.setState`, qui est une méthode fournie par `React.Component`. C'est la méthode que les composants de classe doivent utiliser pour apporter des modifications à la valeur de `this.state`. Vous lui passez un objet avec les paires clé/valeur à mettre à jour. React s'occupe du reste.

Voici le code complet du composant. Il inclut la définition de la méthode `render`, qui est équivalente à la valeur de retour d'un composant fonctionnel sans état.

Les méthodes `_updateOrderName`, `_updateFoodChoice` et `_handleSubmit` sont toutes préfixées par un trait de soulignement. Il s'agit d'une convention courante qui distingue les méthodes privées des méthodes héritées. Ces méthodes privées sont passées en tant que `props` aux gestionnaires d'événements des composants listés dans la méthode `render`. Ces composants recevront ces fonctions et les appelleront de manière aveugle lorsque ces événements seront déclenchés, provoquant ainsi un changement dans l'état de `FoodChooserForm`.

C'est ainsi que la plupart de vos composants peuvent être « stupides » tandis qu'une poignée d'entre eux peuvent être responsables de la maintenance de l'état. Vos composants stupides savent juste assez pour appeler ces fonctions et leur passer les bonnes informations. Dans ce cas, `FoodChooser` appelle `_updateFoodChoice` chaque fois que quelque chose est sélectionné dans son menu déroulant, et `NameLabel` appelle `_updateOrderName` lorsque l'utilisateur tape dans le champ de texte. `FoodChooserForm` reçoit la valeur la plus récente pour le choix de nourriture et le nom de la commande, et la sauvegarde via `this.setState`.

`FoodChooserForm` appelle également une fonction qui lui a été passée en tant que props. Dans le constructeur (où il reçoit toutes ses props), il sauvegarde une référence à `props.submitHandler` en tant que variable d'instance `this.submitHandler`. Dans la méthode `render`, il passe une référence à sa méthode `_handleSubmit` au composant `form`.

Lorsque l'événement de soumission du `form` est déclenché, `_handleSubmit` est appelé et les informations de l'événement lui sont passées. `FoodChooserForm` empêche le `form` de se soumettre (ce qui provoquerait le rechargement de la page). Ensuite, il appelle le `submitHandler`, lui passant la valeur actuelle de `this.state`. Enfin, il réinitialise la valeur de son `state`, réinitialisant effectivement le formulaire en effaçant les valeurs rendues.

Et où vont maintenant ces nouvelles informations de commande de nourriture ? Tout en haut.

### Le composant PitMaster

`PitMaster` maintient une liste de toutes les commandes de nourriture dans le cadre de son `state`, qu'il transmet au `MonitorPanel`. Il fournit à `FoodChooserForm` une liste de choix de nourriture et une fonction de rappel à utiliser chaque fois qu'une nouvelle commande a été passée. Sa méthode `render` est remarquablement concise :

Il possède des méthodes privées pour ajouter et supprimer des commandes, ainsi que pour mettre à jour la liste des températures. Tous les autres comportements ont été cachés dans d'autres composants.

### Conclusion

Apprendre React n'est pas une tâche facile, mais c'est plus facile une fois que vous voyez comment les modèles courants se rapportent aux fondamentaux de JavaScript. Les fonctions transforment vos données en votre interface utilisateur. Les petits composants doivent être composés en composants plus grands, et seuls quelques-uns d'entre eux doivent gérer l'état. Respectez ces directives et vous êtes sur la bonne voie pour maîtriser React.

Mes étudiants de [DigitalCrafts](http://www.digitalcrafts.com/) respirent un peu plus facilement alors qu'ils abordent courageusement un autre nouveau sujet dans le développement web. Ils savent qu'ils peuvent encore utiliser jQuery pour les petits travaux, construire un back-end avec Postgres et Express pour un site web rendu par le serveur, ou utiliser React pour des applications monopages basées sur des composants. Plus important encore, ils sont capables de prendre ces fondamentaux sur lesquels ils ont travaillé pendant de nombreuses heures et de les appliquer à la prochaine nouvelle chose brillante qui se présentera.

Maintenant, je me demande ce qu'ils me demanderont lorsque nous aborderons Redux la semaine prochaine...