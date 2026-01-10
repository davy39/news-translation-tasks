---
title: Pourquoi vous devriez utiliser des composants React au lieu de HTML
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-03-17T15:34:07.000Z'
originalURL: https://freecodecamp.org/news/intro-to-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/still-using-html-start-using-react-components.png
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: JSX
  slug: jsx
- name: React
  slug: react
seo_title: Pourquoi vous devriez utiliser des composants React au lieu de HTML
seo_desc: 'HTML is the language of the web, but creating entire websites with HTML
  alone can be repetitive and hard to manage.

  In this article, we''re going to see how to use the JavaScript library React as
  a way to add convenience and reusability to our website...'
---

HTML est le langage du web, mais créer des sites web entiers avec HTML seul peut être répétitif et difficile à gérer.

Dans cet article, nous allons voir comment utiliser la bibliothèque JavaScript React comme moyen d'ajouter de la commodité et de la réutilisabilité à nos sites web.

React est un outil puissant pour tout développeur qui connaît HTML et souhaite construire des sites web plus organisés et dynamiques, plus rapidement.

Commençons !

## Pourquoi devrais-je utiliser React au lieu de HTML ?

React est arrivé en 2013 comme une meilleure façon de construire des applications web avec JavaScript. Il est souvent appelé une bibliothèque pour construire des interfaces utilisateur, ou UI.

Ce qui rend React si attrayant à apprendre, c'est qu'il ne remplace pas HTML.

Il tire parti de la popularité et de la force de HTML en tant que langage de programmation le plus populaire, en vous permettant d'utiliser une syntaxe très similaire à HTML pour construire des interfaces et ajouter des fonctionnalités dynamiques à l'aide de JavaScript.

## Comment construire une interface utilisateur avec HTML

Compte tenu de la polyvalence de React, nous pouvons recréer n'importe quel site ou interface utilisateur que nous voyons sur le web.

Pour cette leçon, recréons une partie d'une application que vous utilisez probablement tous les jours : Google Search.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-1-1.png)

Cela peut sembler ambitieux si vous êtes tout nouveau dans React, mais cela nécessite seulement la connaissance de deux concepts simples : HTML et les fonctions JavaScript de base.

Quelle est la façon de construire une interface utilisateur sans connaître React ou même JavaScript ?

En utilisant des éléments HTML dans le cadre d'un document HTML simple.

Voici comment nous afficherions les trois premiers résultats qui apparaissent lorsque vous recherchez "reactjs" dans Google.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Résultats de recherche reactjs</title>
  </head>

  <body>
    <section>
      <div>
        <a href="https://reactjs.org"
          >React - Une bibliothèque JavaScript pour construire des interfaces utilisateur</a
        >
        <div>
          <h3>reactjs.org</h3>
        </div>
        <div>
          React rend la création d'interfaces interactives indolore.
        </div>
      </div>
      <div>
        <a href="https://en.wikipedia.org/wiki/React_(web_framework)"
          >React (Framework Web) - Wikipédia</a
        >
        <div>
          <h3>https://en.wikipedia.org  wiki  React_(web_framework)</h3>
        </div>
        <div>
          React est une bibliothèque JavaScript pour construire des interfaces utilisateur.
        </div>
      </div>
      <div>
        <a href="https://twitter.com/reactjs?lang=en"
          >React (@reactjs) | Twitter</a
        >
        <div>
          <h3>https://twitter.com  reactjs</h3>
        </div>
        <div>
          Les derniers tweets de React (@reactjs).
        </div>
      </div>
    </section>
  </body>
</html>

```

Utiliser du HTML statique seul serait suffisant si nous devions afficher seulement quelques liens.

Mais comment pourrions-nous afficher des centaines ou des milliers de liens de cette manière, tous avec des données différentes, comme un moteur de recherche pourrait avoir besoin de le faire ?

Quelle est la meilleure façon, c'est-à-dire une façon plus simple et plus extensible, d'écrire cela ?

Le HTML seul ne sera pas la réponse. Nous aurons besoin d'un moyen de rendre notre site plus dynamique pour afficher autant de liens que nécessaire.

Lorsque nous devons ajouter un comportement à un site, nous avons besoin de JavaScript. Et puisque notre objectif est de construire de grandes applications avec JavaScript, nous savons utiliser React.

## Comment transformer n'importe quel site HTML en une application React

Transformons notre HTML statique en une application React dynamique.

Cela semble difficile ? C'est plus simple que vous ne le pensez.

Nous pouvons construire une application React à partir d'un seul document HTML. Tout ce que nous devons faire est d'intégrer React avec les scripts externes suivants.*

```html
<script src="https://unpkg.com/react@16/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
<script src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>

