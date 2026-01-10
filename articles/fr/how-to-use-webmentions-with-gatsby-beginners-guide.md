---
title: Comment utiliser les Webmentions avec Gatsby.js – Un guide pour débutants
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-07-22T16:33:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-webmentions-with-gatsby-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Web-capture_19-7-2021_222358_iamspruce.dev-1.jpeg
tags:
- name: Gatsby
  slug: gatsby
- name: React
  slug: react
- name: social media
  slug: social-media
seo_title: Comment utiliser les Webmentions avec Gatsby.js – Un guide pour débutants
seo_desc: 'Webmention is a simple protocol developed by the IndieWeb Community that
  you can use to request notifications when your URLs are mentioned on the web.

  When you post on your own site and syndicate elsewhere (POSSE), Webmention lets
  you enable rich int...'
---

[Webmention](https://indieweb.org/webmention) est un protocole simple développé par la communauté IndieWeb que vous pouvez utiliser pour demander des notifications lorsque vos URL sont mentionnées sur le web.

Lorsque vous publiez sur votre propre site et syndiquez ailleurs ([POSSE](https://indieweb.org/POSSE)), Webmention vous permet d'activer des interactions riches sur vos publications syndiquées. Cet article vous guidera à travers la manière la plus simple de transformer vos interactions sur les réseaux sociaux en Webmentions et de les afficher sur votre site Gatsby.js.

Ce tutoriel implémentera les Webmentions sur un site déjà existant, vous devriez donc avoir au moins quelques connaissances de base de React et Gatsby.

## Commencer

Pour vous aider à mieux comprendre comment fonctionnent les Webmentions, consultez l'image ci-dessous :

![Étapes d'envoi et de réception des webmentions](https://www.freecodecamp.org/news/content/images/2021/07/new-webmentions-cycle-1.jpg align="left")

*Différentes étapes du processus Webmention*

Décomposons ces trois étapes et apprenons comment les implémenter.

## Comment envoyer des Webmentions

Un expéditeur de Webmention est une implémentation qui envoie des Webmentions. [Bridgy](https://brid.gy/) est un bon exemple d'expéditeur.

Bridgy est un outil open source qui récupère vos interactions sur les réseaux sociaux à partir de sites populaires et de moteurs de blog comme Twitter, Facebook, Instagram et Medium, et les transforme magiquement en Webmentions.

![Bridgy transformant les interactions sur les réseaux sociaux en Webmentions](https://www.freecodecamp.org/news/content/images/2021/07/bridy-line-1.jpg align="left")

*Bridgy transformant les interactions sociales en Webmentions*

Pour utiliser Bridgy, votre domaine doit supporter le [processus de connexion indieAuth](https://indieauth.com/).

Dans votre composant `layout.js` (ou à partir de n'importe quel composant où vous gérez votre `<head>` avec React Helmet), ajoutez le code suivant pour lier vos profils sociaux :

```javascript
import { Helmet } from "react-helmet"
// autres imports

export default function Layout({ children}) {

  return (
    <div className="wrapper">
      <Helmet>
          
        <link rel="me" href="https://twitter.com/sprucekhalifa" />
        <link rel="me" href="https://github.com/iamspruce" />
          
      </Helmet>
...
    </div>
  )
}
```

Sur chacun des services sociaux que vous venez de lier, assurez-vous que votre profil contient un lien menant à votre page d'accueil comme vous pouvez le voir ci-dessous :

![Liens de retour vers votre site web](https://www.freecodecamp.org/news/content/images/2021/07/twitter-link-back.jpg align="left")

*Ajout d'un lien vers votre page d'accueil sur Twitter*

C'est tout ! Vous avez terminé le processus de connexion IndieAuth. Rendez-vous maintenant sur [Bridgy](https://brid.gy/) et connectez-vous avec Twitter (si vous avez utilisé Twitter pour votre processus IndieAuth).

Désormais, Bridgy analysera périodiquement vos tweets ([Je promets qu'il ne fait rien avec vos données](https://brid.gy/about#privacy)). Pour chaque tweet contenant un lien vers votre site, il récupérera toutes les réponses, les likes, les retweets, etc., et les enverra en tant que Webmentions.

## Comment recevoir des Webmentions

Un récepteur de Webmention est une implémentation qui reçoit des Webmentions vers une ou plusieurs URL cibles.

Cette implémentation peut être un script exécuté sur votre serveur, mais dans le cas de GatsbyJs qui n'a pas de serveur, nous nous appuierons sur un outil tiers appelé [webmention.io](https://webmention.io/) créé par [Aaron Parecki](https://aaronparecki.com/).

Cet outil reçoit vos Webmentions et les stocke et les organise. Il fournit également une API que vous pouvez utiliser pour récupérer facilement vos Webmentions et les afficher sur votre site.

Pour utiliser webmention.io, assurez-vous d'avoir suivi le processus de connexion IndieAuth dans la section "Comment envoyer des Webmentions". Ensuite, allez sur [webmention.io](https://webmention.io/) et connectez-vous avec votre nom de domaine.

Une fois inscrit, ajoutez ce qui suit à la section `<head>` de votre site (et remplacez simplement `username` par le nom d'utilisateur que vous avez obtenu lorsque vous vous êtes connecté) :

```javascript
import { Helmet } from "react-helmet"
// autres imports

export default function Layout({ children}) {

  return (
    <div className="wrapper">
      <Helmet>
        ...
        <link rel="webmention" href="https://webmention.io/username/webmention" />
        <link rel="pingback" href="https://webmention.io/username/xmlrpc" />
          
      </Helmet>
...
    </div>
  )
}
```

Lorsque vous commencez à recevoir des Webmentions de vos URL cibles, vous devriez les voir dans votre tableau de bord comme ceci :

![Tableau de bord webmention.io](https://www.freecodecamp.org/news/content/images/2021/07/Web-capture_21-7-2021_51043_webmention.io.jpeg align="left")

*Tableau de bord webmention.io*

Vous pouvez facilement surveiller vos Webmentions dans votre tableau de bord.

## Comment récupérer les données de Webmentions sur votre site web

C'est la partie amusante où vous allez récupérer vos données de Webmentions à partir de l'API Webmention.io. Pour ce faire, j'ai créé un plugin Gatsby appelé `[gatsby-source-webmentions](https://www.npmjs.com/package/gatsby-source-webmentions)`

NOTE : il existe un autre plugin appelé `[gatsby-plugin-webmentions](https://github.com/ChristopherBiscardi/gatsby-plugin-webmention)` qui récupère les données de Webmentions à partir de l'API webmention.io et les rend disponibles dans Graphql.

### Spruce, s'il existe déjà un plugin Gatsby, pourquoi en créer un autre ?

J'ai créé ce plugin pour deux raisons :

1. D'abord parce que je peux, et pourquoi pas.
    
2. Ensuite, pour l'optimisation des images – ce plugin vous permet d'utiliser le plugin gatsby-image pour optimiser les images retournées par l'API.
    

### Comment installer le plugin

Pour installer le plugin, ouvrez votre terminal système ou le terminal intégré de VS Code et exécutez ce qui suit :

```js
npm install gatsby-source-webmentions
```

Ensuite, vous devrez ajouter le plugin à votre tableau de plugins dans `gatsby-config.js` :

```js
   { 
      resolve: "gatsby-source-webmentions",
      options: {
        DOMAIN: "example.com", // sans https et sans barres obliques
        TOKEN: process.env.WEBMENTIONS_TOKEN, // jeton de webmention.io
        perPage: 100, // optionnel
      },
```

Le plugin prend quelques options :

1. DOMAIN : le nom de domaine que vous avez utilisé pour vous connecter à [webmention.io](http://webmention.io)
    
2. TOKEN : le jeton que vous avez obtenu de votre tableau de bord [webmention.io](http://webmention.io)
    
3. perPage : le nombre de Webmentions que vous souhaitez récupérer par page (ceci est complètement optionnel)
    

Pour éviter de pousser votre jeton secret vers GitHub, ajoutez-le en tant que [variable d'environnement](https://www.gatsbyjs.com/docs/how-to/local-development/environment-variables/).

### Comment afficher les Webmentions côté client

Si vous créez vos pages dynamiquement avec l'API Node [createPage](https://www.gatsbyjs.com/docs/reference/config-files/gatsby-node/#createPages), il y a de fortes chances que vous ayez passé la variable `slug` à toutes les pages de votre site. Si vous n'êtes pas sûr ou si vous l'avez nommée autrement, vérifiez simplement votre fichier `gatsby-node.js`.

![GatsbyJs générant un slug](https://www.freecodecamp.org/news/content/images/2021/07/graphql-variable.jpg align="left")

*Utilisation de Create pages pour générer un slug pour les pages du site*

Dans votre fichier `src/templates/blog.js` ou là où se trouvent vos modèles de page, vous interrogerez les Webmentions uniquement si le `wm_slug` correspond au `slug` de la page.

```js
import React from "react"
import { graphql } from "gatsby"
import Layout from "../components/Layout"
import Comment from "./Comment"


export const query = graphql`
  query($slug: String!) {
    allWebmention(filter: { wm_slug: { eq: $slug } }) {
        totalCount
        edges {
          node {
            id
            published
            publishedFormated: published(formatString: "MMM Do, YYYY")
            author {
                name
                photo
                url
            }
            url
            wm_id
            content {
              html
            }
          }
        }
      }
    }
`

export default function BlogPost({ data, location }) {
...
  const mentions = data.allWebmention

  return (
    <>
      <Layout>
      ...
      // afficher les mentions dans un composant react
      </Layout>
    </>
  )
}
```

`wm_slug` est un nœud que j'ai créé pour récupérer le slug à partir de `wm_target`.

![Image montrant wm_target et wm_slug](https://www.freecodecamp.org/news/content/images/2021/07/wm_slug.jpg align="left")

Maintenant, vous pouvez mapper toutes les Webmentions pour ce slug cible et les afficher dans un composant React :

```js
import React from "react"
import { graphql } from "gatsby"
import Layout from "../components/Layout"
import Comment from "./Comment"


export const query = graphql`
  query($slug: String!) {
    allWebmention(filter: { wm_slug: { eq: $slug } }) {
    // requêtes graphql
      }
    }
`

export default function BlogPost({ data }) {
...
  const mentions = data.allWebmention

  return (
    <>
      <Layout>
      ...
          <ol className="webmentions__list">
      {mentions.edges.map(edge => (
        <Comment
          key={edge.node.wm_id}
          imageUrl={edge.node.author.photo}
          authorUrl={edge.node.author.url}
          authorName={edge.node.author.name}
          dtPublished={edge.node.published}
          dtPublishedFormated={edge.node.publishedFormated}
          content={edge.node.content && edge.node.content.html}
          url={edge.node.url}
        />
      ))}
      </ol>
      </Layout>
    </>
  )
}
```

### Comment regrouper les Webmentions par type

Bien que cela soit complètement optionnel, il est bon de regrouper vos Webmentions par type :

1. `"in_reply_to"` – pour les réponses
    
2. `"like_of"` – pour les likes
    
3. `"retweet_of"` – pour les retweets, etc.
    

```js
...

export const query = graphql`
  query($slug: String!) {
    allWebmention(filter: { wm_slug: { eq: $slug } }) {
      likes: group(field: like_of) {
        totalCount
        edges {
          node {
             // requêtes de nœud
          }
        }
      }

      replies: group(field: in_reply_to) {
        totalCount
        edges {
          node {
            // requêtes de nœud
        }
      }
    }
}
...
```

### Comment optimiser les images des auteurs de Webmentions

J'ai mentionné précédemment que le `gatsby-source-plugin` nous permet d'optimiser les images retournées par la requête Webmentions.

Pour pouvoir optimiser les images, vous devez avoir installé `[gatsby-plugin-image](https://www.gatsbyjs.com/plugins/gatsby-plugin-image/)`, `gatsby-plugin-sharp`, `gatsby-transformer-sharp` et `gatsby-source-filesystem` :

```js
export const query = graphql`
  query($slug: String!) {
    allWebmention(filter: { wm_slug: { eq: $slug } }) {
      likes: group(field: like_of) {
        totalCount
        edges {
          node {
            // autres requêtes de nœud
            author {
                photoSharp {
                  childImageSharp {
                    gatsbyImageData(
                      width: 38
                      placeholder: BLURRED
                      formats: [AUTO, WEBP, AVIF]
                )
              }
             }
            }
          }
        }
      }
    }
`
```

Pour d'autres optimisations et traitements d'image, consultez le [guide de référence](https://www.gatsbyjs.com/docs/reference/built-in-components/gatsby-plugin-image/) de `gatsby-plugin-image`.

### Comment ajouter une pagination personnalisée

Vous pouvez paginer vos Webmentions avec l'un des nombreux plugins de pagination de Gatsby. Mais tout ce que je voulais était un simple bouton "Charger plus", et heureusement, des personnes plus intelligentes comme [Eric Howey](https://www.erichowey.dev/) y ont déjà pensé.

Le code ci-dessous provient de l'article [**Bouton Charger plus et défilement infini dans Gatsby**](https://www.erichowey.dev/writing/load-more-button-and-infinite-scroll-in-gatsby/) (bien que j'aie apporté quelques ajustements) :

```js
import React, { useState, useEffect } from "react"
import { graphql } from "gatsby"
import Button from "./Button"
import Comment from "./Comment"

export const query = graphql`
  query($slug: String!) {
    allWebmention(filter: { wm_slug: { eq: $slug } }) {
        totalCount
        edges {
          node {
          // requêtes de nœud
         }
        }
       }
      }

export default function BlogPost({ data }) {
...
  const replies = data.allWebmention

  const [state, setState] = useState({
    list: [...replies.slice(0, 5)],
    Load_more: false,
    has_more: replies.length > 5,
  })
  const handleState = () => {
    state.Load_more = true
  }
  //gérer le chargement de plus de mentions
  useEffect(() => {
    if (state.Load_more && state.has_more) {
      const currentLength = state.list.length
      const is_more = currentLength < replies.length
      const new_list = is_more
        ? replies.slice(currentLength, currentLength + 5)
        : []
      setState.list = [...state.list, ...new_list]
      setState.Load_more = false
    }
  }, [state.Load_more, state.has_more, replies, state.list])

  useEffect(() => {
    const is_more = state.list.length < replies.length
    setState.has_more = is_more

  }, [state.list,replies.length])
  return (
    <div className="webmentions-wrapper">
      {replies.length > 0 ? (
        <>
    <h4>Commentaires <span className="webmentions-counter">{replies[0].totalCount}</span> </h4>
    <ol className="webmentions__list">
      {state.list.edges.map(edge => (
        <Comment
          key={edge.node.wm_id}
          imageUrl={edge.node.authorImg}
          authorUrl={edge.node.authorUrl}
          authorName={edge.node.authorName}
          dtPublished={edge.node.published}
          dtPublishedFormated={edge.node.publishedFormated}
          content={edge.node.content && edge.node.content.html}
          url={edge.node.url}
        />
      ))}
      </ol>
      <div className="webmentions-load text-center">
      {state.has_more ? (
          <Button
            event={handleState}
            name="Load More"
            label="Load More Webmentions"
            btnSize="small"
            btnType="primary"
          />
      ) : (
        <p>No More Mentions...</p>
      )}
    </div>
        </>
      ) : (
        <p>No Webmentions found</p>
      )}
    </div>
  )
}
```

## Déploiement continu avec les Webmentions

Comme vous l'avez peut-être remarqué, vos données de Webmentions sont récupérées au moment de la construction. Cela signifie que les utilisateurs ne verront pas les nouvelles Webmentions à moins que votre site n'ait été construit.

J'héberge mon site sur Gatsby Cloud et pour éviter de sortir du lit à minuit pour construire mon site, il nous fournit un WEBHOOK qui peut déclencher une construction pour votre site même pendant que vous dormez.

Si vous utilisez Gatsby Cloud, allez sur votre [tableau de bord](https://www.gatsbyjs.com/dashboard/) et copiez le Webhook :

![Tableau de bord Gatsby Cloud](https://www.freecodecamp.org/news/content/images/2021/07/Web-capture_21-7-2021_7512_www.gatsbyjs.com.jpeg align="left")

*Webhooks du tableau de bord Gatsby Cloud*

Une fois que vous avez copié le Webhook, rendez-vous sur votre tableau de bord webmention.io, cliquez sur [Web hooks](https://webmention.io/settings/webhooks) et collez le Webhook copié dans le formulaire :

![Webhook webmention.io](https://www.freecodecamp.org/news/content/images/2021/07/Web-capture_21-7-2021_72655_webmention.io.jpeg align="left")

*Webhooks webmention.io*

C'est tout – vous avez terminé. Maintenant, chaque fois que vous recevez une nouvelle Webmention, le Webhook construira votre site automatiquement.

## Conclusion

Dans ce tutoriel, nous avons appris comment implémenter les Webmentions sur votre site Gatsby. Si vous avez des questions ou si vous avez trouvé ce tutoriel utile, n'hésitez pas à me contacter sur Twitter [@sprucekhalifa](https://twitter.com/sprucekhalifa). Merci.

Bon codage !