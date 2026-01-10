---
title: Comment construire un système de Machine Learning sur une architecture Serverless
subtitle: ''
author: Kuriko Iwai
co_authors: []
series: null
date: '2025-08-26T16:23:28.003Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-machine-learning-system-on-serverless-architecture
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756225357023/04572f1b-b9a7-43e0-aabc-2842faa2703f.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: coding
  slug: coding
- name: serverless
  slug: serverless
seo_title: Comment construire un système de Machine Learning sur une architecture
  Serverless
seo_desc: 'Let’s say you’ve built a fantastic machine learning model that performs
  beautifully in notebooks.

  But a model isn’t truly valuable until it’s in production, serving real users and
  solving real problems.

  In this article, you’ll learn how to ship a pro...'
---

Supposons que vous ayez construit un fantastique modèle de machine learning qui fonctionne parfaitement dans vos notebooks.

Mais un modèle n'a pas de réelle valeur tant qu'il n'est pas en production, au service d'utilisateurs réels et résolvant des problèmes concrets.

Dans cet article, vous apprendrez à déployer une application de ML prête pour la production construite sur une architecture serverless.

### Table des matières

* [Prérequis](#heading-prerequis)
    
* [Ce que nous construisons](#heading-ce-que-nous-construisons)
    
    * [Tarification par IA pour les détaillants](#heading-tarification-par-ia-pour-les-detaillants)
        
    * [Les modèles](#heading-les-modeles)
        
    * [Ajustement et entraînement](#heading-ajustement-et-entrainement)
        
    * [La prédiction](#heading-la-prediction)
        
    * [Validation de la performance](#heading-validation-de-la-performance)
        
* [L'architecture du système](#heading-larchitecture-du-systeme)
    
    * [Ressources AWS clés dans l'architecture](#heading-ressources-aws-cles-dans-larchitecture)
        
* [Le flux de travail de déploiement en action](#heading-le-flux-de-travail-de-deploiement-en-action)
    
    * [Étape 1 : Rédiger les scripts Python](#heading-etape-1-rediger-les-scripts-python)
        
    * [Étape 2 : Configurer les magasins de caractéristiques/modèles dans S3](#heading-etape-2-configurer-les-magasins-de-caracteristiquesmodeles-dans-s3)
        
    * [Étape 3 : Créer une application Flask avec des points de terminaison API](#heading-etape-3-creer-une-application-flask-avec-des-points-de-terminaison-api)
        
    * [Étape 4 : Publier une image Docker sur ECR](#heading-etape-4-publier-une-image-docker-sur-ecr)
        
    * [Étape 5 : Créer une fonction Lambda](#heading-etape-5-creer-une-fonction-lambda)
        
    * [Étape 6 : Configurer les ressources AWS](#heading-etape-6-configurer-les-ressources-aws)
        
* [Création d'une application client (Optionnel)](#heading-creation-dune-application-client-optionnel)
    
    * [L'application React](#heading-lapplication-react)
        
* [Résultats finaux](#heading-resultats-finaux)
    
* [Conclusion](#heading-conclusion)
    

### Prérequis

Ce projet nécessite une expérience de base avec :

* **Machine Learning / Deep Learning :** Le cycle de vie complet, y compris la gestion des données, l'entraînement des modèles, l'ajustement (tuning) et la validation.
    
* **Codage :** Maîtrise de Python, avec une expérience de l'utilisation des principales bibliothèques de ML telles que PyTorch et Scikit-Learn.
    
* **Déploiement Full-stack :** Expérience dans le déploiement d'applications utilisant des API RESTful.
    

## Ce que nous construisons

### Tarification par IA pour les détaillants

Ce projet vise à aider un détaillant de taille moyenne à rivaliser avec de grands acteurs comme Amazon.

Les petites entreprises ne peuvent souvent pas se permettre des remises importantes sur les prix et peuvent donc avoir du mal à trouver les points de prix optimaux à mesure qu'elles élargissent leurs gammes de produits.

Notre objectif est de tirer parti des modèles d'IA pour recommander le meilleur prix pour un produit sélectionné afin de maximiser les ventes du détaillant, et de l'afficher sur une interface utilisateur (UI) côté client :

![Aperçu de l'UI](https://cdn.hashnode.com/res/hashnode/image/upload/v1755873936847/ecf696ef-e161-4453-a6ad-e97d92ac1677.png align="center")

Vous pouvez explorer l'UI à partir d'ici [ici](https://kuriko-iwai.vercel.app/online-commerce-intelligence-hub).

### Les modèles

Je vais entraîner et ajuster plusieurs modèles de sorte que si le modèle principal échoue, un modèle de secours (backup) soit chargé pour fournir des prédictions.

* **Modèle principal** : Réseau feedforward multicouche (via la bibliothèque **PyTorch**)
    
* **Modèles de secours (Backups)** : LightGBM, SVR et Elastic Net (via la bibliothèque **Scikit-Learn**)
    

Les modèles de secours sont priorisés en fonction de leurs capacités d'apprentissage.

### Ajustement et entraînement

Le modèle principal a été entraîné sur un jeu de données d'environ 500 000 échantillons ([source](https://archive.ics.uci.edu/dataset/352/online+retail)) et affiné par l'optimisation bayésienne d' `Optuna`, avec une recherche par grille disponible pour un raffinement ultérieur.

Les backups sont également entraînés sur les mêmes échantillons et ajustés à l'aide du **Framework** `Scikit-Optimize`.

### La prédiction

Tous les modèles fournissent des prédictions sur des **valeurs de quantité logarithmiques.**

Les transformations logarithmiques des données de quantité rendent la distribution plus dense, ce qui aide les modèles à apprendre les schémas plus efficacement. En effet, les logarithmes réduisent l'impact des valeurs extrêmes, ou valeurs aberrantes, et peuvent aider à normaliser les données asymétriques.

### Validation de la performance

Nous évaluerons la performance du modèle à l'aide de différentes métriques pour les données transformées et originales, une valeur plus faible indiquant toujours une meilleure performance.

* **Valeurs logarithmiques** : Erreur Quadratique Moyenne (MSE)
    
* **Valeurs réelles** : Root Mean Squared Log Error (RMSLE) et Mean Absolute Error (MAE)
    

## L'architecture du système

Nous allons construire un écosystème complet autour d'une **fonction AWS Lambda** pour créer un système de ML évolutif :

![Fig. L'architecture du système (Créée par Kuriko IWAI)](https://miro.medium.com/v2/resize:fit:4680/0*ulcNtwJeU5EOfhTg.png align="left")

Fig. L'architecture du système (Créée par [Kuriko IWAI)](https://kuriko-iwai.vercel.app/)

**AWS Lambda** est un environnement de **production serverless** où un fournisseur de services peut exécuter l'application sans gérer de serveurs. Une fois le code téléchargé, AWS assume la responsabilité de la gestion de l'infrastructure sous-jacente.

Dans la production serverless, le code est déployé sous forme d'une **fonction sans état (stateless)** qui s'exécute uniquement lorsqu'elle est déclenchée par un événement tel que des requêtes HTTP ou des tâches planifiées.

Cette nature pilotée par les événements rend la production serverless extrêmement efficace en matière d'allocation de ressources car :

* **Il n'y a pas de gestion de serveur** : Le fournisseur cloud s'occupe des tâches opérationnelles.
    
* **Vous bénéficiez d'une mise à l'échelle automatique** : Les applications serverless montent ou descendent en charge automatiquement selon la demande.
    
* **Vous payez à l'utilisation** : Facturation basée sur la quantité exacte de ressources informatiques consommées par l'application.
    

Notez que d'autres écosystèmes cloud comme Google Cloud Platform (GCP) et Microsoft Azure offrent des alternatives complètes à AWS. Le choix dépend de votre budget, du type de projet et de votre familiarité avec chaque écosystème.

### Ressources AWS clés dans l'architecture

L'architecture du système se concentre sur les points suivants :

* L'application est entièrement conteneurisée sur Docker pour une accessibilité universelle.
    
* L'image du conteneur est stockée dans AWS Elastic Container Registry (ECR).
    
* Les points de terminaison de l'API REST d'API Gateway déclenchent un événement pour invoquer la fonction Lambda.
    
* La fonction Lambda charge l'image du conteneur depuis ECR et effectue l'inférence.
    
* Les modèles entraînés, les processeurs et les caractéristiques d'entrée sont stockés dans des compartiments (buckets) AWS S3.
    
* Un client Redis fournit des données analytiques mises en cache et les prédictions passées stockées dans ElastiCache.
    

Et pour construire le système, nous utiliserons les ressources AWS suivantes :

* **Lambda** : Fournit une fonction pour effectuer l'inférence.
    
* **API Gateway** : Route les appels d'API vers la fonction Lambda.
    
* **Stockage S3** : Sert de magasin de caractéristiques (feature store) et de magasin de modèles (model store).
    
* **ElastiCache** : Stocke les prédictions mises en cache et les données analytiques.
    
* **ECR** : Stocke les images de conteneurs Docker pour permettre à Lambda de récupérer l'image.
    

Chaque ressource nécessite une configuration. Je détaillerai ces points dans la section suivante.

## **Le flux de travail de déploiement en action**

Le flux de travail de déploiement comprend les étapes suivantes :

1. Rédiger les scripts de préparation des données, d'entraînement des modèles et de sérialisation
    
2. Configurer le magasin de caractéristiques et le magasin de modèles désignés dans S3
    
3. Créer une application Flask avec des points de terminaison API
    
4. Publier une image Docker sur ECR
    
5. Créer une fonction Lambda
    
6. Configurer les ressources AWS associées
    

Nous allons maintenant passer en revue chacune de ces étapes pour vous aider à comprendre pleinement le processus.

Pour votre référence, voici la structure du dépôt :

```markdown
.
.venv/                  [.gitignore]    # stocke l'env virtuel uv
│
└── data/               [.gitignore]
│     └── raw/                           # stocke les données brutes
│     └── preprocessed/                  # stocke les données traitées après imputation et ingénierie
│
└── models/             [.gitignore]    # stocke le modèle sérialisé après entraînement et ajustement
│     └── dfn/                           # deep feedforward network
│     └── gbm/                           # light gbm
│     └── en/                            # elastic net
│     └── production/                    # modèles à stocker dans S3 pour l'utilisation en production
|
└── notebooks/                          # stocke les notebooks d'expérimentation
│
└── src/                                # fonctions cœurs
│     └── _utils/                        # fonctions utilitaires
│     └── data_handling/                 # fonctions pour l'ingénierie des caractéristiques
│     └── model/                         # fonctions pour entraîner, ajuster, valider les modèles
│     │     └── sklearn_model
│     │     └── torch_model
│     │     └── ...
│     └── main.py                        # script principal pour exécuter l'inférence localement
│
└── app.py                               # application Flask (points de terminaison API)
└── pyproject.toml                       # configuration du projet
└── .env                [.gitignore]     # variables d'environnement
└── uv.lock                              # verrouillage des dépendances
└── Dockerfile                           # pour l'image du conteneur Docker
└── .dockerignore
└── requirements.txt
└── .python-version                      # verrouillage de la version python (3.12)
```

### Étape 1 : Rédiger les scripts Python

La première étape consiste à rédiger les scripts Python pour la préparation des données, l'entraînement et l'ajustement des modèles.

Nous exécuterons ces scripts dans un **processus par lots (batch)** car il s'agit de tâches gourmandes en ressources et avec état qui ne conviennent pas aux fonctions serverless optimisées pour des tâches courtes, sans état et pilotées par des événements.

Les fonctions serverless peuvent également subir des [**démarrages à froid (cold starts)**](https://www.freecodecamp.org/news/cold-start-problem-in-recommender-systems/). Avec des tâches lourdes dans la fonction, la passerelle API pourrait expirer avant de fournir les prédictions.

`src/main.py`

```python
import os
import torch
import warnings
import pickle
import joblib
import numpy as np
import lightgbm as lgb
from sklearn.linear_model import ElasticNet
from sklearn.svm import SVR
from skopt.space import Real, Integer, Categorical
from dotenv import load_dotenv

import src.data_handling as data_handling
import src.model.torch_model as t
import src.model.sklearn_model as sk


if __name__ == '__main__': 
    load_dotenv(override=True)
    os.makedirs(PRODUCTION_MODEL_FOLDER_PATH, exist_ok=True)
    
    # création des jeux de données d'entraînement, validation et test
    X_train, X_val, X_test, y_train, y_val, y_test, preprocessor = data_handling.main_script()
    
    # stockage du préprocesseur entraîné en local
    joblib.dump(preprocessor, PREPROCESSOR_PATH)
    
    # ajustement et entraînement du modèle
    best_dfn_full_trained, checkpoint = t.main_script(X_train, X_val, y_train, y_val)
    
    # sérialisation du modèle entraîné
    torch.save(checkpoint, DFN_FILE_PATH)
    
    # svr
    best_svr_trained, best_hparams_svr = sk.main_script(
        X_train, X_val, y_train, y_val, **sklearn_models[1]
    )
    if best_svr_trained is not None:
        with open(SVR_FILE_PATH, 'wb') as f:
            pickle.dump({ 'best_model': best_svr_trained, 'best_hparams': best_hparams_svr }, f)
    
    # elastic net
    best_en_trained, best_hparams_en = sk.main_script(
        X_train, X_val, y_train, y_val, **sklearn_models[0]
    )
    if best_en_trained is not None:
        with open(EN_FILE_PATH, 'wb') as f:
            pickle.dump({ 'best_model': best_en_trained, 'best_hparams': best_hparams_en }, f)
    
    # light gbm
    best_gbm_trained, best_hparams_gbm = sk.main_script(
        X_train, X_val, y_train, y_val, **sklearn_models[2]
    )
    
    if best_gbm_trained is not None:
        with open(GBM_FILE_PATH, 'wb') as f:
            pickle.dump({'best_model': best_gbm_trained, 'best_hparams': best_hparams_gbm }, f)
```

Exécutez le script pour entraîner et sérialiser les modèles en utilisant la gestion de paquets `uv` :

```bash
$uv venv
$source .venv/bin/activate
$uv run src/main.py
```

Le script `main.py` comprend plusieurs composants clés.

#### Scripts pour la gestion des données

Ces scripts impliquent le chargement des données originales, la structuration des valeurs manquantes et l'ingénierie des caractéristiques nécessaires à la future prédiction.

`src/data_handling/main.py`

```python
import os
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

import src.data_handling.scripts as scripts
from src._utils import main_logger


# chargement et sauvegarde du dataframe original en parquet
df = scripts.load_original_dataframe()
df.to_parquet(ORIGINAL_DF_PATH, index=False)

# imputation
df = scripts.structure_missing_values(df=df)

# ingénierie des caractéristiques
df = scripts.handle_feature_engineering(df=df)

# sauvegarde du df traité en csv et parquet
scripts.save_df_to_csv(df=df)
df.to_parquet(PROCESSED_DF_PATH, index=False)


# pour le prétraitement, classification des colonnes numériques et catégorielles
num_cols, cat_cols = scripts.categorize_num_cat_cols(df=df, target_col=target_col)
if cat_cols:
    for col in cat_cols: df[col] = df[col].astype('string')

# crée les jeux de données d'entraînement, validation et test (test est uniquement pour l'inférence)
y = df[target_col]
X = df.copy().drop(target_col, axis='columns')
test_size, random_state = 50000, 42
X_tv, X_test, y_tv, y_test = train_test_split(
    X, y, test_size=test_size, random_state=random_state
)
X_train, X_val, y_train, y_val = train_test_split(
    X_tv, y_tv, test_size=test_size, random_state=random_state
)

# transformation des jeux de données d'entrée
X_train, X_val, X_test, preprocessor = scripts.transform_input(
    X_train, X_val, X_test, num_cols=num_cols, cat_cols=cat_cols
)

# réentraînement et sérialisation du préprocesseur
if preprocessor is not None: preprocessor.fit(X)
joblib.dump(preprocessor, PREPROCESSOR_PATH)
```

#### Scripts pour l'entraînement et l'ajustement du modèle (Modèle PyTorch)

Les scripts impliquent l'initiation du modèle, la recherche de l'architecture neuronale et des hyperparamètres optimaux, et la sérialisation du modèle entièrement entraîné afin que le système puisse charger le modèle entraîné lors de l'inférence.

Comme le modèle principal est construit sur PyTorch et que les backups utilisent Scikit-Learn, nous rédigeons les scripts séparément.

#### 1\. Modèles PyTorch

**Le script d'entraînement** contient l'entraînement du modèle avec validation sur un sous-ensemble de données d'entraînement.

Il inclut une logique d'arrêt précoce (early stopping) lorsque l'historique des pertes ne s'améliore pas pendant un nombre donné d'époques consécutives (soit 10 époques).

`src/model/torch_model/scripts/training.py`

```python
import torch
import torch.nn as nn
import optuna # type: ignore
from sklearn.model_selection import train_test_split

from src._utils import main_logger

# device
device_type = device_type if device_type else 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
device = torch.device(device_type)

# scaler de gradient pour la stabilité (applicable uniquement pour cuda)
scaler = torch.GradScaler(device=device_type) if device_type == 'cuda' else None

# début entraînement
best_val_loss = float('inf')
epochs_no_improve = 0
for epoch in range(num_epochs):
    model.train()
    for batch_X, batch_y in train_data_loader:
        batch_X, batch_y = batch_X.to(device), batch_y.to(device)
        optimizer.zero_grad()

        try:
            # le système AMP de pytorch gère automatiquement le casting des tenseurs en Float16 ou Float32
            with torch.autocast(device_type=device_type):
                outputs = model(batch_X)
                loss = criterion(outputs, batch_y)
                
                # interrompre la boucle d'entraînement si les modèles retournent nan ou inf
                if torch.any(torch.isnan(outputs)) or torch.any(torch.isinf(outputs)):
                    main_logger.error(
                        'le modèle pytorch retourne nan ou inf. arrêt de la boucle d\'entraînement.'
                    )
                    break

            # création des gradients mis à l'échelle des pertes
            if scaler is not None:
                scaler.scale(loss).backward()
                scaler.unscale_(optimizer)  # cliping grad
                nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                scaler.step(optimizer)  # dé-mise à l'échelle des gradients
                scaler.update()  # mise à jour de l'échelle

            else:
                loss.backward()
                nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0) # cliping grad
                optimizer.step()

        except:
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
    
    
    # exécution de la validation sur un sous-ensemble du jeu d'entraînement
    model.eval()
    val_loss = 0.0

    # basculement du mode torch
    with torch.inference_mode():
        for batch_X_val, batch_y_val in val_data_loader:
            batch_X_val, batch_y_val = batch_X_val.to(device), batch_y_val.to(device)
            outputs_val = model(batch_X_val)
            val_loss += criterion(outputs_val, batch_y_val).item()

    val_loss /= len(val_data_loader)

    # vérification arrêt précoce
    if val_loss < best_val_loss - min_delta:
        best_val_loss = val_loss
        epochs_no_improve = 0
    else:
        epochs_no_improve += 1
        if epochs_no_improve >= patience:
            main_logger.info(f'arrêt précoce à l\'époque {epoch + 1}')
            break
```

**Le script d'ajustement** utilise le composant `study` de la bibliothèque `Optuna` pour exécuter l'optimisation bayésienne.

Le composant `study` choisit une architecture neuronale et un ensemble d'hyperparamètres à tester à partir de l'espace de recherche global.

Ensuite, il construit, entraîne et valide le modèle pour trouver l'architecture neuronale optimale capable de minimiser la perte (MSE, par exemple).

`src/model/torch_model/scripts/tuning.py`

```python
import itertools
import pandas as pd
import numpy as np
import optuna
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split

from src.model.torch_model.scripts.pretrained_base import DFN
from src.model.torch_model.scripts.training import train_model
from src._utils import main_logger

# device
device_type = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
device = torch.device(device_type)

# fonction de perte
criterion = nn.MSELoss()

# définition de la fonction objectif pour optuna
def objective(trial):
    # modèle
    num_layers = trial.suggest_int('num_layers', 1, 20)
    batch_norm = trial.suggest_categorical('batch_norm', [True, False])
    dropout_rates = []
    hidden_units_per_layer = []
    for i in range(num_layers):
        dropout_rates.append(trial.suggest_float(f'dropout_rate_layer_{i}', 0.0, 0.6))
        hidden_units_per_layer.append(trial.suggest_int(f'n_units_layer_{i}', 8, 256)) # unités cachées par couche

    model = DFN(
        input_dim=X_train.shape[1],
        num_layers=num_layers,
        dropout_rates=dropout_rates,
        batch_norm=batch_norm,
        hidden_units_per_layer=hidden_units_per_layer
    ).to(device)

    # optimiseur
    learning_rate = trial.suggest_float('learning_rate', 1e-10, 1e-1, log=True)
    optimizer_name = trial.suggest_categorical('optimizer', ['adam', 'rmsprop', 'sgd', 'adamw', 'adamax', 'adadelta', 'radam'])
    optimizer = _handle_optimizer(optimizer_name=optimizer_name, model=model, lr=learning_rate)

    # loaders de données
    batch_size = trial.suggest_categorical('batch_size', [32, 64, 128, 256])
    test_size = 10000 if len(X_train) > 15000 else int(len(X_train) * 0.2)
    X_train_search, X_val_search, y_train_search, y_val_search = train_test_split(X_train, y_train, test_size=test_size, random_state=42)
    train_data_loader = create_torch_data_loader(X=X_train_search, y=y_train_search, batch_size=batch_size)
    val_data_loader = create_torch_data_loader(X=X_val_search, y=y_val_search, batch_size=batch_size)

    # entraînement
    num_epochs = 3000 # assez d'époques (l'arrêt précoce arrêtera la boucle en cas de surapprentissage)
    _, best_val_loss = train_model(
        train_data_loader=train_data_loader,
        val_data_loader=val_data_loader,
        model=model,
        optimizer=optimizer,
        criterion = criterion,
        num_epochs=num_epochs,
        trial=trial,
    )
    return best_val_loss


# début optimisation des hyperparamètres et de l'architecture
study = optuna.create_study(direction='minimize', sampler=optuna.samplers.TPESampler())
study.optimize(objective, n_trials=50, timeout=600)

# best 
best_trial = study.best_trial
best_hparams = best_trial.params

# construction du modèle basé sur les résultats de l'ajustement
best_lr = best_hparams['learning_rate']
best_batch_size = best_hparams['batch_size']
input_dim = X_train.shape[1]
best_model = DFN(
    input_dim=input_dim,
    num_layers=best_hparams['num_layers'],
    hidden_units_per_layer=[v for k, v in best_hparams.items() if 'n_units_layer_' in k],
    batch_norm=best_hparams['batch_norm'],
    dropout_rates=[v for k, v in best_hparams.items() if 'dropout_rate_layer_' in k],
).to(device)

# construction d'un optimiseur basé sur les résultats de l'ajustement
best_optimizer_name = best_hparams['optimizer']
best_optimizer = _handle_optimizer(
    optimizer_name=best_optimizer_name, model=best_model, lr=best_lr
)

# création des loaders de données torch
train_data_loader = create_torch_data_loader(
    X=X_train, y=y_train, batch_size=best_batch_size
)
val_data_loader = create_torch_data_loader(
    X=X_val, y=y_val, batch_size=best_batch_size
)

# réentraînement du meilleur modèle avec l'ensemble des données d'entraînement
best_model, _ = train_model(
    train_data_loader=train_data_loader,
    val_data_loader=val_data_loader,
    model=best_model,
    optimizer=best_optimizer,
    criterion = criterion,
    num_epochs=1000
)

# création d'un checkpoint pour la sérialisation
checkpoint = {
    'state_dict': best_model.state_dict(),
    'hparams': best_hparams,
    'input_dim': X_train.shape[1],
    'optimizer': best_optimizer,
    'batch_size': best_batch_size
}

# sérialisation du modèle avec le checkpoint
torch.save(checkpoint, FILE_PATH)
```

#### 2\. Modèles Scikit-Learn (Backups)

Pour les modèles Scikit-Learn, nous exécuterons une **validation croisée k-fold** pendant l'entraînement pour éviter le surapprentissage.

La validation croisée k-fold est une technique d'évaluation de la performance d'un modèle de machine learning en l'entraînant et en le testant sur différents sous-ensembles de données d'entraînement.

Nous définissons la fonction `run_kfold_validation` où le modèle est entraîné et validé à l'aide d'une **validation croisée à 5 plis**.

`src/model/sklearn_model/scripts/tuning.py`

```python
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

def run_kfold_validation(
        X_train,
        y_train,
        base_model,
        hparams: dict,
        n_splits: int = 5, # nombre de plis
        early_stopping_rounds: int = 10,
        max_iters: int = 200
    ) -> float:

    mses = 0.0

    # création composant k-fold
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    for fold, (train_index, val_index) in enumerate(kf.split(X_train)):
        # création d'un sous-ensemble de données d'entraînement et validation
        X_train_fold, X_val_fold = X_train.iloc[train_index], X_train.iloc[val_index]
        y_train_fold, y_val_fold = y_train.iloc[train_index], y_train.iloc[val_index]
        
        # reconstruction du modèle
        model = base_model(**hparams)

        # début de la validation croisée
        best_val_mse = float('inf')
        patience_counter = 0
        best_model_state = None
        best_iteration = 0
        
        for iteration in range(max_iters):
            # entraînement sur un sous-ensemble
            try:
                model.train_one_step(X_train_fold, y_train_fold, iteration)
            except:
                model.fit(X_train_fold, y_train_fold)
             
            # prédiction sur les données de validation 
            y_pred_val_kf = model.predict(X_val_fold)

            # calcul de la perte de validation (MSE)
            current_val_mse = mean_squared_error(y_val_fold, y_pred_val_kf)
        
            # vérification de l'arrêt précoce
           if current_val_mse < best_val_mse:
                best_val_mse = current_val_mse
                patience_counter = 0
                best_model_state = model.get_params()
                best_iteration = iteration
           else:
                patience_counter += 1
            
           # exécution de l'arrêt précoce
           if patience_counter >= early_stopping_rounds:
                main_logger.info(f"Pli {fold}: Arrêt précoce déclenché à l'itération {iteration} (meilleur à {best_iteration}). Meilleur MSE: {best_val_mse:.4f}")
                break
           
       
        # après les époques, reconstruction du modèle le plus performant 
        if best_model_state: model.set_params(**best_model_state)
         
        # prédiction
        y_pred_val_kf = model.predict(X_val_fold)
        
        # accumulation des MSE
        mses += mean_squared_error(y_pred_val_kf, y_val_fold)
    
    # calcul de la perte finale (moyenne des MSE à travers les plis)
    ave_mse = mses / n_splits
    return ave_mse
```

Ensuite, pour le **script d'ajustement**, nous utilisons la fonction `gp_minimize` de la bibliothèque `Scikit-Optimize`.

La fonction `gp_minimize` est utilisée pour ajuster les hyperparamètres avec l'optimisation bayésienne.

Cette fonction recherche intelligemment le meilleur ensemble d'hyperparamètres capable de minimiser l'erreur du modèle, calculée via la fonction `run_kfold_validation` définie précédemment.

Les hyperparamètres les plus performants sont ensuite utilisés pour reconstruire et entraîner le modèle final.

`src/model/sklearn_model/scripts/tuning.py`

```python
from functools import partial
from skopt import gp_minimize


# définition de la fonction objectif pour l'optimisation bayésienne
def objective(params, X_train, y_train, base_model, hparam_names):
    hparams = {item: params[i] for i, item in enumerate(hparam_names)}
    ave_mse = run_kfold_validation(X_train=X_train, y_train=y_train, base_model=base_model, hparams=hparams)
    return ave_mse

# création de l'espace de recherche
hparam_names = [s.name for s in space]
objective_partial = partial(objective, X_train=X_train, y_train=y_train, base_model=base_model, hparam_names=hparam_names)

# recherche des hyperparamètres optimaux
results = gp_minimize(
    func=objective_partial,
    dimensions=space,
    n_calls=n_calls,
    random_state=42,
    verbose=False,
    n_initial_points=10,
)
# résultats
best_hparams = dict(zip(hparam_names, results.x))
best_mse = results.fun

# reconstruction du modèle avec les meilleurs hyperparamètres
best_model = base_model(**best_hparams)

# réentraînement du modèle sur tout le jeu d'entraînement
best_model.fit(X_train, y_train)
```

### Étape 2 : Configurer les magasins de caractéristiques/modèles dans S3

Les modèles entraînés et les données traitées sont stockés dans le compartiment S3 sous forme de **fichiers Parquet**.

Nous rédigeons la fonction `s3_upload` où le **client Boto3**, une interface de bas niveau vers un service AWS, initie la connexion à S3 :

```python
import os
import boto3
from dotenv import load_dotenv

from src._utils import main_logger

def s3_upload(file_path: str):
    # initialisation client boto3
    load_dotenv(override=True)
    S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME') # le bucket créé dans s3
    s3_client = boto3.client('s3', region_name=os.environ.get('AWS_REGION_NAME')) # votre région par défaut

    if s3_client:
        # création de la clé s3 et chargement du fichier vers le bucket
        s3_key = file_path if file_path[0] != '/' else file_path[1:]
        s3_client.upload_file(file_path, S3_BUCKET_NAME, s3_key)
        main_logger.info(f"fichier chargé sur s3://{S3_BUCKET_NAME}/{s3_key}")
    else:
        main_logger.error('échec de la création du client S3.')
```

#### Magasin de modèles (Model Store)

Les modèles PyTorch entraînés sont sérialisés (convertis) en fichiers `.pth`.

Ensuite, ces fichiers sont chargés dans le compartiment S3, permettant au système de charger le modèle entraîné lorsqu'il effectue l'inférence en production.

```python
import torch

from src._utils import s3_upload

# sérialisation du modèle, stockage en local
torch.save(trained_model.state_dict(), MODEL_FILE_PATH)

# chargement vers le magasin de modèles s3
s3_upload(file_path=MODEL_FILE_PATH)
```

#### Magasin de caractéristiques (Feature Store)

Les données traitées sont converties aux formats CSV et Parquet.

Ensuite, les fichiers Parquet sont chargés dans le compartiment S3, permettant au système de charger les données légères lorsqu'il crée les données de prédiction pour l'inférence en production.

```python
from src._utils import s3_upload

# stockage des fichiers csv et parquet en local
df.to_csv(file_path, index=False)
df.to_parquet(DATA_FILE_PATH, index=False)

# stockage dans le feature store s3
s3_upload(file_path=DATA_FILE_PATH)

# le préprocesseur entraîné est également stocké pour transformer les données de prédiction
s3_upload(file_path=PROCESSOR_PATH)
```

### Étape 3 : Créer une application Flask avec des points de terminaison API

Ensuite, nous allons créer une application Flask avec des points de terminaison API.

Flask doit configurer les scripts Python dans le fichier `app.py` situé à la racine du dépôt du projet.

Comme montré dans les extraits de code, le fichier `app.py` doit contenir les composants dans cet ordre :

1. Configuration du client AWS Boto3,
    
2. Configuration de l'application Flask et des points de terminaison API,
    
3. Chargement du préprocesseur entraîné, des données d'entrée traitées `X_test` et des modèles entraînés,
    
4. Invocation de la fonction Lambda via API Gateway, et
    
5. La section de test local.
    

Notez que `X_test` ne doit jamais être utilisé pendant l'entraînement du modèle pour éviter toute fuite de données.

`app.py`

```python
from flask import Flask
from flask_cors import cross_origin
from waitress import serve
from dotenv import load_dotenv

from src._utils import main_logger

# variables globales (seront chargées depuis les buckets S3)
_redis_client = None
X_test = None
preprocessor = None
model = None
backup_model = None

# chargement env si local sinon skip (lambda se réfère à env en production)
AWS_LAMBDA_RUNTIME_API = os.environ.get('AWS_LAMBDA_RUNTIME_API', None)
if AWS_LAMBDA_RUNTIME_API is None: load_dotenv(override=True)


#### <---- 1. CLIENT AWS BOTO3 ---->
# client boto3 
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME', 'ml-sales-pred')
s3_client = boto3.client('s3', region_name=os.environ.get('AWS_REGION_NAME', 'us-east-1'))
try:
    # test de connexion au client boto3
    sts_client = boto3.client('sts')
    identity = sts_client.get_caller_identity()
    main_logger.info(f"Lambda utilise le rôle : {identity['Arn']}")
except Exception as e:
    main_logger.error(f"Erreur d'identifiants/permissions Lambda : {e}")

#### <---- 2. CONFIGURATION FLASK & POINTS D'ENTRÉE API ---->
# configuration app flask
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

# ajout d'un point de terminaison API simple pour tester la prédiction par point de prix
@app.route('/v1/predict-price/<string:stockcode>', methods=['GET', 'OPTIONS'])
@cross_origin(origins=origins, methods=['GET', 'OPTIONS'], supports_credentials=True)
def predict_price(stockcode):
    df_stockcode = None

    # récupération des paramètres de requête
    data = request.args.to_dict()

    try:
        # récupération cache
        if _redis_client is not None:
            # retourne les résultats de prédiction mis en cache si présents sans inférence
            cached_prediction_result = _redis_client.get(cache_key_prediction_result_by_stockcode)
            if cached_prediction_result: 
                return jsonify(json.loads(json.dumps(cached_prediction_result)))

            # données historiques du produit sélectionné
            cached_df_stockcode = _redis_client.get(cache_key_df_stockcode)
            if cached_df_stockcode: df_stockcode = json.loads(json.dumps(cached_df_stockcode))


        # définir la plage de prix pour les prédictions (paramètre ou min/max historique)
        min_price = float(data.get('unitprice_min', df_stockcode['unitprice_min'][0]))
        max_price = float(data.get('unitprice_max', df_stockcode['unitprice_max'][0]))

        # créer des segments dans la plage de prix
        NUM_PRICE_BINS = int(data.get('num_price_bins', 100))
        price_range = np.linspace(min_price, max_price, NUM_PRICE_BINS)

        # créer un jeu de données de prédiction en fusionnant X_test et df_stockcode
        price_range_df = pd.DataFrame({ 'unitprice': price_range })
        test_sample = X_test.sample(n=1000, random_state=42)
        test_sample_merged = test_sample.merge(price_range_df, how='cross') if X_test is not None else price_range_df
        test_sample_merged.drop('unitprice_x', axis=1, inplace=True)
        test_sample_merged.rename(columns={'unitprice_y': 'unitprice'}, inplace=True)

        # prétraitement du jeu de données
        X = preprocessor.transform(test_sample_merged) if preprocessor else test_sample_merged

        # inférence
        y_pred_actual = None
        epsilon = 0
        # essai avec le modèle principal
        if model:
            input_tensor = torch.tensor(X, dtype=torch.float32)
            model.eval()
            with torch.inference_mode():
                y_pred = model(input_tensor)
                y_pred = y_pred.cpu().numpy().flatten()
                y_pred_actual = np.exp(y_pred + epsilon)

        # sinon, utilisation des backups
        elif backup_model:
            y_pred = backup_model.predict(X)
            y_pred_actual = np.exp(y_pred + epsilon)

        
        # finalisation du résultat pour l'application client
        df_ = test_sample_merged.copy()
        df_['quantity'] = np.floor(y_pred_actual) # la quantité doit être un entier
        df_['sales'] = df_['quantity'] * df_['unitprice'] # calcul des ventes
        df_ = df_.sort_values(by='unitprice')

        # agrégation des résultats par prix unitaire
        df_results = df_.groupby('unitprice').agg(
            quantity=('quantity', 'median'),
            quantity_min=('quantity', 'min'),
            quantity_max=('quantity', 'max'),
            sales=('sales', 'median'),
        ).reset_index()
        
        # trouver le point de prix optimal
        optimal_row = df_results.loc[df_results['sales'].idxmax()]
        optimal_price = optimal_row['unitprice']
        optimal_quantity = optimal_row['quantity']
        best_sales = optimal_row['sales']
        
        all_outputs = []
        for _, row in df_results.iterrows():
            current_output = {
                "stockcode": stockcode,
                "unit_price": float(row['unitprice']),
                'quantity': int(row['quantity']),
                'quantity_min': int(row['quantity_min']),
                'quantity_max': int(row['quantity_max']),
                "predicted_sales": float(row['sales']),
            }
            all_outputs.append(current_output)

        # stockage des résultats en cache
        if all_outputs and _redis_client is not None:
             serialized_data = json.dumps(all_outputs)
            _redis_client.set(
                cache_key_prediction_result_by_stockcode, 
                serialized_data,
                ex=3600     # expire dans une heure
            )

        # retourne une liste de tous les résultats
        return jsonify(all_outputs)

    except Exception as e: return jsonify([])
   
 
# gestion des en-têtes (processus de la passerelle API vers Lambda)
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    response.headers['Access-Control-Allow-Origin'] = CLIENT_A
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Origin'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONSS'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

#### <---- 3. CHARGEMENT PRÉPROCESSEUR, JEU DE DONNÉES ET MODÈLES ---->
load_processor()
load_x_test()
load_model()

#### <---- 4. INVOCATION LAMBDA ---->
def handler(event, context):
    logger.info("handler lambda invoqué.")
    try:
        # connexion client redis après invocation lambda
        get_redis_client()
    except Exception as e:
        logger.critical(f"échec de la connexion Redis initiale dans le handler : {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Échec de l\'initialisation du client Redis.'})
        }
    
    # utilisation du package awsgi pour convertir JSON en WSGI
    return awsgi.response(app, event, context)


#### <---- 5. POUR TEST LOCAL ---->
# servir localement sur serveur WSGI waitress
# lambda ignorera cette section.
if __name__ == '__main__':   
    if os.getenv('ENV') == 'local':
        main_logger.info("...démarrage de l'opération (local)...")
        serve(app, host='0.0.0.0', port=5002)
    else:
        app.run(host='0.0.0.0', port=8080)
```

Je vais tester le point de terminaison localement à l'aide du gestionnaire de paquets `uv` :

```python
$uv run app.py --cache-clear

$curl http://localhost:5002/v1/predict-price/{STOCKCODE}
```

Le système a fourni une liste de prédictions de ventes pour chaque point de prix :

![Capture d'écran réponse locale Flask](https://cdn.hashnode.com/res/hashnode/image/upload/v1755607075000/e0e8cbcb-8817-4aa5-b3d1-37b76cc684fb.png align="center")

Fig. Capture d'écran de la réponse locale de l'application Flask

#### Points clés sur la configuration de l'application Flask

Il y a divers points à prendre en considération lors de la configuration d'une application Flask avec Lambda :

##### **1\. Peu de points de terminaison API par conteneur**

L'ajout de trop nombreux points de terminaison API à une seule instance serverless peut mener à un problème de **fonction monolithique** où les problèmes d'un point d'entrée impactent les autres.

Dans ce projet, nous nous concentrons sur un seul point de terminaison par conteneur – et si nécessaire, nous pouvons ajouter des fonctions Lambda séparées.

##### **2\. Comprendre la fonction** `handler` **et le rôle d'AWSGI**

La fonction `handler` est invoquée chaque fois que la fonction Lambda reçoit une requête client de l'API Gateway.

La fonction prend l'argument `event` qui inclut les détails de la requête dans un **dictionnaire JSON** et le transmet à l'application Flask.

**AWSGI** agit comme un adaptateur, traduisant un événement Lambda au format JSON en une requête WSGI que Flask peut comprendre, et convertit la réponse en JSON pour Lambda.

##### **3\. Utilisation du stockage cache**

La fonction `get_redis_client` est appelée une fois que la fonction `handler` est sollicitée par API Gateway. Cela permet à l'application Flask de stocker ou récupérer un cache depuis le client Redis :

```python
import redis
import redis.cluster
from redis.cluster import ClusterNode

_redis_client = None

def get_redis_client():
    global _redis_client
    if _redis_client is None:
        REDIS_HOST = os.environ.get("REDIS_HOST")
        REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
        REDIS_TLS = os.environ.get("REDIS_TLS", "true").lower() == "true"
        try:
            startup_nodes = [ClusterNode(host=REDIS_HOST, port=REDIS_PORT)]
            _redis_client = redis.cluster.RedisCluster(
                startup_nodes=startup_nodes,
                decode_responses=True,
                skip_full_coverage_check=True,
                ssl=REDIS_TLS,                  # encryption in transit activée -> doit être true
                ssl_cert_reqs=None,
                socket_connect_timeout=5,
                socket_timeout=5,
                health_check_interval=30,
                retry_on_timeout=True,
                retry_on_error=[
                    redis.exceptions.ConnectionError,
                    redis.exceptions.TimeoutError
                ],
                max_connections=10,            # limite les connexions pour Lambda
                max_connections_per_node=2     # limite par nœud
            )
            _redis_client.ping()
            main_logger.info("connexion réussie au cluster ElastiCache Redis")
        except Exception as e:
            main_logger.error(f"erreur inattendue lors de la connexion au cluster Redis : {e}", exc_info=True)
            _redis_client = None
    return _redis_client
```

##### **4\. Gestion des tâches lourdes en dehors de la fonction** `handler` 

Les fonctions serverless peuvent subir une **durée de démarrage à froid**.

Alors qu'une fonction Lambda peut s'exécuter jusqu'à 15 minutes, son API Gateway associée a un délai d'expiration de 29 secondes (29 000 ms) pour une API RESTful.

Ainsi, toutes les tâches lourdes comme le chargement des préprocesseurs, des données d'entrée ou des modèles doivent être effectuées une seule fois en dehors de la fonction `handler`, garantissant qu'elles sont prêtes *avant* l'appel du point de terminaison.

Voici les fonctions de chargement appelées dans `app.py`.

`app.py`

```python
import joblib

from src._utils import s3_load, s3_load_to_temp_file

preprocessor = None
X_test = None
model = None
backup_model = None


# chargement processeur
def load_preprocessor():
    global preprocessor
    preprocessor_tempfile_path = s3_load_to_temp_file(PREPROCESSOR_PATH)
    preprocessor = joblib.load(preprocessor_tempfile_path)
    os.remove(preprocessor_tempfile_path)


# chargement données entrée
def load_x_test():
    global X_test
    x_test_io = s3_load(file_path=X_TEST_PATH)
    X_test = pd.read_parquet(x_test_io)


# chargement modèle
def load_model():
    global model, backup_model
    # tentative chargement modèle principal
    try:
        # d'abord charger io depuis le bucket s3
        model_data_bytes_io_ = s3_load(file_path=DFN_FILE_PATH)
        # convertir en dictionnaire checkpoint
        checkpoint_ = torch.load(
            model_data_bytes_io_, 
            weights_only=False, 
            map_location=device
        )
        # reconstruire le modèle
        model = t.scripts.load_model(checkpoint=checkpoint_, file_path=DFN_FILE_PATH)
        # mode évaluation
        model.eval()
    
    # sinon, modèle de secours
     except:
        load_artifacts_backup_model()
```

### Étape 4 : Publier une image Docker sur ECR

Après avoir configuré l'application Flask, nous allons conteneuriser l'ensemble de l'application sur **Docker**.

La conteneurisation permet de regrouper l'application, y compris les modèles, ses dépendances et sa configuration, dans un conteneur.

Docker crée une image de conteneur basée sur les instructions définies dans un `Dockerfile`, et le moteur Docker utilise l'image pour exécuter le conteneur isolé.

Dans ce projet, nous chargerons l'image du conteneur Docker vers ECR, afin que la fonction Lambda puisse y accéder en production.

Ensuite, nous définirons le fichier `.dockerignore` pour optimiser l'image du conteneur :

`.dockerignore`

```plaintext
# données non pertinentes
__pycache__/
.ruff_cache/
.DS_Store/
.venv/
dist/
.vscode
*.psd
*.pdf
[a-f]*.log
tmp/
awscli-bundle/

# modèles expérimentaux, données inutiles
dfn_bayesian/
dfn_grid/
data/
notebooks/
```

`Dockerfile`

```dockerfile
# servir depuis aws ecr 
FROM public.ecr.aws/lambda/python:3.12

# définir répertoire de travail
WORKDIR /app

# copier tout le dépôt (sauf .dockerignore)
COPY . /app/

# installer dépendances
RUN pip install --no-cache-dir -r requirements.txt

# définir commandes
ENTRYPOINT [ "python" ]
CMD [ "-m", "awslambdaric", "app.handler" ]
```

#### Test en local

Ensuite, nous testerons l'image Docker en construisant localement le conteneur nommé `my-app` :

```bash
$docker build -t my-app -f Dockerfile .
```

Ensuite, nous exécuterons le conteneur avec le serveur `waitress` en local :

```bash
$docker run -p 5002:5002 -e ENV=local my-app app.py
```

Le drapeau `-e ENV=local` définit la variable d'environnement dans le conteneur, ce qui déclenchera l'appel `waitress.serve()` dans `app.py`.

Dans le terminal, vous trouverez un message indiquant :

![Réponse app Flask](https://miro.medium.com/v2/resize:fit:1260/0*zu8mamgKMKOUxwCA.png align="left")

Vous pouvez également appeler le point de terminaison pour voir les résultats retournés :

```bash
$uv run app.py --cache-clear

$curl http://localhost:5002/v1/predict-price/{STOCKCODE}
```

#### Publier l'image Docker sur ECR

Pour publier l'image Docker, nous devons d'abord configurer les identifiants AWS par défaut et la région :

* Depuis la console AWS, émettez un jeton d'accès et vérifiez la région par défaut.
    
* Stockez-les dans les fichiers `~/aws/credentials` et `~/aws/config` :
    

`~/aws/credentials`

```plaintext
[default] 
aws_secret_access_key=
aws_access_key_id=
```

`~/aws/config`

```plaintext
[default]
region=
```

Après la configuration, nous publierons l'image Docker sur ECR.

```bash
# authentifier le client docker vers ECR
$aws ecr get-login-password --region <votre-region-aws> | docker login --username AWS --password-stdin <votre-id-compte-aws>.dkr.ecr.<votre-region-aws>.amazonaws.com

# créer le dépôt
$aws ecr create-repository --repository-name <votre-nom-repo> --region <votre-region-aws>

# taguer l'image docker
$docker tag <votre-nom-repo>:<votre-version-app>  <votre-id-compte-aws>.dkr.ecr.<votre-region-aws>.amazonaws.com/<votre-nom-app>:<votre-version-app>

# pousser
$docker push <votre-id-compte-aws>.dkr.ecr.<votre-region-aws>.amazonaws.com/<votre-nom-repo>:<votre-version-app>
```

Détails :

* `<votre-region-aws>` : Votre région AWS par défaut (par exemple, `us-east-1`).
    
* `<votre-id-compte-aws>` : Votre ID de compte AWS à 12 chiffres.
    
* `<votre-nom-repo>` : Le nom de dépôt souhaité.
    
* `<votre-version-app>` : Le tag souhaité (par exemple, `v1.0`).
    

Désormais, l'image Docker est stockée dans ECR avec son tag :

![Capture console AWS ECR](https://miro.medium.com/v2/resize:fit:1260/0*tUQkbDW-uAmrjBfx.png align="left")

Fig. Capture d'écran de la console AWS ECR

### Étape 5 : Créer une fonction Lambda

Ensuite, nous allons créer une fonction Lambda.

Depuis la console Lambda, choisissez :

* L'option `Image de conteneur` (Container Image),
    
* L'URL de l'image du conteneur dans la liste déroulante,
    
* Un nom de fonction de votre choix,
    
* Un type d'architecture (arm64 est recommandé pour un meilleur rapport prix-performance).
    

![Capture configuration Lambda](https://miro.medium.com/v2/resize:fit:1260/0*3b-wIEUzRooQcvN_.png align="left")

Fig. Capture d'écran de la configuration de la fonction AWS Lambda

La fonction Lambda `my-app` a été lancée avec succès.

#### Connecter la fonction Lambda à API Gateway

Ensuite, nous ajouterons API Gateway comme déclencheur d'événement à la fonction Lambda.

Tout d'abord, visitez la console API Gateway et créez des **méthodes API REST** en utilisant l'ARN de la fonction Lambda :

![Capture configuration API Gateway](https://miro.medium.com/v2/resize:fit:1260/0*60TP64gdSjhKfiO8.png align="left")

Fig. Capture d'écran de la configuration d'AWS API Gateway

Ensuite, ajoutez des ressources à la passerelle API créée pour créer un point de terminaison :  
`API Gateway > APIs > Ressources > Créer une ressource`

* Alignez le point de terminaison de la ressource avec le point de terminaison API défini dans [`app.py`](http://app.py).
    
* Configurez le CORS (par exemple, accepter des origines spécifiques).
    
* Déployez la ressource sur une étape (stage).
    

En retournant sur la console Lambda, vous constaterez qu'API Gateway est connecté comme déclencheur :
`Lambda > Fonction > my-app`

![Capture tableau de bord Lambda](https://miro.medium.com/v2/resize:fit:1260/0*DlfiEieZArmYlOuT.png align="left")

Fig. Capture d'écran du tableau de bord AWS Lambda

### Étape 6 : Configurer les ressources AWS

Enfin, nous configurerons les ressources AWS associées pour faire fonctionner le système en production.

#### 1\. Le rôle IAM : Contrôle de l'accès aux ressources

AWS nécessite des **rôles IAM** pour accorder des permissions temporaires et sécurisées aux utilisateurs.

Le rôle IAM utilise des politiques pour accorder des accès au service sélectionné. Les politiques peuvent être émises par AWS ou personnalisées par l'utilisateur.

Il est important d'éviter les droits d'accès trop permissifs.

1. Dans la console de la fonction Lambda, vérifiez le rôle d'exécution :  
    `Lambda > Fonction > <FONCTION> > Autorisations > Rôle d'exécution`.
    
2. Configurez les politiques suivantes :
    
    * **Lambda** `AWSLambdaExecute` : Autorise l'exécution de la fonction.
        
    * **EC2** `Inline policy` : Autorise le contrôle du groupe de sécurité et du VPC de la fonction Lambda.
        
    * **ECR** `AmazonElasticContainerRegistryPublicFullAccess` + `Inline policy` : Autorise le stockage et la récupération de l'image Docker.
        
    * **ElastiCache** `AmazonElastiCacheFullAccess` + `Inline policy` : Autorise le stockage et la récupération des caches.
        
    * **S3** : `AmazonS3ReadOnlyAccess` + `Inline policy` : Autorise la lecture et le stockage des contenus.
        

#### 2\. Le groupe de sécurité : Contrôle du trafic réseau

Un **groupe de sécurité** est un pare-feu virtuel qui contrôle le trafic réseau entrant et sortant pour les ressources AWS.

Créez un nouveau groupe de sécurité pour la fonction Lambda :  
`EC2 > Groupes de sécurité > <VOTRE GROUPE DE SÉCURITÉ>`

Les règles entrantes (Inbound) :

* **S3 → Lambda** : **Type** : HTTPS / **Protocole** : TCP / **Plage de ports** : 443 / Source : Personnalisée\*
    
* **ElastiCache → Lambda** : **Type** : TCP personnalisé / **Plage de ports** : 6379 / Source : Personnalisée\*
    

\*Choisissez le groupe de sécurité créé pour la Lambda comme source.

Les règles sortantes (Outbound) :

* **Lambda → Internet** : **Type** : HTTPS / **Protocole** : TCP / **Plage de ports** : 443 / **Destination** : 0.0.0.0/0
    
* **ElastiCache → Internet** : **Type** : Tout le trafic / **Destination** : 0.0.0.0/0
    

#### 3\. Le Virtual Private Cloud (VPC)

Un **Virtual Private Cloud (VPC)** fournit un réseau privé logiquement isolé pour les ressources AWS.

Bien que ce soit facultatif, nous utiliserons le VPC pour connecter la fonction Lambda au stockage S3 et à ElastiCache.

Le processus :

1. Création d'un point de terminaison VPC : `VPC > Créer un VPC`.
    
2. Création d'un point de terminaison STS (Security Token Service) :  
    `VPC > PrivateLink et Lattice > Points de terminaison > Créer un point de terminaison` :
    
    * **Type** : Service AWS
    * **Nom du service** : com.amazonaws.&lt;VOTRE RÉGION&gt;.sts
    * **Sous-réseaux** : Sélectionnez tous les sous-réseaux.
    * **DNS** : Activer les noms DNS.

3. Création d'un point de terminaison S3 dans le VPC :
    * **Nom du service** : com.amazonaws.&lt;VOTRE RÉGION&gt;.s3
    * **Type** : Passerelle (Gateway)

Enfin, vérifiez que l'ID du VPC de la fonction Lambda dirige bien vers le VPC créé.

C'est tout pour le flux de déploiement.

Nous pouvons maintenant tester le point de terminaison en production. Copiez l'**URL d'appel (Invoke URL)** de l'API déployée. Appelez ensuite l'API pour vérifier si elle répond par des prédictions :

```bash
$curl -H 'Authorization: Bearer VOTRE_TOKEN_API' -H 'Accept: application/json' \
     '<URL_APPEL>/<POINT_ENTREE>'
```

Pour la journalisation et le débogage, nous utiliserons le LiveTail de CloudWatch.

## Création d'une application client (Optionnel)

Pour un déploiement full-stack, nous allons construire une application React simple pour afficher la prédiction en utilisant la bibliothèque [recharts](https://recharts.org/en-US) pour la visualisation.

### L'application React

L'application React crée une page web qui récupère et visualise les prédictions de ventes d'une API externe, recommandant un point de prix optimal.

L'application utilise `useState` pour gérer ses données et son état. Lorsqu'un utilisateur initie une requête, un hook `useEffect` déclenche une requête `fetch` vers le backend Flask.

L'`AreaChart` de la bibliothèque `recharts` visualise ensuite ces données. L'axe X représente le `prix` et l'axe Y représente les `ventes`.

`App.js` : (dans une application React séparée)

```javascript
import { useState, useEffect } from "react"
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine } from 'recharts'


function App() {
  // état
  const [predictions, setPredictions] = useState([])
  const [start, setStart] = useState(false)
  const [isLoading, setIsLoading] = useState(false)

  // données produit
  let selectedStockcode = '85123A'
  let selectedProduct = productOptions.filter(item => item.id === selectedStockcode)[0]

  // url backend flask
  const flaskBackendUrl = "VOTRE URL BACKEND FLASK"

  // création des données du graphique
  const chartDataSales = predictions && predictions.length > 0
    ? predictions
      .map(item => ({
        price: item.unit_price,
        sales: item.predicted_sales,
        volume: item.unit_price !== 0 ? item.predicted_sales / item.unit_price : 0
      }))
      .sort((a, b) => a.price - b.price)
    : [...selectedProduct['histPrices']]

  // prix optimal
  const optimalPrice = predictions.length > 0
    ? predictions.sort((a, b) => b.predicted_sales - a.predicted_sales)[0]['unit_price']
    : 0

  // récupération des résultats
  useEffect(() => {
    const handlePrediction = async () => {
      setIsLoading(true)
      setPredictions([])
      const errorPrices = selectedProduct['errorPrices']

      await fetch(flaskBackendUrl)
        .then(res => {
          if (res.status !== 200) { setPredictions(errorPrices); setIsLoading(false); setStart(false) }
          else return Promise.resolve(res.clone().json())
        })
        .then(res => {
          if (res && res.length > 0) setPredictions(res)
          else setPredictions(errorPrices)
          setIsLoading(false); setStart(false)
        })
        .catch(err => { setPredictions(errorPrices); setIsLoading(false); setStart(false) })
        .finally(setStart(false))
    }

    if (start) handlePrediction()
    if (predictions && predictions.length > 0) setStart(false)
  }, [flaskBackendUrl, start])


  // rendu
  if (isLoading) return <Loading />
  return (
    <div>
      <ResponsiveContainer width="100%" height="100%">
        <AreaChart
          key={chartDataSales.length}
          data={chartDataSales.sort(data => data.unit_price)}
          margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
        >
          <CartesianGrid strokeDasharray="3 3" strokeOpacity={0.6} />

          <XAxis
            dataKey="price"
            label={{ value: "Prix Unitaire ($)", position: "insideBottom", offset: 0, fontSize: 12, marginTop: 10 }}
            tickFormatter={(tick) => `$${parseFloat(tick).toFixed(2)}`}
            tick={{ fontSize: 12 }}
            padding={{ left: 20, right: 20 }}
          />

          <YAxis
            label={{ value: "Ventes Prévues ($)", angle: -90, position: "insideLeft", fontSize: 12 }}
            tick={{ fontSize: 12 }}
            tickFormatter={(tick) => `$${tick.toLocaleString()}`}
          />

          {/* info-bulles avec les données de prédiction */}
          <Tooltip
            contentStyle={{
              borderRadius: '8px',
              padding: '10px',
              boxShadow: '0px 0px 15px rgba(0,0,0,0.5)'
            }}
            formatter={(value, name) => {
              if (name === 'sales') {
                return [`$${value.toFixed(4)}`, 'Ventes Prévues']
              }
              if (name === 'volume') {
                return [`${value.toFixed(0)}`, 'Volume']
              }
              return value
            }}
            labelFormatter={(label) => `Prix: $${label.toFixed(2)}`}
          />

          {/* zone du graphique = ventes */}
          <Area
            type="monotone"
            dataKey="sales"
            fillOpacity={1}
            fill="url(#colorSales)"
          />

          {/* ligne verticale pour le prix optimal */}
          {optimalPrice &&
            <ReferenceLine
              x={optimalPrice}
              strokeDasharray="4 4"
              ifOverflow="visible"
              label={{
                value: `Prix Optimal: $${optimalPrice !== null && optimalPrice > 0 ? Math.ceil(optimalPrice * 10000) / 10000 : ''}`,
                position: "right",
                fontSize: 12,
                offset: 10
              }}
            />
          }
        </AreaChart>
      </ResponsiveContainer>

      {optimalPrice && <p>Prix Optimal: $ {Math.ceil(optimalPrice * 10000) / 10000}</p>}

    </div>
  )
}

export default App
```

## Résultats finaux

Désormais, l'application est prête à être utilisée.

Vous pouvez explorer l'UI [ici](https://kuriko-iwai.vercel.app/online-commerce-intelligence-hub).

Tout le code (backend) est disponible dans [mon dépôt Github](https://github.com/krik8235/ml-sales-prediction).

## Conclusion

La construction d'un système de machine learning nécessite un cadrage de projet et une conception d'architecture réfléchis.

Dans cet article, nous avons construit un système de tarification dynamique via une architecture serverless conteneurisée.

À l'avenir, il faudra considérer les inconvénients potentiels de cette architecture minimale :

* **Augmentation de la durée du cold start** : La couche d'adaptation WSGI `awsgi` ajoute une légère surcharge. Le chargement d'une image de conteneur plus grande prend plus de temps.
    
* **Fonction monolithique :** L'ajout de points de terminaison à la fonction Lambda peut mener à une fonction monolithique.
    
* **Observabilité moins granulaire** : AWS CloudWatch ne fournit pas de métriques individuelles par point de terminaison API sans instrumentation personnalisée.

Pour faire évoluer l'application, l'extraction des fonctionnalités dans un nouveau microservice peut être une bonne stratégie pour l'étape suivante.

Je suis Kuriko IWAI, et vous pouvez trouver plus de mon travail ici :

[**Portfolio**](https://kuriko-iwai.vercel.app/) **/** [**LinkedIn**](https://www.linkedin.com/in/k-i-i/) **/** [**Github**](https://github.com/krik8235)

*Toutes les images sont de l'auteur. Cette application utilise un jeu de données synthétique sous licence Creative Commons Attribution 4.0 International (CC BY 4.0).*

*Ces informations sur AWS sont à jour en date d'août 2025 et sont sujettes à modification.*