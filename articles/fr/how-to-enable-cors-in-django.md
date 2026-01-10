---
title: Comment activer CORS dans Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-28T15:51:42.800Z'
originalURL: https://freecodecamp.org/news/how-to-enable-cors-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745855234567/f09d3338-c824-4cd8-a26f-93bb485f925a.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
- name: CORS
  slug: cors
seo_title: Comment activer CORS dans Django
seo_desc: 'If you''ve ever tried to connect your frontend app to your Django backend
  and suddenly hit an error that looks something like "has been blocked by CORS policy",
  you''re not alone. It’s frustrating, especially when your code seems fine.

  So what’s going ...'
---

Si vous avez déjà essayé de connecter votre application frontend à votre backend Django et que vous avez soudainement rencontré une erreur du type **"a été bloqué par la politique CORS"**, vous n'êtes pas seul. C'est frustrant, surtout lorsque votre code semble correct.

Alors, que se passe-t-il ?

C'est là que **CORS** (Cross-Origin Resource Sharing) intervient. Il s'agit d'une fonctionnalité de sécurité du navigateur qui bloque les pages web d'effectuer des requêtes vers un domaine différent de celui qui a servi la page web.

Elle est là pour protéger les utilisateurs, mais si elle n'est pas configurée correctement, elle peut empêcher votre application de fonctionner comme vous le souhaitez.

Réglez cela.

Dans cet article, je vais vous guider à travers tout ce que vous devez savoir pour activer CORS dans Django sans maux de tête.

### Voici ce que nous allons couvrir :

