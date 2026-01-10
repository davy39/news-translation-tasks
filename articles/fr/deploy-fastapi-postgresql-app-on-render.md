---
title: 'Comment déployer votre application FastAPI + PostgreSQL sur Render : Un guide
  pour débutants'
subtitle: ''
author: Preston Osoro
co_authors: []
series: null
date: '2025-05-22T15:55:44.932Z'
originalURL: https://freecodecamp.org/news/deploy-fastapi-postgresql-app-on-render
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747923566699/58fc1283-d2f5-4964-acfa-b5dcad0f3d4f.png
tags:
- name: PostgreSQL
  slug: postgresql
- name: render.com
  slug: rendercom
- name: FastAPI
  slug: fastapi
seo_title: 'Comment déployer votre application FastAPI + PostgreSQL sur Render : Un
  guide pour débutants'
seo_desc: "This guide is a comprehensive roadmap for deploying a FastAPI backend connected\
  \ to a PostgreSQL database using Render, a cloud platform that supports hosting\
  \ Python web apps and managed PostgreSQL databases.  \nYou can find the complete\
  \ source code he..."
---

Ce guide est une feuille de route complète pour déployer un backend FastAPI connecté à une base de données PostgreSQL en utilisant [Render](https://render.com/), une plateforme cloud qui prend en charge l'hébergement d'applications web Python et de bases de données PostgreSQL gérées.  
  
Vous pouvez trouver le code source complet [ici](https://github.com/preston-56/FastAPI).

## Contexte de déploiement

Lors du déploiement d'une application FastAPI connectée à PostgreSQL, vous devez choisir une plateforme qui prend en charge les applications web Python et les bases de données gérées. Ce guide utilise Render comme plateforme d'exemple car elle fournit à la fois l'hébergement web et un service de base de données PostgreSQL dans un seul environnement, ce qui facilite la connexion de votre backend à la base de données.

Vous pouvez appliquer les concepts ici à d'autres fournisseurs cloud, mais les étapes différeront en fonction des spécificités de la plateforme.

### Voici ce que nous allons couvrir :

1. [Structure du projet pour une application FastAPI réelle](#heading-structure-du-projet)
    
2. [Ce dont vous aurez besoin avant de commencer](#heading-ce-dont-vous-aurez-besoin-avant-de-commencer)
    
3. [Étapes de déploiement](#heading-etapes-de-deploiement)
    
    * [Étape 1 : Configurer la base de données PostgreSQL locale](#heading-etape-1-configurer-la-base-de-donnees-postgresql-locale)
        
    * [Étape 2 : Configurer votre connexion à la base de données](#heading-etape-2-configurer-votre-connexion-a-la-base-de-donnees)
        
    * [Étape 3 : Configurer votre application principale FastAPI](#heading-etape-3-configurer-votre-application-principale-fastapi)
        
    * [Étape 4 : Créer un fichier de dépendances](#heading-etape-4-creer-un-fichier-de-dependances)
        
    * [Étape 5 : Approvisionner une base de données PostgreSQL sur Render](#heading-etape-5-approvisionner-une-base-de-donnees-postgresql-sur-render)
        
    * [Étape 6 : Déployer votre application FastAPI sur Render](#heading-etape-6-deployer-votre-application-fastapi-sur-render)
        
    * [Étape 7 : Tester vos points de terminaison API](#heading-etape-7-tester-vos-points-de-terminaison-api)
        
4. [Flux de travail de développement local](#heading-flux-de-travail-de-developpement-local)
    
5. [Bonnes pratiques et conseils de dépannage](#heading-bonnes-pratiques-et-conseils)
    
6. [Problèmes courants et solutions](#heading-problemes-courants-et-solutions)
    
7. [Conclusion](#heading-conclusion)
    

## Structure du projet

Si vous construisez une API réelle avec [FastAPI](https://fastapi.tiangolo.com/), vous dépasserez rapidement un seul fichier `main.py`. C'est alors qu'une structure de projet modulaire devient essentielle pour la maintenabilité.

Voici un exemple de structure que nous utiliserons tout au long de ce guide :

```python
FastAPI/
├── database/
│   ├── base.py
│   ├── database.py
│   └── __init__.py
├── fastapi_app/
│   └── main.py
├── items/
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── item.py
│   └── schemas/
│       ├── __init__.py
│       └── item.py
├── models/
│   └── __init__.py
├── orders/
│   ├── models/
│   │   ├── __init__.py
│   │   └── order.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── order.py
│   └── schemas/
│       ├── __init__.py
│       └── order.py
└── users/
    ├── models/
    │   ├── __init__.py
    │   └── user.py
    ├── routes/
    │   ├── __init__.py
    │   └── user.py
    └── schemas/
        ├── __init__.py
        └── user.py
```

## Ce dont vous aurez besoin avant de commencer

Avant de vous lancer, assurez-vous d'avoir :

* Un compte gratuit [Render](https://render.com/) (inscrivez-vous si vous n'en avez pas)
    
* Un dépôt GitHub ou GitLab pour votre projet FastAPI
    
* Une familiarité de base avec Python, FastAPI et Git
    
* Votre structure de projet configurée de manière similaire à l'exemple ci-dessus
    

## Étapes de déploiement

### Étape 1 : Configurer la base de données PostgreSQL locale

Pour le développement local, vous devrez configurer PostgreSQL sur votre machine comme suit :

```sql
-- 1. Connectez-vous en tant que superutilisateur
psql -U postgres

-- 2. Créez une nouvelle base de données
CREATE DATABASE votre_bd;

-- 3. Créez un utilisateur avec mot de passe
CREATE USER votre_utilisateur WITH PASSWORD 'votre_mot_de_passe_securise';

-- 4. Accordez tous les privilèges sur la base de données
GRANT ALL PRIVILEGES ON DATABASE votre_bd TO votre_utilisateur;

-- 5. (Facultatif) Autorisez l'utilisateur à créer des tables
ALTER USER votre_utilisateur CREATEDB;

-- 6. Quittez
\q
```

Après avoir configuré votre base de données locale, créez un fichier `.env` à la racine de votre projet :

```bash
DATABASE_URL=postgresql://votre_utilisateur:votre_mot_de_passe_securise@localhost:5432/votre_bd
```

### Étape 2 : Configurer votre connexion à la base de données

Créez `database/database.py` pour gérer votre connexion PostgreSQL avec SQLAlchemy :

Ce fichier est crucial car il crée le moteur de base de données, définit la gestion des sessions et fournit une fonction de dépendance pour vos routes.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
"""
Le moteur gère la connexion à la base de données et exécute les requêtes.
"""
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dépendance de base de données pour les routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Et ajoutez `database/base.py` pour la classe de base :

```python
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```

### Étape 3 : Configurer votre application principale FastAPI

Créez le fichier principal de l'application FastAPI `fastapi_app/main.py` pour importer tous vos modules de route :

```python
import os
from fastapi import FastAPI, APIRouter
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer
import uvicorn
from dotenv import load_dotenv

# Charge les variables d'environnement
load_dotenv()

# Importations de la base de données
from database import Base, engine

# Importation des modèles pour s'assurer qu'ils sont enregistrés avec SQLAlchemy
import models

# Importation des modules de routeur
from items.routes import item_router
from orders.routes import order_router
from users.routes import user_router

# Initialisation de l'application FastAPI
app = FastAPI(
    title="Store API",
    version="1.0.0",
    description="Documentation de l'API pour Store API"
)

# Création des tables de la base de données au démarrage
Base.metadata.create_all(bind=engine)

# Point de terminaison racine
@app.get("/")
async def root():
    return {"message": "Bienvenue sur FastAPI Store"}

# Configuration du routeur API versionné et inclusion des routeurs de module
api_router = APIRouter(prefix="/v1")
api_router.include_router(item_router)
api_router.include_router(order_router)
api_router.include_router(user_router)

# Enregistrement du routeur principal avec l'application
app.include_router(api_router)

# Configuration du schéma OAuth2 pour le flux de connexion Swagger UI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")

# Schéma OpenAPI personnalisé avec configuration de sécurité
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    # Ajout du schéma de sécurité
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    # Application de l'exigence de sécurité globale
    openapi_schema["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Exécution de l'application avec Uvicorn lors de l'exécution directe
if __name__ == "__main__":
    port = os.environ.get("PORT")
    if not port:
        raise EnvironmentError("La variable d'environnement PORT n'est pas définie")
    uvicorn.run("fastapi_app.main:app", host="0.0.0.0", port=int(port), reload=False)
```

### Étape 4 : Créer un fichier de dépendances

À la racine de votre projet, créez un fichier `requirements.txt` qui inclut toutes les dépendances nécessaires :

```python
fastapi>=0.68.0
uvicorn>=0.15.0
sqlalchemy>=1.4.23
psycopg2-binary>=2.9.1
python-dotenv>=0.19.0
pydantic>=1.8.2
```

### Étape 5 : Approvisionner une base de données PostgreSQL sur Render

Connectez-vous à votre tableau de bord Render à l'adresse [dashboard.render.com](https://dashboard.render.com/login).

![Tableau de bord Render](https://cdn.hashnode.com/res/hashnode/image/upload/v1747782796468/e7564ed7-66cd-4466-a1d0-913b93dc9a77.png align="center")

Ensuite, cliquez sur "**Nouveau +**" en haut à droite et sélectionnez "**PostgreSQL**".

Remplissez les détails :

* Nom : `votre-app-bd` (choisissez un nom descriptif)
    
* Base de données : `votre_app` (ce sera le nom de votre base de données)
    
* Utilisateur : laissez par défaut (généré automatiquement)
    
* Région : Choisissez celle la plus proche de vos utilisateurs cibles
    
* Plan : Niveau gratuit
    

Enregistrez et notez l'URL de la base de données interne affichée après la création, qui ressemblera à ceci :

```bash
postgres://utilisateur:motdepasse@instance-postgres.render.com/votre_app
```

### Étape 6 : Déployer votre application FastAPI sur Render

Avec votre base de données approvisionnée, il est temps de déployer votre API. Vous pouvez le faire en suivant ces étapes :

1. Dans le tableau de bord Render, cliquez sur "**Nouveau +**" et sélectionnez "**Service Web**"
    
2. Connectez votre dépôt GitHub/GitLab
    
    ![Connectez-vous à GitHub/GitLab](https://cdn.hashnode.com/res/hashnode/image/upload/v1747813206325/5338209e-eb5c-4ba2-b28a-511296220935.png align="center")
    
3. Nommez votre service
    
    ![Nommer votre service](https://cdn.hashnode.com/res/hashnode/image/upload/v1747813320278/e21998cc-317b-4ea6-8dec-d52493e2969f.png align="center")
    
4. **Configurez ensuite les paramètres de construction** :
    
    * Environnement : `Python 3`
        
    * Commande de construction : `pip install -r requirements.txt`
        
    * Commande de démarrage : `python3 -m fastapi_app.main`
        
5. **Ajoutez vos variables d'environnement** :
    
    ![Ajout de variables d'environnement](https://cdn.hashnode.com/res/hashnode/image/upload/v1747813450598/6b0913b0-3081-44c4-b746-6b28549a2dd0.png align="center")
    
    * Cliquez sur l'onglet "Environnement"
        
    * Ajoutez votre URL de base de données :
        
        * Clé : `DATABASE_URL`
            
        * Valeur : Collez l'**URL de la base de données interne** de votre service PostgreSQL
            
    * Ajoutez toute autre variable d'environnement dont votre application a besoin
        
6. Enfin, cliquez sur **Déployer le service Web**.
    
    * Render commencera à construire et à déployer votre application
        
    * Ce processus prend quelques minutes. Vous pouvez surveiller les logs pendant la construction et le déploiement en temps réel
        

### Étape 7 : Tester vos points de terminaison API

Une fois déployée, accédez à l'URL de votre API (par exemple, [`https://nom-de-votre-app.onrender.com`](https://nom-de-votre-app.onrender.com)).

Accédez à `/docs` pour ouvrir l'interface Swagger interactive, où vous pouvez tester vos points de terminaison directement :

![Tester les points de terminaison dans Swagger](https://cdn.hashnode.com/res/hashnode/image/upload/v1747783210993/95ea29a5-d2aa-430f-a107-ef25c8ab4e24.png align="left")

* Développez un point de terminaison
    
* Cliquez sur **Essayer**
    
* Fournissez toute entrée requise
    
* Cliquez sur **Exécuter**
    
* Voir la réponse
    

## Flux de travail de développement local

Alors que votre application est déployée, vous devrez toujours travailler dessus localement. Voici comment maintenir un flux de travail de développement fluide :

Tout d'abord, créez un fichier `.env` local (ne commitez pas cela sur Git) :

```python
DATABASE_URL=postgresql://utilisateur:motdepasse@localhost:5432/votre_bd_locale
```

Ensuite, installez vos dépendances dans un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

Ensuite, exécutez votre serveur local :

```bash
python3 -m fastapi_app.main
```

Cette commande déclenche le bloc `__main__` dans `fastapi_app/main.py`, qui démarre l'application FastAPI en utilisant Uvicorn. Elle lit le `PORT` de votre environnement, alors assurez-vous qu'il est défini (par exemple, via un fichier `.env`).

Ensuite, apportez des modifications à votre code et testez localement avant de pousser vers GitHub/GitLab. Vous pouvez pousser vos modifications pour déclencher automatiquement un nouveau déploiement sur Render.

## Bonnes pratiques et conseils

1. **Utilisez les migrations de base de données** : Ajoutez Alembic à votre projet pour gérer les changements de schéma
    
    ```bash
    pip install alembic
    alembic init migrations
    ```
    
2. **Séparez les configurations de développement et de production** :
    
    ```python
    if os.environ.get("ENVIRONMENT") == "production":
        # Paramètres de production
    else:
        # Paramètres de développement
    ```
    
3. **Surveillez votre application** :
    
    * Render fournit des logs et des métriques pour votre application. Vous pouvez configurer des alertes pour les erreurs ou une utilisation élevée des ressources.
        
4. **Optimisez les requêtes de base de données** :
    
    * Utilisez les options de chargement de relations de SQLAlchemy.
        
    * Envisagez d'ajouter des index aux champs fréquemment interrogés.
        
5. **Mettez à l'échelle si nécessaire** :
    
    * Render vous permet de mettre à niveau votre plan à mesure que votre application grandit. Envisagez de mettre à niveau votre plan de base de données pour les applications de production.
        

## Problèmes courants et solutions

Lors du déploiement d'une application web Python sur Render, quelques problèmes peuvent survenir couramment. Voici un aperçu plus détaillé de ces problèmes et de la manière de les résoudre.

### **Erreurs de connexion à la base de données** :

Si votre application ne peut pas se connecter à la base de données, vérifiez d'abord que votre variable d'environnement `DATABASE_URL` est correctement définie dans votre tableau de bord Render. Assurez-vous que l'URL inclut le bon nom d'utilisateur, mot de passe, hôte, port et nom de la base de données.

De plus, confirmez que vos modèles SQLAlchemy correspondent au schéma réel dans votre base de données. Une incompatibilité ici peut entraîner des erreurs lors des migrations ou du démarrage de l'application. Si vous utilisez Postgres, assurez-vous que l'utilisateur de la base de données a la permission de lire/écrire des tables et d'effectuer des migrations.

### **Le déploiement échoue entièrement** :

Lorsque le déploiement échoue, Render fournit généralement des logs utiles sous l'onglet "Événements". Vérifiez là pour tout message d'erreur. Voici quelques causes courantes :

* Un fichier `requirements.txt` manquant ou des dépendances oubliées.
    
* Une mauvaise commande `start` dans les paramètres Render. Vérifiez qu'elle pointe vers votre point d'entrée correct (par exemple, `gunicorn app:app` ou `uvicorn main:app --host=0.0.0.0 --port=10000`).
    
* Une version Python incorrecte. Vous pouvez la spécifier dans un fichier `runtime.txt` (par exemple, `python-3.11.1`).
    

### **L'API retourne des erreurs 500 Internal Server** :

Les erreurs internes du serveur peuvent se produire pour plusieurs raisons. Pour les déboguer :

* Ouvrez vos logs Render et recherchez les tracebacks Python ou les exceptions non gérées.
    
* Essayez de reproduire le problème localement en utilisant la même requête et les mêmes données.
    
* Ajoutez des blocs `try/except` autour de la logique critique pour capturer et logger les erreurs plus élégamment.
    

Mieux encore, configurez un logging structuré ou un suivi des erreurs (par exemple, avec Sentry) pour attraper ces erreurs avant vos utilisateurs.

### **Temps de réponse lents** :

Si votre application est lente ou expire intermittemment, vérifiez :

* Si vous êtes toujours sur le niveau gratuit de Render, qui a des CPU et mémoire limités. Envisagez de mettre à niveau si vous gérez un trafic de niveau production.
    
* Si vous exécutez des requêtes de base de données lourdes ou non optimisées, des outils comme `.explain()` de SQLAlchemy ou Django Debug Toolbar peuvent aider.
    
* Si vous récupérez fréquemment les mêmes données, essayez de les mettre en cache en utilisant un cache léger en mémoire comme `functools.lru_cache` ou une instance Redis.
    

## **Conclusion**

Déployer une application FastAPI connectée à PostgreSQL sur Render est simple avec la bonne structure et configuration. Bien que ce guide utilise Render comme exemple, les concepts s'appliquent largement aux plateformes cloud.

Avec cette configuration, vous pouvez développer, tester et déployer des API Python robustes soutenues par des bases de données PostgreSQL de manière efficace.

Le niveau gratuit sur Render a certaines limitations, y compris des bases de données PostgreSQL qui expirent après 90 jours si elles ne sont pas mises à niveau. Pour les applications de production, envisagez de passer à un plan payant pour de meilleures performances et fiabilité.

Bon codage !