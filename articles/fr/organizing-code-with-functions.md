---
title: Comment organiser votre code avec des fonctions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-19T17:29:50.000Z'
originalURL: https://freecodecamp.org/news/organizing-code-with-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/organizing-code-with-functions-thumbnail.jpg
tags:
- name: beginner
  slug: beginner
- name: coding
  slug: coding
- name: functions
  slug: functions
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment organiser votre code avec des fonctions
seo_desc: "By Deborah Kurata\nFunctions are a fundamental building block of programming.\
  \ They help us organize our code into manageable and reusable pieces. \nLet's explore\
  \ the basics of functions by way of a burger joint.\nA burger joint may seem like\
  \ an odd plac..."
---

Par Deborah Kurata

Les fonctions sont un élément fondamental de la programmation. Elles nous aident à organiser notre code en morceaux gérables et réutilisables. 

Explorons les bases des fonctions à travers l'exemple d'un restaurant de burgers.

Un restaurant de burgers peut sembler un endroit étrange pour apprendre l'organisation du code... mais voyons où cela nous mène. Et vous pouvez regarder la vidéo associée ici.

%[https://youtu.be/3f4g8RwELC4]

Avez-vous faim de connaissances ? Ou peut-être d'un burger ?

Aborder un ensemble de tâches importantes nécessite une certaine organisation. Supposons que nous travaillons dans un restaurant de burgers. Nous pourrions définir une vue simplifiée du processus comme suit :

1. Prendre la commande d'un client
2. Si le client a commandé des frites, préparer les frites :
   * Verser les frites dans la friteuse
   * Régler le minuteur
   * Etc.
3. Si le client a commandé un burger, préparer le burger :
   * Sélectionner le type de steak approprié (végétarien, poulet, poisson, bœuf)
   * Faire cuire le burger
   * Griller le petit pain
   * Etc.
4. Mettre les articles dans une boîte
5. Recommencer à l'étape 1

Un employé prend la commande d'un client. Si le client a commandé des frites, il prépare les frites. Remarquez la "sous-liste" décrivant comment préparer les frites. Et si le client a commandé un burger, il prépare le burger. Et il y a une autre "sous-liste" décrivant comment préparer le burger.

Pour garder notre liste principale d'instructions simple et plus facile à suivre, nous pouvons déplacer ces sous-listes vers des ensembles d'instructions séparés.

![Les sous-étapes de préparation des frites sont montrées dans une boîte. Les sous-étapes de préparation d'un burger sont montrées dans une deuxième boîte. Les étapes sans les sous-étapes sont montrées à droite.](https://www.freecodecamp.org/news/content/images/2023/01/figure3.jpg)
_Figure 1. Définition des fonctions_

Le côté gauche de la Figure 1 montre la liste des étapes pour préparer les frites, et la liste pour préparer un burger. Nous référençons ces instructions dans le flux principal, comme montré sur le côté droit de la Figure 1. 

Le résultat est que chaque liste séparée d'instructions est clairement définie. Et le flux principal à droite est plus facile à voir sans toutes les sous-listes.

En programmation, nous appelons chacun de ces ensembles d'instructions autonomes une **fonction**.

Arrêtons-nous à ce stade et réfléchissons à cela. Quels sont les avantages de diviser certaines des instructions en fonctions ? Des idées ?

Séparer notre code en fonctions présente plusieurs avantages :

* Lors de la création ou de la maintenance de la fonction, nous pouvons nous concentrer uniquement sur cette fonction : quelles informations elle nécessite, quelles étapes elle effectue et quel résultat elle fournit.
* Nous pouvons simplifier l'ensemble principal d'instructions, le rendant plus facile à lire et à maintenir au fil du temps.
* Cela nous aide à séparer le travail pour une équipe, en attribuant chaque fonction indépendante à un membre de l'équipe. Jesse peut préparer les frites, Chris les burgers, et Sandhya suit le flux principal, en prenant les commandes.
* Et nous pouvons plus facilement réutiliser la fonction à plusieurs endroits dans l'application.

Avez-vous pensé à d'autres avantages ?

## Qu'est-ce qu'une fonction ?

En programmation :

* Une **fonction** est un ensemble autonome d'instructions pour accomplir une partie d'une tâche plus large.
* Une fonction sépare les responsabilités pour une partie spécifique d'une tâche, rendant la tâche principale plus facile à gérer et à lire.
* Les fonctions ajoutent de la structure à nos programmes et les rendent plus faciles à lire et à modifier au fil du temps.

Voici un conseil : Le code est souvent lu beaucoup plus souvent qu'il n'est écrit, alors rendez votre code lisible.

## Anatomie d'une fonction

Lors de l'écriture de code, les fonctions ressemblent à ceci :

### Préparer les frites

```
function makeFries(fries) {
  ... les instructions vont ici ...
  return cookedFries
}
```

### Préparer un burger

```
function makeBurger(patty, bun, condiments) {
  ... les instructions vont ici ...
  return cookedBurger
}
```

Notez que les détails des fonctions peuvent sembler un peu différents selon le langage de programmation que vous utilisez.

Une fonction prend souvent certaines informations, effectue l'ensemble des instructions en utilisant ces informations et renvoie (ou "retourne") un résultat. Dans notre restaurant de burgers, nous pouvons dire : "Hey Chris, voici un steak, un petit pain et des condiments, allez préparer le burger et rapportez-le moi quand c'est fait."

Les fonctions sont souvent nommées avec la tâche qu'elles accomplissent en suivant une convention de nommage verbeObjet : makeFries et makeBurger.

Le nom est suivi d'une liste des informations dont la fonction a besoin. Dans cet exemple, ces informations sont enfermées entre parenthèses et séparées par des virgules. Pour nos makeFries, nous avons besoin des frites. Et pour le burger, nous avons besoin d'un steak, d'un petit pain et de condiments.

Le corps de la fonction contient l'ensemble des instructions requises pour cette fonction.

Dans de nombreux cas, une fonction effectue son ensemble d'étapes et retourne un résultat. Donc, enfin, nous retournons ce résultat. Le résultat est souvent indiqué avec une instruction return. Dans cet exemple, lorsque les frites sont faites ou que le burger est prêt, nous les renvoyons au flux principal et ils sont mis en boîte pour le client.

## Comment créer une fonction

Regardons un autre exemple à partir d'un site web simple d'adoption d'animaux virtuels comme montré dans la Figure 2.

![Capture d'écran d'une page web qui demande le type d'animal (chat) et combien (3), puis affiche "meow" trois fois.](https://www.freecodecamp.org/news/content/images/2023/01/figure5.jpg)
_Figure 2. Site web d'adoption d'animaux virtuels_

L'utilisateur entre le type et le nombre d'animaux, et clique sur Adopter. L'application affiche ensuite un message et un salut de chacun des animaux virtuellement adoptés.

Lors de l'écriture du code pour ce site web, nous voulons simplifier l'ensemble principal d'instructions en séparant la fonctionnalité qui prépare le salut de l'animal. Nous définissons une fonction pour ces instructions comme ceci :

```js
function prepareGreeting(typeOfPet, numberOfPets) { 
  var greeting = '';
  for (let i = 0; i < numberOfPets; i++) {
    if (typeOfPet === 'cat') { 
      greeting += 'meow' + '<br/>';
    }
    if (typeOfPet === 'dog') { 
      greeting += 'woof' + '<br/>';
    }
  }
  return greeting;
}
```

Cette fonction est nommée "prepareGreeting" en suivant notre convention verbeObjet. Il est considéré comme une bonne pratique de donner à chaque fonction un nom significatif.

Pour qu'une fonction effectue son ensemble d'instructions, elle a souvent besoin de certaines informations. Dans ce cas, elle a besoin du type d'animal et du nombre d'animaux. Lors de la création d'une fonction, nous identifions les informations nécessaires en utilisant des paramètres. 

Un **paramètre** est un espace réservé pour les informations dont la fonction a besoin. Nous donnons à chaque espace réservé un nom descriptif, tel que typeOfPet et numberOfPets. Nous ajoutons les paramètres après le nom de la fonction, souvent entre parenthèses et séparés par des virgules.

Le nom de la fonction avec son ensemble de paramètres est appelé une **signature de fonction**. La signature de la fonction identifie de manière unique la fonction.

Le **corps de la fonction** est l'endroit où nous écrivons le code pour effectuer l'ensemble des instructions. Dans cet exemple, c'est là que nous préparons le salut. 

Dans les langages de programmation qui utilisent des accolades, le corps de la fonction est défini entre la première et la dernière accolade. Dans certains langages, le corps de la fonction est défini simplement par son indentation.

Dans ce corps de fonction, nous préparons le salut de l'animal. Tout d'abord, nous initialisons une variable greeting à une chaîne vide. Cela garantit que nous avons une variable de chaîne (ou de texte) que nous pouvons utiliser pour le texte de salut.

Ensuite, nous faisons une boucle pour chaque animal. Nous utilisons un compteur représenté par "i", répétons la boucle tant que notre compteur est inférieur au nombre total d'animaux, et incrémentons "i" à la fin de chaque boucle. Remarquez que dans la plupart des langages de programmation, le comptage est basé sur zéro, ce qui signifie qu'il compte les itérations de la boucle en commençant à 0 : 0, 1, 2 pour trois animaux.

Dans la boucle, si le type d'animal passé est un chat, nous ajoutons un "meow" pour chaque animal à la variable greeting. Si le type d'animal passé est un chien, nous ajoutons "woof" pour chaque animal. Nous retournons ensuite ce salut résultant à l'ensemble principal d'instructions.

## Comment appeler une fonction

Le code dans une fonction ne fera rien jusqu'à ce que nous appelions cette fonction à partir d'un autre code, tel que notre ensemble principal d'instructions. La syntaxe exacte pour appeler une fonction dépend du langage de programmation que vous utilisez. Mais cela ressemblera à ceci :

```js
greetingForDisplay = prepareGreeting("cat", 3)
```

Nous utilisons le nom de la fonction pour identifier quelle fonction nous voulons appeler. Ensuite, nous passons une valeur pour chaque espace réservé de paramètre. Dans cet exemple, nous passons une chaîne (ou texte) en utilisant des guillemets et un nombre.

Le résultat des instructions de la fonction est retourné au code qui l'a appelée. Dans cet exemple, la valeur est assignée à la variable greetingForDisplay. Le code principal pourrait alors afficher le contenu de cette variable à l'utilisateur.

Lors de l'utilisation de fonctions, assurez-vous de garder ces deux termes clairs :

* **Paramètre** : L'espace réservé dans la signature de la fonction où nous définissons quel type d'informations la fonction nécessite.
* **Argument** : La ou les valeurs passées lors de l'appel de la fonction, donnant à la fonction les informations dont elle a besoin pour effectuer ses instructions.

## Conclusion

Nous utilisons une fonction pour définir un ensemble autonome d'instructions pour une partie d'une tâche plus large. L'utilisation de fonctions aide à diviser le code long en morceaux gérables. Tout comme des blocs de construction, nous combinons des fonctions pour créer des applications et des sites web simples à complexes.

Pour plus d'informations sur les concepts généraux de programmation, consultez mon cours : ["Introduction en douceur à la programmation pour débutants"](https://www.youtube.com/playlist?list=PLErOmyzRKOCrO9bwM1931IY8S3iWfhrr8). Et pour des informations sur le développement web, GitHub, Angular et C#, abonnez-vous à [ma chaîne YouTube](https://www.youtube.com/@deborah_kurata).

Maintenant, allons commander ce burger !