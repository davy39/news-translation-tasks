---
title: 'Gatsby Starter Blog : Comment ajouter des images d''en-tête aux articles avec
  support pour les Twitter Cards'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-29T00:33:15.000Z'
originalURL: https://freecodecamp.org/news/gatsby-blog-header-image-twitter-card
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/freeCodeCamp-GatsbyBlogImageTwitterCard-5.png
tags:
- name: blog
  slug: blog
- name: Gatsby
  slug: gatsby
- name: GraphQL
  slug: graphql
- name: open graph
  slug: open-graph
- name: Twitter
  slug: twitter
seo_title: 'Gatsby Starter Blog : Comment ajouter des images d''en-tête aux articles
  avec support pour les Twitter Cards'
seo_desc: "By David Good\nIf you're like me, you used Gatsby Starter Blog to kickstart\
  \ your personal blog, made a few customizations, and then just rolled with it. \n\
  Adding new posts in the form of markdown is great. But it also means you rarely\
  \ have a reason to ..."
---

Par David Good

Si vous êtes comme moi, vous avez utilisé [Gatsby Starter Blog](https://www.gatsbyjs.com/starters/gatsbyjs/gatsby-starter-blog) pour lancer votre blog personnel, fait quelques personnalisations, et ensuite vous l'avez utilisé tel quel. 

Ajouter de nouveaux articles sous forme de markdown est génial. Mais cela signifie aussi que vous avez rarement une raison de regarder le code. Donc, lorsque j'ai décidé d'ajouter des images d'en-tête à mes articles avec support pour les [Twitter Cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards), je me suis senti perdu.

Mes exigences étaient de pouvoir ajouter une grande image d'en-tête avec une légende à un article comme vous pouvez le voir ici :

%[https://davidagood.com/dynamodb-enhanced-client-java-heterogeneous-item-collections/]

De plus, un tweet contenant un lien vers l'article devrait s'"étendre" en [Carte Résumé Twitter avec Grande Image](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image), comme ceci :

%[https://twitter.com/helloworldless/status/1336323721254948864]

Et enfin, pour les articles qui ne spécifient pas d'image, une image par défaut devrait être affichée en utilisant [Carte Résumé Twitter](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary). Voici à quoi cela ressemble où j'ai utilisé le logo de mon site web comme image par défaut :

%[https://twitter.com/helloworldless/status/1338482084445347844]

**Note :** La documentation de Twitter indique qu'un logo de site web ne doit pas être utilisé pour une image de carte (voir la section `twitter:image` [ici](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary#reference)). Je vous laisse décider si cela a du sens d'utiliser une image fixe comme solution de repli comme je l'ai fait ici.

## Pour commencer

Voici les cinq étapes de haut niveau que je vais vous guider à travers. Je vais essayer d'expliquer tout en profondeur et fournir des liens vers d'autres ressources en cours de route. Ainsi, vous construirez vos connaissances de Gatsby que vous pourrez utiliser pour aborder les étapes ultérieures, plus compliquées.

1. Ajouter des balises de métadonnées de document
2. Source de l'image par défaut en utilisant GraphQL
3. Source des propriétés d'image spécifiques aux articles en utilisant GraphQL
4. Ajouter une image d'en-tête au modèle de blog
5. Ajouter de nouvelles propriétés au frontmatter de l'article

Les outils que nous allons utiliser pour accomplir cela sont tous inclus avec [Gatsby Starter Blog](https://www.gatsbyjs.com/starters/gatsbyjs/gatsby-starter-blog) !

* [React Helmet](https://github.com/nfl/react-helmet) - Utilisé dans le composant `SEO` pour ajouter des balises méta au document head pour supporter les Twitter Cards et autres balises [Open Graph](https://ogp.me/)
* [Gatsby Source Filesystem](https://www.gatsbyjs.com/plugins/gatsby-source-filesystem/) - Un "plugin pour sourcer des données dans votre application Gatsby à partir de votre système de fichiers local", des images dans notre cas
* [Gatsby Image](https://www.gatsbyjs.com/plugins/gatsby-image/) - "un composant React spécialement conçu pour fonctionner de manière transparente avec les requêtes GraphQL de Gatsby. Il combine les capacités de [traitement d'image natif de Gatsby](https://image-processing.gatsbyjs.org/) avec des techniques avancées de chargement d'image pour optimiser facilement et complètement le chargement d'image pour vos sites. `gatsby-image` utilise [gatsby-plugin-sharp](https://www.gatsbyjs.com/packages/gatsby-plugin-sharp/) pour alimenter ses transformations d'image."
* [Gatsby Plugin Sharp](https://www.gatsbyjs.com/plugins/gatsby-plugin-sharp/) - "Expose plusieurs fonctions de traitement d'image construites sur la [bibliothèque de traitement d'image Sharp](https://github.com/lovell/sharp)". Nous utilisons cela pour redimensionner les images.

## Comment ajouter des balises de métadonnées de document

Tout d'abord, nous allons configurer les balises de métadonnées HTML qui peuvent être lues par Twitter et toute autre plateforme ou outil qui comprend [Open Graph](https://ogp.me/) comme Google, Facebook et WhatsApp. 

En savoir plus sur les métadonnées de document ici : [Qu'y a-t-il dans le head ? Métadonnées en HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML).

Ouvrez le composant `SEO` dans `src/components/seo.js`. La première chose à remarquer est que cela utilise [React Helmet](https://github.com/nfl/react-helmet), et il a déjà de nombreuses balises méta Open Graph et Twitter comme `og:title`, `twitter:description`. Il a même une balise `twitter:card` avec une valeur de "summary" qui active une carte résumé Twitter de base sans image :

```js
// src/components/seo.js
const SEO = ({ description, lang, meta, title }) => { 
// Détails omis pour plus de concision 
return ( 
    <Helmet 
        htmlAttributes={{ lang }} 
        title={title} 
        titleTemplate={`%s | ${site.siteMetadata.title}`} 
        meta={[ 
            { name: `description`, content: metaDescription, }, 
            { property: `og:title`, content: title, }, 
            { property: `og:description`, content: metaDescription, }, 
            { property: `og:type`, content: `website`, }, 
            { property: `twitter:card`, content: `summary`, }, 
            { property: `twitter:creator`, 
              content: site.siteMetadata.social.twitter, }, 
            // ...
```

Mettons à jour ce composant :

1. Ajoutez les paramètres `imageUrl` et `imageAlt`. Ceux-ci seront passés en tant que props par le composant `BlogPostTemplate` comme nous le verrons plus tard. Notez que j'ai utilisé "URL" dans le nom de la prop pour transmettre le fait que cela doit être une URL entièrement qualifiée. Les chemins relatifs ne sont pas supportés pour l'image OG !
2. Construisez l'URL de l'image par défaut, `defaultImageUrl`. J'ai écrit une petite fonction utilitaire, `constructUrl`, pour concaténer une URL de base avec un chemin relatif. Nous verrons d'où vient `data.ogImageDefault` dans la section suivante.
3. Ajoutez une variable `ogImageUrl` qui prend la prop `imageSrcUrl` ou, si celle-ci n'est pas fournie, utilise par défaut `defaultImageUrl`.
4. Ajoutez des objets au tableau `meta` passé au composant `Helmet` : `og:image`, `twitter:card`, et `twitter:image:alt`

Quelques points à noter ici :

1. Twitter a bien sa propre balise méta `twitter:image`, mais selon la [documentation](https://developer.twitter.com/en/docs/twitter-for-websites/cards/guides/getting-started#twitter-cards-and-open-graph), nous n'avons pas besoin d'ajouter à la fois la balise `og:image` et la balise `twitter:image` puisque l'analyseur de Twitter se rabattra sur les balises Open Graph.
2. Open Graph spécifie les attributs `meta` `property` et `content` tandis que Twitter spécifie `name` et `content`, respectivement. Mais encore une fois, la documentation de Twitter indique que leur analyseur se rabattra sur les attributs Open Graph. C'est bien car nous pouvons maintenir la cohérence et n'avons pas besoin d'une série de propriétés répétitives avec les mêmes valeurs que nous devons garder synchronisées.
3. Les exceptions notables à l'utilisation de l'attribut `property` sur les balises `meta` sont toutes les balises non-Open Graph comme `description` qui doivent utiliser l'attribut `name`. Je vous encourage à utiliser [Lighthouse](https://developers.google.com/web/tools/lighthouse) qui identifiera les problèmes de base avec votre SEO.

```js
// util.js
export const constructUrl = (baseUrl, path) =>
  (!baseUrl || !path) ? null : `${baseUrl}${path}`;

// src/components/seo.js
// Étape 1 : Ajouter des props
const SEO = ({ description, lang, meta, title, imageUrl, imageAlt }) => { 
    
    const data = useStaticQuery(
        // Cela est expliqué ensuite
    );
                                
    // Étape 2 : Construire l'URL de l'image par défaut
    // ogImageDefault est expliqué ensuite
    const defaultImageUrl = constructUrl(data.site.siteMetadata.siteUrl, data.ogImageDefault?.childImageSharp?.fixed?.src)
    
    // Étape 3 : Ajouter ceci
    const ogImageUrl = imageUrl || defaultImageUrl; 
    
    return ( 
        // Étape 4 : Ajouter de nouveaux objets meta
        <Helmet 
            htmlAttributes={{ lang }} 
            title={title} 
            titleTemplate={`%s | ${site.siteMetadata.title}`} 
            meta={[
                { property: `og:image`, content: ogImageUrl, }, 

                // Si un article a une image, utiliser la carte plus grande. 
                // Sinon, l'image par défaut est juste 
                // un petit logo, donc utiliser la carte plus petite.
                { property: `twitter:card`, content: imageUrl ? `summary_large_image` : `summary`, }, 

                // Ajouter le texte alternatif de l'image
                // Se rabattra sur le texte par défaut qui décrit le logo du site
                { property: `twitter:image:alt`, content: imageAlt || "logo davidagood.com", }, 
                // ...
```

## Comment sourcer l'image par défaut en utilisant GraphQL

C'est ici que les capacités de système de fichiers et de traitement d'image de Gatsby entrent en jeu. Ci-dessous se trouve l'appel `useStaticQuery` de la requête GraphQL du composant `SEO`. J'ai ajouté la partie `ogImageDefault` et le `siteUrl` qui est nécessaire pour l'appel `constructUrl` montré ci-dessus.

```js
// src/components/seo.js
const data = useStaticQuery(
    graphql`
      query {
        site {
          siteMetadata {
            title
            description
            social {
              twitter
            }
            # Ajouter ceci
            siteUrl
          }
        }
        # Ajouter ceci
        ogImageDefault: file(relativePath: {eq: "icon.png"}) { 
          childImageSharp {
            fixed(height: 260, width: 260) {
              src
            }
          }
        }
      }
    `,
);
```

### Requête GraphQL de fichier et de traitement d'image expliquée

Le nœud de niveau supérieur est `ogImageDefault`. Il s'agit d'un [alias GraphQL](https://graphql.org/learn/queries/#aliases) pour la requête `file` qui applique un filtre pour trouver un fichier avec un chemin relatif égal à `icon.png`. Le nom que j'ai choisi, `ogImageDefault`, est complètement arbitraire.

Une chose clé à comprendre ici est ce que le `relativePath` est relatif à. En d'autres termes, où se trouve ce fichier, `icon.png` ? 

Je vais commencer par vous dire l'emplacement du fichier par rapport à la racine du projet : `./content/assets/icon.png`. Dans la requête, je n'ai pas spécifié de chemin relatif, juste le nom du fichier. Alors, comment Gatsby sait-il où le trouver ? 

Entrez `[gatsby-source-filesystem](https://www.gatsbyjs.com/plugins/gatsby-source-filesystem/)`. Si vous regardez dans `gatsby-config.js`, vous verrez une configuration comme ceci :

```js
// gatsby-config.js 
module.exports = { 
    // siteMetadata: {...}, 
    plugins: [ 
        // Autres plugins omis 
        { 
            resolve: `gatsby-source-filesystem`, 
    	    options: { 
                path: `${__dirname}/content/blog`, 
                name: `blog`, 
            }, 
        }, 
        { 
            resolve: `gatsby-source-filesystem`, 
            options: { 
                path: `${__dirname}/content/assets`, 
                name: `assets`, 
            }, 
        }, 
    	// ...
```

Ce que cela fait, c'est enregistrer ces chemins comme des "racines de contenu" et leur donner un nom. Donc le nom `blog` fait référence à `./content/blog` par rapport à la racine du projet. Et le nom `assets` fait référence à `./content/assets` par rapport à la racine du projet. Vous pouvez utiliser ces noms dans les requêtes en filtrant sur `sourceInstanceName` :

```graphql
# http://localhost:8000/___graphql 
{ 
    allFile(filter: {sourceInstanceName: {eq: "blog"}}) { 
        edges { 
            node { 
                absolutePath 
                publicURL 
                sourceInstanceName 
            } 
        } 
    } 
}
```

Le résultat de cette requête :

```js
// Résultat de la requête allFiles avec le filtre sourceInstanceName 
{ 
    "data": { 
        "allFile": { 
            "edges": [{ 
                "node": { 
                    "absolutePath": "/home/dgood/IdeaProjects/davidagood.com/content/blog/clean-code-and-architecture/index.md", 
                    "publicURL": "/static/40bb02d938c4faf7f977dd66c1a399d2/index.md", 
                    "sourceInstanceName": "blog" 
                } 
            }, 
            // résultats supplémentaires...
```

Donc, en revenant à `ogImageDefault` : le `relativePath` que nous avons fourni était simplement `icon.png`, mais le fichier est en fait situé à `./content/assets/icon.png`. 

Gatsby a pu résoudre le fichier car nous avons configuré une "racine de contenu" à `./content/assets`. Nous aurions pu spécifier le `sourceInstanceName` pour éliminer toute ambiguïté quant à la "racine de contenu" dans laquelle ce fichier est situé. 

En fait, je ne suis pas sûr de la façon dont Gatsby se comporterait si le même chemin relatif existait dans plusieurs "racines de contenu". 

Ce serait une bonne opportunité de creuser dans le code source de Gatsby pour comprendre comment tout cela fonctionne, mais je vous laisse le faire !

Ensuite : qu'est-ce que `childImageSharp` ? "Child" fait référence au fait que ce soit un nœud enfant d'un nœud `File`. "Image" est exactement comme cela sonne. "Sharp" fait référence à l'outil de traitement d'image [Sharp](https://github.com/lovell/sharp) et au plugin Gatsby correspondant, [gatsby-plugin-sharp](https://www.gatsbyjs.com/plugins/gatsby-plugin-sharp/), qui active ces fonctionnalités de traitement d'image.

`fixed` signifie que nous voulons transformer l'image en une image de taille fixe. Nous spécifions les dimensions en passant des paramètres comme ceci : `fixed(height: 260, width: 260)`. Il existe quelques alternatives à `fixed` que nous pourrions utiliser, dont l'une que nous verrons ci-dessous.

Enfin, nous avons seulement besoin de la propriété `src` pour les besoins de la balise méta d'image Open Graph.

## Comment sourcer les propriétés d'image spécifiques aux articles en utilisant GraphQL

En suivant ce qui précède, nous devons mettre à jour le composant `BlogPostTemplate` pour passer les props `imageUrl` et `imageAlt` au composant `SEO`. Encore une fois, nous utilisons l'utilitaire `constructUrl` pour convertir le chemin relatif, `src`, en une URL. J'explique l'origine des valeurs de ces props ci-dessous.

```js
// util.js
export const constructUrl = (baseUrl, path) =>
  (!baseUrl || !path) ? null : `${baseUrl}${path}`;

// src/templates/blog-post.js
const BlogPostTemplate = ({ data, pageContext, location }) => { 
    // Détails omis pour plus de concision
    return ( 
        <Layout location={location} title={data.site.siteMetadata.title}> 
            <SEO 
                title={data.markdownRemark.frontmatter.title} 
                description={data.markdownRemark.frontmatter.description || data.markdownRemark.excerpt} 
                imageUrl={
                    constructUrl(
                        data.site.siteMetadata.siteUrl, data.markdownRemark.frontmatter.image?.childImageSharp?.fixed?.src
                )} 
                imageAlt={data.markdownRemark.frontmatter.imageAlt} />
        // ...
```

Le sourçage du texte alternatif de l'image est simple : nous ajoutons `imageAlt` comme propriété à la partie `frontmatter` de la requête GraphQL de notre composant `BlogPostTemplate`. Cette requête est exportée comme un modèle de balise GraphQL. 

Le nom de la constante exportée est arbitraire. Dans mon cas, c'est `const pageQuery`. 

Cette requête est exécutée pour nous par Gatsby, et les résultats sont passés au composant `BlogPostTemplate` dans la prop `data`. 

Cela est expliqué dans la documentation de Gatsby ici : [Interrogation de données dans les pages avec GraphQL](https://www.gatsbyjs.com/docs/how-to/querying-data/page-query/).

Afin de sourcer l'image réelle, nous utilisons à nouveau `childImageSharp` mais de manière légèrement différente de ce que nous avons vu ci-dessus :

```js
// src/templates/blog-post.js
export const pageQuery = graphql`
    query BlogPostBySlug($slug: String!) {
      site {
        siteMetadata {
          title
          siteUrl
        }
      }
      markdownRemark(fields: {slug: {eq: $slug}}) {
        id
        excerpt(pruneLength: 160)
        html
        frontmatter {
          title
          date(formatString: "MMMM DD, YYYY")
          description
          # Ajouter ceci
          image {
            childImageSharp {
              fixed(height: 600, width: 1200) {
                src
              }
              fluid(maxWidth: 700, maxHeight: 500) {
                ...GatsbyImageSharpFluid
              }
            }
          }
          # Ajouter ceci
          imageAlt
          imageTitleHtml
        }
      }
    }
`;
```

Ici, `image` doit correspondre au nom de la propriété que nous avons l'intention de définir dans le frontmatter de l'article. Et la valeur de cette propriété doit être un chemin vers un fichier **relatif au fichier markdown de l'article**. 

Cela est similaire à ce que nous avons fait ci-dessus en utilisant un alias GraphQL et la requête `file`, mais ici c'est implicite et géré en coulisses par Gatsby.

Nous spécifions les dimensions dans les paramètres du champ `fixed`. Lors du choix des dimensions, assurez-vous que toute image que vous utilisez est au moins aussi grande que les dimensions que vous spécifiez ici, et utilisez ces directives de la [documentation](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image#reference) :

> Les images pour cette carte supportent un rapport d'aspect de 2:1 avec des dimensions minimales de 300x157 ou maximales de 4096x4096 pixels

Nous avons également ajouté la propriété `fluid` et un [fragment GraphQL](https://graphql.org/learn/queries/#fragments), `...GatsbyImageSharpFluid`, qui récupère toutes les propriétés disponibles sur ce nœud sans avoir à les énumérer une par une. 

Le composant Gatsby Image est [conçu pour être utilisé de cette manière](https://www.gatsbyjs.com/docs/reference/built-in-components/gatsby-image/#images-that-stretch-across-a-fluid-container) afin de fournir une expérience d'image responsive en utilisant [les capacités d'image responsive natives de HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images).

## Comment ajouter une image d'en-tête à votre modèle de blog

Avec la requête GraphQL mise à jour et les résultats étant passés à notre composant par Gatsby, nous sommes prêts à ajouter l'import de Gatsby Image et le JSX pour l'image d'en-tête et la légende :

```js
// src/templates/blog-post.js
import Image from "gatsby-image";

// Détails omis pour plus de concision

{data.markdownRemark.frontmatter.image?.childImageSharp?.fluid &&
    <>
        <Image
            fluid={data.markdownRemark.frontmatter.image.childImageSharp.fluid}
            alt={data.markdownRemark.frontmatter.imageAlt} 
        />
        <div
            style={{
                textAlign: "center",
                fontSize: "14px",
                lineHeight: "28px",
            }}
            dangerouslySetInnerHTML={{ 
                __html: data.markdownRemark.frontmatter.imageTitleHtml 
            }} 
        />
    	<br/>
        <br/>
    </>
}
```

Si les propriétés `image` ou `imageAlt` ne sont pas définies dans le frontmatter d'un article, cela ne causera aucun problème. Ces propriétés seront simplement `null` dans la prop `data` de l'article, par exemple `data.markdownRemark.frontmatter.image` et `data.markdownRemark.frontmatter.imageAlt`. 

Pour cette raison, j'ai utilisé le [chaînage optionnel](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining) lors du passage de la prop `imageUrl` au composant `SEO` : `data.markdownRemark.frontmatter.image?.childImageSharp?.fixed?.src` et lors de l'ajout optionnel de l'arborescence des composants d'image d'en-tête : `data.markdownRemark.frontmatter.image?.childImageSharp?.fluid`.

## Comment ajouter de nouvelles propriétés au frontmatter d'un article

Il ne reste plus qu'à ajouter le fichier image réel, généralement dans le même répertoire que le markdown où nous voulons l'utiliser. Ensuite, nous ajoutons les propriétés `image`, `imageAlt` et `imageTitleHtml` au frontmatter de l'article. 

J'ai pris le HTML d'attribution suggéré directement depuis [Unsplash](https://unsplash.com/) et l'ai utilisé pour le `imageTitleHtml`.

Rappelez-vous : dans ce cas, le chemin de l'image est relatif au fichier markdown de l'article.

```md
--- 
title: "Travailler avec des collections d'éléments hétérogènes dans le client amélioré DynamoDB pour Java" 
date: "2020-12-07T01:51:34.815Z"
description: "Travailler avec des collections d'éléments hétérogènes avec les SDK Java peut être délicat. Ici, nous voyons comment les gérer avec le client amélioré de l'AWS SDK v2 pour Java."
image: "./kevin-mueller-gGUiw8GNIFE-unsplash.jpg"
imageAlt: "Gouttelettes d'eau sur fond noir"
imageTitleHtml: '<span>Photo par <a href="https://unsplash.com/@kevinmueller?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Kevin Mueller</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>'

--- 

// Markdown ici...
```

## Conclusion

C'est tout — vous l'avez fait ! Nous avons couvert plusieurs concepts dans cet article. Vous devriez maintenant être en mesure d'ajouter des images d'en-tête à vos articles de blog et d'obtenir de belles expériences de prévisualisation basées sur Open Graph sur Twitter, Facebook, Google, WhatsApp, et plus encore.

Vous pouvez trouver le code complet sur GitHub ici :

* [SEO](https://github.com/helloworldless/davidagood.com/blob/55164811e2265de754940c8432c58c2bceec8e43/src/components/seo.js)
* [BlogPostTemplate](https://github.com/helloworldless/davidagood.com/blob/55164811e2265de754940c8432c58c2bceec8e43/src/templates/blog-post.js)
* [Exemple de markdown d'article](https://github.com/helloworldless/davidagood.com/blob/55164811e2265de754940c8432c58c2bceec8e43/content/blog/dynamodb-enhanced-client-java-heterogeneous-item-collections/index.md)

Une fois que vous avez implémenté cela et l'avez déployé, vous pouvez utiliser le [Validateur de Twitter Card](https://cards-dev.twitter.com/validator) pour tester le comportement avant de tweeter un lien.

Par coïncidence, j'ai effectivement rencontré quelques problèmes avec les cartes qui n'étaient pas affichées dans les tweets même si le Validateur montrait qu'elles fonctionnaient. 

Dans un cas, j'ai tweeté un lien en réponse, et il n'y avait aucune carte du tout — juste le lien brut. Le lendemain, j'ai tweeté le même lien, et cette fois la carte fonctionnait bien ! 

Dans un autre cas, je regardais ma page de profil Twitter, et plusieurs de mes tweets avaient les cartes mais l'image n'était pas affichée. J'ai donc ouvert une fenêtre Chrome Incognito, et dans cette fenêtre, les images étaient affichées comme prévu.