---
title: Tout ce que vous devez savoir sur le passage par référence vs par valeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-18T10:59:23.000Z'
originalURL: https://freecodecamp.org/news/understanding-by-reference-vs-by-value-d49139beb1c4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KWzeGf9HU8eLhbDiikaobg.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Tout ce que vous devez savoir sur le passage par référence vs par valeur
seo_desc: 'By Szilard Magyar

  When it comes to software engineering there are quite a few misunderstood concepts
  and misused terms. By reference vs by value is definitely one of them.

  I remember back in the day when I read up on the topic and every source I went...'
---

Par Szilard Magyar

En matière de génie logiciel, il existe plusieurs concepts mal compris et des termes mal utilisés. Le passage par référence vs par valeur en fait définitivement partie.

Je me souviens qu'à l'époque, lorsque j'ai lu sur le sujet, chaque source que j'ai consultée semblait contredire la précédente. Il m'a fallu un certain temps pour bien comprendre le sujet. Je n'avais pas le choix, car c'est un sujet fondamental si vous êtes ingénieur logiciel.

Je suis tombé sur un bug tenace il y a quelques semaines et j'ai décidé d'écrire un article pour que d'autres personnes puissent plus facilement comprendre tout cela.

Je code en Ruby au quotidien. J'utilise également JavaScript assez souvent, donc j'ai choisi ces deux langages pour cette présentation.

Pour comprendre tous les concepts, nous utiliserons également des exemples en Go et Perl.

Pour saisir tout le sujet, vous devez comprendre trois choses différentes :

* Comment les structures de données sous-jacentes sont implémentées dans le langage (objets, types primitifs, mutabilité, etc.).
* Comment fonctionnent l'assignation/copie/réassignation/comparaison de variables.
* Comment les variables sont passées aux fonctions.

### Types de données sous-jacents

En Ruby, il n'y a pas de types primitifs et tout est un objet, y compris les entiers et les booléens.

Et oui, il existe une classe `TrueClass` en Ruby.

```
true.is_a?(TrueClass) => true
3.is_a?(Integer) => true
true.is_a?(Object) => true
3.is_a?(Object) => true
TrueClass.is_a?(Object) => true
Integer.is_a?(Object) => true
```

Ces objets peuvent être soit mutables, soit immuables.

Immuable signifie qu'il n'y a aucun moyen de changer l'objet une fois qu'il est créé. Il n'y a qu'une seule instance pour une valeur donnée avec un `object_id` et il reste le même peu importe ce que vous faites.

Par défaut en Ruby, les types d'objets immuables sont : `Boolean`, `Numeric`, `nil`, et `Symbol`.

> _Dans MRI, l'`object_id` d'un objet est le même que le `VALUE` qui représente l'objet au niveau C. Pour la plupart des types d'objets, ce `VALUE` est un pointeur vers un emplacement en mémoire où les données réelles de l'objet sont stockées._

Désormais, nous utiliserons `object_id` et `adresse mémoire` de manière interchangeable.

Exécutons du code Ruby dans MRI pour un Symbole immuable et une Chaîne mutable :

```
:symbol.object_id => 808668
:symbol.object_id => 808668
'string'.object_id => 70137215233780
'string'.object_id => 70137215215120
```

Comme vous le voyez, tandis que la version symbole conserve le même object_id pour la même valeur, les valeurs de chaîne appartiennent à des adresses mémoire différentes.

Contrairement à Ruby, JavaScript a des types primitifs.

Ils sont — `Boolean`, `null`, `undefined`, `String`, et `Number`.

Le reste des types de données relève de l'ombre des Objets (`Array`, `Function`, et `Object`). Il n'y a rien de compliqué ici, c'est bien plus simple que Ruby.

```
[] instanceof Array => true
[] instanceof Object => true
3 instanceof Object => false
```

### **Assignation de variable, copie, réassignation et comparaison**

En Ruby, chaque variable est simplement une référence à un objet (puisque tout est un objet).

```
a = 'string'
b = a
```

```
# Si vous réassignez a avec la même valeur
```

```
a = 'string'
puts b => 'string'
puts a == b => true # les valeurs sont les mêmes
puts a.object_id == b.object_id => false # les adresses mémoire diffèrent
```

```
# Si vous réassignez a avec une autre valeur
```

```
a = 'new string'
puts a => 'new string'
puts b => 'string'
puts a == b => false # les valeurs sont différentes
puts a.object_id == b.object_id => false # les adresses mémoire diffèrent aussi
```

Lorsque vous assignez une variable, c'est une référence à un objet et non l'objet lui-même. Lorsque vous copiez un objet `b = a`, les deux variables pointeront vers la même adresse.

