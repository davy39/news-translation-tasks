---
title: Les Hooks React que vous pouvez utiliser dans chaque projet – Expliqués avec
  des exemples
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2023-01-06T19:23:16.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-every-project-should-use
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/7-react-hooks.png
tags:
- name: hooks
  slug: hooks
- name: React
  slug: react
seo_title: Les Hooks React que vous pouvez utiliser dans chaque projet – Expliqués
  avec des exemples
seo_desc: "Hooks are one of the most powerful features of React. \nThey enable us\
  \ to easily reuse functionality across our application's components. What's best\
  \ about hooks is their reusability – you can reuse your hooks both across components\
  \ and your projects...."
---

Les Hooks sont l'une des fonctionnalités les plus puissantes de React. 

Ils nous permettent de réutiliser facilement des fonctionnalités dans les composants de notre application. Ce qui est mieux avec les hooks, c'est leur réutilisabilité – vous pouvez réutiliser vos hooks à la fois dans les composants et dans vos projets.

Voici sept des hooks React les plus importants que je réutilise dans chaque projet React que je crée. Essayez-les aujourd'hui et voyez s'ils sont aussi utiles pour vous lors de la création de vos propres applications React.

Avant de commencer, il est important de clarifier que chaque hook React personnalisé n'a pas besoin d'être écrit par vous. En fait, tous les hooks que je vais mentionner proviennent de la bibliothèque `@mantine/hooks`. 

Mantine est une excellente bibliothèque tierce qui inclut ces hooks et bien d'autres. Ils ajouteront à peu près toutes les fonctionnalités significatives à votre application React que vous pouvez imaginer.

Vous pouvez consulter la documentation pour `@mantine/hooks` sur [mantine.dev](https://mantine.dev).

## Le Hook `useIntersection`

Lorsque l'utilisateur fait défiler la page dans votre application, vous pouvez vouloir savoir quand un élément est visible pour lui. 

Par exemple, vous pouvez vouloir démarrer une animation uniquement lorsque l'utilisateur voit un élément spécifique. Ou, vous pouvez vouloir afficher ou masquer un élément après qu'il a fait défiler une certaine quantité vers le bas de la page. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/use-intersection.gif)
_démo useIntersection_

Pour obtenir des informations sur la visibilité d'un élément, nous pouvons utiliser l'**Intersection Observer API**. Il s'agit d'une API JavaScript intégrée au navigateur. 

Nous pouvons utiliser l'API seule avec du JavaScript simple, mais une excellente façon d'obtenir des informations sur l'intersection d'un élément particulier dans son conteneur de défilement est d'utiliser le hook `useIntersection`. 

```js
import { useRef } from 'react';
import { useIntersection } from '@mantine/hooks';

function Demo() {
  const containerRef = useRef();
  const { ref, entry } = useIntersection({
    root: containerRef.current,
    threshold: 1,
  });

  return (
    <main ref={containerRef} style={{ overflowY: 'scroll', height: 300 }}>
      <div ref={ref}>
        <span>
          {entry?.isIntersecting ? 'Complètement visible' : 'Masqué'}
        </span>
      </div>
    </main>
  );
}
```

Pour l'utiliser, tout ce que nous avons à faire est d'appeler le hook dans notre composant et de fournir un élément racine. Root est le conteneur de défilement, et cela peut être fourni comme une référence avec le hook `useRef`. `useIntersection` retourne une référence que nous passons à l'élément cible, dont l'intersection dans le conteneur de défilement nous voulons observer.

Une fois que nous avons une référence à l'élément, nous pouvons suivre si l'élément est en intersection ou non. Dans l'exemple ci-dessus, nous pouvons voir quand l'élément est masqué ou quand il est complètement visible en fonction de la valeur de `entry.isIntersecting`. 

Vous pouvez passer des arguments supplémentaires qui vous permettent de configurer le **seuil** qui est lié au pourcentage de la cible visible.

## Le Hook `useScrollLock`

