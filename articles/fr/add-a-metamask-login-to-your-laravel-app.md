---
title: Comment ajouter une connexion MetaMask à votre application web Laravel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-23T18:38:03.000Z'
originalURL: https://freecodecamp.org/news/add-a-metamask-login-to-your-laravel-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/photo.png
tags:
- name: Laravel
  slug: laravel
- name: Metamask
  slug: metamask
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: Web3
  slug: web3
seo_title: Comment ajouter une connexion MetaMask à votre application web Laravel
seo_desc: 'By Darren Chowles

  Logging into a website via third parties is ubiquitous online. Almost every other
  member-based website allows you to log in with accounts like Facebook, Twitter,
  and Google.

  If you’ve ever visited NFT marketplaces like OpenSea or Ra...'
---

Par Darren Chowles

Se connecter à un site web via des services tiers est omniprésent en ligne. Presque tous les sites basés sur l'adhésion vous permettent de vous connecter avec des comptes comme Facebook, Twitter et Google.

Si vous avez déjà visité des places de marché NFT comme OpenSea ou Rarible, vous aurez remarqué qu'elles vous permettent de vous connecter avec un portefeuille crypto comme MetaMask. 

Ce processus de connexion affirme que vous êtes le propriétaire de l'adresse Ethereum en question et permet au système d'authentifier votre accès. C'est très similaire à la façon dont un nom d'utilisateur et un mot de passe vous permettraient d'accéder à une partie restreinte d'un site web.

## Prérequis

Avant de commencer ce tutoriel, je suppose que vous avez une compréhension de base de Laravel et que vous pouvez initialiser un nouveau projet dans votre environnement. Même si ce tutoriel est axé sur Laravel, vous pouvez l'appliquer à n'importe quel autre projet PHP avec quelques ajustements. Les concepts restent les mêmes.

J'ai essayé de garder cela aussi générique que possible. Je me concentre uniquement sur la signature et la validation MetaMask, sans vous restreindre à l'utilisation de technologies front-end spécifiques (comme React ou Vue) ou d'un scaffolding d'authentification (comme Breeze ou Jetstream). Cela vous donne la liberté de l'implémenter avec un effort minimal dans un projet existant.

Nous aurons besoin des éléments suivants avant de commencer :