Ce comportement est appelé **copie par valeur de référence**.

**Strictement parlant, en Ruby et JavaScript, tout est copié par valeur.**

**En ce qui concerne les objets, les valeurs se trouvent être les adresses mémoire de ces objets. Grâce à cela, nous pouvons modifier les valeurs qui se trouvent à ces adresses mémoire. Encore une fois, cela s'appelle copie par valeur de référence, mais la plupart des gens appellent cela copie par référence.**

Ce serait une copie par référence si, après avoir réassigné `a` à 'new string', `b` pointait également vers la même adresse et avait la même valeur 'new string'.

![Image](https://cdn-media-1.freecodecamp.org/images/EDUJJ3qKxslYQaQU4HGqSfr4CJH5gwgu2e10)
_Lorsque vous déclarez **b = a**, **a** et **b** pointent vers la même adresse mémoire_

![Image](https://cdn-media-1.freecodecamp.org/images/zmQes155ly7g3T0bqcdTDYvL6EQKvlfOADQV)
_Après avoir réassigné **a (a = 'string')**, **a** et **b** pointent vers des adresses mémoire différentes_

Même chose avec un type immuable comme Integer :

```
a = 1
b = a
```

```
a = 1
puts b => 1
puts a == b => true # comparaison par valeur
puts a.object_id == b.object_id => true # comparaison par adresse mémoire
```

Lorsque vous réassignez **a** au même entier, l'adresse mémoire reste la même puisque un entier donné a toujours le même object_id.

Comme vous le voyez, lorsque vous comparez un objet à un autre, il est comparé par valeur. Si vous voulez vérifier s'ils sont le même objet, vous devez utiliser `object_id`.

Voyons la version JavaScript :

```
var a = 'string';
var b = a;
a = 'string'; # a est réassigné à la même valeur
```

```
console.log(a); => 'string'
console.log(b); => 'string'
console.log(a === b); => true // comparaison par valeur
```

```
var a = [];
var b = a;
```

```
console.log(a === b); => true
```

```
a = [];
```

```
console.log(a); => []
console.log(b); => []
console.log(a === b); => false // comparaison par adresse mémoire
```

À l'exception de la comparaison — JavaScript utilise la comparaison par valeur pour les types primitifs et par référence pour les objets. Le comportement semble être le même que dans Ruby.

Eh bien, pas tout à fait.

Les valeurs primitives en JavaScript ne seront pas partagées entre plusieurs variables. Même si vous définissez les variables égales entre elles. Chaque variable représentant une valeur primitive est garantie d'appartenir à un emplacement mémoire unique.

Cela signifie qu'aucune des variables ne pointera jamais vers la même adresse mémoire. Il est également important que la valeur elle-même soit stockée dans un emplacement mémoire physique.

Dans notre exemple, lorsque nous déclarons `b = a`, `b` pointera vers une adresse mémoire différente avec la même valeur 'string' immédiatement. Vous n'avez donc pas besoin de réassigner `a` pour pointer vers une adresse mémoire différente.

**Cela s'appelle copié par valeur** puisque vous n'avez pas accès à l'adresse mémoire, seulement à la valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/-KYjFr8QIDdsGNMvjrsUac-V5KI6soar-ex3)
_Lorsque vous déclarez **a = b**, il est assigné par valeur donc **a** et **b** pointent vers des adresses mémoire différentes_

Voyons un meilleur exemple où tout cela compte.

En Ruby, si nous modifions la valeur qui se trouve à l'adresse mémoire, toutes les références qui pointent vers l'adresse auront la même valeur mise à jour :

```
a = 'x'
b = a
```

```
a.concat('y')
puts a => 'xy'
puts b => 'xy'
```

```
b.concat('z')
puts a => 'xyz'
puts b => 'xyz'
```

```
a = 'z'
puts a => 'z'
puts b => 'xyz'
```

```
a[0] = 'y'
puts a => 'y'
puts b => 'xyz'
```

Vous pourriez penser qu'en JavaScript seule la valeur de `a` changerait, mais non. Vous ne pouvez même pas changer la valeur originale car vous n'avez pas d'accès direct à l'adresse mémoire.

Vous pourriez dire que vous avez assigné 'x' à `a`, mais il a été assigné par valeur donc l'adresse mémoire de `a` contient la valeur 'x', mais vous ne pouvez pas la changer car vous n'avez pas de référence à celle-ci.

```
var a = 'x';
var b = a;
```

```
a.concat('y');
console.log(a); => 'x'
console.log(b); => 'x'
```

```
a[0] = 'z';
console.log(a); => 'x';
```

Le comportement des objets JavaScript et leur implémentation sont les mêmes que ceux des objets mutables de Ruby. Les deux copient par valeur de référence.

Les types primitifs de JavaScript sont copiés par valeur. Le comportement est le même que celui des objets immuables de Ruby qui sont copiés par valeur de référence.

Huh ?

Encore une fois, lorsque vous copiez quelque chose par valeur, cela signifie que vous ne pouvez pas changer (muter) la valeur originale puisque il n'y a pas de référence à l'adresse mémoire. Du point de vue du code, c'est la même chose que d'avoir des entités immuables que vous ne pouvez pas muter.

Si vous comparez Ruby et JavaScript, le seul type de données qui se 'comporte' différemment par défaut est String (c'est pourquoi nous avons utilisé String dans les exemples ci-dessus).

En Ruby, c'est un objet mutable et il est copié/passé par valeur de référence tandis qu'en JavaScript, c'est un type primitif et copié/passé par valeur.

Lorsque vous voulez cloner (pas copier) un objet, vous devez le faire explicitement dans les deux langages pour vous assurer que l'objet original ne sera pas modifié :

```
a = { 'name': 'Kate' }
b = a.clone
b['name'] = 'Anna'
puts a => {:name=>"Kate"}
```

```
var a = { 'name': 'Kate' };
var b = {...a}; // avec la nouvelle syntaxe ES6
b['name'] = 'Anna';
console.log(a); => {name: "Kate"}
```

Il est crucial de s'en souvenir, sinon vous rencontrerez des bugs tenaces lorsque vous invoquerez votre code plus d'une fois. Un bon exemple serait une fonction récursive où vous utilisez l'objet comme argument.

Un autre exemple est React (framework front-end JavaScript) où vous devez toujours passer un nouvel objet pour mettre à jour l'[état](https://facebook.github.io/react/docs/state-and-lifecycle.html) car la comparaison fonctionne sur la base de l'identifiant de l'objet.

C'est plus rapide car vous n'avez pas à parcourir l'objet ligne par ligne pour voir s'il a été modifié.

### Comment les variables sont passées aux fonctions

Le passage de variables aux fonctions fonctionne de la même manière que la copie pour les mêmes types de données dans la plupart des langages.

En JavaScript, les types primitifs sont copiés et passés par valeur et les objets sont copiés et passés par valeur de référence.

Je pense que c'est la raison pour laquelle les gens ne parlent que de passage par valeur ou par référence et ne semblent jamais mentionner la copie. Je suppose qu'ils pensent que la copie fonctionne de la même manière.

```
a = 'b'
```

```
def output(string) # passé par valeur de référence  string = 'c' # réassigné donc pas de référence à l'original  puts string
end
```

```
output(a) => 'c'
puts a => 'b'
```

```
def output2(string) # passé par valeur de référence  string.concat('c') # nous changeons la valeur qui se trouve à l'adresse  puts string
end
```

```
output(a) => 'bc'
puts a => 'bc'
```

Maintenant en JavaScript :

```
var a = 'b';
```

```
function output (string) { // passé par valeur  string = 'c'; // réassigné à une autre valeur  console.log(string);}
```

```
output(a); => 'c'
console.log(a); => 'b'
```

```
function output2 (string) { // passé par valeur  string.concat('c'); // nous ne pouvons pas le modifier sans référence  console.log(string);}
```

```
output2(a); => 'b'
console.log(a); => 'b'
```

Si vous passez un objet (pas un type primitif comme nous l'avons fait) en JavaScript à la fonction, cela fonctionne de la même manière que l'exemple Ruby.

### **Autres langages**

Nous avons déjà vu comment fonctionne la copie/passage par valeur et la copie/passage par valeur de référence. Maintenant, nous allons voir ce que signifie le passage par référence et nous découvrirons également comment nous pouvons changer les objets si nous passons par valeur.

Alors que je cherchais des langages de passage par référence, je n'en ai pas trouvé beaucoup et j'ai fini par choisir Perl. Voyons comment fonctionne la copie en Perl :

```
my $x = 'string';
my $y = $x;
$x = 'new string';
```

```
print "$x"; => 'new string'
print "$y"; => 'string'
```

```
my $a = {data => "string"};
my $b = $a;
$a->{data} = "new string";
```

```
print "$a->{data}\n"; => 'new string'
print "$b->{data}\n"; => 'new string'
```

Eh bien, cela semble être la même chose qu'en Ruby. Je n'ai pas trouvé de preuve, mais je dirais que Perl est copié par valeur de référence pour String.

Maintenant, voyons ce que signifie le passage par référence :

```
my $x = 'string';
print "$x"; => 'string'
```

```
sub foo {  $_[0] = 'new string';  print "$_[0]"; => 'new string'}
```

```
foo($x);
```

```
print "$x"; => 'new string'
```

Puisque Perl est **passé par référence, si vous faites une réassignation dans la fonction, cela changera également la valeur originale de l'adresse mémoire.**

Pour un langage de passage par valeur, j'ai choisi Go car je compte approfondir mes connaissances en Go dans un avenir prévisible :

```
package main
import "fmt"
```

```
func changeAddress(a *int) {  fmt.Println(a)  *a = 0         // définition de la valeur de l'adresse mémoire à 0}
```

```
func changeValue(a int) {  fmt.Println(a)  a = 0          // nous changeons la valeur dans la fonction  fmt.Println(a)}
```

```
func main() {  a := 5  fmt.Println(a)  fmt.Println(&a)  changeValue(a) // a est passé par valeur  fmt.Println(a)  changeAddress(&a) // l'adresse mémoire de a est passée par valeur  fmt.Println(a)}
```

```
Lorsque vous compilez et exécutez le code, vous obtiendrez ce qui suit :
```

```
0xc42000e328
5
5
0xc42000e328
0
```

Si vous voulez changer la valeur d'une adresse mémoire, vous devez utiliser des pointeurs et passer les adresses mémoire par valeur. Un pointeur contient l'adresse mémoire d'une valeur.

L'opérateur `&` génère un pointeur vers son opérande et l'opérateur `*` désigne la valeur sous-jacente du pointeur. Cela signifie essentiellement que vous passez l'adresse mémoire d'une valeur avec `&` et vous définissez la valeur d'une adresse mémoire avec `*`.

### **Conclusion**

Comment évaluer un langage :

1. Comprendre les types de données sous-jacents dans le langage. Lisez quelques spécifications et jouez avec eux. Cela se résume généralement à des types primitifs et des objets. Ensuite, vérifiez si ces objets sont mutables ou immuables. Certains langages utilisent différentes tactiques de copie/passage pour différents types de données.
2. L'étape suivante est l'assignation de variable, la copie, la réassignation et la comparaison. C'est la partie la plus cruciale, je pense. Une fois que vous avez compris cela, vous serez en mesure de comprendre ce qui se passe. Cela aide beaucoup si vous vérifiez les adresses mémoire lorsque vous jouez avec.
3. Le passage de variables aux fonctions n'est généralement pas spécial. Cela fonctionne généralement de la même manière que la copie dans la plupart des langages. Une fois que vous savez comment les variables sont copiées et réassignées, vous savez déjà comment elles sont passées aux fonctions.

Les langages que nous avons utilisés ici :

* **Go** : Copié et passé par valeur
* **JavaScript** : Les types primitifs sont copiés/passés par valeur, les objets sont copiés/passés par valeur de référence
* **Ruby** : Copié et passé par valeur de référence + objets mutables/immuables
* **Perl** : Copié par valeur de référence et passé par référence

Lorsque les gens disent passé par référence, ils veulent généralement dire passé par valeur de référence. **Passer par valeur de référence signifie que les variables sont passées par valeur, mais que ces valeurs sont des références aux objets.**

Comme vous l'avez vu, Ruby n'utilise que le passage par valeur de référence tandis que JavaScript utilise une stratégie mixte. Pourtant, le comportement est le même pour presque tous les types de données en raison de l'implémentation différente des structures de données.

La plupart des langages grand public sont soit copiés et passés par valeur, soit copiés et passés par valeur de référence. Pour la dernière fois : Le passage par valeur de référence est généralement appelé passage par référence.

En général, le passage par valeur est plus sûr car vous ne rencontrerez pas de problèmes puisque vous ne pouvez pas changer accidentellement la valeur originale. C'est aussi plus lent à écrire car vous devez utiliser des pointeurs si vous voulez changer les objets.

C'est la même idée que pour le typage statique vs le typage dynamique — vitesse de développement au détriment de la sécurité. Comme vous l'avez deviné, le passage par valeur est généralement une caractéristique des langages de bas niveau comme C, Java ou Go.

Le passage par référence ou par valeur de référence est généralement utilisé par les langages de haut niveau comme JavaScript, Ruby et Python.

Lorsque vous découvrez un nouveau langage, passez par le processus comme nous l'avons fait ici et vous comprendrez comment il fonctionne.

Ce n'est pas un sujet facile et je ne suis pas sûr que tout soit correct dans ce que j'ai écrit ici. Si vous pensez que j'ai fait des erreurs dans cet article, faites-le moi savoir dans les commentaires.