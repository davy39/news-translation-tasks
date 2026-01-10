---
title: Comment écrire une bonne documentation avec Docsify
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2023-10-26T19:21:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-good-documentation-with-docsify
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/docsify.png
tags:
- name: documentation
  slug: documentation
seo_title: Comment écrire une bonne documentation avec Docsify
seo_desc: 'Documentation is critical to a successful product. Without documentation,
  it''s more difficult for people to use your product, and it''s just as important
  if you''re running an open-source project, too.

  Creating a documentation site can be challenging, ...'
---

La documentation est cruciale pour un produit réussi. Sans documentation, il est plus difficile pour les gens d'utiliser votre produit, et c'est tout aussi important si vous gérez un projet open-source.

Créer un site de documentation peut être un défi, surtout si vous n'êtes pas familier avec le développement front-end. 

Je suis développeur front-end depuis les 8 dernières années. Pendant cette période, j'ai utilisé de nombreux frameworks pour construire de la documentation, comme [Next.js](https://nextjs.org/), [nextra](https://nextra.site/), [content layer](https://contentlayer.dev/), [Ghost CMS](https://ghost.org/), [lume (deno)](https://lume.land/), [docusaurus](https://docusaurus.io/), et [Mark doc](https://markdoc.dev/).

Mais pour utiliser beaucoup de ces outils, vous devez avoir des connaissances essentielles sur JavaScript, Next.js et React. Vous pourriez rencontrer certains défis, comme :

1. Manque de connaissances en JavaScript, React ou autres outils nécessaires
2. Versioning de la documentation 
3. Configuration 
4. Déploiement

Dans ce guide, je vais vous présenter un outil puissant qui peut vous aider à écrire de la documentation sans avoir besoin de autant de connaissances techniques.

## Qu'est-ce que Docsify ?