* [Qu'est-ce que CORS et pourquoi devriez-vous vous en soucier ?](#heading-quest-ce-que-cors-et-pourquoi-devriez-vous-vous-en-soucier)

* [Comment activer CORS dans Django](#heading-comment-activer-cors-dans-django)

  * [1. Installer django-cors-headers](#heading-1-installer-django-cors-headers)

  * [2. Ajoutez-le à INSTALLED_APPS](#heading-2-ajoutez-le-a-installedapps)

  * [3. Ajouter le Middleware](#heading-3-ajouter-le-middleware)

  * [4. Définir les origines autorisées](#heading-4-definir-les-origines-autorisees)

* [Paramètres optionnels dont vous pourriez avoir besoin](#heading-parametres-optionnels-dont-vous-pourriez-avoir-besoin)

  * [Autoriser toutes les origines (non recommandé pour la production)](#heading-autoriser-toutes-les-origines-non-recommande-pour-la-production)

  * [Autoriser les identifiants (Cookies, Auth)](#heading-autoriser-les-identifiants-cookies-auth)

  * [Autoriser des en-têtes spécifiques](#heading-autoriser-des-en-tetes-specifiques)

* [Exemple : Extrait complet du fichier de paramètres](#heading-exemple-extrait-complet-du-fichier-de-parametres)

* [Erreurs courantes (et comment les corriger)](#heading-erreurs-courantes-et-comment-les-corriger)

  * [1. CORS ne fonctionne pas du tout ?](#heading-1-cors-ne-fonctionne-pas-du-tout)

  * [2. La requête de prévol (méthode OPTIONS) échoue](#heading-2-la-requete-de-prevol-methode-options-echoue)

  * [3. Utilisez-vous Django Rest Framework ?](#heading-3-utilisez-vous-django-rest-framework)

* [FAQ](#heading-faq)

  * [Puis-je autoriser plusieurs URL de frontend ?](#heading-puis-je-autoriser-plusieurs-url-de-frontend)

  * [CORS affecte-t-il uniquement le développement local ?](#heading-cors-affecte-t-il-uniquement-le-developpement-local)

  * [Est-il sécurisé d'autoriser toutes les origines ?](#heading-est-il-securise-dautoriser-toutes-les-origines)

  * [Dois-je changer quelque chose sur le frontend ?](#heading-dois-je-changer-quelque-chose-sur-le-frontend)

* [Ressources supplémentaires](#heading-ressources-supplementaires)

* [Réflexions finales](#heading-reflexions-finales)

## Qu'est-ce que CORS et pourquoi devriez-vous vous en soucier ?

Avant de commencer à modifier les paramètres, il est important de comprendre ce qu'est CORS.

Imaginez que vous avez un frontend construit avec React fonctionnant sur `http://localhost:3000` et une API Django fonctionnant sur `http://localhost:8000`.

Lorsque le frontend essaie de communiquer avec le backend, votre navigateur voit qu'ils ne sont pas de la même origine (ils ont des ports différents), et il bloque la requête.

C'est CORS qui fait son travail. Il suppose que vous pourriez essayer de faire quelque chose d'insécurisé - comme voler des cookies ou des données utilisateur - alors il intervient.

Maintenant, en tant que développeur, si vous faites confiance au frontend et que vous possédez les deux extrémités, il est alors sûr de laisser passer ces requêtes. Vous devez simplement dire à Django que c'est acceptable.

## Comment activer CORS dans Django

Vous allez avoir besoin d'un package tiers appelé `django-cors-headers`. Il est largement utilisé et activement maintenu. Voici comment le configurer :

### 1. Installer `django-cors-headers`

Exécutez ceci dans votre terminal :

```bash
pip install django-cors-headers
```

Cela ajoute le package à votre environnement afin que Django puisse l'utiliser.

### 2. Ajoutez-le à `INSTALLED_APPS`

Ouvrez votre fichier `settings.py` et trouvez la section `INSTALLED_APPS`. Ajoutez cette ligne :

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
]
```

Cela enregistre l'application avec Django.

### 3. Ajouter le Middleware

Faites maintenant défiler jusqu'à la section `MIDDLEWARE` dans `settings.py`. Ajoutez ceci **en haut de la liste** :

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```

**Pourquoi en haut ?** Parce que le middleware dans Django s'exécute dans l'ordre. Si vous ne le placez pas en haut, les en-têtes CORS risquent de ne pas être ajoutés correctement, et votre navigateur bloquera toujours vos requêtes.

### 4. Définir les origines autorisées

C'est ici que vous dites à Django quelles origines sont autorisées à communiquer avec votre backend.

Toujours dans `settings.py`, ajoutez :

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

Remplacez `localhost:3000` par le domaine ou le port que votre frontend utilise. Si vous utilisez HTTPS ou déployez, assurez-vous d'inclure l'URL correcte, comme `https://votrefrontend.com`.

Et c'est tout ! Vous autorisez maintenant votre frontend à accéder à votre backend.

## Paramètres optionnels dont vous pourriez avoir besoin

Selon votre projet, vous pourriez rencontrer d'autres problèmes. Voici quelques paramètres supplémentaires que vous pourriez trouver utiles :

### Autoriser toutes les origines (non recommandé pour la production)

Si vous testez simplement et souhaitez tout autoriser (soyez prudent avec cela), vous pouvez utiliser :

```python
CORS_ALLOW_ALL_ORIGINS = True
```

Encore une fois, n'utilisez pas cela en production à moins de comprendre les risques. Cela peut ouvrir votre API à des abus.

### Autoriser les identifiants (Cookies, Auth)

Si votre frontend envoie des identifiants d'authentification comme des cookies ou des jetons, vous avez également besoin de ceci :

```python
CORS_ALLOW_CREDENTIALS = True
```

Et assurez-vous de **ne pas** utiliser `CORS_ALLOW_ALL_ORIGINS` avec ce paramètre - cela ne fonctionnera pas en raison des règles de sécurité. Restez avec `CORS_ALLOWED_ORIGINS`.

### Autoriser des en-têtes spécifiques

Par défaut, les en-têtes courants sont autorisés, mais si vous envoyez des en-têtes personnalisés (comme `X-Auth-Token`), vous pouvez ajouter :

```python
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    "x-auth-token",
    ...
]
```

## Exemple : Extrait complet du fichier de paramètres

Voici une mini version de ce à quoi votre `settings.py` pourrait ressembler après la configuration :

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

CORS_ALLOW_CREDENTIALS = True
```

Vous pouvez ajuster cela en fonction de vos besoins, mais c'est la structure de base.

## Erreurs courantes (et comment les corriger)

### 1. CORS ne fonctionne pas du tout ?

Vérifiez bien :

* Vous avez ajouté `corsheaders.middleware.CorsMiddleware` **en haut** de la liste des middlewares.

* Votre origine frontend correspond exactement, y compris le port et le protocole.

* Vous avez redémarré votre serveur après avoir modifié les paramètres.

### 2. La requête de prévol (méthode OPTIONS) échoue

Parfois, votre navigateur envoie une requête `OPTIONS` d'abord pour vérifier si le serveur permettra la vraie requête. Assurez-vous que vos vues ou votre configuration Django permettent cette méthode, sinon Django retournera une erreur 405.

Vous n'avez généralement rien à faire ici, sauf si vous utilisez un middleware ou un décorateur de vue personnalisé qui le bloque.

### 3. Utilisez-vous Django Rest Framework ?

Aucun problème - `django-cors-headers` fonctionne directement. Assurez-vous simplement qu'il est installé et que le middleware est configuré correctement.

## FAQ

### **Puis-je autoriser plusieurs URL de frontend ?**

Oui ! Il suffit d'ajouter plus d'éléments à la liste :

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://monfrontend.com",
]
```

### **CORS affecte-t-il uniquement le développement local ?**

Non, il s'applique également en production. Chaque fois que votre frontend et votre backend sont sur des origines différentes (domaine ou port différent), vous devez gérer CORS.

### **Est-il sécurisé d'autoriser toutes les origines ?**

Non. Ne faites cela que temporairement pendant le développement. Limitez toujours l'accès en production aux domaines que vous trustez.

### **Dois-je changer quelque chose sur le frontend ?**

Parfois. Si vous envoyez des identifiants (comme des cookies), vous devrez définir `credentials: "include"` dans vos requêtes fetch ou Axios.

Exemple avec fetch :

```js
fetch("http://localhost:8000/api/data", {
  method: "GET",
  credentials: "include",
})
```

## Réflexions finales

CORS peut sembler être un mur contre lequel vous continuez à courir lors de la création d'applications web. Mais une fois que vous avez compris comment cela fonctionne - et comment le configurer dans Django - cela devient une petite chose que vous configurez et passez à autre chose.

Rappelez-vous simplement :

* Soyez spécifique en production

* Redémarrez toujours le serveur après les modifications

* Ne ignorez pas les avertissements dans la console de votre navigateur - ils sont vos amis

Maintenant, vous savez comment activer CORS dans Django de la bonne manière.

### Ressources supplémentaires

* [Page GitHub de django-cors-headers](https://github.com/adamchainz/django-cors-headers) - pour la documentation complète.

* [Aperçu de CORS MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) - pour comprendre comment CORS fonctionne sous le capot.

* [Documentation officielle des Middleware Django](https://docs.djangoproject.com/en/stable/topics/http/middleware/)