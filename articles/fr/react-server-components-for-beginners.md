---
title: Comment utiliser les composants serveur React – Un guide pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-19T20:31:21.000Z'
originalURL: https://freecodecamp.org/news/react-server-components-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-panumas-nikhomkhai-1148820--2-.jpg
tags:
- name: React
  slug: react
seo_title: Comment utiliser les composants serveur React – Un guide pour débutants
seo_desc: 'By Adwaith KS

  React Server Components have been generating significant buzz and excitement lately.
  They''ve recently been adopted as the default option in Next.js 13, so now more
  and more developers are using them.

  React Server Components seamlessly b...'
---

Par Adwaith KS

Les composants serveur React ont suscité beaucoup d'excitation ces derniers temps. Ils ont récemment été adoptés comme option par défaut dans Next.js 13, donc de plus en plus de développeurs les utilisent.

Les composants serveur React combinent parfaitement le rendu côté serveur avec l'interactivité de JavaScript côté client. Et dans ce tutoriel, vous apprendrez tout sur ce que sont les composants serveur React, les problèmes qu'ils résolvent et les capacités puissantes qu'ils offrent.

## **Pourquoi les composants serveur ?**

Commençons par un exemple :

```jsx
const App = () => {
    return (
        <Wrapper>
            <ComponentA />
            <ComponentB />
        </Wrapper>
    )
}
```

Nous avons deux composants **ComponentA** et **ComponentB** qui sont passés en tant que props enfants à un composant **Wrapper**. Le corps de chaque composant ressemble à ceci :

```jsx
const Wrapper = ({children}) => {
  
  const [wrapperData, setWrapperData] = useState({});
  
  useEffect(() => {
    // Appel API pour obtenir les données nécessaires au fonctionnement du composant Wrapper
    getWrapperData().then(res => {
      setWrapperData(res.data);
    });
  }, []);
  
  // Ce n'est qu'après avoir reçu la réponse de l'API que nous commençons le rendu
  // des composants ComponentA et ComponentB (props enfants)
  return (
  	<>
      <h1>{wrapperData.name}</h1>
      <>
        {wrapperData.name && children}
      </>
    </>
  )
}

/*-------------------------------------------------- */

const ComponentA = () => {
  const [componentAData, setComponentAData] = useState({});
  
  useEffect(() => {
    getComponentAData().then(res => {
      setComponentAData(res.data);
    });
  }, []);
  
  return (
  	<>
      <h1>{componentAData.name}</h1>
    </>
  )
}

/*-------------------------------------------------- */

const ComponentB = () => {
  const [componentBData, setComponentBData] = useState({});
  
  useEffect(() => {
    getComponentBData().then(res => {
      setComponentBData(res.data);
    });
  }, []);
  
  return (
  	<>
      <h1>{componentBData.name}</h1>
    </>
  )
}
```

Chaque composant est responsable de la récupération de ses propres données (comme vous pouvez le voir dans le code ci-dessus). Ainsi, aucun composant ne gère des données qui ne sont pas nécessaires à son propre fonctionnement. Parfait, n'est-ce pas ? Eh bien, pas encore.

Supposons que le temps nécessaire pour obtenir la réponse aux appels API déclenchés par chaque composant soit le suivant :

* `**<Wrapper />** prend 1 seconde pour obtenir la réponse`
* `**<ComponentB />** prend 2 secondes pour obtenir la réponse`
* `**<ComponentA />** prend 3 secondes pour obtenir la réponse`

Voyez-vous un problème ici ?

1. **Wrapper** est visible pour l'utilisateur après 1 seconde.
2. Ensuite, **ComponentB** apparaît après 2 secondes.
3. Après 3 secondes, **ComponentA** apparaît. Mais ComponentA entre dans la vue en poussant **ComponentB** vers le bas. Comme si ComponentA venait de surgir de nulle part. Ce n'est pas une grande expérience utilisateur.

Un autre problème est que les composants enfants (ComponentA et ComponentB) ne sont même pas rendus tant que le composant **Wrapper** n'a pas reçu la réponse de l'appel API qu'il a effectué (référez-vous à l'image 2), ce qui entraîne un effet de cascade. La récupération séquentielle des données introduit toujours des cascades.

