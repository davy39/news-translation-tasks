---
title: Routing dans Next.js – Comment configurer le routage dynamique avec le pré-rendu
  dans Next
subtitle: ''
author: Matthes B.
co_authors: []
series: null
date: '2022-07-29T21:21:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-dynamic-routing-in-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-pixabay-2150.jpg
tags:
- name: Next.js
  slug: nextjs
- name: routing
  slug: routing
seo_title: Routing dans Next.js – Comment configurer le routage dynamique avec le
  pré-rendu dans Next
seo_desc: 'In this tutorial, you''ll learn how to set up dynamic routing in Next.js.
  You''ll also learn about pre-rendering and why it''s important.

  🔐 Here''s what we''ll cover:


  You''ll get to know getStaticPaths(), one of the core principles of Next.js.

  You''ll imp...'
---

Dans ce tutoriel, vous apprendrez à configurer le routage dynamique dans Next.js. Vous en apprendrez également sur le pré-rendu et pourquoi c'est important.

## 🔐 Voici ce que nous allons couvrir :

* Vous découvrirez `getStaticPaths()`, l'un des principes de base de Next.js.
* Vous améliorerez vos connaissances générales sur Next.js et votre confiance.
* Vous aurez accès à un exemple rapidement reproductible pour vos propres besoins d'apprentissage de Next.js.

## **📝** Prérequis

* Vous devriez être familier avec ce qu'est Next.js et pourquoi vous devriez envisager de l'utiliser.
* Vous devriez avoir une certaine compréhension de ce que signifient [**Routing**](https://nextjs.org/docs/routing/introduction) et [**Dynamic Routing**](https://nextjs.org/docs/routing/dynamic-routes) dans React et/ou Next.js.
* Pour cet exemple, je travaille avec TypeScript. Mais il n'est pas nécessaire que vous soyez familier avec TypeScript. Je vais aborder le code qui serait omis lors de l'utilisation de JavaScript. De plus, chaque fois que vous voyez `.tsx` concernant des fichiers, vous pouvez simplement le remplacer par `.js` si vous utilisez JavaScript.

## **🏕️** L'objectif

Ce guide rapide vise à vous aider à gérer la récupération de données, qui peut être utilisée à des fins de pré-rendu dans les routes dynamiques de Next.js. Nous discuterons de la théorie ainsi que d'un exemple pratique.

Bien que nous nous concentrions sur la logique réelle du code requis, je ne ferai aucun style CSS. N'hésitez pas à être créatif sur le frontend pour votre propre projet lorsque vous utilisez les techniques que nous discutons dans ce tutoriel.

## 🔧 Comment fonctionne le routage dans Next.js

Alors que React lui-même utilise une approche basée sur le code pour toute intention de routage, Next.js utilise un système de fichiers pour le concept de routage.

Par conséquent, vous êtes probablement familier avec le routage basé sur le code dans React, qui peut ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/React-Routing.PNG)
_Exemple de routage React basé sur le code_

Avec cette approche basée sur le code, vous pouvez, par exemple, naviguer de la route principale à ``/`` vers la page ``about`` via ``/about``.

Vous pouvez également trouver une approche de routage dynamique dans cet exemple React avec le chemin ``:productId``.

Avec Next.js, cependant, nous n'utilisons plus un tel routage basé sur le code. Au lieu de cela, ce framework React utilise un routage basé sur les fichiers. Cela signifie que vous configurez vos routes directement via des fichiers de page.

Considérez le dossier ``pages`` suivant contenant des sous-dossiers et des fichiers :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Nextjs-Routing.PNG)
_Exemple de routage Next.js basé sur les fichiers_

Le fichier ``index.tsx`` serait l'équivalent du chemin ``/`` dans l'exemple de routage React ci-dessus. Vous pourriez donc accéder au contenu du fichier ``user-profile.tsx`` via ``/user-profile`` – c'est tout !

D'un autre côté, si vous souhaitez accéder à un contenu imbriqué, vous pouvez utiliser ``/stars/[id]`` afin de trouver le contenu dans le fichier de page correspondant.

Peut-être avez-vous remarqué que j'utilise des crochets pour ``[id].tsx`` ainsi que pour ``[something].tsx``. C'est nécessaire pour configurer le routage dynamique dans Next.js.

Vous pourriez techniquement insérer n'importe quelle entrée que vous souhaitez pour ``[id]`` et la page se chargerait pour ce chemin spécifique.

