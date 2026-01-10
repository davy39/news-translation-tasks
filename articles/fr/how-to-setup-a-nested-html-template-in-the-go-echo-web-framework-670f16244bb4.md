---
title: Comment configurer un modèle HTML imbriqué dans le framework web Go Echo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T23:01:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-a-nested-html-template-in-the-go-echo-web-framework-670f16244bb4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i1ZfgPCFQ95TeWWMiLa8wA.png
tags:
- name: পিএইচপি ভেরিয়েবল Echo এবং প্রিন্ট স্ট্যাটমেন্ট
  slug: echo
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment configurer un modèle HTML imbriqué dans le framework web Go Echo
seo_desc: 'By Ying Kit Yuen

  Echo is a lightweight but complete web framework in Go for building RESTful APIs.
  It is fast and includes a bunch of middleware for handling the whole HTTP request-response
  cycle. For the rendering part, it works with any template en...'
---

Par Ying Kit Yuen

[Echo](https://echo.labstack.com/) est un framework web léger mais complet en [Go](https://golang.org/) pour construire des APIs RESTful. Il est rapide et inclut un ensemble de middlewares pour gérer le cycle complet des requêtes-réponses HTTP. Pour la partie rendu, il fonctionne avec n'importe quel moteur de template, mais j'utilise le package standard [html/template](https://godoc.org/html/template) pour des raisons de simplicité. À la fin de cet article, nous aurons un projet [Echo](https://echo.labstack.com/) avec un modèle imbriqué configuré.

Si vous avez déjà une idée de comment [Echo](https://echo.labstack.com/) fonctionne, passez à la section [Utilisation d'un modèle imbriqué](#utilisation-d-un-modele-imbrique).

### Configuration de base d'un projet Echo

#### Créer le dossier du projet sous le bon $GOPATH

Le code complet du projet est hébergé sur [Gitlab](https://gitlab.com/ykyuen/golang-echo-template-example). Commençons par créer le dossier du projet ici : _$GOPATH/src/gitlab.com/ykyuen/golang-echo-template-example_.

#### Créer le fichier main.go

Dans le dossier nouvellement créé, copions simplement l'exemple "Hello World" du site officiel d'[Echo](https://echo.labstack.com/) et créons le fichier _main.go_.

**main.go**

#### Télécharger le package Echo en utilisant dep

Exécutez simplement **dep init** si [dep](https://github.com/golang/dep) est installé. Vous pouvez vous référer à cet article pour plus d'informations sur dep : [Gérer les dépendances Go avec dep](https://blog.boatswain.io/post/manage-go-dependencies-using-dep/).

Ou exécutez **go get github.com/labstack/echo** pour télécharger le package [Echo](https://echo.labstack.com/) dans _$GOPATH_.

#### Exécuter le hello world

Démarrez l'application en tapant **go run main.go**, puis visitez [http://localhost:1323](http://localhost:1323) via le navigateur ou la commande **curl**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aExSnI6KPWva_VRT2-2wGg.jpeg)
_Démarrer le serveur Echo._

![Image](https://cdn-media-1.freecodecamp.org/images/1*j-u3NXp7_u7PTVUiYVGwFA.jpeg)
_Envoyer une requête et obtenir le hello world._

### Retourner une réponse JSON

Lors de la construction d'une API RESTful, il est plus probable que le client souhaite recevoir une réponse JSON au lieu d'une chaîne de caractères. Écrivons un peu de code [Go](https://golang.org/) dans _main.go_.

**main.go**

### Retourner un HTML

De manière similaire au retour d'un objet JSON, nous devons simplement appeler une autre méthode dans l'instruction **return**.

**main.go**

Les exemples ci-dessus sont simplement deux exemples basiques. [Echo](https://echo.labstack.com/) propose quelques autres méthodes pratiques pour retourner du JSON et du HTML. Pour plus de détails, veuillez consulter la [documentation](https://echo.labstack.com/guide/response).

#### Rendre du HTML en utilisant un moteur de template

Comme mentionné au tout début, nous pourrions implémenter un moteur de template lors du retour de la réponse HTTP. Mais avant cela, restructurons le projet comme suit :

**main.go**

Dans ce fichier _main.go_, nous définissons un type appelé **TemplateRegistry** et implémentons l'interface **Renderer**. Un **Renderer** est une interface simple qui encapsule la fonction **Render()**. Dans une instance de **TemplateRegistry**, il y a un champ **templates** contenant tous les templates nécessaires pour que le serveur [Echo](https://echo.labstack.com/) rende la réponse HTML, et cela est configuré dans le flux **main()**.

D'autre part, nous définissons le **HomeHandler** afin de garder la logique dans un fichier séparé.

**handler/home_handler.go**

Lorsque **c.Render()** est invoqué, il exécute le template qui est déjà défini dans notre instance **TemplateRegistry** comme indiqué dans **main.go**. Les trois paramètres sont :

1. Le code de réponse HTTP
2. Le nom du template
3. L'objet de données qui peut être utilisé dans le template

**view/home.html**

Ce template ci-dessus est nommé **home.html** comme indiqué dans l'instruction **define**. Il peut lire les chaînes **name** et **msg** de **c.Render()** pour les balises **<title>** et **<h1>**.

#### Utilisation d'un modèle imbriqué

Dans la configuration ci-dessus, chaque modèle HTML contient un ensemble complet de code HTML et beaucoup d'entre eux sont dupliqués. L'utilisation de modèles imbriqués facilite la maintenance du projet.

À l'origine, le champ **templates** dans **TemplateRegistry** contenait tous les fichiers de modèles. Dans la nouvelle configuration, nous l'avons transformé en un tableau et chaque élément du tableau est un ensemble de fichiers de modèles pour une page HTML particulière.

Nous ajoutons quelques fichiers au projet et il devrait ressembler à ceci :

Le code ci-dessous est basé sur ce [gist](https://gist.github.com/rand99/808e6e9702c00ce64803d94abff65678) créé par [rand99](https://gist.github.com/rand99).

**main.go**

Nous ajoutons une nouvelle route **/about** qui est gérée par un **AboutHandler**. Comme vous pouvez le voir dans les lignes [34-36](https://gist.github.com/ykyuen/a8bcf35a338f398ddfe61275ac91e439#file-main-go-L34-L36), le tableau **templates** contient différents ensembles de fichiers de modèles pour différentes pages HTML. La fonction **Render()** prend le paramètre **name** comme clé du tableau **templates** afin qu'elle puisse exécuter le bon ensemble de modèles.

**view/base.html**

L'instruction **template** indique au moteur de template qu'il doit rechercher les définitions **{{title}}** et **{{body}}** dans l'ensemble de modèles, et elles sont définies dans **home.html** ainsi que dans **about.html**.

**view/about.html**

Et voici le **AboutHandler** qui n'a pas de grande différence avec le **HomeHandler**.

**handler/about_handler.go**

### Résumé

Ce n'est qu'un exemple de base implémentant des modèles imbriqués en utilisant la bibliothèque standard [Go](https://golang.org/) [html/template](https://godoc.org/html/template) dans [Echo](https://echo.labstack.com/). Avec une configuration appropriée, nous pourrions développer un modèle plus personnalisé et pratique pour [Echo](https://echo.labstack.com/) ou même le faire fonctionner avec d'autres moteurs de template.

L'exemple complet peut être trouvé sur [gitlab.com](https://gitlab.com/ykyuen/golang-echo-template-example).

— Article original publié sur [Boatswain Blog](https://blog.boatswain.io/post/setup-nested-html-template-in-go-echo-web-framework/).