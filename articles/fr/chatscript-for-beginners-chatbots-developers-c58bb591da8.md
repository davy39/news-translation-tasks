---
title: Comment construire votre premier chatbot en utilisant ChatScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-02T17:49:00.000Z'
originalURL: https://freecodecamp.org/news/chatscript-for-beginners-chatbots-developers-c58bb591da8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tC6objBcZbzBQwS1wrSyYA.png
tags:
- name: Chatscript
  slug: chatscript
- name: '#chatbots'
  slug: chatbots
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment construire votre premier chatbot en utilisant ChatScript
seo_desc: 'By Giorgio Robino


  10–10–2018: article updated with new github repo url.


  Chatbots can help you get things done right inside chat tools like Facebook Messenger,
  Telegram Messenger, Slack, etc, etc. Just say the word and your chatbot will deploy
  your ...'
---

Par Giorgio Robino

> 10–10–2018 : article mis à jour avec la nouvelle [URL du dépôt github](https://github.com/ChatScript/ChatScript).

Les chatbots peuvent vous aider à accomplir des tâches directement dans des outils de chat comme Facebook Messenger, Telegram Messenger, Slack, etc. Il suffit de dire le mot et votre chatbot déploiera votre dernière version, ou vous commandera une pizza.

Et il existe un outil spécial pour construire des chatbots qui existe depuis assez longtemps. Il s'appelle ChatScript. Et comme Slack, il a commencé comme une petite partie d'un jeu vidéo.

En 2009, [Bruce Wilcox](http://brilligunderstanding.com/aboutus.html) travaillait comme développeur de jeux et chercheur en intelligence artificielle. Sa femme, [Sue Wilcox](http://brilligunderstanding.com/aboutus.html), voulait modéliser des personnages virtuels pour ses jeux de fiction interactive. Ensemble, ils ont construit ce qui est finalement devenu ChatScript.

![Image](https://cdn-media-1.freecodecamp.org/images/sfq-G4yfCxunsEuCSJGq-e5TUIytuUOhDlv2)
_Sue Wilcox (source : [http://brilligunderstanding.com/aboutus.html](http://brilligunderstanding.com/aboutus.html" rel="noopener" target="_blank" title="))_

Ce moteur de traitement du langage naturel + plateforme de script de flux de dialogue a aidé Bruce à remporter le [Prix Loebner d'IA](http://www.loebner.net/Prizef/loebner-prize.html) à trois reprises.

![Image](https://cdn-media-1.freecodecamp.org/images/QmL7v89jgnPL3uP7-q5vigSEps4Y11hh5mah)
_[Regarder une conférence de Bruce Wilcox](http://www.fundacionareces.tv/watch/50a63327c31997630a020000" rel="noopener" target="_blank" title=")_

Bruce développe et maintient toujours le projet aujourd'hui. Il est écrit en C et C++, et est open source. En fait, la version 6.8 est sortie il y a quelques semaines.

**ChatScript est l'un des rares moteurs de chatbots OPENSOURCE de traitement du langage naturel !**

Plongeons dans les bases de [ChatScript](https://github.com/ChatScript/ChatScript) et rencontrons un chatbot nommé Harry.

### Installation de ChatScript

Certaines de ces étapes peuvent être légèrement différentes selon le système d'exploitation que vous utilisez. **J'utilise Linux**. Vous n'avez pas réellement besoin de suivre ces étapes pour profiter de cet article si vous ne le souhaitez pas. Lisez simplement.

#### Étape 1 : Installer les composants du système sur votre ordinateur local

Tout d'abord, clonez le dépôt GitHub de ChatScript :

```bash
$ git clone https://github.com/ChatScript/ChatScript
```

Cela créera un répertoire ChatScript, qui contiendra ces sous-répertoires :

```
$ cd ChatScript/
$ ls -d1 */

BINARIES/
DICT/
DOCUMENTATION/
LINUX/
LIVEDATA/
LOEBNERVS2010/
LOGS/
MAC/
RAWDATA/
REGRESS/
SERVER BATCH FILES/
SRC/
SUBLIME TEXT EDITOR/
TMP/
TOPIC/
USERS/
VERIFY/
VS2010/
VS2015/
WEBINTERFACE/
```

* DOCUMENTATION contient les [fichiers de documentation wiki](https://github.com/ChatScript/ChatScript/tree/master/WIKI).

> **Au fait, j'ai personnellement contribué à mettre à jour toute la documentation originale au format markdown pour être lue en ligne et depuis la ligne de commande lors du développement.\u2764**

* RAWDATA contient un sous-répertoire pour chaque bot. Par défaut, la plateforme est livrée avec un bot nommé Harry, qui se trouve dans RAWDATA/HARRY.

Au fait, n'oubliez pas de définir LinuxChatScript64 comme exécutable :

```bash
$ chmod +x ChatScript/BINARIES/LinuxChatScript64
```

> Remarque : ici, je considère évidemment l'environnement du système d'exploitation Linux.   
> Plus d'informations sur l'installation Linux, MacOS ou Windows [ici](https://github.com/bwilcox-1234/ChatScript#getting-started).

#### Étape 2 : Pour exécuter le moteur CS en mode autonome :

```bash
$ BINARIES/LinuxChatScript64 local
```

L'exécution du moteur lancera Harry, avec qui nous pourrons ensuite discuter :

```
ChatScript EVSERVER Version 6.8  64 bit LINUX compiled Aug 16 2016 17:35:43 host=local
Params:   dict:720895 fact:800000 text:70000kb hash:50000
          buffer:22x80kb cache:1x5000kb userfacts:100
WordNet: dict=201350  fact=85710  stext=12703744 Jul26'16-21:58:46
Build0:  dict=67726  fact=130289  stext=1145656 Jul31'16-13:45:49 0
Build1:  dict=167  fact=15  stext=211304 Jul31'16-13:45:44 harry
Used 53MB: dict 269,244 (23693kb) hashdepth 18/1 fact 216,014 (8640kb) text 14183kb
           buffer (1760kb) cache (5000kb) POS: 918 (29kb)
Free 79MB: dict 451,651 hash 924 fact 583,986 text 55,816KB

Enter user name: giorgio

HARRY:  Welcome back
giorgio: > what is your name ?
HARRY:  My name is Harry.
giorgio: > who is Bruce Wilcox?
HARRY:  Bruce Wilcox (born 1951) is an artificial intelligence programmer.
giorgio: > ok, I have to go
HARRY:  Indeed.
giorgio: > :quit
Exiting ChatScript via Quit
$
```

#### Étape 3 : Coder et déboguer vos scripts de chatbot

Le mode autonome constitue un excellent environnement de développement ChatScript. Il vous permet d'exécuter des conversations interactives, puis d'interagir avec elles en utilisant des **:commandes**. Il s'agit d'un ensemble spécial d'outils de commande interactifs pour tester et déboguer vos dialogues pendant la phase de développement et de débogage.

Voici quelques exemples de commandes :

```
# recompiler le bot Harry et réinitialiser le statut des conversations avec l'utilisateur giorgio

giorgio: > :build Harry 
giorgio: > :reset

# demander des statistiques sur le sujet ~pets
giorgio: > :topicstats ~pets
    ~pets     gambits 2 responders 2 rejoinders 5 empties 0
Concepts 1860 Topics 1 rules 9 empties 0
  gambits 2  responders 2 (?: 2 s: 0  u: 0) rejoinders 5
  
# conversation ...
giorgio: > do you like snakes?
HARRY:  I love pythons except ^"Python" (the programming language)

# demander la raison pour laquelle une règle s'est déclenchée
giorgio: > :why
~pets.2.0.5.9.0  ?:  ( << you like snake >> ) I love pythons except Python ( the programming language )
 via ~control.5.9.0  u:  ( ) $$currenttopic = %topic ^if 00m( %response  0 ) 00I{ ^nofail ( TOPIC ^rejoinder ( ) ...
```

Notez que vous pouvez exécuter **:commands** pour afficher la liste complète des commandes disponibles.

Les sujets sont contenus dans des fichiers spécifiques. Par exemple, le code du sujet **_~_**_pets_ est contenu dans le fichier _pets.top_, qui ressemble à ceci :

```
topic: ~pets (dog cat pet animal bird fish snake)

?: ( << you like snake >> )
 I love pythons except ^"Python" (the programming language)
 
?: ( << you ~like ~animals >> ) 
 I love all animals.
 
t: Do you have any pets?
 #! yes
 a: ( ~yes ) Great. You like animals.
 
#! no
 a: ( ~no ) You dont like animals?
 
#! I have two parrots
 a: ( parrots ) Birds are nice.
 
#! I have a cat
 a: ( cat ) I prefer dogs
 
#! I have a canary
 a: ( [parrot bird canary finch swallow] ) Birds are nice.
 
t: I have a dog.
```

ChatScript est un moteur basé sur des règles, où les règles sont créées par des rédacteurs humains dans des scripts de programme à travers un processus appelé script de flux de dialogue. Ceux-ci utilisent un métalangage de script (simplement appelé un "script") comme leur code source.

Voici à quoi ressemble un fichier de script ChatScript :

```
#
# file: food.top
#

topic: ~food []

#! I like spinachs
s: ( I like spinach ) 
   Are you a fan of the Popeye cartoons?
   
a: ( ~yes ) 
       I used to watch him as a child. Did you lust after Olive Oyl?
     b: ( ~no ) Me neither. She was too skinny.
     b: ( ~yes ) You probably like skinny models.
     
a: ( ~no ) What cartoons do you watch?
     b: ( none ) You lead a deprived life.
     b: ( Mickey Mouse ) The Disney icon.
     
#! I often eat chicken
u: ( ![ not never rarely ] I * ~ingest * ~meat ) 
   You eat meat.
   
u: ( !~negativeWords I * ~like * ~meat ) You like meat.

?: (do you eat _ [ ham eggs bacon]) 
   I eat _0
   
?: (do you like _* or _*) 
   I dont like _0 so I guess that means I prefer _1.
   
s: ( ~like ~fruit ![~animal _bear] ) 
   Vegan, you too...
   
?: (do you eat _~meat) 
   No, I hate _0.
   
s: ( I eat _*1 >) 
  $food = _0 
  I eat oysters.
```

Vous pouvez définir les flux de dialogue de votre bot avec un script stocké sous forme de fichier texte normal. Cela est beaucoup plus simple que les méthodes utilisées par d'autres outils de chatbot, qui impliquent souvent des interfaces utilisateur basées sur un navigateur, JSON ou XML.

L'écriture de vos scripts sous forme de fichiers texte vous donne un contrôle total sur vos flux de dialogue. Vous pouvez facilement traiter et mettre à niveau votre code conversationnel avec des scripts et des outils back-end.

Par exemple, vous pourriez mettre à jour automatiquement les règles de dialogue ChatScript en fonction des enregistrements de votre base de données.

Vous pourriez même utiliser des outils d'apprentissage automatique pour exploiter les journaux de conversations. Cela pourrait révéler toutes sortes d'opportunités pour améliorer vos flux de dialogue.

Mais ce sont des sujets pour un futur article sur ChatScript. Je vous laisse jouer avec ChatScript par vous-même.

> **Veuillez contribuer à son code source open source et le marquer d'une étoile sur** [**GitHub**](https://github.com/ChatScript/ChatScript)**!**

[**ChatScript/ChatScript**](https://github.com/ChatScript/ChatScript)  
[_Contribuez au développement de ChatScript/ChatScript en créant un compte sur GitHub._github.com](https://github.com/ChatScript/ChatScript)

![Image](https://cdn-media-1.freecodecamp.org/images/sSgolG-hbTtiw1APxWTmh3CwIkfcWwaIPfBJ)
_**Veuillez appuyer ou cliquer sur «** pour aider à promouvoir cet article auprès des autres._