---
title: Comment créer un blog portfolio simple avec Next.js
subtitle: ''
author: Chidiadi Anyanwu
co_authors: []
series: null
date: '2025-05-30T14:44:09.588Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-portfolio-blog-with-nextjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747235586248/7424bce0-24da-4f70-a5aa-31249d799094.png
tags:
- name: Next.js
  slug: nextjs
- name: portfolio
  slug: portfolio
- name: Blogging
  slug: blogging
- name: Web Development
  slug: web-development
seo_title: Comment créer un blog portfolio simple avec Next.js
seo_desc: 'I have written articles on different platforms including LinkedIn, The
  Network Bits (Substack), and freeCodeCamp. So I wanted to bring all of these articles
  together in a single place where someone could go and see all my work.

  A blog sounded like a ...'
---

J'ai écrit des articles sur différentes plateformes, notamment LinkedIn, The Network Bits (Substack) et freeCodeCamp. J'ai donc voulu rassembler tous ces articles en un seul endroit où quelqu'un pourrait aller et voir tout mon travail.

Un blog semblait être une bonne solution pour cela, alors je me suis lancé dans la création d'un. Dans cet article, je vais vous expliquer comment je l'ai fait avec Next.js.

L'idée de base ici était de construire un site web où je n'aurais pas besoin d'écrire de code à l'avenir. Je voulais simplement pouvoir ajouter l'URL d'un nouvel article à un fichier JSON, et le site web extrairait des informations comme le titre, la date, l'image de couverture, et la description, puis se mettrait à jour avec celles-ci. Pas de base de données.

Pour comprendre comment je m'y prendrais, j'ai vérifié les métadonnées du texte HTML de chacune des plateformes que j'ai considérées. J'ai utilisé mes articles, bien sûr, comme celui dans le dossier du projet. J'ai découvert que la plupart d'entre eux utilisaient les métadonnées Open Graph. Donc, c'était facile à scraper. Mais, j'ai aussi découvert que certaines informations n'étaient pas dans les balises meta – au lieu de cela, elles étaient dans le JSON-LD. À la fin de la journée, j'ai fini par utiliser les deux dans mes fonctions.

### Ce que nous allons couvrir :