Le terme "cascade" fait généralement référence à l'exécution séquentielle de plusieurs requêtes de récupération. Cela signifie que les requêtes de récupération suivantes ne sont initiées qu'après que la requête de récupération précédente a été résolue ou complétée.

Dans notre exemple, ce n'est qu'après avoir obtenu la réponse à l'appel API dans le composant Wrapper que les deux autres composants sont rendus.

Comment pouvons-nous résoudre ce problème ? Eh bien, nous pouvons faire une seule récupération pour obtenir toutes les données dans le composant **App**, puis passer les données nécessaires à chaque composant. Quelque chose comme ceci :

```jsx
const App = () => {
    
    const data = fetchAllStuffs();
    
    return (
        <Wrapper data={data.wrapperData}>
            <ComponentA data={data.componentAData} />
            <ComponentB data={data.componentBData} />
        </Wrapper>
    )
}
```

Il n'y a rien de mal avec cette approche. Mais la réponse de l'API est très couplée à nos composants.

Par exemple, si nous supprimons **ComponentA** à l'avenir, nous voulons également supprimer **componentAData** de la réponse de l'API, puisque nous ne voulons pas gérer des données non utilisées par le composant. Après tout, s'il n'y a pas de ComponentA, alors il n'y a pas besoin de ComponentAData.

## **La solution est les composants serveur**

Le problème ci-dessus est ce que les composants serveur adressent principalement. Pour résumer le problème : les composants font des appels API au serveur depuis le client, et nous attendons que la réponse arrive pour rendre d'autres composants. Lorsque nous avons une récupération séquentielle de données en cours sur le client, cela va créer des cascades (comme mentionné précédemment).

Et si nous déplacions ces composants vers le serveur ? Oui, vous avez bien entendu !

Imaginez simplement que les composants sont sur le serveur. La récupération des données prend-elle le même temps que lorsque les composants étaient côté client ? Non, ce n'est pas le cas.

La récupération des données est beaucoup plus rapide lorsque les composants sont sur le serveur. Eh bien, avez-vous vraiment besoin de récupérer les données maintenant ? Pas vraiment ! Puisque maintenant vos composants sont rendus sur le serveur, vos composants ont accès à l'infrastructure du serveur. Cela signifie que vous pouvez interroger la base de données à partir de vos composants également.

Trop d'informations ? Décomposons un peu.

Pour simplifier, mettons les choses ainsi. Déplacez votre récupération de données vers le serveur. Toute récupération de données effectuée avec l'aide du serveur est beaucoup plus rapide.

Pourquoi ? Parce que vous ne récupérez plus les données depuis le client, donc une latence faible. Vous récupérez les données directement depuis le serveur maintenant.

Eh bien, c'est génial – mais il y a un piège. Vous rendez des composants sur le serveur. Pourrez-vous utiliser des hooks (par exemple, useState, useEffect, et autres), des API Web (comme localStorage), ou des gestionnaires d'événements (comme onClick) comme vous le feriez dans un composant React normal ? Non, vous ne pourrez pas.

C'est parce que les composants serveur sont rendus sur le serveur. Ils sont donc bien adaptés aux situations où les mises à jour en temps réel ou les interactions utilisateur ne sont pas essentielles.

Voici un aperçu de ce à quoi ressemble un composant serveur :

```jsx
// Note.js - Composant Serveur

import NoteEditor from 'NoteEditor';

async function Note(props) {
  const { note } = props;
  
  return (
    <div>
      <h1>{note.title}</h1>
      <section>{note.body}</section>
    </div>
  );
}
```

Cela ressemble à un composant React régulier, n'est-ce pas ? Oui. La différence entre un composant React régulier (également appelé composant client à partir de maintenant) et un composant serveur réside dans leur environnement de rendu et les capacités qu'ils ont tous les deux. Plus d'informations à ce sujet ci-dessous.

## **Ce qu'il faut faire et ne pas faire avec les composants serveur**

