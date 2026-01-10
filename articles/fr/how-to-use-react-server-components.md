---
title: React Server Components – Comment et pourquoi les utiliser dans votre code
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2023-08-01T14:52:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-server-components
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/React-Server-Components-2.png
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: React Server Components – Comment et pourquoi les utiliser dans votre code
seo_desc: 'In late 2020, the React team introduced the "Zero-Bundle-Size React Server
  Components" concept. Since then, the React developer community has been experimenting
  with and learning how to apply this forward-looking approach.

  React has changed how we th...'
---

Fin 2020, l'équipe React a introduit le concept des "React Server Components à taille de bundle nulle". Depuis, la communauté des développeurs React expérimente et apprend à appliquer cette approche visionnaire.

React a changé notre façon de concevoir les interfaces utilisateur. Et le nouveau modèle utilisant les React Server Components est bien plus structuré, pratique et maintenable, et offre une meilleure expérience utilisateur.

La dernière version de `Next.js` a adopté l'approche "Penser en Server Components". Et en tant que développeurs React, nous devons nous adapter à ce nouveau modèle mental pour exploiter pleinement sa puissance dans la construction d'applications.

Dans ce tutoriel, vous apprendrez tout sur les React Server Components (RSC). Vous découvrirez exactement ce qu'ils sont et comment ils fonctionnent, et surtout, quel problème ils résolvent.

Je vous montrerai également de nombreux exemples pour que vous compreniez pourquoi nous avons besoin des RSC. Enfin, vous apprendrez la différence entre `React Server Components` et une autre fonctionnalité au nom similaire mais différente appelée `Server Side Rendering (SSR)`.

Si vous êtes nouveau dans React, vous devrez avoir quelques connaissances de base sur l'architecture des composants, l'état, le passage de données via les props, et l'arbre DOM virtuel avant d'apprendre les React Server Components.

Vous pouvez également lire cet article puis [suivre cette feuille de route complète](https://www.freecodecamp.org/news/react-fundamentals-for-beginners/) sur freeCodeCamp pour solidifier vos bases avec ReactJS.

Tout est prêt ? Commençons.

Si vous aimez apprendre via du contenu vidéo, cet article est également disponible sous forme de tutoriel vidéo ici : 👂

%[https://www.youtube.com/watch?v=5DZvdoMogys]

## React en tant que bibliothèque UI côté client

Depuis sa création, React est une bibliothèque d'interface utilisateur côté client. C'est une bibliothèque open source basée sur JavaScript qui aide les développeurs web et mobiles à construire des applications utilisant une architecture basée sur les composants.

La philosophie de React suggère que nous divisons toute notre conception en morceaux plus petits et autonomes appelés `composants`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-169.png)
_Image montrant un composant divisé en plusieurs composants._

Les composants peuvent alors avoir leurs propres données privées appelées `état` et un moyen de transmettre des données à d'autres composants appelé `props`. Vous divisez ces composants en une hiérarchie de composants, définissez l'état, gérez les effets qui changent l'état, et décidez du flux de données.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-170.png)
_Image montrant comment fonctionnent l'état et les props._

Traditionnellement, tous ces composants sont des fonctions JavaScript (nous ne parlons ici que des composants fonctionnels – nous laisserons les composants de classe dans le passé). Lorsque l'application se charge dans le navigateur, nous téléchargeons le code des composants et rendons l'application fonctionnelle en les utilisant.

Nous utiliserons le terme composants ici. Mais, puisque cet article vous introduit au concept des React Server Components, appelons ces composants traditionnels `Client Components` (car ils sont téléchargés sur le client/navigateur et React effectue sa magie pour les rendre).

## Problèmes courants avec les applications React

Les React Client Components sont excellents et fonctionnent bien pour résoudre certains cas d'utilisation. Mais nous devons examiner le modèle un peu différemment lors de la construction d'applications React. Cela est dû au fait que nous devons nous soucier de :

* `Expérience utilisateur` : Nous construisons des produits logiciels pour nos utilisateurs et clients. L'expérience utilisateur de l'application compte si nous voulons que l'application soit réussie.
* `Maintenabilité` : Le code du projet doit être bien maintenu au fil des années, à travers plusieurs équipes de développement.
* `Coût de performance` : L'application ne doit pas être lente et notre approche de conception ne doit pas ralentir les choses.

Examinons maintenant quelques exemples de problèmes courants que vous pourriez rencontrer. Nous comprendrons également comment nous pouvons implémenter et concevoir pour chacun de ces points clés dans notre développement web quotidien en utilisant React.

### Le problème de décalage de mise en page

Un problème très courant d'expérience utilisateur est le décalage soudain de la mise en page lorsqu'un composant est rendu. Examinons l'extrait de code ci-dessous :

```html
<CourseWraper>
 <CourseList />
 <Testimonials />   
</CourseWraper>
```

Il s'agit d'un code JSX familier où nous avons un composant `CourseWrapper` et deux composants enfants, `CourseList` et `Testimonials`. Supposons que `CourseList` et `Testimonials` effectuent tous deux des appels réseau (appels API) pour récupérer les données.

Voici le composant `CourseList` :

```jsx
function CourseList() {

	// Supposons un appel réseau, dans la vraie vie
    // vous le gérerez avec useEffect
    const info = fetchCourseList();
    
    return(
      <> </>
    )
}
```

Et le composant `Testimonial` :

```jsx
function Testimonials() {

	// Supposons un appel réseau, dans la vraie vie
    // vous le gérerez avec useEffect
    const info = fetchTestimonials();
    
    return(
      <> </>
    )
}
```

Comme ces composants effectuent des appels réseau, il n'y a aucune garantie sur la séquence dans laquelle les réponses peuvent revenir. Cela dépend de la vitesse du réseau, de la latence et de nombreux autres facteurs.

Dans une situation où l'appel réseau pour le composant `Testimonials` se termine avant celui du composant `CourseList`, le composant `Testimonials` sera rendu en premier, puis le composant `CourseList` sera rendu. Il repoussera le composant `Testimonials` pour s'adapter. Vous pouvez voir ce que je veux dire ici :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/layoutshift-1.gif)
_Une représentation au ralenti du problème de décalage de mise en page UX._

