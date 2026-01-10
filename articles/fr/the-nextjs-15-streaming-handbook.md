---
title: Le manuel de diffusion Next.js 15 — SSR, React Suspense et Loading Skeleton
subtitle: ''
author: Sumit Saha
co_authors: []
series: null
date: '2025-08-06T17:57:38.220Z'
originalURL: https://freecodecamp.org/news/the-nextjs-15-streaming-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754503023167/aff9af73-7733-4525-8bf4-0ded59eceefa.png
tags:
- name: next.js streaming
  slug: nextjs-streaming
- name: nextjs-streaming-ssr
  slug: nextjs-streaming-ssr
- name: nextjs-loading
  slug: nextjs-loading
- name: nextjs-loading-skeleton
  slug: nextjs-loading-skeleton
- name: nextjs-suspense
  slug: nextjs-suspense
- name: nextjs-suspense-loading
  slug: nextjs-suspense-loading
- name: nextjs-loading-ui
  slug: nextjs-loading-ui
- name: Next.js
  slug: nextjs
- name: handbook
  slug: handbook
seo_title: Le manuel de diffusion Next.js 15 — SSR, React Suspense et Loading Skeleton
seo_desc: 'Next.js is currently one of the most popular and intelligent Web Frameworks
  out there. But many developers using Next.js often can’t fully utilise its superpowers
  simply because some of its advanced concepts are hard to understand.

  In this handbook, ...'
---

Next.js est actuellement l'un des Frameworks Web les plus populaires et intelligents. Mais de nombreux développeurs utilisant Next.js ne peuvent souvent pas exploiter pleinement ses superpouvoirs simplement parce que certains de ses concepts avancés sont difficiles à comprendre.