Voici une liste de choses que vous pouvez faire et ne pas faire avec les composants serveur. Même si les composants serveur peuvent sembler sophistiqués, cela ne signifie pas que nous pouvons les utiliser partout.

### **Ce que vous pouvez faire**

* Utiliser `async/await` avec des sources de données côté serveur telles que les bases de données, les services internes, les systèmes de fichiers, etc.
* Rendre d'autres composants serveur, des éléments natifs comme div, span, etc. ou des composants client (composants React normaux).

### **Ce que vous ne pouvez pas faire**

* Ne peut pas utiliser les hooks fournis par React comme useState, useReducer, useEffect, etc., car les composants serveur sont rendus sur le serveur.
* Ne peut pas utiliser les API du navigateur comme Local Storage, etc. (Vous pouvez les polyfill sur le serveur, cependant).
* Ne peut pas utiliser de fonctions utilitaires qui dépendent des API spécifiques au navigateur (par exemple : Local Storage) ou des hooks personnalisés qui dépendent de l'état ou des effets.

## **Composants serveur vs composants client**

Vous vous demandez peut-être ce qu'est un composant client maintenant ? Eh bien, ce sont les composants React que vous avez écrits toutes ces années. Oui, la manière régulière d'écrire React.

Comme leur nom l'indique, ils sont rendus côté client, c'est-à-dire dans le navigateur. Juste une note que tout le code React que vous écriviez avant l'existence des composants serveur était rendu côté client (navigateur). Donc pour les différencier des composants serveur qui sont rendus sur le serveur, à partir de maintenant nous appellerons les composants React réguliers (où vous utilisez des états, des effets, des API spécifiques au navigateur) "Composants Client".

Tout d'abord, regardons un exemple de composant serveur :

```jsx
// Note.js - Composant Serveur

import db from 'db'; 
// (A1) Nous importons depuis NoteEditor.js - un composant client.
import NoteEditor from 'NoteEditor';

async function Note(props) {
  const {id, isEditing} = props;
  // (B) Peut accéder directement aux sources de données du serveur pendant le rendu, par exemple les bases de données
  const note = await db.posts.get(id);
  
  return (
    <div>
      <h1>{note.title}</h1>
      <section>{note.body}</section>
      {/* (A2) Rendre l'éditeur dynamiquement uniquement si nécessaire */}
      {isEditing 
        ? <NoteEditor note={note} />
        : null
      }
    </div>
  );
}
```

Attendez, un appel à la base de données à l'intérieur d'un composant React ? Oui, vous voyez un composant serveur nommé **Note**. Ce n'est qu'un composant React qui est rendu sur le serveur. C'est-à-dire qu'un composant serveur est simplement un composant React, où vous avez certaines capacités spéciales comme celle que vous voyez dans l'exemple ci-dessus (accéder directement à la base de données).

Eh bien, le composant **Note** est un composant serveur. Qu'en est-il du composant **NoteEditor** à l'intérieur du composant Note ? Voici le corps du composant NoteEditor :

```jsx
// NoteEditor.js - Composant Client

'use client';

import { useState } from 'react';

export default function NoteEditor(props) {
  const note = props.note;
  const [title, setTitle] = useState(note.title);
  const [body, setBody] = useState(note.body);
  const updateTitle = event => {
    setTitle(event.target.value);
  };
  const updateBody = event => {
    setBody(event.target.value);
  };
  const submit = () => {
    // ...sauvegarder la note...
  };
  return (
    <form action="..." method="..." onSubmit={submit}>
      <input name="title" onChange={updateTitle} value={title} />
      <textarea name="body" onChange={updateBody}>{body}</textarea>
    </form>
  );
}
```

Si vous regardez attentivement le code ci-dessus, nous utilisons `'use client'` pour déclarer ce composant comme un composant client. C'est-à-dire que **NoteEditor** est un composant client. Qu'est-ce qu'un composant client à nouveau ? Juste un composant React régulier que vous avez écrit toutes ces années, et ils sont rendus sur le client, c'est-à-dire le navigateur.

