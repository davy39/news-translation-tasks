---
title: Comment ajouter l'authentification JWT dans FastAPI – Un guide pratique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-07T23:28:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/fcc-fastapi-jwt-auth.png
tags:
- name: authentication
  slug: authentication
- name: FastAPI
  slug: fastapi
- name: JWT
  slug: jwt
- name: Python
  slug: python
seo_title: Comment ajouter l'authentification JWT dans FastAPI – Un guide pratique
seo_desc: 'By Abdullah Adeel

  FastAPI is a modern, fast, battle tested and light-weight web development framework
  written in Python. Other popular options in the space are Django, Flask and Bottle.

  And since it''s new, FastAPI comes with both advantages and disad...'
---

Par Abdullah Adeel

[FastAPI](https://fastapi.tiangolo.com/) est un framework moderne, rapide, testé en conditions réelles et léger pour le développement web, écrit en Python. D'autres options populaires dans ce domaine sont [Django](https://www.djangoproject.com/), [Flask](https://flask.palletsprojects.com/en/2.1.x/) et [Bottle](https://bottlepy.org/docs/dev/).

Et comme il est nouveau, FastAPI présente à la fois des avantages et des inconvénients.

Du côté positif, FastAPI implémente toutes les normes modernes, tirant pleinement parti des fonctionnalités prises en charge par les dernières versions de Python. Il prend en charge l'asynchrone et le typage des hints. Et il est également rapide (d'où le nom FastAPI), non opinionné, robuste et facile à utiliser.

Du côté négatif, FastAPI manque de certaines fonctionnalités complexes comme la gestion des utilisateurs et le panneau d'administration prêts à l'emploi qui sont intégrés avec Django. Le support de la communauté pour FastAPI est bon mais pas aussi important que pour d'autres frameworks qui existent depuis des années et qui disposent de centaines, voire de milliers de projets open-source pour différents cas d'utilisation.

C'était une très brève introduction à FastAPI. Dans cet article, vous apprendrez comment implémenter l'authentification JWT (JSON Web Token) dans FastAPI avec un exemple pratique.

## Installation du projet

Dans cet exemple, je vais utiliser [**replit**](https://replit.com) (un excellent IDE basé sur le web). Alternativement, vous pouvez simplement configurer votre projet FastAPI localement en [suivant la documentation](https://fastapi.tiangolo.com/tutorial/) ou utiliser ce [modèle de démarrage replit](https://replit.com/@abdadeel/FastAPIstarter) en le forkant. Ce modèle a toutes les dépendances requises déjà installées.

Si vous avez configuré le projet sur votre environnement local, voici les dépendances que vous devez installer pour l'authentification JWT (en supposant que vous avez un projet FastAPI en cours d'exécution) :

```shell
pip install "python-jose[cryptography]" "passlib[bcrypt]" python-multipart
```

**NOTE :** Afin de stocker les utilisateurs, je vais utiliser la base de données intégrée de replit. Mais vous pouvez appliquer des opérations similaires si vous utilisez une base de données standard comme PostgreSQL, MongoDB, etc.