```

Le premier est pour construire notre application React, et le second est pour afficher, ou rendre, l'application React dans le navigateur.

Le premier est **React**, le second **ReactDOM**.

Le troisième script est pour intégrer un outil appelé **Babel**. Nous aborderons ce qu'il fait dans un instant.

Voici à quoi ressemble notre code à ce stade :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Résultats de recherche reactjs</title>
    <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>
  </head>

  <body>
    <!-- notre script doit avoir type="text/babel" pour que Babel fonctionne -->
    <script type="text/babel">
      // Le code React ira ici
    </script>
  </body>
</html>

```

... et c'est presque une application React.

Notez que nous avons un script où nous pouvons écrire notre code React, mais pas de HTML.

Corrigeons cela.

## Comment créer et rendre notre application React

Toute application React doit avoir ce qu'on appelle un point d'entrée.

Le **point d'entrée** est un élément HTML où nous insérons notre application React dans la page.

Le point d'entrée conventionnel est une div avec l'id root (`<div id="root"></div>`).

Nous allons ajouter cela, puis utiliser la fonction `render()` de ReactDOM pour effectuer le rendu de l'application.

Le premier est l'application elle-même, c'est-à-dire notre HTML d'avant, et le second doit référencer notre point d'entrée. Nous pouvons créer cette référence en disant `document.getElementById('root')`.

Nous avons donc tout ce dont nous avons besoin pour exécuter notre application React :

```html
<!DOCTYPE html>
<html>

  <head>
    <title>Résultats de recherche reactjs</title>
    <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>
  </head>

  <body>
    <div id="root">

    </div>
    <!-- notre script doit avoir type="text/babel" pour que Babel fonctionne -->
    <script type="text/babel">
      ReactDOM.render(
      <section>
      <div>
        <a href="https://reactjs.org"
          >React - Une bibliothèque JavaScript pour construire des interfaces utilisateur</a
        >
        <div>
          <h3>reactjs.org</h3>
        </div>
        <div>
          React rend la création d'interfaces interactives indolore.
        </div>
      </div>
      <div>
        <a href="https://en.wikipedia.org/wiki/React_(web_framework)">React (Framework Web) - Wikipédia</a>
        <div>
          <h3>https://en.wikipedia.org  wiki  React_(web_framework)</h3>
        </div>
        <div>
          React est une bibliothèque JavaScript pour construire des interfaces utilisateur.
        </div>
      </div>
      <div>
        <a href="https://twitter.com/reactjs?lang=en">React (@reactjs) | Twitter</a>
        <div>
          <h3>https://twitter.com  reactjs</h3>
        </div>
        <div>
          Les derniers tweets de React (@reactjs).
        </div>
      </div>
    </section>, document.getElementById('root'))
    </script>
  </body>

</html>
```

Et si nous regardons notre résultat, cela fonctionne comme avant. Parfait !

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-2-1.png)

Maintenant, utilisons React pour améliorer notre site en affichant dynamiquement nos liens.

## Comment rendre le HTML réutilisable avec les composants React

Si nous examinons notre structure HTML, chaque lien se compose des mêmes parties. Chacun a une URL, un titre, une URL plus courte et un extrait. Pour chaque lien, nous devons répéter les mêmes éléments HTML encore et encore.

En programmation, si vous devez vous répéter beaucoup, c'est probablement un signe que votre code peut être simplifié et raccourci d'une certaine manière. En tant que programmeurs, nous cherchons toujours à nous répéter le moins possible.

Nous essayons d'écrire du code qui est DRY, où vous "ne vous répétez pas".

React est, au cœur, JavaScript plus quelques fonctionnalités pour nous aider à construire des applications.

Et puisque nous travaillons avec JavaScript, quelle est la fonctionnalité JavaScript qui nous permet de créer ou de produire quelque chose autant de fois que nous le souhaitons ?

