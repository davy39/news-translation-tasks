---
title: Comment écrire un raccourcisseur de liens ultra-rapide avec Elixir, Phoenix
  et Mnesia
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T21:49:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-super-fast-link-shortener-with-elixir-phoenix-and-mnesia-70ffa1564b3c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_5mxMoPtToWHgTEyslbYnA.png
tags:
- name: Elixir
  slug: elixir
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment écrire un raccourcisseur de liens ultra-rapide avec Elixir, Phoenix
  et Mnesia
seo_desc: 'By Ben Church

  Let''s start this month’s tutorial with two statements that are going to get me
  in trouble:


  Elixir is the most productive language out there.

  Bit.ly charges way much for their paid plan


  Elixir, the Phoenix framework, and the Erlang VM ...'
---

Par Ben Church

Commençons ce tutoriel du mois avec deux affirmations qui vont me causer des ennuis :

1. Elixir est le langage le plus productif qui existe.
2. Bit.ly facture beaucoup trop pour son plan payant.

Elixir, le framework Phoenix et la machine virtuelle Erlang nous permettent de créer des systèmes prêts pour la production rapidement, facilement et avec très peu de pièces mobiles. À ce stade, vous pouvez voir où nous allons avec cela. Utilisons ce qui est fourni avec Elixir pour créer un raccourcisseur de liens et éviter une facture mensuelle de 500 $.

Plongeons-nous dans le sujet !

### Installation initiale

#### Avant de commencer

Veuillez vous assurer d'avoir les éléments suivants :