Tout composant qui a `'use client'` en haut du fichier est identifié comme un composant client. Si nous ne spécifions pas cela en haut du fichier, le composant dans le fichier est considéré comme un composant serveur.

Pensez-vous donc pouvoir appeler la base de données directement à l'intérieur des composants client ? Non ! Vous n'avez pas accès à l'environnement serveur, puisque les composants client ne sont pas rendus sur le serveur, mais sur le navigateur.

Une question possible que vous pourriez avoir est de savoir si vous pouvez utiliser des composants client à l'intérieur des composants serveur et vice versa.

**Eh bien, les composants client ne peuvent pas importer de composants serveur – mais vous pouvez faire l'inverse.** Importer un composant client ou un composant serveur à l'intérieur d'un composant serveur est possible. Et un composant serveur peut passer un autre composant serveur en tant qu'enfant à un composant client, par exemple :

```jsx
const ServerComponentA = () => {
    return (
        <ClientComponent>
            <ServerComponentB />
        </ClientComponent>
    )
}
```

Dans l'exemple ci-dessus, nous passons un composant serveur nommé ServerComponentB en tant qu'enfant à ClientComponent.

Encore une fois, nous ne pouvons pas importer de composants serveur à l'intérieur des composants client, mais il est tout à fait acceptable de passer un composant serveur en tant qu'enfant à un composant client.

Récapitulons :

* Vous pouvez importer des composants client à l'intérieur des composants serveur.
* Vous ne pouvez pas importer de composants serveur à l'intérieur des composants client.
* Vous pouvez passer un composant serveur en tant que prop enfant à un composant client à l'intérieur d'un composant serveur.

## **Le vrai pouvoir des composants serveur**

Maintenant, nous allons examiner certains des avantages de l'utilisation des composants serveur. Les composants serveur ne concernent pas seulement le rendu des données statiques.

### **Composants avec une taille de bundle nulle**

L'utilisation de bibliothèques est utile pour les développeurs, mais elle augmente la taille du bundle et peut nuire aux performances de l'application.

De nombreuses parties d'une application ne sont pas interactives et n'ont pas besoin d'une cohérence totale des données. Par exemple, une page "détails" montre souvent des informations sur un produit, un utilisateur ou une autre entité et n'a pas besoin d'être mise à jour en réponse aux interactions de l'utilisateur.

Les composants serveur permettent aux développeurs de rendre du contenu statique sur le serveur. Vous pouvez librement utiliser des packages tiers dans les composants serveur tout en subissant **aucun impact sur la taille du bundle**.

```jsx
// NOTE : *avant* les composants serveur

import marked from 'marked'; // 35.9K (11.2K gzipped)
import sanitizeHtml from 'sanitize-html'; // 206K (63.3K gzipped)

function NoteWithMarkdown({text}) {
  const html = sanitizeHtml(marked(text));
  return (/* render */);
}
```

Si nous rendons l'exemple ci-dessus en tant que composant serveur, nous pouvons utiliser le *même code exact* pour notre fonctionnalité mais éviter de l'envoyer au client – une économie de code de plus de 240K (non compressé).

```jsx
// Composant Serveur === taille de bundle nulle

import marked from 'marked'; // taille de bundle nulle
import sanitizeHtml from 'sanitize-html'; // taille de bundle nulle

function NoteWithMarkdown({text}) {
  // même chose qu'avant
}
```

En bref, si vous utilisez une bibliothèque tierce à l'intérieur d'un composant serveur, la bibliothèque n'est pas incluse dans le bundle côté client. Cela réduit la taille du bundle JavaScript.

Mais, si vous utilisez la bibliothèque à l'intérieur de l'un des composants client, alors comme vous l'aurez peut-être deviné, la bibliothèque sera incluse dans le bundle client et sera téléchargée par le navigateur pour l'analyse et l'exécution.

### **Accès complet au backend**

Comme discuté précédemment, les composants serveur peuvent tirer parti de l'accès direct au backend pour utiliser des bases de données, des services internes (micro) et d'autres sources de données spécifiques au backend.

