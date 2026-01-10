---
title: De WordPress à Hugo – Comment j'ai migré un site de 250+ pages et les scripts
  que j'ai utilisés
subtitle: ''
author: Lane Wagner
co_authors: []
series: null
date: '2022-08-30T23:25:47.000Z'
originalURL: https://freecodecamp.org/news/wordpress-to-hugo-scripts
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/1__D5sbQUd4XwTy9yt67BCCA-1.jpeg
tags:
- name: Hugo
  slug: hugo
- name: Static Site Generators
  slug: static-site-generators
- name: WordPress
  slug: wordpress
seo_title: De WordPress à Hugo – Comment j'ai migré un site de 250+ pages et les scripts
  que j'ai utilisés
seo_desc: 'I recently decided to switch Boot.dev''s blog from WordPress to a static
  site generator.

  I decided on Hugo, partly because I’m a huge fan of the Go programming language,
  but also because it just seemed like the best option from a dev-experience perspe...'
---

J'ai récemment décidé de passer le blog de [Boot.dev](https://boot.dev) de WordPress à un générateur de site statique.

J'ai choisi [Hugo](https://gohugo.io/), en partie parce que je suis un grand fan du langage de programmation Go, mais aussi parce que cela semblait être la meilleure option du point de vue de l'expérience de développement.

Voici pourquoi j'ai décidé de quitter WordPress :

* Je voulais écrire et stocker tous mes articles en Markdown.
* Je voulais versionner tous mes articles avec Git/Github.
* Je voulais pouvoir utiliser ctrl+shift+f pour trouver et modifier le contenu de mon blog.
* Je voulais une méthode moins boguée pour gérer les "blocs globaux".
* Je ne voulais pas passer des heures à affiner les performances. Mes articles ne sont que du texte et des images, donc les scores de vitesse de page devraient être de 100 par défaut !
* Je voulais utiliser du CSS pur pour le style, ce qui facilite l'identification du style de mon blog et de mon application.
* Je voulais héberger le site gratuitement.

Avec tous ces objectifs en tête, Hugo était un choix parfait. Je suis super content depuis que j'ai fait le changement, mais il y a eu quelques obstacles en cours de route.

WordPress s'occupe de certaines des nuances de l'optimisation SEO pour vous, et si vous oubliez de les refaire vous-même, vous risquez de sacrifier vos classements.

## Comment exporter les articles WordPress en Markdown

Copier et coller manuellement tous vos articles depuis l'interface graphique de WordPress dans des fichiers Markdown pourrait prendre un temps _très_ long. Surtout si vous avez des centaines d'articles comme moi.

Pour accélérer le processus, j'ai utilisé [ce plugin Markdown](https://wordpress.org/plugins/wp-gatsby-markdown-exporter/) pour exporter tous mes articles en Markdown en une seule fois. Il s'appelle "Gatsby Markdown Exporter", mais il fonctionne tout aussi bien pour Hugo.

Je ne vais pas passer en revue les bases pour commencer avec Hugo, car je suppose que vous êtes déjà familier avec lui. Mais si ce n'est pas le cas, vous pouvez lire le [guide de démarrage rapide ici](https://gohugo.io/getting-started/quick-start/).

## Comment utiliser les modèles SEO intégrés de Hugo

WordPress et ses divers plugins SEO s'occupent de beaucoup de choses liées au SEO pour vous. Donc, lorsque vous passez à un générateur de site statique, vous devez souvent faire certaines de ces choses vous-même.

