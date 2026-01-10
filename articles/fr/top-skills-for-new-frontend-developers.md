---
title: Compétences essentielles pour les nouveaux développeurs frontend
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-15T16:56:37.000Z'
originalURL: https://freecodecamp.org/news/top-skills-for-new-frontend-developers
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Valuavel.png
tags:
- name: 'Career development '
  slug: career-development
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
seo_title: Compétences essentielles pour les nouveaux développeurs frontend
seo_desc: "By Chaitanya Prabuddha\nAs a frontend developer, it's your job to make\
  \ sure that the user interface of a software program functions properly. \nIt's\
  \ a difficult job because you have to make sure that every component works the way\
  \ it's supposed to so th..."
---

Par Chaitanya Prabuddha

En tant que développeur frontend, votre travail consiste à vous assurer que l'interface utilisateur d'un programme logiciel fonctionne correctement. 

C'est un travail difficile car vous devez vous assurer que chaque composant fonctionne comme prévu afin que les utilisateurs aient une bonne expérience.

Le développement frontend est très demandé en ce moment. Les développeurs frontend gèrent l'UI / UX du logiciel. Et cela est important car les utilisateurs interagissent directement avec le frontend d'une application.

Dans cet article, nous allons parler de certaines des compétences les plus précieuses que les développeurs frontend débutants peuvent cultiver. Apprendre les compétences suivantes vous aidera à progresser dans votre carrière.

## Apprendre le JavaScript moderne (ES6)

Le langage de programmation JavaScript a évolué de ES1 à ES6 au cours des 25 dernières années, et il a inclus de nouvelles capacités merveilleuses avec chaque nouvelle version.

En 2015, ES6 a été publié comme une nouvelle version standardisée de JavaScript. ECMAScript 2015 est un autre nom pour cela. Et ES6 a de nombreuses nouvelles fonctionnalités qui peuvent vous aider à écrire un meilleur code. 

Avec les classes orientées objet, les fonctions fléchées, les littéraux de chaîne et bien plus encore, il est la base des bibliothèques modernes comme React et Vue.

### Fonctionnalités utiles de ES6

#### Affectation par décomposition

➡ Vous pouvez lire des valeurs à partir d'un tableau ou des attributs à partir d'un objet dans des variables individuelles en utilisant l'affectation par décomposition.

Exemples de fonctionnement de l'affectation par décomposition dans ES6 :

```javascript
let myName, myRole;
let array = ['Chaitanya', 'Web Developer'];
[myName, myRole] = array;        // affectation positionnelle se produit ici
console.log(myName, myRole);   // Chaitanya Web Developer
```

```javascript
let myName, myRole;
let object = {myName:'Chaitanya', myRole:'Web Developer'};
({myName, myRole}=object); 
   // les propriétés (clés) sont associées aux noms de variables locales

console.log(myName, myRole); 
   // Chaitanya Web Developer
```

#### Expressions de fonction fléchée

➡ Les expressions de fonction fléchée sont une nouvelle syntaxe pour créer des expressions de fonction ordinaires. Nous pouvons ignorer la fonction et retourner avec un code en une ligne en utilisant les expressions de fonction fléchée.

Exemple d'expressions de fonction fléchée dans ES6 :

```javascript
let getName = ((firstName, lastName) => {
 let myRole = 'Web Developer';
 return `Mon nom est ${firstName} ${lastName}
 Je suis un ${myRole}.`;
});
```

#### Paramètres par défaut

➡ La valeur par défaut pour les arguments de fonction en JavaScript est undefined. Donc, parfois, il est plus pratique d'utiliser une valeur différente à la place. Nous pouvons faire cela en utilisant des paramètres de fonction par défaut.

Exemple de fonctionnement des paramètres par défaut dans ES6 :

```javascript
function add(number1, number2) {
 return number1+number2;
}

add (3,4);   // retourne 7
add(3);     // retourne NaN car number2 est undefined
```

```javascript
function add(num1, num2=7) {
 return num1+num2;
}

add (5,2)   // retourne 7
add(3)     // retourne 10 car num2 a une valeur par défaut = 7
```

### Comment apprendre ES6