Gardez simplement à l'esprit que si cette route dynamique nécessite une entrée valide pour ``[id]`` (peut-être un type d'identifiant de produit existant pour lequel nous voulons récupérer les données respectives), alors il pourrait y avoir une erreur.

## ✂️ Récupération de données dans Next.js avec routage dynamique

Imaginez que vous appliquez cette approche de routage dynamique à une page de boutique où vous listez une série d'articles différents. Chaque article aurait un lien pour plus d'informations sur cet article spécifique.

Dans cet élément de lien, vous pourriez diriger l'utilisateur vers une route dynamique avec un paramètre valide (l'identifiant de produit correspondant, par exemple). Pour de tels cas, le routage dynamique est la meilleure approche.

### ❓ Comment fonctionne `getStaticProps()` ?

Avec cette fonction, vous pouvez pré-rendre une page au moment de la construction. Cela est utile pour l'optimisation des moteurs de recherche (SEO), par exemple, et peut générer une meilleure expérience utilisateur.

Les données qui doivent être pré-rendues peuvent généralement être trouvées dans une base de données, par exemple. Comme avec `getStaticProps()`, vous êtes en mesure d'écrire directement n'importe quel code côté serveur dans cette fonction à des fins de récupération de données (au lieu de faire appel à une route API sur le backend, qui passe ensuite par les actions côté serveur requises).