1. [Comment fonctionne le site du blog](#heading-comment-fonctionne-le-site-du-blog)

2. [La structure d'un article sur le blog](#heading-a-quoi-ressemble-un-article)

3. [Comment fonctionne la fonctionnalité de recherche](#heading-comment-fonctionne-la-fonctionnalite-de-recherche)

4. [La structure du projet](#heading-structure-du-projet)

5. [Étapes pour construire le blog](#heading-etapes-pour-construire-le-blog)

6. [Conclusion](#heading-conclusion)

## Prérequis

Comprendre cet article nécessite quelques connaissances en programmation et en développement web. Vous devez avoir des connaissances de base en HTTP, HTML, CSS, JavaScript et React pour pouvoir suivre facilement.

Si vous n'avez pas ces compétences, vous pourrez peut-être encore comprendre la structure générale et les principes de fonctionnement.

## Comment fonctionne le site du blog

Le projet se compose de composants client et de composants serveur. C'est un site web, donc idéalement, ce n'est qu'un front-end. Mais il doit récupérer des données à partir d'URLs – et faire cela côté client ne fonctionnera pas en raison du blocage CORS, car les requêtes émaneront d'un navigateur. Donc, il doit s'exécuter sur le serveur.

![Page d'accueil appelant la fonction fetch articles.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748524048812/76baf11d-a80a-4d07-beba-065c74536541.png align="center")

La fonction `fetchArticles()` s'exécute sur le serveur – puis cela se produit :

![Organigramme approximatif montrant ce qui se passe dans la fonction fetchArticles](https://cdn.hashnode.com/res/hashnode/image/upload/v1748536836320/9813a669-ac07-480a-8270-6f2f36ceda22.png align="center")

La fonction `fetchArticles()` accède aux URLs, extrait et traite les objets HTML et JSON Linked Data de la réponse, et retourne un tableau d'objets Article à la page d'accueil.

![La fonction fetch articles est appelée et retourne un tableau d'objets Article](https://cdn.hashnode.com/res/hashnode/image/upload/v1748536952680/35fec49a-6c44-4978-9acb-755eb5ed810f.png align="center")

Le composant `HomePage` est un composant côté client qui contient un autre composant nommé `HomeClient`. Ce `HomeClient` est un composant côté client. Il doit l'être car il contient des hooks useState.

Mais le composant `HomePage` appelle la fonction `fetchArticles()` et définit la constante `articles` (qui est un tableau d'objets `Article`, tel que défini par l'interface dans le fichier `ArticleCard.tsx`). La constante `articles` est ensuite transmise au composant `HomeClient` en tant que prop.

![Le composant HomePage, et son composant enfant, HomeClient.](https://cdn.hashnode.com/res/hashnode/image/upload/v1746881308147/1fedcbb0-f9d4-47dd-afea-b7f231595a58.png align="center")

À l'intérieur du composant `HomeClient`, il y a deux composants – le composant `Hero` et le composant `MainBody`. Le composant Hero affiche le message de bienvenue et contient également la barre de recherche. Le composant MainBody est l'endroit où se trouvent les tags et la grille d'articles. La logique de filtrage des articles se trouve également dans le composant MainBody.

![Les composants Hero et MainBody à l'intérieur du composant HomeClient.](https://cdn.hashnode.com/res/hashnode/image/upload/v1746881333468/267d0158-df41-4a1d-8098-e3219fe7db4d.png align="center")

À l'intérieur du composant MainBody, il y a le composant `ArticleCard` qui prend le tableau filtré d'objets Article de MainBody en tant que props et rend une carte d'article pour chacun. Ces cartes sont rendues à l'intérieur de la grille dans le composant MainBody.

### À quoi ressemble un article ?

Les articles sont définis par une interface :

```typescript
export interface Article {
  id: number;
  title?: string;
  description?: string;
  publishedDate?: string;
  url: string;
  imgUrl?: string;
  siteName?: string;
  tags?: string[];
}
```

L'interface, comme montré ci-dessus, spécifie que l'objet aura huit propriétés, dont seules les propriétés `id` et `url` sont obligatoires. Ces propriétés obligatoires sont en fait ce qui est nécessaire dans le fichier JSON à partir duquel le serveur web lira.

Lorsque l'URL est visitée par le serveur, le titre, la description et les autres propriétés (sauf les tags) sont obtenus automatiquement et remplis. Ensuite, l'objet est créé.

![Rendus des cartes d'articles](https://cdn.hashnode.com/res/hashnode/image/upload/v1746881670519/a2cbdbbf-6cfd-40e7-91e5-5da711198dc7.png align="center")

Les cartes d'articles se composent de l'image de couverture de l'article, du nom de la plateforme où il a été publié, de la date de publication, du titre et d'une description. Tout cela est enveloppé dans une ancre reliant à l'URL. Les tags ne sont pas visibles sur les cartes, mais sont utilisés dans les opérations de filtrage.

![Tableau d'objets Article dans la console du navigateur.](https://cdn.hashnode.com/res/hashnode/image/upload/v1746881715907/7ab4ad87-7da6-44e2-8329-35bcb999b825.png align="center")

### Comment fonctionne la fonctionnalité de recherche ?

Il y a une raison pour laquelle le composant Hero et le composant MainBody sont dans le même composant parent. Ce n'était pas mon design initial, mais après avoir vu que la barre de recherche serait mieux dans le composant Hero, et que je devais définir l'état `searchTerm` dans le composant Hero et l'utiliser dans le composant MainBody, cela est devenu la meilleure option pour moi : mettre les deux dans le même parent, afin que je puisse transmettre le hook useState en tant que props dans les deux.

La fonctionnalité de recherche fonctionne principalement en filtrant le tableau `articles` en fonction des tags sélectionnés ou du terme de recherche saisi. Voici à quoi ressemble le code :

```typescript
 useEffect(() => {
    const anyTagActive = isActive.some((val) => val);

    const filtered = articles.filter((article) => {
      console.log('Search term: ' + searchTerm || 'searchTerm');
      const searchMatch =
        article.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        article.description?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        article.tags?.some((tag) => tag.toLowerCase().includes(searchTerm.toLowerCase())) ||
        article.siteName?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        article.publishedDate?.toLowerCase().includes(searchTerm.toLowerCase());


        console.log('This is the searchMarch: ' + searchMatch || 'FALSE searchMatch');
        console.log(article.title || 'article.title no wan show');

      const tagMatch = article.tags?.some((tag) => {
        const index = tags.indexOf(tag);
        return index !== -1 && isActive[index];
      }) || false;

      if (anyTagActive) {
        return tagMatch && searchMatch; // Ne retourne les articles que si le tag est actif et que la recherche correspond
      }

      return searchMatch; // Si aucun tag n'est actif, retourne tous ceux qui correspondent au terme de recherche
    });

    setFilteredArticles(filtered);
  }, [articles, searchTerm, isActive]);
```

Ici, nous utilisons un hook `useEffect()` pour surveiller les changements dans les constantes `articles`, `searchTerm` et `isActive`. `isActive` est un hook `useState()` qui contient un tableau de valeurs booléennes de la longueur du tableau des tags.

```typescript
const [isActive, setIsActive] = useState(tags.map(() => false));
```

Ici, la constante `filtered` est égale aux valeurs filtrées de `articles`.

```typescript
const filtered = articles.filter();
```

À l'intérieur de la [méthode filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) se trouve la fonction fléchée avec la logique de filtrage – `(article) => {//logique}`. Nous avons deux constantes : `tagMatch` et `searchMatch`. La constante `searchMatch` est vraie lorsque le titre, la description, les tags, le nom du site ou la date de publication incluent le terme de recherche. Sinon, elle est fausse. La constante `tagMatch` est vraie lorsqu'un tag de l'article est présent dans la liste des tags et a également une valeur `isActive` correspondante de vrai.

Si un tag est actif, alors les résultats pour `tagMatch` et `searchMatch` sont retournés, mais si aucun tag n'est actif, alors seul `searchMatch` est retourné comme vrai.

La liste d'articles filtrée est ensuite transmise au composant `ArticleCard`.

```typescript
<ArticleCard articles={filteredArticles} />
```

## Structure du projet

Voici à quoi ressemble la structure des fichiers du projet :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748605144895/e56eea92-8851-4717-ae82-0e15f70dc31f.png align="center")

À la racine, nous avons les fichiers de configuration et `node_modules` qui ne sont pas affichés ici. Le dossier `public` contient toutes les images et icônes. Ensuite, dans le dossier `src`, nous avons `app`, `component` et `utils`.

Le dossier `components` contient les fichiers pour les composants – la barre de navigation, le pied de page, le héros, le corps principal et la carte d'article. Le dossier `utils` contient toutes les fonctions qui s'exécutent en arrière-plan et n'ont pas besoin de rendre quoi que ce soit. La fonction `fetchArticles` s'y trouve, ainsi que d'autres fonctions pour extraire la date de publication, le titre, la description, l'URL de l'image, et d'autres éléments à partir des réponses HTTP obtenues à partir des URLs des articles. Le dossier `app` contient la favicon, la feuille de style CSS globale, les fichiers `page` et `layout`, `articles.json` qui est le fichier JSON où j'ajoute de nouvelles URLs d'articles pour le rendu, un fichier HTML de test (wsl.html), et les répertoires `about/` et `api/`.

À l'intérieur du dossier about, nous avons la page about, et à l'intérieur du dossier API, nous avons le dossier, `metadata-local-test` qui n'est plus pertinent pour le projet. Je l'ai utilisé initialement pour créer une API interne pour récupérer les données des URLs. Mais j'ai ensuite restructuré la base de code.

## Étapes pour construire le blog

### 1. Installer Next.js

Pour installer Next.js, naviguez vers le dossier où vous souhaitez que le projet réside et ouvrez cet emplacement dans votre terminal. Ensuite, tapez ce qui suit :

```bash
npx create-next-app@latest
```

Vous allez être confronté aux invites suivantes :

![Installation de Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1746881930473/228a02f7-6571-46f0-9503-d4606e19bd10.png align="center")

### 2. Naviguez vers votre nouveau dossier de projet et installez les dépendances

Dans le nouveau dossier de projet créé, exécutez le projet en mode développement pour prévisualiser votre nouveau projet Next. Vous verrez un message vous dirigeant vers localhost sur le port 3000. Maintenant, il est temps pour nous de commencer à créer ce que nous voulons.

![Succès ! Navigation vers le répertoire du projet.](https://cdn.hashnode.com/res/hashnode/image/upload/v1746882046144/df46e975-14f2-4dc9-81d7-5bbb9a344f7b.png align="center")

Maintenant, une autre chose que vous devrez faire. Dans le projet, j'ai utilisé lucide-react pour obtenir l'une des icônes, et cheerio pour extraire des données du HTML. Donc, vous devrez installer ces dépendances.

Pour installer lucide-react, utilisez cette commande dans le dossier du projet :

```bash
npm install lucide-react
```

Ensuite, installez cheerio :

```bash
npm install cheerio
```

### 3. Changer le titre et la description dans les métadonnées de la page

Le titre est ce qui s'affiche en haut de votre onglet de navigateur lorsque vous ouvrez le site web. Pour l'instant, il devrait afficher 'Create Next App.' Nous ne voulons pas cela.

Puisque ce n'est pas juste du HTML, il n'y a pas de `index.html` pour changer le titre dans l'élément header. Au lieu de cela, Next.js nous fournit un objet `Metadata` que nous pouvons utiliser pour changer des choses comme cela. Et il sera dans le fichier `layout.tsx` dans le dossier `app` ou `src`. Rendez-vous là-bas et changez-le en ce que vous voulez que le titre soit. J'utilise « Chidiadi Portfolio Blog ».

![Changement des métadonnées](https://cdn.hashnode.com/res/hashnode/image/upload/v1746882205569/b652a7de-00b7-4f0d-943c-4f80a62a7f91.png align="left")

### 4. Créer les composants nécessaires

Naviguez vers le panneau latéral, et sous le dossier `src`, créez un dossier components. C'est là que les composants vivront. Ici, créez la carte d'article, le pied de page, le corps principal et la barre de navigation.

![Dossier des composants](https://cdn.hashnode.com/res/hashnode/image/upload/v1746882335350/69d1f7ed-ea67-47e7-8b0a-e25429190a3e.png align="left")

Pour la **Navbar**, voici le code :

```typescript
export default function Navbar(){
    return(
        <>
        <div className="text-3xl md:text-base flex w-[100vw] md:w-[98.2vw] lg:w-[98.8vw] h-[60px] bg-black text-white px-0 md:px-7 md:py-2 items-center justify-center md:justify-between">
            <h1 className="font-bold">CHIDIADI   ANYANWU</h1>
            <div className="hidden md:block flex space-x-4">
                <a href="/" className="hover:text-gray-400">Blog</a>
                <a href="/about" className="hover:text-gray-400">À propos</a>    
            </div>
        </div>
        </>
    );
}
```

Voici à quoi ressemble le composant **Hero** :

```typescript
"use client";

import { Search } from 'lucide-react';
import { useState } from 'react';

interface HeroProps {
    searchTerm: string;
    setSearchTerm: React.Dispatch<React.SetStateAction<string>>;
  }
export default function Hero({ searchTerm, setSearchTerm }: HeroProps) {
    const [buttonColor, setButtonColor] = useState('');

    return (
        <div className="bg-[url('/img-one-1.jpg')] bg-cover bg-center bg-no-repeat flex flex-col items-center justify-center h-[400px] relative">
           <div className=" absolute inset-0 bg-black opacity-60"></div> 
            <h1 className="text-4xl text-white font-bold text-center z-10">Mon Portfolio Blog</h1>
            <p className="mt-4 mx-4 text-xlarge text-white md:text-xl text-justify md:text-center z-10" style={{ fontFamily: "Cormorant Garamond" }}>
                Je m'appelle Chidiadi Anyanwu. Je suis un rédacteur technique avec une solide expérience en réseau. 
                J'écris sur le Réseautage, le Cloud, le DevOps, et parfois même sur le développement web comme celui-ci. J'ai construit ce
                site web avec Next.js, et il y a aussi un <a href="/" className="text-blue-500 hover:text-blue-700 hover:underline">article à ce sujet.</a>
                  Ce site web contient mes articles techniques en un seul endroit. C'est un dépôt de mes travaux écrits.
            </p>
            <div id="searchbar" className="h-9xl mt-4 flex align-items-center justify-center w-full" >

                <form onSubmit={(e) => {e.preventDefault();  setSearchTerm(searchTerm);}} className="group mt-4 relative w-[70%] md:w-[50%]">
                    <input  value={searchTerm} onChange={(e) => setSearchTerm(e.target.value) } onFocus={()=>{setButtonColor('bg-blue-500'); console.log('input focused')}} onBlur={()=>{setButtonColor('');}}type="search" placeholder="Rechercher les articles de Chidiadi" className="h-[50px] w-full px-[48px] border-3 border-blue-300 rounded-[25px] focus:outline-none focus:border-blue-500 text-black bg-white"/>
                    <button className={`h-[42px] w-[42px] absolute right-0 mr-1.5 mt-1 rounded-[50%] bg-blue-300 ${buttonColor}`}>
                        <Search  className='m-auto text-white'/>
                    </button>
                </form>

            </div>
        </div>
    );
}
```

Dans ce fichier, nous avons créé l'interface HeroProps pour accepter les props de recherche. Ensuite, nous avons déconstruit à la fois `searchTerm` et `setSearchTerm` de celle-ci en tant que props pour le composant Hero. Nous allons en faire un composant client `'use client'` à cause du hook `useState()` buttonColor qui change lorsque la barre de recherche est cliquée et définit la couleur de fond du bouton de recherche.

Le composant **MainBody** ressemble à ceci :

```typescript
"use client";

import { useEffect, useState } from 'react';
import ArticleCard, { Article } from './ArticleCard';

interface MainBodyProps {
  searchTerm: string;
  articles: Article[];
}

export default function MainBody({ searchTerm, articles }: MainBodyProps) {
  // Obtenez les articles du fichier JSON et créez un tableau d'objets d'articles

  const [filteredArticles, setFilteredArticles] = useState<Article[]>([]);

  const tags = ["Networking", "Cloud", "DevOps", "Web Dev", "Cybersecurity"];
  const [isActive, setIsActive] = useState(tags.map(() => false));


  // Filtrer les articles en fonction du terme de recherche et des tags actifs
  useEffect(() => {
    const anyTagActive = isActive.some((val) => val);

    const filtered = articles.filter((article) => {
      console.log('Search term: ' + searchTerm || 'searchTerm');
      const searchMatch =
        article.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        article.description?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        article.tags?.some((tag) => tag.toLowerCase().includes(searchTerm.toLowerCase())) ||
        article.siteName?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        article.publishedDate?.toLowerCase().includes(searchTerm.toLowerCase());


        console.log('This is the searchMarch: ' + searchMatch || 'FALSE searchMatch');
        console.log(article.title || 'article.title no wan show');

      const tagMatch = article.tags?.some((tag) => {
        const index = tags.indexOf(tag);
        return index !== -1 && isActive[index];
      }) || false;

      if (anyTagActive) {
        return tagMatch && searchMatch; // Ne retourne les articles que si le tag est actif et que la recherche correspond
      }

      return searchMatch; // Si aucun tag n'est actif, retourne tous ceux qui correspondent au terme de recherche
    });

    setFilteredArticles(filtered);
  }, [articles, searchTerm, isActive]); 

  console.log(filteredArticles);

  return (
    <div className='scroll-smooth'>
      <div id="tags" className="flex w-full h-[200px] md:h-[60px] justify-center gap-5 py-4 flex-wrap max-w-[100vw] scroll-smooth">
        {tags.map((tag, index) => (
          <p
            key={index}
            onClick={() => {
              const newIsActive = [...isActive];
              newIsActive[index] = !newIsActive[index];
              setIsActive(newIsActive);
            }}
            className={`h-[48px] w-[140px] border-3 rounded-[40px] px-2 py-2 text-center font-bold ${
              isActive[index]
                ? 'bg-black border-black text-white hover:bg-gray-700 hover:border-gray-700'
                : 'border-blue-500 hover:bg-blue-500 hover:text-white'
            }`}>
            {tag}
          </p>
        ))}
      </div>

      <div id="articlegrid" className="w-[100vw] md:w-[98vw] grid gap-2 grid-cols-1 md:grid-cols-2 xl:grid-cols-3 mt-5 px-3 py-3">
        <ArticleCard articles={filteredArticles} />
      </div>
    </div>
  );
}
```

Ici, nous avons également des props du composant parent, mais nous n'avons besoin que des articles récupérés et du terme de recherche. Nous n'avons pas besoin de définir le terme de recherche à partir de ce composant.

Pour rendre les tags, j'ai d'abord créé le tableau des tags et un tableau de valeurs booléennes pour enregistrer les états des tags (s'ils sont actifs ou inactifs).

```typescript
const tags = ["Networking", "Cloud", "DevOps", "Web Dev", "Cybersecurity"];
const [isActive, setIsActive] = useState(tags.map(() => false));
```

Ensuite, à l'intérieur de l'instruction return, j'ai mappé le tableau des tags pour les rendre un par un. Le gestionnaire d'événements onClick fonctionne également ici pour s'assurer que l'état `isActive` pour ce tag particulier est basculé lorsqu'il est cliqué.

Comment cela fonctionne-t-il ? Il crée un nouveau tableau appelé `newIsActive` qui est une copie du tableau `isActive`. Il obtient ensuite le tag particulier par numéro d'index et l'inverse. Ensuite, il définit le tableau `isActive` sur ce nouveau tableau.

```typescript
{tags.map((tag, index) => (
          <p
            key={index}
            onClick={() => {
              const newIsActive = [...isActive];
              newIsActive[index] = !newIsActive[index];
              setIsActive(newIsActive);
            }} . . .
```

Voici le code pour le **ArticleCard** :

```typescript
import React, { useState } from 'react';
import Image  from 'next/image';

export interface Article {
  id: number;
  title?: string;
  description?: string;
  publishedDate?: string;
  url: string;
  imgUrl?: string;
  siteName?: string;
  tags?: string[];
}

interface ArticleProps {
  articles: Article[];
}

const ArticleCard = ({ articles }: ArticleProps) => {

  return (
    <>
    {articles ?

      (articles.map((item, id) => (
        //balise d'ancrage pour le lien
        <a key={id}  href={item.url} className='max-w-[350px] mx-auto mb-5'>
            <div className="sm:w-[350px] hover:brightness-70" data-title={item.title} data-description={item.description} data-published-date={item.publishedDate} data-tag="Networking" data-site-name={item.siteName}>
            <Image
              src={item.imgUrl || '/img-2.jpg'} 
              alt={item.title || 'Article Image'}
              width={350}
              height={400}
              className="object-cover rounded-[10px]"
            />
            <div className="flex h-[43px] text-[14px] text-gray-500 gap-2">
                <p id="Platform" className="py-2 h-[42px] md:text-sm mt-auto mb-auto">{item.siteName}</p>
                <div className="h-1 w-1 bg-black rounded-full mt-auto mb-auto bg-gray-500"></div>
                <p id="publishedDate" className="py-2 h-[42px] mt-auto mb-auto">{item.publishedDate}</p>
            </div>
            <h1 id="titleOfArticle" className="font-bold text-base md:text-3xl">{item.title}</h1>
            <br/>
            <p className='w-full md:w-[350px]'>{item.description}</p>
            </div>
        </a>
      )))
      :

      ( Array(6).fill(0).map((item, id) => (
        <div key={id} className="w-full md:w-[350px] h-[350px] bg-gray-500 mx-auto mb-5 hover:brightness-80 rounded-[10px] animate-pulse"></div>
      )))
    }
    </>
  );
};

export default ArticleCard;
```

Ici, nous avons défini et exporté l'interface `Article` afin de pouvoir créer des objets `Article` dans le `MainBody`. Ensuite, nous avons créé une interface pour transmettre les props d'un tableau d'objets `Article`.

Ensuite, il y a cette partie pour s'assurer qu'elle rend quelque chose même si pour une raison quelconque aucun objet Article n'a été transmis :

```typescript
{
    article?
    ( {/*Si l'article existe, rendre ceci*/} )
    :
    ( {/*Sinon, rendre ceci */} )
}
```

Notre solution de secours ici est un tableau vide de six objets avec le Tailwind `animate-pulse` :

```typescript
 ( Array(6).fill(0).map((item, id) => (
        <div key={id} className="w-full md:w-[350px] h-[350px] bg-gray-500 mx-auto mb-5 hover:brightness-80 rounded-[10px] animate-pulse"></div>
      )))
```

J'aurais pu rendre cette partie beaucoup mieux, mais je me sentais un peu paresseux. J'ai également utilisé `Image` de Next, au lieu de l'`img` régulier. Cela nécessite que vous modifiiez le fichier `next.config.ts`. J'ai dû ajouter tous les chemins à partir desquels les images pourraient être chargées :

![next.config.ts](https://cdn.hashnode.com/res/hashnode/image/upload/v1746882422600/e3ad4762-1199-4276-a524-d27519a37c52.png align="center")

Tout comme dans la capture d'écran ci-dessus, la syntaxe est :

```typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
        {
            protocol:"https",
            hostname:"licdn.com",
            pathname:"/**"
        },
        {
            protocol:"",
            hostname:"",
            pathname:""
        }
        ],
    },
};
export default nextConfig;
```

Il prend un tableau `remotePatterns` qui se compose d'objets de motifs distants, qui ont une propriété de protocole, d'hôte et de chemin. Assurez-vous que les propriétés de protocole et d'hôte ne sont pas vides comme dans le deuxième objet de l'exemple de code ci-dessus. Cela causerait des erreurs. Soit les objets sont correctement remplis, soit ils sont supprimés.

Le **Footer** ressemble à ceci :

```typescript
export default function Footer() {

    return (
        <footer className="bg-gray-100 text-center py-4 mt-10">
            <div className="flex align-items-center justify-center text-sm text-blue-400 font-bold">
                <a href="/" className="hover:text-blue-600">Accueil</a>
                <p> &nbsp; &nbsp; | &nbsp; &nbsp; </p>
                <a href="/about" className="hover:text-blue-600">À propos</a>
            </div>
            <p className="text-sm text-gray-600"> a9 {new Date().getFullYear()} Chidiadi Anyanwu. Tous droits réservés.</p>
            <p className="text-sm text-gray-600">Conçu avec Next.js et Tailwind CSS</p>
        </footer>
    );

}
```

Ce `new Date().getFullYear()` m'aide à obtenir l'année en cours à tout moment.

### 5. Placer les composants correctement

Les composants de la barre de navigation et du pied de page sont des éléments qui ne changeront pas quelle que soit la page que vous visitez. Ils doivent donc être placés dans un emplacement plus permanent et intouchable. Nous pouvons mettre les deux dans le fichier `layout.tsx` racine comme ceci :

![fichier layout.tsx](https://cdn.hashnode.com/res/hashnode/image/upload/v1746882493175/3d7381ca-48c6-43c1-becc-8692c6b090c4.png align="center")

```typescript
 <body className={`${geistSans.variable} ${geistMono.variable} antialiased scroll-smooth`}>
      <Navbar />
      {children}
      <Footer />
  </body>
```

`{children}` est l'endroit où le contenu de `page.tsx` entrera. Nous avons donc encadré tout le reste du contenu dans la barre de navigation et le pied de page. En dehors de l'ajout de balises `<link />` pour les polices (car c'est ici que se trouve le HTML racine), nous n'avons vraiment plus rien à faire avec ce fichier.

Maintenant, dans le même dossier `app/` où se trouve ce fichier de mise en page, créez le fichier `<HomeClient />`. Voici à quoi il ressemble :

```typescript
'use client';

import { useState } from 'react';
import Hero from '../components/hero';
import MainBody from '../components/mainbody';
import { Article } from '../components/ArticleCard';

interface Props {
  initialArticles: Article[];
}

export default function HomeClient({ initialArticles }: Props) {
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [articles, setArticles] = useState<Article[]>(initialArticles);

  return (
    <div>
      <Hero searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
      <MainBody searchTerm={searchTerm} articles={articles} />
    </div>
  );
}
```

Ensuite, placez le composant `HomeClient` à l'intérieur du fichier `page.tsx` :

```typescript
import { fetchArticles } from '../utils/fetchArticles';
import HomeClient from './HomeClient';

export const revalidate = 3600;

export default async function HomePage() {
  const articles = await fetchArticles(); 

  return <HomeClient initialArticles={articles} />;
}
```

Le serveur est configuré pour récupérer les articles au moment de la construction et pour les récupérer à nouveau (révalider) toutes les heures (3600s). Ainsi, il ne récupère pas les articles des URLs à la demande de l'utilisateur de la page.

Initialement, cela fonctionnait en récupérant chaque fois que le composant était monté, mais j'ai remarqué que cela faisait que la page se chargeait très lentement. Les articles n'apparaissaient pas à temps, car il y avait beaucoup de récupérations à faire.

Dans ce même répertoire `app/`, créez un dossier `about/`, et créez le `page.tsx` pour cette route :

```typescript
import Image from "next/image";
export default function About() {
    return (
        <>
            <div className="flex items-center justify-center">
                <div className="margin-auto w-[90vw] md:w-[60vw] lg:w-[50vw] h-[450px] hover:bg-gray-100 border-1 md:border-2 border-gray-200 shadow-sm flex flex-wrap  items-center justify-center gap-2 mt-10 mb-10 rounded-lg">
                    <Image
                        src="/MyPhotoChidiadi.jpg" 
                        alt="Avatar"
                        className="rounded-[50%] h-30 w-30"
                        width={120} 
                        height={120} 
                    />
                    <div className="w-[90%] mx-auto">
                        <h1 className="text-xl text-center my-1 font-bold">À propos de moi</h1>
                        <p className="text-justify my-3">
                            Je m'appelle Chidiadi Anyanwu. J'aime décomposer des concepts complexes.
                            J'écris sur le Réseautage, le Cloud, le DevOps, et parfois même sur le développement web. 
                            Vous pouvez me contacter en suivant l'un des liens ci-dessous.
                        </p>
                        <hr className="border-gray-300 my-3" />
                        <div className="flex gap-7 w-full my-3 justify-center"> 
                            <a href="https://github.com/chidiadi01">
                                <Image src='/github-icon.svg' alt="logo github" width={24} height={24} />
                            </a>
                            <a href="https://linkedin.com/in/chidiadi-anyanwu">
                                <Image src='linkedin-icon.svg' alt="logo linkedin" width={24} height={24}/>
                            </a>
                            <a href="https://x.com/chidiadi01">
                                <Image src='x-2.svg' alt="logo x" width={24} height={24}/> 
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}
```

### 6. Créer le dossier utils et toutes les fonctions

L'étape suivante consiste à créer tous ces fichiers.

![dossier utils](https://cdn.hashnode.com/res/hashnode/image/upload/v1746947058303/01b6fd3d-3666-46fe-8928-1ad5b1532625.png align="center")

Sous le même répertoire `app/`, créez le dossier `utils/`. `app/utils/`. Ensuite, commencez par la fonction `fetchArticles()`. La fonction `fetchArticles()` est celle qui accède à la route de l'API dans le projet pour obtenir le tableau d'objets Article à partir d'un tableau d'URLs. La fonction `fetchArticles()` retourne un tableau de ces objets qui sont ensuite stockés dans la variable `articles`. Elle ressemble à ceci :

```typescript
import { getPublishedDate } from './getPublishedDate';
import { getTitle } from './getTitle';
import { getImageURL } from './getImageURL';
import { getDescription } from './getDescription';
import { getPlatform } from './getPlatform';
import articleFile from '../app/articles.json';
import { Article } from '../components/ArticleCard';
import * as cheerio from 'cheerio';

export async function fetchArticles(): Promise<Article[]> {
  console.log('Récupération des articles...');
  const results = await Promise.all(
    articleFile.articles.map(async (item) => {
      //Valider l'URL d'abord
       if (!item.url || typeof item.url !== 'string' || item.url.trim() === '') {
        console.warn(`URL invalide : ${item.url}`);
        return null; // Ignorer cet élément
      } 
      console.log('L\'URL : ' + item.url);
      let data;
      try {

        // Récupérer les métadonnées et le HTML de l'URL
        const response = await fetch(item.url, {
          headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.google.com/', 
          },
        });

        console.log('Récupéré : '+ item.url);

        if (!response.ok) {
          console.error(`Erreur HTTP ! Statut : ${response.status} pour l'URL : ${item.url}`);
          throw new Error(`Erreur HTTP ! Statut : ${response.status}`);
        }

        const html = await response.text();
        const $ = cheerio.load(html);
        const jsonScript = $('script[type="application/ld+json"]').html();

        console.log('Réponse HTML obtenue');

        if (!jsonScript) {
          throw new Error('Aucun script JSON-LD trouvé sur la page');
        }

        const metadata = JSON.parse(jsonScript);
        console.log('Métadonnées obtenues');


        // Combiner les métadonnées et le HTML en un seul objet
        data = { metadata, html };
      } catch (error) {
        console.error(`Échec de la récupération des métadonnées pour l'URL : ${item.url}`, error);
        return null;
        console.log('L\'objet vide par défaut a été retourné ici');
      }

      // Utiliser les données combinées (métadonnées et HTML) pour construire l'objet article
      if(getTitle(data) && getDescription(data) &&
         getPublishedDate(data) && getImageURL(data) &&
         getPlatform(data) || (item.title && item.description &&
         item.image)) {
        return {
        ...item,
        id: item.id ?? 0,
        tags: item.tags ?? [],
        title: getTitle(data) || item.title || 'No title',
        description: item.description || getDescription(data) || 'No description',
        publishedDate: getPublishedDate(data) ?? 'No date',
        imgUrl: getImageURL(data) || item.image || '/img-2.jpg',
        siteName: getPlatform(data) || data.metadata?.publisher?.name || 'Unknown site',
        url: item.url || '',
      } as Article;
      console.log('Élément correct retourné');
      } else { return null; }
    })
  );

  // Filtrer les valeurs nulles et trier les articles par date de publication en ordre décroissant
  const filteredResults = results.filter((article): article is Article => article !== null);
  const sortedResults = filteredResults.sort((a, b) => {
    const dateA = new Date(a.publishedDate || '').getTime();
    const dateB = new Date(b.publishedDate || '').getTime();
    return dateB - dateA;
  });
  console.log(sortedResults);
  return sortedResults;
}
```

Elle parcourt les articles dans le fichier articleFile, qui est le fichier JSON avec un tableau d'objets contenant les URLs des articles. Pour chacun d'eux, elle envoie une requête à l'URL, et à partir des données obtenues, retourne un objet Article. Ensuite, le tableau d'objets créé, `results`, est d'abord filtré pour supprimer les objets nuls, et [trié](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) par ordre décroissant selon leurs propriétés de date. Ainsi, le dernier article apparaît en premier.

Il est ensuite assigné dans le composant `HomeClient` :

```typescript
 const articles = await fetchArticles();
```

Dans le code `fetchArticles()` ci-dessus, vous pouvez voir que d'autres fonctions ont été utilisées pour extraire les propriétés des URLs et les assigner. De plus, lors du déploiement, j'ai découvert que Substack ne pouvait pas être accessible par le serveur, donc je vais ajouter du code pour permettre la création d'objets Article à partir d'un flux RSS. Cela sera dans le [dépôt du projet](https://github.com/chidiadi01/simple-writer-portfolio/tree/main/01-simple-blog).

Maintenant, parlons des autres fonctions.

#### **La fonction** `getTitle()` **:**

```typescript
import * as cheerio from 'cheerio';

export function getTitle(data:any): string {
    if(!data) return 'Titre en cours de chargement . . .';

    if (data?.html) {
        const $ = cheerio.load(data?.html);
        const ogTitle = $('meta[property="og:title"]').attr('content') || $('title').text();
        return ogTitle;
    }

        return 'Le Titre de l\'Article';
    }
```

C'est une fonction très simple. Elle prend le paramètre `data`, et s'il n'y a pas de données, elle retourne `Titre en cours de chargement . . .`. Mais s'il y a des données, elle vérifie s'il y a du HTML dans les données. Si c'est le cas, elle utilise cheerio pour charger le texte HTML et extraire le titre des métadonnées Open Graph `title` ou de la balise `<title>` dans l'en-tête HTML. Sinon, elle retourne `Le Titre de l'Article`.

Ici, nous utilisons une syntaxe de type jQuery `$` pour sélectionner les éléments HTML, comme dans `$('title')`. Les données prises en tant que paramètre sont la réponse obtenue d'une requête HTTP à l'URL de l'article.

#### **La fonction** `getDescription()` **:**

```typescript
import * as cheerio from 'cheerio';

export function getDescription(data: any): string {
  if (!data) return 'Description en cours de chargement . . .';

  if (data?.metadata || data?.html) {
    const $ = cheerio.load(data?.html || '');
    const description = data?.metadata?.description ?? $('meta[property="og:description"]').attr('content') ?? 'Aucune description trouvée';
    return description;
  }

  return 'Aucune description trouvée';
}
```

#### **La fonction** `getURL()` **:**

```typescript
import * as cheerio from 'cheerio';

export function getURL(data: any): string{
    if(!data) return 'url';

    if(data?.metadata || data?.html){
        const $ = cheerio.load(data?.html);
        const url = data?.metadata.url || $('meta[property="og:url"]').attr('content');
        return url;
    }
    return 'url';
}
```

Cette fonction n'est pas vraiment utilisée pour obtenir l'URL de l'article pour l'utiliser dans l'objet. Elle est plutôt utilisée pour obtenir l'URL pour une autre fonction, `getPlatform()`. Elle fonctionne de la même manière que celles que nous avons discutées précédemment.

#### **La fonction** `getPlatform()` **:**

```typescript
import { getURL } from './getURL';

export function getPlatform(data: any): string {
    if (!data) return 'Platform1';

    const url = getURL(data);

    if (data?.html) {
      const regex = /^(?:https?:\/\/)?(?:www\.)?([^\/\n]+)\.(?:[a-zA-Z]{2,})/;
      const platform = url.match(regex);
      return platform?.[1].toUpperCase() || 'Platform2'; 
    }

    return 'Platform3';
  }
```

Cette fonction est destinée à extraire le nom de la plateforme où l'article est publié. J'ai joué avec diverses idées sur la manière dont cela devrait fonctionner. L'une d'entre elles était d'utiliser la propriété `siteName` dans les balises meta OG, mais j'ai réalisé lors de mon inspection que toutes les plateformes ne l'avaient pas remplie de manière utile. Ainsi, les résultats obtenus par cette méthode seraient trop imprévisibles.

J'ai donc décidé d'utiliser [regex (Expressions Régulières)](https://www.freecodecamp.org/news/practical-regex-guide-with-real-life-examples/) pour extraire le nom du site à partir de l'URL. Comme vous pouvez le voir dans le code, je n'ai pas obtenu un résultat parfait, mais il est utilisable.

Tout d'abord, il obtient l'URL de l'article avec la fonction `getURL()`. Ensuite, il utilise regex :

```bash
/^(?:https?:\/\/)?(?:www\.)?([^\/\n]+)\.(?:[a-zA-Z]{2,})/
```

Ici, `/` et `/` au début et à la fin sont pour commencer et terminer la chaîne regex. Le caret `^` marque le début d'une ligne.

Ensuite, nous avons quatre groupes `()()()()`. Le premier est un groupe non capturé `(?: )`. Cela signifie que tout texte correspondant à cela doit être regroupé en une chaîne, mais ne doit pas être capturé pour être assigné à la variable. Il capture tout texte avec un 'http' dedans, avec ou sans le s `s?`, et avec deux barres obliques après. Les barres obliques ont été échappées avec des barres obliques inversées pour qu'elles soient reconnues comme des caractères littéraux. Ensuite, le groupe entier est rendu facultatif en ajoutant le point d'interrogation après celui-ci `(...)?`. Donc, que ce groupe soit apparié ou non, le code fonctionne.

Le deuxième groupe est également un groupe non capturé, également désigné par `?:` étant la première chose à l'intérieur de la parenthèse. Celui-ci correspond à tout 'www.' dans la chaîne. Il est également facultatif. Une URL n'a pas nécessairement besoin d'être écrite avec.

Le troisième groupe est un groupe capturé car il n'a pas `?:` à l'intérieur des crochets. Il a plutôt une classe de caractères à l'intérieur `[]`. Mais c'est une classe négative `[^ ]`. Elle s'assure que la classe ne contient pas de caractère de nouvelle ligne `n` (le caractère de nouvelle ligne n est pas une chaîne de lettre n – c'est pourquoi il est échappé) ou une barre oblique `/`, car une URL est censée être sur une seule ligne, et non sur plusieurs lignes. Le `+` signifie un ou plusieurs caractères, `([^\/\n]+)`. Tout ce qui se trouve dans ce groupe sera capturé dans la variable.

Ensuite, le suivant correspond à un point (il est échappé avec une barre oblique inversée `\.`). Après cela se trouve le dernier groupe qui est également non capturé et correspond à tout caractère alphanumérique, majuscule ou minuscule `[a-zA-Z]`, qui se produit plus de deux fois `{2, }`.

Ainsi, si nous avons '[https://www.linkedin,com'](https://www.linkedin,com') nous aurions un tableau de groupes capturés \['[https://www.linkedin.com','https://','www.','linkedin','com'\]](https://www.linkedin.com','https://','www.','linkedin','com'%5D). Groupe 1 = 'https://', groupe 2 = 'www.', groupe 3 ='linkedin', groupe 4 = 'com'. Mais comme seul le groupe 3 est un groupe capturé, les autres seront supprimés, et nous avons un tableau avec seulement deux éléments, la chaîne complète, et le groupe capturé : \['[https://www.linkedin.com','linkedin'\]](https://www.linkedin.com','linkedin'%5D)*.*

Ainsi, ici, nous retournons le deuxième élément du tableau. Le premier élément est toujours la chaîne complète que nous avons appariée.

```typescript
return platform?.[1].toUpperCase()
```

Cela ne tient pas compte des sous-domaines, cependant. Cela est délicat car parfois vous voulez utiliser le nom du sous-domaine (comme dans mon Substack), et parfois vous voulez utiliser le nom du domaine. Donc, je l'ai laissé comme ça.

![Image d'un article avec la plateforme montrant THENETWORKBITS.SUBSTACK](https://cdn.hashnode.com/res/hashnode/image/upload/v1746947172558/7f0f47c0-a1d5-4db7-a8e5-d45d1116aaac.png align="center")

#### **La fonction** `getImageURL()` **:**

```typescript
import * as cheerio from 'cheerio';

export function getImageURL(data: any): string {
    if (!data) return '/img-2.jpg'; 

    if (data?.metadata || data?.html) {
        const $ = cheerio.load(data?.html);
        const ogImage = $('meta[property="og:image"]').attr('content') || data?.metadata.image;
        return ogImage || '/img-2.jpg'; 
    }

    return '/img-2.jpg'; 
}
```

Cette fonction fonctionne comme les autres et obtient l'URL de l'image de couverture à partir de la balise meta Open Graph image `$('meta[property="og:image"]').attr('content')` ou `||` de la propriété image dans les données JSON-LD `data?.metadata.image`.

#### **La fonction** `getPublishedDate()` **:**

```typescript
import * as cheerio from 'cheerio';

export function getPublishedDate(data: any): string {

  if (!data) return 'Date';

  const publishedDate = data?.metadata?.datePublished;

  if (publishedDate) {
    const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(publishedDate).toLocaleDateString('en-US', options);
  }

  if (data?.html) {
    const $ = cheerio.load(data?.html);
    const ogPublishedTime = $('meta[property="article:published_time"]').attr('content') ||
                            $('meta[property="og:published_time"]').attr('content') || 
                            $('meta[name="pubdate"]').attr('content');

    if (ogPublishedTime) {
      const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric' };
      return new Date(ogPublishedTime).toLocaleDateString('en-US', options);
    }
  }
  return 'Date';
}
```

Cette fonction est particulièrement utile en raison de la nécessité de convertir la date du format ISO 8601 (2025-04-07T10:47:19+00:00) au format plus lisible que je souhaite (7 avril 2025). Ici, j'ai utilisé la fonction `.toLocaleDateString()` JavaScript pour la faire fonctionner (voir le ([MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString)).

### 7. Créer votre fichier JSON

Maintenant, rappelez-vous que nous construisons cela pour pouvoir extraire des URLs d'un fichier JSON afin de rassembler et de rendre la page web. Ce fichier JSON est le point de départ de tout. Je pense qu'à ce stade, vous obtenez une erreur à ce sujet. Nous devons donc créer le fichier JSON.

Dans le répertoire `app/`, créez un nouveau fichier et nommez-le `articles.json`.

![Le répertoire app/](https://cdn.hashnode.com/res/hashnode/image/upload/v1746947297567/ed6b282b-971e-428b-a7b6-9d6bf5e44520.png align="center")

Ensuite, remplissez-le comme dans le fichier ci-dessous – un tableau d'objets avec id, URL, tags, etc. Même si nous n'essayons pas d'obtenir le titre, la description et tout directement à partir de ce fichier, j'ai inclus cette fonctionnalité. Si vous retournez à notre fonction `fetchArticles()`, vous verrez que pour la plupart des propriétés, ce que vous écrivez ici remplacera ce qui a été obtenu à partir des URLs.

C'était en partie une solution de secours car je pensais que LinkedIn bloquerait toutes les requêtes, et comme vous pouvez le voir à partir de mon blog, certaines balises de description n'étaient pas bien organisées. Nous pouvons donc les remplacer plus tard par une description plus propre simplement en modifiant ce fichier.

```json
{
    "articles": [
        {
            "id": 1,
            "url": "https://thenetworkbits.substack.com/p/an-overview-of-json",
            "tags": ["Web Dev", "DevOps", "Cloud"],
            "title": "",
            "description": "",
            "image": ""
        },
        {
            "id": 2,
            "url": "https://websecuritylab.org/how-safe-is-public-wi-fi-a-network-engineer-explains/",
            "tags": ["Networking", "Cybersecurity"],
            "title": "",
            "description": "",
            "image": ""
        },
        {
            "id": 3,
            "url": "https://www.freecodecamp.org/news/automate-cicd-with-github-actions-streamline-workflow/",
            "tags": ["DevOps"],
            "title": "",
            "description": "",
            "image": ""
        }
    ]
}
```

Ici, nous avons un objet "articles" avec un tableau d'objets, chacun ayant des propriétés "id", "url", "tags", "title", "description" et "image". Vous n'avez pas nécessairement besoin des valeurs de toutes ces propriétés sauf l'ID et l'URL, mais les clés doivent être présentes pour éviter les erreurs.

### 8. Ajouter les dernières touches

Maintenant, vous pouvez ajouter votre propre favicon dans le répertoire de l'application. Cela peut être un fichier de 24px par 24px, ou de 48px par 48px. Il n'est pas nécessaire qu'il soit dans le répertoire de l'application ou qu'il soit un fichier d'icône ou nommé 'favicon' – mais je l'ai fait de cette manière. Vous pouvez simplement ajouter ceci dans l'en-tête HTML de votre fichier layout.tsx qui est votre version Next.js de `index.html`. La favicon est l'icône qui s'affiche sur l'onglet de votre navigateur lorsque vous ouvrez la page.

```html
<link rel="icon" href="/favicon.ico" sizes="any" />
```

Vous pouvez également lire la documentation de Next.js à ce sujet ici : [Fichiers de métadonnées : favicon, icône et apple-icon | Next.js](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons). Ensuite, ajoutez vos images à votre répertoire `public/`. Assurez-vous de les nommer correctement et de les référencer correctement.

Maintenant, si votre serveur de développement était éteint, relancez-le pour voir vos résultats finaux !

```bash
npm run dev
```

![Le blog au-dessus du pli](https://cdn.hashnode.com/res/hashnode/image/upload/v1746947429494/1134babc-6b26-4f88-99df-7c3c8a2e8ba6.png align="center")

![Articles sur le blog](https://cdn.hashnode.com/res/hashnode/image/upload/v1746947441422/5b87e888-a040-4ca1-bc27-7d09e50561ce.png align="center")

![Page À propos](https://cdn.hashnode.com/res/hashnode/image/upload/v1746947455924/64e57b54-feb9-46c9-99c9-8a7260aff45d.png align="center")

## Conclusion

Si vous avez lu jusqu'ici, alors vous devez être vraiment intéressé à voir les résultats de tout cela :) J'ai déjà couvert cela. [Voici le blog](https://chidiadi-portfolio.vercel.app/). Vous pouvez le parcourir et interagir avec.

De plus, [voici la base de code](https://github.com/chidiadi01/simple-writer-portfolio/tree/main/01-simple-blog). N'hésitez pas à la forker, à la cloner et à interagir avec. Si vous avez aimé l'article, veuillez le partager avec d'autres. Vous pouvez également me contacter sur [LinkedIn](https://linkedin.com/in/chidiadi-anyanwu) ou [X](https://x.com/chidiadi01). Merci d'avoir lu.