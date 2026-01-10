---
title: Comment utiliser un service de validation d'email pour l'authentification des
  utilisateurs Flask
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-03-30T22:22:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-email-validation-api-for-flask-user-authentication
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/email-validation-1.png
tags:
- name: authentication
  slug: authentication
- name: email
  slug: email
- name: Flask Framework
  slug: flask
seo_title: Comment utiliser un service de validation d'email pour l'authentification
  des utilisateurs Flask
seo_desc: "In today's digital world, online security is really important, and user\
  \ authentication is a key aspect of it. \nEmail-based authentication is one of the\
  \ most popular and widely used methods for user registration and login. But it's\
  \ not always reliable..."
---

Dans le monde numérique d'aujourd'hui, la sécurité en ligne est vraiment importante, et l'authentification des utilisateurs en est un aspect clé. 

[L'authentification basée sur l'email](https://ashutoshkrris.hashnode.dev/how-to-set-up-email-verification-in-a-flask-app) est l'une des méthodes les plus populaires et largement utilisées pour l'inscription et la connexion des utilisateurs. Mais elle n'est pas toujours fiable, car les utilisateurs peuvent entrer de fausses adresses email ou des adresses invalides lors de l'inscription. Cela peut entraîner des risques de sécurité et des fraudes. C'est là que les services de validation d'email se révèlent utiles.

Dans ce tutoriel, vous allez utiliser le [Service de Validation d'Email](https://emailvalidation.io/) pour vous aider à automatiser votre processus de validation d'email lors de l'inscription des utilisateurs en validant les informations de contact. 

L'API vérifie la syntaxe, le domaine et la boîte aux lettres d'une adresse email, et peut même détecter les emails jetables et risqués. 

En intégrant cette API à votre application, vous pouvez vous assurer que seules les adresses email valides et authentiques sont utilisées pour l'inscription des utilisateurs, ce qui améliorera la sécurité de votre application.

## Prérequis

Avant de commencer le tutoriel, assurez-vous de satisfaire les exigences suivantes :

* Connaissance pratique de Python
* Python 3.8+ installé sur votre système
* Connaissance de base de [Flask](https://ashutoshkrris.hashnode.dev/getting-started-with-flask), des [Flask Blueprints](https://ashutoshkrris.hashnode.dev/how-to-use-blueprints-to-organize-your-flask-apps) et de [Requests](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python).

## Comment configurer l'environnement virtuel

Avant de commencer à coder, vous devrez vous assurer que tous les outils et bibliothèques nécessaires sont installés. Pour garantir un environnement propre et isolé, vous allez créer un environnement virtuel en utilisant `venv`.

Créez un répertoire de projet et naviguez jusqu'à celui-ci dans le terminal :

```bash
mkdir email-validation
cd email-validation

```

Créez un environnement virtuel nommé `env` en utilisant la commande suivante :

```bash
python -m venv env
```

Python est maintenant livré avec la bibliothèque `venv` préinstallée pour créer des environnements virtuels.

Activez l'environnement virtuel comme suit :

```bash
source env/bin/activate
```

Note : Si vous êtes sous Windows, vous devrez utiliser `source env/Scripts/activate` pour activer l'environnement.

Vous devriez voir `(env)` dans votre invite de terminal, indiquant que l'environnement virtuel a été activé.

## Comment fonctionne le service de validation d'email

La validation d'email est un processus essentiel pour toute application web nécessitant une authentification des utilisateurs, et il existe diverses façons de la réaliser. 

Une méthode consiste à utiliser un service de validation d'email tel que [emailvalidation.io](https://emailvalidation.io/). Cette API permet aux développeurs de valider les adresses email en vérifiant si elles sont syntaxiquement correctes, si le domaine existe et si la boîte aux lettres peut recevoir des messages.

L'API propose une gamme de [plans tarifaires](https://emailvalidation.io/pricing/) pour répondre à différents besoins. Le plan gratuit permet aux développeurs de valider jusqu'à 100 emails, ce qui devrait être suffisant pour nos besoins de test. Les plans payants commencent à 9,99 $ par mois et offrent plus de requêtes, plus de fonctionnalités et des temps de réponse plus rapides.

Dans cette section, vous allez écrire une fonction Python qui envoie une requête GET à l'endpoint de l'API et passe l'adresse email à valider en tant que paramètre. 

Pour authentifier la requête API, vous devrez également passer la clé API avec la requête. Avant de continuer, vous devez créer un compte sur emailvalidation.io pour obtenir une clé API. Une fois votre compte créé, vous serez redirigé vers un tableau de bord, similaire à celui montré ci-dessous. La clé API se trouve dans la zone en surbrillance noire.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-29-112311.png)

Pour faire une requête GET, vous devrez installer la bibliothèque `requests` dans votre environnement virtuel :

```bash
pip install requests
```

Ensuite, créez un fichier `test.py` et ajoutez le code suivant :

```python
import requests
from requests.structures import CaseInsensitiveDict


def is_valid(email: str):
    url = f"https://api.emailvalidation.io/v1/info?email={email}"

    headers = CaseInsensitiveDict()
    headers["apikey"] = "votre-cle-api-ici"

    response = requests.get(url, headers=headers)

    return response.json()

    
print(is_valid("support@emailvalidation.io"))
print(is_valid("venip42579@jdsdhak.com"))

```

La fonction `is_valid` prend une adresse email comme argument et construit une URL avec l'adresse email pour appeler l'API emailvalidation.io. La classe `CaseInsensitiveDict` du module `requests.structures` est utilisée pour créer un dictionnaire avec des clés insensibles à la casse afin de définir la clé API dans l'en-tête de la requête. Vous retournez ensuite la réponse JSON de la fonction.

Enfin, vous appelez la fonction `is_valid` deux fois avec différentes adresses email pour démontrer comment la fonction peut valider à la fois une adresse email valide (`support@emailvalidation.io`) et une adresse email invalide (`venip42579@jdsdhak.com`).

Sortie :

```bash
{
   "email":"support@emailvalidation.io",
   "user":"support",
   "tag":"",
   "domain":"emailvalidation.io",
   "smtp_check":true,
   "mx_found":true,
   "did_you_mean":"",
   "role":true,
   "disposable":false,
   "score":0.64,
   "state":"deliverable",
   "reason":"valid_mailbox",
   "free":false,
   "format_valid":true,
   "catch_all":"None"
}
{
   "email":"venip42579@jdsdhak.com",
   "user":"venip42579",
   "tag":"",
   "domain":"jdsdhak.com",
   "smtp_check":false,
   "mx_found":false,
   "did_you_mean":"",
   "role":false,
   "disposable":false,
   "score":0.64,
   "state":"undeliverable",
   "reason":"invalid_mx",
   "free":false,
   "format_valid":true,
   "catch_all":"None"
}
```

Vous pouvez en apprendre davantage sur les différentes clés de la réponse [ici](https://emailvalidation.io/docs/info#sample-response). Pour déterminer si une adresse email est valide ou invalide en fonction de la réponse JSON d'emailvalidation.io, vous devez vérifier les champs suivants :

1. `format_valid` : Si `true`, l'adresse email est correctement formatée. Si `false`, l'adresse email n'est pas valide.
2. `mx_found` : Si `true`, au moins un enregistrement MX a été trouvé pour le domaine. Si `false`, le domaine n'est pas valide.
3. `smtp_check` : Si `true`, l'adresse email a une boîte aux lettres valide. Si `false`, la boîte aux lettres n'est pas valide.
4. `state` : L'état actuel de l'adresse email. Les valeurs peuvent être "deliverable" ou "undeliverable".

Ainsi, vous pouvez modifier la fonction `is_valid` pour qu'elle retourne une réponse booléenne au lieu d'un objet JSON comme suit :

```python
import requests
from requests.structures import CaseInsensitiveDict


def is_valid(email: str):
    url = f"https://api.emailvalidation.io/v1/info?email={email}"

    headers = CaseInsensitiveDict()
    headers["apikey"] = "nUH1hmV24lEwX1TIXmsgRPRRZw0L0NuOeHrdMp78"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_resp = response.json()
        format_valid = json_resp["format_valid"]
        mx_found = json_resp["mx_found"]
        smtp_check = json_resp["smtp_check"]
        state = json_resp["state"]

        return format_valid and mx_found and smtp_check and state == "deliverable"

    return False


print(is_valid("support@emailvalidation.io"))
print(is_valid("venip42579@jdsdhak.com"))

```

Sortie :

```bash
True
False
```

Dans la section suivante, vous allez utiliser cette fonction pour valider les emails lors de l'inscription des utilisateurs.

## Comment configurer l'authentification de base des utilisateurs dans Flask

Dans cette section, vous allez passer en revue les étapes pour configurer l'authentification de base des utilisateurs dans Flask. Vous allez utiliser le code de [l'un de mes articles précédents](https://blog.ashutoshkrris.in/how-to-set-up-basic-user-authentication-in-a-flask-app) où j'avais expliqué comment implémenter l'authentification de base des utilisateurs. 

Vous pouvez commencer par récupérer le code du dépôt GitHub dans le dossier `email-validation` :

```bash
git init
git remote add origin https://github.com/ashutoshkrris/Flask-User-Authentication.git
git pull origin main
```

Note : La commande `git clone [https://github.com/ashutoshkrris/Flask-User-Authentication.git](https://github.com/ashutoshkrris/Flask-User-Authentication.git) .` ne fonctionnera pas dans ce cas car votre répertoire n'est pas vide.

Ensuite, vous verrez un fichier `requirements.txt` qui contient les dépendances pour exécuter l'application dans votre système. Installez les dépendances en utilisant la commande :

```bash
pip install -r requirements.txt
```

Une fois toutes les dépendances installées, vous devrez ajouter les variables d'environnement requises pour le projet. Le projet contient un fichier `.env` qui contient toutes les variables d'environnement. Exécutez la commande suivante pour exporter toutes les variables d'environnement du fichier `.env` :

```bash
source .env
```

Ensuite, vous devez créer la base de données. Comme le projet utilise Flask-Migrate, la création de la base de données est une tâche assez simple en utilisant les commandes suivantes :

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

Maintenant, vous pouvez exécuter l'application en utilisant la commande :

```bash
python manage.py run
```

L'application va commencer à s'exécuter et vous pouvez aller sur `http://localhost:5000/login` dans votre navigateur web pour voir l'application.

Voici une vidéo de démonstration qui montre l'application :

%[https://www.youtube.com/watch?v=XxSESg89xEI]

À l'intérieur de votre projet `flask-validation`, vous aurez un dossier `src` contenant votre code source et un dossier `tests` contenant les tests unitaires. 

En plus de ceux-ci, vous aurez également un fichier `config.py` qui contient les paramètres de configuration de votre application et un fichier `manage.py` qui utilise Flask-CLI pour ajouter différentes commandes pour exécuter et tester votre application. Vous trouverez également d'autres fichiers tels que `.env` et `requirements.txt` que vous connaissez déjà.

Le dossier `src` contient quatre sous-dossiers – `accounts`, `core`, `templates`, et `static`. Les dossiers `templates` et `static` contiennent les fichiers HTML et les fichiers statiques tels que CSS, images et fichiers JavaScript, respectivement. Les deux autres dossiers, `accounts` et `core`, utilisent le concept de [Flask Blueprints](https://blog.ashutoshkrris.in/how-to-use-blueprints-to-organize-your-flask-apps) et contiennent les codes respectifs pour différentes parties de l'application.

Si vous souhaitez en savoir plus sur l'implémentation de votre application Flask, vous pouvez vous référer à [ce tutoriel](https://blog.ashutoshkrris.in/how-to-set-up-basic-user-authentication-in-a-flask-app).

## Comment intégrer le service de validation d'email dans votre application Flask

Jusqu'à présent, il est possible de s'inscrire avec succès dans l'application en utilisant n'importe quelle adresse email, qu'elle soit valide ou non. 

Mais il n'est pas souhaitable d'avoir des adresses email aléatoires ou incorrectes qui encombrent votre base de données. Il est donc judicieux de valider l'adresse email avant d'inscrire l'utilisateur. Si l'adresse email est valide, vous pouvez procéder à l'inscription de l'utilisateur avec succès.

Ajoutez votre clé API de validation d'email dans le fichier `.env` afin de pouvoir la lire sans l'exposer au public :

```
export SECRET_KEY=fdkjshfhjsdfdskfdsfdcbsjdkfdsdf
export DEBUG=True
export APP_SETTINGS=config.DevelopmentConfig
export DATABASE_URL=sqlite:///db.sqlite
export FLASK_APP=src
export FLASK_DEBUG=1
export API_KEY=votre-cle-api-ici
```

Remplacez `votre-cle-api-ici` par votre clé API correcte. Ensuite, vous devrez à nouveau exécuter la commande suivante pour exporter les variables d'environnement :

```bash
source .env
```

Maintenant, créez un fichier `utils.py` à l'intérieur du sous-dossier `accounts` dans le dossier `src`. Le fichier contiendra la fonction utilitaire pour valider l'email. Ajoutez le code suivant dans le fichier :

```python
import requests
from requests.structures import CaseInsensitiveDict
from decouple import config


def is_valid(email: str):
    url = f"https://api.emailvalidation.io/v1/info?email={email}"

    headers = CaseInsensitiveDict()
    headers["apikey"] = config("API_KEY")

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_resp = response.json()
        format_valid = json_resp["format_valid"]
        mx_found = json_resp["mx_found"]
        smtp_check = json_resp["smtp_check"]
        state = json_resp["state"]

        return format_valid and mx_found and smtp_check and state == "deliverable"

    return False

```

Comme mentionné précédemment, la fonction `is_valid()` retourne une valeur booléenne indiquant si une adresse email est valide ou non. Il est important de noter que la fonction ne code pas en dur la valeur de la clé API, mais la récupère à partir des variables d'environnement.

Ensuite, dans la classe `RegisterForm` du fichier `forms.py`, vous avez une méthode `validate`. Cette méthode est responsable de la validation des données d'entrée soumises par l'utilisateur lors du processus d'inscription. 

Auparavant, cette méthode vérifiait uniquement si l'email était déjà enregistré et si les mots de passe correspondaient. Mais vous pouvez maintenant ajouter une validation supplémentaire pour vérifier si l'email est valide. Ainsi, la méthode `validate` modifiée ressemble à ceci :

```python
...

from src.accounts.utils import is_valid

...

class RegisterForm(FlaskForm):
	...

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        if not is_valid(self.email.data):
            self.email.errors.append("Email is invalid")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match")
            return False
        return True

```

Dans la méthode `validate`, si `self.email.data` (c'est-à-dire l'adresse email de l'utilisateur) n'est pas valide, vous ajoutez un message d'erreur à la liste `self.email.errors` et retournez `False`, ce qui signifie que les données de l'utilisateur ne sont pas valides.

Maintenant, lorsque vous exécutez l'application et essayez de vous inscrire, vous pouvez voir cela en direct. Voici une démonstration montrant les cas valides et invalides.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Validation-Demo-Made-with-Clipchamp.gif)

## Autres cas d'utilisation d'un service de validation d'email

Outre la validation de l'email d'un utilisateur lors de l'inscription, il existe plusieurs autres cas d'utilisation pour les services de validation d'email. Certains d'entre eux sont :

1. Nettoyage des listes d'emails : vous pouvez utiliser les services de validation d'email pour nettoyer les listes d'emails en supprimant les adresses email invalides, inexistantes ou risquées. Cela peut aider à améliorer la délivrabilité des emails et à s'assurer que vos emails atteignent les destinataires prévus.
2. Prévention des activités frauduleuses : vous pouvez également utiliser les services de validation d'email pour détecter les activités frauduleuses telles que la création de faux comptes ou les commandes frauduleuses. En validant les adresses email associées à ces activités, vous pouvez empêcher de telles activités de se produire.
3. Amélioration des campagnes marketing : ces services peuvent également aider à améliorer la précision et l'efficacité des campagnes de marketing par email. En s'assurant que les adresses email sont valides et actives, les entreprises peuvent augmenter leurs taux de délivrabilité des emails et améliorer les performances globales de leurs campagnes.

Dans l'ensemble, les services de validation d'email peuvent être un outil puissant pour garantir l'exactitude et la validité des données utilisateur, prévenir la fraude et améliorer l'expérience utilisateur.

## Conclusion

Les services de validation d'email sont un outil puissant pour toute application nécessitant la vérification des adresses email des utilisateurs. Il est essentiel de s'assurer que les adresses email sont valides pour prévenir les erreurs et garantir que les données saisies par l'utilisateur sont correctes. 

Dans cet article, vous avez vu comment utiliser l'API [emailvalidation.io](https://emailvalidation.io/) pour valider une adresse email en Python. Vous avez également appris d'autres cas d'utilisation potentiels pour les services de validation d'email, tels que la détection de fraude et le marketing par email. 

En implémentant des services de validation d'email dans votre application, vous pouvez améliorer l'expérience utilisateur et vous assurer que vos données sont exactes et à jour.

### Ressources supplémentaires

* [Comment utiliser les Blueprints pour organiser vos applications Flask](https://blog.ashutoshkrris.in/how-to-use-blueprints-to-organize-your-flask-apps)
* [Comment configurer la vérification par email dans une application Flask](https://blog.ashutoshkrris.in/how-to-set-up-email-verification-in-a-flask-app)
* [Documentation emailvalidation.io](https://emailvalidation.io/docs/)