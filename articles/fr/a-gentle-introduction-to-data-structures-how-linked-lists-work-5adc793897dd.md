---
title: 'Une Introduction en Douceur aux Structures de Données : Comment Fonctionnent
  les Listes Chaînées'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-15T20:13:35.000Z'
originalURL: https://freecodecamp.org/news/a-gentle-introduction-to-data-structures-how-linked-lists-work-5adc793897dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a75WWf1cQX8wcKN0nEYMJQ.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Une Introduction en Douceur aux Structures de Données : Comment Fonctionnent
  les Listes Chaînées'
seo_desc: 'By Michael Olorunnisola

  Have you ever built a Rube Goldberg Machine? If not, maybe you’ve built an elaborate
  line of dominoes?

  Okay, maybe you weren’t as nerdy of a kid as I was. So be it. For those of you who
  have had the pleasure to do any of the a...'
---

Par Michael Olorunnisola

Avez-vous déjà construit une machine de Rube Goldberg ? Si ce n'est pas le cas, peut-être avez-vous construit une ligne élaborée de dominos ?

D'accord, peut-être que vous n'étiez pas un enfant aussi geek que je l'étais. Soit. Pour ceux d'entre vous qui ont eu le plaisir de faire l'une des activités ci-dessus, vous avez déjà saisi l'essence de la structure de données d'aujourd'hui : les listes chaînées !