1. [Elixir](https://elixir-lang.org/install.html)
2. [Phoenix](https://hexdocs.pm/phoenix/installation.html)

#### Créer un nouveau projet Phoenix

La première chose à faire, comme toujours, est de faire créer par Phoenix le squelette du projet. Pour cette démonstration, nous n'aurons pas de "frontend", nous pouvons donc dire à l'initialiseur de les omettre.

Dans votre terminal, tapez :

```
mix phx.new shorten_api --no-html --no-brunch
```

#### Mettre à jour vos dépendances

Ensuite, nous allons ajouter quelques dépendances à `mix.exs`. Allez-y et mettez à jour la fonction `deps/0` dans ce fichier pour qu'elle ressemble à ceci :

### Logique !

D'accord, la configuration de base est terminée. Cela signifie que nous passons à la configuration de la logique qui permettra de :

1. Enregistrer des URLs
2. Référencer ces URLs par un HashId unique (ex. `abc123`)
3. Naviguer vers `/abc123` et être redirigé vers l'URL qu'il référence

Commençons par créer un moyen de stocker ces liens.

#### Créer un moyen de stocker ces liens

Utilisons les générateurs intégrés de Phoenix pour le faire. Dans votre terminal, exécutez :

`mix phx.gen.json Links Link links hash:string:unique url:string:unique`

Cela créera :

1. Le contexte `Links`
2. Le modèle `Link`
3. Le contrôleur `Link`
4. La migration de la base de données

C'est honnêtement la fin de cette étape. Il vous demandera de mettre quelques lignes dans votre fichier `router.ex`, mais pour l'instant, vous pouvez sauter cela si vous le souhaitez, car nous y reviendrons plus tard. Passons à la manière dont nous pouvons modifier ce qui a été créé ci-dessus pour générer automatiquement les identifiants que nous utiliserons pour référencer ces liens.

#### Générer automatiquement le HashId lors de la création du lien

Par défaut dans ces systèmes, les modèles reçoivent une colonne `id` dans la base de données qui est un nombre, unique et auto-incrémenté : 1, 2, 3 et ainsi de suite. Dans notre système, nous voulons que l'`id` soit :

1. Court
2. Unique
3. Une chaîne de caractères
4. Qui s'auto-génère.

_Ecto rend cela vraiment facile._

La première chose à faire est de créer un type Ecto personnalisé qui gérera tout cela pour nous. Créez un nouveau fichier `shorten_api/ecto/hash_id.ex` et remplissez-le comme suit :

Ce que nous avons fait ci-dessus est essentiellement de créer un nouveau type qui peut être utilisé de la même manière que nous définissons un champ comme un `String` ou un `Integer`. Maintenant, nous pouvons définir un champ comme un `HashId`.

> _Vous pouvez en apprendre plus sur cela dans la [documentation d'Ecto](https://hexdocs.pm/ecto/Ecto.Type.html)._

Alors faisons cela et mettons à jour `shorten_api/links/link.ex` pour utiliser un `HashId` comme clé primaire au lieu d'un `Integer` :

#### Mettre à jour la migration

Maintenant que le `HashId` est configuré dans notre code, nous voulons mettre à jour la migration pour configurer la base de données afin de refléter ce qui se passe dans notre fichier de modèle. Vous devriez avoir un fichier dans votre projet qui se termine par `_create_links.exs`. Trouvez-le, ouvrez-le et modifiez-le pour qu'il ressemble au code ci-dessous :

D'accord, c'est la majorité de nos étapes de configuration, maintenant nous allons passer à la logique principale de ce projet.

#### Rediriger d'un identifiant vers une URL

Tout d'abord, nous avons besoin d'une fonction dans notre contrôleur qui :

1. Prend un `Id` d'un `Link`
2. Recherche le `Link`
3. Redirige vers l'`URL` attachée à ce `Link`

Pour ce faire, ajoutons une nouvelle fonction à notre contrôleur de lien trouvé ici : `shorten_api_web/controllers/link_controller.ex`

#### Tout connecter à notre routeur

Maintenant que nous avons cette nouvelle fonction de contrôleur, la seule chose restante est de tout connecter. Mettez à jour le fichier `router.ex` pour refléter ce qui suit :

> Remarque : nous ajouterons également les routes suggérées par `mix phx.gen` précédemment

### TADA ! ?

À ce stade, vous devriez pouvoir exécuter le projet avec `mix phx.server` et tout devrait fonctionner comme prévu ! Cependant, nous ne nous arrêtons pas là.

### La sauce secrète

Parce que les raccourcisseurs de liens se situent entre un utilisateur et le contenu réel, il est crucial que ces systèmes soient rapides. Bien qu'Elixir soit déjà rapide, le principal temps de latence dans ce processus provient de notre base de données. Il faut du temps pour rechercher le lien attaché à un identifiant.

Pour accélérer cela, les raccourcisseurs de liens optent souvent pour utiliser un magasin de données en mémoire comme Redis plutôt qu'une base de données sur disque comme Postgres (que Phoenix configure par défaut). **Heureusement, parce qu'Elixir est construit sur la machine virtuelle Erlang, nous avons déjà un magasin de données en mémoire intégré : Mnesia !**

Dans la section suivante, nous allons modifier notre configuration pour utiliser Mnesia au lieu de Postgres.

#### Passer de Postgres à Mnesia

Ce processus est en fait très simple. Tout d'abord, mettez à jour `config.exs` comme indiqué :

#### Créer votre base de données Mnesia

Ensuite, créez l'emplacement où Mnesia sauvegardera les données et initialisez la base de données via Ecto :

```
mkdir priv/data
mkdir priv/data/mnesia
mix ecto.create
mix ecto.migrate
```

**Boom, c'est fait !** Vous utilisez maintenant une base de données en mémoire pour stocker les informations de nos liens. N'était-ce pas facile ?

### Démarrer

Vous pouvez maintenant :

1. démarrer le projet (à nouveau pour beaucoup d'entre vous) :

`mix phx.server`

2. Créer un lien raccourci via `curl` :

```
curl --request POST \  --url http://localhost:4000/api/links/ \  --header 'content-type: application/json' \  --data '{ "link": {  "url": "https://twitter.com/bnchrch" }}'
```

3. Prendre le `hash` retourné dans la réponse

`{"data":{"url":"https://twitter.com/bnchrch","hash":"7cJY_ckq"}}`

4. Et être redirigé correctement lorsque vous allez sur `localhost:4000/{hash}` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5jbpF4xVkeo2K7UIQKJWXg.gif)

### Conclusion

C'est incroyable à quel point il était facile de créer un raccourcisseur de liens rapide, facile à maintenir et simple à étendre avec tous ces outils. Une grande partie du mérite revient à la BEAM (machine virtuelle Erlang), Jose Valim (créateur d'Elixir) et Chris McCord (créateur de Phoenix). Le reste des éloges revient à la simplicité de l'idée d'un raccourcisseur de liens, qui ne justifie en aucun cas un prix d'introduction de 500 $ par mois. Je pense toujours à vous, Bit.ly.

#### ?‍? C'est open source ! Vous pouvez le trouver ici sur Github

#### ❤️ Je n'écris que sur la programmation et le travail à distance. Si vous [me suivez sur Twitter](https://www.twitter.com/bnchrch), je ne perdrai pas votre temps.