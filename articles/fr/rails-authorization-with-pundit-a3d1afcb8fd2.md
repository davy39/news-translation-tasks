---
title: Autorisation Rails avec Pundit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-25T22:41:33.000Z'
originalURL: https://freecodecamp.org/news/rails-authorization-with-pundit-a3d1afcb8fd2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb6e0740569d1a4cae0a6.jpg
tags:
- name: General Programming
  slug: programming
- name: Rails
  slug: rails
- name: Ruby
  slug: ruby
- name: Ruby on Rails
  slug: ruby-on-rails
- name: software development
  slug: software-development
seo_title: Autorisation Rails avec Pundit
seo_desc: 'By Joseph Gefroh

  Pundit is a Ruby gem that handles authorization via a very simple API.

  Remember that authorization is different from authentication — authentication is
  verifying that you are who you say you are, and authorization is verifying that
  y...'
---

Par Joseph Gefroh

[Pundit](https://github.com/elabs/pundit) est une gem Ruby qui gère l'autorisation via une API très simple.

Rappelez-vous que l'autorisation est différente de l'authentification — l'authentification vérifie que vous êtes bien qui vous prétendez être, et l'autorisation vérifie que vous avez la permission d'effectuer une action.

Pundit est clairement dans le camp de l'autorisation — utilisez un autre système d'authentification comme [Devise](https://github.com/plataformatec/devise) pour gérer l'authentification.

### Comment travailler avec Pundit

**Étape 1 :** Vous créez une classe `Policy` qui gère l'autorisation d'accès à un type spécifique d'enregistrement — qu'il s'agisse d'un `Blog`, d'une `PommeDeTerre` ou d'un `Utilisateur`.

**Étape 2 :** Vous appelez la fonction intégrée `authorize` en passant ce que vous essayez d'autoriser.

**Étape 3 :** Pundit trouvera la classe `Policy` appropriée et appellera la méthode `Policy` qui correspond au nom de la méthode que vous autorisez. Si elle retourne vrai, vous avez la permission d'effectuer l'action. Sinon, elle lèvera une exception.

C'est assez simple. La logique pour des modèles spécifiques est encapsulée dans sa propre classe de politique, ce qui est idéal pour garder les choses bien organisées. La bibliothèque d'autorisation concurrente [cancancan](https://github.com/CanCanCommunity/cancancan) avait des problèmes avec des permissions compliquées qui devenaient ingérables.

### Petits ajustements nécessaires

Les conventions simples de Pundit doivent parfois être ajustées pour supporter des cas d'utilisation d'autorisation plus complexes.

#### Accéder à plus d'informations depuis une Policy

Par défaut, Pundit fournit deux objets à votre contexte d'autorisation : l'`Utilisateur` et l'`Enregistrement` étant autorisé. Cela est suffisant si vous avez des rôles système comme `Admin` ou `Modérateur`, mais ce n'est pas assez lorsque vous devez autoriser dans un contexte plus spécifique.

Supposons que vous avez un système qui supporte le concept d'une `Organisation`, et que vous devez supporter différents rôles au sein de ces organisations. Une autorisation système ne suffira pas — vous ne voulez pas qu'un admin de l'Organisation PommeDeTerre puisse faire des choses à l'Organisation Orange à moins qu'il ne soit admin des deux organisations. Lors de l'autorisation de ce cas, vous auriez besoin d'accéder à trois éléments : l'`Utilisateur`, l'`Enregistrement`, et les informations de rôle de l'utilisateur dans l'`Organisation`. Le cas idéal serait d'avoir accès à l'organisation à laquelle appartient l'enregistrement, mais rendons les choses plus difficiles et disons que nous n'avons pas accès à cela via l'enregistrement ou l'utilisateur.

Pundit offre une opportunité de fournir un contexte supplémentaire. En définissant une fonction appelée `pundit_user`, cela vous permet de changer ce qui est considéré comme un `user`. Si vous retournez un objet avec le contexte d'autorisation depuis cette fonction, ce contexte sera disponible pour vos politiques.

`application_controller.rb`

```
class ApplicationController < ActionController::Base  include Pundit
```

```
  def pundit_user    AuthorizationContext.new(current_user, current_organization)  endend
```

`authorization_context.rb`

```
class AuthorizationContext  attr_reader :user, :organization
```

```
  def initialize(user, organization)    @user = user    @organization = organization  endend
```

`application_policy.rb`

```
class ApplicationPolicy  attr_reader :request_organization, :user, :record
```

```
  def initialize(authorization_context, record)    @user = authorization_context.user    @organization = authorization_context.organization    @record = record  end
```

```
  def index?    # Votre politique a accès à @user, @organization, et @record.    endend
```

Vos politiques auront maintenant accès aux trois types d'informations — vous devriez voir comment accéder à plus d'informations si nécessaire.

#### Outrepasser la convention et spécifier quelle Policy utiliser

Pundit utilise des conventions de nommage pour associer ce que vous essayez d'autoriser avec la bonne politique. La plupart du temps, cela fonctionne bien, mais dans certains cas, vous devrez peut-être outrepasser cette convention, par exemple lorsque vous souhaitez autoriser une action générale de tableau de bord qui n'a pas de modèle associé. Vous pouvez passer des symboles pour spécifier quelle action ou politique utiliser pour l'autorisation :

```
# Ci-dessous appellera DashboardPolicy#bake_potato?authorize(:dashboard, :bake_potato?)
```

Si vous avez un modèle qui est nommé différemment, vous pouvez également outrepasser la fonction `policy_class` au sein du modèle lui-même :

```
class DashboardForAdmins  def self.policy_class   DashboardPolicy     # Cela force Pundit à utiliser Dashboard Policy au lieu de chercher    # DashboardForAdminsPolicy  endend
```

### Tests

L'autorisation est l'une de ces choses que je recommande fortement d'avoir une suite de tests automatisés. Les configurer incorrectement peut être catastrophique, et c'est, à mon avis, l'une des choses les plus fastidieuses à tester manuellement. Pouvoir exécuter une seule commande et savoir que vous n'avez pas involontairement changé de règles métier d'autorisation est une grande satisfaction.

Pundit rend les tests d'autorisation très simples.

```
def test_user_cant_destroy?  assert_raises Pundit::NotAuthorizedError do    authorize @record, :destroy?  endend
```

```
def test_user_can_show?  authorize @record, :show?end
```

Dans l'ensemble, j'aime Pundit. Je ne l'utilise que depuis peu, mais je le préfère déjà à cancancan — il semble simplement plus maintenable et testable.

Avez-vous trouvé cette histoire utile ? Veuillez **Applaudir** pour montrer votre soutien !  
Si vous ne l'avez pas trouvée utile, faites-moi savoir pourquoi avec un **Commentaire** !