1. [JavaScript ES6, ES7, ES8: Apprendre à coder à la pointe (Cours complet)](https://youtu.be/nZ1DMMsyVyI)
2. [Tutoriel ES6 JavaScript pour débutants | Cours intensif ES6](https://youtu.be/WZQc7RUAg18)
3. [JavaScript moderne – Apprendre les imports, exports, let, const et promesses en ES6+](https://www.freecodecamp.org/news/learn-modern-javascript/) 

## Performance et qualité web

Il est crucial que votre site web fonctionne sans accroc et sans erreur. Le temps que met votre site web à charger est affecté par plusieurs facteurs liés à la performance web. 

Il existe des étapes que vous pouvez suivre pour améliorer les performances de votre site si vous avez des problèmes avec votre site qui met trop de temps à charger.

### Comment améliorer la performance web :

1. Utilisez des images optimisées et plus petites. [TinyPNG](https://tinypng.com/) est un bon choix pour compresser des images sans perdre beaucoup de qualité.
2. Supprimez le CSS et le JavaScript indésirables, car cela rend votre code volumineux.
3. Obtenez un bon fournisseur d'hébergement. Certains bons à vérifier sont Linode, Digital Ocean ou SiteGround.
4. **Conseil WordPress :** Supprimez les plugins indésirables. Je ne recommande pas d'utiliser plus de 10 plugins, sauf si c'est nécessaire.

Peu importe si vous créez le site web le plus incroyable jamais vu. S'il ne fonctionne pas efficacement et ne livre pas rapidement du contenu à vos utilisateurs, cela n'aura pas d'importance. 

Les utilisateurs n'aiment pas attendre plus de 3 secondes pour qu'un site web se charge – ce n'est pas beaucoup de temps. Donc, si votre site met plus de temps que cela, votre taux de rebond va exploser.

## Chrome DevTools

Les outils de développement Chrome sont inclus dans le navigateur Google Chrome et les développeurs expérimentés les utilisent tout le temps pour itérer, déboguer et analyser des sites web.

### Les outils de développement Google Chrome incluent :

1. Un panneau de console qui interagit avec JavaScript sur la page en tant que shell ou collecte des logs et des données de diagnostic.
2. Une barre d'outils de périphérique qui vous aide à créer des sites web réactifs.
3. Des éléments utilisés pour gérer le CSS et le Document Object Model (DOM).
4. Des informations sur la performance web.
5. Des fonctions de sécurité et de réseau.

Vous pouvez en apprendre plus sur [Chrome DevTools ici](https://developer.chrome.com/docs/devtools/).

Les outils Chrome DevTools sont très utiles une fois que vous comprenez comment les utiliser confortablement. Vous pouvez utiliser ce **[Chrome DevTools - Cours intensif](https://www.youtube.com/watch?v=gTVpBbFWry8)** par freeCodeCamp pour en apprendre plus à leur sujet.

## Contrôle de version avec Git 

Git, ou **Global Information Tracker**, est un système de contrôle de version distribué open source. C'est un logiciel qui suit les changements dans un ensemble de fichiers, et les développeurs l'utilisent généralement pour coordonner lorsqu'ils travaillent sur le code source ensemble pendant le développement logiciel.

Après tout votre travail acharné de codage, la dernière chose que vous voulez faire est de recommencer votre travail depuis le début si quelque chose ne se passe pas comme prévu. Dans cette situation, Git vous aidera à revenir à la version précédente de votre logiciel sans perdre de code.

Connaître les bases de Git est une compétence que vous (et vos employeurs potentiels et clients) apprécierez.

### Comment apprendre Git

1. [Git et GitHub pour débutants - Cours intensif](https://www.youtube.com/watch?v=RGOj5yH7evk)
2. [Tutoriel Git pour professionnels - Outils et concepts pour maîtriser le contrôle de version avec Git](https://www.youtube.com/watch?v=Uszj_k0DGsg)

## Conception réactive

Les gens accèdent à Internet sur tout, des smartphones et tablettes aux ordinateurs portables et de bureau – et tous ces appareils ont des tailles d'écran différentes. Donc, la conception réactive (qui vous aide à concevoir des applications qui fonctionnent sur toutes les tailles d'écran) devrait être une priorité absolue dans toute application ou site web que vous développez.

💡**Fait amusant :** le trafic mobile **>** le trafic des ordinateurs de bureau.

### Comment fonctionne la conception réactive

Un site web avec des fonctionnalités, du contenu et des médias adaptés aux mobiles est appelé un site réactif. Les sites web réactifs s'adaptent à l'appareil qu'un visiteur utilise, y compris les smartphones, les tablettes et les PC.

### Bonnes pratiques pour la conception réactive

1. Vous devriez utiliser des graphiques vectoriels scalables (SVG).

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-19.png)
_Images normales vs SVG_

2. N'oubliez pas le menu de la barre de navigation. Assurez-vous de construire un menu hamburger pour les appareils à petit écran.

3. Testez votre site web réactif sur une variété d'appareils et de navigateurs, comme d'habitude. Vous pouvez utiliser [Test d'optimisation mobile Google](https://search.google.com/test/mobile-friendly) et [Screen Test](http://mattkersley.com/responsive/) pour tester votre site web.

Une chose à garder à l'esprit concernant la conception réactive est qu'il s'agit d'une fonctionnalité intégrée des frameworks CSS comme Tailwind et Bootstrap. Cela signifie que ces frameworks vous aident à rendre les sites web plus réactifs pour toutes les tailles d'appareils avec un peu moins de travail.

Un site web non réactif avec un design incroyable est sans valeur aujourd'hui. La majorité des gens visiteront probablement votre application ou votre site web sur un appareil mobile.

### Comment apprendre la conception réactive pour un site web

1. [Introduction à la conception web réactive - Tutoriel HTML & CSS](https://www.youtube.com/watch?v=srvUrASNj0s)
2. [Framework CSS Bootstrap - Cours complet pour débutants](https://www.youtube.com/watch?v=-qfEOE4vtxE)
3. [Tutoriel de conception UI / UX – Wireframe, Maquette & Design dans Figma](https://www.youtube.com/watch?v=c9Wg6Cb_YlU)

## Apprendre à travailler avec des frameworks

Les frameworks CSS et JavaScript sont des ensembles de fichiers qui prennent en charge beaucoup de travail pour vous en offrant des fonctionnalités standard. Au lieu de commencer avec une page de texte vierge, vous pouvez commencer avec un fichier de code qui contient déjà beaucoup de JavaScript.

Les frameworks JavaScript et CSS changent la façon dont les développeurs écrivent du code. Certains frameworks ont été construits pour vous aider à créer des interfaces utilisateur compliquées, tandis que d'autres excellent à afficher le contenu de votre site web.

Choisir le bon framework est aussi important que de l'apprendre. Les frameworks populaires ne sont pas toujours un bon choix, et vous devriez en choisir un selon vos exigences spécifiques.

Cela dit, il y en a certains qui sont très demandés et qui valent vraiment la peine d'être appris.

### Frameworks JavaScript recommandés :

1. **React** — C'est un framework JavaScript frontend gratuit et open-source pour créer des interfaces utilisateur basées sur des composants UI. Meta le maintient.
2. **Vue** — Vue.js est un framework JavaScript frontend open-source pour créer des applications monopages et des interfaces utilisateur. Evan You l'a créé.
3. **Svelte** — Rich Harris a conçu Svelte, un compilateur frontend gratuit et open-source qui est actuellement maintenu par Vercel.

### Frameworks CSS recommandés :

1. **Bootstrap** — Bootstrap est un framework open-source pour les composants d'interface qui inclut des modèles basés sur CSS et JavaScript.
2. **Tailwind CSS** — Tailwind CSS est un framework CSS basé sur les utilitaires qui inclut des classes pour créer des designs UI personnalisés.
3. **Bulma** — Bulma est un framework CSS open-source. Il a beaucoup de capacités intégrées qui vous aident à accomplir les choses plus rapidement et avec moins de CSS.

## C'est tout !

Merci d'avoir lu cet article. J'écris également régulièrement sur ma newsletter **[The Learners](https://thelearners.substack.com/)**. Vous pouvez vous inscrire directement ici. **👋👋**

<iframe src="https://thelearners.substack.com/embed" width="500" height="100" scrolling="no"></iframe>