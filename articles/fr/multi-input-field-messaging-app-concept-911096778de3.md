---
title: Un concept d'application de messagerie à champs d'entrée multiples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-19T15:44:42.000Z'
originalURL: https://freecodecamp.org/news/multi-input-field-messaging-app-concept-911096778de3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V1FjQERZI5qae8EgEpdjjg.png
tags:
- name: Design
  slug: design
- name: mobile
  slug: mobile
- name: Product Design
  slug: product-design
- name: prototyping
  slug: prototyping
- name: UX
  slug: ux
seo_title: Un concept d'application de messagerie à champs d'entrée multiples
seo_desc: 'By Dawid Woldu

  Some time ago I shared in a Medium article the idea for context aware messenger
  app. The idea challenged the design limitation behind all messenger apps allowing
  you to write only one message at a time.

  What I always missed in these ap...'
---

Par Dawid Woldu

Il y a quelque temps, [j'ai partagé dans un article Medium](https://medium.com/@dawdus/freeing-the-bubbles-context-aware-messaging-app-8466abdcda27) l'idée d'une application de messagerie contextuelle. Cette idée remettait en question la limitation de conception derrière toutes les applications de messagerie qui ne permettent d'écrire qu'un seul message à la fois.

Ce qui m'a toujours manqué dans ces applications, c'était un moyen de sauvegarder le message que je suis en train de taper et de taper et d'envoyer autre chose à la place. Puis un moyen de revenir au message précédemment composé et de continuer. Juste pour rester sur le sujet et garder un certain ordre dans mes conversations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V1FjQERZI5qae8EgEpdjjg.png)
_De gauche à droite : Messages, Slack, Hangouts, Messenger, Whatsapp._

La manière dont je le fais aujourd'hui implique une séquence de gestes liés au champ de texte : **Appui long, Sélectionner tout, Couper, Taper, Envoyer, Appui long, Coller, continuer.**

Mon concept permettait de remplacer cette séquence par un simple appui, mais c'était à l'application de reconnaître le besoin de sauvegarder un message en fonction du contexte de la conversation. J'ai construit un prototype Quartz Composer pour montrer la fonctionnalité en action :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lsq9c3raoWv6ApwNXw8KjQ.gif)

**Mais je n'ai jamais partagé le prototype**, car il n'était pas fonctionnel, ne permettait qu'un seul champ d'entrée supplémentaire et était fait uniquement dans le but d'enregistrer cette vidéo. De plus, les prototypes Origami pour Quartz Composer ne fonctionnaient pas très bien sur l'appareil (sans parler de l'absence de clavier natif).

**La sortie de [Origami Studio](http://origami.design) m'a permis de revisiter le concept et de construire un prototype entièrement fonctionnel (en quelque sorte) à partager.**

J'ai abandonné la partie contextuelle et j'ai permis de sauvegarder autant de brouillons que nécessaire, quand vous le souhaitez.

### **Voici une vidéo de démonstration du nouveau prototype.**

### Construction dans Origami Studio.

Je pourrais écrire un article/tutoriel séparé pour chacun des défis techniques que j'ai rencontrés lors de la construction du prototype, mais je vais me limiter à lister brièvement certains d'entre eux ici. Espérons que ces courtes descriptions seront suffisantes pour susciter des idées lorsque vous rencontrerez des blocs similaires. Si ce n'est pas le cas, n'hésitez pas à [me contacter directement](https://twitter.com/dawidwoldu).

### **Champ d'entrée multilingue.**

Le composant Text Field dans Origami Studio ne permet pas les entrées multilingues. Lorsque vous double-cliquez dessus pour révéler son contenu, vous trouverez le composant Text Input réel qui le fait. Le problème est qu'il n'a pas de curseur/caret. J'ai donc bidouillé un curseur en mesurant la position de la dernière lettre dans le champ de texte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uLDTzgWOHzIkLT8OsL7Q3Q.gif)

Chaque fois que vous tapez une lettre, je vérifie si c'est un 'espace' et si c'est le cas, j'ajoute son index à un tableau d'espaces. Ensuite, je suppose que chaque fois que la hauteur de l'entrée augmente, le texte se brisera au dernier espace enregistré. Ensuite, je mesure le reste du texte pour placer un curseur dans une position correcte de la nouvelle ligne. Lorsque vous ne tapez pas l'espace, je mesure simplement la taille du texte qui correspond à la ligne.

### **Construction d'un fil de conversation.**

Le défi ici était de créer dynamiquement des bulles de chat tout en gardant le bon ordre dans le fil. Lorsque le bot commence à taper, vous pouvez voir la dernière bulle sur le fil avec 3 points sautillants. Mais si vous envoyez le message avant qu'il ne finisse de taper, votre bulle devrait atterrir sur le fil avant la bulle du bot. J'ai réussi à le faire fonctionner en gardant deux tableaux de messages. Un temporaire (bot en train de taper) et un final, et en basculant entre eux chaque fois que le bot commence à taper ou envoie le message.

J'ai créé un fichier de configuration JSON avec les messages du bot qui vous permettent de configurer ce que le bot envoie et quand, et s'il doit attendre vos message(s) pour commencer à taper.

```
{"message":"Ok, I'm dumb. What do you want from me?!", "waitforuser":2,"delay":1}
```

**waitforuser** — décrit combien de messages utilisateur le bot doit attendre avant de commencer à taper. Zéro signifie qu'il n'attendra pas du tout l'utilisateur.  
**delay** — temps en secondes avant que le bot ne commence à taper.

### **Création/suppression de champs d'entrée et gestion de leur ordre.**

Chaque fois que vous créez un champ d'entrée, j'augmente le compte sur le patch Loop, mais dès que vous n'avez plus besoin du champ, j'ai essayé de supprimer le champ de la boucle et de garder les autres champs d'entrée dans leur ordre et leur contenu. Il m'était impossible de comprendre car **les patches de boucle ne gardent pas la référence à l'instance réelle de l'élément qu'ils répliquent**. J'ai contourné cela en masquant et en réutilisant les champs inutilisés au lieu de les supprimer de la boucle.

### Téléchargements !

Vous pouvez télécharger le prototype Origami, le fichier JSON ainsi que le composant de champ de texte multilingue depuis mon [Google Drive](https://drive.google.com/drive/folders/0B9oWvt9KHdw0T2hOcUdlUFMtMVk?usp=sharing).

#### **Manuel de l'utilisateur :**

**Appui long sur le bouton Envoyer** pour sauvegarder le texte actuel et créer un nouveau champ d'entrée. (Oui ! C'est indécouvrable. Je sais.)  
Le prototype est optimisé pour une utilisation sur l'appareil. (Vous ne pouvez pas masquer le clavier)

### **Faits amusants découverts à la dernière minute :**

* Le prototype plante lors de l'utilisation d'emojis. ?  
* Le curseur du champ d'entrée multilingue peut se comporter de manière erratique lors de la frappe super rapide (je partage quand même).  
* Lorsque vous envoyez un message au moment exact où le bot commence à taper, le message vide du bot peut apparaître sur le fil.  
* Autres corrections de bugs et améliorations de performance. (Quoi ?!)