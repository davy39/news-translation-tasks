---
title: Comment créer un composant piloté par les données avec WordPress et Next.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-23T18:34:28.000Z'
originalURL: https://freecodecamp.org/news/create-a-data-driven-component-with-wordpress-and-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/pexels-pixabay-265667.jpg
tags:
- name: components
  slug: components
- name: Next.js
  slug: nextjs
- name: WordPress
  slug: wordpress
seo_title: Comment créer un composant piloté par les données avec WordPress et Next.js
seo_desc: 'By Kevin Cunningham

  When you are building a content-driven website for a client, there is often some
  tension between creating a consistent user experience and adding some flair.

  If, like I am, you are mostly working in a headless way, you may also wa...'
---

Par Kevin Cunningham

Lorsque vous construisez un site web axé sur le contenu pour un client, il y a souvent une certaine tension entre la création d'une expérience utilisateur cohérente et l'ajout d'une touche d'originalité.

Si, comme moi, vous travaillez principalement en mode headless, vous voudrez peut-être aussi que votre CMS capture et serve des données brutes à des points précis. Vous pouvez manipuler et traiter cela dans le Framework front-end de votre choix.

Lorsque nous construisons des front-ends, nous avons tendance à parler d'architecture orientée composants. Cet article examinera la construction d'un tel composant, du backend jusqu'au front.

## Ce que nous allons construire

Je vais construire l'un des composants FrontPanel de mon site web. Il ressemble à ceci :