Dans ce manuel, vous allez plonger dans un concept avancé de Next.js appelé [Streaming](https://nextjs.org/learn/dashboard-app/streaming). Techniquement, il s'agit d'une fonctionnalité de React.js, mais lorsqu'elle est utilisée correctement avec Next.js, elle peut améliorer massivement l'expérience utilisateur de toute application web.

Après avoir lu ceci, vous comprendrez ce qu'est le streaming et comment il fonctionne. Vous serez également en mesure de mettre en œuvre une expérience utilisateur ultra fluide sur votre propre site web. Et votre application ? Elle sera ultra rapide et performante comme un champion ! Alors, sans plus attendre, commençons.

## Voici ce que nous allons couvrir

* [Prérequis](#heading-prerequisites)
    
* [Qu'est-ce que le Streaming](#heading-what-is-streaming) ?
    
* [Pourquoi le Streaming est important](#heading-why-streaming-matters)
    
* [Comment le Streaming fonctionne dans Next.js 15](#heading-how-streaming-works-in-nextjs-15)
    
* [Configuration du projet — Page de démonstration SSR](#heading-installation-demo-ssr-page)
    
    * [Page d'accueil](#heading-home-page)
        
    * [Page de démonstration du Streaming](#heading-streaming-demo-page)
        
    * [Composant ToolsCards](#heading-toolscards-component)
        
    * [Simuler un faux délai avec la fonction getTools()](#heading-simulate-fake-delay-with-gettools-function)
        
    * [Installation du composant Card Shadcn](#heading-installing-shadcn-card-component)
        
    * [Composant IconCard](#heading-iconcard-component)
        
    * [IconComponent](#heading-iconcomponent)
        
    * [Composant client LikeButton](#heading-likebutton-client-component)
        
* [Découverte des problèmes de SSR — UX et fausse interaction](#heading-discovering-ssr-issues-ux-and-false-interaction)
    
    * [Analyse des problèmes de SSR](#heading-breaking-down-ssr-issues)
        
* [Comment le Streaming peut résoudre le problème](#heading-how-streaming-can-solve-the-problem)
    
* [Deux types de Streaming dans Next.js](#heading-two-types-of-streaming-in-nextjs)
    
* [Streaming automatique de Next.js — loading.js](#heading-nextjs-automatic-streaming-loadingjs)
    
    * [Créer le fichier loading.js](#heading-create-the-loadingjs-file)
        
    * [Structurer le composant Loading Skeleton](#heading-structure-the-loading-skeleton-component)
        
    * [Composant CardSkeleton](#heading-cardskeleton-component)
        
    * [Rendre les cartes](#heading-render-the-cards)
        
    * [Comment le Streaming automatique a été appliqué](#heading-how-automatic-streaming-was-applied)
        
    * [Problèmes avec le Streaming automatique de Next.js](#heading-issues-with-nextjs-automatic-streaming)
        
* [Streaming manuel avec une frontière Suspense personnalisée](#heading-manual-streaming-with-custom-suspense-boundary)
    
    * [Supprimer Promise.all()](#heading-remove-promiseall)
        
    * [Comment implémenter Suspense pour la récupération de données concurrentes dans les composants Next.js](#heading-how-to-implement-suspense-for-concurrent-data-fetching-in-nextjs-components)
        
    * [Résumé des étapes pour implémenter le Streaming manuel dans Next.js](#heading-summary-of-steps-to-implement-manual-streaming-in-nextjs)
        
    * [Démonstration finale](#heading-final-demo)
        
* [Forcer le rendu dynamique pour un Streaming efficace](#heading-forcing-dynamic-rendering-for-effective-streaming)
    
* [Résumé](#heading-summary)
    

## Prérequis

Pour suivre et tirer le meilleur parti de ce guide, vous devez avoir :

1. Une compréhension de base de React.js, y compris les composants, les hooks (`useState`), et les props.
    
2. Une familiarité avec les concepts de Next.js tels que le routage, le répertoire `app`, et les composants serveur/client.
    
3. Une connaissance de base du rendu côté serveur (SSR) et de la génération de site statique (SSG) dans Next.js.
    
4. Une certaine expérience de travail avec JavaScript asynchrone, en particulier les Promesses et `async/await`.
    
5. Une compréhension générale de React Suspense et de son utilisation pour gérer le rendu asynchrone.
    
6. Un environnement de développement fonctionnel avec Node.js et npm/yarn installés.
    
7. Optionnel mais utile : Connaissance des bibliothèques de composants UI comme shadcn/ui, comme utilisé dans le projet d'exemple.
    

J'ai également créé une vidéo pour accompagner cet article. Si vous êtes du genre à aimer apprendre à partir de vidéos ainsi que de texte, vous pouvez la consulter ici :

%[https://youtu.be/xTT_Sd_xqh0] 

## Qu'est-ce que le Streaming ?

Imaginez aller sur un site web où la coque de la page se charge presque instantanément. Le contenu comme les images, le texte et les widgets s'écoule pièce par pièce dès qu'il est prêt. C'est le streaming en action.

Au lieu d'attendre que le serveur rassemble toutes les parties du HTML avant d'envoyer le tout en un seul gros lot, le streaming permet au serveur d'envoyer des blocs de balisage dès que chaque bloc finit de se rendre.

Du point de vue de l'utilisateur, la page est plus réactive — vous recevez un squelette ou un en-tête immédiatement, suivi du reste de l'UI qui se déploie sans une longue pause blanche.

## Pourquoi le Streaming est important

Utiliser le streaming apporte de nombreux avantages, comme :

* Vitesse perçue : Les premiers morceaux permettent au navigateur de rendre quelque chose d'utile immédiatement.
    
* Hydratation progressive : React peut hydrater les morceaux interactifs dès qu'ils sont reçus, réduisant le temps d'inactivité.
    
* Meilleure UX : Les utilisateurs peuvent lire ou interagir avec des parties de la page pendant que le reste se charge.
    
* Solutions de repli élégantes : Vous pouvez rendre des placeholders légers (skeletons de chargement) où les données sont en attente, puis échanger avec le contenu réel de manière transparente.
    

En divisant votre HTML en un flux plutôt qu'en un monolithe, vous optimisez à la fois les performances du réseau et du rendu. Et avec les API de streaming côté serveur de React 18 sous le capot, il est plus facile que jamais d'adopter ce modèle dans les frameworks modernes comme Next.js.

## Comment le Streaming fonctionne dans Next.js 15

Next.js 15 s'appuie fortement sur les capacités de streaming intégrées de React 18 et les rend disponibles avec une configuration minimale. Voici le flux de haut niveau :

### 1. Composants serveur et Suspense

Lorsque vous utilisez les composants serveur de React, Next.js peut commencer à rendre votre arbre de composants sur le serveur. Là où vous introduisez une frontière (ou implicitement via un fichier `loading.js`), React peut faire une pause, envoyer le HTML jusqu'à ce point, et le diffuser immédiatement au navigateur.

### 2. Streaming automatique vs manuel

Avec le streaming automatique, vous ajoutez un fichier `loading.js` à côté de n'importe quel segment de route ou de mise en page. Next.js le détectera, rendra d'abord votre squelette de chargement, et diffusera le reste de la page au fur et à mesure que les données deviennent disponibles.

Avec le streaming manuel, en revanche, vous enveloppez des parties spécifiques de votre UI dans des frontières de suspense au sein de vos composants serveur. Seuls ces segments diffusent indépendamment, vous donnant un contrôle granulaire.

### 3. HTML par morceaux sur HTTP

Sous le capot, Next.js utilise le streaming de réponse HTTP de Node. Au fur et à mesure que chaque composant serveur React se termine, Next.js envoie ce HTML dans le flux de réponse. Le navigateur du client commence à analyser immédiatement, et React hydrate le balisage en composants React interactifs à la volée.

### 4. Hydratation transparente

Parce que React sait exactement quels morceaux correspondent à quels composants, il peut hydrater de manière incrémentielle. Cela signifie que vous évitez le chargement en "cascade" où une grande étape d'hydratation bloque le reste de la page.

Dans les sections à venir, nous allons commencer par une simple **démo SSR** puis explorer les pièges courants de cette approche comme les fausses interactions et la mauvaise UX. Ensuite, nous résoudreons ces problèmes en utilisant le Streaming.

Nous couvrirons à la fois le Streaming Automatique avec `loading.js` et le Streaming Manuel via des frontières Suspense personnalisées, afin que vous puissiez choisir le modèle qui correspond à votre besoin. Vous aurez également des exemples de code pratiques pour rendre votre site Next.js 15 ultra rapide.

## Configuration du projet — Page de démonstration SSR

Commençons par un exemple simple. Pour commencer, mettons en place un simple projet Next.js. Exécutez les commandes suivantes dans votre terminal pour créer un modèle Next.js et exécuter le serveur `dev` :

```bash
npx create-next-app@latest nextjs-streaming-demo
cd nextjs-streaming-demo
npm run dev
```

### Page d'accueil

Une fois le serveur de développement en cours d'exécution, ouvrez le fichier `app/page.js` et mettez-le à jour avec le code suivant :

```javascript
// app/page.js
import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Home() {
    return (
        <div className="w-full min-h-screen flex justify-center items-center flex-col gap-24">
            <div>
                <h1 className="text-3xl lg:text-5xl font-bold text-center">
                    Next.js Streaming
                </h1>
            </div>
            <Link href="/streaming-demo" prefetch={false}>
                <Button size="lg" className="cursor-pointer">
                    Streaming Demo
                </Button>
            </Link>
        </div>
    );
}
```

Ce code crée une page d'accueil basique avec un titre "Next.js Streaming" et un lien intitulé "Streaming Demo" qui navigue vers la route `/streaming-demo`.

### Page de démonstration du Streaming

Maintenant, créons la page `streaming-demo`. Créez un autre fichier `page.js` à l'intérieur du dossier `app/streaming-demo` et écrivez le code ci-dessous à l'intérieur :

```javascript
// app/streaming-demo/page.js
import ToolsCards from "@/components/tools-cards";

export default function Home() {
    return (
        <div className="w-full min-h-screen flex justify-center items-center">
            <ToolsCards />
        </div>
    );
}
```

### Composant `ToolsCards`

Il n'y a vraiment pas grand-chose ici. C'est une simple page qui utilise un composant appelé `ToolsCard`. Maintenant, écrivez le code du composant `ToolsCard` :

```javascript
// components/tools-card.js
import IconCard from "@/components/icon-card";
import getTools from "@/lib/getTools";

const ToolsCards = async () => {
    const tools = await getTools();
    const toolsWithData = await Promise.all(tools);

    return (
        <div className="w-full max-w-4xl mx-auto px-4 sm:px-6">
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 grid-rows-2 gap-6 py-6">
                {toolsWithData.map((tool) => (
                    <IconCard key={tool} tool={tool} />
                ))}
            </div>
        </div>
    );
};

export default ToolsCards;
```

### Simuler un faux délai avec la fonction `getTools()`

Dans le composant `ToolsCard` ci-dessus, les outils sont récupérés à l'aide d'une fonction appelée `getTools()`. Maintenant, écrivons la fonction `getTools()` à l'intérieur d'un fichier appelé `lib/getTools.js` :

```javascript
// lib/getTools.js
const TOOLS = [
    "JavaScript",
    "React",
    "Vue",
    "Svelte",
    "Preact",
    "Angular",
    "Astro",
    "Flutter",
    "Solid",
];

const getTools = async () => {
    "use server";

    return TOOLS.map((tool) => generateToolsData(tool, DELAY));
};

export default getTools;
```

La fonction `getTools()` est une [Fonction Serveur](https://nextjs.org/docs/app/getting-started/updating-data#what-are-server-functions). Elle parcourt un tableau appelé `TOOLS`. Si vous vérifiez ce tableau `TOOLS`, il s'agit simplement d'un tableau de chaînes de caractères — des noms de différents outils comme JavaScript, React, Vue, et ainsi de suite.

En parcourant ce tableau `TOOLS`, chaque chaîne d'outil est passée dans une fonction appelée `generateToolsData()`. Cette fonction prend deux paramètres : le nom de l'outil et un délai. Nous avons défini ce délai à 3000 — ce qui signifie 3000 millisecondes ou 3 secondes. Maintenant, créons la fonction `generateToolsData()`. Son objectif principal est de simuler un faux délai :

```javascript
// lib/getTools.js
async function generateToolsData(tool, delay) {
    await new Promise((resolve) => setTimeout(resolve, Math.random() * delay));

    return tool;
}
```

La fonction `generateToolsData()` ci-dessus utilise `setTimeout()` et le multiplie par un nombre aléatoire et votre valeur de délai prédéfinie, de sorte que chaque élément subit un délai légèrement différent.

Pour simuler le délai, vous utilisez une `Promise` et vous l'attendez pour maintenir un comportement asynchrone. Donc, essentiellement, vous simulez que chaque outil prend un peu de temps à "s'accrocher". À cause de cela, la fonction `TOOLS.map()` retourne un tableau de `Promesses`. Puisque c'est une fonction `async`, elle retourne naturellement des `Promesses`.

Maintenant, revenez dans le fichier `tools-card.js`, et vous verrez que vous obtenez un tableau de `Promesses` de `getTools()`. Ensuite, vous passez ce tableau à `Promise.all()`, qui résout toutes les `Promesses` ensemble. Enfin, vous obtenez un tableau de chaînes de caractères — une pour chaque outil — mais chacune a eu un délai avant de se résoudre.

Donc, vous venez de simuler un délai de chargement en utilisant `async` `setTimeout()`. Mais dans la vraie vie, ce délai pourrait provenir de la récupération de données à partir d'une base de données, d'une requête réseau ou de l'appel à un serveur API externe. En gros, pour toute opération `async` qui prend du temps, vous venez de simuler ce comportement.

Maintenant, en utilisant le tableau `toolsWithData`, vous exécutez à nouveau un map(), et pour chaque outil (qui est juste une chaîne de caractères), vous rendez un composant `IconCard`. Le nom de l'outil est passé en tant que prop dans `IconCard`. IconCard peut être simplement un composant de présentation simple qui rend une carte. Vous pouvez utiliser le composant [`Card`](https://ui.shadcn.com/docs/components/card) de la bibliothèque UI [Shadcn](https://ui.shadcn.com/).

### Installation du composant Card Shadcn

Pour installer le composant `Card` de Shadcn, allez dans votre terminal, arrêtez le serveur `dev` de Next.js, et exécutez la commande suivante :

```bash
npx shadcn@latest add card
```

Suivez les instructions à l'écran, et félicitations ! Vous avez installé avec succès le composant `Card` de Shadcn dans votre projet. Redémarrez le serveur `dev` de Next.js.

### Composant `IconCard`

Maintenant, créez un nouveau fichier dans le dossier `components` appelé `icon-card.js` et écrivez le code suivant à l'intérieur :

```javascript
// components/icon-card.js
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import IconComponent from "./icon-component";
import LikeButton from "./like-button";

export default function IconCard({ tool }) {
    return (
        <Card className="w-full hover:cursor-pointer hover:shadow-md transition-all duration-200">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
                <div className="text-lg font-medium h-[28px] w-24">{tool}</div>
                <LikeButton />
            </CardHeader>
            <CardContent className="flex flex-col items-center justify-center py-6">
                <IconComponent id={tool} />
            </CardContent>
        </Card>
    );
}
```

Ici, vous pouvez voir un en-tête de carte affichant le nom de l'outil et un bouton "Like" à côté (qui est son propre composant séparé). Dans la zone de contenu de la carte en dessous, il y a une icône — rendue par un autre composant de présentation `IconComponent`. Il est maintenant temps d'écrire le code pour le `IconComponent` également.

### IconComponent

Créez un nouveau fichier `components/icon-component.js` et écrivez le code suivant :

```javascript
// components/icon-component.js
const icons = [
    {
        id: "Angular",
        icon: (
            <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 223 236"
            >
                <path
                    fill="url(#b)"
                    d="m222.08 39.2-8.02 125.91L137.39 0l84.69 39.2Zm-53.1 162.82-57.94 33.05-57.93-33.05 11.78-28.56h92.3l11.78 28.56ZM111.03 62.68l30.36 73.8H80.68l30.36-73.8ZM7.94 165.12 0 39.19 84.69 0 7.94 165.12Z"
                />
                <path
                    fill="url(#c)"
                    d="m222.08 39.2-8.02 125.91L137.39 0l84.69 39.2Zm-53.1 162.82-57.94 33.05-57.93-33.05 11.78-28.56h92.3l11.78 28.56ZM111.03 62.68l30.36 73.8H80.68l30.36-73.8ZM7.94 165.12 0 39.19 84.69 0 7.94 165.12Z"
                />
                <defs>
                    <linearGradient
                        id="b"
                        x1="49.01"
                        x2="225.83"
                        y1="213.75"
                        y2="129.72"
                        gradientUnits="userSpaceOnUse"
                    >
                        <stop stopColor="#E40035" />
                        <stop offset=".24" stopColor="#F60A48" />
                        <stop offset=".35" stopColor="#F20755" />
                        <stop offset=".49" stopColor="#DC087D" />
                        <stop offset=".74" stopColor="#9717E7" />
                        <stop offset="1" stopColor="#6C00F5" />
                    </linearGradient>
                    <linearGradient
                        id="c"
                        x1="41.02"
                        x2="156.74"
                        y1="28.34"
                        y2="160.34"
                        gradientUnits="userSpaceOnUse"
                    >
                        <stop stopColor="#FF31D9" />
                        <stop offset="1" stopColor="#FF5BE1" stopOpacity="0" />
                    </linearGradient>
                </defs>
            </svg>
        ),
    },
    {
        id: "Astro",
        icon: (
            <svg
                viewBox="0 0 85 107"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path
                    d="M27.5894 91.1365C22.7555 86.7178 21.3444 77.4335 23.3583 70.7072C26.8503 74.948 31.6888 76.2914 36.7005 77.0497C44.4375 78.2199 52.0359 77.7822 59.2232 74.2459C60.0454 73.841 60.8052 73.3027 61.7036 72.7574C62.378 74.714 62.5535 76.6892 62.318 78.6996C61.7452 83.5957 59.3086 87.3778 55.4332 90.2448C53.8835 91.3916 52.2437 92.4167 50.6432 93.4979C45.7262 96.8213 44.3959 100.718 46.2435 106.386C46.2874 106.525 46.3267 106.663 46.426 107C43.9155 105.876 42.0817 104.24 40.6845 102.089C39.2087 99.8193 38.5066 97.3081 38.4696 94.5909C38.4511 93.2686 38.4511 91.9345 38.2733 90.6309C37.8391 87.4527 36.3471 86.0297 33.5364 85.9478C30.6518 85.8636 28.37 87.6469 27.7649 90.4554C27.7187 90.6707 27.6517 90.8837 27.5847 91.1341L27.5894 91.1365Z"
                    fill="white"
                />
                <path
                    d="M27.5894 91.1365C22.7555 86.7178 21.3444 77.4335 23.3583 70.7072C26.8503 74.948 31.6888 76.2914 36.7005 77.0497C44.4375 78.2199 52.0359 77.7822 59.2232 74.2459C60.0454 73.841 60.8052 73.3027 61.7036 72.7574C62.378 74.714 62.5535 76.6892 62.318 78.6996C61.7452 83.5957 59.3086 87.3778 55.4332 90.2448C53.8835 91.3916 52.2437 92.4167 50.6432 93.4979C45.7262 96.8213 44.3959 100.718 46.2435 106.386C46.2874 106.525 46.3267 106.663 46.426 107C43.9155 105.876 42.0817 104.24 40.6845 102.089C39.2087 99.8193 38.5066 97.3081 38.4696 94.5909C38.4511 93.2686 38.4511 91.9345 38.2733 90.6309C37.8391 87.4527 36.3471 86.0297 33.5364 85.9478C30.6518 85.8636 28.37 87.6469 27.7649 90.4554C27.7187 90.6707 27.6517 90.8837 27.5847 91.1341L27.5894 91.1365Z"
                    fill="url(#paint0_linear_1_59)"
                />
                <path
                    d="M0 69.5866C0 69.5866 14.3139 62.6137 28.6678 62.6137L39.4901 29.1204C39.8953 27.5007 41.0783 26.3999 42.4139 26.3999C43.7495 26.3999 44.9325 27.5007 45.3377 29.1204L56.1601 62.6137C73.1601 62.6137 84.8278 69.5866 84.8278 69.5866C84.8278 69.5866 60.5145 3.35233 60.467 3.21944C59.7692 1.2612 58.5911 0 57.0029 0H27.8274C26.2392 0 25.1087 1.2612 24.3634 3.21944C24.3108 3.34983 0 69.5866 0 69.5866Z"
                    fill="white"
                />
                <defs>
                    <linearGradient
                        id="paint0_linear_1_59"
                        x1="22.4702"
                        y1="107"
                        x2="69.1451"
                        y2="84.9468"
                        gradientUnits="userSpaceOnUse"
                    >
                        <stop stopColor="#D83333" />
                        <stop offset="1" stopColor="#F041FF" />
                    </linearGradient>
                </defs>
            </svg>
        ),
    },
    {
        id: "Flutter",
        icon: (
            <svg
                viewBox="0 0 17 20"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path
                    d="M16.15 9.23H10l-5.38 5.39 3.07 3.07 8.46-8.46Z"
                    fill="#54C5F8"
                />
                <path
                    d="M3.08 13.08 0 10 10 0h6.15L3.08 13.08Z"
                    fill="#54C5F8"
                />
                <path
                    d="M7.7 17.7 10 20h6.15l-5.38-5.38-3.08 3.07Z"
                    fill="#01579B"
                />
                <path
                    d="m7.7 11.54-3.08 3.08 3.07 3.07 3.08-3.07-3.08-3.08Z"
                    fill="#29B6F6"
                />
            </svg>
        ),
    },
    {
        id: "JavaScript",
        icon: (
            <svg
                viewBox="-2 -2 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path d="M0 0h20v20H0V0Z" fill="#F7DF1E" />
                <path
                    d="M13.43 15.62c.41.67.92 1.14 1.87 1.14.76 0 1.27-.38 1.27-.92 0-.63-.5-.89-1.36-1.24l-.48-.22c-1.37-.57-2.25-1.3-2.25-2.82 0-1.4 1.08-2.48 2.73-2.48 1.2 0 2.06.41 2.7 1.5l-1.47.94c-.34-.57-.7-.79-1.23-.79-.54 0-.9.35-.9.8 0 .57.36.79 1.18 1.14l.45.19c1.62.7 2.5 1.4 2.5 2.95 0 1.68-1.33 2.63-3.1 2.63-1.75 0-2.9-.85-3.44-1.93l1.53-.9Zm-6.64.16c.29.54.58.98 1.21.98s1.02-.25 1.02-1.17V9.17h1.87v6.42c0 1.97-1.14 2.85-2.8 2.85a2.9 2.9 0 0 1-2.82-1.74l1.52-.92Z"
                    fill="#000"
                />
            </svg>
        ),
    },
    {
        id: "Preact",
        icon: (
            <svg
                viewBox="0 0 20 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path
                    d="m10 0 10 5.77v11.55l-10 5.77-10-5.77V5.77L10 0Z"
                    fill="#673AB8"
                />
                <path
                    d="M2.72 17.22c1.33 1.7 5.56.41 9.55-2.7 3.99-3.12 6.27-6.9 4.94-8.61-1.33-1.7-5.56-.4-9.55 2.71-3.99 3.12-6.27 6.9-4.94 8.6Zm.57-.44c-.44-.56-.25-1.67.6-3.07A17.8 17.8 0 0 1 8.1 9.2a17.8 17.8 0 0 1 5.41-3c1.56-.48 2.68-.4 3.12.16.44.57.25 1.68-.6 3.07a17.8 17.8 0 0 1-4.22 4.53 17.8 17.8 0 0 1-5.4 3c-1.57.48-2.69.4-3.13-.17Z"
                    fill="#fff"
                />
                <path
                    d="M17.2 17.22c1.34-1.7-.94-5.48-4.93-8.6-4-3.12-8.22-4.41-9.55-2.71-1.33 1.7.95 5.49 4.94 8.6 4 3.12 8.22 4.42 9.55 2.71Zm-.56-.44c-.44.57-1.56.65-3.12.17a17.8 17.8 0 0 1-5.41-3 17.8 17.8 0 0 1-4.23-4.53c-.84-1.4-1.03-2.5-.59-3.07.44-.56 1.56-.64 3.12-.16a17.8 17.8 0 0 1 5.41 3 17.8 17.8 0 0 1 4.23 4.52c.84 1.4 1.03 2.5.59 3.07Z"
                    fill="#fff"
                />
                <path
                    d="M9.96 13.1a1.53 1.53 0 1 0 0-3.06 1.53 1.53 0 0 0 0 3.06Z"
                    fill="#fff"
                />
            </svg>
        ),
    },
    {
        id: "React",
        icon: (
            <svg
                viewBox="0 0 23 21"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path
                    d="M11.5 12.3a2 2 0 1 0 0-4.1 2 2 0 0 0 0 4Z"
                    fill="#61DAFB"
                />
                <path
                    d="M11.5 14.4c6 0 11-1.8 11-4.2 0-2.3-5-4.2-11-4.2s-11 2-11 4.2c0 2.4 5 4.2 11 4.2Z"
                    stroke="#61DAFB"
                />
                <path
                    d="M7.9 12.3c3 5.3 7 8.6 9.1 7.5 2-1.2 1.2-6.4-1.9-11.7C12.1 3 8.1-.5 6 .7 4 2 4.8 7.1 7.9 12.3Z"
                    stroke="#61DAFB"
                />
                <path
                    d="M7.9 8.1c-3 5.3-4 10.5-1.9 11.7 2 1.1 6.1-2.2 9.1-7.5 3-5.2 4-10.4 1.9-11.6C15-.5 10.9 3 7.9 8.1Z"
                    stroke="#61DAFB"
                />
            </svg>
        ),
    },
    {
        id: "Solid",
        icon: (
            <svg
                viewBox="0 0 32 30"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <g clipPath="url(#a)">
                    <path
                        d="M31.42 6.75S21.2-.77 13.3.96l-.58.2a5.48 5.48 0 0 0-2.7 1.73l-.38.58-2.9 5.01 5.02.97c2.12 1.35 4.82 1.92 7.32 1.35l8.87 1.73 3.47-5.78Z"
                        fill="#76B3E1"
                    />
                    <path
                        opacity=".3"
                        d="M31.42 6.75S21.2-.77 13.3.96l-.58.2a5.48 5.48 0 0 0-2.7 1.73l-.38.58-2.9 5.01 5.02.97c2.12 1.35 4.82 1.92 7.32 1.35l8.87 1.73 3.47-5.78Z"
                        fill="url(#b)"
                    />
                    <path
                        d="m10.02 6.75-.77.19c-3.27.96-4.24 4.05-2.5 6.75 1.92 2.5 5.97 3.85 9.25 2.89l11.95-4.05S17.73 5.01 10.02 6.75Z"
                        fill="#518AC8"
                    />
                    <path
                        opacity=".3"
                        d="m10.02 6.75-.77.19c-3.27.96-4.24 4.05-2.5 6.75 1.92 2.5 5.97 3.85 9.25 2.89l11.95-4.05S17.73 5.01 10.02 6.75Z"
                        fill="url(#c)"
                    />
                    <path
                        d="M25.83 15.42a8.67 8.67 0 0 0-9.25-2.89L4.63 16.39.77 23.13l21.6 3.67 3.85-6.94c.77-1.35.58-2.9-.39-4.44Z"
                        fill="url(#d)"
                    />
                    <path
                        d="M21.98 22.17a8.67 8.67 0 0 0-9.26-2.9L.77 23.14S11 30.84 18.9 28.92l.58-.2c3.28-.96 4.43-4.05 2.5-6.55Z"
                        fill="url(#e)"
                    />
                </g>
                <defs>
                    <linearGradient
                        id="b"
                        x1="5.3"
                        y1=".58"
                        x2="29.3"
                        y2="12.24"
                        gradientUnits="userSpaceOnUse"
                    >
                        <stop offset=".1" stopColor="#76B3E1" />
                        <stop offset=".3" stopColor="#DCF2FD" />
                        <stop offset="1" stopColor="#76B3E1" />
                    </linearGradient>
                    <linearGradient
                        id="c"
                        x1="18.47"
                        y1="6.28"
                        x2="14.27"
                        y2="20.28"
                        gradientUnits="userSpaceOnUse"
                    >
                        <stop stopColor="#76B3E1" />
                        <stop offset=".5" stopColor="#4377BB" />
                        <stop offset="1" stopColor="#1F3B77" />
                    </linearGradient>
                    <linearGradient
                        id="d"
                        x1="3.55"
                        y1="12.38"
                        x2="27.82"
                        y2="28.88"
                        gradientUnits="userSpaceOnUse"
                    >
                        <stop stopColor="#315AA9" />
                        <stop offset=".5" stopColor="#518AC8" />
                        <stop offset="1" stopColor="#315AA9" />
                    </linearGradient>
                    <linearGradient
                        id="e"
                        x1="14.5"
                        y1="14.36"
                        x2="4.7"
                        y2="50.27"
                        gradientUnits="userSpaceOnUse"
                    >
                        <stop stopColor="#4377BB" />
                        <stop offset=".5" stopColor="#1A336B" />
                        <stop offset="1" stopColor="#1A336B" />
                    </linearGradient>
                    <clipPath id="a">
                        <path fill="#fff" d="M0 0h32v29.94H0z" />
                    </clipPath>
                </defs>
            </svg>
        ),
    },
    {
        id: "Svelte",
        icon: (
            <svg
                viewBox="0 0 20 25"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path
                    d="M18.7 3.2A7.3 7.3 0 0 0 9 1L3.3 4.6A6.4 6.4 0 0 0 .4 9c-.3 1.5 0 3 .7 4.4a6.4 6.4 0 0 0-1 5c.3 1 .6 1.8 1.2 2.5A7.3 7.3 0 0 0 11 23l5.6-3.6a6.4 6.4 0 0 0 2.9-4.3c.3-1.5 0-3-.7-4.3a6.5 6.5 0 0 0 1-5.1c-.3-1-.6-1.8-1.2-2.5"
                    fill="#FF3E00"
                />
                <path
                    d="M8.4 21.2a4.4 4.4 0 0 1-5.5-3.3 4.1 4.1 0 0 1 .1-2.1l.1-.4.3.2c.7.5 1.4.9 2.2 1.1l.2.1v.2c0 .3 0 .6.2.8a1.3 1.3 0 0 0 1.5.6l.3-.2 5.6-3.5a1.2 1.2 0 0 0 .5-1.3l-.2-.5a1.3 1.3 0 0 0-1.4-.5c-.2 0-.3 0-.4.2l-2.1 1.3-1.2.5a4.4 4.4 0 0 1-5.4-3.2A4.1 4.1 0 0 1 3.8 8c.3-.5.7-.9 1.1-1.2l5.6-3.5a4 4 0 0 1 1.1-.5A4.4 4.4 0 0 1 17.1 6a4.1 4.1 0 0 1-.1 2.2l-.1.3-.3-.2c-.7-.5-1.4-.9-2.2-1.1h-.2V7c0-.3 0-.6-.2-.8a1.3 1.3 0 0 0-1.8-.4L6.6 9.4a1.2 1.2 0 0 0-.5 1.3l.2.4a1.3 1.3 0 0 0 1.4.5l.4-.1 2.1-1.4a4 4 0 0 1 1.2-.5 4.4 4.4 0 0 1 5.4 3.3c.1.5.1 1 0 1.6a3.9 3.9 0 0 1-1.7 2.6l-5.6 3.6-1.1.5"
                    fill="#fff"
                />
            </svg>
        ),
    },
    {
        id: "Vue",
        icon: (
            <svg
                viewBox="0 0 24 20"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path
                    d="m14.2 0-2.7 4.6L9 0H0l11.5 20L23.1 0h-8.9Z"
                    fill="#41B883"
                />
                <path
                    d="m14.2 0-2.7 4.6L9 0H4.6l7 12 6.9-12h-4.3Z"
                    fill="#34495E"
                />
            </svg>
        ),
    },
];

export default function IconComponent({ id }) {
    const icon = icons.find((icon) => icon.id === id);

    return <div className="h-24 w-24 text-gray-600 mb-4">{icon.icon}</div>;
}
```

Si vous vérifiez le code pour le `IconComponent`, vous verrez qu'il a un tableau d'icônes SVG. En utilisant la méthode `find()`, il sélectionne l'icône appropriée et la rend.

### Composant client `LikeButton`

Dans le fichier `icon-card.js`, il y a un autre composant appelé `LikeButton`. Écrivons le code pour celui-ci :

```javascript
// components/like-button.js
"use client";

import { Button } from "@/components/ui/button";
import { Heart } from "lucide-react";
import { useState } from "react";

export default function LikeButton() {
    const [liked, setLiked] = useState(false);

    return (
        <Button
            variant="ghost"
            size="icon"
            onClick={(e) => {
                e.stopPropagation();
                setLiked(!liked);
            }}
            className="h-10 w-10"
        >
            <Heart
                className={`h-5 w-5 ${
                    liked ? "fill-red-500 text-red-500" : "text-gray-500"
                }`}
            />
        </Button>
    );
}
```

Remarquez qu'il commence par la directive `'use client'`, car ce bouton gère l'interaction côté client. Il a un événement `onClick` attaché — donc lorsque vous cliquez dessus, un signe "love" apparaît. Cette interaction se produit entièrement côté client. C'est pourquoi vous avez dû le définir comme un [Composant Client](https://react.dev/reference/rsc/use-client).

À l'intérieur du composant, vous utilisez un simple hook `useState()` avec la variable d'état `like` et la fonction `setLike`. Lorsque le bouton est cliqué, vous basculez l'état `like` — s'il est `true`, il devient `false`, et vice versa. Il y a aussi du CSS conditionnel — si like est `true`, le bouton devient "rouge". Sinon, il reste "gris".

## Découverte des problèmes de SSR — UX et fausse interaction

Maintenant, vérifiez votre navigateur. Vous verrez, sur la page d'accueil, que vous avez un titre qui dit "Next.js Streaming". En dessous, il y a un bouton lié à une page appelée "Streaming Demo".

Maintenant, remarquez ce qui se passe lorsque vous cliquez sur le bouton "Streaming Demo" — vous cliquez dessus, mais la page prend un peu de temps à se charger. Et honnêtement, l'expérience utilisateur ici est terrible. Parce que du point de vue d'un utilisateur régulier, il n'est pas clair si le clic a même fonctionné.

![Découverte des problèmes de SSR](https://cdn.hashnode.com/res/hashnode/image/upload/v1754078491159/c3c17d5d-add0-4a1b-973e-cdcd7f4b7533.gif align="center")

Alors, qu'est-ce qui cause ce délai de chargement de la page ? Eh bien, c'est parce que les cartes sur cette page sont chargées dynamiquement. Vous verrez le code bientôt et cela aura plus de sens. Mais ce processus de chargement se fait de manière asynchrone. Et puisque tout dans la page est rendu sur le serveur — ce qui, comme vous le savez peut-être, se passe à l'intérieur du composant `App` dans Next.js — il est rendu en tant que [Composant Serveur](https://react.dev/reference/rsc/server-components).

Maintenant, nous avons deux problèmes principaux ici :

1. Lorsque je clique sur le bouton "Streaming Demo" depuis la page d'accueil, j'ai une mauvaise expérience utilisateur. Après avoir cliqué, je dois attendre — parce que la page prend du temps à se charger.
    
2. Le deuxième problème s'appelle une **Fausse Interaction**. Imaginez ceci : pendant que la page est encore en train de se charger, vous la rechargez et cliquez sur une carte pour lui donner une réaction d'amour. Mais une fois que la page a fini de se charger, cette réaction d'amour a disparu. Cela signifie que vous venez d'avoir une fausse interaction — et cela peut confondre vos utilisateurs. Pourquoi ? Parce que techniquement, la page s'est réhydratée et a remplacé tout — et l'interaction n'a pas persisté. C'est exactement ce que vous entendez par une fausse interaction. Et cela se produit à cause du **Rendu Côté Serveur (SSR)**. C'est l'un de ces inconvénients UX du SSR.
    

![Fausse Interaction - SSR](https://cdn.hashnode.com/res/hashnode/image/upload/v1754078793243/44fcd1d1-a58f-427c-a2f3-a3c5749fb3fc.gif align="center")

### Analyse des problèmes de SSR

Permettez-moi de le décomposer. Lorsque quelqu'un accède à cette page, la requête va d'abord au serveur. Ensuite, toutes les opérations `async` commencent. Nous appelons cela la **phase A**. Une fois que c'est fait, le HTML est généré — nous pouvons appeler cela la **phase B**. Ensuite, le HTML et le CSS atteignent le navigateur — appelons cela **C**. Et enfin, une fois que le bundle JS est entièrement chargé dans le navigateur, vous atteignez la phase d'Hydratation.

Maintenant, si ces termes (comme **Rendu de Page** et **Hydratation**) ne sont pas clairs pour vous, j'ai récemment fait une [vidéo complète couvrant le rendu et la mise en cache de Next.js](https://youtu.be/g3nj8SIO7Vs). C'est un must pour tout développeur Next.js, React, ou web en général. Vous apprendrez comment votre page web est rendue, comment l'Hydratation fonctionne, et comment tout le processus de rendu est coordonné entre le navigateur et le serveur.

Tout deviendra clair pour vous. Alors assurez-vous de regarder cette vidéo si quelque chose vous semble confus.

![Rendu Côté Serveur (SSR)](https://cdn.hashnode.com/res/hashnode/image/upload/v1754079434726/99146526-1387-405d-9b1d-228d29b27128.png align="center")

Revenons au point principal. Vous devriez maintenant comprendre que le Rendu Côté Serveur implique plusieurs tâches bloquantes. Cela signifie que pendant que les données sont en cours de récupération, rien d'autre ne progresse. Jusqu'à ce que cela soit fait, la page ne peut pas se rendre. Et si la page n'est pas rendue, rien n'atteint le navigateur. Et sans cela, l'hydratation ne peut pas commencer.

![Comportement bloquant du SSR](https://cdn.hashnode.com/res/hashnode/image/upload/v1754079470587/15e69637-a83f-4abe-bc0f-1e5c9fc86782.png align="center")

Ces étapes ne peuvent pas s'exécuter simultanément — elles doivent se produire les unes après les autres. C'est pourquoi vous voyez ce problème. Supposons que notre page a 9 cartes. Peut-être que certaines cartes auraient pu se charger plus tôt, mais la page complète attend que les 9 soient prêtes. Résultat ? Nous voyons tout en même temps — à la toute fin. Ne serait-ce pas génial si nous pouvions améliorer cette expérience utilisateur ? C'est là que le **Streaming** entre en jeu.

## Comment le Streaming peut résoudre le problème

![SSR - Mauvaise UX](https://cdn.hashnode.com/res/hashnode/image/upload/v1754079647605/23b58563-1583-464b-b4d2-1d3c837d8c3c.gif align="center")

Il y a quelques instants dans la démonstration, vous avez vu toute l'interface utilisateur se charger en une seule fois. De l'extérieur, il semblait que tous les composants se rendaient ensemble — mais en réalité, chaque partie de votre page est rendue séparément. Parce que dans React, tout est basé sur des composants, n'est-ce pas ?

Maintenant, que se passerait-il si le **Composant A** se termine tôt ? Ne serait-ce pas génial si vous pouviez simplement envoyer le **Composant A** au navigateur immédiatement ? Pendant ce temps, les **Composants B**, **C**, et ainsi de suite sont encore en cours de traitement — et une fois qu'ils sont prêts, ils diffusent ensuite ! C'est exactement comment le **Streaming** fonctionne.

Le rendu côté serveur est définitivement plus rapide que le **rendu côté client**. Mais le vrai problème avec le SSR est l'expérience utilisateur. C'est pourquoi nous utilisons le Streaming.

Pensez à YouTube. Lorsque vous jouez une vidéo, est-ce qu'elle se télécharge entièrement avant de commencer ? Bien sûr que non ! La vidéo joue immédiatement, et le reste continue de se charger par morceaux — c'est la mise en mémoire tampon. En tant qu'utilisateur, vous ne ressentez aucun décalage — c'est une expérience super fluide. Vous voulez la même expérience sur vos pages web, et c'est exactement ce que le Streaming offre.

![Streaming en Action](https://cdn.hashnode.com/res/hashnode/image/upload/v1754079758843/1f1130f4-351a-4b80-8205-b56550c53232.png align="center")

Comme vous pouvez le voir ci-dessus, la section de la barre latérale de l'interface utilisateur est déjà chargée. Mais le contenu du côté droit est toujours en état de chargement. C'est exactement le genre d'expérience que vous voulez construire — où des parties de la page se chargent indépendamment, dès qu'elles sont prêtes. Et cela est définitivement mieux que le SSR traditionnel, car il offre aux utilisateurs une expérience beaucoup plus fluide.

Maintenant, voici quelque chose d'important : le streaming ne fonctionne qu'avec les **composants serveur**. Pour implémenter cela, React nous donne un outil appelé [React Suspense](https://react.dev/reference/react/Suspense). Vous allez maintenant apprendre à utiliser React Suspense pour améliorer votre démonstration actuelle et voir comment vous pouvez porter cette expérience de streaming au niveau supérieur.

## Deux types de Streaming dans Next.js

Permettez-moi de vous ramener au code. La première chose que vous allez faire est de récupérer la démonstration que je vous ai montrée plus tôt — c'est notre code de départ. J'ai sauvegardé ce code de départ exact dans la branche `starter` du [dépôt GitHub](https://github.com/logicbaselabs/nextjs-streaming).

Donc, à partir de la branche `starter`, vous obtiendrez le code exact avec lequel vous commencez. Maintenant, pour implémenter le streaming, vous allez commencer par le système de Streaming par défaut de Next.js. Il y a deux façons de faire du Streaming dans Next.js :

1. **Le streaming par défaut ou automatique**, où vous n'avez vraiment rien à configurer — vous suivez simplement une convention simple.
    
2. **Le streaming personnalisé ou avancé**, où vous configurez les choses manuellement.
    

## Streaming automatique de Next.js — `loading.js`

Je vais d'abord vous montrer la démonstration du Streaming Automatique. Ensuite, je vous expliquerai comment fonctionne le streaming personnalisé. Chaque approche aura sa propre branche séparée. Le code de départ principal reste dans la branche `starter`. Maintenant, créez une nouvelle branche et appelez-la « automatic-streaming », pour la démonstration du Streaming Automatique. Toutes les modifications de code que je fais à partir de maintenant iront dans cette branche automatique.

```bash
git checkout -b automatic-streaming
```

### Créer le fichier `loading.js`

Tout d'abord, à l'intérieur du dossier `streaming-demo`, vous allez créer un fichier `loading.js`. À l'intérieur, vous allez retourner du JSX régulier comme dans n'importe quelle page React standard.

Mais au lieu de simplement afficher du texte comme « Loading... », vous allez adopter l'approche moderne et construire une **UI Skeleton**. Cela signifie que vous allez imiter la même structure des cartes réelles — mais au lieu du contenu réel, vous allez afficher des placeholders squelettes. Ainsi, les utilisateurs verront quelque chose de façonné exactement comme la vraie carte, mais il sera dans un état de chargement.

Lorsque les vraies données arrivent, elles remplaceront le placeholder à cet endroit exact. C'est ainsi que vous allez construire l'interface utilisateur de chargement squelette — tout comme les applications web modernes le font pour une meilleure expérience utilisateur.

### Structurer le composant Loading Skeleton

Implémentons maintenant le même type de squelettes de chargement que les applications modernes utilisent. Si vous allez dans le composant `Home` à l'intérieur du fichier `app/streaming-demo/page.js`, vous verrez que tout commence par `ToolsCard`, n'est-ce pas ? Il y a un `div` wrapper — `<div className="w-full min-h-screen flex justify-center items-center">` — vous aurez besoin de cela comme conteneur extérieur.

Donc, tout d'abord, copiez ce `div` conteneur du composant `Home` et collez-le dans le fichier `loading.js`. C'est votre wrapper extérieur. Compris ?

Ensuite, il y a deux `div` imbriqués à l'intérieur de `ToolsCard` — `<div className="w-full max-w-4xl mx-auto px-4 sm:px-6"><div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 grid-rows-2 gap-6 py-6">` — vous aurez besoin de ceux-ci aussi. Copiez les deux et collez-les en tant qu'enfants à l'intérieur du wrapper extérieur dans `loading.js`. Assurez-vous de fermer correctement les balises de fin manquantes. C'est tout — la structure complète est prête.

```javascript
// app/streaming-demo/loading.js
<div className="w-full min-h-screen flex justify-center items-center">
    <div className="w-full max-w-4xl mx-auto px-4 sm:px-6">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 grid-rows-2 gap-6 py-6">
            <!-- content goes here -->
        </div>
    </div>
</div>
```

### Composant `CardSkeleton`

Maintenant, vous devez insérer 9 cartes à l'intérieur de cette mise en page, tout comme l'interface utilisateur. Pour comprendre à quoi doit ressembler chaque carte, ouvrons le fichier `icon-card.js`. Vous remarquerez que chaque carte est simplement un `IconCard`, n'est-ce pas ? Donc vous allez utiliser cette même structure pour construire vos squelettes de chargement.

Pour gagner du temps, laissez-moi partager le code pour le composant `CardSkeleton` à l'intérieur du dossier `components`/ui — nommé `card-skeleton.jsx`. À l'intérieur de ce composant, j'utilise le composant [`Skeleton`](https://ui.shadcn.com/docs/components/skeleton) de Shadcn. Très simple !

```javascript
// components/ui/card-skeleton.jsx
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";

const CardSkeleton = () => {
    return (
        <Card className="w-full hover:cursor-pointer hover:shadow-md transition-all duration-200">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
                <Skeleton className="h-[28px] w-24" />
                <Skeleton className="h-10 w-10 rounded-full" />
            </CardHeader>
            <CardContent className="flex flex-col items-center justify-center py-6">
                <Skeleton className="h-24 w-24 rounded-md mb-4" />
            </CardContent>
        </Card>
    );
};

export default CardSkeleton;
```

### Rendre les cartes

Sur l'interface utilisateur, vous avez 9 cartes au total. Donc vous allez rendre 9 de ces cartes squelettes. Comment ? À l'intérieur de `loading.js`, vous allez utiliser `Array.from({length : 9})` pour créer un tableau vide de 9 éléments. Ensuite, vous allez utiliser `map()` dessus. Puisque vous n'avez pas besoin des éléments réels du tableau, vous pouvez utiliser un `underscore _` comme variable. Et pour définir une `key` pour chaque composant, vous allez prendre l'index comme deuxième paramètre. Pour chaque itération, vous allez retourner un composant avec la `key` correspondante. Et c'est tout ! Votre composant de chargement basé sur des squelettes est prêt.

```javascript
// app/streaming-demo/loading.js
import CardSkeleton from "@/components/ui/card-skeleton";

export default function Loading() {
    return (
        <div className="w-full min-h-screen flex justify-center items-center">
            <div className="w-full max-w-4xl mx-auto px-4 sm:px-6">
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 grid-rows-2 gap-6 py-6">
                    {Array.from({ length: 9 }).map((_, index) => (
                        <CardSkeleton key={index} />
                    ))}
                </div>
            </div>
        </div>
    );
}
```

### Comment le Streaming automatique a été appliqué

Maintenant, rechargeons la page de démonstration du Streaming. Remarquez que l'expérience de chargement est déjà en action ! Plus de problèmes avec les fausses interactions. Cela signifie que vous ne pouvez plus cliquer sur le bouton "Like" pendant qu'il est en train de charger, car l'interface utilisateur réelle n'a pas encore été rendue.

Donc en réalité, vous n'avez pas fait grand-chose. Vous avez simplement créé un fichier `loading.js` à l'intérieur du dossier `app/streaming-demo`. Et cela seul a déclenché le Streaming Automatique dans Next.js. Comment ?

Jetons un coup d'œil. Vous vous souvenez de ce que vous avez fait ? Vous avez créé un fichier `loading.js`, n'est-ce pas ? Grâce à cette structure de fichier, en coulisses Next.js enveloppe automatiquement le composant de page avec une frontière React Suspense.

![Streaming Automatique avec loading.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1754079977767/5aea584f-3045-4539-ac67-e647e3afb304.png align="center")

Jetez un coup d'œil au côté gauche du diagramme ci-dessus : le composant `Page` est enveloppé dans `Suspense` des deux côtés. Et le `fallback` utilisé là est notre composant `Loading` personnalisé. Tout cet enveloppement est fait automatiquement par Next.js. Vous auriez pu le faire manuellement en écrivant explicitement le composant `Suspense` et son `fallback` — et cela aurait fonctionné aussi. Mais vous n'avez pas eu à le faire, parce que vous utilisez Next.js, un framework intelligent.

Next.js dit essentiellement :

> Vous n'avez pas à faire tout le travail. Il suffit de placer un fichier `loading.js` dans le dossier — je m'occupe du reste pour vous.

Et en interne, il enveloppe votre page avec une frontière `Suspense`. C'est ainsi que le Streaming Automatique est appliqué. Et cela vous a donné une expérience utilisateur beaucoup plus fluide. Là où une partie de la page est prête, elle est montrée immédiatement.

### Problèmes avec le Streaming Automatique de Next.js

Mais regardez de plus près : toute la page apparaît toujours ensemble. Jusqu'à ce moment-là, vous ne voyez que des squelettes comme fallback pour tout. C'est définitivement une amélioration par rapport à la version précédente. Mais... cela pourrait encore être mieux.

Pourquoi ? Parce que les cartes sur la page ne prennent pas toutes le même temps pour se rendre. Peut-être que la carte "JavaScript" se résout rapidement. Mais la carte "Vue.js" prend le plus de temps. Et le délai causé par la carte "Vue.js" affecte la visibilité même de la carte "JavaScript", car toutes les cartes sont affichées ensemble.

Ne serait-ce pas mieux si vous aviez un contrôle de rendu au niveau de chaque carte ? Comment pouvez-vous faire cela ? Simple : si vous enveloppez chaque carte dans sa propre frontière Suspense, vous obtiendrez cette expérience.

Mais avant de vous lancer, analysons le problème réel ici. Actuellement, la "Carte 1" termine les étapes "A", "B", "C", "D" — puis la "Carte 2" commence. Ensuite la "Carte 3". En gros, les cartes se chargent en série.

![Rendu Sériel](https://cdn.hashnode.com/res/hashnode/image/upload/v1754080238122/8e3ca78a-cc44-4f31-806f-3c1554bdc26c.png align="center")

Mais ce que vous voulez, c'est que chaque carte soit dans sa propre frontière Suspense, afin qu'elles puissent se charger de manière concurrente. Celle qui se termine en premier devrait apparaître immédiatement. Et c'est exactement ce que vous allez implémenter ensuite. Vous allez modifier le code et voir exactement quelles modifications sont nécessaires pour que cela fonctionne parfaitement.

![Rendu Concurrent](https://cdn.hashnode.com/res/hashnode/image/upload/v1754080259781/4612905e-516d-452b-a6ec-97c0ef3c9ec1.png align="center")

## Streaming Manuel avec une Frontière Suspense Personnalisée

Retour dans le code maintenant. Avant d'implémenter cette fonctionnalité avancée, engageons l'état actuel de votre code sur GitHub afin que vous puissiez expérimenter et l'ajuster vous-même. Dans le terminal, écrivons ce qui suit :

```bash
git add .
git commit -m "Automatic Streaming"
```

Terminé ! Vous trouverez maintenant le code sous la branche `'automatic-streaming'` dans le [dépôt GitHub](https://github.com/logicbaselabs/nextjs-streaming/tree/automatic-streaming). Passons maintenant à l'apprentissage du **Streaming Personnalisé**. Pour cela, je crée une nouvelle branche :

```bash
git checkout -b custom-streaming
```

Notre nouvelle branche `custom-streaming` est prête. Démarrons notre serveur de développement Next.js :

```bash
npm run dev
```

### Supprimer `Promise.all()`

Puisque vous allez maintenant diffuser manuellement, supprimez d'abord le fichier `loading.js`. Donc, ce fallback de streaming par défaut avec les Card Skeletons ? C'est parti maintenant.

Ensuite, ouvrons le fichier `tools-card.js`. Ici, vous appelez la fonction `getTools()`, qui retourne un tableau de `Promesses`. Auparavant, vous utilisiez `Promise.all()` pour les résoudre toutes en une seule fois. Mais cette fois, vous n'avez plus besoin de le faire. Pourquoi ? Parce que vous allez envelopper chaque composant `IconCard` dans sa propre frontière `Suspense`. Cela signifie que React Suspense gérera la résolution de la promesse pour chaque carte individuellement.

Donc voici ce que vous allez faire :

* Tout d'abord, coupez le composant `<IconCard ... />`. Vous le réutiliserez bientôt.
    
* Ensuite, au lieu de `toolsWithData` — qui est le tableau résolu que vous avez obtenu en utilisant `Promise.all()` — vous allez maintenant directement parcourir le tableau `tools` (qui contient les `Promesses` non résolues).
    

Donc vous pouvez supprimer entièrement la logique `toolsWithData`. Maintenant, dans votre JSX, vous allez remplacer l'ancien `toolsWithData.map()` par `tools.map()`.

### Comment implémenter Suspense pour la récupération de données concurrentes dans les composants Next.js

Auparavant, chaque élément dans la boucle était une `string` résolue appelée `tool`. Mais maintenant, puisque vous traitez avec des `Promesses` non résolues, renommons cette variable en `toolPromise`. Vous allez également récupérer le deuxième argument `index` afin de pouvoir l'utiliser comme clé.

Maintenant, dans l'instruction return de la fonction `map()`, vous allez retourner un `<Suspense></Suspense>` pour chaque itération. À l'intérieur de chaque `Suspense`, vous allez rendre un composant enfant appelé `<ToolCard></ToolCard>`. Vous n'avez pas encore créé le composant `ToolCard` — mais vous allez le faire dans un instant. Vous allez passer `toolPromise` comme prop au composant `ToolCard`.

```javascript
// components/tools-cards.js
const ToolsCards = async () => {
    const toolsPromise = await getTools();

    return (
        <div className="w-full max-w-4xl mx-auto px-4 sm:px-6">
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 grid-rows-2 gap-6 py-6">
                {toolsPromise.map((toolPromise, index) => (
                    <Suspense>
                        <ToolsCard toolPromise={toolPromise} />
                    </Suspense>
                ))}
            </div>
        </div>
    );
};
```

Alors, que se passe-t-il ici ?

* `toolsPromise` est un tableau de `Promesses`
    
* Vous parcourez ce tableau
    
* À chaque itération, vous obtenez une `toolPromise` et un `index`
    
* Puisque `toolPromise` prend du temps à se résoudre, vous l'enveloppez dans un `<Suspense>`
    
* À l'intérieur de ce `Suspense`, vous rendez le composant `ToolCard`
    
* Et vous passez `toolPromise` comme prop
    

J'espère que cette partie est claire. Maintenant, vous allez créer le composant `ToolCard`. Mais avant cela, vous devez définir un `fallback` à l'intérieur du composant `Suspense`. Le fallback signifie que tant que le composant enfant à l'intérieur de Suspense n'a pas terminé la résolution de sa `Promise`, cette interface utilisateur de fallback sera affichée à la place. Donc vous pouvez utiliser `<CardSkeleton />` comme composant de fallback. Cela signifie que, jusqu'à ce que la Promise soit résolue, les utilisateurs verront le composant `CardSkeleton`. De plus, vous devez définir une `key` pour chaque élément — et ici, vous pouvez utiliser l'`index` comme `key`.

```javascript
// // components/tools-cards.js
{toolsPromise.map((toolPromise, index) => (
    <Suspense fallback={<CardSkeleton />} key={index}>
        <ToolsCard toolPromise={toolPromise} />
    </Suspense>
))}
```

D'accord, créons maintenant le composant `ToolCard`. Vous allez le définir dans le même fichier, juste à l'extérieur du composant `ToolsCard`. Écrivons ce qui suit :

```javascript
const ToolCard = () => {
    // code goes here
}
```

À l'intérieur de la fonction, vous allez recevoir `toolPromise` comme prop. Maintenant, vous allez utiliser le hook `use()` de React. Vous allez passer `toolPromise` dans `use()`, et il retournera les données résolues. Vous allez les stocker dans une variable appelée `tool`. Ensuite, vous allez retourner du JSX :

```javascript
const ToolsCard = ({ toolPromise }) => {
    const tool = use(toolPromise);

    // return JSX here
};
```

Vous vous souvenez du composant `IconCard` que vous avez coupé plus tôt ? Il devrait encore être dans votre presse-papiers. Vous allez simplement le retourner ici et vous allez passer l'outil résolu `tool` comme prop dans `IconCard`.

```javascript
const ToolsCard = ({ toolPromise }) => {
    const tool = use(toolPromise);

    return <IconCard tool={tool} />;
};
```

### Résumé des étapes pour implémenter le Streaming Manuel dans Next.js

D'accord, prenons un moment pour bien comprendre ce que vous venez de faire. Auparavant, vous preniez le tableau de Promesses retourné par la fonction `getTools()` et vous les résolviez toutes en une seule fois en utilisant `Promise.all()`. Ce n'est qu'après que toutes étaient résolues que vous rendiez les composants.

Mais maintenant, vous n'utilisez plus `Promise.all()`. Au lieu de cela, vous exploitez **React Suspense**. Vous travaillez directement avec le tableau de Promesses. Chaque Promesse est passée dans le composant `ToolCard` individuellement. Et lorsque cette Promesse spécifique est résolue, le `ToolCard` affiche alors l'`IconCard` correspondant. Jusqu'à ce qu'elle soit résolue, vous affichez le `CardSkeleton` comme fallback à l'intérieur de `Suspense`. Super simple !

### Démonstration finale

Maintenant, vérifions rapidement le terminal, juste pour voir s'il y a des erreurs. Tout devrait être bon — pas d'erreurs ! Maintenant, si vous allez sur le navigateur, et depuis la page d'accueil, cliquez sur le bouton "Streaming Demo", vous devriez voir le Streaming en action !

Toutes les icônes devraient s'afficher une par une. Dès que quelque chose est prêt, il devrait apparaître. Il n'attend plus que tout se résolve en une seule fois. L'élément qui se résout en premier diffuse directement sur la page.

![Démonstration finale - Démonstration du Streaming Manuel](https://cdn.hashnode.com/res/hashnode/image/upload/v1754080577713/2d97114e-a1b1-49f7-8b65-2aa8bd7e66e8.gif align="center")

Voici une autre chose sympa : supposons que vous rechargez la page. Maintenant, l'une des cartes apparaît tôt, et vous lui donnez une réaction "love". Vous verrez "Aucun problème !" Même après que toutes les autres cartes se chargent, votre réaction "love" reste intacte. Pourquoi ? Parce que la carte avec laquelle vous avez interagi a déjà été hydratée. C'est clair ?

Donc ce vieux comportement confus — où un utilisateur interagirait trop tôt et l'action disparaîtrait — oui, ce n'est plus un problème.

![Aucune fausse interaction dans le Streaming SSR](https://cdn.hashnode.com/res/hashnode/image/upload/v1754080760808/7223cdae-1107-47d8-b477-0a33d4b98e1e.gif align="center")

Avec juste un petit changement, vous avez maintenant une expérience de Streaming complète. Si vous voulez diffuser au niveau de la `page`, utilisez simplement un fichier `loading.js`. De cette façon, toute la page montre un état de chargement couvrant toute la zone.

Mais si vous voulez diffuser des choses individuellement — comme différents composants ou sections — vous pouvez simplement les envelopper dans des frontières `Suspense` séparées et les gérer à votre manière. C'est le Streaming en termes de Next.js. Ou, plus simplement, dans le langage de React.

## Forcer le rendu dynamique pour un Streaming efficace

Maintenant, un dernier point que je veux mentionner : vous vous souvenez comment je n'ai pas arrêté de dire "Rendu Côté Serveur ! Rendu Côté Serveur !" ? Mais voici le côté amusant : si j'exécute `npm run build` maintenant et que je construis l'application, cette page `streaming-demo` deviendra en réalité une page **Statiquement Générée**.

Pourquoi ? Parce qu'il ne se passe rien de dynamique ici. Donc selon la logique de rendu de Next.js, cela devient une page **SSG (Static Site Generation)**. N'est-ce pas ? Si vous n'êtes pas familier avec **SSG** ou **SSR**, veuillez consulter [la vidéo](https://youtu.be/xTT_Sd_xqh0) que j'ai recommandée plus tôt. Elle explique tout clairement.

Et pour ceux d'entre vous qui sont familiers avec ces concepts, vous savez que si nous construisons cette page, elle devient une page statique. Cela signifie que le SSR ne s'applique pas vraiment ici — parce que la page est déjà pré-générée au moment de la construction. Lorsque l'utilisateur la demande, elle n'ira pas à travers `getData`, `getTools`, ou toute récupération basée sur les Promesses — parce que tout est déjà pré-rendu et cuit dans la construction.

Maintenant, si cette page était une vraie page rendue côté serveur, alors le Streaming aurait beaucoup plus de sens logique. Alors comment pouvez-vous forcer cela ? Facile ! En haut du fichier `app/streaming-demo/page.js`, ajoutez simplement cette ligne :

```javascript
export const dynamic = 'force-dynamic';
```

Cela dit à Next.js, "Hey, traite cette page comme dynamique, peu importe quoi."

C'est clair ? Maintenant, que vous construisiez l'application ou que vous l'exécutiez en mode `dev`, cette page sera toujours traitée comme une page rendue dynamiquement. Cela signifie qu'elle ne sera rendue sur le serveur que lorsque l'utilisateur fera une demande. Et c'est là que le Streaming devient vraiment significatif.

Donc maintenant, si vous exécutez `npm start` et ouvrez le même site à nouveau, vous verrez la même expérience de streaming, même en mode `production`.

J'espère avoir pu expliquer clairement ce qu'est le Streaming et comment il fonctionne. Et j'espère vraiment que vous comprenez maintenant comment et où cela peut être utile dans vos propres projets.

Si ce tutoriel a été même un peu utile pour obtenir votre première expérience de l'interface utilisateur de Streaming, j'adorerais en entendre parler — et ce serait une grande inspiration pour moi d'écrire plus de guides comme celui-ci à l'avenir.

## Résumé

Vous pouvez trouver tout le code source de ce tutoriel dans [ce dépôt GitHub](https://github.com/logicbaselabs/nextjs-streaming). Si cela vous a aidé d'une manière ou d'une autre, envisagez de lui donner une étoile pour montrer votre soutien !

De plus, si vous avez trouvé les informations ici précieuses, n'hésitez pas à les partager avec d'autres qui pourraient en bénéficier. J'apprécierais vraiment vos commentaires — mentionnez-moi sur X [@sumit\_analyzen](https://x.com/sumit_analyzen) ou sur Facebook [@sumit.analyzen](https://facebook.com/sumit.analyzen), [regardez mes tutoriels de codage](https://youtube.com/@logicBaseLabs), ou simplement [connectez-vous avec moi sur LinkedIn](https://www.linkedin.com/in/sumitanalyzen/).