Si vous souhaitez voir l'implémentation complète, j'ai [ce tutoriel vidéo complet](https://www.youtube.com/watch?v=G8MsHbCzyZ4&) qui inclut tout ce qu'une application FastAPI prête pour la production pourrait avoir.

%[https://replit.com/@abdadeel/FastAPIwithJWTauth]

## Authentification avec FastAPI

L'authentification en général peut avoir de nombreuses parties mobiles, de la gestion du hachage des mots de passe et de l'attribution de jetons à la validation des jetons à chaque requête.

FastAPI utilise [l'injection de dépendances](https://en.wikipedia.org/wiki/Dependency_injection#:~:text=In%20software%20engineering%2C%20dependency%20injection,leading%20to%20loosely%20coupled%20programs.) (un modèle de conception en ingénierie logicielle) pour gérer les schémas d'authentification. Voici la liste de certaines étapes générales du processus :

* Hachage des mots de passe
* Création et attribution de jetons JWT
* Création d'utilisateurs
* Validation des jetons à chaque requête pour assurer l'authentification

## Hachage des mots de passe

Lors de la création d'un utilisateur avec un nom d'utilisateur et un mot de passe, vous devez hacher les mots de passe avant de les stocker dans la base de données. Voyons comment hacher facilement les mots de passe.

Créez un fichier nommé `utils.py` dans le répertoire `app` et ajoutez la fonction suivante pour hacher les mots de passe des utilisateurs.

```python
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)
```

Nous utilisons `passlib` pour créer le contexte de configuration pour le hachage des mots de passe. Ici, nous le configurons pour utiliser `bcrypt`.

La fonction `get_hashed_password` prend un mot de passe en clair et retourne le hachage pour celui-ci qui peut être stocké en toute sécurité dans la base de données. La fonction `verify_password` prend les mots de passe en clair et hachés et retourne un booléen indiquant si les mots de passe correspondent ou non.

## Comment générer des jetons JWT

Dans cette section, nous allons écrire deux fonctions auxiliaires pour générer des jetons d'accès et de rafraîchissement avec une charge utile particulière. Plus tard, nous pourrons utiliser ces fonctions pour générer des jetons pour un utilisateur particulier en passant la charge utile liée à l'utilisateur.

À l'intérieur du fichier `app/utils.py` que vous avez créé précédemment, ajoutez les instructions d'importation suivantes :

```python
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt
```

Ajoutez les constantes suivantes qui seront passées lors de la création des JWT :

```python
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 jours
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # doit être gardé secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']    # doit être gardé secret
```

`JWT_SECRET_KEY` et `JWT_REFRESH_SECRET_KEY` peuvent être n'importe quelles chaînes, mais assurez-vous de les garder secrètes et de les définir comme variables d'environnement.

Si vous suivez ce tutoriel sur replit.com, vous pouvez définir ces variables d'environnement à partir de l'onglet `Secrets` dans la barre de menu de gauche.

Ajoutez les fonctions suivantes à la fin du fichier `app/utils.py` :

```python
def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
```

La seule différence entre ces deux fonctions est que le temps d'expiration pour les jetons de rafraîchissement est plus long que pour les jetons d'accès.

Les fonctions prennent simplement la charge utile à inclure dans le JWT, qui peut être n'importe quoi. Habituellement, vous voudrez stocker des informations comme USER_ID ici, mais cela peut être n'importe quoi, des chaînes aux objets/dictionnaires. Les fonctions retournent les jetons sous forme de chaînes.

À la fin, votre fichier `app/utils.py` devrait ressembler à ceci :

```python
from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 jours
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']     # doit être gardé secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']      # doit être gardé secret

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
```

## Comment gérer les inscriptions des utilisateurs

À l'intérieur du fichier `app/app.py`, créez un autre endpoint pour gérer les inscriptions des utilisateurs. L'endpoint doit prendre l'email/nom d'utilisateur et le mot de passe comme données. Il vérifie ensuite pour s'assurer qu'un autre compte avec le même email/nom d'utilisateur n'existe pas. Ensuite, il crée l'utilisateur et le sauvegarde dans la base de données.

Dans `app/app.py`, ajoutez la fonction de gestion suivante :

```
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
from app.schemas import UserOut, UserAuth
from replit import db
from app.utils import get_hashed_password
from uuid import uuid4

@app.post('/signup', summary="Créer un nouvel utilisateur", response_model=UserOut)
async def create_user(data: UserAuth):
    # interrogation de la base de données pour vérifier si l'utilisateur existe déjà
    user = db.get(data.email, None)
    if user is not None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Un utilisateur avec cet email existe déjà"
        )
    user = {
        'email': data.email,
        'password': get_hashed_password(data.password),
        'id': str(uuid4())
    }
    db[data.email] = user    # sauvegarde de l'utilisateur dans la base de données
    return user
```

## Comment gérer les connexions

FastAPI a une méthode standard pour gérer les connexions afin de se conformer aux normes OpenAPI. Cela ajoute automatiquement l'authentification dans les documents swagger sans aucune configuration supplémentaire.

Ajoutez la fonction de gestion suivante pour les connexions des utilisateurs et attribuez à chaque utilisateur des jetons d'accès et de rafraîchissement. N'oubliez pas d'inclure les imports.

```python
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from app.schemas import UserOut, UserAuth, TokenSchema
from replit import db
from app.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)
from uuid import uuid4

@app.post('/login', summary="Créer des jetons d'accès et de rafraîchissement pour l'utilisateur", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.get(form_data.username, None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email ou mot de passe incorrect"
        )

    hashed_pass = user['password']
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email ou mot de passe incorrect"
        )
    
    return {
        "access_token": create_access_token(user['email']),
        "refresh_token": create_refresh_token(user['email']),
    }
```

Cet endpoint est un peu différent des autres endpoints post où vous avez défini le schéma pour filtrer les données entrantes.

Pour les endpoints de connexion, nous utilisons `OAuth2PasswordRequestForm` comme dépendance. Cela garantira l'extraction des données de la requête et les passera comme argument `form_data` à la fonction de gestion `login`. `python-multipart` est utilisé pour extraire les données du formulaire. Assurez-vous donc de l'avoir installé.

L'endpoint sera reflété dans les documents swagger avec des entrées pour le nom d'utilisateur et le mot de passe.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-49.png)

En cas de réponse réussie, vous obtiendrez des jetons comme montré ici :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-50.png)

## Comment ajouter des routes protégées

Maintenant que nous avons ajouté la prise en charge de la connexion et de l'inscription, nous pouvons ajouter des endpoints protégés. Dans FastAPI, les endpoints protégés sont gérés en utilisant l'injection de dépendances et FastAPI peut l'inférer à partir du schéma OpenAPI et le refléter dans les documents swagger.

Voyons la puissance de l'injection de dépendances. À ce stade, il n'y a aucun moyen de s'authentifier à partir des documents. Cela est dû au fait que nous n'avons actuellement aucun endpoint protégé, donc le schéma OpenAPI ne dispose pas de suffisamment d'informations sur la stratégie de connexion que nous utilisons.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-51.png)
_Aucun bouton dans les documents swagger pour se connecter._

Créons notre dépendance personnalisée. Ce n'est rien d'autre qu'une fonction qui est exécutée avant la fonction de gestion réelle pour obtenir les arguments passés à la fonction de gestion. Voyons avec un exemple pratique.

Créez un autre fichier `app/deps.py` et incluez la fonction suivante :

```python
from typing import Union, Any
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .utils import (
    ALGORITHM,
    JWT_SECRET_KEY
)

from jose import jwt
from pydantic import ValidationError
from app.schemas import TokenPayload, SystemUser
from replit import db

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(reuseable_oauth)) -> SystemUser:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Jeton expiré",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Impossible de valider les identifiants",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    user: Union[dict[str, Any], None] = db.get(token_data.sub, None)
    
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Impossible de trouver l'utilisateur",
        )
    
    return SystemUser(**user)
```

Ici, nous définissons la fonction `get_current_user` comme une dépendance qui, à son tour, prend une instance de `OAuth2PasswordBearer` comme dépendance.

```python
reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)
```

`OAuth2PasswordBearer` prend deux paramètres obligatoires. `tokenUrl` est l'URL dans votre application qui gère la connexion de l'utilisateur et retourne les jetons. `scheme_name` défini sur `JWT` permettra aux documents swagger frontend d'appeler `tokenUrl` depuis le frontend et de sauvegarder les jetons en mémoire. Ensuite, chaque requête ultérieure aux endpoints protégés aura le jeton envoyé comme en-têtes `Authorization` afin que `OAuth2PasswordBearer` puisse le parser.

Maintenant, ajoutons un endpoint protégé qui retourne les informations du compte utilisateur comme réponse. Pour cela, un utilisateur doit être connecté et l'endpoint répondra avec les informations de l'utilisateur actuellement connecté.

Dans `app/app.py`, créez une autre fonction de gestion. Assurez-vous d'inclure les imports également.

```python
from app.deps import get_current_user

@app.get('/me', summary='Obtenir les détails de l\'utilisateur actuellement connecté', response_model=UserOut)
async def get_me(user: User = Depends(get_current_user)):
    return user
```

Dès que vous ajoutez cet endpoint, vous pourrez voir le bouton `Authorize` dans les documents swagger et une icône 🔑 devant l'endpoint protégé `/me`.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-56.png)

C'est la puissance de l'injection de dépendances et de la capacité de FastAPI à générer un schéma OpenAPI automatique.

En cliquant sur le bouton `Authorize`, le formulaire d'autorisation s'ouvrira avec les champs requis pour la connexion. En cas de réponse réussie, les jetons seront sauvegardés et envoyés dans les en-têtes des requêtes ultérieures.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-57.png)
_Formulaire de connexion intégré à Swagger_

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-58.png)
_Connecté avec succès_

À ce stade, vous pouvez accéder à tous les endpoints protégés. Pour rendre un endpoint protégé, vous devez simplement ajouter la fonction `get_current_user` comme dépendance. C'est tout ce que vous avez à faire !

## Conclusion

Si vous avez suivi ce tutoriel, vous devriez avoir une application FastAPI fonctionnelle avec authentification JWT. Sinon, vous pouvez toujours exécuter [ce repl](https://replit.com/@abdadeel/FastAPI-with-JWT-authentication) et jouer avec ou visiter [cette version déployée](https://fastapi-with-jwt-authentication.abdadeel.repl.co/docs). Vous pouvez trouver le code GitHub pour ce projet [ici](https://github.com/mabdullahadeel/fcc-fastapi-jwt).

Si vous avez trouvé cet article utile, suivez-moi sur [twitter](https://twitter.com/abdadeel_) [@abdadeel_](https://twitter.com/abdadeel_). Et n'oubliez pas que vous pouvez toujours regarder [cette vidéo](https://www.youtube.com/watch?v=G8MsHbCzyZ4&ab_channel=ABDLogs) pour une explication détaillée avec un exemple pratique.

Merci ;)