* Un projet Laravel nouveau ou existant.
* [MetaMask](https://metamask.io/) installé dans votre navigateur.

## Modèle de base

Nous allons commencer avec du code de base (boilerplate) en important [Bootstrap 5](https://getbootstrap.com/) et en créant un simple bouton « Se connecter avec MetaMask ».

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-1-2.png)

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Connexion MetaMask</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.ethers.io/lib/ethers-5.2.umd.min.js"></script>
</head>
<body>
<div class="container">
    <div class="row">
        <div class="col-12 text-center">
            <button class="btn btn-primary mt-5">Se connecter avec MetaMask</button>
        </div>
    </div>
</div>
</body>
</html>
```

Assez facile. 😀

Nous importons également la [bibliothèque ethers.js](https://docs.ethers.io/) qui nous permettra d'interagir avec la blockchain Ethereum via MetaMask, qui agit ici comme interface pour le fournisseur (provider) ([Infura](https://infura.io/) par défaut).

### Astuce rapide :

Les fournisseurs (providers) nous permettent d'interagir avec la blockchain Ethereum. Pour vous connecter au réseau, vous avez besoin d'accéder à un nœud. Selon le type de nœud, cela peut nécessiter une grande quantité d'espace disque et de bande passante. Faire fonctionner un nœud peut également être un processus complexe, surtout si vous voulez vous concentrer sur le développement plutôt que sur la maintenance et l'exploitation d'un nœud. 

C'est là qu'intervient le fournisseur ! Des entreprises comme Infura fournissent ces nœuds en tant que service, vous n'avez donc pas à vous soucier de gérer le vôtre. À la place, vous pouvez accéder à cette fonctionnalité via leurs API.

Vous pourriez tomber sur d'anciens tutoriels indiquant que MetaMask injecte web3.js (une bibliothèque offrant des fonctionnalités similaires à ethers.js) dans la page par défaut. Ce n'est [plus le cas](https://docs.metamask.io/guide/provider-migration.html#summary-of-breaking-changes).

## Détecter le fournisseur

Nous allons commencer notre nouvelle fonction `web3Login()` en vérifiant que le navigateur dispose d'un fournisseur disponible. Ce serait le cas si vous avez MetaMask installé. Vous pouvez également tester ce code là où MetaMask n'est pas installé (par exemple, une fenêtre de navigation privée) pour confirmer que la détection fonctionne.

Ajoutez l'événement clic au bouton :

```html
<button class="btn btn-primary mt-5" onclick="web3Login();">Se connecter avec MetaMask</button>
```

Et commencez la fonction avec notre extrait de détection dans notre `<head>` sous l'importation de ethers.js :

```js
<script>
    async function web3Login() {
        if (!window.ethereum) {
            alert('MetaMask non détecté. Veuillez d\'abord installer MetaMask.');
            return;
        }
    }
</script>
```

Allez-y et testez cela dans un navigateur sans MetaMask installé.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-2-2.png)

## Installer les dépendances Laravel

Avant de poursuivre le processus de connexion front-end, nous devons mettre en place certains points de terminaison (endpoints). Notre script de connexion en aura besoin pour que l'utilisateur puisse signer un message avec son portefeuille, et notre système pourra ensuite vérifier sa signature.

Nous devons installer deux dépendances via Composer pour nous aider à effectuer le hachage et à utiliser la cryptographie sur les courbes elliptiques :

```bash
composer require kornrunner/keccak
composer require simplito/elliptic-php
```

## Ajouter les routes Laravel

Ouvrez votre fichier **routes/web.php** et ajoutez les routes suivantes :

```php
Route::get('/web3-login-message', 'Web3LoginController@message');
Route::post('/web3-login-verify', 'Web3LoginController@verify');
```

La première route renverra le message qui doit être signé, et la seconde route vérifiera le message signé.

## Créer le contrôleur de connexion

Il est maintenant temps de créer le contrôleur qui générera le message et effectuera la vérification.

Créez un nouveau fichier nommé **Web3LoginController.php** dans **app/Http/Controllers** et ajoutez-y le code suivant :

```php
<?php

namespace App\Http\Controllers;

use Elliptic\EC;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use kornrunner\Keccak;

class Web3LoginController
{
    public function message(): string
    {
        $nonce = Str::random();
        $message = "Signez ce message pour confirmer que vous possédez cette adresse de portefeuille. Cette action ne coûtera aucun frais de gaz.\n\nNonce : " . $nonce;

        session()->put('sign_message', $message);

        return $message;
    }

    public function verify(Request $request): string
    {
        $result = $this->verifySignature(session()->pull('sign_message'), $request->input('signature'), $request->input('address'));
        // Si $result est vrai, exécutez une logique supplémentaire comme la connexion de l'utilisateur, ou la création d'un compte s'il n'en existe pas basé sur l'adresse Ethereum
        return ($result ? 'OK' : 'ERROR');
    }

    protected function verifySignature(string $message, string $signature, string $address): bool
    {
        $hash = Keccak::hash(sprintf("\x19Ethereum Signed Message:\n%s%s", strlen($message), $message), 256);
        $sign = [
            'r' => substr($signature, 2, 64),
            's' => substr($signature, 66, 64),
        ];
        $recid = ord(hex2bin(substr($signature, 130, 2))) - 27;

        if ($recid != ($recid & 1)) {
            return false;
        }

        $pubkey = (new EC('secp256k1'))->recoverPubKey($hash, $sign, $recid);
        $derived_address = '0x' . substr(Keccak::hash(substr(hex2bin($pubkey->encode('hex')), 1), 256), 24);

        return (Str::lower($address) === $derived_address);
    }
}

```

Il se passe beaucoup de choses ici, alors décomposons :

### Créer le message

La méthode `message()` crée le message que nous fournirons au front-end. Elle inclut également un jeton aléatoire pour garantir que le message à signer sera différent à chaque fois.

Ce jeton est généralement appelé un nonce, ou nombre utilisé une seule fois. Dans ce cas, cependant, il s'agit d'une simple chaîne aléatoire. 

Le but est de prévenir les [attaques par rejeu](https://en.wikipedia.org/wiki/Replay_attack) où, si un utilisateur malveillant obtenait votre signature, il pourrait l'utiliser pour s'authentifier à votre place sur le site.

Le message est ensuite enregistré dans la session et renvoyé au front-end.

### Vérifier le message

Une fois que vous avez signé le message avec votre clé privée via MetaMask, votre adresse Ethereum ainsi que la signature sont envoyées au back-end pour vérification.

Si la vérification réussit, nous déterminons l'adresse Ethereum qui a signé le message et nous assurons qu'elle correspond à l'adresse Ethereum envoyée depuis le front-end lors du processus de signature.

Si cela passe, nous renvoyons un **OK** ou **ERROR** au front-end.

C'est également à ce stade que vous pouvez ajouter une logique supplémentaire comme la connexion du membre ou la création d'un nouvel enregistrement de membre s'il n'en existe pas pour l'adresse Ethereum en question.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Laravel-Metamask.png)

## Finaliser le Front End

Maintenant que le back-end est prêt, nous pouvons terminer le reste du front-end. Cela impliquera de lancer MetaMask, de demander à l'utilisateur de signer le message, puis de vérifier la signature en utilisant notre route back-end.

Voici la fonction `web3Login()` complète :

```js
<script>
    async function web3Login() {
        if (!window.ethereum) {
            alert('MetaMask non détecté. Veuillez d\'abord installer MetaMask.');
            return;
        }

        const provider = new ethers.providers.Web3Provider(window.ethereum);

        let response = await fetch('/web3-login-message');
        const message = await response.text();

        await provider.send("eth_requestAccounts", []);
        const address = await provider.getSigner().getAddress();
        const signature = await provider.getSigner().signMessage(message);

        response = await fetch('/web3-login-verify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'address': address,
                'signature': signature,
                '_token': '{{ csrf_token() }}'
            })
        });
        const data = await response.text();

        console.log(data);
    }
