---
title: Comment construire un blog avec l'API Ghost et Next.js
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2023-04-13T21:14:46.000Z'
originalURL: https://freecodecamp.org/news/build-a-blog-website-with-ghost-api-and-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Ghost-API-and-Nextjs--2-.png
tags:
- name: blog
  slug: blog
- name: Ghost
  slug: ghost-tag
- name: Next.js
  slug: nextjs
seo_title: Comment construire un blog avec l'API Ghost et Next.js
seo_desc: "Ghost CMS is a popular content management system that many devs and companies\
  \ use to host their blogs. \nIt has many features and an editor that's highly optimized\
  \ for writing. You can even build different themes using handlebars.js.\nBut if\
  \ you don't ..."
---

Ghost CMS est un système de gestion de contenu populaire que de nombreux développeurs et entreprises utilisent pour héberger leurs blogs. 

Il possède de nombreuses fonctionnalités et un éditeur hautement optimisé pour l'écriture. Vous pouvez même construire différents thèmes en utilisant **[handlebars](https://handlebarsjs.com/).js**.

Mais si vous ne connaissez pas Handlebars, son apprentissage peut être un processus long et difficile. Si vous êtes déjà un développeur Next.js et que vous ne connaissez pas Handlebars, créer un nouveau thème pour votre site basé sur Ghost peut être difficile.

