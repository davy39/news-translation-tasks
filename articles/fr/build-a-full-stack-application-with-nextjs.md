---
title: Comment créer une application Full-Stack avec Next.js – Un tutoriel étape par
  étape pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-30T21:54:36.000Z'
originalURL: https://freecodecamp.org/news/build-a-full-stack-application-with-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Frame-3-2.jpg
tags:
- name: full stack
  slug: full-stack
- name: Next.js
  slug: nextjs
seo_title: Comment créer une application Full-Stack avec Next.js – Un tutoriel étape
  par étape pour débutants
seo_desc: 'By Yazdun Fadali

  Next.js can seem intimidating at first, with so many new concepts to grasp. But
  don''t worry – in this step-by-step tutorial, I will provide you with all the essential
  information you need to create your first modern full-stack applic...'
---

Par Yazdun Fadali

Next.js peut sembler intimidant au premier abord, avec tant de nouveaux concepts à assimiler. Mais ne vous inquiétez pas – dans ce tutoriel étape par étape, je vais vous fournir toutes les informations essentielles dont vous avez besoin pour créer votre première application full-stack moderne avec Next.js.

Dans ce tutoriel, je vais vous guider à travers les bases de Next.js et vous aider à créer votre toute première application full-stack. À la fin de ce tutoriel, vous aurez la confiance nécessaire pour commencer à construire vos propres applications full-stack avec Next.js.

Alors, plongeons directement et découvrons ensemble le pouvoir de Next.js.

## Voici ce que nous allons couvrir :

