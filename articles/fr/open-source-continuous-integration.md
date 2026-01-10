---
title: Comment j'ai contribué à un grand projet open source sans écrire de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-12T18:48:35.000Z'
originalURL: https://freecodecamp.org/news/open-source-continuous-integration
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-12-at-9.56.22-AM.png
tags:
- name: community
  slug: community
- name: Continuous Integration
  slug: continuous-integration
- name: open source
  slug: open-source
- name: Phoenix framework
  slug: phoenix
seo_title: Comment j'ai contribué à un grand projet open source sans écrire de code
seo_desc: 'By Adam Gordon Bell

  I recently got a pull request merged into the popular Phoenix Framework, and I did
  it without writing any Elixir code. I didn''t write any documentation either. What
  I did was help improve the build process.

  In this post, I''d like ...'
---

Par Adam Gordon Bell

J'ai récemment fait accepter une pull request dans le populaire Framework Phoenix, et ce sans écrire une seule ligne de code Elixir. Je n'ai pas non plus écrit de documentation. Ce que j'ai fait, c'est aider à améliorer le processus de build.

Dans cet article, je souhaite partager les améliorations que j'ai apportées à leur processus de build. Ces améliorations ne sont pas spécifiques au Framework Phoenix et pourraient changer votre façon d'aborder l'intégration continue.

Mais d'abord, un peu de contexte.

## Qu'est-ce que le Framework Phoenix ?

Phoenix est un framework web avec des propriétés très intéressantes. Avec Phoenix, vous pouvez construire des applications web interactives riches sans écrire de code côté client.

Vous pouvez le faire en utilisant une fonctionnalité appelée LiveView qui envoie des mises à jour en temps réel depuis le serveur pour mettre à jour le HTML du navigateur client.

Nous pouvons créer une page qui affiche les derniers tweets sur un sujet, en temps réel, assez facilement.

Voici un exemple :

```elixir
defmodule TimelineLive do
  use Phoenix.LiveView

  def render(assigns) do
    render("timeline.html", assigns)
  end

  def mount(_, socket) do
    Twitter.subscribe("elixirphoenix")
    {:ok, assign(socket, :tweets, [])}
  end

  def handle_info({:new, tweet}, socket) do
    {:noreply,
     update(socket, :tweets, fn tweets ->
       Enum.take([tweet | tweets], 10)
     end)}
  end
end

```

![Image](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2FCorecursive%2FDUy3Kzmdsn.png?alt=media&token=edf6aee0-7744-435e-9e3f-0557e000214e)
_Results Twitter en temps réel sans écrire de JavaScript_

Le framework est écrit dans le langage de programmation Elixir.

Il a été créé par José Valim. Il ressemble beaucoup à Ruby mais a des sémantiques très différentes. Elixir s'exécute sur la VM Erlang, et il alimente des projets comme Discord et est utilisé dans des entreprises comme Heroku.

## Comment reproduire les builds

Le Framework Phoenix utilise GitHub Actions pour leur pipeline de build. Comme de nombreux grands projets, ils disposent d'une suite de tests unitaires qu'ils doivent exécuter sur chaque contribution utilisateur.

Ce n'est pas là que s'arrêtent leurs efforts de test. Ils disposent également d'une suite de tests d'intégration. Phoenix utilise un ORM pour communiquer avec diverses bases de données et les tests d'intégration garantissent qu'aucun changement ne rompt l'intégration avec l'une des 3 bases de données supportées.

C'est un schéma courant. Avoir un grand nombre de tests unitaires faciles à exécuter ainsi qu'une poignée de tests d'intégration plus lents mais plus complets est un excellent moyen d'empêcher l'introduction de bugs dans le projet.

Le Framework Phoenix va encore plus loin, car ils doivent également supporter plusieurs versions du langage Elixir et quelques versions de la plateforme Open Telecom Platform (OTP).

Cela commence à devenir complexe. Nous devons tester chaque changement avec toutes les combinaisons des éléments suivants :

* Bases de données (Postgres, MySQL, MSSQL)
* Elixir (Version actuelle et précédente)
* OTP (Version actuelle et précédente)

Il est relativement facile de configurer cela dans GitHub Actions, mais comment exécuter ces tests localement ?

Installer tout cela serait beaucoup demander, donc les contributeurs ont tendance à s'appuyer sur GitHub Actions pour tester ces combinaisons. Cependant, si tout le monde doit s'appuyer sur l'envoi de code sur GitHub pour voir si les tests passent, le développement devient plus lent.

Comment résoudre ce problème ?

## Comment unifier les exécutions de tests

C'est là que je suis intervenu. Je travaille chez Earthly Technologies en tant qu'avocat des développeurs open source. Nous avons un outil de build open source assez cool, et bien que je contribue occasionnellement directement au projet, mon travail consiste à être le point de contact entre la communauté utilisant l'outil et l'équipe qui travaille dessus.

