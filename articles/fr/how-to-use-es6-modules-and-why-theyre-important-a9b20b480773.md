---
title: Un guide pratique des modules ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T00:02:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PGxaa-3OODqO9Qxz0qnQzA.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Un guide pratique des modules ES6
seo_desc: 'By Dler Ari

  One of the major challenges when building a web-app is how quickly you can scale
  and respond to the market needs. When the demand (requirements) increases, the capabilities
  (features) increase too. It is therefore important to have a soli...'
---

Par Dler Ari

L'un des principaux défis lors de la création d'une application web est la rapidité avec laquelle vous pouvez évoluer et répondre aux besoins du marché. Lorsque la demande (exigences) augmente, les capacités (fonctionnalités) augmentent également. Il est donc important d'avoir une structure architecturale solide afin que l'application croisse de manière organique. Nous ne voulons pas nous retrouver dans des situations où l'application ne peut pas évoluer parce que tout dans l'application est profondément enchevêtré.

> Écrivez du code qui est facile à supprimer, pas facile à étendre.  
> - Tef, Programming is Terrible

Dans cet article, nous allons créer un simple tableau de bord en utilisant des modules ES6, puis présenter des techniques d'optimisation pour améliorer la structure des dossiers et faciliter l'écriture de moins de code. Voyons pourquoi les modules ES6 sont importants et comment les appliquer efficacement.