![Image](https://cdn-media-1.freecodecamp.org/images/1*RDUZJbkbiibhVmnl5OOOMw.gif)

### **Comment fonctionnent les listes chaînées**

La forme la plus simple des listes chaînées — une _liste simplement chaînée_ — est une série de nœuds où chaque nœud individuel contient à la fois une valeur et un pointeur vers le nœud suivant dans la liste.

Les ajouts (**Add**) font croître la liste en ajoutant des éléments à la fin de la liste.

Les suppressions (**Remove**) supprimeront toujours un élément à une position donnée dans la liste.

La recherche (**Contains**) recherchera la liste pour une valeur.

**Cas d'utilisation exemples :**

* Stocker des valeurs dans une table de hachage pour éviter les collisions (plus d'informations à ce sujet dans quelques articles)
* Reconstruire l'Amazing Race !

![Image](https://cdn-media-1.freecodecamp.org/images/0*nYchAJ8wQnhjtMZZ.png)

Gardons cet article léger en travaillant sur un outil que le réseau CBS peut utiliser pour planifier leur prochaine émission de télévision Amazing Race.

Au fur et à mesure que vous avancez, je veux que vous continuiez à vous demander : « En quoi les listes chaînées sont-elles différentes des tableaux ? En quoi sont-elles similaires ? »

Commençons.

Tout d'abord, vous devez créer la représentation de notre liste chaînée :

```
class LinkedList{  constructor(){    this._head = null;    this._tail = null;    this._length = 0;  }
```

```
  size(){    return this._length;  }}
```

Pour garder une trace du point de départ et du point final de la course, vous créez les propriétés head et tail.

Ensuite, pour vous assurer de ne pas rendre la course trop longue ou trop courte pour la saison, vous créez une propriété length et une méthode size. De cette façon, vous pouvez toujours garder une trace de la longueur exacte de la course.

Maintenant que vous avez un moyen de stocker la liste de la course, vous devriez créer un moyen d'ajouter à cette liste. La question est, qu'ajoutez-vous spécifiquement ?

Rappelez-vous, une liste chaînée est une série de nœuds où chaque nœud a une valeur et un pointeur vers le nœud suivant dans la liste. Sachant cela, vous réalisez qu'un nœud est simplement un objet avec une valeur et une propriété next.

Puisque vous allez créer un nouveau nœud chaque fois que vous ajoutez à la liste, vous décidez de créer un constructeur qui facilite la création d'un nouveau nœud pour chaque valeur ajoutée à votre liste.

```
class Node{  constructor(value){    this.value = value;    this.next = null;  }}
```

Avoir ce constructeur disponible vous permet de créer votre méthode add.

```
class Node {  constructor(value) {    this.value = value;    this.next = null;  }}
```

```
class LinkedList {   constructor() {    this._head = null;    this._tail = null;    this._length = 0;  }    add(value) {    let node = new Node(value);         // nous créons notre nœud    if(!this._head && !this._tail){     // Si c'est le premier nœud      this._head = node;                // Le 1er nœud est la tête et la queue      this._tail = node;    }else{    this._tail.next = node;             // ajoute le nœud à l'arrière    this._tail = this._tail.next;       // réinitialise la queue au dernier nœud    }    this._length++;  }    size() {    return this._length;  }}
```

```
const AmazingRace = new LinkedList();AmazingRace.add("Colombo, Sri Lanka");AmazingRace.add("Lagos, Nigeria");AmazingRace.add("Surat, India");AmazingRace.add("Suzhou, China");
```

Maintenant que vous avez ajouté cette méthode, vous pourrez ajouter une série de lieux à votre liste Amazing Race. Voici à quoi cela ressemblera. Notez que j'ai ajouté un peu d'espace blanc supplémentaire pour faciliter la compréhension.

```
{ _head:    { value: 'Colombo, Sri Lanka',     next: { value: 'Lagos, Nigeria',              next: { value: 'Surat, India',                     next: { value: 'Suzhou, China',                             next: null                            }                   }           }    },  _tail: { value: 'Suzhou, China', next: null },  _length: 4 }
```

D'accord, maintenant que vous avez créé cette liste et un moyen d'ajouter, vous réalisez que vous voulez de l'aide pour ajouter des lieux à cette liste parce que vous avez la Decidophobia (oui, c'est une [chose](https://en.wikipedia.org/wiki/Decidophobia)).

Vous décidez de la partager avec votre collègue, Kent, en lui demandant d'ajouter quelques endroits supplémentaires. Le seul problème est que lorsque vous la lui donnez, vous ne lui dites pas quels endroits vous avez déjà ajoutés. Malheureusement, vous avez également oublié après avoir souffert d'amnésie causée par l'anxiété de décision.

Bien sûr, il pourrait simplement exécuter _console.log(AmazingRace)_ et lire ce que la console affiche. Mais Kent est un programmeur paresseux et a besoin d'un moyen de vérifier si quelque chose existe pour éviter les doublons. Avec cela en tête, vous construisez une méthode **contains** pour vérifier les valeurs existantes.

```
class Node {  constructor(value) {    this.value = value;    this.next = null;  }}class LinkedList {   constructor() {    this._head = null;    this._tail = null;    this._length = 0;  }    add(value) {    let node = new Node(value);             if(!this._head && !this._tail){           this._head = node;                      this._tail = this._head;    }else{    this._tail.next = node;                 this._tail = this._tail.next;           }    this._length++;  }    contains(value){    let node = this._head;    while(node){      if(node.value === value){        return true;      }      node = node.next;    }    return false;  }    size() {    return this._length;  }  }
```

```
const AmazingRace = new LinkedList();AmazingRace.add("Colombo, Sri Lanka");AmazingRace.add("Lagos, Nigeria");AmazingRace.add("Surat, India");AmazingRace.add("Suzhou, China");
```

```
// Vérification de Kent
```

```
AmazingRace.contains('Suzhou, China'); // vraiAmazingRace.contains('Hanoi, Vietnam'); // fauxAmazingRace.add('Hanoi, Vietnam');AmazingRace.contains('Seattle, Washington'); // fauxAmazingRace.add('Seattle, Washington');AmazingRace.contains('North Pole'); // fauxAmazingRace.add('North Pole');
```

Super, maintenant Kent a un moyen de vérifier les valeurs avant de les ajouter, pour éviter les doublons.

À part ça, vous vous demandez peut-être pourquoi vous n'avez pas simplement utilisé la méthode contains dans la méthode add pour éviter les ajouts en double ? Lorsque vous implémentez une liste chaînée — ou toute structure de données, d'ailleurs — vous pourriez théoriquement ajouter toute fonctionnalité supplémentaire que vous souhaitez.

Vous pouvez même aller modifier les méthodes natives sur les structures existantes. Essayez ce qui suit dans un REPL :

```
Array.prototype.push = () => { return 'cat';}
```

```
let arr = [];arr.push('eggs'); // retourne 'cat';
```

La raison pour laquelle nous ne faisons aucune de ces choses est à cause des [normes convenues](http://www.ecma-international.org/ecma-262/7.0/index.html#sec-array.prototype.push). Essentiellement, les développeurs ont une attente de la manière dont certaines méthodes devraient fonctionner.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vEGGi4mAQz9c9H6dkoOmLw.gif)

Puisque notre classe de liste chaînée n'est pas native à JavaScript, nous avons plus de liberté dans son implémentation, mais il y a encore des attentes de base sur la manière dont des structures de données comme celles-ci devraient fonctionner. Les listes chaînées ne stockent pas intrinsèquement des valeurs uniques. Mais elles ont des méthodes comme **contains** qui nous permettent de pré-vérifier et de maintenir l'unicité dans notre liste.

Kent revient vers vous avec sa liste de destinations, mais certaines d'entre elles sont discutables. Par exemple, le Pôle Nord pourrait ne pas être la meilleure destination pour l'Amazing Race.

Vous décidez donc de créer une méthode pour pouvoir supprimer un nœud. Il est important de se rappeler que une fois que vous supprimez le nœud, vous déliez la liste, et devrez relier ce qui venait avant et après le nœud supprimé.

```
class Node {  constructor(value) {    this.value = value;    this.next = null;  }}class LinkedList {   constructor() {    this._head = null;    this._tail = null;    this._length = 0;  }    add(value) {    let node = new Node(value);             if(!this._head && !this._tail){           this._head = node;                      this._tail = this._head;    }else{    this._tail.next = node;                 this._tail = this._tail.next;           }    this._length++;  }    remove(value) {    if(this.contains(value)){          // voir si notre valeur existe      let current = this._head;           // commencer au début de la liste      let previous = this._head;        while(current){                   // vérifier chaque nœud          if(current.value === value){            if(this._head === current){   // si c'est la tête              this._head = this._head.next;  // réinitialiser la tête              this._length--;              // mettre à jour la longueur              return;                      // sortir de la boucle            }            if(this._tail === current){   // si c'est le nœud de queue              this._tail = previous;       // s'assurer de le réinitialiser            }            previous.next = current.next;  // délier (voir l'image ci-dessous)            this._length--;            // mettre à jour la longueur            return;                    // sortir de           }          previous = current;          // regarder le nœud suivant          current = current.next;      // ^^        }     }    }      contains(value){    let node = this._head;    while(node){      if(node.value === value){        return true;      }      node = node.next;    }    return false;  }    size() {    return this._length;  }  }
```

```
const AmazingRace = new LinkedList();AmazingRace.add("Colombo, Sri Lanka");AmazingRace.add("Lagos, Nigeria");AmazingRace.add("Surat, India");AmazingRace.add("Suzhou, China");AmazingRace.add('Hanoi, Vietnam');AmazingRace.add('Seattle, Washington');AmazingRace.add('North Pole');
```

```
// Vérification de Kent
```

```
AmazingRace.remove('North Pole');
```

Il y a beaucoup de code dans cette fonction **remove** ci-dessus. Essentiellement, cela se résume aux points suivants :

1. si la valeur existe dans la liste...
2. itérer sur la liste chaînée, en gardant une trace du nœud précédent et actuel
3. puis, s'il y a une correspondance →

4A. si c'est la tête

* réinitialiser la tête au nœud suivant dans la liste
* mettre à jour la longueur
* sortir de la boucle

4B. si c'est la queue

* réinitialiser la queue au nœud précédent dans la liste
* délier le nœud en réinitialisant les pointeurs comme vu ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/0*pMf-_vYuiuI1u3j5.png)
_[Wikipedia](https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjauKOv46rQAhULfiYKHdgFDWYQjhwIBQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FLinked_list&psig=AFQjCNHXY1FhqqxQeG8hKywNnnpfCnVNpw&ust=1479299805807482" rel="noopener" target="_blank" title=")_

4C. Si ce n'est pas une correspondance → _continuer à itérer_

* faire du nœud suivant le nœud actuel
* faire du nœud actuel le nœud précédent

Une dernière chose à noter : vous avez peut-être réalisé que vous n'avez pas réellement supprimé le nœud. Vous avez simplement supprimé les références à celui-ci. Eh bien, ce n'est pas grave car une fois toutes les références à un objet supprimées, le garbage collector nous aide à le supprimer de la mémoire. Vous pouvez lire sur le garbage collection [ici](http://docstore.mik.ua/orelly/webprog/jscript/ch11_03.htm).

Avec la méthode remove maintenant implémentée, vous pouvez exécuter ce petit morceau de code ci-dessous pour vous assurer que les concurrents ne gèlent pas à mort, ou ne dérangent pas accidentellement le Père Noël alors qu'il prépare les festivités de cette année.

```
AmazingRace.remove('North Pole');
```

Vous l'avez fait ! Vous avez créé une implémentation simple d'une liste chaînée. Et vous pouvez faire croître la liste en ajoutant des éléments, et la réduire en supprimant des éléments — tout cela basé sur la valeur de l'élément.

Voyez si vous pouvez ajouter des valeurs à la liste chaînée pour vous permettre d'insérer des valeurs au début, à la fin, ou à n'importe quel point intermédiaire.

Vous avez tout ce dont vous avez besoin pour implémenter ces méthodes. Les noms et arguments de ces méthodes devraient ressembler un peu à ceci :

```
addHead(value) {
```

```
}
```

```
insertAfter(target, value){
```

```
}
```

N'hésitez pas à partager vos implémentations dans les commentaires ci-dessous ?

### **Une analyse de la complexité temporelle des méthodes de la file d'attente**

![Image](https://cdn-media-1.freecodecamp.org/images/1*MIdvIvbjZVo_Tv4tKYsxUw.gif)

Voici le code à nouveau :

```
class LinkedList {   constructor() {    this._head = null;    this._tail = null;    this._length = 0;  }    add(value) {    let node = new Node(value);             if(!this._head && !this._tail){           this._head = node;                      this._tail = this._head;    }else{    this._tail.next = node;                 this._tail = this._tail.next;           }    this._length++;  }    remove(value) {    if(this.contains(value)){                let current = this._head;              let previous = this._head;        while(current){                   if(current.value === value){            if(this._head === current){               this._head = this._head.next;              this._length--;                            return;                                  }            if(this._tail === current){               this._tail = previous;                }            previous.next = current.next;            this._length--;                        return;                              }          previous = current;                    current = current.next;              }     }    }     contains(value){    let node = this._head;    while(node){      if(node.value === value){        return true;      }      node = node.next;    }    return false;  }    size() {    return this._length;  }
```

```
// À Implémenter
```

```
addHead(value) {
```

```
}
```

```
insertAfter(target, value){
```

```
}
```

**Add** est **O(1)** : Puisque vous connaissez toujours le dernier élément de la liste grâce à la propriété tail, vous n'avez pas à itérer sur la liste.

**Remove** est **O(n)** : Dans le pire des cas, vous devrez itérer sur toute la liste pour trouver la valeur à supprimer. La bonne partie est que la suppression réelle du nœud est O(1) car vous réinitialisez simplement les pointeurs.

**Contains** est **O(n)** : Vous devez itérer sur toute la liste pour vérifier si la valeur existe dans votre liste.

**addHead** est **O(1)** : Similaire à notre méthode add ci-dessus, nous connaissons toujours la position de la tête, donc aucune itération nécessaire.

**insertAfter** est **O(n)** : Similaire à notre méthode Remove ci-dessus, vous devrez itérer sur toute la liste pour trouver le nœud cible après lequel votre valeur doit être insérée. De même, l'insertion réelle est O(1) car vous réinitialisez simplement les pointeurs.

### Liste Chaînée vs Tableau ?

Pourquoi utiliser une liste chaînée au lieu d'un tableau ? Les tableaux permettent techniquement de faire tout ce que les listes chaînées font, comme les ajouts, les insertions et les suppressions. De plus, toutes ces méthodes sont déjà disponibles en JavaScript.

Eh bien, la plus grande différence vient des insertions et des suppressions. Puisque les tableaux sont indexés, lorsque vous effectuez une insertion ou une suppression au milieu du tableau, vous devez réinitialiser la position de toutes les valeurs suivantes à leurs nouveaux indices.

Imaginez insérer au début ou au milieu d'un tableau de 100 000 valeurs ! Les insertions et suppressions comme celle-ci sont extrêmement coûteuses. Pour cette raison, les listes chaînées sont souvent préférées pour les grands ensembles de données qui sont souvent déplacés.

D'autre part, les tableaux sont excellents lorsqu'il s'agit de trouver des éléments (accès aléatoire) puisqu'ils sont indexés. Si vous connaissez la position d'un élément, vous pouvez y accéder en temps O(1) via _array[position]_.

Les listes chaînées vous obligent toujours à itérer sur les listes chaînées de manière séquentielle. Étant donné cela, les tableaux sont généralement préférés pour les ensembles de données plus petits, ou les ensembles de données qui ne sont pas souvent déplacés.

### Temps pour un rapide récapitulatif

Listes Chaînées :

1. ont une propriété tail et head pour suivre les extrémités de la liste
2. ont une méthode add, addHead, insertAfter et remove pour gérer le contenu de votre liste
3. ont une propriété length pour suivre la longueur de votre liste chaînée

### Lectures Complémentaires

Il existe également les structures de données de liste doublement chaînée et de liste circulaire chaînée. Vous pouvez lire à leur sujet [sur Wikipedia](https://en.wikipedia.org/wiki/Linked_list#Linked_lists_vs._dynamic_arrays).

De plus, voici un aperçu solide et rapide par Vivek Kumar [ici](http://www.codingeek.com/data-structure/linked-list-types-explanation/).

Enfin, Ian Elliot a écrit un [guide](http://www.i-programmer.info/programming/javascript/5328-javascript-data-structures-the-linked-list.html?start=1) qui vous aide à implémenter toutes les méthodes. Mais voyez si vous pouvez implémenter **addHead()** et **insertAfter()** pour votre liste chaînée avant de jeter un coup d'œil à cela ?