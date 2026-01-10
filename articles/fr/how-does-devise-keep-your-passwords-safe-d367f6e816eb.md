---
title: Comment Devise protège les mots de passe de votre application Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-15T10:45:18.000Z'
originalURL: https://freecodecamp.org/news/how-does-devise-keep-your-passwords-safe-d367f6e816eb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iOXaisZyDdgXEPpwHaFrRQ.jpeg
tags:
- name: Cryptography
  slug: cryptography
- name: Ruby on Rails
  slug: ruby-on-rails
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment Devise protège les mots de passe de votre application Rails
seo_desc: 'By Tiago Alves

  Devise is an incredible authentication solution for Rails with more than 40 million
  downloads. However, since it abstracts most of the cryptographic operations, it’s
  not always easy to understand what’s happening behind the scenes.

  One...'
---

Par Tiago Alves

[Devise](https://github.com/plataformatec/devise) est une solution d'authentification incroyable pour Rails avec [plus de 40 millions de téléchargements](https://rubygems.org/gems/devise). Cependant, comme il abstrait la plupart des opérations cryptographiques, il n'est pas toujours facile de comprendre ce qui se passe en coulisses.

L'une de ces abstractions culmine dans la persistance d'un `encrypted_password` directement dans la base de données. J'ai donc toujours été curieux de savoir ce qu'il représente réellement. Voici un exemple :

`$2a$11$yMMbLgN9uY6J3LhorfU9iuLAUwKxyy8w42ubeL4MWy7Fh8B.CH/yO`

Mais que signifie ce charabia ?

Devise utilise [Bcrypt](https://github.com/codahale/bcrypt-ruby) pour stocker les informations de manière sécurisée. Sur son site, il est mentionné qu'il utilise l'algorithme de hachage de mot de passe « OpenBSD bcrypt() », vous permettant de stocker facilement un hachage sécurisé des mots de passe de vos utilisateurs. Mais qu'est-ce que ce hachage exactement ? Comment fonctionne-t-il et comment protège-t-il les mots de passe stockés ?

C'est ce que je veux vous montrer aujourd'hui.

Travaillons à rebours — du hachage stocké dans votre base de données au processus de chiffrement et de déchiffrement.

Ce hachage `$2a$11$yMMbLgN9uY6J3LhorfU9iuLAUwKxyy8w42ubeL4MWy7Fh8B.CH/yO` est en réalité composé de plusieurs éléments :

* **Version Bcrypt** (`2a`) - la version de l'algorithme bcrypt() utilisée pour produire ce hachage (stockée après le premier signe `$`)
* **Coût** (`11`) - le facteur de coût utilisé pour créer le hachage (stocké après le deuxième signe `$`)
* **Sel** (`$2a$11$yMMbLgN9uY6J3LhorfU9iu`) - une chaîne aléatoire qui, combinée à votre mot de passe, le rend unique (29 premiers caractères)
* **Somme de contrôle** (`LAUwKxyy8w42ubeL4MWy7Fh8B.CH/yO`) - la partie réelle du hachage du `encrypted_password` stocké (chaîne restante après les 29 caractères)

![Image](https://cdn-media-1.freecodecamp.org/images/C1o8LTw8UCfepc7Tq3m5Yd1VGcMcT4XpRkBD)

Explorons les 3 derniers paramètres :

* Lorsque vous utilisez Devise, la valeur **Coût** est définie par une variable de classe appelée [stretches](https://github.com/plataformatec/devise/blob/715192a7709a4c02127afb067e66230061b82cf2/lib/devise.rb#L74) et la valeur par défaut est `11`. Elle spécifie le nombre de fois où le mot de passe est haché. (_Dans votre [initialiseur devise.rb](https://github.com/plataformatec/devise/blob/715192a7709a4c02127afb067e66230061b82cf2/test/rails_app/config/initializers/devise.rb#L70), vous pouvez configurer cette valeur à un niveau inférieur pour l'environnement de test afin de faire tourner votre suite de tests plus rapidement._) *
* Le **sel** est la chaîne aléatoire utilisée pour combiner avec le mot de passe original. C'est ce qui fait que le même mot de passe a des valeurs différentes lorsqu'il est stocké chiffré. (_Voir plus bas pourquoi cela compte et ce que sont les attaques par table arc-en-ciel._) **
* La **somme de contrôle** est le hachage réel généré du mot de passe après avoir été combiné avec le sel aléatoire.

Lorsque qu'un utilisateur s'inscrit sur votre application, il doit définir un mot de passe. Avant que ce mot de passe ne soit stocké dans la base de données, un sel aléatoire est généré via [BCrypt::Engine.generate_salt(cost)](https://www.rubydoc.info/github/codahale/bcrypt-ruby/BCrypt%2FEngine.generate_salt) en tenant compte du facteur de coût mentionné précédemment. _(Note : si la valeur de la [variable de classe](https://github.com/plataformatec/devise/blob/715192a7709a4c02127afb067e66230061b82cf2/lib/devise.rb#L155) [pepper](https://github.com/plataformatec/devise/blob/715192a7709a4c02127afb067e66230061b82cf2/lib/devise.rb#L155) est définie, elle [ajoutera sa valeur au mot de passe](https://github.com/plataformatec/devise/blob/715192a7709a4c02127afb067e66230061b82cf2/lib/devise/encryptor.rb#L9) avant de le saler.)_

Avec ce sel (ex. `$2a$11$yMMbLgN9uY6J3LhorfU9iu`, qui inclut le facteur de coût), il appellera [BCrypt::Engine.hash_secret(password, salt)](https://www.rubydoc.info/github/codahale/bcrypt-ruby/BCrypt%2FEngine.hash_secret) qui calcule le hachage final à stocker en utilisant le sel généré et le mot de passe choisi par l'utilisateur. Ce hachage final (par exemple, `$2a$11$yMMbLgN9uY6J3LhorfU9iuLAUwKxyy8w42ubeL4MWy7Fh8B.CH/yO`) sera à son tour stocké dans la colonne `encrypted_password` de la base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/mKgk9fAildsnwkuXhmOU0SDIiflG-nI8FPUa)

Mais si ce hachage est irréversible et que le sel est généré aléatoirement lors de l'appel à `BCrypt::Password.create` par `BCrypt::Engine.generate_salt(cost)`, **comment peut-il être utilisé pour connecter l'utilisateur ?**

C'est là que ces différents composants de hachage sont utiles. Après avoir trouvé l'enregistrement correspondant à l'email fourni par l'utilisateur pour se connecter, le mot de passe chiffré est récupéré et décomposé en différents composants mentionnés ci-dessus (**Version Bcrypt**, **Coût**, **Sel** et **Somme de contrôle**).

Après cette préparation initiale, voici ce qui se passe ensuite :

1. Récupérer le **mot de passe saisi** (`1234`)
2. Récupérer le **sel** du mot de passe stocké (`$2a$11$yMMbLgN9uY6J3LhorfU9iu`)
3. Générer le **hachage** à partir du mot de passe et du sel en utilisant la même version de bcrypt et le même facteur de coût (`BCrypt::Engine.hash_secret("1234", "$2a$11$yMMbLgN9uY6J3LhorfU9iu")`)
4. Vérifier si le **hachage stocké** est le même que celui calculé à l'étape 3 (`$2a$11$yMMbLgN9uY6J3LhorfU9iuLAUwKxyy8w42ubeL4MWy7Fh8B.CH/yO`)

![Image](https://cdn-media-1.freecodecamp.org/images/kJxy3TSK0VJ3fVqfFcVjmCCPCdgm1HyBb9C8)

Et c'est ainsi que Devise stocke les mots de passe de manière sécurisée et vous protège contre une série d'attaques, même si votre base de données est compromise.

Contactez-moi sur Twitter [@alvesjtiago](https://twitter.com/alvesjtiago) et faites-moi savoir si vous avez trouvé cet article intéressant ! Merci pour votre lecture.

![Image](https://cdn-media-1.freecodecamp.org/images/Lo-yU9BkzXFiqwgk5JS4RAKntUaE4KffvT5-)

> PS : Je ne suis en aucun cas un expert en sécurité ou en cryptographie, alors n'hésitez pas à me contacter si vous trouvez quelque chose de faux. J'espère qu'en simplifiant certains des concepts, il sera plus facile de comprendre ce qui se passe.

_Merci à [@filipepina](https://twitter.com/filipepina), [@ivobenedito](https://twitter.com/ivobenedito), [@jackveiga](https://twitter.com/jackveiga), [@joao_mags](https://twitter.com/joao_mags) et [@pedrosmmoreira](https://twitter.com/pedrosmmoreira) pour les révisions et suggestions. Cet article est également disponible à l'adresse [http://blog.tiagoalves.me/how-does-devise-keep-your-passwords-safe](http://blog.tiagoalves.me/how-does-devise-keep-your-passwords-safe/)._

Plus d'informations sur certains des sujets.

**Facteur de coût **

* [Dangers du facteur de coût bcrypt par défaut](https://labs.clio.com/bcrypt-cost-factor-4ca0a9b03966)
* [Nombre recommandé de rounds pour bcrypt](https://security.stackexchange.com/questions/17207/recommended-of-rounds-for-bcrypt)

**Attaques par table arc-en-ciel **

* [Table arc-en-ciel — Wikipédia](https://en.wikipedia.org/wiki/Rainbow_table)
* [Qu'est-ce que les tables arc-en-ciel et comment sont-elles utilisées ?](https://security.stackexchange.com/a/440)