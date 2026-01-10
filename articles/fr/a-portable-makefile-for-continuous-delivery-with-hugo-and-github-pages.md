---
title: Un Makefile portable pour la livraison continue avec Hugo et GitHub Pages
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-10-21T17:09:00.000Z'
originalURL: https://freecodecamp.org/news/a-portable-makefile-for-continuous-delivery-with-hugo-and-github-pages
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/cover-1.png
tags:
- name: continuous delivery
  slug: continuous-delivery
- name: Continuous Integration
  slug: continuous-integration
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: website development,
  slug: website-development
seo_title: Un Makefile portable pour la livraison continue avec Hugo et GitHub Pages
seo_desc: 'Fun fact: I first launched my GitHub Pages site 1,018 days ago.

  Since then, we’ve grown together. From early cringe-worthy commit messages, through
  eighty-six versions of Hugo, and up until last week, a less-than-streamlined multi-app
  continuous inte...'
---

![Image](https://www.freecodecamp.org/news/content/images/2019/10/cover.png)

Fait amusant : J'ai lancé [mon site GitHub Pages](https://victoria.dev) il y a 1 018 jours.

Depuis, nous avons grandi ensemble. Des premiers messages de commit embarrassants, à travers quatre-vingt-six versions de [Hugo](https://gohugo.io/), et jusqu'à la semaine dernière, un workflow d'intégration et de déploiement continu (CI/CD) multi-applications moins que rationalisé.

Si vous me connaissez un peu, vous savez que j'adore automatiser les choses. J'ai utilisé une combinaison d'AWS Lambda, Netlify et Travis CI pour construire et publier automatiquement ce site. Mon workflow pour cette tâche inclut :

* Construire avec [Hugo](https://gohugo.io/) lors d'un push vers master, et selon un calendrier (Netlify et Lambda) ;
* Optimiser et redimensionner les images (Netlify) ;
* Tester avec [HTMLProofer](https://github.com/gjtorikian/html-proofer) (Travis CI) ; et
* Déployer vers mon [dépôt GitHub Pages public et séparé](https://victoria.dev/blog/two-ways-to-deploy-a-public-github-pages-site-from-a-private-hugo-repository/) (Netlify).

Grâce à l'introduction de GitHub Actions, je peux faire tout ce qui précède avec un seul Makefile portable.

La semaine prochaine, je couvrirai ma configuration Actions ; aujourd'hui, je vais vous guider à travers les détails de mon Makefile afin que vous puissiez écrire le vôtre.

## Portabilité du Makefile

[Make standard POSIX](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/make.html) fonctionne sur tous les systèmes de type Unix. Les [dérivés de Make](https://en.wikipedia.org/wiki/Make_(software)#Derivatives), tels que [GNU Make](https://www.gnu.org/software/make/) et plusieurs versions de BSD Make, fonctionnent également sur des systèmes de type Unix, bien que leur utilisation particulière nécessite l'installation du programme respectif. Pour écrire un Makefile vraiment portable, le mien suit la norme POSIX. (Pour un résumé plus complet des Makefiles compatibles POSIX, j'ai trouvé cet article utile : [A Tutorial on Portable Makefiles](https://nullprogram.com/blog/2017/08/20/).) J'utilise Ubuntu, donc j'ai testé l'aspect portabilité en utilisant les programmes BSD Make `bmake`, `pmake` et `fmake`. La compatibilité avec les systèmes non de type Unix est un peu plus compliquée, car les commandes shell diffèrent. Avec des dérivés comme Nmake, il est préférable d'écrire un Makefile séparé avec des commandes Windows appropriées.

Bien que beaucoup de mon cas d'utilisation particulier pourrait être réalisé avec des scripts shell, je trouve que Make offre certains avantages intéressants. J'apprécie la facilité d'utilisation des variables et des [macros](https://en.wikipedia.org/wiki/Make_(software)#Macros), ainsi que la modularité des [règles](https://en.wikipedia.org/wiki/Makefile#Rules) lorsqu'il s'agit d'organiser mes étapes.

L'écriture des règles se résume principalement à des commandes shell, ce qui est la raison principale pour laquelle les Makefiles sont aussi portables. Le meilleur aspect est que vous pouvez faire presque n'importe quoi dans un terminal, et certainement gérer toutes les étapes du workflow listées ci-dessus.

## Mon Makefile de déploiement continu

Voici le Makefile portable qui gère mon workflow. Oui, j'ai mis des emojis dedans. Je suis un monstre.

```makefile
.POSIX:
DESTDIR=public
HUGO_VERSION=0.58.3

OPTIMIZE = find $(DESTDIR) -not -path "*/static/*" \( -name '*.png' -o -name '*.jpg' -o -name '*.jpeg' \) -print0 | \
xargs -0 -P8 -n2 mogrify -strip -thumbnail '1000>'

.PHONY: all
all: get_repository clean get build test deploy

.PHONY: get_repository
get_repository:
	@echo "? Récupération du dépôt Pages"
	git clone https://github.com/victoriadrake/victoriadrake.github.io.git $(DESTDIR)

.PHONY: clean
clean:
	@echo "? Nettoyage de l'ancienne build"
	cd $(DESTDIR) && rm -rf *

.PHONY: get
get:
	@echo "\u2753 Vérification de la présence de hugo"
	@if ! [ -x "$$(command -v hugo)" ]; then\
		echo "? Récupération de Hugo";\
	    wget -q -P tmp/ https://github.com/gohugoio/hugo/releases/download/v$(HUGO_VERSION)/hugo_extended_$(HUGO_VERSION)_Linux-64bit.tar.gz;\
		tar xf tmp/hugo_extended_$(HUGO_VERSION)_Linux-64bit.tar.gz -C tmp/;\
		sudo mv -f tmp/hugo /usr/bin/;\
		rm -rf tmp/;\
		hugo version;\
	fi

.PHONY: build
build:
	@echo "? Génération du site"
	hugo --gc --minify -d $(DESTDIR)

	@echo "? Optimisation des images"
	$(OPTIMIZE)

.PHONY: test
test:
	@echo "? Test du HTML"
	docker run -v $(GITHUB_WORKSPACE)/$(DESTDIR)/:/mnt 18fgsa/html-proofer mnt --disable-external

.PHONY: deploy
deploy:
	@echo "? Préparation du commit"
	@cd $(DESTDIR) \
	&& git config user.email "hello@victoria.dev" \
	&& git config user.name "Victoria via GitHub Actions" \
	&& git add . \
	&& git status \
	&& git commit -m "? Le bot CD aide" \
	&& git push -f -q https://$(TOKEN)@github.com/victoriadrake/victoriadrake.github.io.git master
	@echo "? Le site est déployé !"

```

Séquentiellement, ce workflow :

1. Clone le dépôt Pages public ;
2. Nettoie (supprime) les fichiers de build précédents ;
3. Télécharge et installe la version spécifiée de Hugo, si Hugo n'est pas déjà présent ;
4. Construit le site ;
5. Optimise les images ;
6. Teste le site construit avec HTMLProofer, et
7. Prépare un nouveau commit et pousse vers le dépôt Pages public.

Si vous êtes familier avec la ligne de commande, la plupart de cela peut vous sembler familier. Voici quelques éléments qui pourraient nécessiter une petite explication.

### Vérifier si un programme est déjà installé

Je pense que ce morceau est assez propre :

```sh
if ! [ -x "$$(command -v hugo)" ]; then\
...
fi
```

J'utilise une conditionnelle `if` négative en conjonction avec `command -v` pour vérifier si un exécutable (`-x`) appelé `hugo` existe. Si ce n'est pas le cas, le script récupère la version spécifiée de Hugo et l'installe. [Cette réponse Stack Overflow](https://stackoverflow.com/a/677212) offre un bon résumé de pourquoi `command -v` est un choix plus portable que `which`.

### Optimisation des images

Mon Makefile utilise `mogrify` pour redimensionner et compresser par lots les images dans certains dossiers. Il les trouve automatiquement en utilisant l'extension de fichier, et ne modifie que les images qui sont plus grandes que la taille cible de 1000px dans n'importe quelle dimension. J'ai écrit plus sur [la commande one-liner de traitement par lots dans cet article](https://victoria.dev/blog/how-to-quickly-batch-resize-compress-and-convert-images-with-a-bash-one-liner/).

Il existe plusieurs façons différentes d'accomplir cette même tâche, l'une d'entre elles, théoriquement, étant de tirer parti des [règles de suffixe](https://en.wikipedia.org/wiki/Make_(software)#Suffix_rules) de Make pour exécuter des commandes uniquement sur les fichiers image. Je trouve le script shell plus lisible.

### Utilisation de HTMLProofer Dockerisé

HTMLProofer est installé avec `gem`, et utilise Ruby et [Nokogiri](https://nokogiri.org/tutorials/ensuring_well_formed_markup.html), ce qui ajoute beaucoup de temps d'installation pour un workflow CI. Heureusement, [18F](https://github.com/18F) a une [version Dockerisée](https://github.com/18F/html-proofer-docker) qui est beaucoup plus rapide à implémenter. Son utilisation nécessite de démarrer le conteneur avec le répertoire du site construit [monté comme un volume de données](https://docs.docker.com/storage/volumes/#start-a-container-with-a-volume), ce qui est facilement réalisé en ajoutant à la commande `docker run`.

```sh
docker run -v /absolute/path/to/site/:/mounted-site 18fgsa/html-proofer /mounted-site
```

Dans mon Makefile, je spécifie le chemin absolu du site en utilisant la [variable d'environnement par défaut](https://help.github.com/en/articles/virtual-environments-for-github-actions#environment-variables) `GITHUB_WORKSPACE`. J'approfondirai cela et d'autres fonctionnalités de GitHub Actions dans le prochain article.

En attendant, bon Make !