> JavaScript a eu des modules depuis longtemps. Cependant, ils étaient implémentés via des bibliothèques, pas intégrés dans le langage. ES6 est la première fois que JavaScript a des modules intégrés ([source](http://exploringjs.com/es6/ch_modules.html)).

TL;DR — Si vous voulez voir un exemple pratique où nous créons un tableau de bord en utilisant des modules ES6 à partir d'une maquette de conception architecturale, passez à la section 4.

### Voici ce que nous allons aborder

1. Pourquoi les modules ES6 sont nécessaires
2. Retour dans le temps où les scripts étaient chargés manuellement
3. Comment fonctionnent les modules ES6 (`import` vs `export`)
4. Construisons un tableau de bord avec des modules
5. Techniques d'optimisation pour l'exemple de tableau de bord

> Si vous voulez devenir un meilleur développeur web, démarrer votre propre entreprise, enseigner aux autres ou améliorer vos compétences en développement, je publierai des conseils et astuces hebdomadaires sur les derniers langages web.

### 1. Pourquoi les modules ES6 sont nécessaires

Examinons quelques scénarios pour comprendre pourquoi les modules sont pertinents.

#### Scénario 1 — Ne réinventez pas la roue

En tant que développeurs, nous recréons souvent des choses qui ont déjà été créées sans même en être conscients, ou copions et collons des éléments pour gagner du temps. À la fin, cela s'accumule et nous nous retrouvons avec x nombre de copies identiques dispersées dans l'application. Et chaque fois que nous devons changer quelque chose, nous devons le faire x fois selon le nombre de copies que nous avons.

**Exemple**  
Par exemple, imaginez une usine de voitures essayant de réinventer le moteur à chaque fois qu'elle produit une nouvelle voiture, ou un architecte commençant de zéro après chaque dessin. Ce n'est pas impossible à faire, mais alors quel est l'intérêt de la connaissance si vous ne pouvez pas réutiliser l'expérience que vous avez acquise.

#### Scénario 2 — Barrière de connaissance

Si le système est profondément enchevêtré et manque de documentation, il est difficile pour les anciens/nouveaux développeurs d'apprendre comment l'application fonctionne et comment les choses sont connectées.

**Exemple**  
Par exemple, un développeur devrait être capable de voir le résultat d'un changement sans deviner, sinon nous nous retrouvons avec beaucoup d'erreurs sans savoir par où commencer. Une solution est d'utiliser des modules pour encapsuler le comportement, nous pouvons facilement réduire le processus de débogage et identifier rapidement la racine du problème.

> J'ai récemment écrit un article sur [« Développeurs qui veulent constamment apprendre de nouvelles choses »](https://codeburst.io/developers-that-constantly-want-to-learn-new-things-heres-a-tip-7a16e42302e4), avec des conseils sur la façon d'améliorer les connaissances.

#### Scénario 3 — Comportement inattendu

En évitant la séparation des préoccupations (principe de conception), cela peut conduire à un comportement inattendu.

**Exemple**  
Par exemple, disons que quelqu'un augmente le volume dans la voiture, et cela démarre les essuie-glaces. C'est un exemple de comportement inattendu, et ce n'est pas quelque chose que nous voulons dans notre application.

En bref, nous avons besoin des modules ES6 afin de réutiliser, maintenir, séparer et encapsuler efficacement le comportement interne du comportement externe. Il ne s'agit pas de rendre le système complexe, mais d'avoir la capacité d'évoluer facilement et de supprimer des éléments sans casser le système.

### 2. Retour dans le temps où les scripts étaient chargés manuellement

Si vous avez fait du développement web pendant quelques années, alors vous avez définitivement rencontré des conflits de dépendances tels que des scripts ne se chargeant pas dans le bon ordre, ou que les éléments de l'arbre DOM ne peuvent pas être accessibles par JS.

La raison est que le HTML sur une page est chargé dans l'ordre dans lequel il apparaît, ce qui signifie que nous ne pouvons pas charger les scripts avant que le contenu à l'intérieur de l'élément `<body>` ait fini de se charger.

Par exemple, si vous essayez d'accéder à un élément dans la balise `<body>` en utilisant `document.getElementById("id-name")` et que l'élément n'est pas encore chargé, alors vous obtenez une erreur indéfinie. Pour vous assurer que les scripts sont chargés correctement, nous pouvons utiliser `defer` et `async`. Le premier s'assurera que chaque script se charge dans l'ordre où il apparaît, tandis que le second charge le script dès qu'il devient disponible.

L'ancienne méthode pour résoudre ce problème était de charger les scripts juste avant l'élément `</body>`.

```html
<!DOCTYPE html>
<head>
</head>
<body>
  
  <!-- Le contenu HTML va ici -->
  
  <script src="js/jquery.js"></script>
  <script src="js/script2.js"></script>
  <script src="js/script3.js"></script>
  <script src="js/script4.js"></script>
</body>
</html>
```

Mais à long terme, le nombre de scripts s'accumule et nous pouvons nous retrouver avec 10+ scripts tout en essayant de maintenir les versions et les conflits de dépendances.

#### Séparation des préoccupations

En général, charger des scripts comme montré ci-dessus n'est pas une bonne idée en termes de performance, de dépendances et de maintenabilité. Nous ne voulons pas que le fichier `index.html` ait la responsabilité de charger tous les scripts — nous avons besoin d'une sorte de structure et de séparation de la logique.

La solution est d'utiliser la syntaxe ES6, les instructions `import` et `export`, une approche élégante et maintenable qui nous permet de garder les choses séparées et disponibles uniquement lorsque nous en avons besoin.

#### Les instructions `import` et `export`

Le mot-clé `export` est utilisé lorsque nous voulons rendre quelque chose disponible quelque part, et `import` est utilisé pour accéder à ce que `export` a rendu disponible.

> La règle de base est que pour `importer` quelque chose, vous devez d'abord l'`exporter`.

Et que pouvons-nous réellement `exporter` ?

* Une variable
* Un littéral d'objet
* Une classe
* Une fonction
* ++

Pour simplifier l'exemple comme montré ci-dessus, nous pouvons envelopper tous les scripts dans un fichier.

```js
import { jquery } from './js/jquery.js';
import { script2 } from './js/script2.js';
import { script3 } from './js/script3.js';
import { script4 } from './js/script4.js';
```

Et ensuite, charger simplement le script `app.js` dans notre `index.html`. Mais d'abord, pour que cela fonctionne, nous devons utiliser `type="module"` ([source](https://caniuse.com/#search=modules)) afin que nous puissions utiliser `import` et `export` pour travailler avec des modules.

```js
<!DOCTYPE html>
<head>
</head>
<body>
  
  <!-- Le contenu HTML va ici -->
  
  <script type="module" src="js/app.js"></script>
</body>
</html>

```

Comme vous pouvez le voir, le `index.html` est maintenant responsable d'un seul script, ce qui facilite la maintenance et l'évolution. En bref, le script `app.js` devient notre point d'entrée que nous pouvons utiliser pour démarrer notre application.

Note : Je ne recommanderais pas d'avoir tous les scripts chargés dans un seul fichier comme `app.js`, sauf ceux qui le nécessitent.

Maintenant que nous avons vu comment nous pouvons utiliser les instructions `import` et `export`, voyons comment cela fonctionne lorsque nous travaillons avec des modules en pratique.

### 3. Comment fonctionnent les modules ES6

Quelle est la différence entre un module et un composant ? Un module est une collection de petites unités indépendantes (composants) que nous pouvons réutiliser dans notre application.

#### **Quel est le but ?**

* Encapsuler le comportement
* Facile à utiliser
* Facile à maintenir
* Facile à évoluer

Oui, cela facilite le développement !

#### Alors, qu'est-ce qu'un composant vraiment ?

Un composant peut être une variable, une fonction, une classe, etc. En d'autres termes, tout ce qui peut être exporté par l'instruction `_export_` est un composant (ou vous pouvez l'appeler un bloc, une unité, etc.).

![Image](https://cdn-media-1.freecodecamp.org/images/1*bFMIUptzzXPzaPmtmkdDfw.png)
_Qu'est-ce qu'un composant_

#### Alors, qu'est-ce qu'un module vraiment ?

Comme mentionné, un module est une collection de composants. Si nous avons plusieurs composants qui communiquent, ou qui doivent simplement être affichés ensemble pour former un tout intégré, alors vous avez probablement besoin d'un module.

![Image](https://cdn-media-1.freecodecamp.org/images/1*c1vjeFupwd9ZTALYTluBSw.png)
_Qu'est-ce qu'un module_

#### C'est un défi de tout rendre réutilisable

Un ingénieur principal avec plus de 30 ans d'expérience en ingénierie électrique a un jour dit que nous ne pouvons pas nous attendre à ce que tout soit réutilisé en raison du temps, du coût et que tout n'est pas destiné à être réutilisé. Il est préférable de réutiliser dans une certaine mesure plutôt que de s'attendre à ce que les choses soient réutilisées à 100 %.

En général, cela signifie que nous n'avons pas à rendre tout réutilisable dans l'application. Certaines choses sont simplement destinées à être utilisées une fois. La règle de base est que si vous avez besoin de quelque chose plus de deux fois, alors peut-être est-il bon de créer un module ou un composant.

Au début, cela peut sembler facile de rendre quelque chose réutilisable, mais rappelez-vous, cela nécessite de sortir le composant de son environnement et de s'attendre à ce qu'il fonctionne dans un autre. Mais souvent, nous devons modifier des parties de celui-ci pour le rendre entièrement réutilisable, et avant de vous en rendre compte, vous avez créé deux nouveaux composants.

[Antoine](https://www.freecodecamp.org/news/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773/undefined), a écrit un article décrivant 3 règles essentielles pour créer des composants JS réutilisables, que je recommande de lire. Lorsqu'il a présenté VueJS à son équipe, un collègue expérimenté dit :

> C'est génial en théorie, mais dans mon expérience, ces choses "réutilisables" fantaisistes ne sont jamais réutilisées.

L'idée est que tout ne doit pas être réutilisé, comme les boutons, les champs de saisie et les cases à cocher, etc. Le travail de rendre quelque chose réutilisable nécessite des ressources et du temps, et souvent nous nous retrouvons avec des scénarios de sur-réflexion qui ne se produiraient jamais.

Le PDG de Stack Overflow, Joel Spolsky, dit :

> Une solution à 50 % qui fonctionne résout plus de problèmes et survit plus longtemps qu'une solution à 99 % que personne n'a parce qu'elle est dans votre laboratoire où vous polissez sans fin cette chose. La livraison est une fonctionnalité. Une fonctionnalité vraiment importante. Votre produit doit l'avoir.

### 4. Construisons un tableau de bord avec des modules

Maintenant que nous avons une compréhension de base de comment les modules fonctionnent, examinons un exemple pratique que vous rencontrerez probablement lorsque vous travaillerez avec des frameworks JS. Nous allons créer un simple tableau de bord en suivant une conception architecturale qui consiste en des mises en page et des composants.

Le code pour l'exemple peut être trouvé [ici](https://stackblitz.com/edit/modules-example).

#### Étape 1 — Concevez ce dont vous avez besoin

Dans la plupart des cas, les développeurs sauteraient directement dans le code. Cependant, la conception est une partie importante de la programmation et elle peut vous faire gagner beaucoup de temps et de maux de tête. Rappelez-vous, la conception ne doit pas être parfaite, mais quelque chose qui vous mène dans la bonne direction.

Voici donc ce dont nous avons besoin basé sur la conception architecturale.

* **Composants :** `users.js`, `user-profile.js` et `issues.js`
* **Mises en page :** `header.js` et `sidebar.js`
* **Tableau de bord :** `dashboard.js`

Tous les composants et mises en page seront chargés dans `dashboard.js` et ensuite nous démarrerons `dashboard.js` dans `index.js`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HMlBg4FARbr57a6Wrw2cYg.png)
_Conception architecturale de notre tableau de bord_

Alors pourquoi avons-nous des dossiers de mises en page et de composants ?

Une mise en page est quelque chose dont nous avons besoin une fois, par exemple un modèle statique. Le contenu à l'intérieur du tableau de bord peut changer, mais la barre latérale et l'en-tête resteront les mêmes (et ce sont ce que l'on appelle des mises en page). Une mise en page peut être soit une page d'erreur, un pied de page, une page de statut, etc.

Le dossier des composants est pour les composants généraux que nous réutiliserons probablement plus d'une fois.

Il est important d'avoir une structure de base solide lorsque l'on travaille avec des modules. Pour évoluer efficacement, les dossiers doivent avoir des noms raisonnables qui facilitent la localisation des éléments et le débogage.

> Plus tard, je vous montrerai comment créer une interface dynamique, ce qui nécessite d'avoir un espace de dossier pour les composants et les mises en page dont nous avons besoin.

#### Étape 2 — Configuration de la structure des dossiers

Comme mentionné, nous avons 3 dossiers principaux : dashboard, components et layouts.

```
- dashboard
- components 
- layouts
index.html
index.js ( point d'entrée ) 
```

Et dans chaque fichier à l'intérieur du dossier, nous `exportons` une `classe`.

```
- dashboard
    dashboard.js
- components
    issues.js
    user-profile.js
    users.js 
- layouts
    header.js
    sidebar.js
index.html
index.js ( point d'entrée )
```

#### Étape 3 — Implémentation

La structure des dossiers est prête, donc la prochaine chose à faire est de créer le composant (une `classe`) dans chaque fichier et ensuite l'`exporter`. La convention de code est la même pour le reste des fichiers : chaque composant est simplement une `classe`, et une `méthode` qui console "x component is loaded" où x est le nom du composant afin d'indiquer que le composant a été chargé.

Créons une `classe` utilisateur et ensuite `exportons`-la comme montré ci-dessous.

```js
class Users {

  loadUsers() {
    console.log('Users component is loaded...')
  }
  
}

export { Users };  
```

Remarquez, nous avons diverses [options](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export) lorsque nous traitons avec l'instruction `export`. L'idée est que vous pouvez soit `exporter` des composants individuels, soit une collection de composants. Par exemple, si nous `exportons` la `classe`, nous pouvons accéder aux méthodes déclarées à l'intérieur en créant une nouvelle instance de la `classe`.

```js
export { name1, name2, …, nameN };
export function FunctionName(){...}
export class ClassName {...}
...

export * from …;
export { name1, name2, …, nameN } from …;
export { import1 as name1, import2 as name2, …, nameN } from …;
export { default } from …;
...
```

D'accord, donc si vous regardez le diagramme architectural à l'étape 1, vous remarquerez que le composant `user-profile` est encapsulé par la mise en page `header`. Cela signifie que lorsque nous chargeons la mise en page `header`, elle chargera également le composant `user-profile`.

```js
import { UserProfile } from '../components/users-profile.js';

class Header {

  loadHeader() {
    // Créer une nouvelle instance
    const userProfile = new UserProfile(); 
    
    // Invoquer la méthode (composant)
    userProfile.loadUserProfile();
    
    // Sortie du statut de chargement
    console.log('Header component is loaded...')
  }
  
}

export { Header };
```

Maintenant que chaque composant et mise en page a une `classe` exportée, nous l'`importons` ensuite dans notre fichier `dashboard` comme ceci :

```js
// Depuis le dossier des composants
import { Users } from '../components/users.js';
import { Issues } from '../components/issues.js';

// Depuis le dossier des mises en page
import { Header } from '../layouts/header.js';
import { Sidebar } from '../layouts/sidebar.js';


class Dashboard {

  loadDashboard(){

    // Créer de nouvelles instances
    const users = new Users();
    const issues = new Issues();
    const header = new Header();
    const sidebar = new Sidebar();

    console.log('Dashboard component is loaded');
  }

}

export { Dashboard } 
```

Pour comprendre ce qui se passe vraiment dans le fichier `dashboard`, nous devons revisiter le dessin à l'étape 1. En bref, puisque chaque composant est une `classe`, nous devons créer une nouvelle instance et ensuite l'assigner à un objet. Ensuite, nous utilisons l'objet pour exécuter les méthodes comme montré dans la méthode `loadDashboard()`.

Actuellement, l'application ne produit aucune sortie car nous n'avons pas exécuté la méthode `loadDashboard()`. Pour la faire fonctionner, nous devons `importer` le module `dashboard` dans le fichier `index.js` comme ceci :

```js
import { Dashboard } from './dashboard/dashboard.js'; 

const dashboard = new Dashboard(); 

dashboard.loadDashboard(); 
```

Et ensuite la console produit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*XNy3aKKd_uVYy7O5zcgX3w.png)
_Composants ES6 chargés_

Comme montré, tout fonctionne et les composants se chargent avec succès. Nous pouvons également créer deux instances et ensuite faire quelque chose comme ceci :

```js
import { Dashboard } from './dashboard/dashboard.js'; 

const dashboard_1 = new Dashboard(); 
const dashboard_2 = new Dashboard(); 

dashboard_1.loadDashboard();
dashboard_2.loadDashboard();
```

Ce qui produit le même résultat que montré ci-dessus, mais puisque nous avons deux nouvelles instances, nous obtenons les résultats deux fois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G4-R59VGgccpysU6nxs2dA.png)
_Deux instances uniques de dashboard_

En général, cela nous permet de maintenir et de réutiliser facilement le module dans les fichiers nécessaires sans interférer avec d'autres modules. Nous créons simplement une nouvelle instance qui encapsule les composants.

Cependant, comme mentionné précédemment, le but était de couvrir la dynamique de la façon dont nous pouvons travailler avec des modules et des composants en utilisant les instructions `import` et `export`.

Dans la plupart des cas, lorsque nous travaillons avec des frameworks JS, nous avons généralement une route qui peut changer le contenu du `dashboard`. Actuellement, tout est chargé chaque fois que nous invoquons la méthode `loadDashboard()`, ce qui n'est pas une approche idéale.

### 5. Techniques d'optimisation pour l'exemple de tableau de bord

Maintenant que nous avons une compréhension de base de comment les modules fonctionnent, l'approche n'est pas vraiment évolutive ou intuitive lorsque nous traitons avec de grandes applications qui consistent en de nombreux composants.

Nous avons besoin de quelque chose qui est connu sous le nom d'interface dynamique. Elle nous permet de créer une collection des composants dont nous avons besoin et d'y accéder facilement. Si vous utilisez Visual Studio Code, l'IntelliSense vous montre quels composants sont disponibles et lesquels vous avez déjà utilisés. Cela signifie que vous n'avez pas à ouvrir le dossier/fichier manuellement pour voir quels composants ont été exportés.

Donc, si nous avons un module avec vingt composants, nous ne voulons pas `importer` chaque composant l'un après l'autre. Nous voulons simplement obtenir ce dont nous avons besoin, et c'est tout. Si vous avez travaillé avec des espaces de noms dans des langages comme C#, PHP, C++ ou Java, vous remarquerez que ce concept est similaire dans la nature.

Voici ce que nous voulons réaliser :

```js
// FICHIER : dashboard.js

// Depuis le dossier des composants
import { users, issues } from '../components';

// Depuis le dossier des mises en page
import { header, sidebar } from '../layouts'; 


class Dashboard {

  loadDashboard(){

    // Invoquer les méthodes
    users.loadUsers();
    issues.loadIssues();
    header.loadHeader();
    sidebar.loadSidebar();

    console.log('Dashboard component is loaded');
  }

}

export let dashboard = new Dashboard(); 
```

Comme montré, nous avons moins de lignes de code, et nous l'avons rendu déclaratif sans perdre le contexte. Voyons quels changements nous avons apportés.

#### Créer une interface dynamique (également connue sous le nom de barils)

Une interface dynamique nous permet de créer une collection des choses dont nous avons besoin. C'est comme créer une boîte à outils avec nos outils préférés. Une chose importante à mentionner est qu'une interface dynamique ne doit pas être ajoutée dans chaque dossier, mais dans les dossiers qui consistent en de nombreux composants.

> Ils simplifient grandement les imports et les rendent plus clairs. Nous ne voulons simplement pas avoir trop de fichiers barils puisque cela est contre-productif et conduit généralement à des problèmes de _dépendance circulaire_ qui peuvent parfois être assez délicats à résoudre.   
> - [Adrian Fâciu](https://www.freecodecamp.org/news/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773/undefined)

Pour créer une interface dynamique, nous créons un fichier nommé `index.js` qui est situé à la racine de chaque dossier pour ré-exporter un sous-ensemble de fichiers ou de composants dont nous avons besoin. Le même concept fonctionne en TypeScript, vous changez simplement le type de `.js` à `.ts` comme `index.ts`.

Le `index.js` est le premier fichier qui se charge lorsque nous accédons à l'espace du dossier racine — c'est le même concept que `index.html` qui démarre notre contenu HTML. Cela signifie que nous n'avons pas à écrire explicitement `import { component } from './components**/index.js**'` **,** mais plutôt `import { component } from './components`.

Voici à quoi ressemble une interface dynamique.

```js
// Espace racine -> dossier des composants

// Interface dynamique
export { users } from './users';
export { issues } from './issues';
export { userProfile } from './user-profile';
```

En utilisant une interface dynamique, nous finissons avec un niveau racine de moins à accéder, et aussi moins de code.

```js
// Avant
import { Users } from '../components/users.js';
import { Issues } from '../components/issues.js';
import { Header } from '../layouts/header.js';
import { Sidebar } from '../layouts/sidebar.js';

// Après (avec interface dynamique)
import { users, issues } from '../components';
import { header, sidebar } from '../layouts'; 
```

#### Créer une nouvelle instance à l'exécution

Nous avons supprimé les quatre instances dans notre `dashboard.js`, et à la place créé une instance à l'exécution lorsque chaque composant est exporté. Si vous voulez décider du nom de l'objet, vous pouvez faire `export default new Dashboard()`, et ensuite `import dashView` sans les accolades.

```js
// Avant
export class { dashboard }; 
const dashboard = new Dashboard(); 
dashboard.loadDashboard(); 

// Après
export const dashboard = new Dashboard(); 
dashboard.loadDashboard()
```

Comme montré, nous pouvons directement invoquer la méthode sans avoir besoin de créer une nouvelle instance, et aussi écrire moins de code. Cependant, cela relève de la préférence personnelle et vous pouvez librement décider ce qui est un cas d'utilisation pratique pour votre application et vos exigences.

Et enfin, nous chargeons tous les composants et mises en page avec une méthode.

```js
import { dashboard } from './dashboard/dashboard';

dashboard.loadDashboard();
```

### Conclusion

J'ai commencé avec l'intention de montrer simplement un court exemple de la façon dont vous pouvez `importer` et `exporter` un composant, mais j'ai ensuite ressenti le besoin de partager tout ce que je sais (presque). J'espère que cet article vous donne un aperçu de la façon de gérer efficacement les modules ES6 lors de la création d'applications, et des choses qui sont importantes en termes de séparation des préoccupations (principe de conception).

#### **Les points à retenir :**

* Avec les modules ES6, nous pouvons facilement réutiliser, maintenir, séparer et encapsuler les composants pour qu'ils ne soient pas modifiés par un comportement externe
* Un module est une collection de composants
* Un composant est un bloc individuel
* N'essayez pas de rendre tout réutilisable car cela nécessite du temps et des ressources, et le plus souvent nous ne le réutilisons pas
* Créez un diagramme architectural avant de plonger dans le code
* Pour rendre les composants disponibles dans d'autres fichiers, nous devons d'abord les `exporter` puis les `importer`
* En utilisant `index.js` (même concept pour TypeScript `index.ts`), nous pouvons créer des interfaces dynamiques (barils) pour accéder rapidement aux choses dont nous avons besoin avec moins de code et moins de chemins hiérarchiques
* Vous pouvez `exporter` une nouvelle instance à l'exécution en utilisant `export let objectName = new ClassName()`

La bonne nouvelle est que les choses ont changé et que nous nous dirigeons vers un paradigme basé sur les composants et réutilisable. La question est de savoir comment nous pouvons réutiliser non seulement du code JS simple, mais aussi des éléments HTML de manière pratique et intuitive. Il semble que les modules ES6 combinés avec les [composants web](https://developer.mozilla.org/en-US/docs/Web/Web_Components) pourraient bien nous donner ce dont nous avons besoin pour construire des applications performantes et évolutives.

Voici quelques articles que j'ai écrits sur l'écosystème web ainsi que des conseils et astuces de programmation personnels.

* [Une comparaison entre Angular et React](https://medium.freecodecamp.org/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76)
* [Un esprit chaotique conduit à un code chaotique](https://medium.freecodecamp.org/a-chaotic-mind-leads-to-chaotic-code-e7d6962777c0)
* [Développeurs qui veulent constamment apprendre de nouvelles choses](https://codeburst.io/developers-that-constantly-want-to-learn-new-things-heres-a-tip-7a16e42302e4)
* [Apprenez ces concepts Web de base](https://medium.freecodecamp.org/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0?gi=6274e9c4d599)
* [Améliorez vos compétences avec ces méthodes JavaScript importantes](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f)
* [Programmez plus vite en créant des commandes bash personnalisées](https://codeburst.io/learn-how-to-create-custom-bash-commands-in-less-than-4-minutes-6d4ceadd9590)

Vous pouvez me trouver sur Medium où je publie sur une base hebdomadaire. Ou vous pouvez me suivre sur [Twitter](http://twitter.com/dleroari), où je poste des conseils et astuces pertinents pour le développement web ainsi que des histoires de développement personnelles.