Dans cet article, je vais vous apprendre à utiliser Ghost CMS comme backend et Next.js comme frontend. Je vais vous guider à travers tout ce qui concerne le [répertoire d'applications Nextjs 13](https://beta.nextjs.org/docs/getting-started) et l'API Ghost CMS. 

L'équipe Next.js 13 travaille actuellement sur le dossier expérimental des applications. Next utilise un routage basé sur les fichiers avec le répertoire `page`. Le nouveau répertoire `app` est basé sur le routage du système de fichiers et fournit des fonctionnalités supplémentaires comme les mises en page, la gestion des erreurs, le chargement des composants, et le rendu côté serveur et côté client, prêts à l'emploi.

Tout le code est disponible sur [GitHub](https://github.com/officialrajdeepsingh/nextjsghostcms). Vous pouvez également consulter le site de démonstration en direct [demo website](https://nextjsghostcms.vercel.app/).

## Table des matières

1. [Pourquoi utiliser Next.js pour le Front End et non un thème Ghost CMS ?](#heading-pourquoi-utiliser-nextjs-pour-le-front-end-et-non-un-theme-ghost-cms)
2. [Exigences du projet](#heading-exigences-du-projet)
3. [Comment configurer Ghost CMS](#heading-comment-configurer-ghost-cms)
4. [Comment configurer Ghost CMS avec le Cloud](#heading-comment-configurer-ghost-cms-avec-le-cloud)
5. [Comment obtenir le modèle de blog](#heading-comment-obtenir-le-modele-de-blog)
6. [Comment configurer Next.js](#heading-comment-configurer-nextjs)
7. [Ce qu'il faut savoir avant de suivre ce tutoriel](#heading-ce-quil-faut-savoir-avant-de-suivre-ce-tutoriel)
8. [Structure des dossiers](#heading-structure-des-dossiers)
9. [Comment configurer Ghost CMS et Next.js](#heading-comment-configurer-ghost-cms-et-nextjs)
10. [Comprendre le dossier d'applications Next.js 13](#heading-comprendre-le-dossier-dapplications-nextjs-13)
11. [Données de démonstration pour le projet](#heading-donnees-de-demonstration-pour-le-projet)
12. [Comment construire le blog](#heading-comment-construire-le-blog)
13. [Comment construire l'en-tête](#heading-comment-construire-len-tete)
14. [Comment construire le pied de page](#heading-comment-construire-le-pied-de-page)
15. [Comment construire la mise en page](#heading-comment-construire-la-mise-en-page) 
16. [Comment construire la page d'accueil](#heading-comment-construire-la-page-daccueil)
17. [Comment construire la page de lecture](#heading-comment-construire-la-page-de-lecture)
18. [Comment construire la page de tag](#heading-comment-construire-la-page-de-tag) 
19. [Comment construire la page d'auteur](#heading-comment-construire-la-page-dauteur)
20. [Comment construire des pages uniques](#heading-comment-construire-des-pages-uniques)
21. [Comment gérer la pagination](#heading-comment-gerer-la-pagination)
22. [SEO Next.js](#heading-nextjs-seo)
23. [Comment activer la recherche](#heading-comment-activer-la-recherche)
24. [Gestion des erreurs](#heading-gestion-des-erreurs)
25. [Comment reconstruire votre site statique avec des webhooks](#heading-comment-reconstruire-votre-site-statique-avec-des-webhooks)
26. [Conclusion](#heading-conclusion)

Dans cet article, nous couvrons les bases du répertoire d'applications expérimental de Next. Ensuite, je vous apprendrai à configurer Next et Ghost CMS localement et comment intégrer Ghost avec Next. Enfin, je vous montrerai comment consommer des données depuis le backend (via l'API Ghost CMS) et les afficher sur le site avec React.js.

## Pourquoi utiliser Next.js pour le Front End et non un thème Ghost CMS ?

Il y a plusieurs raisons pour lesquelles vous pourriez envisager d'utiliser Next comme framework frontend pour votre blog :

1. Ghost CMS ne génère pas de builds statiques, mais Next.js le fait.
2. Vous obtenez une vitesse et des performances accrues du site avec Next.js et il offre désormais un support SEO intégré et d'autres optimisations. Ghost n'a pas certaines de ces fonctionnalités.
3. Pour les développeurs React, il est facile de construire un nouveau blog avec Next (puisque Next est basé sur React), et vous n'avez pas besoin d'apprendre des outils supplémentaires.
4. Vous trouverez quelques fournisseurs de services disponibles pour Ghost pour déployer un blog Ghost en un clic. La plupart d'entre eux viennent avec un plan payant tandis qu'un ou deux offrent un plan gratuit (mais ceux-ci tendent à avoir des limitations de temps et de fonctionnalités). Pour Next.js, de nombreux acteurs sont disponibles sur le marché.

En gros, en ce qui concerne les builds statiques et les performances du site, Ghost ne performe pas aussi bien dans les deux cas. L'alternative est d'utiliser une plateforme frontend comme Next, React, Angular ou Vue.

J'ai choisi Next parce que c'est un framework React très demandé et populaire, et de nombreux outils et bibliothèques sont construits autour de lui. 

Notez que le projet actuel n'est pas prêt pour TypeScript, mais je travaille dessus. À cause de cela, [j'ai désactivé TypeScript pendant le build](https://medium.com/frontendweb/basic-explanation-about-the-next-config-js-file-eaa539e1fea3) comme ceci :

```typescript
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  
  typescript: {
    ignoreBuildErrors: false,
  },
  
}

module.exports = nextConfig

```

## Exigences du projet

Pour suivre ce tutoriel, vous aurez besoin de connaissances de base sur les packages suivants :

1. [PNPM](https://pnpm.io/) est un gestionnaire de packages Node.js similaire à npm ou yarn (vous pouvez utiliser celui que vous préférez).
2. [TypeScript](https://www.typescriptlang.org/) vous aide à écrire du code sécurisé en JavaScript, et peut également aider à améliorer la productivité. Ce n'est pas obligatoire, cependant. Vous pouvez utiliser JavaScript dans votre projet.
3. [React.js](https://react.dev/) est une bibliothèque JavaScript front-end gratuite et open-source pour construire des interfaces utilisateur avec des composants de classe et de fonction.
4. [Next.js 13 (app)](https://beta.nextjs.org/docs/getting-started) est basé sur React et fournit des fonctionnalités supplémentaires comme le routage, la gestion des erreurs et les mises en page.
5. [Ghost CMS API](https://ghost.org/docs/content-api/) est un système de gestion de contenu (CMS) open-source similaire à WordPress. Ghost est spécifiquement conçu et construit pour le blogging. Dans ce projet, nous utiliserons Ghost comme backend et Next comme frontend. Pour la communication entre le développement backend et frontend, nous utiliserons l'API Ghost CMS. 
6. [Tailwind CSS](https://tailwindcss.com/) est un framework basé sur CSS open source similaire à [Bootstrap](https://getbootstrap.com/). Nous utiliserons Tailwind CSS pour concevoir notre site de blog. 

## Comment configurer Ghost CMS

L'étape suivante consiste à installer Ghost localement, ce que vous pouvez faire avec une seule commande. Tout d'abord, vous devez installer `ghost-cli` globalement avec pnpm, yarn ou npm.

```bash
pnpm add -g ghost-cli@latest

# ou

yarn global add ghost-cli@latest

# ou

npm install ghost-cli@latest -g
```

Après avoir installé le CLI Ghost, vous pouvez créer un nouveau projet de blog Ghost localement avec la commande suivante :

```bash
ghost install local
```

Après l'installation du blog, vous pouvez démarrer votre serveur de développement local avec la commande `ghost start` et votre serveur de développement local sur `http://localhost:2368/ghost`.

### Commandes supplémentaires du CLI Ghost

Il y a quelques commandes supplémentaires qui sont utiles lors de l'utilisation du CLI Ghost :

* `ghost start` : démarrez votre serveur.
* `ghost stop` : arrêtez votre serveur Ghost en cours d'exécution.
* `ghost help` : vérifiez la liste des commandes disponibles.

**Note :**

Assurez-vous que votre répertoire d'installation actuel est vide avant l'installation. Actuellement, vous installez Ghost en mode développement. Pour la production, vous ne suivrez pas les mêmes étapes.

## Comment configurer Ghost CMS avec le Cloud 

Si vous rencontrez des problèmes avec l'installation locale de Ghost, ou peut-être que c'est trop compliqué et que vous n'avez pas assez d'espace sur votre disque, vous pouvez utiliser un outil comme [digital press](https://www.digitalpress.blog/) ou tout autre service cloud comme GCP ou AWS, Digital Ocean, etc.

J'aime digital press car il vient avec un plan gratuit. Les autres services cloud ne fournissent pas cela, c'est pourquoi je le suggère.

## Comment obtenir le modèle de blog

Créer un nouveau blog à partir de zéro peut être difficile. Dans ce tutoriel, nous utiliserons un modèle pré-construit de [the frontend web](https://github.com/orgs/frontendweb3). Tous les modèles ont une licence MIT open-source, donc vous pouvez les utiliser, et vous n'avez pas besoin de tout configurer.

J'ai choisi le modèle [Open-blog](https://github.com/frontendweb3/open-blog) de frontend web. 

## Comment configurer Next.js

La configuration de Next est l'une des principales parties de ce tutoriel, où vous passerez du temps et de l'énergie à coder, déboguer et déployer le site. 

Voici les commandes à exécuter selon que vous utilisiez npx, yarn ou pnpm :

```bash
npx create-next-app@latest --experimental-app

# ou

yarn create next-app --experimental-app

# ou

pnpm create next-app --experimental-app
```

![créer une nouvelle application nextjs.](https://www.freecodecamp.org/news/content/images/2023/03/ghostandnextjs--1-.png)
_créer une nouvelle application nextjs._

Après avoir terminé le processus d'installation, nous devons installer quelques packages Node supplémentaires pour le blog.

Ces packages Node peuvent vous aider à accélérer votre processus de développement. Assurez-vous d'installer tous les packages ci-dessous pour suivre ce guide :

### Packages Node à installer :

1. `pnpm add @tryghost/content-api` (requis)
2. `pnpm add @types/tryghost__content-api` (requis par TypeScript)
3. `pnpm add tailwindcss postcss autoprefixer`
4. `pnpm add @tailwindcss/typography`
5. `pnpm add react-icons`
6. `pnpm add date-fns`
7. `pnpm add next-themes`
8. `pnpm add @radix-ui/react-popover`

Voici ce que fait chacun de ces packages :

* Le package [@tryghost/content-api](https://www.npmjs.com/package/@tryghost/content-api) est une bibliothèque cliente JavaScript Ghost pour récupérer les données de l'API de contenu.
* Le package [@types/tryghost__content-api](https://www.npmjs.com/package/@types/tryghost__content-api) contient les définitions de type pour @tryghost/content-api.
* TailwindCSS, autoprefixer et PostCSS sont des packages requis pour [Tailwind CSS](https://beta.nextjs.org/docs/styling/tailwind-css).
* Le package [@tailwindcss/typography](https://tailwindcss.com/docs/typography-plugin) pour gérer la typographie dynamique avec Tailwind CSS.
* Le package [next-themes](https://www.npmjs.com/package/next-themes) permet des thèmes comme le passage du mode sombre au mode clair sur votre site.
* Le package [react-icons](https://www.npmjs.com/package/react-icons) fournit de nombreuses icônes SVG pour le projet. Ainsi, vous n'avez pas besoin de les télécharger manuellement.
* [@radix-ui/react-popover](https://www.radix-ui.com/docs/primitives/components/popover#installation) fait partie de l'écosystème Radix UI. Je choisis le composant popover de Radix pour la conception du composant de recherche sur le site.
* Le package [date-fns](https://www.npmjs.com/package/date-fns) aide à convertir votre date `published_at` dans un format de date différent. 

## Ce qu'il faut savoir avant de suivre ce tutoriel

Avant de construire ce projet, je vous recommande vivement de regarder quelques tutoriels sur YouTube (surtout si vous êtes débutant avec Next.js). Ceux-ci vous aideront à comprendre quelques bases sur le dossier d'applications expérimental de Next.js. 

Chaque vidéo explique le même type de sujet. Si vous regardez chacune des quatre vidéos, vous avez une idée de base de comment fonctionne le dossier d'applications de Next.js. Cela rendra ce tutoriel avancé plus facile à suivre.

### [Vercel](https://www.youtube.com/@VercelHQ)

%[https://www.youtube.com/watch?v=gSSsZReIFRk&t=512s]

Dans ce tutoriel, Lee Robinson couvre les bases du routage, des segments de route dynamiques, de la récupération de données, de la mise en cache et des métadonnées.

### [Sakura Dev](https://www.youtube.com/@SakuraDev)

%[https://www.youtube.com/watch?v=6htDA6v4FPM]

Sakura Dev vous apprend la différence entre les pages Next.js et le dossier d'applications et le routage avec des exemples.

### Tuomo Kankaanpaa

%[https://www.youtube.com/watch?v=xXwxEudjiAY]

Tuomo Kankaanpaa vous apprend le routage du dossier d'applications Next, les mises en page et les composants serveur. 

### [Piyush Garg](https://www.youtube.com/watch?v=CBfBZvDQLis)

%[https://www.youtube.com/watch?v=CBfBZvDQLis]

Piyush Garg compile toutes les nouvelles fonctionnalités de Next et les convertit en un petit cours accéléré, et construit un projet de démonstration.

Maintenant que vous êtes prêt, commençons à construire notre blog.

## Structure des dossiers

Notre structure de dossiers ressemble à ceci pour notre application de démonstration :

```bash
.
├── next.config.js
├── next-env.d.ts
├── package.json
├── pnpm-lock.yaml
├── postcss.config.js
├── public
├── README.md
├── search.json
├── src
│   └── app
│       ├── authors
│       │   └── [slug]
│       │       └── page.tsx
│       ├── BlogLayout.tsx
│       ├── cards.min.css
│       ├── Card.tsx
│       ├── error.tsx
│       ├── favicon.ico
│       ├── Footer.tsx
│       ├── ghost-client.ts
│       ├── globals.css
│       ├── Header.tsx
│       ├── layout.tsx
│       ├── not-found.tsx
│       ├── pages
│       │   └── [slug]
│       │       └── page.tsx
│       ├── page.tsx
│       ├── pagination
│       │   └── [item]
│       │       └── page.tsx
│       ├── Pagination.tsx
│       ├── read
│       │   └── [slug]
│       │       ├── Newsletter.tsx
│       │       └── page.tsx
│       ├── Search.tsx
│       ├── SocialIcons.tsx
│       └── tags
│           └── [slug]
│               └── page.tsx
├── tailwind.config.js
└── tsconfig.json

13 répertoires, 30 fichiers
```

## Comment configurer Ghost CMS et Next.js

L'étape suivante consiste à configurer la récupération des données pour l'API de contenu Ghost. C'est pourquoi nous avons installé le package [@tryghost/content-api](https://www.npmjs.com/package/@tryghost/content-api) ci-dessus.  

Ghost CMS est livré avec deux types d'API : la première est l'API de contenu, et la seconde est l'API d'administration. Pour le blog, nous utiliserons l'API de contenu.

L'API de contenu est une API RESTful qui récupère le contenu publié de la base de données Ghost. C'est une API en lecture seule. Vous ne pouvez pas appeler de requêtes POST avec elle. 

Pour la configurer, nous créons un nouveau fichier à l'intérieur du dossier `src/app` avec `ghost-client.ts`. À l'intérieur du fichier, nous avons une nouvelle instance de l'API Ghost. 

```typescript
// ghost-client.ts

import GhostContentAPI from "@tryghost/content-api";

// Créer une instance API avec les informations d'identification du site
const api = new GhostContentAPI({
  url: process.env.GHOST_URL as string,
  key: process.env.GHOST_KEY as string,
  version: "v5.0"
});
```

Nous avons besoin de l'URL du blog, de la clé et de la version pour configurer l'API de contenu Ghost dans Next. Vous pouvez trouver à la fois les URL et la clé dans le tableau de bord Ghost, ainsi que la valeur de la version qui est votre version actuelle de Ghost CMS.

Allez dans le tableau de bord Ghost :

![Obtenez votre CLÉ et URL](https://www.freecodecamp.org/news/content/images/2023/03/ghost-next.gif)
_Obtenez votre CLÉ et URL_

Allez dans `dashboard` > `settings` > `integrations` > `Your-intergration-id` et obtenez votre `GHOST_URL` et `GHOST_KEY`. Maintenant, vous pouvez copier les deux et les coller à l'intérieur de votre fichier `.env.local`.

![Obtenez votre Ghost_Key et Ghost_URL](https://www.freecodecamp.org/news/content/images/2023/03/next-and-ghost.png)
_Obtenez votre `GHOST_KEY` et `GHOST_URL`_

## Comprendre le dossier d'applications Next.js 13

Il y a eu beaucoup de changements dans le dossier `pages` de Next.js et le dossier `app` avec la sortie de Next.js 13. Nous allons discuter de certaines choses importantes maintenant et plus lorsque nous construirons l'application :

1. Il n'y a pas de `_app`, `_document`, `getServerSideProps`, `getStaticProps`, `getStaticPaths`, `404` et `useRouter`.
2. Maintenant, il combine les fichiers `_app` et `_document` avec le fichier `layout`.
3. `useRouter` est importé depuis `next/navigation`.
4. Le fichier `404` est remplacé par la fonction `notFound()`. 
5. Le fichier `error.tsx` fournit des fonctionnalités comme réagir aux limites d'erreur.
6. Maintenant, le fichier `index.js` est remplacé par `page.js`.
7. Le passage des segments de route dynamique `pages/blog/[slug].js` est modifié, et le répertoire d'applications Next ressemble à ceci : `app/blog/[slug]/page.js`.

### Exemples

Pour comprendre le dossier d'applications expérimental de Next, regardons un exemple réel :

1. **page de tag** => `app/tag/[slug]/page.ts`
2. **catégorie** => `app/tag/[slug]/page.ts`

Maintenant, vous pouvez créer cinq fichiers à l'intérieur de chaque route. Par exemple, si vous créez une route `tag` ou **`category`** dans votre dossier d'applications, alors vous pouvez créer quatre fichiers à l'intérieur de votre dossier de route d'applications.

* `page.ts` (requis) : c'est votre fichier principal.
* `layout.ts` (optionnel) : il aide à concevoir votre mise en page
* `loading.ts` (optionnel) : il crée un indicateur de chargement avec React suspense. 
* `error.ts` (optionnel) : il aide à gérer les erreurs dans votre application React.
* `components` (optionnel) : vous pouvez également créer un autre composant dans vos routes.

Comprenons comment fonctionne la nouvelle route d'applications Next.js 13 avec un exemple concret : votre dossier de route de tag ressemble à ceci.

```typescript
app/tag/[slug]/page.ts
app/tag/[slug]/loading.ts
app/tag/[slug]/layout.ts
app/tag/[slug]/error.ts
app/tag/[slug]/my-card-component.ts
```

## Données de démonstration pour le projet 

Vous n'avez pas à vous soucier de créer une démonstration ou des données de blog factices. Pour vos tests, vous pouvez les télécharger depuis ce [dépôt GitHub](https://github.com/officialrajdeepsingh/nextjsghostcms/blob/main/.github/demo-post-for-ghost.json).

## Comment construire le blog

Nous allons passer en revue et construire chaque partie du blog dans les sections suivantes afin que vous puissiez suivre à la maison.

1. [Comment construire l'en-tête](#heading-comment-construire-len-tete)
2. [Comment construire le pied de page](#heading-comment-construire-le-pied-de-page)
3. [Comment construire la mise en page](#heading-comment-construire-la-mise-en-page)
4. [Comment construire la page d'accueil](#heading-comment-construire-la-page-daccueil)
5. [Comment construire la page de lecture](#heading-comment-construire-la-page-de-lecture)
6. [Comment construire la page de tag](#heading-comment-construire-la-page-de-tag)
7. [Comment construire la page d'auteur](#heading-comment-construire-la-page-dauteur)
8. [Comment construire des pages uniques](#heading-comment-construire-des-pages-uniques)
9. [Comment gérer la pagination](#heading-comment-gerer-la-pagination)
10. [SEO Next.js](#heading-nextjs-seo)
11. [Comment activer la recherche](#heading-comment-activer-la-recherche)
12. [Gestion des erreurs](#heading-gestion-des-erreurs)
13. [Comment reconstruire votre site statique avec des webhooks](#heading-comment-reconstruire-votre-site-statique-avec-des-webhooks)

### Comment construire l'en-tête

La première et principale partie du site est l'en-tête. Tout d'abord, nous allons créer un en-tête simple pour notre blog de démonstration. Notre en-tête ressemblera à ceci :

![En-tête du site](https://www.freecodecamp.org/news/content/images/2023/04/header.png)
_Conception de l'en-tête_

Tout d'abord, il y a le logo, ensuite la barre de navigation avec divers éléments, et enfin la section des icônes. Toutes les données proviennent de l'API Ghost CMS. Vous pouvez modifier les éléments à l'intérieur de Ghost CMS et cela se reflétera sur le site.

Voici le code pour construire le composant d'en-tête :

```typescript
// Header.tsx

import Link from "next/link";
import SocialIcons from "./SocialIcons";
import Image from "next/image";
import type { Settings } from "@tryghost/content-api";

function Header({ setting }: { setting: Settings }) {

  return (
    <header className="px-2 sm:px-4 py-2.5 dark:bg-gray-900 w-full">

      <div className="container flex flex-wrap items-center justify-between mx-auto">
        {/* Logo pour le blog */}
        <Link href="/" className="flex items-center">
          {setting.logo !== null ?
            <Image
              alt={setting.title} width={200} height={100} src={setting.logo} className="self-center text-xl font-semibold whitespace-nowrap dark:text-white" />
            : setting.title}
        </Link>
        <div className="flex md:order-2">

          <ul className="flex flex-wrap p-4 md:space-x-8 md:mt-0 md:text-sm md:font-medium">

            {
              /* Navigation du blog Modifier dans GHOST CMS  */
              setting.navigation !== undefined ? setting?.navigation.map(item => <li key={item.label} className="block py-2 pl-3 pr-4 text-gray-700 rounded hover:text-blue-700 dark:hover:text-blue-700 md:p-0 dark:text-white"
                aria-current="page">
                <Link href={item.url}>
                  {item.label}
                </Link>
              </li>) : " "

            }

          </ul>

        </div>
        <SocialIcons setting={setting} />
      </div>

    </header >
  )

}
export default Header

```

### Comment construire le pied de page

Le pied de page est également une section importante d'un site de blog. Il montre vos informations importantes et divers liens utiles. 

![Concevoir le pied de page](https://www.freecodecamp.org/news/content/images/2023/04/footer.png)
_Conception du pied de page_

J'ai conçu un pied de page basique avec un texte copyright et j'ai ajouté des icônes sociales pour le site. Les icônes sociales proviennent de l'API Ghost CMS.

```typescript
// Footer.tsx

import { FaTwitter, FaFacebook } from "react-icons/fa";
import Link from "next/link";
import type { Settings } from "@tryghost/content-api";

function Footer({ setting }: { setting: Settings }) {

  return (

    <footer className="px-2 sm:px-4 py-2.5 dark:bg-gray-900 w-full">

      <div className="container flex flex-wrap items-center justify-between mx-auto">

        <Link href="https://github.com/frontendweb3" className="flex items-center">
          <span className="self-center text-gray-800 text-sm font-semibold whitespace-nowrap dark:text-white">2023 copyright frontend web</span>
        </Link>

        <div className="flex md:order-2">

          <ul className="flex p-4 flex-row md:space-x-8 md:mt-0 md:text-sm font-medium">

            {
              setting.twitter !== null ? <li>
                <Link target="_blank" href={`https://twitter.com/${setting.twitter}`} className="block py-2 pl-3 pr-4 text-gray-700 rounded hover:text-blue-700 dark:hover:text-blue-700 md:p-0 dark:text-white" aria-current="page">
                  <FaTwitter />
                </Link>
              </li> : " "

            }

            {
              setting.facebook !== null ? <li>
                <Link target="_blank" href={`https://www.facebook.com/${setting.facebook}`} className="block py-2 pl-3 pr-4 text-gray-700 rounded hover:text-blue-700 dark:hover:text-blue-700 md:p-0 dark:text-white ">
                  <FaFacebook />
                </Link>
              </li> : " "

            }

          </ul>
        </div>

      </div>
    </footer>

  )
}

export default Footer

```

### Comment construire la mise en page

J'ai conçu une mise en page basique pour le blog. Pour construire des mises en page dans Next.js, il y a un fichier spécial `layout.tsx`.

Avant de créer la conception de la mise en page, nous devons définir une fonction `getNavigation` pour **récupérer** la navigation et les données de base liées au site web depuis Ghost. 

```typescript
// ghost-client.ts


export async function getNavigation() {
  return await api.settings.browse()
}
```

#### Les données ressemblent à ceci :

```object
{
  title: 'Rajdeep Singh',
  description: 'Pensées, histoires et idées.',
  logo: 'http://localhost:2368/content/images/2023/04/nextjsandghostlogo-2.png',
  icon: 'http://localhost:2368/content/images/size/w256h256/2023/04/nextjs-60pxx60px.png',
  accent_color: '#d27fa0',
  cover_image: 'https://static.ghost.org/v4.0.0/images/publication-cover.jpg',
  facebook: 'ghost',
  twitter: '@ghost',
  lang: 'en',
  locale: 'en',
  timezone: 'Etc/UTC',
  codeinjection_head: null,
  codeinjection_foot: null,
  navigation: Array(5) [
    { label: 'Home', url: '/' }, { label: 'JavaScript', url: '/tags/javascript/' }, { label: 'Nextjs', url: '/tags/nextjs/' },
    { label: 'Reactjs', url: '/tags/reactjs/' }, { label: 'Ghost CMS', url: '/tags/ghost-cms/' }
  ],
  secondary_navigation: Array(1) [ { label: 'Login', url: '#/portal/' } ],
  meta_title: 'My demo post',
  meta_description: 
    'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
  og_image: null,
  og_title: null,
  og_description: 
    'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
  twitter_image: null,
  twitter_title: null,
  twitter_description: 
    'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
  members_support_address: 'noreply',
  members_enabled: true,
  members_invite_only: false,
  paid_members_enabled: false,
  firstpromoter_account: null,
  portal_button_style: 'icon-and-text',
  portal_button_signup_text: 'Subscribe',
  portal_button_icon: null,
  portal_plans: Array(1) [ 'free' ],
  portal_name: true,
  portal_button: true,
  comments_enabled: 'all',
  url: 'http://localhost:2368/',
  version: '5.39'
}
```

La fonction `getNavigation` retourne les données des paramètres, puis nous passons les données en tant que props dans les composants d'en-tête et de pied de page.

Notre fichier principal `layout.tsx` fonctionne côté serveur. Il aide à récupérer les données côté serveur avec le hook React `use`.

```typescript
// Layout.tsx


import "./globals.css";
import BlogLayout from './BlogLayout'
import { getNavigation, } from "./ghost-client"
import { use } from "react"
import type { Settings } from "@tryghost/content-api"

interface UpdateSettings extends Settings {
  accent_color?: string;
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {

  const settings: UpdateSettings = use(getNavigation())

  return (

    <html className='light' lang="en">

      <body
        style={{
          '--bg-color': settings?.accent_color ? settings.accent_color : "",
        }}
        className={` bg-[--bg-color] dark:bg-gray-900`}>

        <BlogLayout setting={settings}>

          {children}

        </BlogLayout>

      </body>

    </html>

  )
}

```

#### Composant BlogLayout

Le composant `BlogLayout` fonctionne côté client. Dans le dossier d'applications Next.js, vous pouvez facilement convertir votre composant côté serveur en côté client avec la syntaxe suivante `"use client"`.

Le but du composant BlogLayout est de contenir [ThemeProvider](https://www.npmjs.com/package/next-themes), l'en-tête et le pied de page. ThemeProvider est un composant d'ordre supérieur, et il fournit des fonctionnalités supplémentaires, comme changer le thème du mode sombre au mode clair. Nous enveloppons le site intra avec le composant supérieur de ThemeProvider. Dans l'ancien répertoire des pages, nous obtenons une fonctionnalité similaire avec l'application personnalisée nextjs `_app.ts`.

Le composant ThemeProvider aide à changer le thème du mode clair au mode sombre.

```typescript
"use client"

// BlogLayout.tsx

import Footer from "./Footer";
import Header from "./Header";
import { ThemeProvider } from 'next-themes';
import type { Settings } from "@tryghost/content-api";
function Layout({ setting, children }: { setting: Settings, children: React.ReactNode }) {
  return <ThemeProvider attribute="class">
    <Header setting={setting} />
    {children}
    <Footer setting={setting} />
  </ThemeProvider>

}
export default Layout

```

### Comment construire la page d'accueil

Next.js a un fichier spécial `app/page.tsx` pour concevoir et construire la page d'accueil. La page d'accueil de notre site de blog ressemble à ce que vous voyez ci-dessous. Nous importons l'en-tête, la carte, la pagination et le pied de page sur la page d'accueil. L'en-tête et le pied de page font partie de `layout.tsx`.

![Page d'accueil](https://www.freecodecamp.org/news/content/images/2023/04/Home-page-1.png)
_Page d'accueil_

Tout d'abord, nous récupérons toutes les données des articles de Ghost CMS à l'aide de la fonction `getPosts`, que j'ai définie dans le fichier `ghost-client.ts`. 

```typescript
// ghost-client.ts

export async function getPosts() {
  return await api.posts
    .browse({
      include: ["tags", "authors"],
      limit: 10
    })
    .catch(err => {
      throw new Error(err)
    });
}
```

Par défaut, `api.post.browse()` retourne uniquement les données des articles, mais vous pouvez facilement les étendre. Dans chaque article ou donnée de publication, nous incluons également les tags et les auteurs à l'aide de `include`. Ensuite, nous définissons la limite des articles à dix.

#### Les données ressemblent à ceci :

```json
 [
  {
    id: '6422a742136f5d40f37294f5',
    uuid: '8c2fcfda-a6e4-4383-893b-ba18511c0f67',
    title: 'Demo Posts with Nextjs and Ghost Editor',
    slug: 'demo-posts-with-nextjs-and-reactjs',
    html: `<p><strong>Lorem Ipsum</strong> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text si
nce the 1500s when an unknown printer scrambled a galley of type and scrambled it to make a type specimen book. </p><p>It has survived five centuries and the leap i
nto electronic typesetting, remaining essentially unchanged. </p><p>It was popularised in the 1960s with Letraset sheets containing Lorem Ipsum passages and, more r
ecently, desktop publishing software like Aldus PageMaker, including versions of Lorem Ipsum.</p><figure class="kg-card kg-gallery-card kg-width-wide kg-card-hascap
tion"><div class="kg-gallery-container"><div class="kg-gallery-row"><div class="kg-gallery-image"><img src="http://localhost:2368/content/images/2023/03/Build-and-d
eploy.png" width="1500" height="400" loading="lazy" alt srcset="http://localhost:2368/content/images/size/w600/2023/03/Build-and-deploy.png 600w, http://localhost:2
368/content/images/size/w1000/2023/03/Build-and-deploy.png 1000w, http://localhost:2368/content/images/2023/03/Build-and-deploy.png 1500w" sizes="(min-width: 720px)
 720px"></div><div class="kg-gallery-image"><img src="http://localhost:2368/content/images/2023/03/Build-and-deploy-profile-1.png" width="1500" height="400" loading
="lazy" alt srcset="http://localhost:2368/content/images/size/w600/2023/03/Build-and-deploy-profile-1.png 600w, http://localhost:2368/content/images/size/w1000/2023
/03/Build-and-deploy-profile-1.png 1000w, http://localhost:2368/content/images/2023/03/Build-and-deploy-profile-1.png 1500w" sizes="(min-width: 720px) 720px"></div>
</div><div class="kg-gallery-row"><div class="kg-gallery-image"><img src="http://localhost:2368/content/images/2023/03/Build-and-deploy-profile--1--1.png" width="15
00" height="400" loading="lazy" alt srcset="http://localhost:2368/content/images/size/w600/2023/03/Build-and-deploy-profile--1--1.png 600w, http://localhost:2368/co
ntent/images/size/w1000/2023/03/Build-and-deploy-profile--1--1.png 1000w, http://localhost:2368/content/images/2023/03/Build-and-deploy-profile--1--1.png 1500w" siz
es="(min-width: 720px) 720px"></div><div class="kg-gallery-image"><img src="http://localhost:2368/content/images/2023/03/Build--Test-and-Deploy-profile-1.png" width
="1500" height="400" loading="lazy" alt srcset="http://localhost:2368/content/images/size/w600/2023/03/Build--Test-and-Deploy-profile-1.png 600w, http://localhost:2
368/content/images/size/w1000/2023/03/Build--Test-and-Deploy-profile-1.png 1000w, http://localhost:2368/content/images/2023/03/Build--Test-and-Deploy-profile-1.png 
1500w" sizes="(min-width: 720px) 720px"></div></div></div><figcaption>Build and deploy</figcaption></figure><h2 id="why-do-we-use-it">Why do we use it?</h2><p>It is
 a long-established fact that a reader will be distracted by the readable content of a page when looking at its layout. </p><p>The point of using Lorem Ipsum is tha
t it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. </p><p>Many desktop 
publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their 
infancy. </p><p>Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p><hr><h2 id="where-can-i
-get-some">Where can I get some?</h2><p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by i
njected humour, or randomised words which don't look even slightly believable. </p><p>If you are going to use a passage of Lorem Ipsum, you need to be sure there is
n't anything embarrassing hidden in the middle of text. </p><p>All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making 
this the first true generator on the Internet. </p><p>It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generat
e Lorem Ipsum which looks reasonable. </p><p>The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.</
p><div class="kg-card kg-callout-card kg-callout-card-red"><div class="kg-callout-emoji">💡</div><div class="kg-callout-text">My note is here&nbsp;</div></div><p></
p><div class="kg-card kg-header-card kg-width-full kg-size-small kg-style-dark" style data-kg-background-image><h2 class="kg-header-card-header" id="product">Produc
t</h2><h3 class="kg-header-card-subheader" id="my-blog-list">My blog list</h3></div><p></p><figure class="kg-card kg-embed-card kg-card-hascaption"><iframe width="2
00" height="113" src="https://www.youtube.com/embed/_q1K7cybyRk?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gy
roscope; picture-in-picture; web-share" allowfullscreen title="Next.js 13.1 Explained!"></iframe><figcaption>youtube</figcaption></figure><hr><figure class="kg-card
 kg-embed-card"><blockquote class="twitter-tweet"><p lang="en" dir="ltr">In 2022, we enabled developers to create at the moment of inspiration, now with over 2 mill
ion deployments per week.<br><br>Here's what we shipped 👇 <a href="https://t.co/6k7Xmbpna3?ref=localhost">pic.twitter.com/6k7Xmbpna3</a></p>&mdash; Vercel (@ver
cel) <a href="https://twitter.com/vercel/status/1611094825587167254?ref_src=twsrc%5Etfw&ref=localhost">January 5, 2023</a></blockquote>\n` +
      '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>\n' +
      '</figure><hr><figure class="kg-card kg-bookmark-card kg-card-hascaption"><a class="kg-bookmark-container" href="https://medium.com/frontendweb/what-is-progre
ssive-web-app-and-how-to-enable-it-in-nextjs-application-17f2e3240390?ref=localhost"><div class="kg-bookmark-content"><div class="kg-bookmark-title">What is Progres
sive Web App and How to enable it in nextjs Application?</div><div class="kg-bookmark-description">A detailed guide to Progressive Web Apps: How to use it with next
js and publish on Google play store, Microsoft store, Meta Quest, and🂅</div><div class="kg-bookmark-metadata"><img class="kg-bookmark-icon" src="https://cdn-static-
1.medium.com/_/fp/icons/Medium-Avatar-500x500.svg" alt><span class="kg-bookmark-author">FrontEnd web</span><span class="kg-bookmark-publisher">Rajdeep singh</span><
/div></div><div class="kg-bookmark-thumbnail"><img src="https://miro.medium.com/v2/resize:fit:1200/1*yAoHfq4Wm2Bp8DU1Dav29Q.png" alt></div></a><figcaption>Bookmark<
/figcaption></figure><div class="kg-card kg-header-card kg-width-full kg-size-small kg-style-dark" style data-kg-background-image><h2 class="kg-header-card-header" 
id="thank-you">Thank you</h2></div>',
    comment_id: '6422a742136f5d40f37294f5',
    feature_image: 'https://images.unsplash.com/photo-1543966888-7c1dc482a810?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDE2fHxqYXZhc2Nya
XB0fGVufDB8fHx8MTY3OTk5MjY1NA&ixlib=rb-4.0.3&q=80&w=2000',
    featured: false,
    visibility: 'public',
    created_at: '2023-03-28T08:37:22.000+00:00',
    updated_at: '2023-03-28T08:51:38.000+00:00',
    published_at: '2023-03-28T08:50:44.000+00:00',
    custom_excerpt: 'It has survived five centuries and the leap into electronic typesetting, remaining essentially unchanged. ',
    codeinjection_head: null,
    codeinjection_foot: null,
    custom_template: null,
    canonical_url: null,
    tags: [ [Object] ],
    authors: [ [Object] ],
    primary_author: {
      id: '1',
      name: 'Rajdeep Singh',
      slug: 'rajdeep',
      profile_image: 'https://www.gravatar.com/avatar/dafca7497609ae294378279ad1d6136c?s=250&r=x&d=mp',
      cover_image: null,
      bio: 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. ',
      website: 'https://officialrajdeepsingh.dev',
      location: 'India',
      facebook: 'officialrajdeepsingh',
      twitter: '@Official_R_deep',
      meta_title: null,
      meta_description: null,
      url: 'http://localhost:2368/author/rajdeep/'
    },
    primary_tag: {
      id: '6422aa9a136f5d40f3729552',
      name: 'demo',
      slug: 'demo',
      description: null,
      feature_image: null,
      visibility: 'public',
      og_image: null,
      og_title: null,
      og_description: null,
      twitter_image: null,
      twitter_title: null,
      twitter_description: null,
      meta_title: null,
      meta_description: null,
      codeinjection_head: null,
      codeinjection_foot: null,
      canonical_url: null,
      accent_color: null,
      url: 'http://localhost:2368/tag/demo/'
    },
    url: 'http://localhost:2368/demo-posts-with-nextjs-and-reactjs/',
    excerpt: 'It has survived five centuries and the leap into electronic typesetting, remaining essentially unchanged. ',
    reading_time: 3,
    access: true,
    comments: true,
    og_image: null,
    og_title: null,
    og_description: null,
    twitter_image: null,
    twitter_title: null,
    twitter_description: null,
    meta_title: null,
    meta_description: null,
    email_subject: null,
    frontmatter: null,
    feature_image_alt: 'Demo Posts with Nextjs and Ghost Editor',
    feature_image_caption: 'Photo by <a href="https://unsplash.com/@pinjasaur?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Paul Esch-Laurent</a> / 
<a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Unsplash</a>'
  },
meta:{
    pagination: { page: 1, limit: 10, pages: 2, total: 12, next: 2, prev: null }
  }
]
```

Maintenant, nous appelons la fonction `getPosts` côté serveur. Elle retourne toutes les données des articles avec les tags et auteurs associés. Maintenant, vous pouvez parcourir les données avec une fonction `map()`. 

Nous passons les données dans `app/page.tsx` aux composants `card.tsx`. Nous passons les données des articles en tant que props dans le composant de carte.

```typescript

// src/app/page.tsx

import { getPosts } from "./ghost-client"
import Card from './Card'

export default async function Home() {

  const getPost = await getPosts()

  return (
    <>
      <main className="container my-12 mx-auto grid grid-cols-1 gap-2 md:gap-3 lg:gap-4 lg:grid-cols-3 md:grid-cols-2 xl:grid-cols-4 2xl:grid-cols-4">

        {
          getPost?.map(
            item => {
              return <Card key={item.uuid} item={item} />
            })
        }

      </main>

    </>
  )
}
```

#### Composant Card

J'ai conçu une carte basique pour le blog. Le composant de carte ressemble à ceci :

![Composant de carte](https://www.freecodecamp.org/news/content/images/2023/04/card.png)
_Composant de carte_

J'ai rendu chaque élément de données provenant de la page d'accueil en tant que props et je l'ai affiché sur le site avec `Card.tsx`.

```typescript
// Card.tsx

import Image from "next/image"
import Link from "next/link"
import type { PostOrPage } from "@tryghost/content-api";
import { format } from 'date-fns'

function Card({ item }: { item: PostOrPage }) {

  return (
    <div className="max-w-full bg-white dark:bg-gray-800" >

      {
        item.featured !== null && item.feature_image !== undefined ? <Link href={`/read/${item.slug}`}>
          <Image className="rounded-lg p-3" width={1000} height={324} src={item.feature_image} alt={item.feature_image_alt || item.title} />
        </Link> : " "
      }

      <div className="p-3">

        <div className="flex mb-3">
          {
            item.published_at !== null && item.published_at !== undefined ? <p className="text-sm text-gray-500 dark:text-gray-400">
              {format(new Date(item.published_at), 'dd MMMM, yyyy')}
            </p> : ""
          }
          <p className="text-sm text-gray-500 dark:text-gray-400 mx-1"> , </p>
          <p className="text-sm text-gray-500 dark:text-gray-400">
            {item.reading_time} min read
          </p>
        </div>

        <Link href={`/read/${item.slug}`}>
          <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
            {item.title}
          </h5>
        </Link>


      </div>

    </div>

  )

}



export default Card
```

### Comment construire la page de lecture

La page de lecture est la deuxième page la plus importante pour le site de blog. Si les gens ne peuvent pas comprendre comment lire ce que l'auteur écrit, c'est un gros problème pour les développeurs front-end. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/ghostandnext-reading.png)
_Page de lecture_

Tout d'abord, nous obtenons un article unique de l'API Ghost CMS en fonction de son slug. Nous le passons au composant `Card` avec le composant `Link`.

```typescript
// ghost-client.ts

export async function getSinglePost(postSlug: string) {
  return await api.posts
    .read({
      slug: postSlug
    }, { include: ["tags", "authors"] })
    .catch(err => {
      console.error(err);
    });
}

```

La fonction `getSinglePost(<votre-slug>)` retourne les données d'un article unique, et vous pouvez rendre ces données sur la page.

```typescript
// src/app/read/[slug]/page.tsx

import Newsletter from "./Newsletter";
import Link from "next/link";
import { getSinglePost, getPosts } from "../../ghost-client"
import Image from "next/image";
// import icon
import { FaAngleLeft } from "react-icons/fa";

// types pour typescript
import type { Metadata } from "next";
import type { PostOrPage } from "@tryghost/content-api";

// format the date
import { format } from 'date-fns'

// css for card
import "../../cards.min.css"


export async function generateStaticParams() {
  const posts = await getPosts()
  return posts.map((post) => ({
    slug: post.slug,
  }));
}


async function Read({ params }: { params: { slug: string }; }) {

  const getPost = await getSinglePost(params.slug)

  return (
    <>
      <main className="pt-8 pb-16 lg:pt-16 lg:pb-24 dark:bg-gray-900">

        <div className="flex justify-between px-4 mx-auto max-w-screen-xl ">

          <article className="mx-auto w-full max-w-3xl prose prose-xl prose-p:text-gray-800  dark:prose-p:text-gray-100 sm:prose-base prose-a:no-underline prose-blue dark:prose-invert">

            <div className="flex mb-4 w-full justify-between">

              <Link className="inline-flex items-center" href={`/`}>
                <FaAngleLeft /> Back
              </Link>

              {
                getPost.primary_tag ? <Link href={`/tags/${getPost?.primary_tag.slug}`}>
                  # {getPost?.primary_tag.name}
                </Link> : ""
              }

            </div>

            <h1 className="mb-4 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl dark:text-white">
              {getPost.title}
            </h1>

            <p className="lead">
              {getPost.excerpt}
            </p>

            <header className="mb-4 lg:mb-6 not-format">

              <address className="flex items-center mb-6 not-italic">

                <div className="inline-flex items-center mr-3 text-sm text-gray-900 dark:text-white">

                  <Image width={32} height={32} className="mr-4 w-10 h-10 rounded-full" src={getPost?.primary_author.profile_image} alt={getPost?.primary_author.name} />
                  {
                    getPost.primary_author ? <Link href={`/authors/${getPost?.primary_author.slug}`} rel="author" className="text-xl font-bold text-gray-800 dark:text-white">{getPost?.primary_author.name}</Link> : " "
                  }

                  {
                    getPost.published_at ? <time className="text-base font-light text-gray-800 dark:text-white mx-1" dateTime={getPost?.published_at} title={format(new Date(getPost?.published_at), 'yyyy-MM-dd')}>
                      {format(new Date(getPost?.published_at), 'dd MMMM, yyyy')}
                    </time> : ""
                  }

                  <div className="text-base w-1 h-1 rounded-full bg-black dark:bg-white mx-1"></div>

                  <p className="text-base font-light text-gray-500 dark:text-gray-400"> {getPost.reading_time}  Min Read</p>

                </div>

              </address>

            </header>

            <figure>
              <Image className="mx-auto" width={1000} height={250} src={getPost.feature_image} alt={getPost.feature_image_alt} />
              <figcaption className="text-center"
                dangerouslySetInnerHTML={{
                  __html: getPost?.feature_image_caption
                }}></figcaption>
            </figure>

            <div dangerouslySetInnerHTML={{ __html: getPost?.html }}></div>

          </article>
        </div>
      </main>
      <Newsletter />
    </>
  )

}
export default Read

```

Vous rendez les données HTML de l'article avec `dangerouslySetInnerHTML`. Mais vous devez écrire beaucoup de CSS pour gérer le contenu dynamique provenant de l'API Ghost CMS. 

Pour résoudre cela, j'ai utilisé le package `@tailwindcss/typography`. J'ai également téléchargé `cards.min.css` depuis Ghost. Maintenant, vous n'avez pas besoin d'écrire une seule ligne de CSS dans votre application Next.

Générez le site statique avec la fonction `generateStaticParams`. Auparavant, nous utilisions la fonction `getStaticProps`.

```typescript
// ghost-client.ts


export async function generateStaticParams() {

  // fetch All posts

  const posts = await getPosts()
  
  // return the slug 
  
  return posts.map((post) => ({
    slug: post.slug,
  }));
  
}
```

###   
Comment construire la page de tag

J'ai conçu une page de tag simple pour le blog. La page de tag montre les articles liés aux tags qui sont utilisés. 

Vous pouvez également créer une page de catégorie. Les pages de tags et les pages de catégories utilisent la même logique et les mêmes fonctionnalités.

![Page de tag](https://www.freecodecamp.org/news/content/images/2023/04/ghostandnextjs-tag.png)
_Page de tag_

Similaire à la page de lecture, nous obtiendrons des articles basés sur les tags depuis l'API Ghost CMS.

```typescript
// ghost-client.ts


// return all posts realted to tag slug
export async function getTagPosts(tagSlug: string) {

  return await api.posts.browse({ filter: `tag:${tagSlug}`, include: 'count.posts' })
    .catch(err => {
      throw new Error(err)
    });
  ;

}

// return all the slugs to build static with generateStaticParams
export async function getAllTags() {
  return await api.tags.browse({
    limit: "all"
  }).catch(err => {
    console.log(err)
  })
}
```

La fonction `getTagPosts(<tag-slug>)` retourne tous les articles disponibles liés à un tag spécifique. 

Après avoir reçu tous les articles avec `getTagPosts()`, nous rendons tous les articles à l'aide de la méthode `map()`.

```typescript
// src/app/tag/[slug]/page.tsx

import React from 'react'
import Card from "../../Card"

import { getTagPosts, getAllTags } from "../../ghost-client"

import { notFound } from 'next/navigation';

import type { PostsOrPages } from "@tryghost/content-api";


export async function generateStaticParams() {

  const allTags: Tags = await getAllTags()

  let allTagsItem: { slug: string }[] = []
  
// genrate the slug for static site

  allTags?.map(item => {
    allTagsItem.push({
      slug: item.slug,
    })
  })

  return allTagsItem

}


async function Tag({ params }: { params: { slug: string }; }) {

  let tagPosts: PostsOrPages = await getTagPosts(params.slug)

// Handling 404 error

  if (tagPosts.length === 0) {
    notFound()
  }

  return (
    <aside aria-label="Related articles" className="py-8 lg:py-24 dark:bg-gray-800">
      
      <div className="px-4 mx-auto max-w-screen-xl">

        <h2 className="mb-8 text-2xl font-bold text-gray-900 dark:text-white">
          More articles from {params.slug.split("-").join(" ")}
        </h2>

        <div className="container my-12 mx-auto grid grid-cols-1 gap-12 md:gap-12 lg:gap-12  lg:grid-cols-3  md:grid-cols-2 xl:grid-cols-4 2xl:grid-cols-4 ">
        
          {
            tagPosts.map(
              item => <Card key={item.uuid} item={item} />
            )
          }
        
        </div>

      </div>

    </aside>
  )

}

export default Tag
```

Générez le site statique avec la fonction `generateStaticParams`. Elle aide à générer les slugs de la construction statique.

```typescript
// ghost-client.ts

export async function getAllTags() {
  return await api.tags.browse({
    limit: "all"
  }).catch(err => {
    console.log(err)
  })
}
```

### Comment construire la page d'auteur

La dernière et l'une des pages les plus importantes pour le site de blog est la page d'auteur. C'est là que les lecteurs peuvent en savoir plus sur l'auteur. 

Pour le blog de démonstration, j'ai conçu une page basique pour l'auteur. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/nextandghostauthor.png)
_Page d'auteur_

Nous allons construire cela de manière similaire à la façon dont nous avons construit la page de tag. Tout d'abord, nous obtenons les métadonnées de l'auteur et les articles de l'auteur depuis l'API Ghost CMS. 

```typescript
// ghost-client.ts


// get author meta Data

export async function getSingleAuthor(authorSlug: string) {
  return await api.authors
    .read({
      slug: authorSlug
    }, { include: ["count.posts"] })
    .catch(err => {
      console.log(err)
    });

}

// get author related posts

export async function getSingleAuthorPosts(authorSlug: string) {
  return await api.posts.browse({ filter: `authors:${authorSlug}` })
    .catch(err => {
      console.log(err)
    })
};

// get All author from Ghost CMS for generateStaticParams

export async function getAllAuthors() {

  return await api.authors
    .browse({
      limit: "all"
    })
    .catch(err => {
      throw new Error(err)
    });

}
```

La fonction `getSingleAuthor(<author-slug>)` retourne les données d'un seul auteur en fonction du slug de l'auteur, et la fonction `getSingleAuthorPosts(<author-slug>)` retourne tous les articles liés à l'auteur.

Nous rendons les données des articles à l'aide de la méthode `map()`. 

```typescript
// src/app/author/[slug]/page.tsx

import React from 'react';
import Link from "next/link";
import { FaFacebook, FaTwitter, FaGlobe } from "react-icons/fa";
import Card from "../../Card"

import { getSingleAuthor, getSingleAuthorPost, getAllAuthors } from "../../ghost-client"

import Image from 'next/image';
import { notFound } from 'next/navigation';

import type { Author, PostsOrPages } from "@tryghost/content-api";



export async function generateStaticParams() {

  const allAuthor: Author[] = await getAllAuthors()


  let allAuthorItem: { slug: string }[] = []

  allAuthor.map(item => {
    allAuthorItem.push({
      slug: item.slug,
    })
  })
  return allAuthorItem

}


async function AuthorPage({ params }: { params: { slug: string }; }) {

  const getAuthor: Author = await getSingleAuthor(params.slug)

  const allAuthor: PostsOrPages = await getSingleAuthorPost(params.slug)

// Handling 404 errors
  if (allAuthor?.length === 0) {
    notFound()
  }

  return (
    <>
      <section className="dark:bg-gray-900">
        <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">

          <div className=" p-10 text-gray-500 sm:text-lg dark:text-gray-400">

            {
              getAuthor?.profile_image !== undefined ? <Image height={30} width={30} className="w-36 h-36 p-2 rounded-full mx-auto ring-2 ring-gray-300 dark:ring-gray-500" src={getAuthor?.profile_image} alt={getAuthor?.name} /> : ""
            }

            {
              getAuthor?.name ? <h2 className="mb-4 mt-4 text-4xl tracking-tight font-bold text-center text-gray-900 dark:text-white">
                {getAuthor?.name.split(" ")[0]}
                <span className="font-extrabold">
                  {getAuthor?.name?.split(" ")[1]}
                </span>
              </h2> : ""
            }

            <p className="mb-4 font-light text-center">{getAuthor?.bio} </p>


            <ul className="flex flex-wrap p-4 justify-center md:space-x-8 md:mt-0 md:text-sm md:font-medium">

              {
                (getAuthor?.website !== null) ? (<li>
                  <Link href={getAuthor?.website} className="block py-2 pl-3 pr-4 text-gray-700 hover:text-blue-700 dark:hover:text-blue-700 rounded md:p-0 dark:text-white" aria-current="page">
                    <FaGlobe />
                  </Link> </li>) : " "


              }

              {
                (getAuthor?.twitter !== null) ? (<li>
                  <Link href={getAuthor?.twitter} className="block py-2 pl-3 pr-4 text-gray-700 rounded hover:text-blue-700 dark:hover:text-blue-700 md:p-0 dark:text-white" aria-current="page">
                    <FaTwitter />
                  </Link>
                </li>) : " "
              }

              {
                (getAuthor?.facebook !== null && getAuthor.facebook !== undefined) ? (<li>
                  <Link href={getAuthor?.facebook}
                    className="block py-2 pl-3 pr-4 text-gray-700 rounded  hover:text-blue-700 dark:hover:text-blue-700 md:p-0 dark:text-white"> <FaFacebook />
                  </Link>
                </li>) : " "

              }

            </ul>

          </div>
        </div>
      </section>

      <aside aria-label="Related articles" className="py-8 lg:py-24 dark:bg-gray-800">
        <div className="px-4 mx-auto max-w-screen-xl">

          <h2 className="mb-8 text-2xl font-bold text-gray-900 dark:text-white">
            More articles from {getAuthor?.name}
          </h2>

          <div className="container my-12 mx-auto grid grid-cols-1 gap-12 md:gap-12 lg:gap-12  lg:grid-cols-3  md:grid-cols-2 xl:grid-cols-4 2xl:grid-cols-4 ">

            {
              allAuthor?.map(item => <Card key={item?.uuid} item={item} />)
            }

          </div>
        </div>
      </aside>


    </>
  )

}
export default AuthorPage
```

Pour générer le slug de l'auteur pour le site statique, nous devons utiliser la fonction `generateStaticParams`. Nous n'avons pas besoin d'autre chose pour construire le site statique.

```typescript
// ghost-client.ts


// Build Static Site 

export async function generateStaticParams() {

  const allAuthor: Author[] = await getAllAuthors()


  let allAuthorItem: { slug: string }[] = []

  allAuthor.map(item => {
    allAuthorItem.push({
      slug: item.slug,
    })
  })
  return allAuthorItem

}
```

### Comment construire des pages uniques

Pour des pages uniques comme À propos, Contact, Politique de confidentialité, etc., vous pouvez également les créer avec l'API de contenu Ghost.

Notre conception de page unique ressemble à ceci :

![page de blog unique](https://www.freecodecamp.org/news/content/images/2023/04/single-blog.png)
_page de blog unique_

Tout d'abord, vous devez récupérer toutes les pages et les données des pages uniques depuis l'API de contenu Ghost. 

```typescript
// ghost-client.tsx

// fetch all pages

export async function getSinglePage(pageSlug: string) {
  return await api.pages
    .read({
      slug: pageSlug
    })
    .catch(err => {
      console.error(err);
    });
}

// single page data 

export async function getSinglePage(pageSlug: string) {
  return await api.pages
    .read({
      slug: pageSlug
    }, { include: ["tags"] })
    .catch(err => {
      console.error(err);
    });
}
```

La fonction `getSinglePage(page-slug)` retourne les données de la page unique en fonction du slug de la page, et la fonction `getAllPages()` retourne toutes les données de page publiées disponibles pour générer les paramètres dynamiques avec la fonction `generateStaticParams()`. 

```typescript
// src/app/pages/[slug]/page.tsx

import { getSinglePage, getAllPages } from "../../ghost-client"
import { notFound } from 'next/navigation';
import type { PostOrPage } from "@tryghost/content-api";
import "../../cards.min.css"

// genrate Static slug or params for blog

export async function generateStaticParams() {
  const pages = await getAllPages()

  return pages.map((post) => ({
    slug: post.slug,
  }));
}

async function Pages({ params }: { params: { slug: string }; }) {

// fetch single page
  const getPage = await getSinglePage(params.slug)

  // handle 404 error
  if (!getPage) {
    notFound()
  }

  return (
    <>
      <main className="pt-8 pb-16 lg:pt-16 lg:pb-24 dark:bg-gray-900">
        <div className="flex justify-between px-4 mx-auto max-w-screen-xl ">

          <article className="mx-auto w-full max-w-3xl prose prose-xl prose-p:text-gray-800  dark:prose-p:text-gray-100 sm:prose-base prose-a:no-underline prose-blue dark:prose-invert">


            <h1 className="mb-14 text-3xl font-extrabold leading-tight text-gray-900 lg:mb-6 lg:text-4xl dark:text-white">
              {getPage.title}
            </h1>

            <div dangerouslySetInnerHTML={{ __html: getPage?.html }}></div>

          </article>
        </div>
      </main>
    </>
  )

}
export default Pages

```

### Comment gérer la pagination

La pagination aide à accélérer votre site ainsi qu'à diviser votre site en parties plus petites et plus digestes. Vous pouvez lier vos articles les uns aux autres avec `prev` et `next`. 

```json
meta:{
    pagination: { page: 1, limit: 10, pages: 2, total: 12, next: 2, prev: null }
 }
```

Tout d'abord, nous allons créer un fichier `Pagination.tsx` en tant que composant React.

```typescript
// Pagination.tsx

import Link from "next/link"
import { Pagination } from "@tryghost/content-api"

function PaginationItem({ item }: { item: Pagination }) {

  let paginationItems = []

  for (let index = 1; index <= item?.pages; index++) {
    paginationItems.push(<li key={index * 2} ><Link href={index === 1 ? "/" : `/pagination/${index}`} className="px-3 py-2 leading-tight bg-blue-100 hover:bg-blue-200 border-transparent border rounded-lg text-black dark:bg-gray-800 dark:text-gray-400 mx-2 dark:hover:bg-gray-700 dark:hover:text-white">
      {index}
    </Link></li>)
  }

  return (

    <nav aria-label="pagination" className="mx-auto my-20 container">

      <ul className="mx-auto flex justify-center -space-x-px">

        <li>
          {
            item.prev ? <Link href={item.prev === 1 ? "/" : `/pagination/${item.prev}`} className="px-3 py-2 mr-2 border border-transparent rounded-md  leading-tight bg-white hover:text-blue-700 dark:bg-gray-800 dark:text-gray-400
              dark:hover:bg-gray-700 dark:hover:text-white">
              Prev
            </Link> : " "
          }
        </li>

        {paginationItems}

        <li>
          {
            item.next ? <Link href={`/pagination/${item.next}`} className="px-3 py-2 ml-2 border border-transparent rounded-md leading-tight bg-white hover:text-blue-700 dark:bg-gray-800 dark:text-gray-400
            dark:hover:bg-gray-700 dark:hover:text-white">
              Next
            </Link> : " "
          }
        </li>


      </ul>

    </nav>

  )

}


export default PaginationItem
```

Lorsque vous appelez la requête `api.posts.browse({ limit: 10 })`, le point de terminaison de l'API retourne dix articles et un objet `meta` avec `pagination`.

#### Les données retournées `api.posts.browse({ limit: 10 })` ressemblent à ceci :

```json
 [
  {title: 'Demo Posts with Nextjs and Ghost Editor',... },
  {title: Trigger the hook and rebuild the nextjs site',... }

meta:{
    pagination: { page: 1, limit: 10, pages: 2, total: 12, next: 2, prev: null }
  }
]
```

Maintenant, en fonction de `meta`, nous pouvons créer une pagination et passer `meta.pagination` en tant que props au composant `Pagination`.

```typescript
// src/app/page.tsx

import { getPosts } from "./ghost-client"
import Pagination from "./Pagination"

export default async function Home() {

  const getPost = await getPosts()

  const AllPostForSerach = await getSearchPosts()

  return (
    <>
     {/* rest of code  */}
      <Pagination item={getPost.meta.pagination} />
    </>
  )
}

```

Pour activer la pagination dynamique, nous allons créer une route `src/app/pagination/[item]/page.tsx` dans le blog. Vous pouvez utiliser le nom que vous voulez pour la route de pagination.

```typescript
// ghost-client.tsx

// return all posts for generateStaticParams

export async function getPosts() {
  return await api.posts
    .browse({
      include: ["tags", "authors"],
      limit: 10
    })
    .catch(err => {
      throw new Error(err)
    });
}

// 
export async function getPaginationPosts(page: number) {
  return await api.posts
    .browse({
      include: ["tags", "authors"],
      limit: 10,
      page: page
    })
    .catch(err => {
      throw new Error(err)
    });
}
```

La fonction `getPosts` est utilisée pour rendre le composant `Pagination` sur la page de pagination. La partie importante est la fonction `getPaginationPosts(<pagination-page-number>)` qui retourne les articles en fonction du numéro de page de pagination.

```typescript
// src/app/pagination/[item]/page.tsx

import { getPaginationPosts, getPosts } from "../../ghost-client"
import Card from '../../Card'
import PaginationItem from "../../Pagination"
import type { Metadata } from "next";
import type { PostsOrPages } from "@tryghost/content-api";




export async function generateStaticParams() {

  const posts:PostsOrPages = await getPosts()

  let paginationItem: { item: number }[] = []

  for (let index = 1; index <= posts?.meta.pagination.pages; index++) {
    paginationItem.push({
      item: index,
    })

  }

  return paginationItem

}



export default async function Pagination({ params }: { params: { item: string }; }) {

  let getParams: number = Number.parseInt(params.item)

  const getPost: PostsOrPages = await getPaginationPosts(getParams)

  return (
    <>

      <main className="container my-12 mx-auto grid grid-cols-1 gap-2 md:gap-3 lg:gap-4 lg:grid-cols-3 md:grid-cols-2 xl:grid-cols-4 2xl:grid-cols-4">

        {
          getPost?.map(
            item => {
              return <Card key={item.uuid} item={item} />
            })
        }
      </main>

      <PaginationItem item={getPost.meta.pagination} />

    </>
  )
}

```

### SEO Next.js 

Si vous êtes blogueur, vous savez à quel point le SEO est important pour aider les gens à trouver votre blog et vos articles. Pour le SEO, Next.js fournit une fonction `generateMetadata` pour générer des métadonnées SEO dynamiques pour votre site. Cela signifie que vous n'avez pas besoin de packages supplémentaires pour le SEO.  

À des fins d'exemple, je vais expliquer comment activer le SEO pour le blog uniquement sur la page d'accueil et la page de lecture. Vous pouvez utiliser la même logique pour l'activer sur n'importe laquelle de vos autres pages. 

Tout d'abord, voyons comment activer le SEO sur la page d'accueil :

```typescript
// ghost-client.ts


// Obtenez vos métadonnées de paramètres depuis Ghost CMS
export async function getNavigation() {
  return await api.settings.browse()
}
```



```typescript
// src/app/page.tsx

import { getNavigation } from "./ghost-client"

export async function generateMetadata(): Promise<Metadata> {
  const Metadata = await getNavigation()
  return {
    title: Metadata.title,
    description: Metadata.description,
    keywords: ['Next.js', 'React', 'JavaScript'],
  }
}
```

Maintenant, nous allons voir comment activer le SEO sur la page de lecture :

```typescript
// ghost-client.ts


export async function getSinglePost(postSlug: string) {
  return await api.posts
    .read({
      slug: postSlug
    }, { include: ["tags", "authors"] })
    .catch(err => {
      console.error(err);
    });
}
```

La fonction `generateMetadata` a des props de paramètres, qui aident à accéder au slug. Ensuite, en fonction du slug, nous obtenons les données et les retournons. 

```typescript


export async function generateMetadata({ params }: { params: { slug: string }; }): Promise<Metadata> {

  const metaData: PostOrPage = await getSinglePost(params.slug)

  let tags = metaData?.tags.map(item => item.name)

  return {
    title: metaData.title,
    description: metaData.description,
    keywords: tags,
    openGraph: {
      title: metaData.title,
      description: metaData.excpet,
      url: metaData.url,
      keywords: tags,
      images: [
        {
          url: metaData.feature_image,
        },
      ],
      locale: metaData.locale,
      type: 'website',
    },
  }
}
```

### Comment activer la recherche

Activer la recherche sur un blog statique est difficile à faire à partir de zéro. Au lieu de cela, vous pouvez utiliser une page Node tierce comme [Orama](https://github.com/oramasearch/orama) ou [Flex search](https://github.com/nextapps-de/flexsearch).

![Image](https://www.freecodecamp.org/news/content/images/2023/04/searchbarinnextjs.gif)

Pour notre démonstration, nous avons créé une fonctionnalité de barre de recherche très simple sans installer de packages supplémentaires.

Tout d'abord, nous obtenons tous les articles de l'API Ghost CMS.

```typescript
// ghost-client.ts

export async function getSearchPosts() {
  return await api.posts.browse({ limit: "all"}).catch(err => {
    console.log(err)
  });
```

Après l'avoir converti en chaîne avec l'aide de `JSON.stringify()`, nous créons ensuite un nouveau fichier `search.json`. À chaque requête, il met à jour ou réécrit notre fichier `search.json`.

```typescript
// src/app/page.tsx

import {  getSearchPosts } from "./ghost-client"
import * as fs from 'node:fs';



export default async function Home() {

  
// get All posts for search 
  const AllPostForSerach = await getSearchPosts()

  // Enable getSearch  

  try {

    const jsonString = JSON.stringify(AllPostForSerach)

    fs.writeFile('search.json', jsonString, 'utf8', err => {
      if (err) {
        console.log('Error writing file', err)
      } else {
        console.log('Successfully wrote file')
      }
    })

  } catch (error) {
    console.log('error : ', error)
  }


  return (
    <>
      <main className="container my-12 mx-auto grid grid-cols-1 gap-2 md:gap-3 lg:gap-4 lg:grid-cols-3 md:grid-cols-2 xl:grid-cols-4 2xl:grid-cols-4">
      {/* rest code... */}
      </main>
    </>
  )
}

```

Lorsque vous entrez le texte dans l'entrée de recherche, en fonction de la requête de texte, nous comparons la requête ou le texte dans les données du fichier `serach.json`. Si cela correspond au titre de l'article avec la requête, alors nous stockons la variable `searchPost`, et enfin nous rendons les données stockées dans la page de la variable `searchPost`.

```typescript
"use client"

import React, { useEffect, useState } from 'react';
import * as Popover from '@radix-ui/react-popover';
import { FaSearch } from "react-icons/fa";
import Link from 'next/link';
import searchData from '../../search.json'
import type { PostOrPage } from "@tryghost/content-api"


let searchPost: PostOrPage[] = []


function Search() {

  const [query, setQuery] = useState(null)

  useEffect(() => {

    searchPost.length = 0;

    searchData.map((item: PostOrPage) => {

      if (item?.title.trim().toLowerCase().includes(query?.trim().toLowerCase())) {
        searchPost.push(item)
      }

    })

  }, [query])


  return (
    <Popover.Root>
      <Popover.Trigger asChild>
        <button
          className="cursor-pointer outline-none"
          aria-label="Search"
        >
          <FaSearch />
        </button>
      </Popover.Trigger>

      <Popover.Portal>

        <Popover.Content
          className="rounded p-2 bg-white dark:bg-gray-800 w-[480px] will-change-[transform,opacity] data-[state=open]:data-[side=top]:animate-slideDownAndFade data-[state=open]:data-[side=right]:animate-slideLeftAndFade data-[state=open]:data-[side=bottom]:animate-slideUpAndFade data-[state=open]:data-[side=left]:animate-slideRightAndFade"
          sideOffset={5}
        >

          <div className='my-2'>
            <label htmlFor="default-search" className="mb-2 mt-5 text-sm font-medium text-gray-900 sr-only dark:text-white">Search bar </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                <svg className="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
              </div>
              <input type="search" id="default-search" onChange={(event) => setQuery(event?.target.value)} className="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Start searching here ..." required />

            </div>
          </div>


          {

            serachPost.length > 0 ? serachPost.map(item => {

              return (
                <div key={item.uuid} className='my-3'>
                  <div className="text-white my-2 py-2 bg-blue-400 dark:bg-gray-900 dark:hover:bg-blue-400 border-none rounded-md dark:text-white">
                    <Link href={`read/${item.slug}`} className="relative inline-flex items-center rounded-lg w-full px-4 py-2 text-sm font-medium">
                      {item.title}
                    </Link>
                  </div>
                </div>
              )
            }) : " "

          }

        </Popover.Content>

      </Popover.Portal>

    </Popover.Root >
  )
}

export default Search;

```

### Gestion des erreurs

Next.js a deux types de [gestion des erreurs](https://beta.nextjs.org/docs/routing/error-handling#how-errorjs-works). Le premier est basé sur la mise en page, et le second est la [gestion des erreurs globales](https://beta.nextjs.org/docs/routing/error-handling#handling-errors-in-root-layouts). Pour la démonstration ici, nous utiliserons la gestion des erreurs basée sur la mise en page.

Next fournit un type spécial de fichier `error.tsx` pour gérer les erreurs sur votre site. Il ne gère pas les erreurs 404, 500, etc. – il ne gère que les erreurs d'exécution.

```typescript
'use client'; // Les composants d'erreur doivent être des composants Client
import React from 'react';
import { useEffect } from 'react';
import Link from 'next/link';
export default function Error({ error, reset }: { error: Error; reset: () => void; }) {

  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <section className="dark:bg-gray-900 my-16">

      <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">

        <div className="mx-auto max-w-screen-sm text-center">

          <h1 className="mb-4 text-7xl tracking-tight font-extrabold lg:text-9xl text-primary-600 dark:text-primary-500">Something wrong</h1>
          <p className="mb-4 text-lg p-2 font-light bg-red-500 text-white dark:bg-red-400 dark:text-white">{error.message}</p>

          <div className='flex justify-around mt-2'>

            <Link href="#" className="inline-flex bg-gray-600 text-white hover:bg-gray-700 focus:ring-4 font-medium rounded-lg text-sm p-2
                text-center">Back to Homepage</Link>

            <button className='bg-gray-600 text-white rounded-lg p-2' onClick={() => reset()}>
              Try again
            </button>


          </div>

        </div>

      </div>

    </section>
  );
}

```

#### Comment gérer les erreurs 404

Pour gérer les erreurs 404 dans le dossier d'applications Next.js, vous devez créer un fichier `not-found.tsx` au niveau de la racine. 

Notre fichier 404 ressemble à ceci :

![erreur 404](https://www.freecodecamp.org/news/content/images/2023/04/nextjsandghosterror.png)
_erreur 404_

Voici le code pour cela :

```typescript
import Link from "next/link"

function NotFound() {

  return (
    <section className="bg-white dark:bg-gray-900 my-16">
      <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
        <div className="mx-auto max-w-screen-sm text-center">
          <h1 className="mb-4 text-7xl tracking-tight lg:text-9xl text-primary-600 dark:text-primary-500">404</h1>
          <p className="mb-4 text-3xl tracking-tight font-bold text-gray-900 md:text-4xl dark:text-white"> Something wrong</p>
          <p className="mb-4 text-lg font-light text-gray-500 dark:text-gray-400">
            Sorry, we cant find that article. You will find lots to explore on the home page.
          </p>
          <Link href="/" className="inline-flex text-white bg-black dark:bg-white dark:text-black p-3 hover:bg-gray-800 my-4">Back to Homepage</Link>
        </div>
      </div>
    </section >
  )

}

export default NotFound
```

Le gros problème avec le fichier d'erreur `not-found.tsx` est qu'il ne s'affiche pas automatiquement dans Next (v13.3.0). Pour afficher une erreur 404, vous devez afficher l'erreur manuellement. Voici comment faire :

```typescript
import { notFound } from 'next/navigation';

async function Read({ params }: { params: { slug: string }; }) {

  const getPost = await getSinglePost(params.slug)

  // if not found getPost, then show 404 error

  if (!getPost) {
    notFound()
  }

  return (
      <main className="pt-8 pb-16 lg:pt-16 lg:pb-24 dark:bg-gray-900">
      
          rest of code ....
      
      </main>
      )
}
```

### Comment reconstruire votre site statique avec des webhooks

Le plus gros problème lorsque vous créez un site statique se produit si quelqu'un écrit un nouvel article ou modifie un article existant dans Ghost. Pour un projet personnel, vous pouvez redéployer manuellement votre site. Mais pour un site plus grand, vous ne pourrez pas faire cela à chaque fois que cela se produit.

La meilleure solution est d'utiliser des webhooks. Ghost fournit un support pour les webhooks. Si vous mettez à jour un article existant ou en écrivez un nouveau, il sera mis à jour dans Ghost. 

Dans le projet de démonstration, nous utilisons les webhooks Vercel pour déployer notre blog. Lorsque nous créons un nouveau blog ou mettons à jour quelque chose sur le site, Ghost déclenche le webhook Vercel. Ensuite, Vercel reconstruit le site si nécessaire.

Vous n'avez pas besoin d'écrire le code pour cela – suivez simplement et copiez-collez au fur et à mesure.

#### Comment obtenir le webhook de Vercel

Tout d'abord, allez dans le tableau de bord Vercel.

![Tableau de bord Vercel](https://www.freecodecamp.org/news/content/images/2023/04/select1.png)
_Tableau de bord Vercel_

Sélectionnez votre projet, où vous allez déployer votre frontend Ghost.

![Sélectionnez le projet dans votre tableau de bord vercel](https://www.freecodecamp.org/news/content/images/2023/04/select2.png)
_Sélectionnez le projet dans votre tableau de bord Vercel_

Cliquez sur l'onglet des paramètres dans votre projet Vercel.

![Cliquez sur l'onglet Git](https://www.freecodecamp.org/news/content/images/2023/04/select3.png)
_Cliquez sur l'onglet Git_

Ensuite, cliquez sur l'onglet Git. Après avoir fait défiler vers le bas, vous pouvez voir la sélection du hook de déploiement.  

![Aller à la section des hooks de déploiement](https://www.freecodecamp.org/news/content/images/2023/04/select4.png)
_Aller à la section des hooks de déploiement_

Entrez le nom de votre webhook et le nom de la branche et cliquez sur le bouton "create hook".

![Copiez votre URL de webhook](https://www.freecodecamp.org/news/content/images/2023/04/select5.png)
_Copiez votre URL de webhook_

Cliquez sur le bouton de copie pour copier votre webhook vercel. 

#### Comment intégrer les webhooks Vercel dans le tableau de bord Ghost

Lorsque quelque chose change dans Ghost, il déclenche l'URL du webhook Vercel. Ensuite, Vercel redéploie le site de blog. 

Pour intégrer le webhook Vercel avec Ghost, suivez simplement ces étapes :

Ouvrez le tableau de bord Ghost CMS.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/ghost1.png)
_Tableau de bord Ghost_

Cliquez sur l'icône des paramètres.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/ghost3.png)
_Paramètres Ghost_

Cliquez sur le bouton Nouvelle intégration personnalisée.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/ghost4.png)
_Ajouter une nouvelle intégration personnalisée_

Entrez le nom de l'intégration.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/ghost5.png)
_Ajouter le nom de l'intégration_

Cliquez pour ajouter le bouton de webhook.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/ghost7.png)
_Comment ajouter le webhook_

Tout d'abord, entrez le nom, puis sélectionnez Événement et collez l'URL que vous avez copiée depuis le tableau de bord Vercel.

En fonction de l'événement, Ghost appellera le webhook, et votre site web sera reconstruit. Les redéploiements prennent du temps en fonction de la taille de votre site, etc.

## Conclusion

Tout devrait bien fonctionner en utilisant Next.js et l'API Ghost CMS comme nous l'avons travaillé dans ce tutoriel.

Mais certains des composants de l'éditeur Ghost, comme les bascules, où vous avez besoin d'une interaction JavaScript, ne fonctionnent pas. Vous pouvez résoudre ce problème en écrivant votre propre JavaScript ou en obtenant un fichier JavaScript pour Ghost et en l'ajoutant au fichier `read/[slug]/page.tsx`.  

Vous pouvez économiser beaucoup d'argent sur l'hébergement en combinant Next.js et l'API Ghost CMS, mais vous perdez certaines fonctionnalités comme l'inscription intégrée, la connexion, les comptes, les abonnements, la barre de recherche et les niveaux d'accès des membres.

Vous pouvez me suivre et me partager sur [Twitter](https://twitter.com/Official_R_deep) et [Linkedin](https://www.linkedin.com/in/officalrajdeepsingh/). Si vous aimez mon travail, vous pouvez lire plus de contenu sur mon blog, [officialrajdeepsingh.dev](https://officialrajdeepsingh.dev/), [frontend web](https://medium.com/frontendweb), et vous inscrire à ma [newsletter gratuite](https://officialrajdeepsingh.medium.com/subscribe).

Vous pouvez également consulter [awesome-next](https://github.com/officialrajdeepsingh/awesome-nextjs), une liste organisée de bibliothèques basées sur Nextjs qui aident à construire des applications petites et grandes avec Next.js.

Voici quelques ressources supplémentaires que vous pouvez utiliser si vous avez besoin de plus d'aide ou d'informations en suivant ce tutoriel :

%[https://ghost.org/docs/jamstack/next/]

%[https://www.digitalocean.com/community/tutorials/how-to-build-your-blog-on-digitalocean-with-ghost-and-next-js]

%[https://ghost.org/docs/content-api/]

%[https://beta.nextjs.org/docs/getting-started]

J'écris beaucoup d'articles sur Next. Si vous êtes intéressé par Next et les sujets connexes, vous pouvez me suivre sur [Medium](https://officialrajdeepsingh.medium.com/) et rejoindre la [publication frontend web](https://medium.com/frontendweb).