Un autre hook lié au défilement est le hook `useScrollLock`. Ce hook est très simple : il vous permet de verrouiller tout défilement sur l'élément body. 

Je l'ai trouvé utile chaque fois que vous souhaitez afficher une superposition ou une modale par-dessus la page actuelle et ne souhaitez pas permettre à l'utilisateur de faire défiler la page en arrière-plan. Cela vous permet soit de concentrer l'attention sur la modale, soit de permettre le défilement dans son propre conteneur de défilement.

```js
import { useScrollLock } from '@mantine/hooks';
import { Button, Group } from '@mantine/core';
import { IconLock, IconLockOpen } from '@tabler/icons';

function Demo() {
  const [scrollLocked, setScrollLocked] = useScrollLock();

  return (
    <Group position="center">
      <Button
        onClick={() => setScrollLocked((c) => !c)}
        variant="outline"
        leftIcon={scrollLocked ? <IconLock size={16} /> : <IconLockOpen size={16} />}
      >
        {scrollLocked ? 'Déverrouiller le défilement' : 'Verrouiller le défilement'}
      </Button>
    </Group>
  );
}
```

`useScrollLock` verrouille le défilement de l'utilisateur à leur position actuelle sur la page. La fonction retourne un tableau, qui peut être déstructuré, comme dans le code ci-dessus. 

La deuxième valeur est une fonction qui nous permet de verrouiller le défilement. La première valeur déstructurée, en revanche, est un booléen qui nous indique si le défilement a été verrouillé ou non. 

Cette valeur est utile, par exemple, si vous souhaitez afficher un certain contenu lorsque le défilement est verrouillé ou pour informer l'utilisateur qu'il a été verrouillé. Vous pouvez voir dans l'exemple ci-dessous que nous indiquons dans notre bouton lorsque le défilement a été verrouillé ou déverrouillé.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/use-scroll-lock.gif)
_démo useScrollLock_

## Le Hook `useClipboard`

Dans de nombreux cas, vous souhaitez fournir un bouton qui permet à l'utilisateur de copier quelque chose dans son presse-papiers, où le texte copié est stocké. 

Un excellent exemple de cela est si vous avez un extrait de code sur votre site web et que vous souhaitez que les utilisateurs puissent le copier facilement. Pour cela, nous pouvons utiliser une autre API web – l'**API Clipboard**. 

`@mantine/hooks` nous offre un hook pratique `useClipboard`, qui retourne quelques propriétés : `copied`, qui est un booléen indiquant si une valeur a été copiée dans le presse-papiers en utilisant le hook, ainsi qu'une fonction `copy`, à laquelle nous pouvons passer n'importe quelle valeur de chaîne pour qu'elle soit copiée. 

Dans notre exemple, nous souhaitons copier un extrait de code pour que nos utilisateurs puissent le coller où ils le souhaitent, comme vu dans la vidéo ci-dessous : 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/use-clipboard.gif)
_démo useClipboard_

Nous appelons notre fonction `copy` lorsqu'ils cliquent sur notre bouton de copie désigné, lui passons l'extrait de code, puis affichons une petite coche ou autre chose indiquant que le texte a été copié. 

Ce qui est intéressant, c'est que le hook `useClipboard` vient avec une **valeur de timeout**. Après une période de timeout donnée, qui est en millisecondes, l'état copié sera réinitialisé, indiquant à l'utilisateur qu'il peut copier le texte à nouveau.

## Le Hook `useDebouncedValue`

Le hook suivant, `useDebouncedValue`, est essentiel si vous avez une entrée de recherche dans votre application.

Chaque fois qu'un utilisateur effectue une recherche à l'aide d'une entrée, l'opération de recherche implique généralement une requête HTTP à une API. 

Un problème typique que vous rencontrerez, surtout si vous souhaitez que vos utilisateurs reçoivent des résultats de recherche au fur et à mesure qu'ils tapent, est qu'une requête sera effectuée à chaque frappe. Même pour une simple requête de recherche, il n'est pas nécessaire d'effectuer autant de requêtes avant qu'un utilisateur n'ait fini de taper ce qu'il veut. 