Nous pouvons améliorer un peu l'expérience en utilisant un indicateur de chargement ou un effet de scintillement indiquant à nos utilisateurs de s'attendre à quelque chose dans un moment (mais nous ne sommes pas sûrs de quand).

### Le problème de la cascade réseau

Discutons d'un autre problème typique d'expérience utilisateur. Imaginez un composant React similaire à celui que nous avions dans le dernier exemple :

```jsx
function Course() {
 return(
     <CourseWraper>
 		<CourseList />
 		<Testimonials />   
	 </CourseWraper>
 )
}
```

Apportons une petite modification ici. En plus des composants `CourseList` et `Testimonials`, maintenant `CourseWrapper` effectue également un appel réseau.

```jsx
function CourseWrapper() {

    // Supposons un appel réseau, dans la vraie vie
    // vous le gérerez avec useEffect
    const info = fetchWrapperInfo();
    
    return(
      <> </>
    )
}
```

Ainsi, le composant parent effectue un appel réseau pour récupérer des données et ses deux composants enfants effectuent également des appels réseau.

Maintenant, la chose intéressante est que le composant parent ne se rendra pas tant que son appel réseau n'est pas terminé. Il retarde également le rendu de ses composants enfants.

Ce phénomène où nous attendons la réponse de la chose précédente pour commencer la chose actuelle est connu sous le nom de `Waterfall`. Dans ce cas, nous avons à la fois des problèmes de cascade réseau et de rendu de composants.

Maintenant, vous pourriez penser à supprimer tous ces appels réseau de chaque composant et les regrouper en un seul appel afin que les composants individuels n'attendent pas la réponse. C'est une bonne idée, mais cela peut causer un problème de maintenabilité. Apprenons-en davantage à ce sujet dans la section suivante.

### Problèmes de maintenabilité

Maintenant que nous avons examiné quelques problèmes d'expérience utilisateur liés aux interactions côté serveur, considérons un problème de maintenabilité.

Supposons maintenant qu'aucun de nos composants ne fasse d'appels réseau. Nous récupérons tous les détails pour tous les composants (oui, y compris le composant parent) en une seule fois en utilisant un seul appel API `fetchAllDetails()`.

Après cela, nous passons les informations requises à chacun des composants en tant que props. C'est mieux que le problème de "Waterfall" que nous avons vu ci-dessus, n'est-ce pas ?

```jsx
function Course() {
	
	// Supposons un appel réseau, dans la vraie vie
    // vous le gérerez avec useEffect    
    const info = fetchAllDetails();
    
    return(
    	<CourseWrapper
        	ino={info.wrapperInfo} >
            <CourseList
        		ino={info.listInfo} />
            <Testimonials
        		ino={info.testimonials} />
        </CourseWrapper>     
    )
 }
```

