---
title: Comment intégrer WordPress en tant que CMS headless avec Next.js – avec exemples
  de code
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2024-10-02T09:07:58.757Z'
originalURL: https://freecodecamp.org/news/integrate-wordpress-with-nextjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727738740919/4dd5ea12-6e0c-4df9-8b8d-fc4f168b89c5.jpeg
tags:
- name: WordPress
  slug: wordpress
- name: Next.js
  slug: nextjs
- name: cms
  slug: cms
seo_title: Comment intégrer WordPress en tant que CMS headless avec Next.js – avec
  exemples de code
seo_desc: 'When building a dynamic blog website, it''s common to fetch data from a
  content source, such as a CMS (Content Management System) like WordPress.

  Recently, I faced the challenge of integrating WordPress into my existing Next.js
  project. I had a blog h...'
---

Lors de la création d'un site de blog dynamique, il est courant de récupérer des données à partir d'une source de contenu, telle qu'un CMS (Content Management System) comme WordPress.

Récemment, j'ai été confronté au défi d'intégrer WordPress dans mon projet Next.js existant. J'avais un blog hébergé sur WordPress et je voulais le migrer vers mon application Next.js.

J'avais besoin d'une solution qui me permettrait d'utiliser WordPress comme un CMS headless. L'objectif était simple : tirer parti de la puissance de WordPress pour la gestion du contenu tout en utilisant un Framework frontend moderne pour l'affichage.

Dans cet article, nous allons voir comment intégrer WordPress à une application Next.js.

## Pourquoi utiliser un CMS headless ?

Un CMS headless sépare la gestion du contenu (back-end) de la couche de présentation (front-end). Cela donne aux développeurs plus de flexibilité sur la manière dont le contenu est livré et affiché, sans être limité par les thèmes ou les mises en page traditionnels.

C'est excellent pour la performance et l'évolutivité, offrant plus de contrôle sur le rendu du contenu sur le frontend. Dans ce cas, vous utiliserez WordPress comme système de gestion de contenu mais afficherez le contenu de manière plus moderne et performante en utilisant Next.js.

## Qu'est-ce que Next.js ?

Si vous n'avez pas encore découvert Next.js, c'est un Framework puissant basé sur React qui facilite grandement la création d'applications optimisées avec rendu côté serveur (SSR).

Il offre de nombreuses fonctionnalités prêtes à l'emploi comme le routage basé sur les fichiers, les API routes, la génération de sites statiques (SSG) et la régénération statique incrémentale (ISR). Tout cela en fait un excellent choix pour créer des sites web rapides et optimisés pour le SEO.

## Comment connecter WordPress et Next.js

Lorsque vous utilisez WordPress comme CMS headless, il existe deux manières principales de connecter votre application Next.js à votre backend WordPress :

1. **API REST WP** : WordPress est livré avec une API REST intégrée, qui vous permet de récupérer du contenu de WordPress au format JSON.
    
2. **WPGraphQL** : WordPress prend en charge la gestion de contenu headless grâce à l'utilisation de GraphQL (avec des plugins tels que [WPGraphQL](https://www.wpgraphql.com/)), ce qui facilite l'interrogation et la récupération de contenus spécifiques, comme les articles de blog, pour une utilisation dans un Framework front-end comme React.
    

Bien que l'API REST soit populaire, nous allons opter pour WPGraphQL car il permet des requêtes plus précises et plus de flexibilité. Avec GraphQL, vous pouvez demander exactement les données dont vous avez besoin, ce qui peut réduire la quantité de données transférées et améliorer les performances.

### Étapes pour connecter WordPress et Next.js en utilisant WPGraphQL

![Page du plugin WordPress WPGraphQL](https://cdn.hashnode.com/res/hashnode/image/upload/v1727738853280/6e07d4f5-d4c7-40a8-9355-804251707593.png align="center")

La première chose à faire est d'installer le plugin WPGraphQL sur votre site WordPress. Ce plugin active la fonctionnalité d'API GraphQL dans WordPress. Vous pouvez installer le plugin comme n'importe quel autre en naviguant dans le tableau de bord d'administration de WordPress.

Tout d'abord, allez dans **Extensions** et sélectionnez **Ajouter**. Ensuite, recherchez **WPGraphQL**, et une fois que vous l'avez trouvé, installez et activez simplement le plugin.

Après l'installation et l'activation du plugin, l'IDE GraphQL apparaîtra sur le tableau de bord WordPress. Ici, vous pouvez tester diverses requêtes dont vous pourriez avoir besoin pour votre développement frontend.

Passons maintenant au frontend.

### Comment récupérer des données depuis WPGraphQL dans Next.js

Dans votre projet Next.js, vous devrez récupérer des données depuis l'API GraphQL. Voici un exemple simple utilisant `graphql-request` :

1\. Installez `graphql-request` pour faciliter l'interrogation de l'API GraphQL :

```bash
npm install graphql-request
```

2\. Dans votre composant Next.js, créez une requête GraphQL pour récupérer les articles de blog :

```typescript
import BlogHeader from '@/components/blog/BlogHeader';
import BlogNewsletter from '@/components/blog/BlogNewsletter';
import BlogPosts from '@/components/blog/BlogPosts';
import Link from 'next/link';
import React from 'react';

import { request, gql } from "graphql-request";

const query = gql`
{
  posts(first: 10) {
    edges {
      node {
        id
        title
        excerpt
        content
        date
        author {
          node {
            id
            name            
          }
        }
        date
        slug
        featuredImage {
          node {
            sourceUrl
          }
        }
        categories {
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}
`

export async function getStaticProps() {
  try {
    // Tentative de récupération des articles depuis le point de terminaison GraphQL
    const posts: any = await request('https://blog.intercity.ng/graphql', query);

    return {
      props: { posts }
    }
  } catch (error) {
    console.error('Erreur lors de la récupération des articles :', error);
    return {
      props: {
        posts: []
      }
    };
  }
}

const Index = ({ posts }: { posts: any }) => {

  return (
    <main className="relative pb-10 pt-10 lg:pt-0 lg:mt-[-3%]">
      <div className='t40-container w-full'>
        <BlogHeader />
        <BlogPosts posts={posts} />
        <BlogNewsletter />
      </div>
    </main>
  )
}

export default Index
```

Dans le code ci-dessus, votre application Next.js récupère les articles de blog de votre backend WordPress via GraphQL et les affiche sur le frontend. La requête GraphQL est conçue pour récupérer les détails de l'article tels que le titre, l'auteur, le contenu et l'image à la une.

En utilisant `getStaticProps` de Next.js, les données sont récupérées au moment du build et transmises comme props au composant. Les articles de blog sont rendus via des composants personnalisés comme `BlogHeader`, `BlogPosts` et `BlogNewsletter`, rendant la page dynamique et efficace.

Ceci démontre comment WordPress peut être utilisé comme un CMS headless pour une application Next.js. Maintenant que vous avez intégré avec succès WordPress en tant que CMS headless dans votre application Next.js, vous pouvez continuer à récupérer plus de données de l'API GraphQL pour enrichir les fonctionnalités de votre application.

### Conclusion

En utilisant WordPress comme CMS headless et Next.js pour le frontend, nous pouvons construire un blog rapide, optimisé pour le SEO, tout en profitant des puissantes fonctionnalités de gestion de contenu de WordPress.

L'utilisation de WPGraphQL nous a permis de récupérer efficacement uniquement les données dont nous avions besoin, nous donnant plus de contrôle et améliorant les performances du site.

J'espère que cela vous a été utile. Bon codage !