* [Qu'allons-nous construire ?](#heading-quallons-nous-construire)
* [Premiers pas](#heading-premiers-pas)
* [Comment créer une mise en page partagée dans Next.js](#heading-comment-creer-une-mise-en-page-partagee-dans-nextjs)
* [Comment créer une barre de navigation personnalisée dans Next.js](#heading-comment-creer-une-barre-de-navigation-personnalisee-dans-nextjs)
* [Comment créer une route API dans Next.js](#heading-comment-creer-une-route-api-dans-nextjs)
* [Comment construire la page d'accueil](#heading-comment-construire-la-page-daccueil)
* [Qu'est-ce que le routeur d'application dans Next.js ?](#heading-quest-ce-que-le-routeur-dapplication-dans-nextjs)
* [Comment améliorer la modularité et la maintenabilité de votre base de code Next.js](#heading-comment-ameliorer-la-modularite-et-la-maintenabilite-de-votre-base-de-code-nextjs)
* [Comment créer une page de personnage dynamique](#heading-comment-creer-une-page-de-personnage-dynamique)
* [Comment créer des routes API dynamiques dans Next.js](#heading-comment-creer-des-routes-api-dynamiques-dans-nextjs)
* [Comment créer des routes UI dynamiques dans Next.js](https://www.freecodecamp.org/news/p/66b07963-0044-4140-a058-5e8a5ff76dd3/how-to-create-dynamic-ui-routes-in-next-js)
* [Qu'est-ce que `generateStaticParams` dans Next.js ?](#heading-quest-ce-que-generatestaticparams-dans-nextjs)
* [À quoi sert `dynamicParams` lors de la génération de pages statiques dans Next.js ?](#heading-a-quoi-sert-dynamicparams-lors-de-la-generation-de-pages-statiques-dans-nextjs)
* [Comment générer des pages statiques avec `generateStaticParams`](#heading-comment-generer-des-pages-statiques-avec-generatestaticparams)
* [Comment construire la section quiz](#heading-comment-construire-la-section-quiz)
* [Comment créer un composant côté client dans Next.js](#heading-comment-creer-un-composant-cote-client-dans-nextjs)
* [Conclusion](#heading-conclusion)

Très bien, plongeons-nous dans le vif du sujet !

## Qu'allons-nous construire ?

Dans ce tutoriel, nous allons créer une application engageante qui présente des informations sur les personnages de Family Guy. De plus, nous inclurons une section quiz où les utilisateurs pourront tester leurs connaissances sur la série.

Pour garder les choses simples et familières pour vous, nous éviterons d'utiliser une base de données et utiliserons plutôt des données JSON locales. En éliminant la complexité de l'intégration de la base de données, nous pouvons nous concentrer sur la maîtrise des concepts fondamentaux de Next.js.

![Application Nex.js affichant des données sur les personnages de Family Guy](https://www.freecodecamp.org/news/content/images/2023/05/ezgif-2-c0def76210.gif)
_Aperçu de l'application_

## **Premiers pas**

Pour commencer ce tutoriel, je vous recommande vivement d'utiliser le [modèle de démarrage fourni](https://github.com/Yazdun/next-fcc-familyguy/tree/starter) que j'ai spécialement créé pour ce tutoriel. Il vous fait gagner un temps précieux en incluant déjà les dépendances nécessaires et la structure des dossiers, éliminant ainsi le besoin de configurer votre projet à partir de zéro.

Il vous suffit de cloner le [modèle de démarrage](https://github.com/Yazdun/next-fcc-familyguy/tree/starter) depuis le dépôt GitHub, puis de suivre le tutoriel. De cette façon, vous pouvez vous concentrer sur l'apprentissage et la mise en œuvre des concepts sans vous perdre dans les détails de configuration.

* Modèle de démarrage : [Voir sur GitHub](https://github.com/Yazdun/next-fcc-familyguy/tree/starter)
* Version finale : [Voir sur GitHub](https://github.com/Yazdun/next-fcc-familyguy)

Une fois que vous avez configuré le modèle de démarrage et l'avez exécuté avec succès sur votre machine locale, vous devriez pouvoir voir la page initiale. Cette page marque le début de notre tutoriel et servira de point de départ pour notre voyage.

![Page initiale du modèle](https://www.freecodecamp.org/news/content/images/2023/05/image-87.png)
_Page initiale du modèle_

À partir de là, nous allons progressivement construire sur le code existant et implémenter quelques fonctionnalités intéressantes dans notre application. Plongeons-nous et commençons tout de suite !

## Comment créer une mise en page partagée dans Next.js

Souvent dans vos applications, vous avez des éléments qui sont partagés sur plusieurs pages, comme une barre de navigation ou un pied de page. Ajouter manuellement ces éléments à chaque page peut être fastidieux et sujet aux erreurs. Heureusement, Next.js fournit un moyen pratique de créer des mises en page partagées qui peuvent être réutilisées dans toute notre application.

Le premier type de mise en page s'appelle la mise en page racine. Comme son nom l'indique, cette mise en page est partagée sur toutes les pages de notre application. Elle sert de mise en page la plus haute et fournit une structure cohérente pour toute notre application. La mise en page racine est **requise** et nous devons nous assurer qu'elle inclut les balises HTML et body nécessaires.

Ensuite, considérons les segments de route individuels dans votre application. Chaque segment a la possibilité de définir sa propre mise en page. Ces mises en page, similaires à la mise en page racine, seront partagées sur toutes les pages de ce segment. Cela vous permet d'avoir des mises en page spécifiques pour différentes sections de votre application, tout en maintenant une structure cohérente dans chaque segment.

Maintenant, ouvrez `app/layout.js` et ajoutez le code suivant :

```jsx
// 📁 app/layout.js

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Family Guy',
  description: 'Venez ici et en savoir plus sur Family Guy !',
}

export default function RootLayout({ children }) {
  return (
    <html lang="fr">
      <body className={inter.className}>
        <Navigation />
        {children}
      </body>
    </html>
  )
}

```

Le composant que vous voyez ici est le composant de mise en page racine, qui joue un rôle crucial dans la création d'une mise en page partagée pour toute votre application. Examinons de plus près sa structure et sa fonctionnalité.

Dans le composant, vous définissez l'objet `metadata`, qui contient les balises de métadonnées par défaut pour votre application. La propriété `title` spécifie le titre de votre application, tandis que la propriété `description` fournit une brève description. Ces balises de métadonnées sont importantes pour le référencement (SEO) et peuvent être remplacées pour des routes spécifiques si nécessaire.

À l'intérieur de la fonction `RootLayout`, vous structurez le document HTML en utilisant les balises `html` et `body`. Vous définissez l'attribut `lang` de la balise `html` sur `"fr"` pour indiquer que le contenu est en français.

À l'intérieur de la balise `body`, vous incluez le composant `Navigation`, qui est importé depuis le répertoire `components`. Ce composant représente votre barre de navigation et sera partagé sur toutes les pages de votre application. En l'incluant ici, vous vous assurez qu'il est affiché de manière cohérente dans toute votre application.

La propriété `children` est une propriété spéciale qui représente le contenu rendu à l'intérieur du composant `RootLayout`. Cela vous permet d'imbriquer d'autres composants et contenu dans la mise en page partagée.

Enfin, vous exportez le composant `RootLayout`, le rendant disponible pour une utilisation dans toute votre application.

## Comment créer une barre de navigation personnalisée dans Next.js

Dans cette section, vous allez créer un composant de barre de navigation simple pour votre application. La barre de navigation inclura un logo et un lien qui emmène les utilisateurs à la section quiz. Ouvrez `components/Navigation.jsx` et ajoutez le code suivant :

```jsx
// 📁 components/Navigation.jsx

export const Navigation = () => {
  return (
    <div className="sticky top-0 backdrop-blur-xl bg-[rgba(0,0,0,0.8)] border-b border-slate-800 z-50">
      <Container className="flex justify-between py-5">
        <Link href="/">
          <Image src="/logo.png" alt="Family Guy" width={70} height={50} />
        </Link>
        <Link
          href="/quiz"
          className="flex items-center justify-center gap-1 px-5 font-semibold text-black transition-colors bg-green-500 rounded-md duration-600 hover:bg-green-600"
        >
          <TbArrowBigRightFilled className="text-lg" />
          Faire un Quiz
        </Link>
      </Container>
    </div>
  )
}

```

Vous avez maintenant un composant `Navigation` collant qui est partagé dans toute l'application. Si vous ouvrez votre serveur local, vous devriez pouvoir voir le résultat suivant :

![Aperçu de la barre de navigation collante](https://www.freecodecamp.org/news/content/images/2023/05/image-88.png)
_Aperçu de la barre de navigation collante_

Félicitations pour vos progrès jusqu'à présent ! Vous avez réussi à créer une mise en page partagée avec une barre de navigation pour votre application Next.js. Cette mise en page partagée assure la cohérence sur toutes les pages, facilitant la gestion des éléments comme la barre de navigation dans toute votre application.

Maintenant, il est temps de se concentrer sur la construction de la page d'accueil pour afficher les personnages. Pour afficher les personnages sur la page d'accueil, vous devez créer une route API qui récupère tous les personnages de votre fichier JSON local, vous permettant de peupler dynamiquement la page d'accueil avec les informations pertinentes.

## Comment créer une route API dans Next.js

Le routage dans Next.js est un concept fondamental qui détermine comment différentes parties de votre application sont accessibles. Lorsque vous créez un dossier à l'intérieur du répertoire `app` dans Next.js, il devient automatiquement une route. Mais vous avez la flexibilité de définir s'il doit s'agir d'une route UI ou d'une route API.

Nommer le fichier à l'intérieur du dossier de route `page.jsx` le transforme en une route UI. Cela signifie qu'il servira de page régulière avec des composants UI. En revanche, si vous nommez le fichier `route.js`, il devient une route API. Cela signifie qu'il gérera les requêtes et réponses API.

Il est important de garder à l'esprit que dans un seul répertoire, vous pouvez avoir soit une route UI, soit une route API, mais pas les deux. Cette séparation claire permet une structure propre et organisée lors de la construction de votre application Next.js.

Dans la section suivante, vous allez créer votre première route API dans Next.js. Les routes API dans Next.js fournissent un moyen simple et pratique de créer des endpoints côté serveur au sein de votre application.

Avec les routes API, vous pouvez définir des routes personnalisées qui gèrent les requêtes et réponses HTTP, vous permettant de récupérer ou modifier des données, d'effectuer des calculs côté serveur ou de vous intégrer à des services externes.

Ces routes sont écrites sous forme de fonctions JavaScript qui sont automatiquement déployées en tant que fonctions serverless dans le cloud. Les routes API fournissent une fonctionnalité de type backend au sein de votre application frontend Next.js, vous permettant de construire des applications web dynamiques et interactives sans avoir besoin d'un serveur séparé.

## Comment construire la page d'accueil

Dans cette section, vous allez créer une route API qui vous permettra de récupérer tous les personnages disponibles stockés dans le fichier JSON local. En implémentant cette route API, vous pourrez récupérer et afficher les personnages sur la page d'accueil de votre application.

### Comment créer la route API des personnages

Afin d'assurer une séparation claire entre votre code API et votre code UI, vous allez héberger toutes vos routes API dans le répertoire `app/api`.

En adoptant cette approche, vous pouvez isoler efficacement la fonctionnalité liée à l'API de votre interface utilisateur, favorisant ainsi une meilleure organisation et maintenabilité.

Cette section vous guidera à travers le processus de création de la route API des personnages. Ouvrez simplement le fichier `app/api/characters/route.js` et ajoutez le code suivant :

```js
// 📁 app/api/characters/route.js

export async function GET() {
  return NextResponse.json({ characters: characters.data })
}
```

Dans cet extrait de code, vous importez un fichier JSON appelé `characters.json`. Ce fichier contient des données sur les personnages que vous souhaitez utiliser dans votre application.

Ensuite, vous importez l'objet `NextResponse` du module `next/server`. Cet objet fournit des fonctions pour gérer les réponses du serveur dans une application Next.js.

Après cela, vous définissez une fonction asynchrone appelée `GET()`. Cette fonction est associée à la méthode de requête HTTP GET, qui est couramment utilisée pour récupérer des données d'un serveur.

À l'intérieur de la fonction `GET()`, vous utilisez la fonction `NextResponse.json()` pour construire la réponse du serveur. Vous passez un objet avec une propriété appelée `characters`, qui contient les données du fichier `characters.json`. Cette réponse est ensuite retournée par la fonction.

En termes plus simples, ce code crée une route API qui répond aux requêtes GET. Lorsqu'une requête GET est faite à cette route, elle retourne une réponse JSON contenant les données du fichier `characters.json`. Cela vous permet de récupérer les données des personnages depuis votre application et de les utiliser dans d'autres parties de notre code.

Maintenant, il est temps de tester votre route API et de vous assurer que tout fonctionne correctement. Pour simplifier ce processus, vous allez utiliser le navigateur lui-même pour faire la requête API. Ouvrez votre navigateur et entrez l'URL suivante : [http://localhost:3000/api/characters](http://localhost:3000/api/characters).

En faisant cela, vous serez dirigé vers une page où vous pourrez observer les résultats de la requête API. Cette étape nous permet de vérifier que la route API fonctionne comme prévu et qu'elle récupère avec succès les données des personnages :

![Données JSON dans le navigateur](https://www.freecodecamp.org/news/content/images/2023/05/image-89.png)
_Données JSON dans le navigateur_

Voici les données JSON qui contiennent la liste des personnages. Si les données JSON semblent étranges dans votre navigateur, assurez-vous d'installer une extension de formateur JSON sur votre navigateur. J'utilise Google Chrome, donc j'utilise [ce formateur JSON](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa) sur mon navigateur.

### Comment afficher les personnages sur la page d'accueil

Maintenant que vous avez configuré votre API, créons l'interface utilisateur pour notre page d'accueil et affichons les personnages. Pour ce faire, ouvrez le fichier `app/page.jsx` et ajoutez l'extrait de code suivant :

```jsx
// 📁 app/page.jsx

async function getAllCharacters() {
  const data = await fetch(`${endpoint}/characters`)

  if (!data.ok) {
    throw new Error('Échec de la récupération des données')
  }

  return data.json()
}

export default async function Page() {
  const data = await getAllCharacters()

  return (
    <main>
      <Container className="grid grid-cols-2 gap-1 py-5 md:grid-cols-3 lg:grid-cols-4">
        {data?.characters?.map(item => {
          return (
            <Link
              href={`/characters/${item.slug}`}
              key={item.name}
              className="overflow-hidden rounded-md"
            >
              <Image
                src={item.avatar}
                alt=""
                className="transition-all duration-500 hover:scale-110 hover:-rotate-2"
                width={500}
                height={500}
              />
            </Link>
          )
        })}
      </Container>
    </main>
  )
}

```

Dans l'extrait de code ci-dessus, vous avez un composant React appelé `Page` qui est défini comme une fonction asynchrone. Ce composant est responsable du rendu de l'interface utilisateur de la page d'accueil.

Tout d'abord, vous avez une fonction asynchrone appelée `getAllCharacters` qui utilise la fonction "fetch" pour faire une requête HTTP asynchrone à l'endpoint de l'API. La réponse de cette requête est stockée dans la variable `data`.

Ensuite, vous avez une vérification de gestion des erreurs. Si la réponse HTTP a retourné une erreur (code de statut autre que 200), nous lançons une erreur indiquant que la récupération des données a échoué.

Passons au composant `Page`, il attend le résultat de l'appel de la fonction `getAllCharacters`. Les données résultantes sont stockées dans la variable `data`.

L'instruction return rend l'interface utilisateur de la page d'accueil. Elle utilise une balise `main` comme conteneur de niveau supérieur et un composant `Container` pour contenir une mise en page de grille avec plusieurs colonnes.

À l'intérieur du `Container`, vous mappez sur le tableau `characters` dans l'objet `data` et générez une liste d'éléments. Pour chaque personnage, nous créons un composant "Link" qui sert de lien cliquable vers une page spécifique du personnage. L'URL du lien est générée en fonction de la propriété slug du personnage.

À l'intérieur du `Link`, vous avez un composant `Image` qui affiche l'image de l'avatar du personnage.

Dans l'ensemble, ce code récupère des données d'un endpoint d'API, spécifiquement des données de personnage. Il utilise ensuite ces données pour rendre dynamiquement une mise en page de grille d'avatars de personnages avec des liens cliquables vers les pages individuelles des personnages.

![Page d'accueil de l'application affichant une liste de personnages de Family Guy](https://www.freecodecamp.org/news/content/images/2023/05/image-90.png)
_Page d'accueil_

Votre page d'accueil a maintenant l'air fantastique, mais vous avez peut-être remarqué quelque chose d'inhabituel dans la manière dont nous avons récupéré les données. Typiquement, vous pourriez être familier avec l'utilisation du hook useEffect pour récupérer des données d'une API. Mais dans ce cas, vous n'avez utilisé aucun hook – pourtant votre code fonctionne parfaitement.

Dans la section suivante, nous allons examiner de plus près ce qui s'est exactement passé dans ce composant. En examinant le code et son exécution, vous allez acquérir une compréhension plus approfondie des mécanismes de Next.js.

## Qu'est-ce que le routeur d'application dans Next.js ?

Le routeur d'application dans Next.js introduit un nouveau paradigme pour le développement d'applications en tirant parti des dernières fonctionnalités de React. Si vous êtes déjà familier avec Next.js, vous découvrirez que le routeur d'application représente une évolution naturelle du routeur de pages existant, qui est basé sur le système de fichiers.

Le routeur d'application permet essentiellement d'exécuter du code React sur le serveur par défaut, donc vous récupérez des données sur le serveur et ne retournez que le HTML statique au client. Cela signifie que nous avons un **composant serveur** qui récupère des données du serveur et rend son contenu côté serveur.

Il y a un point à considérer : vous n'aurez pas accès aux fonctionnalités côté client comme l'état React et les hooks React à l'intérieur des **composants serveur**, puisque ils ne s'exécutent que sur le serveur.

Si vous voulez utiliser des fonctionnalités côté client, vous devez spécifier cela dans votre fichier de composant en ajoutant `"use client"` en haut du fichier.

### Quel est l'intérêt du rendu côté serveur dans Next.js ?

Dans Next.js, le SSR permet au serveur de générer le contenu HTML d'une page web et de l'envoyer au navigateur. Cela signifie que lorsque vous visitez un site web Next.js, vous n'avez pas à attendre que le code JavaScript se charge et s'exécute sur le navigateur avant de voir un quelconque contenu. Au lieu de cela, le serveur envoie une page HTML pré-rendue, qui peut être affichée presque instantanément.

L'avantage du SSR est qu'il améliore le temps de chargement initial d'une page web, offrant une expérience utilisateur plus rapide et plus fluide. Il aide également au référencement (SEO) car les moteurs de recherche peuvent facilement explorer et indexer le contenu HTML rendu par le serveur.

### Méthodes de rendu côté serveur dans Next.js

Next.js fournit plusieurs méthodes pour rendre les pages. Chacune de ces méthodes sert un objectif spécifique et peut être utilisée dans différents scénarios :

* **Génération de site statique (SSG) :** La génération statique est une méthode de rendu côté serveur où Next.js génère du HTML au moment de la construction. Pendant le processus de construction, Next.js récupère des données depuis des API ou d'autres sources de données et pré-rend les pages HTML. Ces pages pré-rendues peuvent ensuite être servies au client à la demande. La SSG est adaptée aux sites web dont le contenu ne change pas fréquemment.
* **Rendu côté serveur (SSR) :** Le rendu côté serveur est une autre méthode où Next.js génère du HTML à chaque requête. Lorsqu'un utilisateur visite une page, Next.js récupère les données et rend le HTML sur le serveur avant de l'envoyer au client. Le SSR est utile pour les sites web avec du contenu fréquemment mis à jour ou des expériences utilisateur personnalisées.
* **Régénération statique incrémentielle (ISR) :** L'ISR est une fonctionnalité de Next.js qui vous permet de générer des pages de manière statique à la demande, plutôt qu'au moment de la construction. Cela signifie que votre site peut être à la fois généré de manière statique et dynamique en même temps.

Maintenant que nous avons une meilleure compréhension du rendu côté serveur dans Next.js, nous pouvons passer à la section suivante.

## Comment améliorer la modularité et la maintenabilité de votre base de code Next.js

Afin d'éviter la répétition de code et d'améliorer la réutilisabilité du code, vous pouvez adopter une approche modulaire dans votre projet Next.js. En isolant les fonctions couramment utilisées comme `getAllCharacters` dans un module séparé, vous pouvez y accéder et les réutiliser facilement dans plusieurs parties de votre base de code.

Vous pouvez apporter une petite modification à votre projet. Tout d'abord, accédez au fichier `app/page.jsx` et localisez la fonction `getAllCharacters` en haut. Coupez cette fonction du fichier.

Ensuite, ouvrez le fichier `lib/characters.js` et exportez la fonction `getAllCharacters` depuis ce fichier. En déplaçant la fonction vers un module séparé, vous pouvez facilement l'importer et l'utiliser dans différentes parties de votre base de code :

```js
// 📁 lib/characters.js

import { endpoint } from '@/utils/endpoint'

export async function getAllCharacters() {
  const data = await fetch(`${endpoint}/characters`)

  if (!data.ok) {
    throw new Error('Échec de la récupération des données')
  }

  return data.json()
}

```

Maintenant, importons la fonction `getAllCharacters` depuis `lib/characters.js` et utilisons-la dans `app/page.jsx` :

```jsx
// 📁 app/page.jsx

import { getAllCharacters } from '@/lib/characters'

export default async function Page() {
  const data = await getAllCharacters()

  return (
    <main>
       //contenu ici ...
    </main>
  )
}
```

De cette façon, vous aurez accès à cette fonction de récupération dans toute votre base de code.

## Comment créer une page de personnage dynamique

Félicitations pour être arrivé à ce stade du tutoriel ! À ce stade, vous avez acquis une solide compréhension des bases de Next.js.

Dans cette section, vous allez créer une route API dynamique. Cette route vous permettra de récupérer des données pour chaque personnage individuellement et ensuite de construire une interface utilisateur (UI) pour présenter ces personnages à vos utilisateurs.

### Comment créer des routes API dynamiques dans Next.js

En créant une route API dynamique dans Next.js, vous pouvez récupérer des données de personnage en fonction du slug du personnage. Pour ce faire, vous devez utiliser des crochets pour nommer vos dossiers, indiquant à Next.js qu'il s'agit d'une route dynamique. En nommant les dossiers de manière appropriée, vous pouvez accéder à cette valeur dynamique dans votre code, ce qui vous permet de récupérer et d'afficher les données du personnage souhaité.

Ouvrez `api/characters/[slug]/route.js` et ajoutez l'extrait suivant :

```js
// 📁 api/characters/[slug]/route.js 

export async function GET(req, { params }) {
  try {
    const character = characters.data.find(item => item.slug === params.slug)

    if (!character) {
      return new NextResponse('non trouvé', { status: 404 })
    }

    const character_qoutes = qoutes.data.filter(
      item => item.character_id === character.id,
    )

    return NextResponse.json({
      character,
      character_qoutes: character_qoutes.length > 0 ? character_qoutes : null,
    })
  } catch (error) {
    return new NextResponse('Erreur interne du serveur', { status: 500 })
  }
}
```

Dans l'extrait de code ci-dessus, vous avez une fonction asynchrone nommée `GET` qui gère une requête GET dans une route API Next.js. Décomposons cela étape par étape :

1. Vous importez les données `characters` et `quotes` depuis leurs fichiers JSON respectifs en utilisant le système de fichiers Next.js (`@/data/characters.json` et `@/data/quotes.json`).
2. La fonction reçoit deux paramètres : `req` (représentant la requête entrante) et un objet appelé `params` qui contient les paramètres dynamiques extraits de l'URL de la requête.
3. Dans un bloc try-catch, le code tente de trouver un personnage dans les données `characters` en comparant le paramètre `slug` de `params` avec la propriété `slug` de chaque objet personnage.
4. Si aucun personnage n'est trouvé, le code retourne une réponse "non trouvé" avec un code de statut 404 en utilisant la classe `NextResponse` du package `next/server`.
5. Si un personnage est trouvé, le code procède au filtrage du tableau de données `quotes` en fonction de la propriété `character_id` correspondant à l'`id` du personnage trouvé.
6. Les citations de personnages filtrées sont assignées à la variable `character_quotes`.
7. Enfin, le code retourne une réponse JSON en utilisant `NextResponse.json()`, incluant l'objet `character` et le tableau `character_quotes` (ou `null` si aucune citation n'est trouvée).

Next.js extrait automatiquement les paramètres dynamiques de l'URL et les rend disponibles dans l'objet `params`. Dans ce code, vous accédez au paramètre `slug` en utilisant `params.slug`. Cela vous permet de récupérer le slug spécifique du personnage depuis l'URL et de l'utiliser pour trouver le personnage correspondant dans les données `characters`.

Vous pouvez maintenant tester ce point de terminaison pour voir le résultat, ouvrez [http://localhost:3000/api/characters/peter-griffin](http://localhost:3000/api/characters/peter-griffin) dans votre navigateur et vous devriez pouvoir voir les données JSON suivantes :

![Données JSON dans le navigateur](https://www.freecodecamp.org/news/content/images/2023/05/image-91.png)
_Données JSON dans le navigateur_

### Comment créer des routes UI dynamiques dans Next.js

Maintenant que votre API est configurée et capable de récupérer les données des personnages, il est temps de créer une page UI dynamique pour présenter ces données.

Le processus de création d'une page UI dynamique est assez similaire à ce que vous avez fait lors de la configuration de la route API dynamique. Mais cette fois, vous allez utiliser `page.jsx` au lieu de `route.js` pour générer une route UI.

Ouvrez `app/characters/[slug]/page.jsx` et ajoutez l'extrait suivant :

```jsx
// 📁 app/characters/[slug]/page.jsx

import { getAllCharacters } from '@/lib/characters'

export const dynamicParams = false

export async function generateStaticParams() {
  const { characters } = await getAllCharacters()
  return characters.map(character => ({ slug: character.slug }))
}

export async function getCharacterBySlug(slug) {
  const data = await fetch(`${endpoint}/characters/${slug}`)

  if (!data.ok) {
    throw new Error('Échec de la récupération des données')
  }

  return data.json()
}

export default async function Page({ params }) {
  const { character, character_qoutes } = await getCharacterBySlug(params.slug)

  return (
    <Container className="flex flex-col gap-5 py-5" as="main">
      <div className="flex flex-col gap-2">
        <h1 className="text-2xl font-semibold capitalize">{character.name}</h1>
        <ul className="flex gap-1 text-sm">
          {character.occupations.map(item => {
            return (
              <li
                key={item}
                className="p-2 text-gray-300 bg-gray-800 rounded-md"
              >
                {item}
              </li>
            )
          })}
        </ul>
      </div>
      <p className="text-sm leading-6">{character.description}</p>
      <ul className="grid gap-2 sm:grid-cols-2">
        {character.images.map(image => {
          return (
            <li
              key={image}
              className="relative flex overflow-hidden bg-gray-900 rounded-xl"
            >
              <Image
                className="transition-all duration-500 hover:scale-110 hover:rotate-2"
                src={image}
                alt=""
                width={760}
                height={435}
              />
            </li>
          )
        })}
      </ul>
      {character.skills && (
        <>
          <h2 className="text-xl font-bold">Pouvoirs et Compétences</h2>
          <ul className="flex flex-wrap gap-1">
            {character.skills.map(item => {
              return (
                <li
                  className="flex justify-center flex-grow px-2 py-1 text-orange-400 rounded-full bg-orange-950"
                  key={item}
                >
                  {item}
                </li>
              )
            })}
          </ul>
        </>
      )}
      {character_qoutes && (
        <>
          <h2 className="text-xl font-bold">Citations Célèbres</h2>
          <ul className="grid gap-5">
            {character_qoutes.map((item, idx) => {
              return (
                <li
                  className="p-2 italic text-gray-400 border-l-4 border-green-400 rounded-md"
                  key={item.idx}
                >
                  {item.qoute}
                </li>
              )
            })}
          </ul>
        </>
      )}
    </Container>
  )
}

```

Ne soyez pas intimidé par la longueur du code que vous voyez ici ! Cela peut sembler écrasant au premier abord, mais c'est en fait assez simple. Examinons de plus près ce que nous avons fait dans ce code :

### Qu'est-ce que `generateStaticParams` dans Next.js ?

Dans Next.js, la fonction `generateStaticParams` est utilisée pour spécifier les routes dynamiques qui doivent être pré-rendues au moment de la construction.

Pour l'expliquer en termes plus simples, imaginons que vous avez un site web avec plusieurs articles de blog, et chaque article de blog a une URL unique. Avec `generateStaticParams`, vous pouvez dire à Next.js quelles URL d'articles de blog doivent être générées et pré-rendues pendant le processus de construction.

Lorsque vous implémentez `generateStaticParams`, vous lui fournissez une fonction qui retourne un tableau d'objets représentant les chemins dynamiques que vous souhaitez pré-rendre.

Chaque objet contient généralement un paramètre qui correspond à la partie dynamique de l'URL. Par exemple, si vos articles de blog ont des URL comme `/blog/post-1`, `/blog/post-2`, et ainsi de suite, vous retournerez un tableau avec des objets comme `{ params: { slug: 'post-1' } }`, `{ params: { slug: 'post-2' } }`, et ainsi de suite.

Dans notre cas, nous récupérons une liste de personnages en utilisant la fonction `getAllCharacters()`. Ensuite, nous mappons sur les personnages et retournons un tableau d'objets, chacun contenant une propriété `slug` avec la valeur du slug du personnage.

Next.js utilisera ensuite ces informations pour générer les fichiers HTML statiques pour ces chemins pendant le processus de construction. Cela permet aux pages d'être servies en tant que fichiers statiques, améliorant les performances et le référencement.

### À quoi sert `dynamicParams` lors de la génération de pages statiques dans Next.js ?

Dans Next.js, le comportement des segments dynamiques qui n'ont pas été générés en utilisant `generateStaticParams` est contrôlé par `dynamicParams`.

Lorsque `dynamicParams` est défini sur `true`, Next.js tentera de récupérer la page correspondante de manière dynamique lorsqu'un segment dynamique est visité.

En revanche, si `dynamicParams` est défini sur `false`, Next.js retournera une page 404 s'il ne parvient pas à trouver la page demandée.

Ce paramètre vous permet de définir comment Next.js gère les segments dynamiques qui n'ont pas été pré-générés, offrant ainsi une flexibilité dans la gestion des routes dynamiques dans vos applications.

### Comment générer des pages statiques avec `generateStaticParams`

Maintenant que vous avez généré avec succès un chemin statique pour chaque personnage, voyons comment vous pouvez récupérer des données pour chaque personnage.

La fonction `getCharacterBySlug` est une fonction asynchrone qui prend le paramètre `slug`, récupère des données depuis l'endpoint de l'API spécifié en utilisant `fetch`, et retourne les données de réponse au format JSON. Si la réponse n'est pas réussie (`!data.ok`), une erreur est lancée.

Le composant `Page` reçoit l'objet `params` en tant que prop, qui contient les valeurs des paramètres dynamiques extraits de l'URL. Il appelle la fonction `getCharacterBySlug`, en passant le slug du personnage extrait de `params` pour récupérer les données spécifiques du personnage.

Les données retournées sont ensuite utilisées pour remplir l'interface utilisateur, qui inclut l'affichage du nom du personnage, de ses occupations, de sa description, de ses images, de ses pouvoirs et compétences (si disponibles), et de ses citations célèbres (si disponibles).

Idéalement, vous pouvez mettre `getCharacterBySlug` dans `lib/characters.js` et l'exporter depuis là, mais c'est à vous de décider !

![Application Family Guy avec des routes dynamiques](https://www.freecodecamp.org/news/content/images/2023/05/ezgif-5-035df8a17a-1.gif)
_Notre application jusqu'à présent_

## Comment construire la section Quiz

Félicitations pour être arrivé à ce stade du tutoriel ! Vous avez accompli beaucoup de choses en créant des routes API et UI dynamiques, et en comprenant les différentes méthodes de rendu dans Next.js.

Maintenant, ajoutons une touche d'interactivité à cette application. Dans cette section, vous allez construire une section quiz engageante où les utilisateurs pourront tester leurs connaissances sur Family Guy.

### Comment créer une route API pour récupérer des questions aléatoires

Pour garantir une expérience excitante et unique pour chaque utilisateur, il est important d'éviter de répéter la même question dans le quiz à chaque fois. Nous voulons garder les choses fraîches et engageantes.

Pour y parvenir, nous allons mettre en place un mécanisme qui présente aux utilisateurs différentes questions à chaque fois qu'ils commencent le quiz.

Ouvrez `app/api/quiz/random/route.js` et ajoutez l'extrait suivant :

```js
// 📁 app/api/quiz/random/route.js

export async function GET() {
  try {
    const random = Math.floor(Math.random() * questions.data.length)
    return NextResponse.json({
      randomQuestion: questions.data[random].id,
    })
  } catch (error) {
    return new NextResponse('Erreur interne du serveur', { status: 500 })
  }
}

```

Dans cette route API Next.js, vous implémentez la logique pour récupérer une question aléatoire à partir d'un ensemble de questions stockées dans un fichier JSON appelé `quiz.json`. Tout d'abord, nous importons les données `questions` du fichier JSON et l'objet `NextResponse` du package serveur Next.js.

À l'intérieur de la fonction `GET`, nous générons un nombre aléatoire en utilisant les fonctions `Math.random()` et `Math.floor()`. Ce nombre est utilisé pour sélectionner une question aléatoire à partir du tableau `questions.data`. Nous récupérons la question en utilisant son index, et spécifiquement la propriété `id` de la question sélectionnée aléatoirement.

Maintenant, créons une interface utilisateur pour utiliser cette question aléatoire.

### Comment créer une page d'introduction pour le Quiz

Vous allez maintenant créer une interface utilisateur (UI) pour la section d'introduction du quiz. Cette UI servira d'écran initial que les utilisateurs voient avant de commencer le quiz.

Vous allez utiliser la route API que vous venez de créer pour rediriger dynamiquement les utilisateurs vers une nouvelle question à chaque fois qu'ils commencent le quiz.

Ouvrons `app/quiz/page.jsx` et ajoutons le code suivant :

```jsx
// 📁 app/quiz/page.jsx

export async function getRandomQuizQuestion() {
  const data = await fetch(`${endpoint}/quiz/random`, { cache: 'no-store' })

  if (!data.ok) {
    throw new Error('Échec de la récupération des données')
  }

  return data.json()
}

export default async function Page() {
  const data = await getRandomQuizQuestion()

  return (
    <Container
      as="main"
      className="flex flex-col gap-5 py-5 md:flex-row-reverse md:justify-between"
    >
      <div className="relative overflow-hidden rounded-2xl">
        <div className="md:w-[24rem]">
          <Image src="/wallpaper.jpg" alt="" width={700} height={700} />
        </div>
        <div className="absolute top-0 bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent md:bg-gradient-to-r"></div>
      </div>

      <div className="md:w-[50%] flex flex-col gap-5">
        <h1 className="text-2xl font-semibold">Quiz Family Guy</h1>
        <p className="text-sm leading-6 text-gray-300">
          Faites ce quiz pour découvrir combien vous en savez sur la sitcom animée à succès Family Guy. Testez vos connaissances sur les personnages, les
          épisodes, et les nombreuses références à la culture pop de la série.
        </p>
        <Link
          href={`/quiz/${data.randomQuestion}`}
          className="flex items-center justify-center gap-1 px-5 py-4 font-semibold text-orange-500 transition-colors rounded-md outline duration-600 hover:bg-orange-950"
        >
          <TbArrowBigRightFilled className="text-lg" />
          Faire un Quiz Maintenant !
        </Link>
      </div>
    </Container>
  )
}

```

Ce code configure l'interface utilisateur pour la section d'introduction du quiz, récupère une question aléatoire de l'API, et fournit un bouton pour que les utilisateurs commencent le quiz.

Dans ce code, vous avez peut-être remarqué un changement où nous passons un paramètre à la méthode `fetch` : `{ cache: 'no-store' }`.

Ce changement est significatif car il garantit que la page sur laquelle nous travaillons ne sera pas générée de manière statique en utilisant la méthode de génération de site statique (SSG). Au lieu de cela, elle effectuera une requête API à l'endpoint fourni et récupérera des données fraîches à chaque fois que les utilisateurs visitent la page.

En utilisant `{ cache: 'no-store' }`, nous désactivons la mise en cache pour cette requête spécifique. Cela garantit que chaque fois qu'un utilisateur accède à cette page, une nouvelle question sera récupérée.

Cette approche ajoute un élément dynamique et interactif à l'expérience du quiz, garantissant que les utilisateurs rencontrent toujours une question différente à chaque fois qu'ils visitent la page.

![Une page d'introduction pour la section quiz de Family Guy](https://www.freecodecamp.org/news/content/images/2023/05/image-93.png)
_Page d'introduction du quiz_

### Comment créer une route API dynamique pour les questions du quiz

Pour fournir des questions de quiz dynamiques, vous devez créer une nouvelle route API qui récupérera et retournera les questions du quiz. De cette façon, vous pouvez récupérer les questions de manière dynamique et les présenter aux utilisateurs.

Ouvrez `app/api/quiz/[id]` et ajoutez le code suivant :

```js
// 📁 app/api/quiz/[id]

export async function GET(req, { params }) {
  try {
    const question = questions.data.find(item => item.id === params.id)

    if (!question) {
      return new NextResponse('non trouvé', { status: 404 })
    }

    const { correct_answer, ...rest } = question

    return NextResponse.json({
      question: rest,
    })
  } catch (error) {
    return new NextResponse('Erreur interne du serveur', { status: 500 })
  }
}

```

Dans cette route Next.js, vous gérez une requête GET pour récupérer une question spécifique d'un quiz. Vous importez les données `questions` depuis un fichier JSON. En utilisant l'ID fourni dans les paramètres de la requête, vous recherchez une question correspondante. Si la question n'est pas trouvée, vous retournez une réponse "Non trouvé" avec un code de statut 404.

Si la question est trouvée, vous extrayez la bonne réponse et stockez les détails restants de la question dans la variable `rest`.

Enfin, vous retournez une réponse JSON contenant les détails de la question (à l'exclusion de la bonne réponse). Si des erreurs se produisent pendant le processus, vous retournez une réponse "Erreur interne du serveur" avec un code de statut 500.

Vous pouvez maintenant tester cette route API dans votre navigateur en ouvrant votre serveur local [http://localhost:3000/api/quiz/CfQnf3lH56](http://localhost:3000/api/quiz/CfQnf3lH56) :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-94.png)
_http://localhost:3000/api/quiz/CfQnf3lH56_

### Comment créer une route API dynamique pour récupérer les réponses

Avant d'implémenter l'interface utilisateur, créons une route API où vous pourrez récupérer la bonne réponse pour chaque question.

Ouvrez `app/api/quiz/answer/[id]/route.js` et ajoutez le code suivant :

```jsx
// 📁 app/api/quiz/answer/[id]/route.js

export async function GET(req, { params }) {
  try {
    const question = questions.data.find(item => item.id === params.id)

    if (!question) {
      return new NextResponse('non trouvé', { status: 404 })
    }

    const { correct_answer } = question

    const filteredQuestions = questions.data.filter(
      item => item.id !== params.id,
    )
    const random = Math.floor(Math.random() * filteredQuestions.length)

    return NextResponse.json({
      correct: correct_answer,
      random: filteredQuestions[random].id,
    })
  } catch (error) {
    return new NextResponse('Erreur interne du serveur', { status: 500 })
  }
}

```

Le but de cette route API est de récupérer une question spécifique d'un quiz en fonction de l'ID fourni. Le code recherche la question en comparant l'ID donné avec les ID des questions stockées dans les données `questions`. Si la question demandée est trouvée, sa bonne réponse est extraite.

Pour suggérer la question suivante, le code retire la question actuelle du pool de questions disponibles en la filtrant. Il génère ensuite un index aléatoire dans la plage des questions restantes. En utilisant cet index aléatoire, une nouvelle question est sélectionnée comme suggestion pour la question suivante.

Le code construit et retourne une réponse JSON contenant la bonne réponse pour la question demandée et l'ID de la question suivante choisie aléatoirement. Cette fonctionnalité permet aux utilisateurs de récupérer des questions de quiz spécifiques et de recevoir des suggestions pour la question suivante, améliorant ainsi l'expérience interactive du quiz.

### Comment créer des routes UI dynamiques pour les questions du Quiz

Maintenant que vous avez construit avec succès tous les endpoints API nécessaires, il est temps de passer à l'étape suivante et de créer une interface utilisateur (UI) qui permet aux utilisateurs d'interagir avec les API que vous avez développées. Cette UI servira de passerelle pour les utilisateurs afin d'accéder et d'utiliser les fonctionnalités offertes par vos API.

Dans cette section, vous allez apprendre le rendu côté serveur dynamique (SSR) dans Next.js. Nous avons déjà couvert les pages statiques (SSG), et maintenant vous allez explorer le SSR. De plus, le SSR est beaucoup plus facile à implémenter.

Ouvrez `app/quiz/[id]/page.jsx` et ajoutez le code suivant :

```jsx
// 📁 app/quiz/[id]/page.jsx

async function getQuizQuestion(id) {
  const data = await fetch(`${endpoint}/quiz/${id}`)

  if (!data.ok) {
    throw new Error('Échec de la récupération des données')
  }

  return data.json()
}


export default async function Page({ params }) {
  const { question } = await getQuizQuestion(params.id)

  return (
    <Container as="main" className="flex flex-col gap-5 py-5">
      <h1 className="text-lg font-semibold">{question.title}</h1>
      <Answer answers={question.answers} questionId={params.id} />
    </Container>
  )
}

```

Ce composant de page Next.js récupère les données de la question depuis un endpoint API en utilisant la fonction `getQuizQuestion`. Il rend ensuite le titre de la question et les réponses correspondantes en utilisant des composants JSX.

![Route UI Next.js qui affiche la question dynamique](https://www.freecodecamp.org/news/content/images/2023/05/image-96.png)
_Route UI de la question_

C'est tout ce que vous deviez faire pour rendre une page Next.js côté serveur !

Dans la section suivante, vous allez créer un composant côté client pour gérer l'interaction de l'utilisateur avec les réponses.

### Comment créer un composant côté client dans Next.js

Dans la section finale de ce tutoriel, vous allez créer un composant côté client pour gérer les interactions d'un utilisateur avec les réponses.

Ouvrez `components/Answer.jsx` et ajoutez le code suivant :

```jsx
// 📁 components/Answer.jsx

'use client'

import { useEffect, useState } from 'react'
import cn from 'classnames'
import Link from 'next/link'
import { FiRepeat } from 'react-icons/fi'
import { MdNearbyError } from 'react-icons/md'
import { FaCheck } from 'react-icons/fa'

export const Answer = ({ answers, questionId }) => {
  const [selected, setSeleceted] = useState(null)
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    let subscribed = true
    if (selected) {
      setLoading(true)
      fetch(`/api/quiz/answer/${questionId}`)
        .then(res => res.json())
        .then(data => {
          setLoading(false)
          if (subscribed) {
            setData(data)
          }
        })
    }

    return () => {
      console.log('annulé !')
      subscribed = false
    }
  }, [questionId, selected])

  return (
    <>
      <ul className="grid grid-cols-2 gap-2 md:grid-cols-4">
        {answers.map(item => {
          const isLoading = selected === item && loading
          const isWrong =
            selected === item && data && data?.correct !== selected
          const isCorrect = data?.correct === item

          return (
            <li key={item}>
              <button
                disabled={data || loading}
                onClick={() => setSeleceted(item)}
                className={cn(
                  'p-2 rounded-md  items-center justify-between w-full flex text-sm font-semibold disabled:cursor-not-allowed transition-all',
                  isLoading && 'animate-pulse',
                  isWrong ? 'bg-red-700' : 'bg-slate-800',
                  isCorrect && 'outline text-green-500',
                )}
              >
                {item}
                {isCorrect && <FaCheck />}
                {isWrong && <MdNearbyError />}
              </button>
            </li>
          )
        })}
      </ul>
      {data?.random && (
        <Link
          href={`/quiz/${data.random}`}
          className="flex items-center gap-1 text-blue-400"
        >
          <FiRepeat className="mt-1" />
          Recommencer
        </Link>
      )}
    </>
  )
}
```

Il s'agit d'un composant React qui prend deux props : `answers` et `questionId`. Il configure l'état en utilisant le hook `useState` pour suivre la réponse sélectionnée, les données récupérées et le statut de chargement.

À l'intérieur du composant, il y a un hook `useEffect` qui s'exécute chaque fois que la valeur `questionId` ou `selected` change. Si une réponse `selected` existe, il effectue une requête API pour récupérer les données correspondantes en utilisant `fetch` et met à jour l'état en conséquence.

Le composant rend une liste d'options de réponse en utilisant une fonction map. Chaque option de réponse est représentée par un bouton. L'apparence du bouton est modifiée en fonction de la réponse sélectionnée, du statut de chargement et de l'exactitude de la réponse. Il affiche également différentes icônes, telles qu'une coche ou une icône d'erreur, en fonction de l'exactitude de la réponse sélectionnée.

De plus, si les données récupérées incluent une propriété `random`, un lien est rendu pour répéter le quiz avec une nouvelle question aléatoire.

Voici à quoi ressemble la version finale de notre quiz :

![Version finale du quiz](https://www.freecodecamp.org/news/content/images/2023/05/ezgif-3-0bd6e0e0c5.gif)
_Version finale du quiz_

## Conclusion

Nous voici à la fin ! Vous avez réussi à construire votre première application full-stack en utilisant Next.js. Tout au long de ce tutoriel étape par étape, vous avez appris les bases de Next.js, exploré ses fonctionnalités puissantes et acquis les connaissances nécessaires pour créer des applications web modernes.

Grâce à ce tutoriel, vous n'avez pas seulement construit une application fonctionnelle, mais vous avez également acquis la confiance nécessaire pour commencer à créer vos propres applications full-stack avec Next.js. Vous avez appris le routage, le rendu côté serveur, l'intégration d'API, et bien plus encore.

Maintenant que vous avez une base solide en Next.js, les possibilités sont infinies. Vous pouvez continuer à explorer des sujets avancés, tels que l'intégration de bases de données, l'authentification et le déploiement, pour faire passer vos applications au niveau supérieur.

Vous pouvez me suivre sur [Twitter](https://twitter.com/Yazdun) où je partage plus de conseils utiles sur le développement web. Bon codage !