![Image](https://res.cloudinary.com/kc-cloud/images/w_1024,h_370,c_scale/v1618999629/Group-6/Group-6-1024x370.png)
_Version annotée du composant FrontPanel_

En regardant le composant, je veux décomposer les données dont j'ai besoin pour pouvoir le générer le plus efficacement possible.

1. Le titre
2. Un texte de description
3. Quatre liens vers des articles pertinents
4. Deux boutons pointant vers d'autres contenus

Maintenant que je sais ce que je vais construire, je dois être capable de capturer et de requêter les données. Pour ce faire, je vais utiliser l'extension [Advanced Custom Fields](https://www.advancedcustomfields.com/) pour WordPress. Cela nous permet d'ajouter des champs à des emplacements spécifiques pour capturer les données dont nous avons besoin.

Si vous utilisez l'extension gratuite, vous bénéficiez de nombreuses fonctionnalités excellentes. La mise à niveau vers ACF Pro ajoute des types de champs vraiment utiles que j'utilise beaucoup dans mon travail pour des clients et dont j'ai du mal à me passer. Pour moi, les points forts sont les [champs Répéteur](https://www.advancedcustomfields.com/resources/repeater/), les [champs de Contenu Flexible](https://www.advancedcustomfields.com/resources/flexible-content/) et les [pages d'Options](https://www.advancedcustomfields.com/resources/options-page/). 

Mais ceci n'est pas une publicité pour ACF ! Pour cet article, j'utiliserai l'extension gratuite. Notez que sur la page d'accueil de ce site web, j'utilise cette même stratégie avec un champ de Contenu Flexible qui me permet de mélanger et d'associer ce composant avec d'autres composants.

## Comment créer des champs personnalisés avec ACF

Une fois que vous avez installé et activé l'extension ACF, vous aurez un nouvel élément dans la barre latérale de votre panneau d'administration WordPress.

![Image](https://res.cloudinary.com/kc-cloud/images/v1618999628/Screenshot-2021-04-21-at-11.03.32/Screenshot-2021-04-21-at-11.03.32.png)

Cliquer sur "Add New" vous permettra de commencer à remplir les champs pour le composant. Il y a beaucoup d'options possibles ici, mais pour les deux premiers champs, nous n'allons remplir que le libellé, le nom et le type.

![Image](https://res.cloudinary.com/kc-cloud/images/w_973,h_1024,c_scale/v1619003387/Screenshot-2021-04-21-at-11.49.59/Screenshot-2021-04-21-at-11.49.59-973x1024.png)

La troisième section de données que nous voulions était un lien vers des articles pertinents. Avec ACF Pro, je configurerais cela comme un champ répéteur, ce qui me permettrait de varier le nombre d'articles. 

Pour l'instant, j'utiliserai un type de champ groupe et j'aurai quatre champs pour capturer les articles pertinents. Chacun des champs du groupe sera de type Post Object. Cela devrait ressembler un peu à ceci :

![Image](https://res.cloudinary.com/kc-cloud/images/w_1024,h_992,c_scale/v1619003386/Screenshot-2021-04-21-at-11.55.48/Screenshot-2021-04-21-at-11.55.48-1024x992.png)

Les derniers champs que nous devons capturer sont ceux des deux boutons. Créons un groupe pour chaque bouton qui aura un libellé et une destination.

![Image](https://res.cloudinary.com/kc-cloud/images/w_1024,h_691,c_scale/v1619003385/Screenshot-2021-04-21-at-12.01.07/Screenshot-2021-04-21-at-12.01.07-1024x691.png)

Tout est prêt ! Notre ensemble final de champs devrait ressembler à ceci :

![Image](https://res.cloudinary.com/kc-cloud/images/w_1024,h_308,c_scale/v1619003384/Screenshot-2021-04-21-at-12.01.30/Screenshot-2021-04-21-at-12.01.30-1024x308.png)

## Comment rendre les champs disponibles

Nous avons le contrôle sur l'endroit et la manière dont ces champs sont affichés dans notre zone d'administration. Je veux que ces panneaux soient disponibles sur n'importe quelle page. Donc, sous les définitions de champs, je vais définir cette règle d'emplacement.

![Image](https://res.cloudinary.com/kc-cloud/images/w_1024,h_159,c_scale/v1619003383/Screenshot-2021-04-21-at-12.03.55/Screenshot-2021-04-21-at-12.03.55-1024x159.png)

Vous pouvez être encore plus granulaire et rendre ces champs disponibles sur une page ou un article particulier. Mais construire une interface avec ACF risque de complexifier excessivement l'expérience de vos éditeurs. Assurez-vous de ne rendre les champs disponibles que là où ils doivent absolument l'être.

Parmi les options que nous n'avons pas examinées lors de la définition de nos champs figuraient celles concernant la mise en page. Cela vous donne un excellent contrôle sur la position et la taille des champs dans l'interface d'administration de WordPress. Il y a beaucoup de possibilités pour que cela fonctionne bien pour vous et votre équipe de création de contenu.

## Comment créer une page avec notre composant

Pour le moment, nous ajoutons le composant ACF à un type de contenu existant. Cela signifie que nous verrons l'éditeur Gutenberg et les champs de notre composant.

Il est possible d'avoir nos champs ACF encapsulés par un bloc Gutenberg, mais il y a quelques raisons pour lesquelles nous n'examinons pas cela dans cet article.

1. Cela nécessite ACF Pro, et je voulais écrire ceci du point de vue de l'extension gratuite
2. Le support des blocs Gutenberg dans GraphQL n'est pas encore tout à fait au point.

Pour l'instant, je vais ajouter du contenu et remplir les champs pour notre composant.

![Image](https://res.cloudinary.com/kc-cloud/images/w_1024,h_971,c_scale/v1619075618/Screenshot-2021-04-22-at-07.54.38/Screenshot-2021-04-22-at-07.54.38-1024x971.png)

Lorsque nous sélectionnons un article, nous obtenons une liste déroulante de tous les articles de notre instance WordPress parmi lesquels choisir. Je vais sélectionner les articles que je veux (qui, dans cette instance d'exemple, concernent tous le WordPress Headless) et enfin remplir les détails de mes boutons.

![Image](https://res.cloudinary.com/kc-cloud/images/w_1024,h_575,c_scale/v1619075617/Screenshot-2021-04-22-at-07.56.12/Screenshot-2021-04-22-at-07.56.12-1024x575.png)

## Comment préparer la requête GraphQL

Il y a deux extensions que nous devons ajouter à notre instance WordPress. WPGraphQL est une extension incroyable construite par Jason Bahl et d'autres contributeurs. Elle est disponible sur le répertoire des extensions WordPress.

Pour rendre les champs ACF disponibles pour GraphQL, une deuxième extension est nécessaire. Elle s'appelle WPGraphQL for Advanced Custom Fields. Elle n'est pas encore dans le répertoire des extensions, mais vous pouvez la télécharger et [l'installer depuis le site web ici](https://www.wpgraphql.com/acf/).

Une fois installée, nous devons retourner dans nos champs personnalisés pour effectuer une dernière configuration.

![Image](https://res.cloudinary.com/kc-cloud/images/w_1024,h_333,c_scale/v1619075616/Screenshot-2021-04-22-at-08.06.17/Screenshot-2021-04-22-at-08.06.17-1024x333.png)

Au bas de notre bloc de champs, nous avons maintenant l'option d'afficher ces champs dans GraphQL et de leur donner un nom. C'est ainsi que nous y ferons référence dans notre requête GraphQL.

Dirigeons-nous vers l'interface GraphiQL pour construire notre requête avant de passer à Next.js pour implémenter cette fonctionnalité.

![Image](https://res.cloudinary.com/kc-cloud/images/w_1024,h_577,c_scale/v1619075615/Screenshot-2021-04-22-at-08.08.11/Screenshot-2021-04-22-at-08.08.11-1024x577.png)

Ce qui est génial avec GraphQL, c'est que nous demandons exactement les données dont nous avons besoin. Ici, je demande tous les nœuds de page et spécifiquement les champs FrontPanel. J'inclurai également le bloc de code au cas où vous voudriez faire un copier-coller.

```graphql
query MyQuery {
  pages {
    nodes {
      frontPanelFields {
        fieldGroupName
        text
        title
        button1 {
          label
          link
        }
        button2 {
          label
          link
        }
        posts {
          post1 {
            ... on Post {
              id
              slug
              title
            }
          }
          post2 {
            ... on Post {
              id
              slug
              title
            }
          }
          post3 {
            ... on Post {
              id
              slug
              title
            }
          }
          post4 {
            ... on Post {
              id
              slug
              title
            }
          }
        }
      }
    }
  }
}
```

## Comment intégrer les données dans Next.js

Si vous n'avez pas encore commencé avec Next.js et WordPress, je vous recommande vivement le [starter Next de mon ami Colby Fayock](https://github.com/colbyfayock/next-wordpress-starter/). Je trouve que la façon dont Colby a structuré les requêtes et les fonctions est vraiment utile. Lorsque j'ajoute de nouvelles fonctionnalités, je l'utilise comme modèle. 

Mon seul reproche est qu'il n'utilise pas Tailwind, qui est mon Framework de style préféré (j'ai commencé un fork pour avoir toutes les fonctionnalités épiques de Colby avec le style Tailwind et j'espère le terminer bientôt).

Je vais supposer que vous utilisez un type de starter WordPress/Next.js ou que vous avez Apollo opérationnel dans votre application Next. Nous devrons utiliser la requête que nous avons construite ci-dessus et l'utiliser au bon endroit.

En suivant l'exemple de Colby, j'ai ajouté une nouvelle fonction de requête à `/data/pages.js`.

```js
export function getQueryFrontPanelById(id) {
  return gql`query {
    page(id: "${id}") {
      frontPanelFields {
        fieldGroupName
        text
        title
        button1 {
          label
          link
        }
        button2 {
          label
          link
        }
        posts {
          post1 {
            ... on Post {
              id
              slug
              title
            }
          }
          post2 {
            ... on Post {
              id
              slug
              title
            }
          }
          post3 {
            ... on Post {
              id
              slug
              title
            }
          }
          post4 {
            ... on Post {
              id
              slug
              title
            }
          }
        }
      }
    }
  }
  `
}
```

C'est exactement la même chose qu'avant, sauf que j'utilise l'id de la page pour obtenir les bonnes données. Les pages sont hiérarchiques dans WordPress et nous ne pouvons donc pas effectuer de recherche par slug. Au lieu de cela, nous devons obtenir l'id et l'utiliser pour trouver la page correspondante.

C'est ce que je fais dans `/lib/pages.js` :

```js
export async function getContentAndFields(slug) {
  // Récupérer toutes les pages WordPress
  const { pages } = await getAllPages()

  // Trouver celle qui a un slug correspondant
  const filteredPages = pages.filter(page => page.slug === slug)

  // Si aucune n'est trouvée, retourner null
  if (filteredPages.length === 0) {
    return null
  }

  // Sinon, récupérer la première
  const page = filteredPages[0]

  // Récupérer les informations du Front Panel
  const { frontPanelFields } = await getFrontPanelById(page.id)

  // et retourner toutes les données.
  return { ...page, frontPanelFields }
}
```

Il se passe beaucoup de choses ici, mais j'espère que les commentaires clarifient les choses.

Maintenant, je vais créer un fichier `[slug].js` dans le répertoire pages que j'utiliserai pour accéder à ma page avec les Front Panels. Voici à quoi ressemble ma version de la page. Encore une fois, je vais annoter avec des commentaires. Cela aura plus de sens si vous commencez par le bas et regardez la fonction `getServerSideProps`, puis recommencez par le haut.

```js
import Layout from "components/Layout"
import FrontPanelComponent from "components/FrontPanelComponent"
import { getContentAndFields } from "lib/pages"

import Error from "next/error"

export default function PageWithAcfComponents({ pageData }) {
  // Si pageData n'existe pas, la page n'existe pas, donc renvoyer une erreur 404.
  if (!pageData) {
    return <Error statusCode={404} />
  }

  // Déstructurer le contenu et les données du panneau à partir des données de la page.
  const { content, frontPanelFields } = pageData;

  return <Layout>
    <div className="mx-auto px-4 sm:px-6 lg:px-8 py-8 blog-post max-w-2xl">
      // Si frontPanelFields existe, afficher le composant.
      {frontPanelFields && <FrontPanelComponent data={frontPanelFields} />}
      // Afficher le reste du contenu dans le DOM.
      <div
        className=""
        dangerouslySetInnerHTML={{
          __html: content,
        }}
      />
    </div>
  </Layout>
}


export async function getServerSideProps({ params = {} } = {}) {
  // Récupérer le slug à partir de la route de la requête.
  const slug = params?.slug;
  // Récupérer les champs et le contenu en utilisant la fonction définie précédemment
  const pageData = await getContentAndFields(slug)
  // Retourner pageData au composant ci-dessus.
  return {
    props: {
      pageData
    }
  }
}
```

Ouf ! C'est beaucoup de code. Nous y sommes presque. La dernière chose que nous devons faire est de construire le FrontPanelComponent.

Voici le code pour cela :

```js
import Link from "next/link";
import Image from "next/image";
import { getMetaImage } from "lib/image";

export default function FrontPanelComponent({ data: { title, text, button1, button2, posts, ...rest } }) {
  return <div className="bg-white p-4 py-20">
    <h2 className="text-center font-bold text-dlblue text-3xl">{title}</h2>
    <div className="flex flex-col md:flex-row justify-between">
      <div>{mapPosts(posts)}</div>
      <div className="text-xl text-black leading-none px-8 xl:text-2xl lg:text-xl -pt-4">
        <div>{text}</div>
      </div>
    </div>
    <div
      className="flex md:flex-row flex-wrap md:justify-end mt-8"
    >
      <div className="text-normal lg:text-xl mx-2">
        <a className="text-white rounded-xl p-4 text-primary hover:bg-primary hover:text-white border-2 border-primary bg-white" href={button1.link} target="_blank">
          {button1.label}
        </a>
      </div>
      <div className="text-normal md:text-xl mx-2">
        <a className="hover:text-lightPrimary hover:bg-white border-2  hover:border-primary text-white bg-lightPrimary rounded-xl p-4" href={button2.link} target="_blank">
          {button2.label}
        </a>
      </div>
    </div>
  </div>
}

function mapPosts(posts) {
  const { post1, post2, post3, post4 } = posts;
  return <div className="pt-8 grid grid-rows-2 grid-cols-2">

    <div className="mx-2">
      <Link href={`/posts/${post1.slug}`}>
        <a>
          <Image src={getMetaImage(post1.title)} width="380" height="200" />
        </a>
      </Link>
    </div>
    <div className="mx-2">
      <Link href={`/posts/${post2.slug}`}>
        <a>
          <Image src={getMetaImage(post2.title)} width="380" height="200" />
        </a>
      </Link>
    </div>
    <div className="mx-2">
      <Link href={`/posts/${post3.slug}`}>
        <a>
          <Image src={getMetaImage(post3.title)} width="380" height="200" />
        </a>
      </Link>
    </div>
    <div className="mx-2">
      <Link href={`/posts/${post4.slug}`}>
        <a>
          <Image src={getMetaImage(post4.title)} width="380" height="200" />
        </a>
      </Link>
    </div>

  </div>
}
```

Pour l'essentiel, il s'agit d'afficher et de styliser les données. J'utilise Tailwind pour mon style, donc cela peut paraître un peu étrange si vous ne le connaissez pas. Cela explique pourquoi j'ai des noms de classes aux sonorités si bizarres !

Il y a trois choses distinctes sur lesquelles j'aimerais attirer l'attention dans ce bloc de code :

1. J'utilise le composant Next Link. Cela indique à Next que je fais référence à un lien interne à l'application et gère le pré-chargement et les changements de page sans rafraîchissement.
2. J'utilise également le composant Next Image. Celui-ci gère l'optimisation des images et le lazy loading. Il fonctionne comme une balise image normale, mais vous devez fournir les dimensions de l'image finale.
3. J'utilise une fonction appelée `getMetaImage`. Cette fonction construit un lien Cloudinary qui superpose le titre de l'article sur une image de base que j'utilise pour tous mes articles.

## Et nous y sommes...

Il y a beaucoup de code dans cet article, bravo d'avoir tenu bon jusqu'ici. Vous pouvez voir le produit final des FrontPanels sur ma page d'accueil (https://kevincunningham.co.uk).

Comme j'ai utilisé l'extension ACF gratuite, je n'ai pas pu traiter les champs répéteurs ou le contenu flexible. Ce sera l'objet d'un autre article. Pour l'instant, vous pouvez voir le flux de création de champs, leur remplissage, leur exposition à GraphQL, puis la création des composants sur le front-end.

J'espère que cela vous a été utile. Je vais faire plus de diffusions en direct et produire plus de contenu vidéo sur ces sujets. [Inscrivez-vous à ma newsletter](https://kevincunningham.co.uk/newsletter) si vous souhaitez être informé de ces contenus et plus encore.