Il y a plus à dire sur `getStaticProps()`. Si vous êtes assez nouveau dans tout cela, je vous recommande vivement de consulter la [documentation officielle de Next.js](https://nextjs.org/docs/basic-features/data-fetching/get-static-props) sur ce sujet.

### ❓ Quel est le but de `getStaticPaths()` ?

Alors que `getStaticProps()` semble déjà faire tout le travail dont nous avons besoin pour nos pages, nous rencontrerons une erreur lorsque nous utiliserons cette fonction seule sur des pages de routage dynamique. Le message d'erreur vous indiquera en fait ce fait spécifique que `getStaticPaths()` est manquant.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/error-message.PNG)
_Capture d'écran de l'erreur serveur. SSG signifie Static-Site Generation_

`getStaticProps()` utilise le concept de génération de site statique. Ainsi, Next.js pré-rendra la page respective au moment de la construction. Dans le cas des routes dynamiques, cependant, Next.js ne sait pas par lui-même quels chemins pré-rendre. Au lieu de cela, vous devez intervenir et aider – et c'est là que `getStaticPaths()` est utile.

Ainsi, avec `getStaticPaths`, vous pouvez spécifier quels chemins du routage dynamique doivent être pré-rendus et/ou comment les chemins inconnus doivent être gérés.

### 📋 Note rapide

Si vous utilisez `getServerSideProps()`, qui peut être utilisé pour des raisons similaires à `getStaticProps()`, vous remarquerez que `getStaticPaths()` n'est en fait pas nécessaire. Pourquoi ?

`getServerSideProps()` n'utilise pas le principe de génération statique. Au lieu de construire la page, Next.js pré-rend la page à chaque requête avec les données retournées. Cela s'appelle le rendu côté serveur.

Nous n'avons pas à dire à Next.js quels chemins doivent être pré-rendus statiquement lors de l'utilisation de `getServerSideProps()`, puisque il n'y a pas une telle chose pour cette fonction en premier lieu.

Si vous souhaitez en savoir plus sur cette fonction, je peux à nouveau recommander la documentation officielle de Next.js pour le [rendu côté serveur](https://nextjs.org/docs/basic-features/data-fetching/get-server-side-props). Cependant, cela est hors du cadre de ce guide rapide et je n'aurai pas besoin de `getServerSideProps()` pour aucune des étapes suivantes.

## 🔧 Comment configurer notre projet

Pour cet exemple, nous allons reproduire un petit cas de routage dynamique. Pour cela, j'ai préparé un sous-dossier `test` dans le dossier `pages`. Le dossier `pages` est automatiquement créé par Next.js.

Dans le dossier `test`, j'insère le fichier `[something].tsx` (`[something].js` si vous utilisez JavaScript et non TypeScript).

Il y a également un dossier `backendData` au niveau racine de notre application Next.js avec le fichier `some-backend-data.json` (donc pas dans le dossier `pages`). Ce fichier nous fournira les données que nous insérerons dynamiquement.

### 🔧 Configuration des données backend `JSON`

Pour cet exemple, je crée des données factices qui seront intégrées dans le `some-backend-data.json` dans le dossier `backendData`. De cette façon, nous pouvons reproduire une situation où vous avez accès à une sorte de données dans le backend que vous souhaitez utiliser sur le frontend.

Voici à quoi ressemble le fichier `some-backend-data.json` :

```json
{
    "stars": [
        { 
            "id": "St2-18", 
            "name": "Stephenson 2-18", 
            "description": "Stephenson 2-18 est une supergéante rouge (RSG) ou une hypergéante rouge extrême (RHG) dans la constellation du Scutum.", 
            "link": "https://en.wikipedia.org/wiki/Stephenson_2-18" 
        },
        { 
            "id": "UY-SC", 
            "name": "UY Scuti", 
            "description": "UY Scuti est une hypergéante rouge extrême ou une supergéante rouge dans la constellation Scutum.", 
            "link": "https://en.wikipedia.org/wiki/UY_Scuti"
        },
        { 
            "id": "RSGC1", 
            "name": "RSGC1-F01", 
            "description": "RSGC1-F01 est une supergéante rouge située dans l'amas ouvert RSGC1 dans la constellation du Scutum.", 
            "link": "https://en.wikipedia.org/wiki/RSGC1-F01"
        }
    ]
}
```

Dans ce fichier, vous trouverez des données formatées en `JSON`. Il y a `"stars"` qui est simplement un tableau avec trois objets. Les trois objets ont le même format et incluent un `id`, un `name`, une `description` et un `link` vers une page web externe.

Comme vous l'avez peut-être deviné, ce sont en fait des étoiles réelles dans notre univers.

Dans une situation réelle, vous auriez probablement une sorte de connexion à une base de données, mais les données réelles que vous recevez de cette base de données pourraient techniquement être formatées comme dans cet exemple. Donc cela est suffisant pour notre configuration d'exemple.

### 🔧 Imports et interface

En tant qu'étape suivante, nous pouvons plonger dans la création réelle de la route dynamique Next.js `[something].tsx`. Commençons par les imports requis pour cet exemple :

```typescript
import { GetStaticProps, GetStaticPaths  } from 'next';
import { useRouter } from 'next/router';
import path from 'path';
import fs from 'fs/promises';

interface starInterface {
    id: string
    name: string
    description: string
    link: string
}
```

Gardez à l'esprit que j'utilise TypeScript ici. Si vous utilisez JavaScript, c'est bien sûr correct également. Souvenez-vous simplement que vous n'avez pas besoin de l'`interface starInterface` ou de `import { GetStaticProps, GetStaticPaths } from 'next'`.

### 🔧 Comment créer la fonction de récupération de données

Pour l'étape suivante, je vais préparer une fonction `async` appelée `getData()`, qui sera utile pour les fonctions `getStaticProps()` et `getStaticPaths()`. Cela peut sembler assez confus, surtout si vous n'avez jamais eu de contact avec le code JavaScript backend comme vous pourriez vous y attendre dans une application Node.js, par exemple.

Restez avec moi encore quelques secondes. Vous n'avez pas besoin de comprendre le code suivant en détail. Nous devons simplement savoir quel est le résultat de la fonction `getData()`.

```typescript
async function getData() {
    const filePath = path.join(process.cwd(), 'backendData', 'some-backend-data.json');
    const fileData = await fs.readFile(filePath);
    const data = JSON.parse(jsonData.toString());

    return data;
  }
```

Comme vous pouvez le voir, il y a trois variables : `filePath`, `fileData` et `data`. Avec `filePath`, nous nous concentrons simplement sur le fichier où nous avons placé nos données `JSON`. Nous ciblons donc le répertoire de travail actuel (cwd), puis le dossier `backendData`, et enfin le fichier `JSON`.

Avec `fileData`, nous essayons de lire ce fichier et d'extraire les données `JSON` réelles qui y sont stockées.

Nous avons besoin de `data` pour convertir ces `fileData` afin de pouvoir les utiliser pour nos prochaines étapes.

En résumé, `getData()` nous fournit simplement les données du fichier `some-backend-data.json` afin que nous puissions les utiliser dans `getStaticProps()` ainsi que dans `getStaticPaths()`. Il n'y a pas grand-chose de plus à dire.

### 🔧 Configuration pour `getStaticProps()`

Après avoir implémenté `getData()` (qui sera utile lorsque nous essaierons de récupérer nos données backend factices), nous allons maintenant créer la fonction `getStaticProps()`.

Ici, nous utiliserons `getStaticProps()` pour activer le pré-rendu des données spécifiques récupérées pour les chemins de notre route dynamique.

Avant de plonger directement dans l'exemple de code ci-dessous, réfléchissez rapidement à ce que nous voulons réellement accomplir.

L'utilisateur doit être dirigé vers cette route dynamique spécifique, qui est indiquée par un identifiant unique dans l'URL. Par cela, je veux dire que nous voulons que `/test/St2-18` et `test/UY-SC` mènent à la même page dynamique.

Les données que l'utilisateur verra doivent cependant différer les unes des autres puisque nous voulons récupérer des données pour `St2-18` et `UY-SC`, respectivement.

Nous avons une fonction `getData()` qui aide à atteindre nos données backend. Mais nous devons encore savoir quelles données exactes nous voulons extraire de notre backend factice.

Pour cette étape, nous pouvons extraire l'identifiant spécifique de l'URL, `St2-18` par exemple, et combiner cela avec nos données `getData()` extraites.

À partir de là, nous pouvons rechercher l'objet spécifique contenant les données que nous voulons afficher dans le résultat `getData()` de notre backend.

Maintenant, retournons à notre exemple de code pour voir ce processus en action.

Voir la section de code suivante où nous implémentons `getStaticProps()` :

```typescript
export const getStaticProps: GetStaticProps = async (context) => {
    const itemID = context.params?.something;
    const data = await getData();
    const foundItem = data.stars.find((item: starInterface) => itemID === item.id);
  
    if (!foundItem) {
      return {
        props: { hasError: true },
      }
  }
  
  return {
    props: {
      specificStarData: foundItem
    }
  }
}
```

Pour JavaScript, vous pouvez simplement omettre `GetStaticProps` en tant que type pour `getStaticProps()`.

`getStaticProps()` peut nous fournir un paramètre `context` grâce auquel nous pouvons atteindre certaines méthodes utiles. Pour l'instant, il est simplement important de comprendre que grâce à `context`, nous sommes en mesure d'accéder à `params` et ensuite d'atteindre l'identifiant actuel de notre chemin spécifique pour lequel `something` est le placeholder.

Rappelez-vous que ce fichier s'appelle en fait `[something].tsx`, c'est pourquoi nous accédons à `something` dans ce contexte.

Avec cette approche, nous extrayons avec succès les informations dont nous avons besoin de notre URL pour rechercher l'objet spécifique dans notre tableau de données backend. Ensuite, nous sauvegardons ces informations dans la variable `itemID`.

Disons que l'utilisateur accède à `/test/St2-18`, alors `itemID` contiendrait la valeur `St2-18`.

Puisque nous avons notre fonction pratique `getData()`, nous pouvons simplement obtenir nos données backend via cette fonction et les sauvegarder dans `data`.

Puisque nous avons maintenant `itemID` ainsi que `data`, nous pouvons combiner les deux variables et créer `foundItem`. Cela retourne l'objet qui inclut `itemID` en tant qu'`id`.

Avec l'instruction `if`, nous vérifions si `foundItem` existe réellement. Ou en d'autres termes, nous vérifions si nos données backend contiennent des données avec l'`id` correspondant que nous avons extrait via notre `itemID`.

Si aucune donnée ne peut être trouvée, nous retournons ce booléen `hasError` avec la valeur `true`. Cela nous aide à gérer de tels cas sur le frontend.

S'il y a des données, alors nous retournons notre `foundItem` au frontend. Gardez à l'esprit que tout ce que vous retournez dans cet objet `props` sera en fait exposé au frontend. Donc ne retournez aucune information d'identification (clés API personnelles, par exemple).

### 🔧 Configuration pour `getStaticPaths()`

Avant de passer à la partie frontend de notre page dynamique, nous devons encore implémenter la fonction `getStaticPaths()` :

```typescript
  export const getStaticPaths: GetStaticPaths = async () => {
    const data = await getData();
    const pathsWithParams = data.stars.map((star: starInterface) => ({ params: { something: star.id }}))

    return {
        paths: pathsWithParams,
        fallback: true
    }
  }
```

Pour JavaScript, vous pouvez simplement omettre `GetStaticPaths` en tant que type pour `getStaticPaths()`. Vous pouvez également supprimer `starInterface` pour JavaScript.

Dans la fonction `getStaticPaths()`, nous voulons dire à Next.js quels chemins doivent être pré-rendus.

Pour cette étape, nous accédons à nos données backend avec `getData()`, comme vous l'avez vu dans `getStaticProps()`.

`getStaticPaths()` exige une forme spécifique pour les `paths` dans le retour. Vous avez en fait deux options :

* La première est l'approche que j'utilise dans cet exemple : `paths: [{ params: { something: star.id } }]`. Il devrait s'agir d'un tableau avec un objet pour chaque chemin que vous voulez que Next.js pré-rende.
* La deuxième option est d'utiliser des chaînes de chemin comme ceci : `paths: ['/test/St2-18', '...', '...']`.

Les deux techniques atteignent le même comportement, alors choisissez celle que vous préférez.

### Qu'est-ce que la propriété `fallback` ?

Il est important de comprendre que vous n'avez pas besoin d'inclure chaque chemin qui doit être pré-rendu. Cela est particulièrement utile lorsque vous avez beaucoup de cas à considérer et que vous ne voulez pas que tout soit pré-rendu.

Pour gérer de tels cas, la propriété `fallback` est particulièrement utile.

Vous pouvez lire plus de détails sur le `fallback` dans la [documentation officielle de Next.js](https://nextjs.org/docs/api-reference/data-fetching/get-static-paths#fallback-false).

En mes propres mots, je l'expliquerais comme suit :

* ``fallback`` défini sur ``false`` mènerait automatiquement à une page d'erreur 404 chaque fois que l'utilisateur essaierait d'accéder à un chemin qui n'a pas été reconnu par ``getStaticPaths()`` via la propriété paths.
* ``fallback`` défini sur ``true`` ne mène pas automatiquement à une page d'erreur 404 chaque fois que l'utilisateur essaie d'accéder à un chemin qui n'existe pas dans ``getStaticPaths()``.
De cette façon, nous atteignons toujours le frontend et sommes en mesure de gérer la situation là-bas en affichant une sorte de séquence de chargement, par exemple. Vous pouvez également afficher une erreur sur le frontend s'il n'y avait aucune donnée à récupérer lorsqu'il n'y avait aucune donnée d'élément valide pour le paramètre de chemin spécifique.
* ``fallback`` défini sur ``'blocking'`` ne mène pas automatiquement à une page d'erreur 404 chaque fois que l'utilisateur essaie d'accéder à un chemin qui n'existe pas dans ``getStaticPaths()``. Il est similaire à ``fallback`` défini sur ``true`` mais maintenant nous omettons essentiellement tous les processus de chargement manuels. Au lieu de cela, le navigateur prend simplement un peu plus de temps pour récupérer les données et affiche ensuite la page prête à l'emploi. Cela est utile lorsque vous ne souhaitez pas présenter un "Chargement..." à l'utilisateur, par exemple, et préférez simplement le faire attendre un peu plus longtemps avant que la page ne soit chargée avec succès. Si aucune donnée n'a pu être trouvée, alors nous avons toujours l'opportunité de créer une erreur manuelle sur le frontend.

Puisque nous avons un ensemble de données si petit, nous donnons simplement chaque chemin possible à `getStaticPaths()`. Nous n'avons donc techniquement pas besoin de trop d'attention pour la propriété `fallback`.

Néanmoins, je définis `fallback` sur `true` pour vous montrer comment vous pouvez gérer de telles erreurs manuelles ainsi que les séquences de chargement qui pourraient se produire.

### 🔧 Comment configurer le frontend

Dans la dernière étape, nous allons configurer notre page réelle. Tout ce qui se trouve ici sera le contenu frontend que l'utilisateur verra :

```typescript
function projectPage(props: { specificStarData: starInterface, 
hasError: boolean }) {
  const router = useRouter();

  if (props.hasError) {
    return <h1>Erreur - veuillez essayer un autre paramètre</h1>
  }

  if (router.isFallback) {
      return <h1>Chargement...</h1>
  }

  return (
    <div>
      <h1>{props.specificStarData.name}</h1>
      <p>{props.specificStarData.description}</p>
      <a href={props.specificStarData.link}>Plus d'informations ici (lien)</a>
    </div>
  )
}

export default projectPage;
```

Pour JavaScript, vous n'avez pas à mentionner `starInterface` ainsi que `boolean` dans les arguments de la fonction.

Dans le code ci-dessus, vous pouvez trouver notre `specificStarData` ainsi que `hasError`, qui contiennent tous deux certaines valeurs. En outre, nous utilisons le hook `useRouter()` afin d'avoir accès à `isFallback`, ce qui nous aide à gérer les cas de `fallback`.

Rappelez-vous que le `fallback` de `getStaticPaths()` peut être défini sur `true` ou `'blocking'` si vous n'êtes pas en mesure de fournir chaque route dynamique pour le pré-chargement. Dans ces cas, cela empêcherait votre page de planter.

Au lieu de cela, elle se chargera pendant un certain temps à la volée lorsque l'utilisateur accède à cette route dynamique spécifique et fournira ensuite les informations respectives.

Pour cette séquence de chargement potentielle, nous utilisons `router.isFallback` afin de retourner du JSX avec une sorte d'indication de chargement pour l'utilisateur.

S'il y a effectivement une erreur parce que l'utilisateur a essayé d'accéder à un chemin dynamique pour lequel aucune donnée ne peut être trouvée, `hasError` intervient, indiquant qu'il y a une erreur réelle.

En supposant que l'utilisateur a effectivement atteint un chemin dynamique pour lequel des données ont pu être récupérées, la sortie JSX prévue sera retournée.

En suivant toutes les étapes de configuration (avec `fallback: true`), nous recevons cette sortie pour le chemin `/test/St2-18` :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-250.png)
_Résultat pour **/test/St2-18**_

Si nous essayons de mettre un paramètre invalide, il essaie d'abord de charger puis retourne notre message d'erreur configuré manuellement :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-252.png)
_Résultat pour **/test/this-will-produce-an-error**_

### 🎲 Comment tester la propriété `fallback`

Et c'est à peu près tout ! Le résultat est une route dynamique qui utilise `getStaticProps()` ainsi que `getStaticPaths()` afin de pré-rendre les données récupérées de notre backend factice.

Lorsque vous travaillez avec `getStaticPaths()` pour la première fois, je recommande d'essayer les différentes valeurs de `fallback` (`true`, `false`, `'blocking'`) pour découvrir comment le comportement de votre application change exactement.

Puisque nous utilisons `fallback: true` dans notre exemple, nous sommes également en mesure de simplement insérer un chemin possible sur les trois sans que notre application ne plante.

Donc, disons que nous changeons la propriété `paths` dans `getStaticPaths()` en `paths: ['/test/St2-18']`. Alors que nous avons inséré tous les chemins auparavant, nous n'utilisons maintenant qu'un seul chemin avec la méthode de chaîne que j'ai mentionnée plus tôt au lieu du format `{ params: { something: star.id }}`.

Avec cette configuration, vous pouvez toujours accéder à `/test/UY-SC`, par exemple, mais vous remarquerez que le message `Chargement...` apparaît pendant un bref moment parce que nous avons préparé ce cas dans notre instruction if avec `router.isFallback`. Après que les données soient chargées, elles s'afficheront avec succès à l'écran.

Lorsque vous utilisez `fallback: 'blocking'` et `paths: ['/test/St2-18']`, vous remarquerez que vous ne pouvez pas voir de `Chargement...`. Au lieu de cela, le navigateur prend simplement un peu plus de temps pour charger les données avant de changer le contenu du navigateur.

C'est à vous de choisir la méthode que vous préférez.

## **✅** Conclusion

Bien que cet exemple montre les parties fondamentales de `getStaticProps()` ainsi que `getStaticPaths()`, il y a encore plus à lire sur ces fonctions Next.js.

Néanmoins, tout ce que vous avez lu ici est suffisant pour commencer à travailler avec `getStaticProps()` et `getStaticPaths()` par vous-même dans de nombreux cas.

## **📃** Ressources et matériel d'apprentissage

* Documentation officielle de Next.js pour [**Data Fetching**](https://nextjs.org/docs/basic-features/data-fetching/overview).
* Pour en savoir plus sur Next.js dans son ensemble, je peux fortement recommander de consulter le [cours Udemy de Maximilian Schwarzmüller pour Next.js](https://www.udemy.com/course/nextjs-react-the-complete-guide/). Ce cours m'a beaucoup aidé, en tout cas.