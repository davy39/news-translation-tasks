---
title: Créer un générateur de captures d'écran de sites web avec Python et Flask
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2025-10-29T16:50:16.892Z'
originalURL: https://freecodecamp.org/news/build-a-website-screenshot-generator-with-python-and-flask
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761756575904/17a940c5-352e-47a2-992e-a1973c030c05.png
tags:
- name: Python
  slug: python
- name: Flask Framework
  slug: flask
seo_title: Créer un générateur de captures d'écran de sites web avec Python et Flask
seo_desc: 'Have you ever needed to take screenshots of websites automatically – maybe
  to track visual changes, include them in reports, or generate previews? Doing this
  manually can be time-consuming, especially if you need to capture multiple pages
  regularly.

  ...'
---

Avez-vous déjà eu besoin de prendre des captures d'écran de sites web automatiquement – peut-être pour suivre des changements visuels, les inclure dans des rapports ou générer des aperçus ? Faire cela manuellement peut prendre beaucoup de temps, surtout si vous devez capturer plusieurs pages régulièrement.

Dans ce tutoriel, vous apprendrez à construire un générateur simple de captures d'écran de sites web en utilisant Python et Flask. L'application permettra aux utilisateurs de saisir n'importe quelle URL de site web et d'obtenir instantanément une capture d'écran de cette page – le tout propulsé par une API de capture d'écran.