Pour vous aider à résoudre ce problème, je recommande un outil appelé [**docsify**](https://docsify.js.org/#/). Docsify est un générateur de documentation simple et léger. Vous pouvez commencer à l'utiliser sans avoir aucune connaissance de JavaScript ou React. 

Docsify ne nécessite aucune configuration, ne génère pas de fichiers HTML statiques, supporte plusieurs thèmes, dispose d'une API de plugins intégrée et offre une recherche en texte intégral avec un plugin. Il se déploie également sur une large gamme de plateformes comme GitHub Pages, GitLab Pages, Firebase, Netlify, Vercel et autres. 

J'ai créé un projet de démonstration pour vous montrer comment l'utiliser – le [code source est disponible](https://github.com/officialrajdeepsingh/docsifyjs) sur GitHub. Vous pouvez également [consulter le site de démonstration en direct](https://officialrajdeepsingh.github.io/docsifyjs/#/).

### Comment installer et utiliser Docsify

Vous pouvez créer un nouveau projet avec [docsify-cli](https://cli.docsifyjs.org/). Pour utiliser docsify-cli, vous devez installer Node et NPM si vous ne les avez pas déjà installés. 

```bash
npm install -g docsify-cli
# ou
yarn add -g docsify-cli
# ou
pnpm add -g docsify-cli
```

La sortie de la commande ressemble à ceci :

```bash
❯ pnpm add -g docsify-cli

Packages: +198
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Progress: resolved 199, reused 114, downloaded 84, added 198, done
.pnpm/docsify@4.13.1/node_modules/docsify: Running postinstall script, done in 196ms

/home/rajdeepsingh/.local/share/pnpm/global/5:
+ docsify-cli 4.4.4
+ pnpm 8.7.0

Done in 13.9s
```

Créez votre nouveau projet avec l'option docsify-cli init.

```
❯ docsify init docs

Initialization succeeded! Please run docsify serve ./docs
```

Vous pouvez également spécifier le `--theme` et `--plugins`.

```bash
❯ docsify init docs --theme buble --plugins
```

Vous pouvez en savoir plus sur [docsify-cli](https://cli.docsifyjs.org/) sur la page de documentation.

![Installez les plugins avec l'option docsify init.](https://www.freecodecamp.org/news/content/images/2023/09/docsify-plugins.gif)
_Installez les plugins avec l'option docsify init._

Ensuite, démarrez votre serveur de développement local en utilisant docsify-cli. Pour cela, exécutez la commande suivante :

```bash
docsify serve docs
# ou
docsify serve .
```

Votre serveur local s'exécute sur le port 3000 localement.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-20-22-37-52.png)
_Exécutez docsify serve_

Votre site devrait ressembler à ceci lorsque vous l'ouvrez dans le navigateur :

![Demo docsify](https://www.freecodecamp.org/news/content/images/2023/09/docsify-demo.png)
_Demo Docsify_

## Structure de dossier de Docsify

Docsify a une structure de dossier simple. Par défaut, lorsque vous créez un nouveau projet avec [docsify-cli](https://cli.docsifyjs.org/), il y a trois fichiers principaux :

```bash
├── index.html // C'est un fichier d'entrée HTML.
├── .nojekyll  // Cela est utile lorsque vous déployez votre projet sur GitHub Pages.
└── README.md  // C'est la page d'accueil ou le routeur /

```

## Comment personnaliser Docsify

Docsify offre de nombreuses options de personnalisation, et vous n'avez pas besoin de connaissances supplémentaires pour le configurer – c'est assez simple, comme copier et coller du code. 

Dans ce guide, nous explorerons certaines des options de personnalisation les plus courantes. Pour une configuration avancée, vous pouvez consulter la documentation de Docsify.

1. [Configuration de base](#heading-configuration-de-base)
2. [Écran de chargement](#heading-ecran-de-chargement)
3. [Barre latérale](#heading-barre-laterale)
4. [En-tête](#heading-en-tete)
5. [Page de couverture](#heading-page-de-couverture)
6. [Plugins](#heading-plugins)
7. [Thèmes](#heading-themes)
8. [Déploiement](#heading-deploiement)

### Configuration de base

Dans la configuration de base, vous pouvez changer ou ajouter un logo, un nom, ajouter le lien de votre dépôt GitHub, une couleur de thème, etc.

Voici le code pour le faire – vous pouvez remplir vos propres détails.

```html
 <!-- index.html -->
 <script>
      window.$docsify = {
        logo: '/_media/icon.svg',  <!-- ajouter un logo -->
        name: "Document",  <!-- Nom du site, il apparaît dans la barre latérale. -->
        nameLink: '/',  <!-- url pour le nom -->
        repo: "officialrajdeepsingh/docsifyjs",<!-- dépôt github -->
        maxLevel: 2,  <!-- Niveau maximum de la table des matières. -->
        themeColor: '#3F51B5', <!-- Personnaliser la couleur du thème -->
      };
</script>
```

### Écran de chargement

Activer un écran de chargement ou une boîte de dialogue est généralement très compliqué, surtout si vous venez de l'écosystème JavaScript et React.js.

![Écran de chargement dans Docsify](https://www.freecodecamp.org/news/content/images/2023/10/ezgif.com-video-to-gif-2.gif)
_Écran de chargement dans Docsify_

Dans Docsify, vous pouvez [activer un écran de chargement](https://docsify.js.org/#/quickstart?id=loading-dialog) sans aucune configuration. Il vous suffit d'écrire un peu de texte avec un élément HTML à l'intérieur de votre ID d'application, qui s'affichera alors comme un écran de chargement. Cela ressemble à ceci :

```html
<!-- index.html -->
<div id="app">Veuillez patienter...</div>

<!-- ou -->

<div id="app">
<h1> Veuillez patienter... </h1>
</div>




```

### Barre latérale

Par défaut, la barre latérale affiche la table des matières. Mais vous pouvez la personnaliser très facilement. Tout d'abord, vous devez [activer la barre latérale](https://docsify.js.org/#/more-pages?id=sidebar).

```html
<!-- index.html -->
<script>
   window.$docsify = {
       
        loadSidebar: true, <!-- Activer la barre latérale -->
  
   };
</script>


```

Ensuite, créez un nouveau fichier `_sidebar.md` au niveau racine et collez le code suivant :

```_sidebar.md
- [Accueil](README.md)
- [Article brouillon](draft-article.md)
- [Guide](guide.md)
- [Premier](page-first.md)
- [Deuxième](page-second.md)
- [Troisième](page-third.md)
- [Quatrième](page-four.md)

```

Votre barre latérale devrait maintenant ressembler à ceci :

![Votre barre latérale ressemble à ceci.](https://www.freecodecamp.org/news/content/images/2023/10/customizer-sidebar.png)
_Votre barre latérale ressemble à ceci._

### En-tête

Par défaut, vous ne pourrez pas voir la barre de navigation sur votre site Docsify :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/navbar.png)
_Pas de barre de navigation_

Mais ne vous inquiétez pas, vous pouvez changer cela. Pour afficher la [barre de navigation, vous devez d'abord l'activer](https://docsify.js.org/#/custom-navbar) comme ceci :

```html
<!-- index.html -->
    <script>
      window.$docsify = {
       
        
        loadNavbar: true,     <!-- activer la barre de navigation -->
       
      };
    </script>
  </body>
</html>

```

Ensuite, créez un nouveau fichier `_navbar.md` au niveau racine et collez le code suivant :

```markdown
* Commencer

  * [Démarrage rapide](quickstart.md)
  * [Écrire plus de pages](more-pages.md)
  * [Barre de navigation personnalisée](custom-navbar.md)
  * [Page de couverture](cover.md)

* Configuration
  * [Configuration](configuration.md)
  * [Thèmes](themes.md)
  * [Utiliser des plugins](plugins.md)
  * [Configuration Markdown](markdown.md)
  * [Mise en évidence de la syntaxe](language-highlight.md)

```

Votre barre de navigation devrait maintenant ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/customizer-navbar.png)
_Personnaliser la barre de navigation dans Docsify_

### Page de couverture

Tout d'abord, [activez la page de couverture](https://docsify.js.org/#/cover) dans docsify avec le code suivant :

```html
<!-- index.html -->
<script>
      window.$docsify = {
       
        coverpage: true,     <!-- activer la page de couverture -->
        
      };
</script>

```

L'étape suivante consiste à créer un nouveau fichier `_coverpage.md`.

```markdown
# Apprendre Docsify 
### Apprendre docsify à partir du début.

[Commencer à apprendre]()
[Github](#/README)
```

Votre page de couverture devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/coverpage.png)
_Votre page de couverture_

La page de couverture et votre interface dépendent du thème, ils différeront donc d'un thème à l'autre. 

### Plugins

Les plugins aident à fournir des fonctionnalités et des caractéristiques supplémentaires à Docsify et améliorent également l'expérience utilisateur. 

Vous pouvez créer et utiliser des plugins selon vos propres exigences. **[D**ocsify**](https://github.com/docsifyjs/awesome-docsify)** dispose de nombreux plugins disponibles qui sont open-source et créés par divers contributeurs. 

Vous pouvez utiliser n'importe quel plugin en copiant-collant simplement le code. Vous pouvez même créer vos propres plugins avec docsify.

#### Comment utiliser des plugins tiers

Dans cet exemple, nous allons activer la fonctionnalité de la barre de recherche avec l'aide du plugin docsify.

Pour activer la barre de recherche, copiez et collez le script suivant à l'intérieur de votre fichier `index.html` :

```javascript
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
```

Maintenant, la barre de recherche apparaîtra et fonctionnera sur votre site. Avec le plugin de recherche, vous pouvez également configurer diverses fonctionnalités – lisez-en plus sur la [page d'installation et de configuration du plugin de recherche](https://docsify.js.org/#/plugins?id=full-text-search).

![Image](https://www.freecodecamp.org/news/content/images/2023/10/searchbar.png)
_Plugin de recherche Docsify_

#### Comment créer votre propre plugin avec docsify

Pour créer votre propre plugin dans docsify, il y a un hook intégré que vous devrez utiliser pour le plugin.

Docsify dispose de six hooks intégrés : `init`, `mounted`, `beforeEach`, `afterEach`, `doneEach`, et `ready`. 

1. `init` : est invoqué une fois lorsque le script docsify est initialisé.
2. `mounted` : est invoqué une fois lorsque l'instance docsify a été montée sur le DOM.
3. `beforeEach` : est invoqué à chaque chargement de page avant que le nouveau markdown ne soit transformé en HTML.
4. `afterEach` : est appelé à chaque chargement de page après que le markdown a été transformé en HTML.
5. `doneEach` : est invoqué à chaque chargement de page après que le nouveau HTML a été ajouté au DOM.
6. `ready` : est invoqué une fois après le rendu de la page initiale.

Avec l'aide de ces hooks, vous pouvez créer un plugin. Pour en savoir plus sur la création de vos propres plugins, consultez la [page de documentation des plugins personnalisés](https://docsify.js.org/#/write-a-plugin?id=template).

Dans cet exemple, nous allons créer un bouton d'édition en utilisant le hook de plugin beforeEach. Il affiche le bouton EDIT DOCUMENT sur chaque page.

```html
<!-- index.html -->
    <script>
      window.$docsify = {
        
        plugins: [
        
        <!-- écrire un plugin personnalisé -->
        function editButton(hook, vm) {

          // appeler le hook
          hook.beforeEach(function (html) {
           
            var url = "https://github.com/officialrajdeepsingh/docsifyjs/edit/master/" + vm.route.file;
            
              // correction de route de base 
            let tempFile = url.replace("docsifyjs/README.md", "README.md",)
              ? url.replace("docsifyjs/README.md", "README.md")
              : url;

            // Ajouter le bouton d'édition
            var editHtml = "[📝 EDIT DOCUMENT](" + url + ")\n";

            // Ajouter le bouton d'édition en haut du fichier
            return editHtml + html + "\n----\n" + "Dernière modification " + editHtml;
          });
        },
        ],
        
        
      };
    </script>
```

### Thèmes

Docsify dispose de [thèmes officiels et créés par la communauté](https://docsify.js.org/#/themes?id=themes). Vous pouvez utiliser n'importe lequel d'entre eux, et le bon côté est que vous n'avez pas besoin d'écrire de code supplémentaire lorsque vous changez de thème. 

```html
<!-- thème vue -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify/themes/vue.css" />

<!-- thème buble -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify/themes/buble.css" />

<!-- thème sombre -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify/themes/dark.css" />

<!-- thème pur -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify/themes/pure.css" />

```

Vous pouvez choisir de compresser ou non les fichiers CSS des thèmes. Le fichier CSS compressé est une version minifiée du thème, et c'est un fichier CSS léger pour la production. D'autre part, un fichier CSS de thème non compressé est utile pour le développement.

Il vous suffit de copier le thème CSS (Vue, buble, dark et pure) et de le coller à l'intérieur de l'élément head. Et avec cela, votre thème est changé.  

En termes de thèmes non officiels, je pense que le thème [docsify-themeable](https://jhildenbiddle.github.io/docsify-themeable/#/) est la meilleure option pour vous.

### Déploiement

Docsify offre diverses options de déploiement. Vous pouvez déployer votre site Docsify sur GitHub Pages, [GitLab Pages](https://docsify.js.org/#/deploy?id=gitlab-pages), [Firebase Hosting](https://docsify.js.org/#/deploy?id=firebase-hosting), [VPS](https://docsify.js.org/#/deploy?id=vps) (Nginx), [Netlify](https://docsify.js.org/#/deploy?id=netlify), [Vercel](https://docsify.js.org/#/deploy?id=vercel), [AWS Amplify](https://docsify.js.org/#/deploy?id=aws-amplify), et [Docker](https://docsify.js.org/#/deploy?id=docker).

Sur certaines plateformes comme GitHub Pages, vous déployez votre site docsify directement avec le dépôt GitHub sans écrire de configuration.

Voici le processus pour le faire :

Vous irez dans **Paramètres** > **Pages** > **Source** > puis sélectionnez Déployer à partir d'une branche > **Branche** > Sélectionnez votre branche avec le dossier et cliquez sur le bouton enregistrer.

![Déployer docsify avec GitHub Pages](https://www.freecodecamp.org/news/content/images/2023/10/github-deploy.png)
_Déployer docsify avec GitHub Pages_

Cela prendra un certain temps, selon la taille de votre site. Après la fin du déploiement, vous devriez voir votre URL de production. 

![Terminer le déploiement](https://www.freecodecamp.org/news/content/images/2023/10/deploy-github-pages.png)
_Terminer le déploiement_

## Conclusion

Docsify est un outil puissant pour générer des sites de documentation. Dans docsify, vous pouvez vous concentrer sur la rédaction de la documentation, pas sur la conception de l'interface utilisateur. 

Docsify est une bonne option pour les développeurs qui ne sont pas très familiers avec JavaScript. Si vous vous concentrez davantage sur les langages de bas niveau comme C++ ou Rust, docsify peut vous aider à commencer à rédiger votre documentation avec une seule commande.

J'ai récemment utilisé docsify pour mon dépôt [awesome-nextjs](https://github.com/officialrajdeepsingh/awesome-nextjs). Vous pouvez facilement déployer sur la page GitHub sans aucune configuration. 

Gardez simplement à l'esprit qu'il y a deux **inconvénients** à docsify :

1. Docsify ne génère pas de balises méta SEO dynamiques pour une page. Il ne génère qu'un titre et une description.
2. Le thème docsify ne fournit pas une sensation d'interface utilisateur moderne.

Mais c'est toujours très utile ! Amusez-vous à créer votre documentation :)