C'est un excellent cas d'utilisation pour le hook `useDebounceValue`, qui applique une fonction de debounce sur le texte qui lui a été passé. 

```js
import { useState } from 'react';
import { useDebouncedValue } from '@mantine/hooks';
import { getResults } from 'api';

function Demo() {
  const [value, setValue] = useState('');
  const [results, setResults] = useState([])
  const [debounced] = useDebouncedValue(value, 200); // temps d'attente de 200 ms
    
  useEffect(() => {
    if (debounced) {
      handleGetResults() 
    }
     
    async function handleGetResults() {
       const results = await getResults(debounced)   
       setResults(results)
    }
  }, [debounced])

  return (
    <>
      <input
        label="Entrez la requête de recherche"
        value={value}
        style={{ flex: 1 }}
        onChange={(event) => setValue(event.currentTarget.value)}
      />
      <ul>{results.map(result => <li>{result}</li>}</ul>
    </>
  );
}
```

Vous stockez le texte de votre entrée dans un état avec `useState` et passez la variable d'état à `useDebouncedValue`. 

En tant que deuxième argument de ce hook, vous pouvez fournir un temps d'attente, qui est la période de temps pendant laquelle la valeur est débouncée. Le debounce est ce qui nous permet d'effectuer beaucoup moins de requêtes.

Vous pouvez voir le résultat dans la vidéo ci-dessous où l'utilisateur tape quelque chose et seulement après 200 millisecondes, nous voyons la valeur débouncée.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/use-debounced-value.gif)
_démo useDebouncedValue_

## Le Hook `useMediaQuery`

Un autre hook très utile que j'utilise tout le temps est le hook `useMediaQuery`. 

Les Media Queries sont utilisées en CSS simple et le hook `useMediaQuery` nous permet de nous abonner à n'importe quelle media query que nous passons au hook. 

Par exemple, dans notre composant, disons que nous voulons afficher du texte ou changer les styles d'un composant en fonction d'une certaine largeur d'écran, comme 900 pixels. Nous fournissons une media query comme nous le ferions en CSS et `useMediaQuery` nous retourne une valeur `matches` qui est soit vraie soit fausse.

```js
import { useMediaQuery } from '@mantine/hooks';

function Demo() {
  const matches = useMediaQuery('(min-width: 900px)');

  return (
    <div style={{ color: matches ? 'teal' : 'red' }}>
      {matches ? 'Je suis vert' : 'Je suis rouge'}
    </div>
  );
}
```

Il nous indique le résultat de cette media query en JavaScript, ce qui est particulièrement utile lorsque nous avons des styles que nous voulons changer directement dans notre JSX en utilisant la prop `style`, par exemple. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/use-media-query.gif)
_useMediaQuery_

En bref, c'est un hook essentiel pour ces quelques cas où CSS ne peut pas être utilisé pour gérer les media queries. 

## Le Hook `useClickOutside`

Ce hook suivant – `useClickOutside` – peut sembler étrange, mais vous verrez à quel point il est important lorsque vous en aurez réellement besoin. 

Lorsque vous développez une liste déroulante ou quelque chose qui apparaît devant le contenu d'une page et qui doit être fermé ensuite (comme une modale ou un tiroir), ce hook est indispensable. Il est très facile d'ouvrir l'un de ces types de composants en cliquant sur un bouton. Fermer ces composants est un peu plus difficile. 

Pour suivre les bonnes pratiques UX, nous voulons que tout ce qui obstrue la vue de l'utilisateur puisse être facilement fermé en cliquant à l'extérieur de l'élément. C'est spécifiquement ce que le hook `useClickOutside` nous permet de faire. 

Lorsque nous appelons `useClickOutside`, il retourne une référence que nous devons passer à l'élément en dehors duquel nous voulons détecter les clics. Habituellement, cet élément sera contrôlé par un état booléen tel que celui que nous avons dans notre exemple ci-dessous (c'est-à-dire la valeur `opened`). 

