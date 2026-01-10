---
title: Comment implémenter l'injection de dépendances dans FastAPI
subtitle: ''
author: Nneoma Uche
co_authors: []
series: null
date: '2025-11-14T14:46:01.279Z'
originalURL: https://freecodecamp.org/news/how-to-implement-dependency-injection-in-fastapi
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1763131442081/76eff35b-be68-49c1-9743-d78ebc87b292.png
tags:
- name: dependency injection
  slug: dependency-injection
- name: FastAPI
  slug: fastapi
- name: backend
  slug: backend
- name: Python
  slug: python
seo_title: Comment implémenter l'injection de dépendances dans FastAPI
seo_desc: 'Several languages and frameworks depend on dependency injection—no pun
  intended. Go, Angular, NestJS, and Python''s FastAPI all use it as a core pattern.

  If you''ve been working with FastAPI, you''ve likely encountered dependencies in
  action. Perhaps yo...'
---


Plusieurs langages et frameworks dépendent de l'injection de dépendances — sans mauvais jeu de mots. Go, Angular, NestJS et FastAPI de Python l'utilisent tous comme un pattern central.

Si vous avez travaillé avec FastAPI, vous avez probablement déjà rencontré des dépendances en action. Vous avez peut-être vu `Depends()` dans un tutoriel ou dans la documentation et avez été confus pendant un moment. Ce fut certainement mon cas. Cette confusion a déclenché des semaines d'expérimentation avec ce système. La vérité est qu'on ne peut pas éviter l'injection de dépendances lors de la construction de services backend avec FastAPI. Elle est ancrée dans l'ADN du Framework, alimentant tout, de l'authentification et des connexions aux bases de données jusqu'à la validation des requêtes.

La documentation de FastAPI décrit son système d'injection de dépendances comme étant « puissant mais intuitif ». C'est exact, une fois que l'on comprend comment il fonctionne. Cet article le décortique, couvrant les dépendances de fonction, les dépendances de classe, les portées des dépendances, ainsi que des exemples pratiques.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Dépendances et injection de dépendances dans FastAPI](#heading-dependances-et-injection-de-dependances-dans-fastapi)
    