Mais cela pourrait causer quelques problèmes de maintenabilité.

Supposons qu'un beau jour, le produit décide de supprimer la fonctionnalité Testimonials. Nous pouvons donc simplement supprimer le composant Testimonials du code ci-dessus. Cela fonctionne ! Mais nous pourrions oublier de nettoyer les données que nous obtenons en utilisant l'appel `fetchAllDetails()`. Elles pourraient être là inutilement sans être utilisées.

Pour atténuer cela, vous pourriez finir par modifier votre code de manière que nous avons déjà discutée dans les sections précédentes en expliquant les problèmes d'expérience utilisateur possibles. Nous devons donc trouver une meilleure solution. Mais avant cela, parlons d'une autre considération, le `Coût de performance`.

### Coûts de performance

La dernière zone problématique que nous allons discuter est celle des coûts de performance.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-171.png)
_J'ai trouvé ce mème drôle sur Internet - Il représente la lourdeur que JS apporte aux clients._

Traditionnellement, les composants React sont des fonctions JavaScript côté client. Ils sont les blocs de construction de votre application React. Lorsque nous chargeons l'application sur le client, les composants sont téléchargés sur le client et React effectue ce qui est nécessaire pour les rendre pour vous.

Mais cela pose deux problèmes significatifs :

Premièrement, lorsque l'utilisateur envoie la demande, l'application télécharge le HTML ainsi que le JavaScript lié, le CSS et d'autres actifs comme les images.

Sur le site client (dans le navigateur), React commence sa magie et hydrate la structure HTML. Il analyse le HTML, attache les écouteurs d'événements au DOM et récupère les données du magasin. Ainsi, le site devient une application React pleinement opérationnelle.

Mais le point est qu'il se passe beaucoup de choses sur le client. Nous finissons par télécharger tout ce code sur le client.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-182.png)
_Quantité de scripts téléchargés sur le navigateur_

Le plus souvent, nous avons besoin de bibliothèques externes (modules Node) comme dépendances pour notre projet. Toutes ces dépendances seront téléchargées côté client, le rendant encore plus volumineux.

Maintenant que vous comprenez les problèmes, je pense que vous apprécierez définitivement ce que les `React Server Components` offrent et comment ils peuvent résoudre ces problèmes.

Mais avant d'en parler, comprenons un peu mieux le client et le serveur.

## Le modèle Client-Serveur

Nous avons utilisé les termes client et serveur à plusieurs reprises dans cet article. Donnons donc une définition formelle de ceux-ci et expliquons leur relation à un niveau élevé.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-175.png)
_Diagramme montrant la relation entre le client et le serveur_

* `Client` : Un client par rapport à une application est un système qui exécute les tâches du côté de l'utilisateur final. Des exemples de clients sont votre PC, ordinateur portable, mobile, navigateur, etc.
* `Serveur` : Un serveur, comme son nom l'indique, fournit des services aux clients. Il peut être colocalisé avec un magasin de données ou une base de données pour un accès rapide aux données.
* `Requête` : Une requête est un mode de communication qu'un client utilise pour demander un service à un serveur.
* `Réponse` : Une réponse est également un mode de communication qu'un serveur utilise pour renvoyer le service (données/informations) au client.

## React Client Components

Comme je l'ai mentionné ci-dessus, traditionnellement, les composants React vivent du côté client. Lorsqu'ils interagissent avec un serveur, ils envoient une requête et attendent que la réponse revienne. À la réception d'une réponse, le client déclenche le prochain ensemble d'actions.

Si le service demandé se termine avec succès, le composant client agit sur l'UI en conséquence et affiche un message de succès. En cas d'erreur, le composant client signale cela aux utilisateurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-176.png)
_React Client Components - dans un modèle Client Serveur._

Lorsque cela provoque une cascade réseau, la réponse du composant client est retardée et provoque une mauvaise expérience utilisateur. Alors, comment pouvons-nous atténuer cela ?

## Comment les React Server Components (RSCs) aident

Et si nous déplacions nos composants React vers le serveur ? Et peut-être les colocaliser avec le magasin de données... mais est-ce même possible ?

