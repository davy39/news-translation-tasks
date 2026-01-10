---
title: Qu'est-ce que le Cross-Site Request Forgery (CSRF) ? Tutoriel sur la sécurité
  Web Laravel
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2022-10-04T21:40:49.000Z'
originalURL: https://freecodecamp.org/news/laravel-web-security-csrf
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Dark-Neon-Simple-Futuristic-UIUX-Designer-LinkedIn-Banner--7
seo_title: Qu'est-ce que le Cross-Site Request Forgery (CSRF) ? Tutoriel sur la sécurité
  Web Laravel
---

1-.png
tags:
- name: Laravel
  slug: laravel
- name: Sécurité Web
  slug: securite-web
seo_title: null
seo_desc: 'Dans ce tutoriel, vous découvrirez la sécurité web de Laravel et comment sécuriser
  vos applications web et les protéger contre les attaques de type Cross-Site Request Forgery, ou CSRF.

  Le CSRF est une activité malveillante qui consiste pour un attaquant à effectuer des actions au nom
  d''un utilisateur...'
---

Dans ce tutoriel, vous découvrirez la sécurité web de Laravel et comment sécuriser vos applications web et les protéger contre les attaques de type Cross-Site Request Forgery, ou CSRF.

Le CSRF est une activité malveillante qui consiste pour un attaquant à effectuer des actions au nom d'un utilisateur authentifié. Heureusement, Laravel fournit des mesures prêtes à l'emploi pour prévenir ce type de vulnérabilité.

**Dans ce tutoriel, vous apprendrez :**

* Qu'est-ce que le CSRF ?
* Comment prévenir une requête CSRF
* Comment et où se produit la vérification CSRF

## Qu'est-ce que le CSRF ?

Les attaques CSRF détournent les sessions utilisateur. Elles le font en trompant un utilisateur pour qu'il envoie une requête via des balises de formulaire cachées ou des URL malveillantes (images ou liens) à l'insu de l'utilisateur. 

Cette attaque entraîne un changement de l'état de la session utilisateur, des fuites de données, et les attaquants peuvent parfois manipuler les données des utilisateurs finaux dans une application.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-03-at-14.59.14-1.png)
_Explication du CSRF_

L'image ci-dessus illustre ce scénario où un Acteur (Utilisateur) envoie une requête depuis **malicious.xyz** via le **serveur web** vers **application.xyz**. Il se rend ensuite compte que ses informations ont été manipulées en **mettant à jour** son **mot de passe**.

## Comment prévenir les requêtes CSRF

Pour chaque session utilisateur, Laravel génère des jetons sécurisés qu'il utilise pour s'assurer que l'utilisateur authentifié est bien celui qui sollicite l'application. 

Puisque ce jeton change à chaque fois qu'une session utilisateur est régénérée, un attaquant malveillant ne peut pas y accéder. 

Chaque fois qu'il y a une requête pour modifier les informations de l'utilisateur côté serveur (back-end) comme `POST`, `PUT`, `PATCH` et `DELETE`, vous devez inclure un `@csrf` dans la requête du formulaire HTML. Le `@csrf` est donc une directive Blade utilisée pour générer un jeton caché validé par l'application. 

La **directive Blade** est la syntaxe utilisée au sein du moteur de template de Laravel appelé **Blade**. Pour créer un fichier blade, vous lui donnez un nom – dans notre cas form – suivi de l'extension blade. Cela signifie que le fichier aura le nom `form.blade.php`.

Vous utilisez le fichier blade pour rendre des vues aux utilisateurs sur la page web. Il existe quelques directives par défaut ou syntaxes raccourcies Blade que vous pouvez utiliser. Par exemple, `@if` vérifie si une condition est remplie, `@empty` vérifie si les enregistrements ne sont pas vides, `@auth` vérifie si un utilisateur est authentifié, et ainsi de suite. 

Mais ici, nous sommes plus intéressés par la directive `@csrf`. Voici comment l'utiliser :

```php
<form method="POST" action="{{route('pay')}}">

    @csrf
    
</form>
```

Les versions précédentes de Laravel ressemblaient un peu à ceci – les deux fonctionnent et font la même chose en coulisses.

```php
<form method="POST" action="{{route('pay')}}">
    
    <input type="hidden" name="_token" value="{{ csrf_token() }}" />
    
</form>
```

Lorsque le jeton CSRF n'est pas présent dans la requête du formulaire envoyée ou s'il semble invalide, Laravel renvoie un message d'erreur "Page Expired" avec un code d'état 419.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-03-at-15.11.43-1.png)
_Page Laravel 419 Expired_

## Comment et où se produit la vérification CSRF

Le middleware `VerifyCsrfToken` gère la vérification CSRF au sein de l'application Laravel. Le middleware est enregistré dans le Kernel.php, et se trouve dans le groupe de middleware de route web de l'application. Cela signifie que le middleware est déclenché pour les requêtes au sein du Web, pas celles liées aux API.

```php
protected $middlewareGroups = [
        'web' => [
           .
           .
           .
           .
           .
            \\App\\Http\\Middleware\\VerifyCsrfToken::class,
        ],
    ];
```

Le middleware VerifyCsrfToken étend la classe `Illuminate\\Foundation\\Http\\Middleware\\VerifyCsrfToken`. Cela signifie que la vérification CSRF est logée au sein de la classe. 

Plongeons plus profondément pour apprendre comment Laravel gère la vérification CSRF. 

Au sein de la classe, nous avons la fonction `tokensMatch`.

```php
protected function tokensMatch($request)
    {
        $token = $this->getTokenFromRequest($request);

        return is_string($request->session()->token()) &&
               is_string($token) &&
               hash_equals($request->session()->token(), $token);
    }
```

La fonction fait deux choses :

1. `$this->getTokenFromRequest` récupère le jeton de la requête entrante attaché via un champ caché ou l'en-tête de la requête. Le jeton est décrypté puis renvoyé à la variable token.

```php
protected function getTokenFromRequest($request)
    {
        $token = $request->input('_token') ?: $request->header('X-CSRF-TOKEN');

        if (! $token && $header = $request->header('X-XSRF-TOKEN')) {
            try {
                $token = CookieValuePrefix::remove($this->encrypter->decrypt($header, static::serialized()));
            } catch (DecryptException $e) {
                $token = '';
            }
        }

        return $token;
    }
```

2. Convertit le jeton de la requête et la session en chaîne de caractères, puis utilise la fonction PHP intégrée hash_equals pour comparer si les deux chaînes sont égales en un temps constant. Le résultat de cette opération est toujours un **booléen (true) ou (false)**.

## Conclusion

Dans cet article, vous avez découvert le CSRF, comment le gérer et s'en protéger, et les coulisses de la manière dont Laravel effectue la vérification.

Vous pouvez en savoir plus à ce sujet dans la [documentation de Laravel](https://laravel.com/docs/9.x/csrf). Et vous pouvez en savoir plus sur [PHP hash equals dans la documentation ici](https://www.php.net/manual/en/function.hash-equals.php).

Bon codage !