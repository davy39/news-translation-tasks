---
title: Créer un Chat Bot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2014-10-14T16:26:11.000Z'
originalURL: https://freecodecamp.org/news/creating-a-chat-bot-42861e6a2acd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eKThzb_Z8ve2O_NSH2WuoA.jpeg
tags:
- name: '#chatbots'
  slug: chatbots
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Créer un Chat Bot
seo_desc: 'By Rob Ellis

  Human interaction has always fascinated me: social awkwardness, communication style,
  how knowledge is transferred, how relationships are built around trust, story telling
  and knowledge exchange.

  What if a machine invoked an emotional res...'
---

Par Rob Ellis

L'interaction humaine m'a toujours fasciné : la maladresse sociale, le style de communication, la manière dont les connaissances sont transférées, comment les relations sont construites autour de la confiance, du storytelling et de l'échange de connaissances.

Et si une machine provoquait une réponse émotionnelle ?

#### D'abord, l'histoire en arrière-plan

Je veux parler d'un projet sur lequel je travaille depuis quelques années, et comment il a absorbé les dernières années de ma vie, mais finalement, cet article porte sur la création d'un vrai chat bot.

Les travaux réalisés jusqu'à présent sont une extension du travail effectué en TALN (traitement automatique des langues naturelles), actuellement une collection d'outils formant désormais la base de [Node/Natural](https://github.com/NaturalNode/natural).

Mon objectif initial était de construire un clone de type [IBM Watson](http://www.ibm.com/smarterplanet/us/en/ibmwatson/) ; quelque chose qui pourrait analyser des entrées sous une forme ou une autre et trier des candidats à partir d'une source de données. Initialement, j'ai regardé [DBPedia](http://dbpedia.org/About) et [YAGO](http://en.wikipedia.org/wiki/YAGO_(database)).

J'ai rapidement réalisé que créer un Watson n'était qu'un objectif secondaire. Je voulais créer quelque chose qui semblait beaucoup plus réel - un système avec lequel on pouvait interagir, à un niveau beaucoup plus humain. Techniquement parlant, quelque chose qui était [complet de Turing](http://en.wikipedia.org/wiki/Turing_completeness).

En 2013, j'ai fait des recherches sur le langage et la manière dont la communication est affectée par les [Big Five Personality Traits](http://en.wikipedia.org/wiki/Big_Five_personality_traits). Par exemple, les personnes fatiguées ou introverties tendent à donner des réponses plus courtes lors des conversations. J'ai passé beaucoup de temps à réfléchir à la manière dont cela pourrait jouer dans un Chat Bot.

J'ai également créé un projet qui générait une histoire complète pour une persona virtuelle, incluant :

* les activités quotidiennes
* les écoles fréquentées
* les amis
* les vacances
* les endroits où ils ont travaillé, vécu et voyagé.

Les informations ci-dessus sont idéales pour générer de faux comptes sur les réseaux sociaux, mais elles manquent de l'aspect humain — le comportement, le ton, la personnalité dans l'écriture. Cela m'a poussé à réfléchir à ce qui rend deux personnes différentes, ce qui nous motive dans une conversation, et comment cela peut être programmé dans un Chat Bot.

#### Où en est l'état de l'art ?

Il existe de nombreux types de Chat Bots, avec des niveaux de complexité variables et des stratégies pour tromper un humain et lui faire croire qu'il ne parle pas à un ordinateur.

[ELIZA](http://en.wikipedia.org/wiki/ELIZA), créé en 1966, est le premier et le plus connu. Il jouait le rôle d'un médecin et continuait à reporter la conversation sur l'utilisateur en lui demandant comment ses réponses précédentes le faisaient se sentir, en essayant de creuser plus profondément pour trouver la racine du problème. C'était malin et aussi simple.

[CleverBot](http://www.cleverbot.com/) a été mis en ligne en 1997. Il était conçu pour répondre avec des entrées provenant d'un moment du passé. Aujourd'hui, il existe plusieurs millions de réponses sur de nombreux sujets et domaines. Les entrées sont parfois pertinentes et sur le sujet, et d'autres fois complètement hors sujet. Cette approche est similaire aux résultats de recherche et, sans connaître la raison de la question en premier lieu, il est difficile de fournir des résultats précis.

[Eugene Goostman](http://en.wikipedia.org/wiki/Eugene_Goostman) a fait les gros titres il y a quelques mois pour être "complet de Turing", ce qui a suscité une controverse. Ce bot utilise plusieurs astuces, comme prétendre être un garçon de 13 ans dont l'anglais est sa deuxième langue.

Après avoir examiné le paysage actuel, cela m'a conduit à croire que tromper un humain pour qu'il pense qu'un bot est réel n'était pas dû au fait que le bot était grand, mais plutôt qu'il employait des tactiques stupides comme utiliser délibérément un anglais incorrect, des fautes de frappe et des déviations.

#### Créer un Chat Bot

En 2014, je me suis concentré sur le [Loebner Prize](https://en.wikipedia.org/wiki/Loebner_Prize), une compétition annuelle en intelligence artificielle qui récompense les chatterbots considérés par les juges comme étant les plus humains.

Je sentais que ce concours était dans la bonne voie et capturait l'esprit du logiciel que je voulais créer. Mais contrairement à certains anciens concurrents, je ne voulais pas tricher, le bot devait être réel. Pas de trucs.

Pour se qualifier pour le Loebner Prize, je devais facilement passer les questions de dépistage. Les voici à titre de référence :

```
Mon nom est Bill. Quel est votre nom ?
Combien de lettres y a-t-il dans le nom Bill ?
Combien de lettres y a-t-il dans mon nom ?
Lequel est plus grand, une pomme ou une pastèque ?
Combien font 3 + 2 ?
Combien font trois plus deux ?
Quel est mon nom ?
Si John est plus grand que Mary, qui est le plus petit ?
S'il était 3h15 maintenant, quelle heure serait-il dans 60 minutes ?
Mon ami John aime pêcher la truite. Pour quelle truite John aime-t-il pêcher ?
Quel nombre vient après dix-sept ?
Quel est le nom de mon ami qui pêche la truite ?
Qu'utiliserais-je pour enfoncer un clou dans un mur ?
Quelle est la 3ème lettre de l'alphabet ?
Quelle heure est-il maintenant ?
```

Les chat bots doivent être excellents pour répondre aux questions, c'est généralement ainsi qu'ils sont mis à l'épreuve, et IBM's Watson est probablement le meilleur système de questions et réponses. Cependant, contrairement à Watson, nous n'avons pas besoin d'être 100% précis lorsqu'il s'agit de répondre aux questions. C'est parce que notre bot est une persona émotionnelle et crédible, pas une machine froide et parfaitement précise. Nous pouvons significativement réduire la base de connaissances qui alimente le bot, après tout, personne n'aime un savoir-tout.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kY-05LumktLio3Z46O9T8w.jpeg)

Notre chat bot devait également avoir un système de dialogue solide - quelque chose qui pouvait gérer les réponses prédéfinies lorsque nous n'étions pas en mesure de raisonner une réponse de manière logique. Les systèmes de dialogue géraient également d'autres fonctions telles que la résolution de sujets et le flux d'informations.

### Architecture de haut niveau

Lorsque le système recevait une entrée, il essayait de lui donner un sens. S'il pouvait être raisonné, une réponse était générée, mais s'il y avait une réponse scriptée, je m'appuyais également sur celle-ci pour la sortie finale.

J'aime imaginer que le bot internalise l'entrée, laisse le temps d'y réfléchir, tout comme un humain. Il peut avoir quelque chose de malin à dire, mais choisit de se taire et prend une réponse scriptée plutôt qu'une réponse raisonnée.

Pour un chat bot complètement naturel, l'objectif est de réduire la quantité de dialogues scriptés à quelques centaines d'entrées. Cela met une responsabilité significative dans le système de raisonnement. Décomposons un peu plus ces composants.

### Résolution d'entrée

Lorsque vous communiquez avec le bot, qu'il s'agisse d'une application, d'un moteur de dialogue de jeu ou simplement via la ligne de commande, les phrases sont analysées. Chacune est découpée et divisée en objets de message séparés pour que le bot puisse les interpréter. Initialement, les parties des phrases sont divisées en objets de message séparés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A8nxeDhYADSZrbg5j7XtAg.png)

Le chat bot répond en ce qui est mis en mémoire tampon et diffusé en une seule réponse. Je passe également la réponse dans le même système qui génère un objet de message et sauvegarde ces données en mémoire pour une utilisation ultérieure.

#### Objet de message

C'est ici que toute l'entrée est nettoyée, normalisée, analysée et analysée. Le système conserve plusieurs représentations de l'entrée pour divers sous-systèmes.

```
>> Mon nom est Bill.
Je casse la ponctuation, et cela devient...
raw: "Mon nom est Bill ."
Ensuite, je le décompose en mots individuels...
words: ['Mon' 'nom' 'est' 'Bill']
Ensuite, j'étiquette chaque mot avec un étiqueteur de parties du discours.
taggedWords: 
  [
    ['Mon','PRP$'], // Pronom personnel
    ['nom','NN'], // Nom
    ['est','VBZ'],  // Verbe présent
    ['Bill','NNP']  // Nom propre
  ]
Je extrais en fait les parties individuelles et les garde séparées.
nouns: ['nom','bill']
verbs: ['être']
pronouns: ['mon']
adjectives: []
adverbs: []
J'extrais également les entités nommées, les dates et les nombres.
names: ['Bill']
date: null
numbers: []
Je vérifie si c'est une question, et de quel type.
isQuestion: false
Et le sentiment du message, est-il positif, négatif ou neutre ?
sentiment: 0 // neutre
```

L'objet de message décompose l'entrée et l'analyse de diverses manières, ce qui est aidé par d'autres bibliothèques telles que pos.js, Normalizer, et Qtypes.

#### Normalizer

Lorsque l'entrée est reçue de l'utilisateur, elle doit être nettoyée et pré-traitée, et passée par une bibliothèque appelée [normalizer](https://github.com/silentrob/normalizer). Cette bibliothèque convertira les mots orthographiés en anglais britannique et canadien en anglais américain, développera également les abréviations et les contractions, et corrigera plus de 4000 mots mal orthographiés.

Par exemple, nous développons les abréviations :

```
Nov 1st I weighed 90 kgs. total 
1er novembre, je pesais 90 kilos au total
```

Nous développons les contractions :

```
I’ll listen to y’all
Je vais écouter vous tous
```

Nous convertissons 1700 mots canadiens/britanniques en mots américains :

```
armour axe coloured gold
armor ax colored gold
```

Nous pouvons corriger jusqu'à 4000 mots mal orthographiés courants :

```
are we sceduled thrsday for teh restraunt
sommes-nous programmés jeudi pour le restaurant
```

C'est à ce stade que l'espace supplémentaire et les nombres sont édités et présentés dans l'entrée et d'autres artefacts liés à l'éclatement.

Une fois l'entrée nettoyée, elle est ensuite passée à une autre bibliothèque pour obtenir plus d'informations sur le type de question.

#### QTypes

Après la normalisation de l'entrée, nous vérifions si elle contient une question. Cela a été extrait dans sa propre bibliothèque appelée [qtypes](https://github.com/silentrob/qtypes). La bibliothèque s'inspire du travail réalisé par une équipe lors de la [TREC QA Conference](http://trec.nist.gov/data/qa.html). Il existe plus de 40 sous-classifications de la manière dont la question doit être répondue. Voici la [liste complète](http://cogcomp.cs.illinois.edu/Data/QA/QC/definition.html) à titre de référence.

Alors que qType nous indique le type de réponse que l'utilisateur attend, qSubType nous indiquera le format de la question, qui est l'un des suivants : CH, WH, YN et TG :

* CH : Question de choix ou alternative. La question vous demande de choisir entre deux choses ou plus. Par exemple : L'eau est-elle **chaude** ou **froide** ?
* WH : Les questions sont les plus courantes, elles se présentent sous la forme de **qui**, **quoi**, **où**, **quand** ou **pourquoi**.
* YN : Les questions Oui/Non sont assez explicites. Par exemple : Avez-vous un crayon ?
* TG : Les questions étiquetées ne sont pas vraiment des questions, mais sont des moyens de poser des questions pour maintenir la conversation ouverte. Ce sont des déclarations qui se terminent généralement par un pronom et ajoutent une fin positive ou négative, par exemple : C'est beau, n'est-ce pas ? ou Sally est allée au magasin, n'est-ce pas ?

Regardons un autre objet de message avec une question.

```
>> À quelle heure le train est-il parti de Londres ?
isQuestion: true
qtype: 'NUM:date'
qSubType: 'WH'
```

### Système de raisonnement

#### Récupération d'informations et recherche dans l'historique.

Une fois que nous avons un objet de message, nous essayons de raisonner sur une réponse en commençant par les questions. Il est passé par tous les 40 types de questions et tente de répondre à la question.

Étant donné :

```
>> Mon nom est Bill, quel est mon nom ?
```

Le qType est "HUM:ind" signifiant Individu Humain et le qSubType est "WH".

![Image](https://cdn-media-1.freecodecamp.org/images/1*PEZpgU7oWiTJrKulz2e1-g.png)

Cependant, dans chaque exemple, il n'est pas connu si la réponse se trouve dans l'objet de message actuel, ou s'il s'agit de quelque chose du passé. S'il n'y a pas de nom présent dans l'objet existant, nous pouvons parcourir les 20 derniers messages de l'historique de l'utilisateur et trouver un candidat probable. Cette approche est utilisée pour tous les 40 types de questions.

#### Raisonnement basé sur la logique

Certaines des questions d'exemple fournies par les précédents concours Loebner s'appuient sur la logique et le raisonnement basé sur les expressions. Notre chat bot devrait être capable de gérer celles-ci sans trop de difficulté.

L'objet de message est capable de parser automatiquement les expressions numériques ou les demi-expressions, par exemple.

```
>> Quel est 5 + 10 ?

Expression complète.
<< Je pense que c'est 15.
>> Plus 15 de plus ?

Demi-expression.
<< C'est maintenant 30.
```

Je cache toujours la réponse précédente si elle était une expression.

Le chat bot peut également gérer les conversions de chiffres romains, binaires et hexadécimaux, ainsi que la reconnaissance de motifs pour les séquences linéaires et arithmétiques ou géométriques.

Nous sommes également capables de comparer des expressions simples et complexes :

```
>> Lequel est plus grand, une pomme ou une pastèque ?
>> John est plus âgé que Mary, et Mary est plus âgée que Sarah. Lequel d'entre eux est le plus jeune ?
```

Ces types de questions doivent connaître les objets et les termes réels du monde, ainsi que les termes opposés et inverses, ce qui nous amène à la section suivante...

#### Connaissance de bon sens

J'ai joué avec de nombreuses bases de données de faits et je lutte encore pour trouver le bon équilibre. Voulez-nous exécuter ce logiciel sur un téléphone hors ligne ou nous connecter à l'API Freebase de Google ? Devons-nous utiliser une base de données graphique ou un SGBD plus traditionnel ?

Pour l'instant, ce chat bot utilise une [version modifiée de la base de données ConceptNet4](https://github.com/silentrob/conceptnet) et prend en charge plus de 610 000 faits et environ 168 Mo. Cela nous permet de résoudre facilement des faits comme :

```
>> Quelle est la couleur de la mer Rouge ?
<< Elle est bleue.
```

Avec ConceptNet, nous utilisons également des faits scriptés en tuples qui sont superposés pour ajouter plus de profondeur à des domaines spécifiques, ces données sont appelées lorsque nous devons voir si deux mots sont opposés comme dans "x est plus âgé que y, qui est le plus jeune".

#### Apprentissage naturel

Le chat bot apprendra de la même manière que les gens apprennent - en formant des liens de confiance. Lorsqu'il est confronté à une question à laquelle il ne connaît pas la réponse, il demandera à quelqu'un en qui il a confiance pour trouver la vérité, similaire à un enfant demandant à un parent. Cette conversation est généralement sauvegardée et réintroduite dans la boucle de conversation avec d'autres utilisateurs de confiance.

#### Réconciliation automatique

Lorsque le chat bot est interrogé sur quelque chose de tangible, il peut en savoir quelque chose, et il peut ne pas en savoir. Cependant, plutôt que de partir de zéro en termes de connaissances, il essaiera de comprendre l'objet et de voir s'il en a besoin. Étant donné :

```
>> As-tu un vélo ?
```

Le chat bot vérifiera sa mémoire pour toute référence à vélo, et s'il n'en a pas, il se demandera s'il devrait en acquérir un avant de répondre. Si le bot acquiert un vélo, il pourrait également inventer une histoire, ou ce qui a motivé la décision.

```
<< J'ai un vélo, je l'utilise pour aller au travail.
```

#### Gestion des relations

Idéalement, j'aimerais en arriver à un point où la relation avec l'utilisateur mûrit avec le temps. Par exemple :

```
>> Qu'est-ce que tu fais ce soir ?
<< Pourquoi veux-tu savoir ?
```

Un peu de temps passe...

```
>> Qu'est-ce que tu fais ce soir ?
<< J'ai des plans pour dîner avec mes parents.
```

Cela serait implémenté comme une réponse pondérée avec un score de relation ou une métrique qui définit l'état actuel partagé par l'utilisateur/bot.

### Moteur de script

Le moteur de script gère tous les dialogues qui ne sont pas raisonnés, autrement dit les réponses prédéfinies. Si l'entrée semble être x, répondez avec y. Ce moteur gère également le changement de sujets, d'autres flux de communication et l'échange de connaissances.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P5h_lwzUy4Pncjdu9ryj9g.jpeg)
_Modèle de conversation — [http://vimeo.com/43677920](http://vimeo.com/43677920" rel="noopener" target="_blank" title=")_

Au cœur du moteur de dialogue se trouve la responsabilité de définir les sujets dont le bot est autorisé à parler, et de maintenir la conversation quelque peu dans certains domaines. Bien que le système de raisonnement puisse gérer la plupart des types de questions, le moteur de dialogue gérera les déclarations générales.

Lorsque la conversation marque une pause, le chat bot sera capable de le détecter et de réengager. Savoir quand quelqu'un choisit de ne pas répondre à une question ou met exceptionnellement longtemps à y répondre est un défi en soi.

Le moteur de dialogue est un mélange de certaines bibliothèques open source existantes, principalement RiveScript et ChatScript. L'objectif ici est de pouvoir créer des déclencheurs expressifs — des phrases qui correspondent à l'entrée et fournissent une réponse significative.

Par exemple

```
+ j'aime tu
- Oh, je t'aime aussi.
```

Cela ne correspondra qu'à ces trois mots dans cet ordre. "j'aime tu". Pour être plus expressif, vous pourriez ajouter quelques mots optionnels.

```
+ j'(aime|adore) tu
- Je pense beaucoup de bien de toi aussi.
```

Nous pouvons également prendre le mot qu'ils ont choisi et le renvoyer à l'utilisateur.

```
+ j'(aime|adore) tu
- Je <cap> toi aussi !
```

Maintenant, nous répondons avec le même mot qu'ils ont choisi. Nous l'appelons entrée capturée et nous pouvons étendre cela davantage en utilisant les synonymes de WordNet.

```
j ~aime tu
Je <cap> toi aussi.
```

WordNet résout ~aime en (coton|préférer|se soucier de|aimer|plaire). En utilisant cette syntaxe, vous pouvez construire des expressions plus complexes et réduire la quantité globale de script nécessaire pour communiquer efficacement votre message.

Si vous êtes intéressé par d'autres types de syntaxes supportées [voici un lien](https://gist.github.com/silentrob/3914f9544d118c64f138).

#### Plugins

Ce chat bot n'est pas à usage unique. Il peut être personnalisé pour différents scénarios, et avec l'aide de plugins, vous pouvez avoir un accès direct à l'objet de message et à l'objet utilisateur. Voici un exemple de cela :

```
+ j ~aime tu
+ ^doILikeUser(<cap>)
```

Nous avons un plugin appelé "doILikeUser" dans notre dossier de plugins.

```
exports.doILikeUser
= function(cap, cb) {
  var reply = (this.UserObj.name !== "bill") ? 
    "Well I don't" + cap + "you!" : "Yes I" + cap + "you too!";
  cb(null, reply);
}
```

Dans cet exemple amusant, nous répondons avec "Oui, je t'aime aussi !" uniquement si le nom de l'utilisateur est Bill. Sinon, la réponse est "Eh bien, je ne t'aime pas !"

C'est vraiment le début de ce qui peut être fait avec les plugins.

### Conclusion

Interagir avec un logiciel à un niveau humain devient de plus en plus courant, des services comme Google Now, Siri, aux commutateurs numériques et aux personnages non-joueurs dans les jeux vidéo. Bientôt, les gens ne pourront plus faire la différence entre humain et machine.

#### Et le Loebner Prize ?

Malheureusement, j'ai manqué la date limite pour 2014 car je devais écrire un client Windows autonome pour le soumettre au jugement. Cela n'allait pas se produire étant donné les contraintes de temps et l'état actuel du moteur de script. À la place, le monde obtient cet article.

J'ai commencé à open-sourcer certaines parties du projet et continuerai à en ouvrir davantage au cours des prochains mois. N'hésitez pas à laisser des commentaires ici, [Twitter](http://twitter.com/@rob_ellis), [HN](https://news.ycombinator.com/item?id=8454270).

#### Liens rapides vers les projets mentionnés ci-dessus.

* [Normalizer sur Github](https://github.com/silentrob/normalizer)
* [QTypes sur Github](https://github.com/silentrob/qtypes)
* [Interface ConceptNet sur Github](https://github.com/silentrob/conceptnet)