```jsx
import db from 'db';

async function Note({id}) {
  const note = await db.notes.get(id);
  return <NoteWithMarkdown note={note} />;
}
```

Dans l'extrait de code ci-dessus, nous passons **note** au composant **NoteWithMarkdown**. D'où obtenons-nous cette **note** ? De la base de données.

Si vous examinez attentivement le code, nous n'avons pas fait d'appels API fetch pour obtenir la **note**. Au lieu de cela, nous avons simplement exécuté la requête de base de données directement à l'intérieur du composant **Note** (généralement nous faisons des requêtes de base de données dans le code côté serveur). Cela est possible parce que c'est un composant serveur, et il est rendu sur le serveur.

Regardons un autre exemple, où vous pouvez accéder au système de fichiers de votre serveur à partir d'un composant serveur :

```jsx
import fs from 'fs';

async function Note({id}) {
  const note = JSON.parse(await fs.readFile(`${id}.json`));
  return <NoteWithMarkdown note={note} />;
}
```

Comme vous pouvez le voir dans le code ci-dessus, nous utilisons le module `fs` (abréviation de file system) pour lire les fichiers présents sur le serveur.

### **Fractionnement de code automatique**

Les composants serveur traitent toutes les importations de composants client comme des points de fractionnement de code potentiels.

```jsx
// PhotoRenderer.js - Composant Serveur

// l'un de ceux-ci commencera à charger *une fois rendu et diffusé vers le client* :
import OldPhotoRenderer from './OldPhotoRenderer.js';
import NewPhotoRenderer from './NewPhotoRenderer.js';

function Photo(props) {
  // Basculer sur les drapeaux de fonctionnalité, connecté/déconnecté, type de contenu, etc. :
  if (FeatureFlags.useNewPhotoRenderer) {
    return <NewPhotoRenderer {...props} />;
  } else {
    return <OldPhotoRenderer {...props} />;
  }
}
```

Dans l'exemple ci-dessus, nous avons deux composants **NewPhotoRenderer** et **OldPhotoRenderer** (et les deux sont des composants client) qui sont rendus conditionnellement.

Supposons que `if (FeatureFlags.useNewPhotoRenderer)` évalue à True, et que NewPhotoRenderer est le composant que l'utilisateur va voir. Seule cette composante est envoyée au client (ou navigateur). OldPhotoRenderer sera chargé de manière paresseuse (c'est-à-dire qu'il ne sera pas envoyé au client immédiatement). Ainsi, seul le JavaScript lié au composant visible pour l'utilisateur est nécessaire.

### **Plus de cascades**

Comme discuté précédemment, la récupération séquentielle des données introduit des cascades. Nous voulions trouver un moyen d'éviter le délai de trajet aller-retour séquentiel du client au serveur. (C'est-à-dire que nous devons attendre qu'une requête se termine, et la requête peut prendre un certain temps à remplir puisqu'elle doit voyager du client au serveur.)

```jsx
// Note.js - Composant Serveur

async function Note(props) {
  // NOTE : charge *pendant* le rendu, avec un accès aux données à faible latence sur le serveur
  const note = await db.notes.get(props.id);
  if (note == null) {
    // gérer la note manquante
  }
  return (/* rendre la note ici... */);
}
```

Les composants serveur permettent aux applications d'atteindre cet objectif en déplaçant les trajets aller-retour séquentiels vers le serveur. (c'est-à-dire plus d'appels fetch du client au serveur)

Le problème n'est pas vraiment les trajets aller-retour, c'est qu'ils proviennent du client vers le serveur. En déplaçant cette logique vers le serveur, nous réduisons la latence des requêtes et améliorons les performances. Encore une fois, déplacez votre récupération de données vers le serveur (si possible).

## **Conclusion**

Et c'est tout ! Actuellement, Next.js 13 est la voie à suivre si vous souhaitez utiliser les composants serveur. Faire des composants serveur l'option par défaut est probablement le changement le plus audacieux apporté dans Next.js 13.

Amusez-vous à jouer avec les composants serveur dans Next.js 13. Bon codage !