---
title: Comment créer un JSON Web Token dans le Django Rest Framework
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-16T19:07:11.497Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-json-web-token-in-the-django-rest-framework
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744827939254/f99ab71c-f3a6-4858-8682-592e2e41bd45.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Comment créer un JSON Web Token dans le Django Rest Framework
seo_desc: 'When you''re building an API, security should be at the top of your list.
  You want to make sure only the right people can access the right stuff – and that’s
  where authentication comes in.

  One of the most common and reliable ways to handle authenticat...'
---

Lorsque vous construisez une API, la sécurité doit être en tête de votre liste. Vous voulez vous assurer que seules les bonnes personnes peuvent accéder aux bonnes choses – et c'est là que l'authentification intervient.

L'une des méthodes les plus courantes et fiables pour gérer l'authentification dans les applications web modernes est l'utilisation de JWT, abréviation de JSON Web Tokens.

Si vous travaillez avec le Django Rest Framework (DRF), vous savez peut-être déjà qu'il vient avec de nombreux outils utiles pour construire des APIs.

Mais lorsqu'il s'agit de l'authentification basée sur les tokens, vous aurez besoin d'un peu d'aide supplémentaire. JWT n'est pas intégré par défaut dans DRF, mais il est très facile à configurer une fois que vous connaissez les étapes.

Dans ce tutoriel, je vais vous guider étape par étape pour créer et utiliser des JWTs dans le Django Rest Framework.

### Table des matières :

