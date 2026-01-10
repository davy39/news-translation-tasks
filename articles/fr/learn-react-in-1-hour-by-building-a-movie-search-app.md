---
title: Apprendre React en 1 Heure en Construisant une Application de Recherche de
  Films
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-06T14:17:15.000Z'
originalURL: https://freecodecamp.org/news/learn-react-in-1-hour-by-building-a-movie-search-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-01-at-17.18.11.png
tags:
- name: React
  slug: react
seo_title: Apprendre React en 1 Heure en Construisant une Application de Recherche
  de Films
seo_desc: "By Per Harald Borgen\nIf you've been meaning to learn React but are unsure\
  \ of where to start, Scrimba's brand new Build a Movie Search App course is perfect\
  \ for you! \nIn this course, you'll be guided through the app's creation from start\
  \ to finish in ..."
---

Par Per Harald Borgen

Si vous avez l'intention d'apprendre React mais que vous ne savez pas par où commencer, le tout nouveau cours de Scrimba [Construire une Application de Recherche de Films](https://scrimba.com/course/greactmovie?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) est parfait pour vous !

Dans ce cours, vous serez guidé à travers la création de l'application de début à fin en seulement une heure. Et vous travaillerez sur des défis interactifs tout au long du parcours qui vous aideront à acquérir la mémoire musculaire nécessaire pour devenir un développeur React efficace.

## Pourquoi apprendre React ?

React est le framework front-end le plus populaire au monde. Comme le stipulent [les docs](https://reactjs.org/), React rend la création d'interfaces utilisateur interactives et de code plus prévisible, ce qui est plus facile à déboguer. Avec React, vous pouvez produire des interfaces utilisateur complexes en construisant des composants réutilisables qui gèrent leur propre état.

## Que fait ce cours ?

[![Cartes de films stylisées](https://dev-to-uploads.s3.amazonaws.com/i/mspewise511f3ub7eyn9.png)](https://scrimba.com/course/greactmovie?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

Ce parcours d'apprentissage vous guide à travers 11 screencasts interactifs, vous montrant les concepts clés suivants de React moderne :

- Comment obtenir une clé API
- Ajout de styles de base
- Création et stylisation de composants
- Création de fonctions
- Gestion de l'état en utilisant les hooks
- Affichage d'informations
- Création et stylisation de cartes

## Introduction à l'enseignant

Ce tutoriel est dirigé par James Q. Quick, un développeur Web full-stack qui parle régulièrement lors d'événements communautaires et participe à des Hackathons. Il gère également une chaîne YouTube enseignant le développement web. Sa devise 'Apprendre. Construire. Enseigner.' fait de lui l'enseignant parfait pour ce cours pratique.

## Prérequis

Pour étudier ce cours efficacement, vous devez avoir des connaissances de base en HTML, CSS et JavaScript. Il sera également utile d'avoir déjà vu du code React, mais ce n'est pas une obligation.

Si vous avez besoin de plus de connaissances de base, consultez ces excellents cours gratuits de Scrimba :

- [HTML et CSS](https://scrimba.com/course/ghtmlcss?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)
- [Javascript](https://scrimba.com/course/gintrotojavascript?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

Si vous êtes prêt à vous lancer avec React, commençons !

## Introduction au cours

[![Titre de la première diapositive du cours Construire une Application de Recherche de Films](https://dev-to-uploads.s3.amazonaws.com/i/n0xmel3r6k0qiazx8v0p.png)](https://scrimba.com/p/pZaznUL/cdVKdrtr?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

Dans [le premier scrim](https://scrimba.com/p/pZaznUL/cdVKdrtr?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), James nous présente quelques-unes des fonctionnalités clés de l'application que nous allons construire et nous donne un bref aperçu de son fonctionnement. Enfin, James nous présente l'API que nous allons utiliser - [themoviedb.org](https://www.themoviedb.org/).

## Comment obtenir votre clé API Movie DB

[![Génération d'une clé API MovieDB](https://dev-to-uploads.s3.amazonaws.com/i/xe8kqht68qhkbpn6bvo5.png)](https://scrimba.com/p/pZaznUL/cdVKdLSk?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

Dans [ce court cast](https://scrimba.com/p/pZaznUL/cdVKdLSk?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), James nous explique comment obtenir une clé API Movie DB en s'inscrivant avec un compte gratuit. C'est super simple et cela prend seulement quelques minutes. Cliquez sur l'image ci-dessus pour accéder au cours.

## Ajouter des styles de base à votre application

[Ensuite](https://scrimba.com/p/pZaznUL/cNDyQvc2?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), James nous montre l'application React de base qu'il a instanciée pour nous :

```js
import React from "react";
import ReactDOM from "react-dom";

class Main extends React.Component {
	render() {
		return <h1>Bonjour le monde !</h1>;
	}
}

ReactDOM.render(<Main />, document.getElementById("root"));
```

Nous ajoutons ensuite quelques styles de base à notre fichier `style.css` incluant les marges et le padding, les styles de titre et, le Graal de CSS - centrer le contenu de l'application. [Cliquez ici](https://scrimba.com/p/pZaznUL/cNDyQvc2?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) pour voir les styles par vous-même.

## Créez votre premier composant

[![Notre première application React en action](https://dev-to-uploads.s3.amazonaws.com/i/avats2r0wi0mz89mivbr.png)](https://scrimba.com/p/pZaznUL/caZvgqTk?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

[Dans ce scrim](https://scrimba.com/p/pZaznUL/caZvgqTk?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), nous avons notre premier défi - créer un composant React. James utilise un fichier `test.js` pour nous donner un bref aperçu de ce qui est nécessaire avant de décomposer la tâche en morceaux gérables :

```html
//pour créer le composant SearchMovies //form avec une classe de form //label avec
htmlFor="query" et une classe de Label //input de type text avec un nom de "query"
et un placeholder //button class de button et un type de submit
```

Cliquez sur le lien ou l'image ci-dessus pour mettre la main à la pâte et essayer le défi.

## Stylisez le composant Search Movies

[![Notre première application React avec des styles ajoutés](https://dev-to-uploads.s3.amazonaws.com/i/752w2eczfd6vo21o1b1j.png)](https://scrimba.com/p/pZaznUL/c6WdV7Ap?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

[Ensuite](https://scrimba.com/p/pZaznUL/c6WdV7Ap?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), il est temps de styliser notre nouvelle application. James suggère quelques styles pour notre `<form>`, `<label>`, `<input>` et `<button>` et ajoute une requête média pour ajuster les styles sur les grands écrans :

```css
@media (min-width: 786px) {
	.form {
		grid-template-columns: auto 1fr auto;
		grid-gap: 1rem;
		align-items: center;
	}

	.input {
		margin-bottom: 0;
	}
}
```

N'oubliez pas que Scrimba est entièrement interactif, donc vous pouvez être aussi créatif que vous le souhaitez avec les styles - ces idées ne sont que quelques possibilités.

## Créez la fonction Search Movies

```js
export default function SearchMovies(){

    const searchMovies = async (e) => {
        e.preventDefault();

        const query = "Jurassic Park";

        const url = `https://api.themoviedb.org/3/search/movie?api_key=5dcf7f28a88be0edc01bbbde06f024ab&language=en-US&query=${query}&page=1&include_adult=false`;

        try {
            const res = await fetch(url);
            const data  = await res.json();
            console.log(data);
        }catch(err){
            console.error(err);
        }
    }
```

Dans [ce screencast](https://scrimba.com/p/pZaznUL/cdVQEGh9?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), nous créons une fonction asynchrone qui utilisera l'API Fetch pour récupérer les informations sur les films à partir de l'API Movie DB. Cliquez sur le lien pour voir comment cela se fait.

## Gérez l'état avec le hook React useState

Dans [ce scrim](https://scrimba.com/p/pZaznUL/c73GVeS4?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), James nous montre comment utiliser l'état pour suivre la requête de l'utilisateur avec le hook `useState` :

```js
const [query, setQuery] = useState("");
```

Ensuite, nous définissons l'`onChange` sur notre `<input>` pour le lier à cet état :

```js
<input
	className="input"
	type="text"
	name="query"
	placeholder="ex. Jurassic Park"
	value={query}
	onChange={(e) => setQuery(e.target.value)}
/>
```

Puis il est temps pour notre deuxième défi - créer l'état pour les informations sur les films et mettre à jour cet état comme il se doit. Rendez-vous sur le tutoriel pour l'essayer.

## Afficher les informations sur les films

[![Application affichant les informations sur les films](https://dev-to-uploads.s3.amazonaws.com/i/wv0o08oujgigzbi3h8jz.png)](https://scrimba.com/p/pZaznUL/cgKVEEf4?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

Maintenant que nous pouvons rechercher nos films, il est temps d'[afficher les informations](https://scrimba.com/p/pZaznUL/cgKVEEf4?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) à l'utilisateur. Cliquez sur le lien ou l'image pour voir comment cela se fait !

## Stylisez les cartes de films

[![Cartes de films stylisées](https://dev-to-uploads.s3.amazonaws.com/i/mspewise511f3ub7eyn9.png)](https://scrimba.com/p/pZaznUL/c9qaG6sD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article)

[Ensuite](https://scrimba.com/p/pZaznUL/c9qaG6sD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article), James nous montre comment styliser nos cartes de films pour créer une application attrayante et conviviale. Nous commençons par notre conteneur de carte `<div>` :

```js
.card {
    padding: 2rem 4rem;
    border-radius: 10px;
    box-shadow: 1px 1px 5px rgba(0,0,0,0.25);
    margin-bottom: 2rem;
    background-color: white;
}
```

Avec cela fait, nous passons à nos titres et images. Cliquez sur le lien ou l'image ci-dessus pour obtenir les détails.

## Créez le composant Movie Card (Défi)

Notre [dernière tâche](https://scrimba.com/p/pZaznUL/cE9N3nsw?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) est de créer un composant séparé pour afficher la carte de film. Cela garantit la maintenabilité si notre projet grandit, et est une bonne habitude à prendre en préparation pour des projets plus importants.

Dans le style vrai de Scrimba, James présente ce défi et nous guide ensuite à travers sa solution. Rendez-vous sur le cast maintenant pour essayer par vous-même. **Note :** Les props sont nécessaires pour cela, mais James donne un rapide comment faire dans l'explication de la tâche.

## Conclusion

Félicitations pour avoir terminé l'application de recherche de films ! Vous savez maintenant comment construire une application entièrement fonctionnelle en utilisant les concepts clés de React, y compris les composants fonctionnels, les hooks, les requêtes fetch, le stylisme et les composants réutilisables.

J'espère que vous avez beaucoup appris de ce cours et que vous vous sentez inspiré pour continuer votre parcours d'apprentissage. Pour en savoir plus sur React, rendez-vous sur le cours gratuit de six heures de Scrimba [Apprendre React gratuitement](https://scrimba.com/course/glearnreact?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article).

Après cela, pourquoi ne pas consulter tous les autres excellents cours disponibles sur [Scrimba](https://scrimba.com/?utm_source=dev.to&utm_medium=referral&utm_campaign=greactmovie_launch_article) pour voir où vous irez ensuite ?

Où que votre parcours vous mène, bon codage :)


%[https://www.youtube.com/watch?v=UKmsNUk7RxM]