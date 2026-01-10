---
title: Apprendre React.js en construisant des projets – Créer une application de rappel
  d'anniversaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-20T21:46:50.000Z'
originalURL: https://freecodecamp.org/news/react-practice-project-birthday-reminder-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/screenzy-1605635100197.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Apprendre React.js en construisant des projets – Créer une application
  de rappel d'anniversaire
seo_desc: "By Mehul Mohan\nWhen you're learning a new skill, video tutorials can only\
  \ take you so far. Many people agree that getting your hands dirty by building a\
  \ project is the way to go. \nSo, in this series of hands-on articles, we'll build\
  \ not one or two, b..."
---

Par Mehul Mohan

Lorsque vous apprenez une nouvelle compétence, les tutoriels vidéo ne peuvent vous mener que jusqu'à un certain point. Beaucoup de gens s'accordent à dire que le fait de mettre la main à la pâte en construisant un projet est la meilleure façon d'apprendre. 

Ainsi, dans cette série d'articles pratiques, nous allons construire non pas un ou deux, mais cinq petites applications React.

Ces applications iront de petites à moyennes et vous devrez construire l'ensemble vous-même. Vous coderez vraiment l'application, passerez les cas de test et vous assurerez d'apprendre chaque compétence.

Prêt à commencer ?

## Comment cela va fonctionner

Cet article est fortement inspiré de la [vidéo de freeCodeCamp ici](https://www.youtube.com/watch?v=a_7Z7C_JCyo). Mais au lieu de simplement regarder la vidéo, vous devrez compléter les projets avec vos propres mains.

Au cours de cette mini-série de blog, vous construirez cinq petits projets. Et pour chaque projet, il y a quelques règles de base :

1. Vous devez coder certains (ou tous) les aspects d'une fonctionnalité
2. Vous devez passer les tests donnés pour les défis
3. Vous pouvez chercher de l'aide externe. Mais je vous recommande de passer d'abord un peu de temps avec l'interface et les instructions. Cela est dû au fait que l'interface est conçue en fonction de la manière dont vous passerez probablement votre temps en tant que développeur dans des outils basés sur le développement.

Juste une note : codedamn lance une instance de serveur pour chaque utilisateur, donc pour utiliser la salle de classe, vous devez vous enregistrer/vous connecter.

Si vous souhaitez simplement consulter le code et travailler sur le projet par vous-même, et non dans la salle de classe, vous pouvez le voir sur GitHub. J'ai lié GitHub dans chaque section ci-dessous afin que vous puissiez accéder à la partie pertinente du code.

Alors commençons avec le premier projet. Si je reçois de bons retours, je continuerai les rédactions et les projets.

## Comment construire une application de rappel d'anniversaire (Projet #1)

Étant donné que c'est notre premier projet, je vais garder la complexité très faible. Dans ce projet, nous allons utiliser React pour rendre une liste d'éléments de données, c'est-à-dire les anniversaires de quelques personnes.

Ces données seront rendues à partir d'une source de données statique et devraient vous aider à comprendre comment importer et utiliser/effacer des données à l'intérieur d'un état. Nous travaillerons à l'intérieur d'une salle de classe que j'ai créée avec mon projet Codedamn. Vous pouvez [commencer cette salle de classe ici](https://codedamn.com/practice/react-birthday-reminder).

Je vous recommande vivement de compléter cette salle de classe et d'autres autant que possible par vous-même. Vous pouvez (et devriez) utiliser cet article de blog comme guide.

Voici ce que vous apprendrez dans cette salle de classe :

1. À quoi ressemble un projet React de base
2. Comment charger des données à partir d'un fichier JS statique
3. Comment utiliser useState pour stocker des données
4. Comment effacer la variable d'état et voir cela reflété dans l'UI

### Lab 1 - Introduction au projet

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-17-at-11.39.47-PM.png)
_Aperçu du lab où vous complétez cette tâche_

[Voici le lien vers ce lab](https://codedamn.com/practice/react-birthday-reminder/9e55078e-70ce-4773-90e3-47798f815323).

Ce premier défi vous présente le projet et sa structure. Passez un peu de temps à localiser tous les éléments pertinents dans celui-ci, et une fois que vous avez terminé, cliquez simplement sur "Exécuter les tests" pour passer ce défi. Rien de compliqué ici :)

### Lab 2 - Comment créer le conteneur de vue d'anniversaire

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-17-at-11.40.43-PM.png)
_Aperçu du lab où vous complétez cette tâche_

