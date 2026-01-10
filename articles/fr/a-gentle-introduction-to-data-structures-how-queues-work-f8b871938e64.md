---
title: 'Une introduction en douceur aux structures de données : comment fonctionnent
  les files d''attente'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-06T04:38:49.000Z'
originalURL: https://freecodecamp.org/news/a-gentle-introduction-to-data-structures-how-queues-work-f8b871938e64
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vQPzNuz_TAOwQAkBfuaC6A.jpeg
tags:
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: queue
  slug: queue
- name: Software Engineering
  slug: software-engineering
- name: Stacks
  slug: stacks
seo_title: 'Une introduction en douceur aux structures de données : comment fonctionnent
  les files d''attente'
seo_desc: 'By Michael Olorunnisola

  Black Friday’s right around the corner, and the new Microsoft Surface Studio out
  in stores (I’m a loyal windows guy ?). So let’s talk about everyone’s favorite shopping
  past-time: waiting in line. And that age-old data structu...'
---

Par Michael Olorunnisola

Le Black Friday est juste au coin de la rue, et le nouveau Microsoft Surface Studio est en magasin (je suis un fidèle de Windows ?). Alors parlons du passe-temps préféré de tout le monde en matière de shopping : attendre en ligne. Et cette ancienne structure de données, la file d'attente.

N'hésitez pas à partager cet article avec vos amis qui vont se précipiter pour obtenir les derniers produits à la mode. Mais attention — les gens ont tendance à oublier comment fonctionnent les files d'attente le Black Friday.

### Files d'attente

Une file d'attente est une ligne (oui, la même que celle de la maternelle… pas de triche encore !)

Les ajouts (**enqueue**) se font toujours à l'arrière de la ligne

Les retraits (**dequeue**) se font toujours à l'avant de la ligne

Les files d'attente suivent le modèle **F**irst **I**n **F**irst **O**ut (FIFO).