Oui ! Découvrons maintenant les `React Server Components`. Ces nouveaux composants peuvent récupérer des données plus rapidement car ils sont sur le serveur. Ils ont accès à votre infrastructure serveur comme les systèmes de fichiers et le magasin de données sans effectuer d'allers-retours sur le réseau.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-177.png)
_React Server Components - Dans un modèle Client Serveur_

C'est un changement complet de paradigme pour les développeurs React, car nous devons maintenant penser en termes de composants serveur.

Avec les RSCs, vous pouvez déplacer votre logique de récupération de données vers le serveur (de sorte que votre composant récupère les données sans appel réseau) et les préparer sur le serveur lui-même. Les données qui reviennent au client sont un composant bien construit avec toutes les données qui y sont intégrées. N'est-ce pas génial ?

Cela signifie qu'en utilisant les composants serveur React, vous pouvez écrire du code comme ceci :

```jsx
import { dbConnect } from '@/services/mongo'

import { addCourseToDB } from './actions/add-course'

import CourseList from './components/CourseList'

export default async function Home() {

  // Obtenir une connexion MongoDB
  await dbConnect();
  
  // Obtenir tous les cours de la base de données en utilisant le modèle
  const allCourses = await courses.find();
  
  // Cela s'affiche sur la console du serveur
  console.log({allCourses})

  return (
    <main>
      <div>
        <CourseList allCourses={allCourses} />  
      </div>
    </main>
  )
}
```

Regardez ça ! Vous pouvez repérer certains des changements immédiatement :

* Le composant est de type `async` car il gérera des appels asynchrones.
* Nous nous connectons à la base de données (MongoDB) depuis le composant lui-même. Wow ! Habituellement, nous voyons ce type de code avec `Node.js` ou `Express`, n'est-ce pas ?
* Ensuite, nous interrogeons la base de données et récupérons les données à passer à notre JSX pour le rendu.

Remarquez que le log de la console affichera les informations sur la console du serveur, et non sur la console de votre navigateur.

De plus, nous nous sommes débarrassés de la gestion d'état (useState) et de la gestion des effets (useEffect) complètement. C'est propre et simple.

Avec les composants serveur React, vous n'aurez peut-être plus jamais besoin d'utiliser useEffect.

### Limites des React Server Components

Avec tous ces avantages, les RSCs ont également quelques limites que vous devez garder à l'esprit :

* Les RSCs restent sur le serveur et sont rendus sur le serveur. Ils n'ont rien qui soit lié au côté client. Cela signifie que vous ne pouvez pas ajouter d'interactivité utilisateur aux composants serveur. Par exemple, vous ne pouvez pas utiliser de gestionnaires d'événements ou de hooks React comme useState, useReducer, useEffect dans vos composants serveur.
* Vous ne pouvez pas utiliser les API Web du navigateur comme localstorage, bluetooth, web USB, etc. dans les composants serveur.
* Pour tout ce qui est lié aux interactions client, vous devez continuer à utiliser les composants client.

Cela a du sens ? Alors, comment pouvez-vous organiser au mieux vos composants pour votre application ?

### Comment utiliser les composants Client et Serveur ensemble

Votre application peut être une combinaison de composants serveur et client. Vous verrez bientôt un exemple, mais comprenons d'abord le concept.

Les composants serveur peuvent importer et rendre des composants client, mais les composants client ne peuvent pas rendre les composants serveur. Si vous souhaitez utiliser un composant serveur dans un composant client, vous pouvez le passer en tant que props et l'utiliser de cette manière.

Il est préférable d'avoir les composants serveur à la racine de votre hiérarchie de composants et de pousser les composants client vers les feuilles de l'arbre de composants.

La récupération des données peut se faire en haut dans les composants serveur et vous pouvez les passer comme React le permet. Les interactions utilisateur (gestionnaires d'événements) et l'accès aux API du navigateur peuvent être gérés dans le composant client au niveau des feuilles.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-186.png)
_Un arbre de composants avec des composants Serveur et Client_

### Attendez, les RSCs ne sont-ils pas les mêmes que le Server Side Rendering (SSR) ?

Non, ils ne le sont pas. Les RSC et SSR ont le mot "serveur" dans leurs noms et la similarité s'arrête là.

Avec le Server Side Rendering, nous envoyons le HTML brut du serveur au client, puis tout le JavaScript côté client est téléchargé. React commence le processus d'hydratation pour transformer le HTML en un composant React interactif. Dans le SSR, le composant ne reste pas sur le serveur.