Une fonction.

Créons-en une ici, et nous l'appellerons Link.

```js
function Link() {
  // créer la sortie HTML du lien
}

```

La raison étant que nous voulons que cette fonction retourne ou produise le HTML d'un lien chaque fois que nous l'appelons.

Pour ce faire, retournons le HTML de notre premier lien :

```js
function Link() {
  return (
    <div>
      <a href="https://reactjs.org">
        React - Une bibliothèque JavaScript pour construire des interfaces utilisateur
      </a>
      <div>
        <h3>reactjs.org</h3>
      </div>
      <div>React rend la création d'interfaces interactives indolore.</div>
    </div>
  );
}

```

Maintenant, utilisons-le pour afficher chaque lien qu'il retourne.

Pour ce faire, au lieu de l'appeler comme `Link()`, dans React, nous pouvons l'écrire comme s'il s'agissait d'un élément HTML `<Link />`.

Si vous voyez cela pour la première fois, cela peut un peu vous perturber.

Ici, nous utilisons la syntaxe HTML, mais nous appelons une fonction JavaScript ! Vous vous y habituerez à mesure que vous verrez cela plus souvent.

(Aussi, avez-vous remarqué que nous n'avons pas eu à utiliser une balise ouvrante et fermante, comme pour un élément HTML normal ? Plus d'informations à ce sujet dans un instant.)

**Comment React convertit-il la syntaxe ressemblant à HTML en JavaScript ?**

Il le fait avec l'aide d'un outil spécial appelé Babel, le troisième script que nous avons ajouté. Vous pouvez voir comment il fonctionne en action ici :

