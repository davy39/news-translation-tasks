---
title: Comment cross-poster automatiquement depuis votre blog GatsbyJS avec RSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-11T18:45:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-automatically-cross-post-from-your-gatsbyjs-blog-with-rss
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/gatsby-rss.jpg
tags:
- name: blog
  slug: blog
- name: canonical url
  slug: canonical-url
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: rss feed
  slug: rss-feed
- name: SEO
  slug: seo
seo_title: Comment cross-poster automatiquement depuis votre blog GatsbyJS avec RSS
seo_desc: 'By Dane Stevens

  With the recent exodus from Medium many developers are now creating their own GatsbyJS
  Blogs and then cross-posting to Medium or publications like freecodecamp.org and
  dev.to.

  Cross-posting is time consuming, but necessary to drive tr...'
---

Par Dane Stevens

Avec l'exode récent de [Medium](https://medium.com), de nombreux développeurs créent désormais leurs propres blogs GatsbyJS, puis cross-postent vers [Medium](https://medium.com) ou des publications comme [freecodecamp.org](https://www.freecodecamp.org/news/) et [dev.to](https://dev.to).

Le cross-posting est chronophage, mais nécessaire pour générer du trafic vers votre site personnel. Voyons comment nous pouvons automatiser cela en ajoutant un flux RSS à votre blog GatsbyJS personnel.

## Ajouter des URL canoniques à votre blog

Qu'est-ce qu'une URL canonique ?

