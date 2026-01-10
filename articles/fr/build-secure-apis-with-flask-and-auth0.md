---
title: Comment créer des API sécurisées avec Flask et Auth0
subtitle: ''
author: Juan Cruz Martinez
co_authors: []
series: null
date: '2023-02-08T00:32:04.000Z'
originalURL: https://freecodecamp.org/news/build-secure-apis-with-flask-and-auth0
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/3.png
tags:
- name: api
  slug: api
- name: Auth0
  slug: auth0
- name: authorization
  slug: authorization
- name: Flask Framework
  slug: flask
- name: Security
  slug: security
seo_title: Comment créer des API sécurisées avec Flask et Auth0
seo_desc: "APIs are at the heart of modern development. They support all kinds of\
  \ systems, from mobile, web, and desktop applications, to IoT devices and self-driving\
  \ cars. They are a bridge between your clients and your application logic and storage.\
  \ \nThis cen..."
---

Les API sont au cœur du développement moderne. Elles supportent tous types de systèmes, des applications mobiles, web et de bureau, aux appareils IoT et aux voitures autonomes. Elles constituent un pont entre vos clients et la logique de votre application ainsi que son stockage.

Ce point d'accès central aux données de votre application soulève la question suivante : comment fournir l'accès aux informations à ceux qui en ont besoin tout en refusant l'accès aux requêtes non autorisées ?

