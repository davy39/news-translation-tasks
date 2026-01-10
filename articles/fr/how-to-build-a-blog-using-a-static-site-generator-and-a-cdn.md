---
title: Comment créer un blog en utilisant un générateur de site statique et un CDN
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-29T16:46:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-blog-using-a-static-site-generator-and-a-cdn
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c95e0740569d1a4ca0ebe.jpg
tags:
- name: Blogging
  slug: blogging
- name: 'content delivery network '
  slug: content-delivery-network
- name: Netlify
  slug: netlify
- name: Static Site Generators
  slug: static-site-generators
seo_title: Comment créer un blog en utilisant un générateur de site statique et un
  CDN
seo_desc: 'By Aaron Katz

  I wanted to set up a fun project for myself to learn some new technologies. And
  this time I decided I wanted to learn a bit about Static Site Generators (SSGs).

  My goal was to build a blog using an SSG and have it deploy any time the co...'
---

Par Aaron Katz

Je voulais mettre en place un projet amusant pour moi-même afin d'apprendre quelques nouvelles technologies. Et cette fois, j'ai décidé que je voulais en apprendre un peu plus sur les **Générateurs de Sites Statiques** (SSG).

Mon objectif était de créer un blog en utilisant un SSG et de le déployer chaque fois que le dépôt de code changeait. Vous pouvez voir le résultat sur [https://caliburnsecurity.com](https://caliburnsecurity.com).

## Exigences du blog

Voici les exigences que j'ai rassemblées pour déterminer ce que je voulais que mon blog supporte.

* Prise en charge de Markdown pour la génération de contenu
* Mise en évidence de la syntaxe
* Numérotation des lignes de code
* "Serverless"
* Thèmes/plugins prêts à l'emploi - je ne suis absolument pas un développeur frontend
* Capacités SEO
* Navigation par mot-clé/catégorie
* Prise en charge de la recherche (puisque cela est généré statiquement, la recherche se fait via l'index de Google - il existe d'autres articles qui discutent de la façon d'ajouter une recherche dynamique alimentée par JavaScript)
* Prise en charge de RSS
* Contrôle de version
* Statique - pas de contenu dynamique (avec un effet secondaire intéressant de réduire la surface d'attaque du site et d'améliorer la sécurité)

## Qu'est-ce qu'un générateur de site statique ?

En bref, un SSG est un framework conçu pour gérer votre site web et le transformer en un site servant uniquement des pages statiques.

## Pourquoi utiliser un SSG pour créer le blog ?

Une chose qui m'a pris un certain temps à comprendre était pourquoi j'utiliserais un site statique, si j'avais déjà un CMS. Il y avait tant d'articles en ligne sur l'utilisation d'un SSG avec un CMS headless... mais pourquoi ?

D'après ce que je peux dire, les avantages sont simplement que vous avez plus de flexibilité en utilisant des frameworks familiers tels que React ou Vue, tout en utilisant un CMS pour gérer tout le contenu.

Cependant, comme je ne suis en aucun cas un développeur frontend, j'ai failli abandonner ce projet. Je me suis dit "Oh bien, je devrais juste utiliser Ghost - c'est seulement 5 $/mois si hébergé sur une plateforme comme DigitalOcean, et c'est une plateforme tout-en-un pour servir le contenu ainsi que pour gérer le contenu".

Cependant, je voulais vraiment essayer d'apprendre quelque chose de nouveau, et voir si je pouvais déployer un blog gratuitement en utilisant uniquement Markdown.

Comme toujours, ce que j'espérais prendre quelques heures a pris beaucoup plus de temps alors que je plongeais dans le terrier de la recherche sur diverses technologies.

J'ai joué avec plusieurs technologies différentes, telles que (toutes ne sont pas des SSG, plus d'informations à ce sujet plus tard) :

* Pelican (Python)
* Hugo (Go)
* Hexo
* Gridsome (Vue - JS)
* VuePress (Vue - JS)
* Ghost
* Gatsby (React - JS)
* Jekyll (Ruby)

### Pourquoi j'ai choisi Hugo

Je ne vais pas entrer dans trop de détails sur toutes les technologies que j'ai examinées. Mais en général, j'ai trouvé que Hugo était super rapide à configurer et à construire, et simplement le **PLUS SIMPLE** de toutes les options.

Bien que je sache que cela ressemble à Jekyll, je ne voulais vraiment pas avoir à configurer un environnement Ruby, et la vitesse de Hugo a laissé tout le reste dans la poussière.

## Comment commencer à construire le blog

Pour cet exercice, construisons un blog statique hébergé par Netlify (gratuit !).

Note : J'utiliserai PowerShell sur ma machine Windows pour ce tutoriel, alors rappelez-vous cela si vous copiez/collez.

### Assurez-vous d'avoir ces dépendances :

* Git
* Visual Studio Code (ou votre éditeur préféré)
* Binaire Hugo

### Voici un aperçu de haut niveau de notre flux de travail :

1. Télécharger/Installer Hugo
2. Créer un projet Hugo
3. Ajouter et configurer un thème
4. Ajouter à Git
5. Déployer sur Netlify
6. (Optionnel) Configurer le CMS gratuit de Netlify

### Télécharger ou installer Hugo

Pour [installer Hugo](https://gohugo.io/getting-started/installing/), je suis allé sur leur page [GitHub Releases](https://github.com/gohugoio/hugo/releases) et j'ai téléchargé leur binaire autonome Windows x64. Je l'ai placé dans mon répertoire Projects, où nous allons créer notre site (vous pouvez toujours l'installer correctement/ajouter le binaire à votre PATH, mais je voulais quelque chose de rapide).

## Comment créer le site Hugo

Pour créer un nouveau site, exécutez simplement les commandes suivantes :

```powershell
.\hugo.exe new site hugo-blog
mv .\hugo.exe .\hugo-blog
cd .\hugo-blog
.\hugo.exe server -D --gc

```

Nous avons maintenant notre projet créé, et nous venons de démarrer le serveur Hugo. Nous avons utilisé le drapeau **-D** pour dire à Hugo d'afficher le contenu des brouillons, et j'ajoute généralement **--gc** pour m'assurer que le nettoyage est effectué à chaque fois en vidant le cache.

Vous pouvez accéder à votre site sur http://localhost:1313.

### Comprendre la structure du répertoire

Vous devriez maintenant voir la structure de répertoire suivante :

```shell
|__archetypes
|__assets *ceci n'apparaîtra pas par défaut
|__config *ceci n'apparaîtra pas par défaut
|__content
|__data
|__layouts
|__static
|__themes
|__config.toml

```

* **archetypes** : Fichiers de modèles de contenu avec des métadonnées préconfigurées. Nous ne toucherons pas vraiment à cela.
* **assets** : Stocke les fichiers traités par [Hugo Pipes](https://gohugo.io/hugo-pipes/). Cela est hors de portée pour ce tutoriel.
* **config** : Répertoire optionnel pour stocker les fichiers de configuration. Nous ne ferons rien de trop fou, donc nous utiliserons simplement le fichier de configuration config.toml par défaut.
* **content** : C'est là que vit votre contenu - vos articles et pages. Les dossiers de premier niveau dans ce répertoire sont traités comme une _section_.
* **data** : Contient les fichiers de configuration utilisés par Hugo. Je n'ai jamais eu besoin de toucher à ce répertoire.
* **layouts** : Stocke les modèles HTML partiels ou complets pour le site. Tout ce qui se trouve ici peut écraser une entrée correspondante de votre thème, vous permettant de personnaliser le thème sans modifier les fichiers réels du thème.
* **static** : Stocke tout contenu statique, tel que des images, du CSS ou des scripts. Tout dans ce dossier est copié tel quel, sans aucune modification ou interprétation par Hugo. C'est ici que vous stockerez vos médias, tels que des images, pour référence dans vos articles de blog.
* **themes** : Le répertoire où vous installerez les thèmes Hugo.
* **config.toml** : La configuration par défaut du site. Vous pouvez utiliser un répertoire séparé si vous souhaitez séparer différents environnements.

## Comment ajouter votre premier thème

Pour ce blog, nous utiliserons le thème [tale](https://github.com/EmielH/tale-hugo) pour Hugo. Exécutez les commandes suivantes à partir de la racine du projet :

```powershell
git submodule add https://github.com/EmielH/tale-hugo.git .\themes\tale

```

Nous **NE** modifierons **AUCUN** fichier du thème, mais nous apporterons toutes les modifications dans le dossier **layouts** discuté ci-dessus. Cela nous permettra de toujours mettre à jour le sous-module pour mettre à jour notre thème sans nous soucier de écraser les modifications que nous avons apportées.

Pour initialiser le thème, modifiez le fichier **config.toml** dans votre répertoire racine et ajoutez les lignes suivantes (tout en modifiant les valeurs par défaut) :

```toml
# Paramètres du thème
theme = "tale"
[params]
  Author = "Aaron Katz" # Ajoutez le nom de l'auteur (ce thème ne prend en charge qu'un seul auteur)
[author]
  name = "Caliburn Security" # Utilisé par le copyright du pied de page

```

Voilà, le thème est maintenant actif ! (Notez que dans de nombreux cas, les thèmes vous demanderont de copier et coller le fichier **theme.toml** du thème dans votre **config.toml**)

Allez-y et consultez votre page - chaque fois que vous enregistrez un fichier, Hugo reconstruit le site en direct.

### Comment modifier les fichiers du thème

Un problème avec le thème actuel est que le contenu non-article sera affiché dans la liste de la page d'accueil.

Pour changer cela, copions la page **.\themes\tale\layouts\index.html** vers **.\layouts\index.html**.

Une fois là, remplacez : `{{range (.Paginate .Site.RegularPages).Pages}}` par `{{ range where .Paginator.Pages "Section" "post" }}`. Cela garantira que seule la section "post" sera affichée dans la liste.

Je voulais également ajouter un pied de page, alors allez-y et créez un nouveau fichier à **.\layouts\footer.html** et ajoutez le code suivant :

```html
<footer>
    <span>
    &copy; <time datetime="{{ now }}">{{ now.Format "2006" }}</time> {{ .Site.Author.name }}
    </span>
</footer>
```

### Comment ajouter Google Analytics

Je voulais également ajouter Google Analytics à mon blog, et j'ai remarqué que le thème n'incorporait pas cette fonctionnalité.

Heureusement, Hugo rend l'ajout d'analytics extrêmement simple. Ouvrez le fichier **config.toml** et ajoutez la ligne suivante :

```toml
googleAnalytics = "" # Le numéro UA-XXX de Google Analytics

```

Une fois la configuration enregistrée, copiez le fichier **.\themes\tale\layouts\partial\head.html** vers **.\layouts\partial\head.html** et ajoutez le code suivant juste en dessous de la balise _head_ :

```go
{{ template "_internal/google_analytics_async.html" . }}

```

Voilà, nous avons maintenant Google Analytics qui fonctionne. Cool !

## Comment écrire du contenu

Ajoutons une belle page À propos pour que les gens sachent tout ce qu'il y a à savoir sur moi. :)

```powershell
.\hugo.exe new about.md

```

Pour vous assurer que cette page est ajoutée au menu principal, ajoutez la ligne suivante aux métadonnées de la page : `menu: main`.

_Note : Pour construire Hugo, ce qui générera le contenu dans le dossier **.\public**, exécutez simplement `.\hugo.exe`_

### Qu'est-ce que le front matter ?

C'était un nouveau terme pour moi. Essentiellement, le front matter est simplement des métadonnées structurées pour votre contenu.

Par défaut, votre modèle ajoutera les champs de métadonnées suivants à chaque page ou article que vous créez :

* title
* date
* draft

D'autres éléments de front matter potentiellement utiles sont :

* description - Cela vous permet d'entrer une description pour le contenu.
* expiryDate - Définissez une date et une heure pour lorsque le contenu ne doit plus être publié.
* keywords - Les mots-clés méta pour le contenu.
* lastmod - La date et l'heure de la dernière modification du contenu (si vous utilisez la commande de configuration enableGitInfo, cela sera automatiquement défini comme la dernière fois que le fichier a été modifié dans Git)
* markup - Lorsque défini sur "rst", vous pouvez utiliser reStructuredText au lieu de Markdown (cette fonctionnalité est expérimentale)
* publishDate - Définissez une date dans le futur pour que le contenu soit affiché.
* slug - La fin de l'URL de sortie. Par défaut, le nom du fichier si non spécifié.
* summary - Le texte utilisé lors de la fourniture d'un résumé de l'article. Je trouve cela utile si je ne veux pas que le premier paragraphe apparaisse dans le résumé, ce qui est le défaut typique.
* <taxonomies> - Utilisez la forme plurielle de l'index de taxonomie, telle que _tags_ ou _categories_.

#### Comment créer un archétype pour les articles de blog

Allons-y et changeons le front matter par défaut que nous voyons pour les articles de blog. Dans le dossier archetypes, créez un nouveau fichier appelé **posts.md** et ajoutez ce qui suit :

```yaml
---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true

slug: {{ .File.BaseFileName }} # Prendra le nom du fichier comme slug. N'hésitez pas à changer cela pour un format que vous préférez. J'aime inclure cela, afin de me rappeler que j'ai l'option de changer si je veux.

summary: "" # Supprimez cela si vous voulez que Hugo utilise simplement les 70 premiers caractères (configurables) de l'article comme résumé.
description: ""

# Listes
keywords:
tags:
categories:
---

```

Maintenant, faisons une dernière construction avec `.\hugo.exe` et préparons-nous à configurer notre dépôt Git.

## Comment configurer Git

Il est temps de configurer le projet pour Git :

```powershell
git init
git remote add origin <VOTRE URL GIT>
git push -u origin master

```

Super, nous avons maintenant notre code stocké dans notre dépôt, et nous sommes prêts pour le déploiement !

## Comment déployer votre blog

Maintenant que nous avons notre site stocké dans Git, il est temps de déployer ! Presque terminé - je vais maintenant montrer comment déployer sur Netlify en moins de 10 minutes.

Tout d'abord, nous devons créer l'application Netlify (n'hésitez pas à créer un compte en utilisant n'importe quelle méthode disponible) :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-192.png)

Ensuite, nous devons créer le site et lui indiquer où se trouve notre dépôt Git pour notre contenu Hugo :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-193.png)
_Indiquez à Netlify où se trouve votre site_

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-194.png)
_Sélectionnez le dépôt_

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-195.png)
_Ces paramètres peuvent être laissés par défaut_