```js
import { useState } from 'react';
import { useClickOutside } from '@mantine/hooks';

function Demo() {
  const [opened, setOpened] = useState(false);
  const ref = useClickOutside(() => setOpened(false));

  return (
    <>
      <button onClick={() => setOpened(true)}>Ouvrir la liste déroulante</button>
      {opened && (
        <div ref={ref} shadow="sm">
          <span>Cliquez à l'extérieur pour fermer</span>
        </div>
      )}
    </>
  );
}
```

`useClickOutside` accepte une fonction de rappel qui contrôle ce qui se passe lorsque vous cliquez réellement à l'extérieur de cet élément. 

Dans la plupart des cas, nous voulons faire quelque chose de très simple, qui est de simplement le fermer. Pour ce faire, vous aurez probablement besoin d'un setter d'état (comme `setOpened`) et de lui passer une valeur de false pour ensuite masquer votre contenu superposé.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/use-click-outside.gif)
_démo useClickOutside_

## Le Hook `useForm`

Mon hook préféré et le plus utile de cette liste est le hook `useForm`. 

Ce hook provient spécifiquement de Mantine et implique l'installation d'un package spécifique de la bibliothèque : `@mantine/form`. Il devrait vous fournir tout ce dont vous avez besoin pour créer des formulaires dans React, y compris la capacité de valider les entrées, d'afficher des messages d'erreur et de vous assurer que les valeurs des entrées sont correctes avant que le formulaire ne soit soumis.

`useForm` accepte certaines valeurs initiales qui correspondent aux entrées que vous avez dans votre formulaire.

```js
import { TextInput, Button } from '@mantine/core';
import { useForm } from '@mantine/form';

function Demo() {
  const form = useForm({
    initialValues: {
      email: ''
    },

    validate: {
      email: (value) => (/^\S+@\S+$/.test(value) ? null : 'Email invalide'),
    },
  });

  return (
    <div>
      <form onSubmit={form.onSubmit((values) => console.log(values))}>
        <TextInput
          withAsterisk
          label="Email"
          placeholder="votre@email.com"
          {...form.getInputProps('email')}
        />
        <Button type="submit">Soumettre</Button>
      </form>
    </div>
  );
}
```

Le grand avantage de `useForm` est ses helpers, comme la fonction `validate`, qui reçoit la valeur qui a été tapée dans chaque entrée, puis vous permet de créer des règles de validation. 

Par exemple, si vous avez une entrée d'email, vous pouvez avoir une expression régulière pour déterminer si elle est en fait un email valide (comme vous pouvez le voir dans le code ci-dessus). Si ce n'est pas le cas, alors vous pouvez afficher un message d'erreur et empêcher le formulaire d'être soumis. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/use-form.gif)
_démo useForm_

Comment obtenir les valeurs qui ont été tapées dans le formulaire ? 

Mantine fournit un helper très pratique appelé `getInputProps`, où vous fournissez simplement le nom de l'entrée avec laquelle vous travaillez (comme email) et il configure automatiquement un onChange pour suivre les valeurs que vous avez tapées dans votre formulaire. 

De plus, pour gérer la soumission du formulaire et empêcher la soumission si ses valeurs ne passent pas les règles de validation, il dispose d'une fonction spéciale `onSubmit` que vous enveloppez autour de votre fonction onSubmit régulière. En plus d'appliquer les règles de validation, elle s'occupera d'appeler `preventDefault()` sur l'événement du formulaire afin que vous n'ayez pas à le faire manuellement. 

Je ne fais qu'effleurer la surface avec ce hook, mais je vous recommande vivement de l'utiliser pour votre prochain projet. Les formulaires sont traditionnellement un casse-tête à faire fonctionner correctement, surtout les formulaires qui nécessitent une validation et des messages d'erreur visibles. `useForm` les rend incroyablement faciles !

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même. 

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*