J'avais entendu parler de ce problème de reproductibilité que l'équipe Phoenix rencontrait. Je pensais pouvoir aider à écrire un script de build qui pourrait être utilisé à la fois dans GitHub Actions et pour un workflow de développement local. J'ai donc commencé à travailler sur une PR.

### Exécuter les tests localement

Ce que j'ai fini par créer, légèrement simplifié, est ceci :

```dockerfile
installation:
   ARG ELIXIR=1.10.4
   ARG OTP=23.0.3
   # Pull a Docker Image to Run Build Inside Of
   FROM hexpm/elixir:$ELIXIR-erlang-$OTP-alpine-3.12.0
   ...
 
test-dintegration:
    FROM +installation
    COPY . .
    # Pull In Dependencies
    RUN mix deps.get 
    # Start Up Service Dependencies
    WITH DOCKER --compose docker-compose.yml 
        # Run Tests
        RUN mix test --include database 
    # Stop Service Dependencies
    END


```

Ceci est un Earthfile. Il est composé de plusieurs cibles, comme `installation` et `test-dintegration`. Les cibles peuvent avoir des dépendances entre elles. Vous pouvez utiliser l'outil en ligne de commande `earthly` pour exécuter n'importe quelle cible et chacune est exécutée dans un conteneur Docker. La conteneurisation va nous permettre d'exécuter le build où nous le choisissons.

Cet exemple exécute le `test-dintegration` à l'intérieur du conteneur Docker `hexpm/elixir` avec la version spécifiée d'Elixir et d'OTP installée.

Avant d'exécuter les tests avec `mix test --include database`, nous utilisons Docker compose pour démarrer toutes les dépendances nécessaires :

```dockerfile
 WITH DOCKER --compose docker-compose.yml
        RUN mix test --include database
 END 

```

Le fichier Docker compose ressemble à ceci :

```yaml
version: '3'
services:
  postgres:
    image: postgres
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: postgres
  mysql:
    image: mysql
    ports:
      - "3306:3306"
    environment:
      MYSQL_ALLOW_EMPTY_PASSWORD: "yes"
  mssql:
    image: mcr.microsoft.com/mssql/server:2019-latest
    environment:
      ACCEPT_EULA: Y
      SA_PASSWORD: some!Password
    ports:
      - "1433:1433"	

```

Ce sont les bases de données dont nous avons besoin pour tester Phoenix.

Maintenant, nous pouvons exécuter les tests d'intégration en ligne de commande comme suit :

```
>  earthly -P +test-dintegration

```

Et si nous voulons tester une version différente d'Elixir, nous pouvons spécifier la version comme arguments de build :

```
 > earthly -P --build-arg ELIXIR=1.11.0 --build-arg OTP=23.1.1 +test-dintegration

```

Il existe d'autres moyens d'y parvenir. Une combinaison d'un makefile et de dockerfiles aurait également fonctionné. L'essentiel est de sortir la logique de build d'un format spécifique à GHA et de la mettre dans quelque chose qui peut être exécuté n'importe où.

## Comment l'exécuter dans GitHub Actions

Pour utiliser ce même processus dans GitHub Actions, la seule chose que nous devons faire est d'ajuster notre yaml GitHub Actions pour utiliser Earthly pour le pipeline de build et nous sommes prêts.

```javascript
  test-dintegration-elixir:
    runs-on: ubuntu-latest
    env:
      FORCE_COLOR: 1
    
    strategy:
      fail-fast: false
      matrix:
        include:
          - elixir: 1.11.1
            otp: 21.3.8.18
          - elixir: 1.11.1
            otp: 23.1.1
    steps:
      - uses: actions/checkout@v2
      - name: Download released earth
        run: "sudo /bin/sh -c 'wget https://github.com/earthly/earthly/releases/download/v0.4.1/earthly-linux-amd64 -O /usr/local/bin/earthly && chmod +x /usr/local/bin/earthly'"
      - name: Execute tests
        run: earthly -P --build-arg ELIXIR=${{ matrix.elixir }}  --build-arg OTP=${{ matrix.otp }} +test-dintegration

```

Nous y voilà, nous sommes maintenant en mesure d'exécuter notre pipeline de build localement, sans aucune configuration d'environnement complexe. Nous pouvons également exécuter le même processus de build sur notre machine de développement sans avoir besoin d'installer quoi que ce soit sauf Earthly. Cela facilite l'approche du projet pour les nouveaux contributeurs.

## Le résultat final

Finalement, avec l'aide de l'équipe Phoenix, j'ai fait approuver ce changement et le projet Phoenix dispose désormais d'un moyen facile de tester et d'itérer sur leur pipeline de build localement. Et je n'ai même pas écrit une seule ligne de code Elixir ! Vous pouvez trouver plus de détails dans la [PR](https://github.com/phoenixframework/phoenix/pull/4072).

Merci d'avoir lu cet article. Si vous souhaitez en savoir plus sur Earthly, [vous pouvez trouver beaucoup d'informations ici](http://earthly.dev/). Et si vous souhaitez mon aide pour le build de votre projet open source, faites-le moi savoir.