![URL canonique pour Tueri.io](https://cdn.tueri.io/274877907146/carbon.png)

Une URL canonique indique aux moteurs de recherche quelle page est la page principale ou autoritaire lorsque du contenu dupliqué est trouvé (c'est-à-dire le cross-posting).

Installons [gatsby-plugin-canonical-urls](https://www.gatsbyjs.org/packages/gatsby-plugin-canonical-urls/)

**Astuce rapide :** `npm i` est un alias pour `npm install --save`

```
npm i gatsby-plugin-canonical-urls

```

**Remarque :** Si vous utilisez `gatsby-plugin-react-helmet`, installez plutôt ce plugin : [gatsby-plugin-react-helmet-canonical-urls](https://www.gatsbyjs.org/packages/gatsby-plugin-react-helmet-canonical-urls/)*

```
npm i gatsby-plugin-react-helmet-canonical-urls

```

Ajoutez la configuration du plugin à `/gatsby-config.js`

```javascript
// Dans votre gatsby-config.js
plugins: [
  {
    resolve: `gatsby-plugin-canonical-urls`,
    // ou
    // resolve: `gatsby-plugin-react-helmet-canonical-urls`
    options: {
      // Changez `siteUrl` par votre domaine
      siteUrl: `https://tueri.io`
      
      // Les paramètres de chaîne de requête sont inclus par défaut.
      // Définissez `stripQueryString: true` si vous ne voulez pas que `/blog`
      // et `/blog?tag=foobar` soient indexés séparément
      stripQueryString: true
    }
  }
]

```

Avec cette configuration, le plugin ajoutera un `<link rel="canonical" ... />` à l'en-tête de chaque page, par exemple :

```html
<link rel="canonical" href="https://tueri.io/2019-04-04-how-to-securely-deploy-to-kubernetes-from-bitbucket-pipelines/" />

```

## Installer un générateur de flux RSS

Nous utiliserons [gatsby-plugin-feed](https://www.gatsbyjs.org/packages/gatsby-plugin-feed/) pour générer un flux RSS à partir de nos articles de blog.

```
npm i gatsby-plugin-feed

```

Ajoutez la configuration du plugin à `/gatsby-config.js`

```javascript
// Dans votre gatsby-config.js
plugins: [
  {
    resolve: `gatsby-plugin-feed`,
    options: {
      query: `
        {
          site {
            siteMetadata {
              title
              description
              siteUrl
              site_url: siteUrl
            }
          }
        }
      `,
      feeds: [
        {
          serialize: ({ query: { site, allMarkdownRemark } }) => {
            return allMarkdownRemark.edges.map(edge => {
              return Object.assign({}, edge.node.frontmatter, {
                description: edge.node.excerpt,
                date: edge.node.frontmatter.date,
                url: site.siteMetadata.siteUrl + edge.node.fields.slug,
                guid: site.siteMetadata.siteUrl + edge.node.fields.slug,
                custom_elements: [{ "content:encoded": edge.node.html }],
              })
            })
          },
          query: `
            {
              allMarkdownRemark(
                sort: { order: DESC, fields: [frontmatter___date] },
              ) {
                edges {
                  node {
                    excerpt
                    html
                    fields { slug }
                    frontmatter {
                      title
                      date
                    }
                  }
                }
              }
            }
          `,
          output: "/rss.xml",
          title: "Flux RSS de votre site",
          // configuration optionnelle pour insérer la référence du flux dans les pages :
          // si une `chaîne` est utilisée, elle servira à créer une RegExp puis à tester si le chemin
          // de la page actuelle satisfait cette expression régulière ;
          // si non fourni ou `indéfini`, toutes les pages auront une référence de flux insérée
          match: "^/blog/",
        },
      ],
    }
  }
]

```

**REMARQUE :** Ce plugin ne génère le(s) fichier(s) `xml` que lorsqu'il est exécuté en mode `production` ! Pour tester votre flux, exécutez : `gatsby build && gatsby serve`

Voici à quoi ressemble notre flux : [Flux RSS de Tueri.io](https://tueri.io/rss.xml)

Pour plus d'informations sur la configuration de votre flux, consultez la [documentation du plugin](https://www.gatsbyjs.org/packages/gatsby-plugin-feed/).

## Connecter [dev.to](https://dev.to) à votre flux RSS

1. Connectez-vous à votre compte [dev.to](https://dev.to)
2. Allez dans : Paramètres > Publishing from RSS ou [https://dev.to/settings/publishing-from-rss](https://dev.to/settings/publishing-from-rss)
3. Ajoutez votre "URL de flux RSS" par exemple [https://tueri.io/rss.xml](https://tueri.io/rss.xml)
4. Cochez "Marquer la source RSS comme URL canonique par défaut"
5. Cliquez sur "Mettre à jour"

![Capture d'écran des paramètres RSS de dev.to](https://cdn.tueri.io/274877907149/screencapture-dev-to-settings-publishing-from-rss-2019-06-06-06_48_32.png)

## Connecter [Medium](https://medium.com) à votre flux RSS

La connexion pour [Medium](https://medium.com) n'est pas tout à fait aussi directe, mais assez simple avec [Zapier](https://zapier.com).

Rendez-vous sur [Zapier](https://zapier.com) et créez un compte gratuit.

### "Créer un Zap"

1. Choisissez "RSS" comme "Application de déclenchement"
2. Sélectionnez "Nouvel élément dans le flux"
3. Collez votre "URL de flux"
4. Sélectionnez un exemple de votre flux.
5. Choisissez "Medium" comme "Application d'action"
6. Sélectionnez "Créer une histoire"
7. Autorisez votre compte Medium
8. Sélectionnez vos champs : assurez-vous de sélectionner votre URL canonique
9. Envoyez un test à Medium
10. Terminez et activez votre Zap

![Capture d'écran de la connexion de RSS à Medium avec Zapier](https://cdn.tueri.io/274877907150/screencapture-zapier-app-editor-59814153-nodes-59814313-fields-2019-06-06-06_53_55.png)

## Conclusion

Assurez-vous que Google vous crédite pour votre contenu en utilisant des URL canoniques.

J'espère que vous avez trouvé cela utile et que cela vous fera gagner beaucoup de temps à cross-poster votre contenu !

---

*Initialement publié sur [Tueri.io](https://tueri.io/blog/2019-06-06-how-to-automatically-cross-post-from-your-gatsbyjs-blog-with-rss/?utm_source=Freecodecamp&utm_medium=Post&utm_campaign=)*