Vous utiliserez [**Flask**](https://blog.ashutoshkrris.in/getting-started-with-flask), un Framework web léger, pour créer une interface web simple et gérer les requêtes. Ensuite, vous intégrerez une API externe pour capturer des captures d'écran de sites web de manière programmatique.

À la fin de ce tutoriel, vous aurez appris à :

* Construire une application web Flask de base
    
* Accepter les entrées utilisateur via un formulaire HTML
    
* Effectuer des requêtes HTTP vers une API externe
    
* Afficher des images de manière dynamique sur une page web
    

Ce projet est un excellent moyen d'apprendre comment les API peuvent étendre les capacités de vos applications web, et comment Python peut facilement gérer des tâches telles que la génération et l'affichage d'images.

### Ce que nous allons aborder :

* [Prérequis](#heading-prerequis)
    
* [Configuration du projet](#heading-configuration-du-projet)
    
* [Intégration de l'API ScreenshotBase](#heading-integration-de-l-api-screenshotbase)
    
* [Ajout d'options de personnalisation](#heading-ajout-d-options-de-personnalisation)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer à construire l'application, assurez-vous d'avoir couvert quelques bases :

### 1\. Python installé

Vous aurez besoin de Python 3.9 ou supérieur installé sur votre machine. Vous pouvez vérifier votre version en exécutant :

```bash
python --version
```

Si vous ne l'avez pas, vous pouvez le télécharger sur [python.org/downloads](https://www.python.org/downloads/).

### 2\. Connaissances de base de Python et Flask

Vous n'avez pas besoin d'être un expert Flask. Ayez simplement une certaine familiarité avec la création de routes et de templates, et la gestion des données de formulaire dans Flask.

Si vous débutez avec Flask, ne vous inquiétez pas – nous irons étape par étape.

### 3\. Clé API de capture d'écran

Nous utiliserons l'[**API ScreenshotBase**](https://screenshotbase.com/) pour capturer les captures d'écran des sites web. Elle fournit un endpoint REST simple qui prend une URL et renvoie une image de capture d'écran.

Vous pouvez obtenir une clé API gratuite en vous inscrivant sur leur site web. Une fois que vous avez la clé, gardez-la à portée de main, car nous l'utiliserons lors de l'intégration de l'API dans les étapes ultérieures.

### 4\. Un éditeur de code et un terminal

Vous pouvez utiliser n'importe quel éditeur que vous préférez, comme VS Code, PyCharm ou même un simple éditeur de texte. Assurez-vous que votre terminal ou invite de commande peut exécuter des commandes Python et installer des packages via `pip`.

## Configuration du projet

Commençons par configurer un nouveau projet Flask à partir de zéro.

### Étape 1 : Créer un nouveau dossier

Créez un nouveau dossier pour votre projet. Vous pouvez le nommer `screenshot-generator` :

```bash
mkdir screenshot-generator
cd screenshot-generator
```

### Étape 2 : Créer un environnement virtuel

Un environnement virtuel aide à garder les dépendances de votre projet isolées des autres projets Python.

Exécutez les commandes suivantes :

```bash
python -m venv venv
```

Ensuite, activez-le :

* Sur macOS/Linux :
    
    ```bash
    source venv/bin/activate
    ```
    
* Sur Windows :
    
    ```bash
    venv\Scripts\activate
    ```
    

Une fois activé, vous devriez voir `(venv)` au début de votre invite de terminal.

### Étape 3 : Installer les dépendances

Nous aurons besoin de deux packages pour ce projet :

* **Flask** pour construire l'application web
    
* **Requests** pour effectuer des appels API vers ScreenshotBase
    

Installez-les via pip :

```bash
pip install flask requests
```

### Étape 4 : Configurer la structure du projet

À l'intérieur de votre dossier de projet, créez les fichiers et dossiers suivants :

```bash
screenshot-generator/
├── app.py
├── templates/
│   └── index.html
└── static/
```

Voici le rôle de chaque partie :

* `app.py` : fichier Python principal qui exécute votre application Flask
    
* `templates/` : stocke les templates HTML
    
* `static/` : stocke les images, le CSS et les fichiers JavaScript
    

### Étape 5 : Ajouter une application Flask de base

Ouvrez `app.py` et ajoutez le code de départ suivant :

```python
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
API_KEY = os.getenv("SCREENSHOTBASE_API_KEY")
SCREENSHOTBASE_BASE_ENDPOINT = "https://api.screenshotbase.com/v1/take"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        # Placeholder: Nous ajouterons l'appel API ici dans la section suivante
        return render_template('index.html', url=url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Ceci configure une application Flask minimale avec une route (`/`). Nous ajouterons l'appel à l'API ScreenshotBase dans la section suivante.

### Étape 6 : Créer un template HTML simple

Maintenant que nous avons écrit le backend Flask pour gérer la demande de capture d'écran, créons le frontend pour notre application.

À l'intérieur de votre dossier de projet, créez un nouveau répertoire nommé `templates`, et à l'intérieur, ajoutez un fichier appelé `index.html`. Flask cherchera automatiquement les templates dans ce dossier.

Voici à quoi devrait ressembler le template :

```xml
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Générateur de captures d'écran de sites web</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB"
      crossorigin="anonymous"
    />
    <style>
        body {
            padding-top: 2rem;
        }
        .screenshot-container {
            max-height: 80vh;
            overflow-y: auto;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 1rem;
            background: #f8f9fa;
        }
    </style>
</head>
<body>
    <div class="container text-center">
        <h1 class="mb-4">Générateur de captures d'écran de sites web</h1>
        <form method="POST" class="d-flex justify-content-center mb-4">
            <input 
                type="text" 
                name="url" 
                placeholder="Entrez l'URL du site web" 
                class="form-control w-50 me-2"
                required
            >
            <button type="submit" class="btn btn-primary">Capturer</button>
        </form>

        {% if screenshot %}
            <h4>Aperçu de la capture d'écran :</h4>
            <div class="screenshot-container mx-auto">
                <img src="{{ screenshot }}" alt="Capture d'écran du site web" class="img-fluid rounded shadow">
            </div>
        {% elif request.method == 'POST' %}
            <div class="alert alert-danger mt-3">
                Désolé, une erreur s'est produite lors de la capture d'écran. Veuillez réessayer.
            </div>
        {% endif %}
    </div>
</body>
</html>
```

Ce template HTML utilise Bootstrap pour garder le design propre et réactif sans trop de styles personnalisés. Le formulaire en haut permet aux utilisateurs de saisir n'importe quelle URL de site web et de la soumettre à l'application Flask via la méthode `POST`. Une fois que l'application récupère l'URL de la capture d'écran de l'API, elle affiche dynamiquement l'image sur la page.

La classe `img-fluid` de Bootstrap garantit que la capture d'écran s'adapte correctement à toutes les tailles d'écran tout en conservant son ratio d'aspect. De plus, le `.screenshot-container` fournit une zone défilante, ce qui aide à afficher des captures d'écran de pages complètes sans trop les réduire ou casser la mise en page.

Maintenant, votre projet est configuré et prêt à capturer de vraies captures d'écran en utilisant l'API ScreenshotBase.

Dans la section suivante, nous écrirons la logique pour appeler l'API ScreenshotBase et afficher la capture d'écran résultante dynamiquement dans le navigateur.

## Intégration de l'API ScreenshotBase

Maintenant que notre application Flask est configurée, connectons-la à l'API ScreenshotBase afin de pouvoir générer de réelles captures d'écran à partir de n'importe quelle URL.

### Étape 1 : Comprendre l'endpoint de l'API

L'API ScreenshotBase fournit un endpoint simple qui prend une URL de site web et renvoie une image de capture d'écran.

Un appel API typique ressemble à ceci :

```bash
GET https://api.screenshotbase.com/v1/take
```

Vous envoyez l'URL du site cible en tant que paramètre de requête (`url`) et incluez votre clé API dans l'en-tête de la requête sous le nom `apikey`.

Voici l'exemple cURL de leur documentation :

```bash
curl -G https://api.screenshotbase.com/v1/take?url=https%3A%2F%2Fbbc.com \
    -H "apikey: VOTRE-CLE-API"
```

Cette requête capture une capture d'écran de `https://bbc.com` et renvoie l'image de la capture d'écran en réponse.

### Étape 2 : Ajouter l'appel API dans Flask

Mettons à jour notre route `home` dans `app.py` pour envoyer une requête à l'API ScreenshotBase lorsqu'un utilisateur soumet une URL.

Voici la version mise à jour de `app.py` :

```python
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
API_KEY = os.getenv("SCREENSHOTBASE_API_KEY")
SCREENSHOTBASE_BASE_ENDPOINT = "https://api.screenshotbase.com/v1/take"

@app.route('/', methods=['GET', 'POST'])
def home():
    screenshot_url = None

    if request.method == 'POST':
        target_url = request.form.get('url')

        params = {"url": target_url}
        headers = {"apikey": API_KEY}

        try:
            # Envoyer une requête GET à l'API ScreenshotBase
            response = requests.get(SCREENSHOTBASE_BASE_ENDPOINT, params=params, headers=headers, timeout=30)
            response.raise_for_status()

            # Sauvegarder l'image retournée
            image_path = os.path.join('static', 'screenshot.png')
            with open(image_path, 'wb') as f:
                f.write(response.content)

            screenshot_url = image_path

        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la capture d'écran : {e}")

    return render_template('index.html', screenshot=screenshot_url)

if __name__ == '__main__':
    app.run(debug=True)
```

Voici ce que fait ce code :

1. Capture l'entrée utilisateur (URL).
    
2. Envoie une requête GET à l'endpoint `/v1/take`.
    
3. Transmet votre clé API dans l'en-tête de la requête (`apikey`).
    
4. Sauvegarde l'image retournée dans le dossier `static`.
    
5. Affiche la capture d'écran sur la page.
    

### Étape 3 : Tester votre application

Lancez à nouveau l'application :

```python
python app.py
```

Ensuite, ouvrez [http://127.0.0.1:5000](http://127.0.0.1:5000) dans votre navigateur.

Entrez une URL comme :

```python
https://github.com/ashutoshkrris
```

Après avoir soumis, vous devriez voir la capture d'écran de ce site web s'afficher sous le formulaire.

Votre application Flask est maintenant pleinement fonctionnelle ! Elle prend une URL, l'envoie à l'API ScreenshotBase et affiche la capture d'écran résultante.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1761133080971/d0feb78c-09cb-4f01-b254-a56fca3a58c8.png align="center")

Dans la section suivante, nous améliorerons l'application en ajoutant des options de personnalisation telles que les captures d'écran de pages complètes, les paramètres de viewport et les délais. Plus tard, nous explorerons les SDK ScreenshotBase pour les langages populaires comme Python, Node.js et PHP.

## Ajout d'options de personnalisation

Pour l'instant, notre application prend simplement une capture d'écran de l'URL du site web donné en utilisant les paramètres par défaut. Cependant, la plupart des API de capture d'écran (y compris celle que nous utilisons) vous permettent de personnaliser la sortie en passant des paramètres supplémentaires dans la requête.

L'API ScreenshotBase offre plusieurs options de personnalisation puissantes pour vous aider à adapter chaque capture d'écran à vos besoins :

* **Format d'image** : Choisissez entre `png`, `jpg`, `gif` ou `webp`, selon vos exigences de qualité d'image ou de compression.
    
* **Capture de page complète** : Capturez l'intégralité de la page web défilante (`full_page=1`) ou juste le viewport visible (`full_page=0`).
    
* **Dimensions du viewport** : Définissez la taille de la fenêtre du navigateur avec `viewport_width` et `viewport_height` pour simuler des captures d'écran d'écrans de bureau, de tablette ou de mobile.
    

Ces options rendent ScreenshotBase idéal pour construire des outils d'automatisation, des générateurs de miniatures, des tableaux de bord de test et des systèmes de documentation visuelle. Ajoutons ces options pour rendre notre générateur de captures d'écran plus flexible.

### Mise à jour du code Flask

Ouvrez votre fichier `app.py` et mettez à jour la route qui gère les soumissions de formulaires pour inclure ces paramètres optionnels :

```python
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
API_KEY = os.getenv("SCREENSHOTBASE_API_KEY", "scr_live_9Qkn1gs01rivZqrFk7lusXPiqAUg85J86aU6bHvG")
SCREENSHOTBASE_BASE_ENDPOINT = "https://api.screenshotbase.com/v1/take"


@app.route('/', methods=['GET', 'POST'])
def home():
    screenshot_url = None

    if request.method == 'POST':
        target_url = request.form.get('url')
        format_ = request.form.get('format', 'png')
        full_page = request.form.get('full_page') == 'on'

        params = {
            "url": target_url,
            "format": format_,
            "full_page": int(full_page)
        }
        headers = {"apikey": API_KEY}

        try:
            # Envoyer une requête GET à l'API ScreenshotBase
            response = requests.get(SCREENSHOTBASE_BASE_ENDPOINT, params=params, headers=headers, timeout=30)
            response.raise_for_status()

            # Sauvegarder l'image retournée
            image_extension = format_ if format_ != 'jpeg' else 'jpg'
            image_path = os.path.join('static', f'screenshot.{image_extension}')
            with open(image_path, 'wb') as f:
                f.write(response.content)

            screenshot_url = image_path

        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la capture d'écran : {e}")

    return render_template('index.html', screenshot=screenshot_url)
    

if __name__ == '__main__':
    app.run(debug=True)
```

### Mise à jour du template HTML

Ensuite, modifions le formulaire dans notre `index.html` pour inclure les options de personnalisation :

```xml
<form method="POST" class="d-flex flex-column justify-content-center mb-4">
  <!-- URL et bouton de soumission sur une seule ligne -->
  <div class="input-group mb-4">
    <input
      type="text"
      name="url"
      placeholder="Entrez l'URL du site web"
      class="form-control w-50 me-2"
      required
    />
    <button type="submit" class="btn btn-primary">Capturer</button>
  </div>

  <!-- Options sur deux colonnes -->
  <div class="row g-3">
    <!-- Case à cocher Page Complète -->
    <div class="col-md-6">
      <div class="form-check">
        <input
          type="checkbox"
          name="full_page"
          id="full_page"
          class="form-check-input"
        />
        <label class="form-check-label" for="full_page">
          Capturer la page complète
        </label>
      </div>
    </div>

    <!-- Menu déroulant Format -->
    <div class="col-md-6">
      <label for="format" class="form-label">Format de capture</label>
      <select class="form-select" name="format" id="format" required>
        <option value="png">PNG</option>
        <option value="jpg">JPG</option>
        <option value="gif">GIF</option>
        <option value="webp">WEBP</option>
      </select>
    </div>

    <!-- Largeur du Viewport -->
    <div class="col-md-6">
      <label for="viewport_width" class="form-label">Largeur du Viewport</label>
      <input
        type="number"
        name="viewport_width"
        id="viewport_width"
        class="form-control"
        value="1280"
        min="320"
      />
    </div>

    <!-- Hauteur du Viewport -->
    <div class="col-md-6">
      <label for="viewport_height" class="form-label">Hauteur du Viewport</label>
      <input
        type="number"
        name="viewport_height"
        id="viewport_height"
        class="form-control"
        value="720"
        min="320"
      />
    </div>
  </div>
</form>
```

Le formulaire mis à jour donne aux utilisateurs le contrôle sur la manière dont la capture d'écran est générée. Le menu déroulant de format leur permet de choisir entre PNG, JPG, GIF ou WEBP. La case à cocher Page Complète permet de choisir si l'API capture l'intégralité de la page web défilante ou juste le viewport visible. Les champs de largeur et de hauteur du viewport définissent les dimensions de la fenêtre du navigateur, ce qui est utile si vous souhaitez simuler différentes tailles d'appareils ou des mises en page réactives.

Lorsque le formulaire est soumis, Flask lit ces valeurs et les envoie en tant que paramètres de requête dans la demande API.

Par exemple, une requête pour capturer une capture d'écran PNG de 1920×1080 en page complète de votre site ressemblerait à ceci :

```xml
https://api.screenshotbase.com/v1/take?url=https%3A%2F%2Fgithub.com%2Fashutoshkrris&format=png&full_page=1&viewport_width=1920&viewport_height=1080
```

Cette flexibilité permet d'affiner facilement les captures d'écran pour différents cas d'utilisation – que vous génériez des miniatures, testiez la réactivité ou automatisiez des rapports visuels.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1761134646387/b9145271-303f-408e-ab53-444ea125849e.gif align="center")

Note : Si vous préférez travailler avec des SDK plutôt qu'avec des appels API directs, ScreenshotBase propose également des SDK officiels pour les langages populaires comme Python, JavaScript, Ruby, PHP et Go.

Ces SDK offrent un moyen plus simple et plus pratique d'interagir avec l'API, en gérant l'authentification et le formatage des requêtes en arrière-plan.

Vous pouvez les explorer dans la [documentation du SDK ScreenshotBase](https://screenshotbase.com/docs/sdks).

## Conclusion

Dans ce tutoriel, vous avez appris à construire une application Flask simple qui capture des captures d'écran de sites web en utilisant une API tierce. Nous avons exploré comment envoyer des requêtes, gérer les réponses d'images et ajouter des options de personnalisation telles que le format d'image, la capture de page complète et la taille du viewport – tout en gardant le projet léger et facile à étendre.

Ce petit projet démontre comment les tâches d'automatisation web, telles que la génération d'aperçus ou de rapports visuels, peuvent être simplifiées à l'aide d'API modernes. Vous pouvez vous appuyer sur cette base pour créer des outils de capture d'écran par lots, des systèmes de surveillance visuelle ou même intégrer des captures d'écran dans des applications web plus larges.

Le point clé à retenir est de comprendre comment interagir avec des API externes, traiter les réponses et concevoir une interface propre pour les utilisateurs. Ce sont des compétences essentielles pour les développeurs backend et full-stack.