1. [Qu'est-ce qu'un JWT ?](#heading-quest-ce-quun-jwt)

2. [Pourquoi utiliser JWT dans le Django Rest Framework ?](#heading-pourquoi-utiliser-jwt-dans-le-django-rest-framework)

3. [Comment configurer JWT dans le Django Rest Framework](#heading-comment-configurer-jwt-dans-le-django-rest-framework)

4. [Comment utiliser ces tokens](#heading-comment-utiliser-ces-tokens)

5. [FAQs](#heading-faqs)

6. [Meilleures pratiques](#heading-meilleures-pratiques)

7. [Réflexions finales](#heading-reflexions-finales)

## Qu'est-ce qu'un JWT ?

Un JWT (JSON Web Token) est une méthode compacte et autonome pour envoyer des informations de manière sécurisée entre deux parties. Il est souvent utilisé pour l'authentification.

Lorsque quelqu'un se connecte, il reçoit un token. Ce token est stocké dans le frontend (comme dans localStorage), et chaque fois que l'utilisateur fait une requête, il est envoyé avec celle-ci.

Le serveur vérifie ce token, et si tout est correct, il donne accès aux données demandées. Pas besoin de cookies ou de sessions.

Un JWT est composé de trois parties :

1. **En-tête** – contient le type de token et l'algorithme de signature.

2. **Charge utile** – contient les données (comme l'ID de l'utilisateur).

3. **Signature** – utilisée pour vérifier que le token n'a pas été modifié.

## Pourquoi utiliser JWT dans le Django Rest Framework ?

Voici pourquoi JWT est un bon choix pour les applications DRF :

* **Sans état** : Aucune session n'est nécessaire sur le serveur.

* **Évolutif** : Puisqu'il est sans état, il fonctionne bien avec des applications plus grandes et des microservices.

* **Largement utilisé** : JWT est une norme courante. De nombreux frameworks frontend (comme React, Vue, etc.) savent déjà comment travailler avec lui.

## Comment configurer JWT dans le Django Rest Framework

Passons à l'action. Voici comment configurer l'authentification JWT dans DRF.

### Étape 1 : Installer les packages requis

Vous aurez besoin d'une bibliothèque pour gérer les JWTs. La plus populaire est [djangorestframework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt).

Exécutez cette commande dans votre terminal :

```bash
pip install djangorestframework-simplejwt
```

Cela installe tout ce dont vous avez besoin pour générer, rafraîchir et vérifier les JSON web tokens dans votre projet DRF.

### Étape 2 : Mettre à jour vos paramètres Django

Allez dans votre fichier `settings.py` et mettez à jour la partie `REST_FRAMEWORK` comme suit :

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

Cela indique à DRF de rechercher un JWT dans l'en-tête `Authorization` de la requête et de l'utiliser pour authentifier l'utilisateur. Cela remplace l'authentification basée sur les sessions, typique pour les applications web, par une authentification basée sur les tokens, idéale pour les APIs.

### Étape 3 : Ajouter les URLs de token à votre `urls.py`

JWT fonctionne en émettant une paire de tokens : un token `access` (de courte durée) et un token `refresh` (de longue durée). Ces tokens sont gérés via deux vues principales.

Dans votre fichier [`urls.py`](http://urls.py) (généralement dans le projet racine ou l'application `api`) :

```python
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

Dans ce code :

* `/api/token/` : Les clients (comme les applications frontend ou mobiles) envoient les identifiants de l'utilisateur à ce point de terminaison pour obtenir des tokens d'accès et de rafraîchissement.

* `/api/token/refresh/` : Lorsque le token d'accès expire, le client envoie le token de rafraîchissement ici pour obtenir un nouveau token d'accès.

### Étape 4 : Tester

Supposons que vous avez un utilisateur avec un nom d'utilisateur et un mot de passe.

Vous pouvez faire une requête POST à `/api/token/` :

```json
{
  "username": "votre_nom_dutilisateur",
  "password": "votre_mot_de_passe"
}
```

Si les identifiants sont corrects, vous recevrez quelque chose comme :

```json
{
  "refresh": "long_token_de_rafraichissement",
  "access": "court_token_dacces"
}
```

Vous utiliserez le token `access` pour faire des requêtes authentifiées. Lorsqu'il expire, envoyez le token `refresh` à `/api/token/refresh/` pour en obtenir un nouveau.

## Comment utiliser ces tokens

Incluez le token d'accès dans l'en-tête `Authorization` de vos requêtes API comme ceci :

```javascript
Authorization: Bearer votre_token_dacces_ici
```

Lorsque le token d'accès expire, envoyez le token de rafraîchissement à `/api/token/refresh/` comme ceci :

```json
{
  "refresh": "votre_token_de_rafraichissement_ici"
}
```

Et vous recevrez un nouveau token d'accès.

### Sécuriser vos vues API

Pour vous assurer que seuls les utilisateurs authentifiés peuvent accéder à certains points de terminaison, ajoutez la classe de permission `IsAuthenticated` à vos vues.

Voici un exemple :

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class SecureView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Vous êtes authentifié !"})
```

Cette vue ne retournera une réponse que si la requête inclut un JWT valide. S'il n'y a pas de token ou s'il est invalide/expiré, l'utilisateur reçoit une erreur 401 Non autorisé.

### Résumé

Voici ce que nous venons de faire :

* Installé et configuré `simplejwt` pour DRF.

* Configuré les points de terminaison de génération et de rafraîchissement des tokens.

* Protégé les vues avec une authentification basée sur les tokens.

* Expliqué comment faire et rafraîchir les requêtes basées sur les tokens.

JWT est une méthode puissante et évolutive pour sécuriser vos APIs Django. C'est parfait pour les applications web et mobiles modernes.

Souhaitez-vous une étape bonus pour personnaliser les charges utiles des tokens (par exemple, ajouter des rôles d'utilisateur ou un email au JWT) ? Faites-le moi savoir !

## FAQs

### **Combien de temps le token dure-t-il ?**

Par défaut, le token d'accès dure 5 minutes, et le token de rafraîchissement dure 1 jour. Vous pouvez personnaliser cela dans vos paramètres :

```python
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```

Ce que cela signifie :

* Cela définit la durée de validité de vos **tokens JWT** :

* `ACCESS_TOKEN_LIFETIME` : Durée de validité du token d'accès (par exemple, 15 minutes).

* `REFRESH_TOKEN_LIFETIME` : Durée de validité du token de rafraîchissement (par exemple, 1 jour).

Pourquoi c'est important :

* Le **token d'accès** est ce qui permet à l'utilisateur d'interagir avec les points de terminaison protégés.

* Le **token de rafraîchissement** est utilisé pour obtenir un nouveau token d'accès sans se reconnecter.

### **Où dois-je stocker le token sur le frontend ?**

Idéalement dans `localStorage` ou `sessionStorage`. Soyez simplement conscient des risques XSS. Ne stockez pas de données sensibles dans le token lui-même.

Vous pouvez stocker les tokens d'accès/rafraîchissement JWT sur le frontend dans :

* `localStorage` : Les données persistent même après la fermeture de l'onglet/navigateur.

* `sessionStorage` : Les données sont perdues lorsque l'onglet/navigateur est fermé.

* Ne stockez pas de données utilisateur sensibles dans le token ou dans le stockage.

* Les tokens stockés dans `localStorage` peuvent être vulnérables aux attaques XSS.

* Si possible, envisagez d'utiliser des cookies httpOnly pour une meilleure sécurité (bien que plus complexe à configurer).

### **Puis-je ajouter des champs personnalisés au token ?**

Oui ! Vous pouvez remplacer `TokenObtainPairSerializer` pour inclure des données personnalisées dans la charge utile, comme ceci :

```python
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
```

Ensuite, connectez-le dans votre `urls.py`.

* Vous personnalisez la charge utile JWT pour inclure des informations utilisateur supplémentaires (comme `username`).

* Cela signifie que lorsque l'utilisateur se connecte, le JWT contiendra désormais le `username` dans la charge utile.

* Cela est utile si votre frontend souhaite afficher le nom de l'utilisateur sans faire un autre appel API.

### Résumé :

| **Section** | **Objectif** |
| --- | --- |
| Paramètres `SIMPLE_JWT` | Contrôle l'expiration des tokens |
| `localStorage/sessionStorage` | Où stocker les tokens sur le frontend |
| Sérialiseur de token personnalisé | Ajoute des informations utilisateur supplémentaires au token (par exemple, username) |
| Configuration [`urls.py`](http://urls.py) | Connecte votre vue de token personnalisée au point de terminaison de connexion |

## Meilleures pratiques

Examinons maintenant certaines des meilleures pratiques DRF afin que vous puissiez utiliser efficacement ce framework :

### 1. **Utilisez toujours HTTPS**

HTTPS chiffre les données transmises entre le client (navigateur ou application) et le serveur. Si vous utilisez HTTP à la place, n'importe qui sur le même réseau (comme un Wi-Fi public) pourrait intercepter des données sensibles – y compris les tokens d'accès – via une méthode appelée attaques de type man-in-the-middle (MITM).

#### Meilleures pratiques :

* Utilisez un certificat SSL pour activer HTTPS pour tous les points de terminaison.

* Redirigez toutes les requêtes HTTP vers HTTPS.

* Utilisez les en-têtes HSTS (HTTP Strict Transport Security) pour imposer HTTPS côté client.

### 2. **Ne stockez pas de données sensibles dans le token**

Les tokens comme les **JWTs** sont souvent stockés côté client (dans localStorage, sessionStorage ou des cookies).

S'ils contiennent des données sensibles (comme des mots de passe, des informations personnelles ou des clés secrètes), ils deviennent un risque majeur pour la sécurité – surtout s'ils sont volés ou compromis.

#### Que faire à la place :

* Stockez uniquement les informations minimales nécessaires (comme l'ID de l'utilisateur ou le rôle).

* Utilisez des tokens opaques (chaînes aléatoires) qui ne transportent pas de données intégrées lorsque cela est possible.

* Stockez les données sensibles de manière sécurisée sur le serveur, et non dans le token.

### 3. **Gardez votre clé de signature secrète**

#### Qu'est-ce qu'une clé de signature ?

Dans les systèmes utilisant des JWTs, la clé de signature (ou clé secrète) est utilisée pour signer le token – une méthode cryptographique pour s'assurer que le token n'a pas été falsifié.

Si quelqu'un obtient votre clé de signature, il peut forger des tokens valides et usurper l'identité des utilisateurs.

#### Meilleures pratiques :

* Stockez votre clé dans des environnements sécurisés (comme des variables d'environnement, des gestionnaires de secrets).

* Ne commitez jamais la clé dans le contrôle de source.

* Utilisez des secrets forts et générés aléatoirement.

* Envisagez d'utiliser des clés asymétriques (paires de clés publiques/privées) pour une meilleure évolutivité et sécurité (par exemple, avec l'algorithme RS256).

### 4. **Faites tourner les tokens si nécessaire**

#### Qu'est-ce que la rotation des tokens ?

La rotation des tokens fait référence au processus de génération périodique de nouveaux tokens et d'invalidation des anciens.

Cela est important car si un token est volé ou divulgué, le faire tourner régulièrement limite la fenêtre dans laquelle l'attaquant peut l'utiliser. C'est particulièrement important pour les tokens de rafraîchissement, qui ont tendance à vivre plus longtemps.

#### Meilleures pratiques :

* Utilisez des tokens d'accès de courte durée et des tokens de rafraîchissement de longue durée.

* Invalidez les tokens de rafraîchissement une fois qu'ils sont utilisés (une pratique appelée « rotation des tokens de rafraîchissement »).

* Suivez les tokens de rafraîchissement émis côté serveur pour détecter la réutilisation ou le vol.

### 5. **Définissez une courte durée de vie pour les tokens d'accès et utilisez les tokens de rafraîchissement judicieusement**

Les tokens d'accès accordent la permission d'accéder aux ressources protégées. S'ils sont volés, ils peuvent être utilisés par des attaquants jusqu'à leur expiration.

#### Meilleures pratiques :

* Définissez les tokens d'accès pour qu'ils expirent rapidement (5 à 15 minutes est courant).

* Utilisez les tokens de rafraîchissement pour permettre au client d'obtenir de nouveaux tokens d'accès sans se reconnecter.

* Stockez les tokens de rafraîchissement de manière sécurisée (préférez les cookies HTTP-only).

* Révoquez les tokens de rafraîchissement lors de la déconnexion, en cas d'activité suspecte ou de changement de périphérique.

## Réflexions finales

* Les **tokens d'accès** doivent être de courte durée et limités en portée.

* Les **tokens de rafraîchissement** doivent être de longue durée mais tournés et révoqués avec soin.

* Stockez toujours les secrets de manière sécurisée, servez via HTTPS et évitez de faire confiance au client avec des données ou une logique sensibles.

Souhaitez-vous que je montre comment tout cela se combine dans un flux d'exemple (comme le fonctionnement d'une connexion, de l'émission de token et du rafraîchissement) ?

Les JWTs rendent l'authentification plus facile et plus évolutive pour les APIs. Une fois que vous l'avez configuré dans le Django Rest Framework, cela fonctionne simplement – et vous avez une manière sécurisée de laisser les utilisateurs entrer et de garder le trafic indésirable à l'extérieur.

C'est un must si vous construisez des APIs avec Django.

### Lectures et ressources supplémentaires

* [Documentation SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

* [Documentation officielle DRF](https://www.django-rest-framework.org/)

* [JWT.io](https://jwt.io/) – excellent pour le débogage et l'apprentissage du fonctionnement des JWTs.

* [OWASP Cheat Sheet sur JWT](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)