---
title: Comment construire un système d'IA conversationnelle de bout en bout en utilisant
  des arbres de comportement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-12T15:48:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-end-to-end-conversational-ai-system-using-behavior-trees-658a7122e794
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gr-Ixi5QqOjf5bFR9ybNag.jpeg
tags:
- name: AI
  slug: ai
- name: bots
  slug: bots
- name: Machine Learning
  slug: machine-learning
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
seo_title: Comment construire un système d'IA conversationnelle de bout en bout en
  utilisant des arbres de comportement
seo_desc: 'By Lior Messinger

  At their core, AI projects can be depicted as a simple pipeline of a few building
  blocks. The diagram above explains that pretty nicely: Unstructured content, usually
  in huge amounts of data, comes in from the left, and is fed into ...'
---

Par Lior Messinger

Au cœur des projets d'IA, on peut représenter une simple pipeline de quelques blocs de construction. Le diagramme ci-dessus explique cela assez bien : du contenu non structuré, généralement en grandes quantités de données, arrive de la gauche et est alimenté dans des classificateurs d'IA. Ces modèles pré-entraînés de machine learning ou de deep learning séparent le bon grain de l'ivraie et réduisent l'entrée à quelques valeurs de sortie numériques ou textuelles.

Par exemple, des mégaoctets de pixels et de couleurs dans une image sont réduits à une étiquette : c'est une girafe. Ou un zèbre. En audio, des millions de fréquences d'ondes produisent une phrase grâce aux modèles de Speech To Text. Et dans l'IA conversationnelle, cette phrase peut être réduite davantage à quelques chaînes représentant l'intention de l'orateur et les entités dans les phrases.

Une fois que l'entrée a été _reconnue_, nous devons faire des choses et générer une sortie significative. Par exemple, une voiture reconnue trop proche devrait tourner le volant dans une voiture autonome. Une demande de réservation de vol devrait produire des requêtes de base de données RESTFul et des appels POST, et émettre une confirmation ou un refus à l'utilisateur.

Cette dernière partie, montrée dans le diagramme comme une logique basée sur des règles, est une partie inséparable de tout système d'IA, et il n'y a pas de changement en vue à cela. Cela a généralement été fait par codage, des milliers et des milliers de lignes de code — si c'est un système sérieux — ou quelques scripts si c'est un chatbot jouet.

### Arbres de comportement

Un [arbre de comportement](https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)) est un paradigme de programmation qui a émergé dans les jeux vidéo pour créer des comportements humains chez les personnages non-joueurs. Ils forment un excellent langage visuel avec lequel un architecte logiciel, un développeur junior et même un designer technique non-codeur peuvent tous créer des scripts complexes. En fait, puisque les arbres de comportement (BT) permettent des opérations logiques comme AND et OR, des boucles et des conditions, tout programme qui peut être créé par du code peut être créé avec des BT.