[Voici le lien vers ce lab pratique](https://codedamn.com/practice/react-birthday-reminder/b96e0967-f575-4f01-ab4d-31df229bf161).

Vous pouvez également trouver les fichiers de configuration du lab sur GitHub [ici](https://github.com/codedamn-classrooms/react-birthday-project/tree/lab2).

Maintenant que vous avez vu comment la structure du projet et les fichiers sont organisés, il est temps de créer quelques vues statiques. 

N'oubliez pas que vous pouvez toujours créer des supports de données statiques d'abord, puis les remplir avec des données dynamiques plus tard.

C'est une approche très propre pour construire des composants dynamiques, car elle vous permet de préparer le composant avant de le remplir dynamiquement avec des données.

Dans ce lab, vous avez les défis suivants à compléter :

* À l'intérieur de votre fichier App.jsx, créez la hiérarchie HTML suivante :

```
main > section.container > h3 + List
```

* Indice : L'abréviation ci-dessus signifie que votre structure devrait ressembler à ce qui suit :

```html
<main>
	<section class="container">
    	<h3></h3>
        <List />
    </section>
</main>
```

* Votre `h3` devrait contenir le texte :

```
0 anniversaires aujourd'hui
```

* Votre composant `<List />` devrait être le composant `List.jsx` qui est importé en haut.

Pour passer tous les tests, assurez-vous de faire ce qui suit :

* Un élément 'h3' devrait être présent dans votre fichier App.jsx
* Votre balise 'h3' devrait contenir "0 anniversaires aujourd'hui" (sans les guillemets)
* Votre composant 'List' devrait être rendu

Voici la solution à ce défi :

```jsx
import React, { useState } from 'react'
import data from './data'
import List from './List'
function App() {
	// Modifiez votre instruction return ici pour correspondre aux instructions
	return (
		<main>
			<section className="container">
				<h3>0 anniversaires aujourd'hui</h3>
				<List />
			</section>
		</main>
	)
}

export default App

```

### Lab 3 - Comment remplir les données de liste statique

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-17-at-11.41.34-PM.png)
_Aperçu du lab où vous complétez cette tâche_

[Voici le lien vers ce lab](https://codedamn.com/practice/react-birthday-reminder/efb8b149-919b-4a27-a718-a9413a153871).

Vous pouvez également trouver les fichiers de configuration du lab sur GitHub [ici](https://github.com/codedamn-classrooms/react-birthday-project/tree/lab3).

Nous avons l'UI de base à notre disposition. Remplissons maintenant les données statiques à partir du fichier `data.js`. 

Ce fichier a déjà été ouvert pour vous sur le côté droit de l'éditeur. Consultez ce fichier et voyez à quoi ressemblent les données JSON.

Dans ce lab, vous devez faire les choses suivantes :

* À l'intérieur de votre fichier `App.jsx`, vous devez maintenant remplacer `0 Anniversaires Aujourd'hui` par `<nombre d'éléments> Anniversaires Aujourd'hui`. Par conséquent, initialement, il devrait afficher `5 Anniversaires Aujourd'hui`. N'oubliez pas que le `<nombre d'éléments>` provient du nombre d'éléments à l'intérieur de votre variable `data` importée en haut.
* Indice : Vous pouvez utiliser `data.length`
* Passez la variable `data` importée en tant que prop au composant `List`. Cette prop devrait s'appeler `people`
* Indice : `<List people={data} />`
* Dans le composant `List`, utilisez ces données passées pour rendre uniquement les noms des personnes pour l'instant. Vous pouvez `map` sur ces personnes et afficher leurs noms.

Voici 3 tests que vous devez passer :

* Votre App.jsx devrait maintenant afficher "5 Anniversaires Aujourd'hui" où "5" provient de la longueur des éléments importés en haut
* Votre écran devrait afficher les noms de toutes les personnes dans la liste
* Vous devriez utiliser la prop "people" dans le composant List pour passer les données et il devrait afficher les noms

Et voici la solution pour le défi.

Fichier App.jsx :

```jsx
import React, { useState } from 'react'
import data from './data'
import List from './List'
function App() {
	return (
		<main>
			<section className="container">
				{/* Apportez une modification à "0" ici */}
				<h3>{data.length} anniversaires aujourd'hui</h3>
				{/* passez les données au composant list */}
				<List people={data} />
			</section>
		</main>
	)
}

export default App

```

Fichier List.jsx :

```jsx
import React from 'react'

// acceptez les props ici
const List = (props) => {
	const { people } = props
	// Map sur la prop "people" et affichez uniquement les noms de la manière que vous préférez
	return people.map((item) => {
		return <p key={item.id}>{item.name}</p>
	})
}

export default List

```

### Lab 4 - Comment afficher la nouvelle UI

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-17-at-11.42.54-PM.png)

[Voici un lien vers ce lab](https://codedamn.com/practice/react-birthday-reminder/b8513131-b3e6-422c-a4bb-304e3fbc8f74)

Vous pouvez également trouver les fichiers de configuration du lab sur GitHub [ici](https://github.com/codedamn-classrooms/react-birthday-project/tree/lab4).

Maintenant que nous avons les noms des personnes à partir des données statiques, améliorons un peu l'UI. Vous pouvez parcourir tout le CSS dans les fichiers `css` d'abord, puis nous commencerons simplement à utiliser les classes CSS directement.

Dans ce défi, vous devez simplement construire à partir du dernier défi et créer une UI à l'intérieur du composant `List`.

Dans ce lab, vous devez faire les choses suivantes :

* À l'intérieur de votre fichier `List.jsx`, itérez sur la prop `people` et affichez la structure HTML suivante :

```jsx
<article class="person">
	<img src="<image de l'utilisateur>" alt="<nom de l'utilisateur>" />
	<div>
		<h4>NOM_DE_L_UTILISATEUR</h4>
		<p>AGE_DE_L_UTILISATEUR ans</p>
	</div>
</article>
```

* Assurez-vous de remplacer les espaces réservés de manière appropriée. De plus, les classes CSS dans React JSX sont nommées `className`, juste un rappel !

Voici 4 tests que vous devez passer :

* Votre composant List devrait rendre la balise "article" comme parent
* Votre composant List devrait rendre la balise "img" à l'intérieur de la balise "article" avec le src et la balise alt corrects
* Votre composant List devrait rendre le "div > h4" à l'intérieur de la balise "article" avec le nom de la personne
* Votre composant List devrait rendre le "div > p" à l'intérieur de la balise "article" avec l'âge de la personne

Et voici la solution (fichier List.jsx) :

```jsx
import React from 'react'

// acceptez les props ici
const List = (props) => {
	const { people } = props
	// Map sur la prop "people" et codez la bonne structure

	return people.map((person) => {
		const { id, name, age, image } = person
		return (
			<article key={id} className="person">
				<img src={image} alt={name} />
				<div>
					<h4>{name}</h4>
					<p>{age} ans</p>
				</div>
			</article>
		)
	})
}

export default List

```

### Lab 5 - Comment ajouter un bouton Effacer tout

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-17-at-11.44.02-PM.png)

[Voici un lien vers ce lab](https://codedamn.com/practice/react-birthday-reminder/c17707a4-a56e-43ec-ba71-5408a6ccd937)

Vous pouvez également trouver les fichiers de configuration du lab sur GitHub [ici](https://github.com/codedamn-classrooms/react-birthday-project/tree/lab5).

Dans ce dernier lab, ajoutons maintenant un bouton "Effacer" qui effacera les enregistrements et les réinitialisera à 0 anniversaire. Le bouton est déjà disponible pour vous, vous devez simplement vous assurer qu'il fonctionne correctement.

Dans ce lab, vous devez faire les choses suivantes :

* Créez une nouvelle variable d'état appelée `people`
* La valeur initiale de cette variable d'état devrait être les données importées en haut.
* Passez cette variable d'état maintenant dans le composant `List`.
* Lorsque le bouton `Effacer` est pressé, videz la variable d'état afin qu'aucun enregistrement ne soit affiché (Indice : définissez-la sur un tableau vide)

Et voici les tests que vous devez passer :

* Il devrait y avoir un bouton "Effacer tout" à l'écran (déjà fait pour vous)
* Initialement, tous les enregistrements devraient être visibles
* Lorsque le bouton "Effacer tout" est pressé, il devrait supprimer tous les enregistrements de l'écran

Voici le fichier de solution `App.jsx` pour ce lab :

```jsx
import React, { useState } from 'react'
import data from './data'
import List from './List'
function App() {
	// créez une variable d'état ici
	const [people, setPeople] = useState(data)

	// cela devrait effacer tous les enregistrements
	function clearAllRecords() {
		setPeople([])
	}
	return (
		<main>
			<section className="container">
				<h3>{people.length} anniversaires aujourd'hui</h3>
				<List people={people} />
				<button onClick={clearAllRecords}>Effacer tout</button>
			</section>
		</main>
	)
}

export default App
```

Et vous avez terminé ! Félicitations pour avoir complété un petit projet en React. Continuez comme ça :)

## Conclusion

J'espère que vous avez apprécié cette salle de classe codedamn. Vous pouvez en trouver beaucoup d'autres dans le [parcours d'apprentissage React Mastery](https://codedamn.com/learning-paths/react-mastery) sur codedamn. 

Il reste encore beaucoup de lacunes à combler, mais il y a de bonnes chances que cela vous lance assez facilement si vous êtes nouveau. 

Assurez-vous de me dire comment s'est passée votre expérience sur mon [compte Twitter](https://twitter.com/mehulmpt), car cela m'aidera à structurer les prochaines salles de classe pratiques.