![Image](https://cdn-media-1.freecodecamp.org/images/GMjTKmWR6yBI5GEXVEnsZ81dlQHLK5L2dKei)

#### **Cas d'utilisation exemples**

* Résoudre des requêtes simultanées de plusieurs utilisateurs, comme 3 personnes achetant le dernier billet pour un avion presque au même moment
* Mettre en file d'attente des données lors d'une [recherche en largeur](https://en.wikipedia.org/wiki/Breadth-first_search).

Abordons le premier cas d'utilisation en aidant Microsoft à créer une structure de file d'attente pour gérer toutes leurs requêtes pour le nouveau Surface Studio. Je suis trop occupé à coder et à écrire ces articles pour en acheter un moi-même, alors si vous êtes un représentant de Microsoft en train de lire ceci, n'hésitez pas à m'en envoyer un. ?

Avant de commencer, une petite note sur les tableaux JavaScript. Similaire aux [piles](https://medium.freecodecamp.com/data-structures-stacks-on-stacks-c25f2633c529#.cj82kpcg8), les tableaux JavaScript ont naturellement la fonctionnalité d'une file d'attente intégrée.

### Comment représenter les files d'attente en utilisant des tableaux JavaScript

**Enqueue** ajoute à l'arrière du tableau :

```
Array.push(someVal)
```

**Dequeue** retire et retourne le premier élément du tableau :

```
Array.shift() 
```

Si pour une raison quelconque vous vous sentez rebelle (quel codeur ne l'est pas ?), vous pourriez ajouter à l'avant du tableau, puis retirer de l'arrière.

**Enqueue** ajoute un élément à l'avant du tableau :

```
Array.unshift(someVal) 
```

**Dequeue** retire un élément de l'arrière du tableau :

```
Array.pop()
```

Cela dit, pour être complet, vous allez le reconstruire en utilisant un objet JavaScript.

La première chose que vous devez faire pour Microsoft est de créer la file d'attente où vous allez stocker les membres individuels qui cliquent sur le bouton d'achat sur leur site web.

```
class Queue{  constructor(){    this._storage = {};    this._start = -1; //répliquant l'index 0 utilisé pour les tableaux    this._end = -1; //répliquant l'index 0 utilisé pour les tableaux  }    size(){   return this._end - this._start;  }}
```

```
let appleQueue = new Queue();
```

Pour rappel, le _ signifie simplement que c'est une variable privée et ne doit pas être accédée directement.

Contrairement à la [structure de données de pile](https://medium.freecodecamp.com/data-structures-stacks-on-stacks-c25f2633c529#.cj82kpcg8), où les ajouts et les retraits se font du même côté, la nature de la file d'attente nous oblige à suivre les deux extrémités. Pour cette raison, vous créez la variable start pour toujours suivre l'avant de la file d'attente, et la variable end pour suivre la fin de la file d'attente.

Enfin, la manière la plus simple de suivre la taille d'une file d'attente (sans créer une variable de compteur inutile) est de suivre la différence entre vos points de départ et de fin.

Tout d'abord, vous devriez créer un moyen pour que les personnes qui cliquent sur "acheter" soient ajoutées à la file d'attente. Vous pouvez le faire via la méthode enqueue :

```
class Queue{  constructor(){    this._storage = {};    this._start = -1; //répliquant l'index 0 utilisé pour les tableaux    this._end = -1; //répliquant l'index 0 utilisé pour les tableaux  }    enqueue(val){    this._storage[++this._end] = val;          //++this._end signifie simplement incrémenter la variable end en premier    //C'est équivalent à    //this._end++   //->    //this._storage[this._end] = val;  }    size(){   return this._end - this._start;  }}
```

```
let microsoftQueue = new Queue();
```

```
microsoftQueue.enqueue("{user: ILoveWindows@gmail.com}")microsoftQueue.enqueue("{user: cortanaIsMyBestFriend@hotmail.com}")microsoftQueue.enqueue("{user: InternetExplorer8Fan@outlook.com}")microsoftQueue.enqueue("{user: IThrowApplesOutMyWindow@yahoo.com}")
```

Super ! Maintenant, votre stockage microsoftQueue va ressembler à quelque chose comme ceci :

```
{
```

```
  0: "{email: ILoveWindows@gmail.com}"
```

```
  1: "{email: cortanaIsMyBestFriend@hotmail.com}"
```

```
  2: "{email: InternetExplorer8Fan@outlook.com}"
```

```
  3: "{email: IThrowApplesOutMyWindow@yahoo.com}"
```

```
}
```

Une petite note sur la façon dont les utilisateurs sont représentés ci-dessus ({user: …}).

Lorsque l'utilisateur clique sur le bouton d'achat côté client, il envoie toutes ses informations pertinentes au serveur, qui traitera la requête. Lorsque des données sont souvent échangées entre des systèmes, comme le côté client et le côté serveur, elles sont le plus souvent envoyées sous forme de [JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) (**J**ava**S**cript **O**bject **N**otation), via [Ajax](http://www.w3schools.com/xml/ajax_intro.asp).

Cela ressemble aux objets JavaScript, en ce sens que ce n'est qu'une version stringifiée de paires clé-valeur. Pour ceux qui ne connaissent pas JavaScript, c'est similaire à un dictionnaire ou une table de hachage (que nous aborderons plus tard dans cette série). Pour plus d'informations à ce sujet, il y a un excellent article [ici](http://stackoverflow.com/questions/383692/what-is-json-and-why-would-i-use-it) sur StackOverflow par Andreas Grech.

Retour à votre file d'attente.

Grâce à la file d'attente que vous avez créée, Microsoft dispose désormais d'un moyen efficace de suivre toutes les personnes ayant acheté le Surface Studio, et dans l'ordre chronologique de leur achat. Pour vous assurer que ces personnes sont servies dans le bon ordre, vous devez créer une méthode dequeue précise qui suit l'ordre des acheteurs et les retire de la file d'attente une fois qu'ils ont été servis.

```
class Queue{  constructor(){    this._storage = {};    this._start = -1; //répliquant l'index 0 utilisé pour les tableaux    this._end = -1; //répliquant l'index 0 utilisé pour les tableaux  }    enqueue(val){    this._storage[++this._end] = val;   }
```

```
  dequeue(){    if(this._end > this._start){ //vérifie s'il y a des valeurs      let nextUp = this._storage[++this._start];      delete this._storage[this._start];      return nextUp;    }  }      size(){   return this._end - this._start;  }}
```

```
let microsoftQueue = new Queue();
```

```
microsoftQueue.enqueue("{user: ILoveWindows@gmail.com}")microsoftQueue.enqueue("{user: cortanaIsMyBestFriend@hotmail.com}")microsoftQueue.enqueue("{user: InternetExplorer8Fan@outlook.com}")microsoftQueue.enqueue("{user: IThrowApplesOutMyWindow@yahoo.com}")
```

```
//Fonction pour envoyer à tout le monde leur Surface Studio !let sendSurface = recepient => {   sendTo(recepient);}
```

```
//Lorsque votre serveur est prêt à gérer cette file d'attente, exécutez ceci :
```

```
while(microsoftQueue.size() > 0){  sendSurface(microsoftQueue.dequeue());}
```

Et voilà ! Tout le monde qui attendait dans la microsoftQueue reçoit maintenant son nouveau Surface Studio grâce à vous.

Pour être complet, il existe certainement quelques optimisations rapides qui peuvent rendre le code plus logique.

1. Vous pouvez réinitialiser vos valeurs de début et de fin à 0 une fois que tout le monde dans la file d'attente a été servi. Il est peu probable que votre file d'attente atteigne jamais le nombre "max" de JavaScript, mais mieux vaut prévenir que guérir.
2. Vous pouvez remplacer la vérification "end > start" par la méthode size, grâce à 0 étant évalué comme "faux" en raison de la coercition de type JavaScript. Lisez tout à ce sujet [ici](https://developer.mozilla.org/en-US/docs/Glossary/Falsy).

```
dequeue(){    if(this.size()){ //0 est une valeur fausse...coercée pour retourner false      let nextUp = this._storage[++this._start];      delete this._storage[this._start];
```

```
      if(!this.size()){ //Revérifier après incrémentation (!0 == true)        this._start = -1;        this._end = -1;       }            return nextUp;    }}
```

Et voilà, vous avez terminé l'écriture de votre file d'attente de base !

### Une [analyse de la complexité temporelle](http://bigocheatsheet.com/) sur les méthodes de file d'attente

Voici le code à nouveau :

```
class Queue{  constructor(){    this._storage = {};    this._start = -1; //répliquant l'index 0 utilisé pour les tableaux    this._end = -1; //répliquant l'index 0 utilisé pour les tableaux  }    enqueue(val){    this._storage[++this._end] = val;   }
```

```
  dequeue(){    if(this.size()){ /      let nextUp = this._storage[++this._start];      delete this._storage[this._start];
```

```
      if(!this.size()){         this._start = -1;        this._end = -1;       }            return nextUp;    }  }    size(){   return this._end - this._start;  }}
```

La même logique pour les piles s'applique ici :

**Enqueue** (ajout) est **O(1)**. Puisque vous savez toujours où se trouve la fin de la file d'attente (grâce à votre variable end), vous n'avez pas besoin d'itérer pour ajouter un élément.

**Dequeue** (retrait) est **O(1)**. Aucune itération n'est nécessaire pour le retrait puisque vous avez toujours la position de départ actuelle.

**Size** est **O(1)**. La taille est toujours connue grâce à vos variables start et end.

Une chose vraiment importante à noter ici est que les files d'attente ne sont pas censées être infinies, bien que notre classe de file d'attente et le tableau JavaScript vous permettront de continuer à ajouter des éléments jusqu'à ce que le système manque de mémoire.

Une façon d'optimiser est de créer un tableau à espace limité pour créer une file d'attente circulaire. Damian Gordon fournit une très bonne [vidéo explicative](https://www.youtube.com/watch?v=ia__kyuwGag) sur YouTube. Cela sera également utile pour lorsque nous aborderons les tables de hachage dans les futurs articles !

### Temps pour un rapide récapitulatif

Files d'attente :

1. Suivent un modèle First In First Out (FIFO)
2. Ont une propriété start et end pour suivre l'avant et l'arrière de votre file d'attente
3. Ont une méthode enqueue (ajout) et dequeue (retrait) pour gérer le contenu de votre file d'attente
4. Ont une propriété size qui vous permet de suivre la taille de votre file d'attente

### **Voici un petit défi**

En utilisant ce que vous savez maintenant sur les piles et ce que vous avez appris aujourd'hui sur les files d'attente, essayez de réimplémenter une file d'attente en utilisant uniquement des piles.

Comme indice rapide, vous n'aurez besoin que de deux piles.

Merci à Jason Holtkamp pour ce petit défi !

### **Lectures complémentaires**

[Wikipedia](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) comme toujours ?

[Cet article Wikipedia](https://en.wikipedia.org/wiki/Priority_queue) sur la file d'attente prioritaire. Nous reviendrons sur ce sujet dans les futurs articles.

Une belle [démo](https://www.khanacademy.org/computer-programming/queue-structure/6427851233820672) par Larry Serflaten sur Khan Academy, où il utilise push et pull à la place de enqueue et dequeue.

Et voici la [réponse](http://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks) pour le petit défi. Ne regardez cela qu'après avoir essayé par vous-même. Vous pouvez également consulter la réponse de [Levent Divilioglu](http://stackoverflow.com/users/3128926/levent-divilioglu) pour une représentation graphique fantastique.