Il s'avère que Hugo a des solutions clés en main pour la plupart de ces problèmes, donc l'utilisation des bons [modèles internes](https://gohugo.io/templates/internal/) peut vous fournir toutes les balises open-graph, schema et Twitter meta directement.

Pour moi, cela signifiait simplement ajouter ces 3 lignes à mon fichier `layouts/partials/header.html` dans la balise `<head>` :

```html
{{ template "_internal/opengraph.html" . }}
{{ template "_internal/twitter_cards.html" . }}
{{ template "_internal/schema.html" . }}
```

Maintenant, nous allons aborder les scripts que j'ai écrits pour m'aider dans ce processus.

## Script 1 – Vérification des liens brisés

Vous pouvez résoudre beaucoup de vos problèmes WordPress en installant des plugins pour diverses tâches. À condition que ces plugins ne cassent pas toute votre installation WP.

Avec Hugo, j'écris simplement de petits scripts de manipulation de texte ou HTTP pour faire ce que je veux.

Ce premier script est un simple itérateur qui parcourt le site et signale les liens brisés. Vous pouvez voir [le code source complet ici](https://github.com/bootdotdev/blog/blob/main/scripts/linkcheck/main.go). C'est une petite modification du script que l'équipe Go utilise pour vérifier les liens brisés sur le site web du langage de programmation Go.

## Script 2 – Minification des images

Lorsque vous travaillez avec WordPress, vous téléchargez généralement une image de blog, et un plugin SEO optimise la taille de cette image pour vous.

Avec Hugo, aucune optimisation de ce type n'est faite pour vous. Il sert simplement l'image exacte que vous ajoutez à votre dossier "static".

J'ai écrit un petit script pour optimiser mes images. Il fait ce qui suit :

* Prend une image d'entrée de presque n'importe quel type (.png, .jpeg, .gif, etc).
* La convertit au format `.webp` (un format performant).
* Réduit l'image à une taille maximale que j'ai configurée si elle est trop grande.

Ce script est écrit en Node.js et [le code source peut être trouvé ici](https://github.com/bootdotdev/blog/blob/main/scripts/image-min.js).

## Script 3 – Gestion des shortcodes globaux

WordPress avait une fonctionnalité appelée "blocs globaux". Ils sont super utiles pour des choses comme les boîtes d'inscription à la newsletter qui apparaissent au milieu de vos articles, mais que vous voulez pouvoir mettre à jour en un seul endroit.

Dans Hugo, vous pouvez utiliser des [shortcodes](https://gohugo.io/content-management/shortcodes/) pour atteindre un but similaire.

Malheureusement, c'est l'insertion et la suppression des shortcodes _eux-mêmes_ qui deviennent fastidieuses à grande échelle.

Par exemple, supposons que j'ai ajouté mon shortcode d'inscription à la newsletter après le 5ème paragraphe dans tous mes articles, mais que maintenant je veux qu'il apparaisse après le 7ème paragraphe. Je dois aller copier/coller manuellement le shortcode !

Eh bien, plus maintenant. Encore une fois, c'est l'avantage de stocker tous vos articles de blog dans un format texte – nous pouvons écrire des scripts pour des solutions simples. J'ai écrit deux scripts, et leur code source peut être trouvé ici :

* [rmshorts](https://github.com/bootdotdev/blog/blob/main/scripts/rmshorts/main.go)
* [addshorts](https://github.com/bootdotdev/blog/blob/main/scripts/addshorts/main.go)

Ces deux scripts me permettent de déplacer mes blocs globaux avec facilité. Par exemple, pour supprimer toutes les instances de `myshortcode` du blog :

```bash
rmshorts myshortcode
```

Puis pour ajouter `myshortcode` en tant que paragraphe après la 2ème section de chaque article de blog sur le site :

```bash
addshorts myshortcode 2
```

Cela m'a fait gagner beaucoup de temps.

## Script 4 – Conversion de .docx en Markdown

Enfin, je travaille avec certains rédacteurs non techniques. Mes rédacteurs ne sont pas habitués à écrire en Markdown. Google Docs est leur outil de choix.

Je n'ai aucun problème avec cela, car je veux qu'ils soient efficaces. Ma solution a été d'écrire un [petit script bash](https://github.com/bootdotdev/blog/blob/main/scripts/docxmd.sh) qui utilise [pandoc](https://pandoc.org/) pour convertir les documents Google Docs en fichiers Markdown.

## Conclusion

J'espère que certains de ces scripts vous seront utiles, et je ne peux vraiment pas recommander assez de passer à un générateur de site statique. Si vous êtes prêt à consacrer quelques heures pour mettre en place un excellent environnement de travail pour votre blog, cela vous fera gagner beaucoup de temps et d'argent à long terme.

N'oubliez pas, automatisez toujours les tâches ennuyeuses !