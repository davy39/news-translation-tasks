---
title: Les directives *ngFor et *ngIf d'Angular expliquées pour les débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-07T20:45:34.000Z'
originalURL: https://freecodecamp.org/news/angular-ngfor-and-ngif-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/How-to-Build-a-Weather-Application-using-React--3-.png
tags:
- name: Angular
  slug: angular
- name: clean code
  slug: clean-code
seo_title: Les directives *ngFor et *ngIf d'Angular expliquées pour les débutants
seo_desc: 'By Nishant Kumar

  ngIf and ngFor can help you keep your Angular code clean, simple, and effective.
  So, let''s learn what ngFor and ngIf are all about.

  What is *ngFor?

  Let''s talk about ngFor first. You use the ngFor directive to traverse over an array
  o...'
---

Par Nishant Kumar

*ngIf et *ngFor peuvent vous aider à garder votre code Angular propre, simple et efficace. Alors, apprenons ce que sont *ngFor et *ngIf.

## Qu'est-ce que *ngFor ?

Parlons d'abord de *ngFor. Vous utilisez la directive *ngFor pour parcourir un objet de type tableau et afficher les données dans l'interface utilisateur.

Voici un exemple de son fonctionnement :

```
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular-project';
  friendslist = [
    {
      name: 'Nishant',
      age: 25
    },
    {
      name: 'Shailesh',
      age: 45
    },
    {
      name: 'Abhishek',
      age: 36
    },
    {
      name: 'Akshay',
      age: 65
    },
    {
      name: 'Ashish',
      age: 12
    },
    {
      name: 'Uday',
      age: 31
    },
    {
      name: 'Mayank',
      age: 45
    },
    {
      name: 'Raju',
      age: 74
    },
  ]

}

```

J'ai ici un tableau d'objets qui contient les noms des personnes et leurs âges.

Maintenant, nous allons utiliser *ngFor pour afficher ces noms dans l'interface.

Tout d'abord, créez une balise Unordered List, et à l'intérieur de celle-ci, créez une balise List, comme ceci :

```
<ul>
  <li>
    
  </li>
</ul>
```

Ensuite, nous allons utiliser *ngFor dans la balise List, comme dans l'exemple ci-dessous :

```
<ul>
  <li *ngFor="let item of friendslist">
	Le nom et l'âge sont ici
  </li>
</ul>
```

Dans cet exemple, nous créons un élément en utilisant le mot-clé `let` du tableau **`friendlist`**. Il va itérer sur chaque élément du tableau et afficher le nom de l'élément et l'âge de l'élément, ou toute autre clé d'objet que nous avons dans l'objet du tableau.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-04-112438-1.png)

Vous verrez la sortie ci-dessus lorsque vous enregistrerez. C'est parce que nous avons 8 éléments dans le tableau. Donc, nous obtenons 8 éléments dans notre balise de liste. Mais il s'agit de données statiques, alors changeons-les en données dynamiques.

```
<ul>
  <li *ngFor="let item of friendslist">
    {{ item.name }} {{ item.age }}
  </li>
</ul>
```

Ici, nous utilisons `item.name` et `item.age` entre deux accolades. Cela s'appelle l'interpolation, et c'est ainsi que nous affichons les données dans le modèle HTML.

Enregistrez le fichier, et vous verrez ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-04-113446.png)
_Affichage des objets du tableau sous forme de liste_

Nous pouvons également faire quelque chose comme ceci :

```
<ul>
  <li *ngFor="let item of friendslist">
    {{ item.name }} a {{ item.age }} ans
  </li>
</ul>

```

Ainsi, dans cet exemple, nous affichons la liste dans un format différent. Si vous enregistrez, vous verrez la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-04-113652.png)

## Qu'est-ce que *ngIf ?

Vous utilisez la directive *ngIf dans Angular pour afficher certaines données ou un certain élément en fonction d'une condition.

Supposons que nous appelons une API. Nous affichons un message indiquant que les données sont en cours de chargement pendant que l'application récupère les données de l'API, car cela peut prendre un certain temps en fonction du serveur. Et lorsque l'appel à l'API est terminé, nous affichons les données.

Dans ce cas, nous pouvons utiliser *ngIf.

Voici un exemple de son fonctionnement :

```
<ul>
  <li *ngFor="let item of friendslist">
    {{ item.name }} a {{ item.age }} ans
  </li>
</ul>
```

Ici, nous affichons les données du tableau dans le modèle.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-04-113652-1.png)

Maintenant, créons un bouton et donnons-lui le titre _Cliquez pour masquer la liste_.

```
<ul>
  <li *ngFor="let item of friendslist">
    {{ item.name }} a {{ item.age }} ans
  </li>
</ul>

<button>
  Cliquez pour masquer la liste
</button>
```

Maintenant, dans le fichier TypeScript, créez une variable booléenne appelée `isVisible` :

```
isVisible: boolean = true;
```

Initialement, la valeur de isVisible est true. Créez également une fonction appelée `hideList()` qui changera la valeur de `isVisible` en false si elle est déclenchée.

```
hideList(){
    this.isVisible = false;
}
```

Au clic du bouton que nous avons créé, nous exécuterons cette fonction :

```
<button (click)="hideList()">
  Cliquez pour masquer la liste
</button>
```

Ainsi, chaque fois que le bouton est cliqué, cette fonction s'exécutera. Cela changera la valeur de `hideList` de true à false.

Maintenant, utilisons *ngIf pour afficher notre liste de tableau lorsque `isVisible` est true.

```
<ul *ngIf="isVisible">
  <li *ngFor="let item of friendslist">
    {{ item.name }} a {{ item.age }} ans
  </li>
</ul>

<button (click)="hideList()">
  Cliquez pour masquer la liste
</button>
```

Si vous cliquez sur le bouton Masquer la liste, la liste sera masquée et vous ne verrez que le bouton.

Nous pouvons également changer la valeur comme ceci :

```
hideList(){
    this.isVisible = !this.isVisible;
}
```

Ainsi, si la valeur est true, elle passera à false. Et si la valeur est false, elle passera à true. En d'autres termes, cette fonction basculera la valeur de `isVisible`.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-04-115129.png)
_Si la valeur de isVisible est true_

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-04-115200-1.png)
_Si la valeur de isVisible est false_

## **Conclusion**

Félicitations ! Nous avons maintenant appris à utiliser *ngFor et *ngIf dans Angular.

Alors, allez-y et expérimentez un peu. Il y a des tonnes de choses que vous pouvez faire.

Vous pouvez consulter ma vidéo sur [Angular *ngFor et *ngIf expliqués en 10 minutes](https://www.youtube.com/watch?v=ULHisBAyWZI&t=39s&ab_channel=Cybernatico), qui est sur ma chaîne YouTube.

N'hésitez pas à télécharger le code ici : [https://github.com/nishant-666/Angular-ngFor-and-ngIf](https://github.com/nishant-666/Angular-ngFor-and-ngIf)

> Bon apprentissage.