[Servo](https://github.com/servo-ai/servo-platform) est un framework conversationnel d'IA open-source construit sur un framework d'arbres de comportement JavaScript appelé [Behavior3](https://github.com/behavior3/). Il est conçu pour faire l'orchestration nécessaire des entrées et des sorties pour les systèmes d'IA conversationnelle. C'est ce qu'on appelle un framework "low-code" : vous n'avez besoin de coder qu'un peu, et la plupart des tâches peuvent être faites dans l'éditeur visuel.

Ce n'est pas le jouet habituel des débutants : il a été conçu pour être étendu en utilisant des fichiers sources et des classes JS réels et débogables, et se conformer à toute méthodologie de gestion de projet d'équipe. De plus, il est adapté aux équipes qui grandissent en taille, permettant l'introduction et la réutilisation de nouveaux modules à travers des sous-processus abstraits et découplés.

Je suis le principal développeur de Servo. Après 30 ans de codage, ressentant la douleur des projets à long délai et regardant les systèmes hérités s'effondrer sous leur propre poids, je voulais atteindre une flexibilité maximale avec un codage minimal. Ici, je vais expliquer la magie qui peut être faite lorsque l'on combine les arbres de comportement avec des moteurs NLU/NLP, en utilisant Servo et [Wit.ai](https://www.wit.ai/).

Tout développeur peut bénéficier de ce tutoriel, mais il est préférable que vous soyez un développeur avec de l'expérience dans la construction de chatbots ou de voicebots et que vous ayez des connaissances en travaillant avec des moteurs NLU/NLP comme LUIS, Wit.AI, Lex (le moteur Alexa), ou Dialogflow. Si ce n'est pas le cas, ce n'est pas grave, mais je vais couvrir certains sujets un peu brièvement.

Si vous voulez apprendre sur les moteurs NLU et NLP, il y a d'excellentes ressources partout sur Internet — cherchez simplement 'tutoriel Wit'. Si vous voulez apprendre à construire un assistant lourd, alors continuez simplement à lire.

### Commencer avec Servo

Je ne vais pas entrer dans les détails de l'installation de Servo ici, mais je dirai simplement que commencer avec Servo est vraiment facile. Vous pouvez en lire plus [ici](https://medium.com/datadriveninvestor/building-context-aware-stateful-bots-using-servo-a2dc3f557469). En essence, vous clonez le [dépôt Github](https://github.com/servo-ai/servo-platform), vous l'installez avec npm selon le readme, et vous l'exécutez localement. Ensuite, chaque nouveau projet démarrera avec un petit bot prêt à l'emploi pour commencer :

![Image](https://cdn-media-1.freecodecamp.org/images/6sE9DDHxTVQymZl9jk9I6SlhRyKBkgo6LQLt)
_Chaque nouveau projet a un arbre de départ_

Vous pouvez remarquer ici les hexagones verts nommés 'chit-chat', 'cancel' et autres. À la fin de cet article, vous aurez une idée claire de ce qu'ils sont et de leur fonctionnement. Mais d'abord, abordons les premiers défis.

### Construire un modèle NLU

Parlons de la construction d'un assistant bancaire, et spécifiquement, un qui travaille pour le département de transfert d'argent. Si c'était une application web, nous aurions un formulaire avec quelques champs, parmi lesquels le montant et le compte du bénéficiaire (également appelé bénéficiaire) sont les plus importants. Utilisons ceux-ci ici pour ce tutoriel. En fait, lorsque nous utilisons des moteurs NLU, nous pouvons encore penser à cela comme des formulaires, avec les champs maintenant appelés _entités_ (également _slots_, dans le jargon Alexa). Les moteurs NLU produisent également une intention, qui peut être vue comme le nom du formulaire qui guidera l'assistant vers la zone de cette fonctionnalité de l'intention de l'utilisateur.

Nous devrions entraîner le moteur NLU avec quelques phrases, telles que :

* "J'aimerais envoyer de l'argent"
* "J'aimerais envoyer 100 $"
* "Veuillez transférer 490 $ sur le compte #01-10099988"

Et pour celles-ci, nous devons dire au moteur de produire ce qui suit :

* une intention _TransferIntent_ pour de telles phrases
* Un _wit/number_ pour le montant
* Une _accountNumberEntity_ pour le compte du bénéficiaire

Faisons cela sur Wit.ai. Encore une fois, je ne vais pas entrer dans un tutoriel Wit — il y a beaucoup de guides. Servo vient avec un modèle Wit général que vous pouvez prendre depuis le Github de Servo [ici](https://github.com/servo-ai/servo-platform/tree/master/server/convocode/nlu-models/wit.ai). Ensuite, ouvrez votre propre application Wit et importez-le.

J'ai créé une entité [_free-text_](https://wit.ai/docs/recipes#which-entity-should-i-use) pour les numéros de compte (car le numéro de compte peut inclure d'autres symboles), et une entité _wit/number_ pour le montant. J'ai trouvé que les [entités composites](https://medium.com/wit-ai/introducing-composite-entities-ba2639a26e0) fonctionnent assez bien, aussi, bien qu'elles nécessitent un peu d'entraînement. Pour simplifier, pour les numéros de compte, j'ai entraîné le modèle à être un # suivi de 8 chiffres.

En général, il est toujours préférable d'expérimenter avec différents modèles d'entités. Dans notre cas, nous pourrions obtenir deux nombres dans la même phrase (numéro de compte et montant) et nous avons besoin d'un moyen de les distinguer, donc il est préférable que ce soit deux noms d'entités différents. Mais vous pouvez essayer d'autres types : l'IA est encore une science très empirique...

Nous avons ensuite entraîné le modèle avec quelques phrases et laissé Wit construire le modèle de transfert bancaire. Pour plus de commodité, je l'ai ajouté [ici](https://github.com/servo-ai/servo-platform/tree/master/server/convocode/nlu-models/wit.ai), et j'ai également configuré le bot de tutoriel bancaire pour venir avec les exemples préchargés.

![Image](https://cdn-media-1.freecodecamp.org/images/caZ8ij2dktQha7o2gUHDXBWU7HFeh1LtStdS)
_Entraînement de Wit avec des phrases de transfert bancaire_

Enfin, nous devons connecter le NLU à l'assistant. Allez dans _Paramètres_ dans Wit, et copiez le **_jeton d'accès_**. Nous devons le coller dans les propriétés de la racine de notre arbre. Nous faisons cela en ouvrant l'éditeur de Servo, en sélectionnant la racine, en ouvrant ses propriétés, et en le collant sous **_nlu_**. Comme vous pouvez le voir, Servo supporte les assistants multilingues et différents moteurs NLU :

![Image](https://cdn-media-1.freecodecamp.org/images/LwtOTiDXrX4g1TmVNh428PR7A1dcm-errJBE)

### Démarrer l'assistant bancaire

Maintenant, nous pouvons nous tourner vers Servo. Nous devrions construire un petit arbre avec une question pour chaque entité et intention.

Pour rappel, les règles de base des arbres de comportement de Servo sont les suivantes

1. La boucle principale de l'arbre exécute la racine en continu
2. Chaque nœud exécute ses enfants
3. Un nœud AskAndMap (le nœud "Age" dans le diagramme ci-dessus) pose une question à l'utilisateur et attend une réponse
4. Une fois qu'une réponse arrive, le flux est routé vers l'enfant approprié selon l'intention et les entités que le moteur NLU lui a données

Changeons d'abord la question principale, la plus haute, de **"Age ?"** en **"Que souhaitez-vous faire ?"**. Supprimons également le premier enfant (c'est-à-dire le plus à gauche) et ses nœuds, car nous n'allons plus les utiliser :

![Image](https://cdn-media-1.freecodecamp.org/images/6uwN7pG2TCHq8kU6oIm6-flNzeI91jYxNEEc)
_Tapez la question initiale de l'assistant_

Pourquoi voyons-nous les tirets rouges autour du nœud ? Survolez-le et vous verrez l'erreur :

_Le nombre de contextes doit être égal au nombre d'enfants_

Nous allons corriger cela dans une minute.

Maintenant, construisons le flux de transfert. Nous supposerons que lorsque l'utilisateur dit "J'aimerais transférer de l'argent", nous voulons descendre dans le premier enfant, le plus à gauche. Pour cela, nous sélectionnons le nœud "Comment puis-je vous aider" et allons dans ses propriétés. Là, changez le premier contexte pour avoir un **intentId** de "TransferIntent" :

![Image](https://cdn-media-1.freecodecamp.org/images/uTc0c33ugCcriSii5HG2tdvEapPuWmHfGVQx)

Cela fera en sorte que toute phrase que Wit détermine avoir une TransferIntent soit routée là.

### Cartographier une entité

Maintenant, une fois que le NLU a reconnu notre intention de transférer de l'argent, nous devrions obtenir tous les différents "champs", ou entités. Ajoutons un nœud pour le **_montant_** :

![Image](https://cdn-media-1.freecodecamp.org/images/l2FnqEyC9qTdllUVE-kAN34RzoNbewEQqf6m)

Nous avons ajouté un nœud AskAndMap, et défini son prompt à une question sur le montant. Nous avons également changé son titre — c'est toujours une bonne pratique. Enfin, n'oubliez pas de sauvegarder votre travail en utilisant le bouton Sauvegarder ou Ctrl-S.

Vous pouvez également remarquer que l'avertissement rouge a disparu du nœud _Comment puis-je vous aider_.

Enfin, ajoutons une **_entité number_** à l'un des contextes enfants du nœud Montant, et mappons la valeur dans un champ appelé **_montant_**.

```
"contexts": [
 {
   "entities": [
    {
      "contextFieldName": "amount",
      "entityName": "number",
      "expectedValue": "",
      "entityIndex": 0
    } 
   ]
 }
```

Tout cela semble très simple, et c'est le cas : si un utilisateur dit quelque chose comme "J'ai besoin d'envoyer de l'argent", on lui demandera : "Quel est le montant ?". Une fois qu'il a entré le montant, le **_number_** sera extrait par le NLU et mappé au **_context.amount_** dans Servo. Ensuite, nous pourrons l'utiliser plus tard dans le jeu. Visuellement, le flux a commencé à partir de la racine :

![Image](https://cdn-media-1.freecodecamp.org/images/HBQ2me6T-igEkyhMaqKYPPWZstYk6yuS7ecX)

Et l'assistant demanderait :

**"Comment puis-je vous aider ?"**

Si l'utilisateur répondait :

**"J'aimerais transférer de l'argent"**

le moteur NLU produirait une **_TransferIntent_** et le flux continuerait en aval vers le contexte qu'il a identifié — l'enfant le plus à gauche — et poserait la question suivante, sur le montant :

![Image](https://cdn-media-1.freecodecamp.org/images/X5dhFMpmKZMCnRvocGYljF-OKkPGOs0TFUcO)

Mais que se passe-t-il si l'utilisateur ne saisit pas de montant ?

### Construire des aides

Les nœuds AskAndMap supportent un autre type de contexte enfant, appelé **_Helper_**. Ce contexte est sélectionné lorsque l'utilisateur a répondu quelque chose qui n'a pas pu être mappé à _aucun autre contexte_. Ajoutons-en un dans notre What's the amount AskAndMap :

```
"contexts":[  
   {  
      "entities":[  
         {  
            "contextFieldName":"amount",
            "entityName":"number",
            "expectedValue":"",
            "entityIndex":0
         }
      ]
   },
   {  
      "helper":true
   }
]
```

Ajoutons maintenant un enfant le plus à droite avec un message d'aide. Quelque chose comme :

![Image](https://cdn-media-1.freecodecamp.org/images/kLl4cXh8KcX2cmKncUd8n1IC83VfUOxmcIEK)

Bien sûr, il ne peut y avoir qu'un seul contexte enfant _helper_ pour le AskAndMap.

On pourrait imaginer un exemple de flux :

Utilisateur : **"J'aimerais transférer de l'argent"**

Assistant : "**Quel est le montant ?**"

Utilisateur : "**Tu crois que je le saurais. Mais je ne suis pas sûr**"

Assistant : "**Veuillez fournir le montant à transférer**"

Cela semble simple : évidemment, l'assistant n'a pas compris le "**Tu crois que je le saurais. Mais je ne suis pas sûr**" et a continué avec le message d'aide "**Veuillez fournir le montant à transférer**".

Mais en fait, si vous exécutez le bot, vous obtiendrez une phrase surprenante après cette dernière ligne :

Utilisateur : "**Tu crois que je le saurais. Mais je ne suis pas sûr**"

Assistant : "**Veuillez fournir le montant à transférer**"

Assistant : **"Comment puis-je vous aider ?"**

Que s'est-il passé ici ? D'où vient le **"Comment puis-je vous aider ?"** ?

Voici le flux. Le nœud helper a dit sa ligne et a retourné SUCCESS à son parent, le AskAndMap. Celui-ci, à son tour, a également retourné SUCCESS, et ainsi de suite, jusqu'à ce que la racine soit atteinte. À ce moment-là, tout l'arbre a été redémarré, et nous obtenons la question initiale **"Comment puis-je vous aider ?"**.

Donc, pour éviter cela, nous devons mettre une boucle avant le AskAndMap, afin qu'il ne retourne pas tant qu'il n'a pas _vraiment_ réussi. Cela se fait avec ce qu'on appelle un _décorateur_.

### Ajouter un décorateur repeat

Les arbres de comportement implémentent des boucles en utilisant des _décorateurs_, qui sont des nœuds ayant un parent et un enfant. Représenté par un losange ⬦, nous utiliserons ici le décorateur RepeatUntilSuccess pour boucler le AskAndMap jusqu'à ce qu'il soit complété avec succès. Recevoir un message d'aide ne le compléterait pas, donc nous devons retourner un FAILURE après le message d'aide. Nous faisons cela en séquencant un nœud Failer juste après le message. En résumé, voici la décoration que nous ajoutons à la construction AskAndMap :

![Image](https://cdn-media-1.freecodecamp.org/images/X-2TTcbuxGni0WWV6eiiWV9lACdaIcxol55H)

Maintenant, il est temps d'ajouter le nœud suivant qui mappait le numéro de compte du bénéficiaire. Encore une fois, assez simple : comme précédemment, nous ajoutons un AskAndMap avec la question pour le numéro de compte et une carte de accountNumberEntity vers un membre accountNumber sur le contexte. Nous le définissons comme enfant d'un décorateur RepeatUntilSuccess, et un enfant helper qui explique ce qui est nécessaire pour cette entité.

Ensuite, nous devrions ajouter la logique métier réelle pour effectuer le transfert. Cela signifierait probablement plusieurs appels API avec les entités collectées. Nous simulerions cela avec un message : **_nous allons transférer $X sur le compte #Y_**. Pour cela, vous devez faire glisser un GeneralMessage comme premier enfant de accountNumberEntity, et définir ses propriétés comme suit :

```
"debug-log":"",
 "runningTimeoutSec":600,
 "maxRetriesNumber":5,
 "replayActionOnReturnFromContextSwitch":true,
 "view":false,
 "prompt":[ 
 "About to transfer <%=context.amount%> to account <%=context.accountNumber%>"
],
…
```

Voici à quoi ressemble l'arbre maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/04qfwmwrgiugey7IA8Xci0zOOLkIe3JOCyfU)

L'arbre est fourni avec Servo. Ses fichiers se trouvent sous _server/convocode/anonymous/drafts/bank-bot_.

### Exécution et test

Testons le bot et voyons ce qui se passe avec diverses entrées. Cliquez sur l'onglet Debugger, puis sur le bouton de lecture ▶️. Sur le côté droit, le simulateur apparaîtra :

![Image](https://cdn-media-1.freecodecamp.org/images/zPDBlRIMUzxFbWKRMLyQGI45p-sr1OQe3V3W)

Vous pouvez entrer une phrase comme :

**_J'aimerais envoyer de l'argent._**

Cela serait répondu, comme prévu, avec

"**Quel est le montant ?**"

Et vous pouvez mettre le montant, et continuer.

Mais que se passe-t-il si nous disons

**_J'aimerais envoyer 14141 $_**??

Testez-le, et vous verrez comment l'assistant saute joliment la question du montant directement au numéro de compte :

"**Quel est le numéro de compte ?**"

Maintenant, rendons sa vie encore plus difficile :

**_J'aimerais envoyer de l'argent sur le compte #87654321_**

Assez joliment, il ne demande que le montant. Supposons que vous entriez 3400 $, il sauterait alors le numéro de compte (puisqu'il le connaît déjà) pour passer à la phrase de confirmation finale :

**_Sur le point de transférer 3400 sur le compte #87654321._**

Comment sait-il faire toute cette magie ?

### Le flux de contexte

Servo est équipé d'un ensemble puissant d'algorithmes de reconnaissance de contexte qui l'aident à faire tout cela. Ce qui s'est passé ici en montre un peu. Prenons le dernier exemple. Après que l'assistant a demandé :

**"Comment puis-je vous aider ?"**

Et l'utilisateur a répondu :

**_J'aimerais envoyer de l'argent sur le compte #87654321_**

Le moteur NLU a produit une **_TransferIntent_** et le flux a continué en aval vers la question suivante, sur le montant :

![Image](https://cdn-media-1.freecodecamp.org/images/TzwMBZx2JMHoxXQDzU9-nGaX6jWb7YD27IZm)

Mais le NLU a également retourné une **accountNumberEntity !** Donc avant de descendre, cette entité est sauvegardée sur le contexte '_Comment puis-je vous aider_'. Et, chaque AskAndMap définit son propre contexte.

C'est en fait une remarque importante, donc je vais la répéter : **_chaque AskAndMap définit son propre contexte._**

À tout moment dans le flux, lorsqu'une entité est mentionnée, Servo recherche en arrière (lire : vers le haut) dans la conversation pour la trouver. Si elle ne l'a pas trouvée, elle la demandera.

Ainsi, après que le montant est entré, une fois que nous continuons vers le nœud du numéro de compte, Servo trouve que l'**_accountNumberEntity_** a déjà été mentionnée, et l'utilise.

Au fait, un processus de caractéristiques similaires se produit également lorsque nous arrivons au dernier nœud de confirmation GeneralMessage. Son prompt lit :

**Sur le point de transférer <%=context.amount%> sur le compte <%=context.accountNumber%>**

Pour résoudre cela, Servo recherche dans l'arbre de contexte les entités ou membres de contexte nécessaires.

Cela vous rappelle-t-il quelque chose ? Les personnes familières avec l'héritage prototypique JavaScript verront qu'il utilise essentiellement le même design. Dans Servo, nous avons implémenté cela puisque nous avons besoin de plus de contrôle sur les variables. Mais il est toujours intéressant de voir comment les concepts orientés objet sont réellement appliqués à la vie réelle, aux conversations naturelles.

Mais que se passe-t-il si l'utilisateur demande quelque chose de beaucoup plus sans rapport, comme :

**"Combien d'argent ai-je sur mon compte ?"**

Ou plus encore

**"Qui es-tu, au nom du ciel ??"**

À quoi le bot répond :

**"Je suis un assistant d'intelligence artificielle construit par Servo Labs."**

Whaaaaaaaaaat ?? D'où vient cela ?

### Contexte et sous-arbres

Presque toutes les conceptions structurelles que les architectes utilisent pour construire des systèmes volumineux gérables peuvent être divisées en deux catégories :

* Réutilisation
* Modularisation

Si Servo doit se tenir comme l'infrastructure de grands systèmes d'IA, il doit fournir un mécanisme permettant aux développeurs d'atteindre ces objectifs. Et c'est là que les sous-arbres entrent en jeu.

Nous avons mentionné auparavant les hexagones verts :

![Image](https://cdn-media-1.freecodecamp.org/images/vOpQmHfU9hfBvwCk5vwPg-ZNakYT6ssQp3vT)

Ceci est un sous-arbre. **Double-cliquez dessus**, et vous entrerez dans un nouvel arbre, avec ce nom. Pour créer un nouveau sous-arbre, survolez **Trees** dans le panneau de gauche et sélectionnez **New** :

![Image](https://cdn-media-1.freecodecamp.org/images/KeD7CXJx-i8DJr7Jne94zbddR-AMPJvRc4yG)

Un arbre avec un nom GUID unique apparaîtra. Changez son nom en quelque chose de significatif, et construisez-le en utilisant n'importe quel nœud du panneau de gauche. Une fois construit, vous pouvez le faire glisser, le déposer et le connecter à n'importe quel point dans n'importe quel autre arbre (y compris lui-même, d'ailleurs, mais soyez très prudent à ce sujet). Puisque les sous-arbres peuvent avoir de nombreux nœuds feuilles, vous pouvez les connecter uniquement en tant que feuilles, aussi.

Que s'est-il passé lorsque l'utilisateur a demandé à l'assistant "Qui es-tu" ?

Tout d'abord, le NLU, déjà entraîné pour de telles questions, a retourné une **_WhoAreYouIntent_**. Ensuite, la recherche de contexte a été activée. Si la conversation était quelque part au milieu d'une conversation de transfert, la recherche est allée vers le haut, essayant de trouver un contexte avec WhoAreYouIntent. Ce contexte est trouvé : il se trouve sur le 4ème contexte, dans le nœud _Comment puis-je vous aider_. Le flux a ensuite été redirigé là, ce qui signifie que cette route a été rendue active. Le flux ici a continué en aval dans le sous-arbre chit-chat, a répondu à la question, est revenu avec un SUCCESS et le routage a été retourné à son contexte précédent, celui du transfert.

Ici, nous avons appris quelque chose de très important. **_Le flux de conversation descend, mais le contexte est recherché vers le haut._** Ne l'oubliez jamais :

![Image](https://cdn-media-1.freecodecamp.org/images/ZPNg-j6-113QHHDPjO6D9Rfn2lHDmaRl2Z2U)
_**Le flux de conversation descend, mais le contexte est recherché vers le haut**_

### Connexion à un client de messagerie

Jusqu'à présent, nous avons utilisé le simulateur et le débogueur internes comme client de messagerie. Connectons notre petit assistant à un vrai Facebook messenger. Il y a un grand changement important dans les propriétés de la racine de notre arbre, et c'est de changer le nom du canal du canal par défaut "chatsim" à "facebook" :

"channels":"facebook"

Du côté Facebook, voici les principales étapes de haut niveau que l'on doit suivre :

1. Ouvrez une page Facebook sous votre compte Facebook
2. Créez une nouvelle application Facebook dans le [centre de développement Facebook](https://developers.facebook.com/)
3. Ajoutez une fonctionnalité de messagerie à votre application
4. Abonnez l'application pour écouter les événements dans la page
5. Définissez l'adresse de rappel de l'assistant comme le webhook pour poster. Servo publie toujours son bot avec le format

<URI>/entry/<channel id>/<assistant name>

Donc pour un assistant bank-bot, fonctionnant sur [www.mydomain.com,](http://www.mydomain.com%2C/) l'adresse serait :

[https://<www.mydomain.com>/entry/fb/bank-bot](https://www.mydomain.com/entry/fb/bank-bot)

Vous devez le définir dans la section d'abonnement de la page de l'application Facebook, dans le portail des développeurs. Vous devez sélectionner au moins _messages_, _messaging_postbacks_, et faire correspondre le _verify token_ avec le jeton de validation que vous avez défini dans les propriétés de la racine du bot :

![Image](https://cdn-media-1.freecodecamp.org/images/TAxJMvN8uOHgzYe6d8u0UNj2ar9NeYh4CbEn)

Au fait, [https://serveo.net](https://serveo.net/) est un excellent système de tunneling (une autre alternative est ngrok), si vous développez vos assistants, comme moi, sur localhost.

Dans les propriétés de la racine de l'assistant, définissez le même jeton de vérification et republiez-le :

```
"facebook": {
    "validationToken": "mytoken123",
    "accessToken": "<token here>"
  },
```

Le jeton d'accès doit également être défini, pris de la zone messenger de Facebook :

![Image](https://cdn-media-1.freecodecamp.org/images/YVCodrLcDGHFb7gZC5xMJjLoPvHVwZk1Xj1z)

Enfin, sélectionnez une page pour abonner votre webhook aux événements de la page :

![Image](https://cdn-media-1.freecodecamp.org/images/EWZohg-wYOzch3vfNe8Qjc0LWhUBAOsornRk)

et... une fois que vous connectez toutes ces extrémités, vous devriez avoir, enfin, un système d'IA conversationnelle complet, orchestré, de bout en bout !

### Connexion des backends

Les connexions de la vie réelle varient, mais heureusement, la plupart d'entre elles ces jours-ci sont faites en utilisant des API RESTFul. Pour celles-ci, consultez la [documentation](https://servo-ai.github.io/servo-platform/) sur **_RetrieveJSONAction_** et _PostAction_. Une fois les données récupérées, ou une réponse reçue, elles sont définies dans un [champ mémoire (context/global/volatile)](https://github.com/servo-ai/servo-platform/wiki/Building-context-aware,-stateful-chatbots-using-Servo#hierarchical-memory). Vous voudrez probablement l'interroger. Cela se fait en utilisant **_ArrayQueryAction,_** qui implémente un langage de requête de type Mongo en mémoire_. Pour les requêtes MongoDB directes, utilisez l'action **_MongoQuery_**.

### En résumé

Servo est un IDE et un framework open-source qui utilise une recherche de reconnaissance de contexte pour placer l'utilisateur sur la bonne conversation et produire les bonnes questions. Nous avons appris comment construire une conversation simple, et comment envelopper de telles conversations dans des sous-arbres pour le découplage et la réutilisation. Servo a de nombreuses autres fonctionnalités qui valent la peine d'être explorées, parmi lesquelles vous pourriez trouver

* Connecteurs pour Facebook, Alexa, Twilio et Angular
* Connecteurs pour les bases de données MongoDB, Couchbase et LokiJS
* Harnais pour les tests automatisés de conversation
* Un débogueur de conversation
* Plus d'actions, de conditions et de décorateurs
* Mécanismes de contrôle de flux
* Assignation et comparaison de champs
* Manipulation de contexte
* Validation
* Requêtes de type mongo en mémoire
* Et toute action personnalisée que vous inventez

N'hésitez pas à le vérifier et à poser des questions sur le forum Github ou à mon nom Github @lmessinger. Amusez-vous !