![Babel gif](https://dev-to-uploads.s3.amazonaws.com/i/p3550r6dthfd6onee5eg.gif)

Que se passe-t-il ?

Babel, un outil JavaScript appelé compilateur, convertit ("compile") ce code qui ressemble à HTML en JavaScript valide.

## Qu'est-ce que cette syntaxe de type HTML ? JSX

Ce HTML, qui est en fait du JavaScript, est appelé **JSX**, qui signifie "JavaScript XML".

XML, si vous n'êtes pas familier, est une façon légèrement plus stricte d'écrire HTML.

Plus stricte signifie que nous devons utiliser une barre oblique de fermeture pour les éléments avec une seule balise. Par exemple : `<input>` en HTML en tant que JSX valide est `<input />`.

Donc, pour réitérer, JSX n'est pas du code JavaScript valide.

Cela signifie que vous ne pourriez pas mettre JSX dans un navigateur et vous attendre à ce qu'il fonctionne. Nous avons besoin à la fois d'un compilateur, comme Babel, pour le convertir en JavaScript valide, puis de React pour utiliser ce JavaScript créé.

Maintenant, pour utiliser notre élément Link personnalisé, nous supprimons tout le HTML des trois liens et les remplaçons par trois Links, comme ceci :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Résultats de recherche reactjs</title>

    <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>
  </head>

  <body>
    <div id="root"></div>

    <script type="text/babel">
      ReactDOM.render(
        <section>
          <Link />
          <Link />
          <Link />
        </section>,
        document.getElementById("root")
      );
    </script>
  </body>
</html>

```

Et si nous regardons notre résultat, nous avons effectivement trois liens.

C'est la puissance de React : il prend la réutilisabilité des fonctions JavaScript, mais nous permet de les utiliser comme s'il s'agissait de HTML.

Nous appelons ces éléments personnalisés créés avec JavaScript des **composants**.

Nous avons donc gagné beaucoup en lisibilité ici en utilisant des composants. Nous n'avons aucune confusion sur ce que nous regardons si nous avons bien nommé nos composants. Pas besoin de lire à travers une tonne d'éléments HTML pour voir ce que l'application affiche.

Nous voyons immédiatement que nous avons trois liens personnalisés.

## L'anatomie d'un composant fonctionnel

Maintenant que nous savons comment fonctionnent les composants, prenons un second regard sur notre composant fonctionnel Link :

Notre code peut sembler assez simple, mais il y a quelques choses subtiles auxquelles vous devez prêter attention ici :

```js
function Link() {
  return (
    <div>
      <a href="https://reactjs.org">
        React - Une bibliothèque JavaScript pour construire des interfaces utilisateur
      </a>
      <div>
        <h3>reactjs.org</h3>
      </div>
      <div>React rend la création d'interfaces interactives indolore.</div>
    </div>
  );
}

```

Le nom du composant fonctionnel est en majuscule : Link au lieu de link. Il s'agit d'une convention de nommage requise pour les composants React. Nous utilisons un nom en majuscule pour distinguer les composants des fonctions normales. Notez que les fonctions qui retournent du JSX ne sont pas les mêmes que les fonctions JavaScript normales.

Remarquez comment le JSX que nous retournons a une paire de parenthèses autour. Lorsque vous écrivez votre code React pour la première fois, il est facile d'oublier ces parenthèses, ce qui entraînera une erreur. Entourez votre JSX de parenthèses s'il s'étend sur plus d'une ligne.

Enfin, notre fonction Link retourne du JSX. Chaque composant React doit retourner soit des éléments JSX, soit d'autres composants React. Et oui, les composants React peuvent retourner d'autres composants.

Puisque les composants React peuvent retourner d'autres composants React, nous pouvons créer un composant App.

Ce composant App contiendra l'ensemble ou l'**arbre de composants** et montrera de quoi notre application est composée.

Et avec un composant App, cela rend notre méthode de rendu beaucoup plus facile à lire :

```html
<!DOCTYPE html>
<html>

  <head>
   ...
  </head>

  <body>
    <div id="root"></div>

    <script type="text/babel">
      function Link() {
        return (
          <div>
            <a href="https://reactjs.org">
              React - Une bibliothèque JavaScript pour construire des interfaces utilisateur
            </a>
            <div>
              <h3>reactjs.org</h3>
            </div>
            <div>React rend la création d'interfaces interactives indolore.</div>
          </div>
        );
      }

      function App() {
        return (
          <section>
            <Link />
            <Link />
            <Link />
          </section>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>

</html>
```

Nous voyons à partir de ce code que les composants React ont une hiérarchie ou un ordre comme les éléments HTML. En conséquence, nous pouvons nous référer à différentes parties de notre arbre de composants comme étant des **parents** ou des **enfants**.

Dans ce cas, par exemple, pour chaque composant Link rendu, App est le parent. Pour App, les trois Links sont ses enfants.

Notez que chaque fois que nous rendons ou retournons du JSX, il ne peut y avoir qu'un seul composant parent. Mais un composant parent peut avoir autant de composants enfants (ainsi que d'éléments) que nécessaire.

Lorsque nous regardons la sortie de notre code, vous avez probablement remarqué le problème suivant :

Nous avons trois instances du même lien ! C'est parce que nous utilisons les mêmes données pour chaque lien que nous créons. Pourtant, nous savons que chaque lien a des données différentes : un titre, une URL, une URL courte et un extrait différents.

Alors, comment transmettons-nous des données uniques à nos composants ?

## Comment transmettre des données dynamiques aux composants : Props

Si nous voulions transmettre un texte de titre à une fonction JavaScript normale, nous le ferions comme ceci :

```js
Link("Notre titre de lien ici");

```

Mais comment transmettons-nous des données aux **composants fonctionnels** ?

Les éléments HTML normaux acceptent des données sous forme d'attributs. Mais contrairement aux attributs HTML, les attributs ne sont pas reconnus sur les composants React. Les données ne restent pas sur le composant lui-même. Où vont-elles ?

En tant qu'arguments de la fonction composant. Encore une fois, c'est quelque chose que nous connaissons puisque nous connaissons les bases des fonctions.

Nous savons que les fonctions produisent des données en utilisant `return` et acceptent des données avec des _arguments_.

Si nous avions un élément HTML, disons un div avec un attribut appelé "title", ce code serait invalide. HTML n'a pas d'attributs de titre pour aucun de ses éléments :

```html
<div title="Notre titre de lien ici"></div>

```

Mais si nous créions cet attribut "title" sur notre composant Link :

```html
<link title="Notre titre de lien ici" />

```

Cela est valide. Et puisque nous avons écrit title comme un attribut sur notre composant, il est passé à la fonction Link en tant qu'argument appelé "title".

En code, nous pouvons le penser comme ceci :

```js
const linkData = { title: "Notre titre de lien ici" };

Link(linkData);

```

Remarquez que l'argument linkData est un objet.

React collecte et organise les données passées à un composant donné en un seul objet.

Le nom des données passées à un composant, comme title, est **props**.

Toutes les valeurs de props existent au sein du composant fonctionnel lui-même sur un objet props.

Et puisque notre objectif est d'utiliser notre prop title au sein de notre composant Link, nous pouvons écrire ce qui suit :

```js
function Link(props) {
  return <a>{props.title}</a>;
}

```

Nous utilisons la syntaxe des accolades `{}` pour insérer la prop title de props.title où nous le voulons. Et cela s'applique à toute autre prop transmise à un composant.

Ces accolades nous permettent d'insérer ou d'interpoler des valeurs dynamiques où nous en avons besoin.

Maintenant, nous avons tout ce dont nous avons besoin pour corriger nos liens. Pour chacun des composants Link, nous devons transmettre leur titre, URL, URL courte et extrait en tant que props individuels :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Résultats de recherche reactjs</title>

    <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6.26.0/babel.js"></script>
  </head>

  <body>
    <div id="root"></div>

    <script type="text/babel">
      function Link(props) {
        return (
          <div>
            <a href={props.url}>{props.title}</a>
            <div>
              <h3>{props.shortUrl}</h3>
            </div>
            <div>{props.excerpt}</div>
          </div>
        );
      }

      function App() {
        return (
          <section>
            <Link
              title="React - Une bibliothèque JavaScript pour construire des interfaces utilisateur"
              url="https://reactjs.org"
              // les props composées de deux mots ou plus doivent être écrites en camelcase
              shortUrl="reactjs.org"
              excerpt="React rend la création d'interfaces interactives indolore."
            />
            <Link
              title="React (Framework Web) - Wikipédia"
              url="https://en.wikipedia.org/wiki/React_(web_framework)"
              shortUrl="en.wikipedia.org  wiki  React_(web_framework)"
              excerpt="React est une bibliothèque JavaScript pour construire des interfaces utilisateur."
            />
            <Link
              title="React (@reactjs) | Twitter"
              url="https://twitter.com/reactjs"
              shortUrl="twitter.com  reactjs"
              excerpt="Les derniers tweets de React (@reactjs)."
            />
          </section>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>
</html>

```

En regardant notre sortie, nous obtenons toujours le même résultat.

Mais il y a eu un compromis ici. Grâce aux props, nous avons pu rendre notre composant Link beaucoup plus lisible.

Maintenant, nous pouvons créer n'importe quel Link basé sur les données de props (valides) que nous lui donnons.

Mais maintenant, vous pouvez voir que notre composant App est devenu beaucoup plus grand en fournissant les valeurs des props immédiatement sur chaque Link.

_N'y a-t-il pas un moyen de déplacer toutes ces données ailleurs ?_

## Comment séparer les données de l'interface

Déplaçons nos données hors de l'arbre de composants et mettons-les quelque part de plus pratique, mais utilisons toujours les données selon les besoins.

Pour ce faire, nous allons créer un tableau d'objets avec les données de lien à transmettre aux composants Link via les props.

Cela nous permet de mettre nos données où nous voulons, même dans un autre fichier JavaScript. L'avantage est qu'elles n'encombrent plus nos composants.

```html
<!DOCTYPE html>
<html>
  <head>
    ...
  </head>

  <body>
    <div id="root"></div>

    <script type="text/babel">
      const linkData = [
        {
          title: "React - Une bibliothèque JavaScript pour construire des interfaces utilisateur",
          url: "https://reactjs.org",
          shortUrl: "reactjs.org",
          excerpt: "React rend la création d'interfaces interactives indolore."
        },
        {
          title: "React (Framework Web) - Wikipédia",
          url: "https://en.wikipedia.org/wiki/React_(web_framework)",
          shortUrl: "en.wikipedia.org  wiki  React_(web_framework)",
          excerpt: "React est une bibliothèque JavaScript pour construire des interfaces utilisateur."
        },
        {
          title: "React (@reactjs) | Twitter",
          url: "https://twitter.com/reactjs",
          shortUrl: "twitter.com  reactjs",
          excerpt: "Les derniers tweets de React (@reactjs)."
        }
      ];

      function Link(props) {
        return (
          <div>
            <a href={props.url}>{props.title}</a>
            <div>
              <h3>{props.shortUrl}</h3>
            </div>
            <div>{props.excerpt}</div>
          </div>
        );
      }

      function App() {
        return (
          <section>
            <Link title="" url="" shortUrl="" excerpt="" />
            <Link title="" url="" shortUrl="" excerpt="" />
            <Link title="" url="" shortUrl="" excerpt="" />
          </section>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>
</html>

```

Maintenant, comment affichons-nous chaque Link avec ses données en utilisant le tableau linkData ?

Si vous avez déjà travaillé avec des tableaux, pour obtenir chaque élément, nous parcourons ou itérons sur le tableau. Ici, pour chaque boucle, nous pouvons transmettre les données des props au composant Link à nouveau.

Ce modèle est très courant dans React. Tellement courant qu'il existe une méthode de tableau spéciale que nous pouvons utiliser pour effectuer cette itération, appelée .map(). Elle n'est pas la même que la méthode map en JavaScript régulier—elle est pour travailler avec JSX et les composants seuls.

```html
<!DOCTYPE html>
<html>

  <head>
    ...
  </head>

  <body>
    <div id="root"></div>

    <script type="text/babel">
      const linkData = [
        {
          title: "React - Une bibliothèque JavaScript pour construire des interfaces utilisateur",
          url: "https://reactjs.org",
          shortUrl: "reactjs.org",
          excerpt: "React rend la création d'interfaces interactives indolore."
        },
        {
          title: "React (Framework Web) - Wikipédia",
          url: "https://en.wikipedia.org/wiki/React_(web_framework)",
          shortUrl: "en.wikipedia.org  wiki  React_(web_framework)",
          excerpt: "React est une bibliothèque JavaScript pour construire des interfaces utilisateur."
        },
        {
          title: "React (@reactjs) | Twitter",
          url: "https://twitter.com/reactjs",
          shortUrl: "twitter.com  reactjs",
          excerpt: "Les derniers tweets de React (@reactjs)."
        }
      ];

      function Link(props) {
        return (
          <div>
            <a href={props.url}>{props.title}</a>
            <div>
              <h3>{props.shortUrl}</h3>
            </div>
            <div>{props.excerpt}</div>
          </div>
        );
      }

      function App() {
        return (
          <section>
            {linkData.map(function(link) {
              return (
                <Link
                  key={link.url}
                  title={link.title}
                  url={link.url}
                  shortUrl={link.shortUrl}
                  excerpt={link.excerpt}
                />
              );
            })}
          </section>
        );
      }

      ReactDOM.render(<App />, document.getElementById("root"));
    </script>
  </body>

</html>
```

En déplaçant nos données hors de l'interface utilisateur et en affichant chaque lien en utilisant .map(), nous avons une application React beaucoup plus simple qui peut accepter autant de liens que nous choisissons.

Enfin, notez dans notre code que là où nous parcourons notre linkData, l'expression entière est entourée de nos accolades. Soyez conscient que JSX nous permet d'insérer n'importe quelle expression JavaScript valide entre les accolades.

## Comment construire des applications à la manière "React"

Quel était l'intérêt de couvrir ces différents modèles ?

Non seulement pour couvrir les bases de JSX et comment React combine HTML et JavaScript, mais aussi pour vous montrer comment les développeurs React pensent.

Comment pensez-vous comme un développeur React ? En sachant comment décomposer votre interface utilisateur en composants réutilisables.

Lorsque qu'un développeur React planifie une application qu'il veut créer, il commence par identifier toutes les parties individuelles de l'application et voit quelles parties peuvent être transformées en composants réutilisables.

Nous faisons cela en voyant si chaque partie a les mêmes structures visuelles (HTML) et accepte les mêmes ensembles de données ou très similaires (via les props).

Maintenant, pour boucler la boucle, prenons un nouveau regard sur l'interface utilisateur de départ que nous voulions recréer au début.

Si nous devions regarder cela comme un développeur React, cela pourrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/image-3-1.png)

Plus vous devenez bon dans l'utilisation des composants, plus vous serez en mesure de construire vos propres sites web et applications avec facilité.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.reactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.reactbootcamp.com)
*Cliquez pour commencer*