L'industrie a fourni plusieurs protocoles et bonnes pratiques pour sécuriser les API. Aujourd'hui, nous allons nous concentrer sur [OAuth2](https://auth0.com/docs/authorization/protocols/protocol-oauth2?utm_source=freecodecamp?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask), l'une des options les plus populaires pour autoriser les clients à accéder à nos API.

Mais comment implémenter OAuth2 ? Il existe deux approches possibles :

1. L'approche "faites-le vous-même"
2. Travailler avec un tiers de confiance comme [Auth0](https://auth0.com/?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask)

Dans cet article, je vais vous guider à travers une implémentation d'OAuth2 pour Python et [Flask](https://flask.palletsprojects.com/) en utilisant Auth0 comme fournisseur d'identité. Mais d'abord, nous allons discuter de l'approche "faites-le vous-même".

## Pourquoi ne pas construire votre propre système d'authentification et d'autorisation ?

Depuis quelques années, je voulais rendre à la communauté qui m'a tant aidé en m'enseignant la programmation et en m'aidant à progresser dans ma quête de connaissances. J'ai toujours pensé qu'une excellente façon de contribuer était d'avoir mon propre blog, une chose que j'ai essayée plus d'une fois et échoué.

Mais où ai-je échoué ? Au lieu de me concentrer sur l'écriture, j'ai essayé de construire mon propre moteur de blog parce que c'est dans ma nature. C'est ce que font les développeurs. Ils adorent construire.

Mais pourquoi en parler ici ? Parce que beaucoup tombent dans le même piège lors de la construction d'API. Laissez-moi expliquer avec un exemple.

Bob est un excellent développeur, et il a cette idée géniale pour une application ToDo qui pourrait être la prochaine grande chose. Bob est très conscient que pour une implémentation réussie, les utilisateurs ne peuvent accéder qu'à leurs propres données.

Voici la chronologie de l'application de Bob :

- Sprint 0 : Recherche d'idées et début du prototypage
- Sprint 1 : Construction de la table des utilisateurs et de l'écran de connexion avec l'API
- Sprint 2 : Ajout des écrans de réinitialisation du mot de passe et construction de tous les modèles d'e-mails
- Sprint 3 : Construction, création et liste des écrans ToDos
- Sprint 4 : Le MVP est mis en ligne
- Retours des utilisateurs :
  - Certains utilisateurs ne peuvent pas se connecter en raison d'un bug
  - Certains utilisateurs se sentent en insécurité sans authentification à deux facteurs
  - Certains utilisateurs ne veulent pas avoir un autre mot de passe. Ils préfèrent une connexion unique avec Google ou Facebook.
  - …

Parlons de ce qui s'est passé. Bob a passé les premiers sprints non pas à construire son application, mais à construire les blocs de base, comme la fonctionnalité de connexion et de déconnexion, les notifications par e-mail, et ainsi de suite. Ce temps précieux aurait pu être utilisé différemment, mais ce qui se passe ensuite est plus préoccupant.

Le backlog de Bob commence à se remplir. Maintenant, il doit improviser une méthode d'authentification à deux facteurs, ajouter une connexion unique, et plus de fonctions non liées au produit qui pourraient potentiellement retarder son produit.

Et il reste encore une grande question à répondre : Bob a-t-il implémenté tous les mécanismes de sécurité correctement ? Une erreur critique pourrait exposer toutes les informations des utilisateurs à des tiers.

Ce que Bob a fait est ce que j'ai fait avec mon blog à plusieurs reprises. Parfois, il est utile de s'appuyer sur des tiers si nous voulons faire les choses correctement.

Aujourd'hui, les pirates et les attaques sont devenus si sophistiqués que la sécurité n'est plus un facteur trivial. C'est un système compliqué en soi, et il est souvent préférable de laisser son implémentation à des experts – non seulement pour qu'elle soit bien faite, mais aussi pour que nous puissions nous concentrer sur ce qui compte : construire nos applications et nos API.

## Comment configurer un compte gratuit de gestion d'identité Auth0

[Auth0](https://auth0.com/?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask) est un fournisseur leader d'authentification et d'autorisation, mais voyons comment il peut aider Bob (ou vous) à construire une meilleure application :

1. Il [fait gagner du temps](https://auth0.com/learn/finn-ai-saves-10-5-ongoing-engineering-time-auth0/?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask)
2. Il est [sécurisé](https://auth0.com/security?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask)
3. Il a un [plan gratuit](https://auth0.com/pricing?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask)

Passons à la pratique. Tout d'abord, assurez-vous d'avoir un compte Auth0. Si ce n'est pas le cas, vous pouvez en créer un [ici gratuitement](https://auth0.com/signup/?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask).

### Créer une nouvelle API Auth0

Il y a encore une chose que nous devons faire avant de commencer à coder. Rendez-vous dans la section [API](https://manage.auth0.com/#/apis?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask) de votre tableau de bord Auth0 et cliquez sur le bouton « Créer une API ». Après cela, remplissez le formulaire avec vos détails. Cependant, assurez-vous de sélectionner `RS256` comme `Algorithme de signature`.

Votre formulaire devrait ressembler à ce qui suit :

![Image](https://lh5.googleusercontent.com/XccGez21ClEDsCECuKwiF_1AF5gj2OXXaJKEXVUOBFmxQ7Ci11a1g1O3cu_io185YbdnSJkAlu3dmP0pt6Ww-N6cPqQLTIeweSi2hNv4ototIkuSZhfiprjqcMrFhcMLaGkKfedkm8D0PR2IcjdLPGUChKS27wsiPMvqCsysQRJyGANVYc5Q5EbFdaFo)
_Création de l'API – image montrant les champs à remplir_

La page des détails de l'API s'ouvre après avoir créé avec succès une API. Gardez cet onglet ouvert, car il contient des informations dont nous avons besoin pour configurer notre application. Si vous le fermez, ne vous inquiétez pas, vous pouvez toujours y accéder à nouveau.

## Comment démarrer notre application

Parce que nous allons nous concentrer uniquement sur les aspects de sécurité, nous allons prendre quelques raccourcis lors de la construction de notre API de démonstration. Cependant, lors du développement [d'API réelles](https://livecodestream.dev/post/python-flask-api-starter-kit-and-project-layout/?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask), veuillez suivre [les meilleures pratiques pour les API Flask](https://auth0.com/blog/best-practices-for-flask-api-development/?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask).

### Installer les dépendances

Tout d'abord, installez les dépendances suivantes pour configurer Flask et authentifier les utilisateurs.

```shell
pipenv install flask python-dotenv python-jose flask-cors six
```

### Construire les endpoints

Notre API sera très simple. Elle consistera en seulement trois endpoints, tous publics pour l'instant. Cependant, nous allons bientôt corriger cela. Voici nos endpoints :

* `/` (endpoint public)
* `/user` (nécessite un utilisateur connecté)
* `/admin` (uniquement les utilisateurs avec le rôle admin)

Commençons :

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_view():
    """
    Endpoint par défaut, il est public et peut être accédé par n'importe qui
    """
    return jsonify(msg="Hello world!")

@app.route("/user")
def user_view():
    """
    Endpoint utilisateur, ne peut être accédé que par un utilisateur autorisé
    """
    return jsonify(msg="Hello user!")

@app.route("/admin")
def admin_view():
    """
    Endpoint admin, ne peut être accédé que par un admin
    """
    return jsonify(msg="Hello admin!")

```

Très simple, n'est-ce pas ? Exécutons-le :

```shell
~ pipenv run flask run
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Et si nous accédons à notre endpoint :

```shell
~ curl -i http://localhost:5000
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 23
Server: Werkzeug/2.0.1 Python/3.9.1
Date: Tue, 24 Jan 2023 21:24:57 GMT

{"msg":"Hello world!"}

~ curl -i http://localhost:5000/user
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 22
Server: Werkzeug/2.0.1 Python/3.9.1
Date: Tue, 24 Jan 2023 21:25:42 GMT

{"msg":"Hello user!"}

~ curl -i http://localhost:5000/admin
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 23
Server: Werkzeug/2.0.1 Python/3.9.1
Date: Tue, 24 Jan 2023 21:26:18 GMT

{"msg":"Hello admin!"}
```

## Comment sécuriser les endpoints

Puisque nous utilisons OAuth, nous allons authentifier les requêtes en validant un token d'accès au format [JWT](https://auth0.com/learn/json-web-tokens/?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask). Nous allons l'envoyer à l'API à chaque requête dans les en-têtes HTTP.

### Variables de configuration Auth0

Comme mentionné dans la section précédente, notre API doit être consciente et nécessitera des informations de notre tableau de bord Auth0. Donc, retournez à votre [page de détails de l'API](https://manage.auth0.com/#/apis?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask), et récupérez deux valeurs différentes.

**Tout d'abord, l'identifiant de l'API :**

C'est la valeur requise lors de la création de l'API. Vous pouvez également l'obtenir à partir de votre page de détails de l'API :

![Image](https://lh5.googleusercontent.com/UffKcasZXNZmXldeB8nhDEjzmOPVao3PR6EUVPbtWzXStuDzcCw2kr5ztEnr0VlWCkBLbhleAM-D11Cv5Cv8fcII8m24D6TfEe4XfxWe8HXN1aNrF-dHeN05zeVeoNfQISWh-VPf0__x8uVfJPL3GGHYIC87utfrr6734Z9Wdk-9eJUApslcdUKOyoSh)
_Comment trouver l'identifiant de l'API sur la page de détails de l'API_

**Ensuite, le domaine Auth0 :**

Sauf si vous utilisez un domaine personnalisé, cette valeur sera [`[NOM_DU_TENANT].auth0.com`](about:blank), et vous pouvez la récupérer dans l'onglet `Test` (assurez-vous de ne pas inclure `https://` et le dernier slash `/`).

![Image](https://lh4.googleusercontent.com/cA63NdLr4AWOz2O3jTWBXTTqc7DrGOr1aPOIpNDRYl97-o84I_lX8KtotCm6hRWF06ai0RjiJzgTjS_zRlySKFAB-XO1w737N05i7-bC2-GZioOpcWuS5gaRoEnDL63gXnm5CyP6JOEQusRLQMF1sY_1vjfXtdMVIr5uCW1PMIpokH76lpMq2VFZSIyf)
_Obtention du domaine Auth0_

Ensuite, passez ces valeurs dans des variables afin qu'elles puissent être utilisées dans les fonctions de validation.

```python
AUTH0_DOMAIN = 'VOTRE-DOMAINE-AUTH0'
API_IDENTIFIER = 'IDENTIFIANT-API'
ALGORITHMS = ["RS256"]
```

### Méthodes d'erreur

Lors de cette implémentation, nous aurons besoin d'un moyen de lever des erreurs lorsque l'authentification échoue. Nous utiliserons donc les helpers suivants pour ces besoins :

```python
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
```

### Comment capturer le token JWT

La première étape pour valider un utilisateur est de récupérer le token JWT des en-têtes HTTP. Cela est très simple, mais il y a quelques points à garder à l'esprit. Voici un exemple :

```python
def get_token_auth_header():
    """
    Obtient le token d'accès de l'en-tête d'autorisation
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "L'en-tête d'autorisation est attendu"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "L'en-tête d'autorisation doit commencer par"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token non trouvé"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "L'en-tête d'autorisation doit être"
                            " Bearer token"}, 401)

    token = parts[1]
    return token
```

### Comment valider le token

Avoir un token passé à notre API est un bon signe, mais cela ne signifie pas que c'est un client valide. Nous devons vérifier la signature du token.

Puisque la logique pour nécessiter une authentification peut être utilisée pour plus d'un endpoint, il serait important de l'abstraire et de la rendre facilement accessible pour que les développeurs puissent l'implémenter. La meilleure façon de faire cela est d'utiliser des [décorateurs](https://book.pythontips.com/en/latest/decorators.html).

```python
def requires_auth(f):
    """
    Détermine si le token d'accès est valide
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_IDENTIFIER,
                    issuer="https://"+AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                "description": "token is expired"}, 401)
            except jwt.JWTClaimsError:
                raise AuthError({"code": "invalid_claims",
                                "description":
                                    "incorrect claims,"
                                    "please check the audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                "description":
                                    "Unable to parse authentication"
                                    " token."}, 401)

            _request_ctx_stack.top.current_user = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                        "description": "Unable to find appropriate key"}, 401)
    return decorated
```

Le nouveau décorateur `requires_auth`, lorsqu'il est appliqué à un endpoint, rejettera automatiquement la requête si aucun utilisateur valide ne peut être authentifié.

### Comment nécessiter une requête authentifiée pour un endpoint

Nous sommes prêts à sécuriser nos endpoints, mettons à jour les endpoints `user` et `admin` pour utiliser notre décorateur.

```python
@app.route("/user")
@requires_auth
def user_view():
    """
    Endpoint utilisateur, ne peut être accédé que par un utilisateur autorisé
    """
    return jsonify(msg="Hello user!")

@app.route("/admin")
@requires_auth
def admin_view():
    """
    Endpoint admin, ne peut être accédé que par un admin
    """
    return jsonify(msg="Hello admin!")
```

Notre seul changement a été d'ajouter `@required_auth` en haut de la déclaration de chaque fonction d'endpoint, et avec cela nous pouvons tester à nouveau :

```shell
~ curl -i http://localhost:5000/user
HTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 89
Server: Werkzeug/2.0.1 Python/3.9.1
Date: Tue, 24 Jan 2023 21:42:26 GMT

{"code":"authorization_header_missing","description":"Authorization header is expected"}

~ curl -i http://localhost:5000/admin
HTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 89
Server: Werkzeug/2.0.1 Python/3.9.1
Date: Tue, 24 Jan 2023 21:42:42 GMT

{"code":"authorization_header_missing","description":"Authorization header is expected"}
```

Comme prévu, nous ne pouvons pas accéder à nos endpoints car l'en-tête d'autorisation est manquant. Mais avant d'en ajouter un, vérifions si notre endpoint public fonctionne toujours :

```shell
~ curl -i http://localhost:5000
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 23
Server: Werkzeug/2.0.1 Python/3.9.1
Date: Tue, 24 Jan 2023 21:43:55 GMT

{"msg":"Hello world!"}
```

Super, cela fonctionne comme prévu.

### Comment le tester

Pour tester nos nouveaux endpoints sécurisés, nous devons obtenir un token d'accès valide que nous pouvons passer à la requête. Nous pouvons le faire directement dans l'onglet `Test` de la page de détails de l'API, et c'est aussi simple que de copier une valeur de l'écran :

![Image](https://lh5.googleusercontent.com/XCAWL5taQUs3_5qcAdukl9FP_aTVLya-jyS_4IivFW6JCAfX5d2hbPPCIV4PB8QgcuceQrzC__YYpWMQB1y8HT9AnKO01XH5rCiofvQJAmiAPnGF42FcJFxaVHTLLQcL9UpzFjYgan0Qasna69DlZ8AIkoATbqAtqtqibWUszhvakHZiytPNduTU7_Hb)
_Copie du token pour le test_

Une fois que nous avons le token, nous pouvons modifier notre requête curl en conséquence :

```shell
~ curl -i -H "Authorization: bearer [ACCESS_TOKEN]"  http://localhost:5000/user
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 22
Server: Werkzeug/2.0.1 Python/3.9.1
Date: Tue, 24 Jan 2023 22:17:06 GMT

{"msg":"Hello user!"}
```

N'oubliez pas de remplacer `[ACCESS_TOKEN]` par la valeur que vous avez copiée du tableau de bord.

Cela fonctionne ! Mais nous avons encore du travail à faire. Même si notre endpoint `/admin` est sécurisé, il peut être accédé par n'importe quel utilisateur :

```shell
~ curl -i -H "Authorization: bearer [ACCESS_TOKEN]"  http://localhost:5000/admin
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 23
Server: Werkzeug/2.0.1 Python/3.9.1
Date: Tue, 24 Jan 2023 22:21:09 GMT

{"msg":"Hello admin!"}
```

### Contrôle d'accès basé sur les rôles

Pour le contrôle d'accès basé sur les rôles, il y a quelques choses que nous devons faire :

1. Créer des permissions pour l'API
2. Activer l'ajout de permissions au JWT pour l'API
3. Mettre à jour le code
4. Tester avec des utilisateurs

Les deux premiers points sont très bien expliqués dans la [documentation Auth0](https://auth0.com/docs/authorization/rbac/auth-core-features?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask), alors assurez-vous d'ajouter les permissions correspondantes à votre API.

Ensuite, nous devons mettre à jour le code. Nous avons besoin d'une fonction pour vérifier si une permission donnée existe dans le token d'accès et retourner `True` si c'est le cas et `False` si ce n'est pas le cas :

```python
def requires_scope(required_scope):
    """
    Détermine si la portée requise est présente dans le token d'accès
    Args:
        required_scope (str): La portée requise pour accéder à la ressource
    """
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("scope"):
            token_scopes = unverified_claims["scope"].split()
            for token_scope in token_scopes:
                if token_scope == required_scope:
                    return True
    return False
```

Et enfin, cela peut être utilisé comme suit :

```python
@app.route("/admin")
@requires_auth
def admin_view():
    """
    Endpoint admin, ne peut être accédé que par un admin
    """
    if requires_scope("read:admin"):
        return jsonify(msg="Hello admin!")

    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)
```

Maintenant, seuls les utilisateurs avec la permission `read:admin` peuvent accéder à notre endpoint admin.

Pour tester votre implémentation finale, vous pouvez suivre les étapes détaillées sur [obtaining an access token](https://auth0.com/docs/quickstart/backend/python/02-using#obtaining-an-access-token?utm_source=freecodecamp&utm_medium=sc&utm_campaign=securing_flask) pour un utilisateur donné.

Vous pouvez également utiliser le tableau de bord Auth0 pour tester les permissions, mais cela est hors du cadre de cet article. Si vous souhaitez en savoir plus, lisez [ici](https://auth0.com/blog/permission-based-security-aspnet-webapi/#Testing-Permissions).

## Conclusion

Aujourd'hui, nous avons appris comment sécuriser une API Flask. Nous avons exploré la voie du "faites-le vous-même", et nous avons construit une API sécurisée avec trois niveaux d'accès – accès public, accès privé et accès privé avec portée.

Il y a tellement plus que Auth0 peut faire pour vos API et aussi pour vos applications clientes. Aujourd'hui, nous avons à peine effleuré la surface, et c'est à vous et à votre équipe, lors de la gestion de scénarios réels, d'explorer tout le potentiel de leurs services.

Le code complet est disponible sur [GitHub](https://gist.github.com/bajcmartinez/5062aa41ccbe2df1bbf4f1a9b95bd085).

Merci d'avoir lu ! Si vous aimez mon style d'enseignement, vous pouvez [vous abonner à ma newsletter hebdomadaire](https://livecodestream.dev/newsletter/) pour les développeurs et les constructeurs et recevoir un e-mail hebdomadaire avec du contenu pertinent.