* [Prise en main : Configuration de l'environnement](#heading-prise-en-main-configuration-de-lenvironnement)
    
* [Types de dépendances dans FastAPI](#heading-types-de-dependances-dans-fastapi)
    
    * [Comment utiliser les dépendances de fonction dans FastAPI](#heading-comment-utiliser-les-dependances-de-fonction-dans-fastapi)
        
    * [Comment utiliser les dépendances de classe dans FastAPI](#heading-comment-utiliser-les-dependances-de-classe-dans-fastapi)
        
* [Portée des dépendances](#heading-portee-des-dependances)
    
    * [Niveau de l'opération de chemin](#heading-niveau-de-loperation-de-chemin)
        
    * [Niveau du routeur](#heading-niveau-du-routeur)
        
    * [Niveau de l'application](#heading-niveau-de-lapplication)
        
* [Cas d'utilisation courants pour l'injection de dépendances](#heading-cas-dutilisation-courants-pour-linjection-de-dependances)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre cet article, vous devriez avoir :

* Une connaissance pratique de Python.
    
* La capacité de créer et d'activer des environnements virtuels.
    
* Une compréhension de base de FastAPI.
    
* Une familiarité avec les concepts de la Programmation Orientée Objet (POO).
    

## Dépendances et injection de dépendances dans FastAPI

Une dépendance est un morceau de logique réutilisable, comme l'authentification, une connexion à une base de données ou une validation, dont vos opérations de chemin ont besoin. L'injection de dépendances (DI) est la manière dont FastAPI fournit ces dépendances à des parties spécifiques de votre application : vous les déclarez en utilisant `Depends()` et FastAPI les exécute automatiquement lorsque la route associée reçoit une requête.

Pensez-y comme si vous demandiez les outils dont votre application a besoin. Vous déclarez les dépendances une fois et FastAPI les fournit partout où elles sont nécessaires, sans configuration répétitive à travers les routes.

Cela permet de créer des applications modulaires et évolutives. Sans DI, vous devriez répéter le même code de configuration sur chaque point de terminaison, ce qui rendrait les mises à jour fastidieuses et les bugs plus probables.

## Prise en main : Configuration de l'environnement

Configurons votre environnement de développement pour travailler sur les exemples de ce guide.

Commencez par créer un dossier de projet, puis :

Créez et activez un environnement virtuel :

```bash
python -m venv deps
source deps/bin/activate          # sur Mac
deps\Scripts\activate             # sur Windows
```

Installez FastAPI avec toutes les dépendances :

```python
pip install 'fastapi[all]'
```

Organisez votre projet comme suit :

```python
fastapi-deps/
├── deps/                 # Environnement virtuel
├── function_deps.py
├── class_deps.py
├── router_deps.py
├── app.py
└── requirements.txt
```

## Types de dépendances dans FastAPI

Dans FastAPI, une dépendance est un objet callable qui récupère ou vérifie des informations avant l'exécution d'une route. Les dépendances peuvent être implémentées sous forme de fonctions ou de classes.

Les **dépendances de fonction** sont l'approche la plus simple et fonctionnent bien pour la plupart des cas d'utilisation, y compris la validation, l'authentification et la récupération de données. Les **dépendances de classe** peuvent gérer les mêmes tâches mais sont particulièrement utiles lorsque vous avez besoin d'une logique avec état, de plusieurs instances avec des configurations différentes, ou si vous préférez les patterns orientés objet.

### Comment utiliser les dépendances de fonction dans FastAPI

Une dépendance de fonction est une fonction utilitaire (par exemple pour l'authentification ou la récupération de données) qui peut être injectée dans les opérations de chemin. Pour illustrer cela, nous allons créer une dépendance simple d'authentification d'utilisateur utilisant une base de données en mémoire — une liste de dictionnaires.

Vous vous souvenez de la structure des dossiers de tout à l'heure ? Nous allons écrire ce code dans `fastapi-deps/function_deps.py`.

Commencez par importer les modules requis :

```python
from fastapi import FastAPI, Depends, HTTPException
import uvicorn
```

Vous importez `FastAPI` pour créer l'instance de l'application, `Depends` pour l'injection de dépendances, et `HTTPException` pour gérer les erreurs avec élégance. `uvicorn` sera utilisé pour lancer l'application plus tard.

Ensuite, instanciez l'application FastAPI :

```python
app = FastAPI()
```

`app = FastAPI()` crée votre instance d'application : l'objet qui contiendra tous vos points de terminaison et dépendances.

Ensuite, créez une base de données en mémoire. Définissez une liste de dictionnaires pour agir comme votre base de données temporaire. Chaque dictionnaire représente une entrée utilisateur contenant un nom et un mot de passe.

```python
users = [
    {"name": "Ore", "password": "jkzvdgwya12"},
    {"name": "Uche", "password": "lga546"},
    {"name": "Seke", "password": "SK99!"},
    {"name": "Afi", "password": "Afi@144"},
    {"name": "Sam", "password": "goTiger72*"},
    {"name": "Ozi", "password": "xx%hI"},
    {"name": "Ella", "password": "Opecluv18"},
    {"name": "Claire", "password": "cBoss@14G"},
    {"name": "Sena", "password": "SenDaBoss5"},
    {"name": "Ify", "password": "184Norab"}  
]
```

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Ce type de base de données n'est pas persistant ; toutes les données stockées sont perdues lors du redémarrage de l'application.</div>
</div>

Ensuite, définissez une fonction de dépendance pour la validation de l'utilisateur. La fonction utilitaire simple ci-dessous vérifie si un nom d'utilisateur et un mot de passe fournis par l'utilisateur correspondent à un utilisateur existant dans la base de données.

```python
# la fonction de dépendance
def user_dep(name: str, password: str):
    for u in users:
        if u["name"] == name and u["password"] == password:
            return {"name": name, "valid": True}
```

Cette fonction attend deux paramètres de type chaîne, `name` et `password`, provenant de la requête entrante. Si elle trouve une correspondance dans la base de données `users`, elle retourne un dictionnaire confirmant la validité de l'utilisateur. FastAPI convertit automatiquement ce dictionnaire en une réponse JSON.

Ensuite, injectez la dépendance dans une fonction de chemin :

```python
# le point de terminaison web
@app.get("/users/{user}")
def get_user(user = Depends(user_dep)) -> dict:
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return user
```

La fonction `user_dep` est injectée dans l'opération de chemin en utilisant `Depends()`. Lorsqu'une requête HTTP est faite à ce point de terminaison, FastAPI exécute d'abord la dépendance, valide l'entrée et passe sa valeur de retour au paramètre `user`.

L'annotation `-> dict:` indique que la fonction retourne un dictionnaire, que FastAPI convertit automatiquement en JSON. Si aucun enregistrement correspondant n'est trouvé, une `HTTPException` avec un code d'état 401 est levée ; sinon, les données de l'utilisateur vérifié sont renvoyées.

Maintenant, vous allez démarrer le serveur FastAPI. Pour lancer le serveur, ouvrez votre terminal dans le répertoire du projet et exécutez :

```python
uvicorn function_deps:app --reload
```

* `function_deps` est le nom de votre fichier Python (sans l'extension **.py**).
    
* `--reload` redémarre automatiquement le serveur chaque fois que vous enregistrez des modifications.
    

Une fois lancé, vous verrez une sortie similaire à l'image ci-dessous :

![sortie uvicorn dans le terminal](https://cdn.hashnode.com/res/hashnode/image/upload/v1762651145390/479b187c-f455-4617-aa7f-e075bf668ee5.jpeg align="center")

Vous pouvez maintenant tester le point de terminaison. Ouvrez votre navigateur ou l'application Postman pour valider l'utilisateur **"Seke"**. Collez cette URL dans votre navigateur : *http://127.0.0.1:8000/users/{user}?name=Seke&password=SK99!*

Alternativement, vous pouvez tester le point de terminaison en utilisant la documentation intégrée de FastAPI à l'adresse : http://127.0.0.1:8000/docs

Dans l'interface Swagger UI :

* Cliquez sur le point de terminaison **Get User**
    
* Cliquez sur **Try it out**
    
* Entrez « Seke » dans le champ name et « SK99! » dans le champ password
    
* Cliquez sur **Execute**
    

Vous devriez obtenir un code d'état 200, avec le contenu présent dans cette image :

![payload pour le point de terminaison get_user](https://cdn.hashnode.com/res/hashnode/image/upload/v1762651845087/9495107e-1ab8-4349-a701-04e5de461fb6.jpeg align="center")

Vous pouvez également tester le point de terminaison avec des noms d'utilisateur ou des mots de passe qui n'existent pas dans la base de données. À chaque fois, vous devriez voir une erreur **401** comme ceci :

![erreur non autorisé dans la doc FastAPI](https://cdn.hashnode.com/res/hashnode/image/upload/v1762652045213/c8dc8bb1-e2c4-456f-92f5-911dddae73eb.jpeg align="center")

### Comment utiliser les dépendances de classe dans FastAPI

Bien que les fonctions soient le moyen le plus courant de définir des dépendances, FastAPI prend également en charge les dépendances basées sur des classes. Les classes sont utiles lorsque vous avez besoin d'instances réutilisables avec un état configurable ou si vous préférez les patterns orientés objet.

Les dépendances de classe s'injectent de la même manière : via la fonction `Depends` dans votre opération de chemin.

Convertissons la dépendance de fonction `user_dep` en une classe. Elle authentifiera les utilisateurs, accordera l'accès aux identifiants valides et lèvera des exceptions pour les tentatives non autorisées. Nous l'appliquerons à un point de terminaison de tableau de bord utilisateur pour garantir que seuls les utilisateurs authentifiés accèdent à leurs ressources.

```python
# Classe de dépendance pour l'authentification utilisateur
class UserAuth():
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

    def __call__(self):
        # vérifier si le nom et le mot de passe saisis correspondent à une ligne dans la db
        for user in users:
            if user["name"] == self.name and user["password"] == self.password:
                return
        # Si aucune correspondance n'est trouvée, lever une erreur
        raise HTTPException(status_code=401, detail="Invalid username or password")
```

La méthode `__init__` reçoit les paramètres de la requête (`name` et `password`) et les stocke comme attributs d'instance. Ceux-ci peuvent ensuite être consultés dans la méthode `__call__`, qui contient la logique de la dépendance.

Notez que `__call__` ne retourne pas de valeur dans cet exemple. Elle lève simplement une `HTTPException` si l'authentification échoue. La méthode `__call__` rend l'instance de la classe callable, permettant à FastAPI de l'invoquer comme une fonction régulière.

Voici comment injecter `UserAuth` dans une fonction de chemin :

```python
# Injection de la dépendance de classe dans une opération de chemin
@app.get("/user/dashboard")
def get_dashboard(user: UserAuth = Depends(UserAuth)):
    return {"message": f"Access granted to {user.name}"}
```

**Ce qui se passe ici :**

Lorsqu'un client appelle le point de terminaison `/user/dashboard`, FastAPI exécute d'abord la dépendance. Reconnaissant `UserAuth` comme une classe, FastAPI crée automatiquement une instance et la remplit avec les valeurs des paramètres de requête.

Voici le flux d'exécution pour vous aider à comprendre :

* `Depends(UserAuth)` dit à FastAPI : « Avant d'exécuter cette route, crée une instance de `UserAuth`. »
    
* FastAPI extrait le nom et le mot de passe de l'URL de la requête (par exemple, */user/dashboard?name=Seke&password=SK99!*).
    
* Il appelle ensuite `UserAuth(name="Seke", password="SK99!")` pour créer l'instance.
    

* L'instance `UserAuth`, avec ses attributs name et password stockés, est passée au paramètre `user` dans `get_dashboard`.
    
* La fonction de route peut accéder directement à `user.name` et `user.password`.
    
* Si `__call__` lève une exception, la route n'est jamais exécutée.
    

Testez le point de terminaison avec des identifiants valides de la liste des utilisateurs, et vous devriez voir un résultat comme celui-ci :

![sortie dépendance de classe](https://cdn.hashnode.com/res/hashnode/image/upload/v1762655384549/ac5ab413-0f75-4711-8166-4c99bcca9d7c.jpeg align="center")

Un regard plus attentif sur la [documentation officielle de FastAPI](https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/#use-it) propose une approche alternative pour les classes en tant que dépendances. Cependant, l'utilisation de la méthode `__call__` est, à mon avis, l'approche la plus simple et la plus autonome. Elle garde votre logique d'authentification modulaire sans ajouter de code supplémentaire à l'opération de chemin.

Le compromis est que les dépendances de classe sont plus verbeuses que les fonctions utilitaires, mais plus propres pour une logique complexe.

## Portée des dépendances

FastAPI offre deux façons d'injecter des dépendances dans une opération de chemin : en tant que **paramètre de fonction** ou via le **décorateur de chemin**. Lorsque vous incluez une dépendance en tant que paramètre de fonction, la valeur de retour de la dépendance est disponible dans la fonction. Mais lorsqu'elle est injectée dans le décorateur, la dépendance s'exécute sans passer de valeur de retour à la fonction de chemin.

Au-delà des points de terminaison uniques, FastAPI vous permet d'injecter des dépendances au niveau du routeur ou au niveau global. Examinons ces portées plus en détail.

### Niveau de l'opération de chemin

Alors que le premier exemple injectait des dépendances dans les paramètres de la fonction de chemin, vous pouvez également les injecter directement dans le décorateur en utilisant le paramètre `dependencies`. Cette approche est utile pour les effets secondaires (par exemple, les gardes d'authentification, la limitation de débit ou la journalisation des requêtes) où les données de retour ne sont pas requises dans l'opération de chemin.

Remplacez le code précédent dans `fastapi-deps/function_deps.py` par celui-ci :

```python
# fonction dep à passer dans le décorateur
def user_dep(name: str, password: str):
    for u in users:
        if u["name"] == name and u["password"] == password:
            return
    raise HTTPException(status_code=401, detail="Invalid username or password")
       
# fonction de chemin
@app.get("/users/{user}", dependencies=[Depends(user_dep)])
def get_user() -> dict:
    return {"message" : "Access granted!"}
```

Cette dépendance basée sur le décorateur agit comme une pré-vérification avant l'exécution du point de terminaison. Elle valide les identifiants sans passer de valeurs à la fonction de chemin. En cas d'échec de l'authentification, FastAPI lève une HTTPException et empêche l'opération de chemin de s'exécuter.

Si vous testez cela en utilisant un nom et un mot de passe valides de la base de données en mémoire, votre sortie devrait ressembler à ceci :

![sortie dépendance décorateur de chemin](https://cdn.hashnode.com/res/hashnode/image/upload/v1762656537394/06fc80cf-a8b2-44d2-8955-ec914be699ba.jpeg align="center")

### Niveau du routeur

L'injection de dépendances au niveau du routeur permet à plusieurs points de terminaison de partager une logique commune sans répéter la dépendance dans chaque route.

Nous utiliserons la même fonction `user_dep` mais nous l'injecterons au niveau du routeur. Ajoutez ces imports à `fastapi-deps/router_deps.py` :

```python
from fastapi import APIRouter, Depends

# importer la fonction de dépendance
from function_deps import user_dep
```

Ensuite, créez une instance d' `APIRouter`, en passant votre dépendance au paramètre `dependencies`. Cela fait en sorte que la dépendance s'exécute automatiquement pour chaque route que vous définissez sous ce routeur.

Dans cet exemple, `user_dep` s'exécute avant `get_user()` et tout autre point de terminaison que vous ajoutez au routeur, éliminant ainsi le besoin de la déclarer sur chaque route.

```python
router = APIRouter(prefix="/users", dependencies=[Depends(user_dep)])

# définir les routes avec ou sans dépendances supplémentaires
@router.get("/{user}")
def get_user() -> dict:
    return {"message" : "Access granted!"}
```

Dans votre fichier d'application principal (`app.py`), importez le routeur et enregistrez-le auprès de votre application FastAPI en utilisant `include_router()`. Cela rend toutes les routes définies dans le routeur accessibles via votre application.

```python
from fastapi import FastAPI
import uvicorn
from router_deps import router as user_router

app = FastAPI()
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
```

Démarrez votre serveur et testez la route en utilisant une paire nom-mot de passe valide de la liste des utilisateurs, puis essayez-en une qui ne correspond pas. Vous devriez obtenir un statut **200** pour les identifiants corrects et **401** pour les invalides.

### Niveau de l'application

Les dépendances au niveau de l'application (également appelées *dépendances globales*) sont définies lors de l'instanciation de l'application FastAPI et s'appliquent à chaque route de votre application. Contrairement aux dépendances au niveau du routeur qui ciblent des groupes de points de terminaison spécifiques, les dépendances au niveau de l'application s'étendent à toute l'application. Toute dépendance injectée dans l'objet application FastAPI s'exécutera automatiquement pour toutes les fonctions de chemin.

Injectons une simple dépendance de *logging* aux côtés de la dépendance d' *authentification utilisateur* que nous avons utilisée tout au long de cet article.

Mettez à jour `fastapi-deps/app.py` avec ce code :

```python
from fastapi import FastAPI, Depends
import uvicorn
from function_deps import user_dep
from router_deps import router as user_router
from datetime import datetime

# Dépendance de logging basique
def log_request():
    print(f"[{datetime.now()}] Request received.")

app = FastAPI(dependencies=[Depends(log_request), Depends(user_dep)])
app.include_router(user_router)

@app.get("/home")
def get_main():
    return "Welcome back!!!"


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
```

Lorsque vous envoyez une requête à n'importe quel point de terminaison de cette application, `log_request` l'accuse réception et affiche l'heure à laquelle la requête a été faite. Comme nous n'envoyons pas les logs vers une base de données particulière, ils seront simplement affichés dans le terminal (ou la console) comme ceci :

![sortie dépendance logging dans la console](https://cdn.hashnode.com/res/hashnode/image/upload/v1762673203094/d1c43e1b-0cc2-46e5-ae54-ee4849d1af66.jpeg align="center")

Appelez le point de terminaison avec des identifiants valides en utilisant votre navigateur, cURL, Postman ou l'interface Swagger UI. Vous devriez obtenir cette réponse :

![Réponse du serveur pour la requête API vers la page d'accueil](https://cdn.hashnode.com/res/hashnode/image/upload/v1762673465276/28d90221-4feb-4467-8c6c-8557dd54de03.jpeg align="center")

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Bien que la même logique d'authentification et de journalisation s'applique à tous les routeurs enregistrés, le message spécifique que les utilisateurs voient dépend de ce que vous programmez dans chaque routeur.</div>
</div>

## Cas d'utilisation courants pour l'injection de dépendances

L'injection de dépendances résout plusieurs défis courants dans le développement d'API. Voici les cas d'utilisation les plus fréquents où vous appliquerez ce pattern.

1. **Connexions aux bases de données :** La réutilisation de la logique de connexion sur plusieurs points de terminaison évite les fuites de connexion et garantit que chaque requête dispose d'une session isolée.
    
2. **Authentification et autorisation :** Les dépendances aident à valider les jetons et à vérifier les rôles des utilisateurs sur les routes protégées.
    
3. **Journalisation et surveillance (Logging & Monitoring) :** Une dépendance de journalisation peut enregistrer automatiquement chaque requête dans votre système de surveillance ou votre base de données. C'est bénéfique pour le débogage et le suivi de l'utilisation de l'API.
    
4. **Limitation de débit (Rate Limiting) :** Vous pouvez contrôler la fréquence des requêtes et prévenir les abus de l'API en injectant une logique de limitation de débit dans les fonctions de chemin.
    
5. **Configuration et paramètres :** Le système d'injection de dépendances de FastAPI simplifie la gestion de la configuration en vous permettant d'injecter des paramètres tels que des clés API ou des variables d'environnement partout où cela est nécessaire, gardant votre code cohérent.
    
6. **Pagination et filtrage :** L'injection de paramètres communs comme `page_size` et `limit` standardise les patterns de récupération de données à travers les points de terminaison.
    

## **Conclusion**

Le système d'injection de dépendances de FastAPI vous aide à gérer efficacement la logique et les ressources partagées tout en respectant les principes *DRY* (Don't Repeat Yourself). Cependant, savoir quand injecter une dépendance et quand s'en passer est une compétence qui s'acquiert avec la pratique.

L'injection de dépendances n'est pas nécessaire pour une logique simple et autonome. Mais pour les ressources nécessitant une gestion du cycle de vie, une logique partagée ou de la modularité, le système d'injection de dépendances de FastAPI simplifie les vérifications et les opérations de l'application — avec ou sans valeurs de retour.