Nous savons maintenant que, avec les React Server Components, les composants restent sur le serveur et ont accès à l'infrastructure du serveur sans effectuer d'allers-retours réseau.

Le SSR est utile pour un chargement plus rapide de la page initiale de votre application. Vous pouvez utiliser le SSR et les RSCs ensemble dans votre application sans aucun problème.

## Comment construire une page de liste de cours en utilisant Next.js (avec React Server Components) et MongoDB

Construisons maintenant une application qui utilise les React Server Components. Next.js est le principal framework web qui a adopté les RSCs dans sa dernière version.

Nous allons donc construire une page de liste de cours pour montrer comment nous pouvons créer des composants serveur dans Next.js et en quoi cela diffère des composants client.

Notez que vous n'apprendrez pas Next.js ou MongoDB en profondeur ici. Nous utilisons simplement cette application comme exemple pour vous enseigner comment fonctionnent les React Server Components et en quoi ils diffèrent des composants client.

Tout d'abord, ajoutons les données des cours dans un magasin de données. Pour cette application, j'ai utilisé MongoDB. L'image ci-dessous montre que trois documents ont été ajoutés pour trois cours.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-178.png)
_Mongo Compass - collection de cours_

Ensuite, nous créerons une fonction utilitaire pour établir une connexion à MongoDB. Il s'agit d'un code générique que vous pouvez utiliser pour tout projet basé sur JavaScript pour vous connecter à MongoDB en utilisant Mongoose et l'URI MongoDB.

```js
import mongoose from "mongoose";

export async function dbConnect(): Promise<any> {
  try {
    const conn = await mongoose.connect(String(process.env.MONGO_DB_URI));
    console.log(`Database connected : ${conn.connection.host}`);
    return conn;
  } catch (err) {
    console.error(err);
  }
}
```

Maintenant, nous devons créer le modèle qui correspond au document dans MongoDB. Comme nous traitons des données de cours, voici le modèle correspondant :

```js
import mongoose, { Schema } from "mongoose";

const schema = new Schema({
  name: {
      required: true,
      type: String
  },
  description: {
      required: true,
      type: String
  },
  cover: {
    required: true,
    type: String
  },
  rating: {
    required: true,
    type: Number
  },
  price: {
    required: true,
    type: Number
  },
  createdOn: {
    type: { type: Date, default: Date.now }
  },
  link: {
    required: true,
    type: String
  },
  type: {
    required: true,
    type: String
  },
  comments: {
    required: false,
    type: [{ body: String, date: Date }]
  }
});

export const courses = mongoose.models.course ?? mongoose.model("course", schema);
```

Maintenant, la magie commence ! Avec le routeur d'applications Next.js, tous les composants sont par défaut des composants serveur. Cela signifie qu'ils sont situés près du serveur et ont accès à votre écosystème serveur.

Le code ci-dessous est un composant Next.js régulier mais avec une fonctionnalité spéciale : nous pouvons obtenir directement une connexion à la base de données dans le composant et interroger les données directement sans passer par une gestion d'état et d'effets. Cool, non ?

Tout ce que vous loggez depuis ce composant ne sera jamais loggé dans la console de votre navigateur car il s'agit d'un composant serveur. Vous pouvez voir le log dans la console de votre serveur (peut-être un terminal où vous avez démarré le serveur en utilisant la commande `yarn dev`).

Comme l'interaction avec la base de données est asynchrone, nous utilisons le mot-clé `await` lors des appels et utilisons le mot-clé `async` pour le composant. À la réception de la réponse, nous la passons en tant que prop aux composants enfants.

```jsx

import { dbConnect } from '@/services/mongo'
import { courses } from '@/models/courseModel'
import { addCourseToDB } from './actions/add-course'

import AddCourse from './components/AddCourse'
import CourseList from './components/CourseList'

export default async function Home() {

  // Obtenir une connexion MongoDB
  await dbConnect();
  
  // Obtenir tous les cours de la base de données en utilisant le modèle
  const allCourses = await courses.find().select(
  						["name", "cover", "rating"]);
  
  // Cela s'affiche sur la console du serveur
  console.log({allCourses})

  return (
    <main>
      <div>
        <h1>Courses</h1> 
        <AddCourse addCourseToDB={addCourseToDB} />
        <CourseList allCourses={allCourses} />  
      </div>
    </main>
  )
}

```

Le composant Home contient :