</script>

```

Décomposons-la :

* Nous définissons d'abord le fournisseur sur le `window.ethereum` fourni par MetaMask.
* Ensuite, nous récupérons le message renvoyé par notre back-end (rafraîchissez la page plusieurs fois pour essayer, vous remarquerez que le jeton aléatoire change à chaque fois).
* Une fois que nous avons le message, nous obtenons l'adresse Ethereum de l'utilisateur et lui demandons de signer le message.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-3-2.png)

* Nous envoyons ensuite l'adresse et la signature au back-end via POST (avec notre jeton CSRF Laravel) pour vérification.
* Le résultat est soit une chaîne **OK** soit **ERROR** que nous affichons dans la console.
* À ce stade, vous pouvez choisir d'afficher un message d'erreur (si applicable) ou de rediriger l'utilisateur s'il a été enregistré ou connecté pendant la vérification du back-end.

## Conclusion

Dans ce tutoriel, nous avons couvert les bases de l'ajout d'une connexion MetaMask à votre site web. J'espère que cela vous a été utile ! [Inscrivez-vous à ma newsletter](https://webdev.chowles.com/) ou [visitez mon blog](https://www.chowles.com/) où je partage des articles de développement web instructifs pour booster vos compétences.

Voici quelques idées pour aller plus loin dans votre intégration :

* Intégrez une bibliothèque comme [Web3Modal](https://github.com/web3modal/web3modal) pour offrir aux utilisateurs diverses options de portefeuille au lieu de seulement MetaMask.
* Une fois l'adresse Ethereum de l'utilisateur validée, proposez-lui des fonctions comme l'affichage de son solde ETH.

### Ressources

* Télécharger [MetaMask](https://metamask.io/).
* Consulter la [documentation de ethers.js](https://docs.ethers.io/).
* Dernière [documentation Laravel](https://laravel.com/docs).