Ensuite, nous allons configurer un domaine personnalisé pour notre site :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-196.png)
_Sélectionnez l'option de domaine personnalisé_

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-197.png)
_Entrez votre domaine personnalisé_

Vous devriez maintenant voir votre domaine avec un message vous demandant de **vérifier la configuration DNS**. Cliquez dessus, et entrez les informations d'enregistrement DNS fournies dans le service de gestion de vos enregistrements DNS :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-198.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-200.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-201.png)
_Exemple de configuration dans mon compte Cloudflare_

Une fois terminé, attendez quelques minutes pour que les paramètres DNS se propagent, puis sélectionnez **Vérifier la configuration DNS** :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-202.png)

Et voilà, votre site est maintenant en ligne !

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-203.png)
_Exemple de mon nouveau blog hébergé sur Netlify !_

Enfin, nous devrions configurer SSL pour notre site comme bonne pratique. Netlify offre l'option d'utiliser [Let's Encrypt](http://letsencrypt.org/howitworks/) pour provisionner automatiquement un certificat pour votre application. Pour ce faire, sélectionnez simplement **Provisionner le certificat** :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-204.png)

_Note : Il peut falloir un certain temps pour que le certificat soit généré, alors soyez patient._

### Paramètres de déploiement de Netlify

Nous avons une dernière étape avant d'être vraiment prêts à utiliser Netlify. Malheureusement, la version de Hugo utilisée par Netlify est quelque peu obsolète par défaut. Cependant, nous pouvons corriger cela en créant notre propre configuration pour que Netlify suive lors du déploiement de notre site.

Tout d'abord, créez un fichier appelé `netlify.toml` à la racine de votre dépôt, puis ajoutez la configuration suivante :

```toml
[build]
publish = "public"
command = "hugo --gc --minify"

[context.production.environment]
HUGO_VERSION = "0.74.3"
HUGO_ENV = "production"
HUGO_ENABLEGITINFO = "true"

[context.split1]
command = "hugo --gc --minify --enableGitInfo"

[context.split1.environment]
HUGO_VERSION = "0.74.3"
HUGO_ENV = "production"

[context.deploy-preview]
command = "hugo --gc --minify --buildFuture -b $DEPLOY_PRIME_URL"

[context.deploy-preview.environment]
HUGO_VERSION = "0.74.3"

[context.branch-deploy]
command = "hugo --gc --minify -b $DEPLOY_PRIME_URL"

[context.branch-deploy.environment]
HUGO_VERSION = "0.74.3"

[context.next.environment]
HUGO_ENABLEGITINFO = "true"
```

Il ne reste plus qu'à sélectionner **Déployer le site** dans la console Netlify, et votre site est maintenant en ligne sur un domaine personnalisé avec SSL !

## Conclusion

Ouf ! C'était un long article de blog, mais j'espère que cela montre à quel point il est rapide de se lancer avec un blog "serverless". Voyons ce que j'ai appris :)

### Ce que j'ai aimé

* Super simple à construire, il suffit d'exécuter `hugo serve`
* Rechargement en direct - faites une modification, enregistrez, et la page se rechargera
* Juste simple en général - je n'ai pas eu besoin de gérer grunt, gulp, webpack, ou autres
* Les formats de sortie personnalisables vous permettent de générer votre site statique, ainsi qu'un site Google AMP, des fichiers JSON, et ainsi de suite.
* RAPIDE. Ai-je mentionné rapide ?
* Peut être déployé presque n'importe où - que ce soit en utilisant Netlify (mon choix actuel), Amazon S3 & Cloudfront, Heroku, GitHub Pages, et plus encore.
* Les shortcodes sont disponibles si Markdown ne suffit pas
* Déploiement continu - tout est contrôlé par version, et déployé lorsque je publie sur la branche master
* Permet les commentaires et le partage des articles

### Défis

* Hugo est parfois trop simple. Aucun plugin ou extension du tout, etc.
* Utiliser Go est moins intuitif et les shortcodes semblent plus désordonnés que quelque chose comme Vue
* Pas trop de thèmes disponibles, mais je m'attends à ce que la bibliothèque continue de croître, car il y a une base d'utilisateurs très active

### Ai-je besoin d'un CMS ?

Après tout cela, cette question me trottait toujours dans la tête. Et la réponse est, "ça dépend".

Si j'incorporais beaucoup de médias, comme des images ou des vidéos que je dois télécharger, cela deviendrait certainement fastidieux de les ajouter et de les organiser tous dans le dossier images dans **static**.

À ce stade, je chercherais un CMS headless comme Ghost, Netlify, ou Sanity pour gérer le contenu, tant que je pourrais toujours écrire mes articles en utilisant Markdown.

### Références

* https://medium.com/backticks-tildes/hugo101-getting-started-with-hugo-and-deploying-to-netlify-9a813fe23b94
* https://blog.risingstack.com/static-site-generator-hugo-netlify/
* http://cloudywithachanceofdevops.com/posts/2018/05/17/setting-up-google-analytics-on-hugo/
* https://www.sitepoint.com/premium/books/a-beginner-s-guide-to-creating-a-static-website-with-hugo/read/1