* Un titre
* Un composant (AddCourse) qui enveloppe un bouton pour ajouter un cours
* Un composant (CourseList) pour afficher les cours sous forme de liste.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-25-at-9.58.57-AM.png)
_La page de liste des cours_

Nous savons qu'un composant serveur peut rendre à la fois des composants client et serveur. Le composant `AddCourse` nécessite une interaction utilisateur, car les utilisateurs doivent cliquer sur un bouton pour ajouter un cours. Il ne peut donc pas s'agir d'un composant serveur (rappellez-vous les limitations des composants serveur que vous avez lues ci-dessus) !

Créons donc un composant client pour `AddCourse`. Avec le routeur d'applications Next.js, tous les composants sont des composants serveur par défaut. Si vous souhaitez créer un composant client, vous devez explicitement en créer un en utilisant la directive appelée `'use client'` en haut du composant (même avant toute instruction d'importation).

```js
'use client'

import { useState } from 'react';
import Modal from './Modal';
import AddCourseForm from "./AddCourseForm";

export default function AddCourse({
  addCourseToDB,
}: {
  addCourseToDB: (data: any) => Promise<void>
}) {
  const [showAddModal, setShowAddModal] = useState(false);
  const add = async(data: any) => {
    await addCourseToDB(data);
    setShowAddModal(false);
  }

  return (
    <>
    <button
      onClick={() => setShowAddModal(true)}
    >
      Add Course
    </button>
    <Modal 
      shouldShow={showAddModal} 
      body={
        <AddCourseForm 
          saveAction={add} 
          cancelAction={() => setShowAddModal(false)} />} />
    </>
  )
}
```

Le composant `CourseList` n'a pas besoin de gestionnaires d'événements, nous pouvons donc le garder en tant que composant serveur.

```js

import Image from 'next/image'
import Link from 'next/link'

export default function CourseList(courseList: any) {
  const allCourses = courseList.allCourses;
  return(
    <div>
      {
        allCourses.map((course: any) =>
        <Link key={course['_id']} href={`/courses/${course['_id']}`}>
          <div>
            <Image
              src={course.cover}
              width={200}
              height={200}
              alt={course.name}
            />
            <h2>{course.name}</h2>
            <p>{course.rating}</p>
          </div> 
        </Link> 
      )}
    </div>  
  )

}
```

Remarquez également l'onglet `Sources` des outils de développement du navigateur pour identifier ce qui est téléchargé sur le client et ce qui reste sur le serveur. Voyez-vous le fichier `page.tsx` ou `CourseList.tsx` ici ? Non. Parce que ce sont des composants serveur et ils ne font jamais partie de vos bundles client.

Nous ne voyons que les composants que nous avons explicitement marqués comme composants client dans notre application.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-179.png)
_Inspection du bundle client_

J'espère que ce flux d'application vous a montré comment toute la théorie se connecte à la pratique. Vous devriez maintenant comprendre comment utiliser les composants serveur dans vos applications React.

## En résumé

Pour résumer,

* Les React Server Components ont accès au backend sans aucun aller-retour réseau.
* Nous pouvons éviter les cascades réseau en utilisant les React Server Components.
* Les React Server Components supportent le fractionnement automatique du code et améliorent les performances de votre application avec une taille de bundle nulle.
* Comme ces composants sont du côté serveur, ils n'ont pas accès aux gestionnaires d'événements côté client, à l'état et aux effets. Cela signifie que vous ne pouvez pas utiliser de gestionnaires d'événements, ou de hooks React comme useState, useReducer et useEffect.
* Un React Server Component peut importer et rendre un composant client mais l'inverse n'est pas vrai. Mais vous pouvez passer un composant serveur en tant que props à un composant client.

## **Avant de terminer...**

C'est tout pour l'instant. J'espère que vous avez trouvé cet article informatif et perspicace.

Restez en contact.

* Je suis un éducateur sur ma chaîne YouTube, `tapaScript`. Veuillez vous [ABONNER](https://www.youtube.com/tapasadhikary?sub_confirmation=1) à la chaîne si vous souhaitez apprendre JavaScript, ReactJS, Node.js, Git, et tout sur le développement web de manière fondamentale.
* [Suivez-moi sur Twitter](https://twitter.com/tapasadhikary) ou [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils en développement web et en programmation.
* Consultez mes travaux Open Source sur [GitHub](https://github.com/atapas).

À bientôt avec mon prochain article. En attendant, prenez soin de vous et restez heureux.