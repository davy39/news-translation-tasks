---
title: Comment utiliser Nano Banana pour la génération d'images - Expliqué avec des
  exemples de code
subtitle: ''
author: Tarun Singh
co_authors: []
series: null
date: '2025-09-19T13:20:23.501Z'
originalURL: https://freecodecamp.org/news/nano-banana-for-image-generation
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758287738949/b33b68f4-0e84-46df-a85f-9ff6aacfd72c.png
tags:
- name: image processing
  slug: image-processing
- name: AI
  slug: ai
- name: Python
  slug: python
seo_title: Comment utiliser Nano Banana pour la génération d'images - Expliqué avec
  des exemples de code
seo_desc: AI is changing the image generation and editing process into a smooth workflow.
  Now, with just a single prompt, you can tell your computer to generate or edit an
  existing image. Google just launched its new model for image generation or editing,
  "Nan...
---

L'IA transforme le processus de génération et d'édition d'images en un flux de travail fluide. Désormais, avec un seul prompt, vous pouvez demander à votre ordinateur de générer ou de modifier une image existante. Google vient de lancer son nouveau modèle pour la génération ou l'édition d'images, ["Nano Banana" – Gemini 2.5 Flash](https://gemini.google/overview/image-generation/). C'est un outil puissant et agile qui change notre façon de concevoir la génération et la manipulation d'images, et c'est un outil que vous voudrez certainement avoir dans votre boîte à outils de développeur.

Dans cet article, vous apprendrez comment utiliser « Nano Banana » pour la génération d'images à l'aide de Gemini 2.5 Flash Image. Alors, c'est parti !

## Table des matières

* [Qu'est-ce que « Nano Banana » ?](#heading-quest-ce-que-nano-banana)
    
    * [Pourquoi « Nano Banana » ?](#heading-pourquoi-nano-banana)
        
* [Configuration de votre projet](#heading-configuration-de-votre-projet)
    
    * [Étape 1 : Obtenir une clé API de Google Gemini](#heading-etape-1-obtenir-une-cle-api-de-google-gemini)
        
    * [Étape 2 : Installer le SDK et les autres dépendances](#heading-etape-2-installer-le-sdk-et-les-autres-dependances)
        
    * [Étape 3 : Configurer votre environnement](#heading-etape-3-configurer-votre-environnement)
        
    * [Étape 4 : Génération et édition d'images](#heading-etape-4-generation-et-edition-dimages)
        
* [Au-delà des bases : que pouvez-vous faire d'autre ?](#heading-au-dela-des-bases-que-pouvez-vous-faire-dautre)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que « Nano Banana » ?

Nano Banana est le dernier outil hybride d'édition et de génération d'images de Google DeepMind. Oubliez un instant le jargon formel. Imaginez que vous avez à votre disposition un artiste incroyablement talentueux et rapide comme l'éclair. Vous pouvez lui décrire *n'importe quoi* – « un astronaute chevauchant un cheval sur la Lune » – et *pouf*, l'image apparaît. Ou bien, vous lui donnez une photo de votre chien et dites : « Fais en sorte que le chien porte une casquette sur la tête », et il le fait instantanément, tout en gardant votre chien reconnaissable.

C'est essentiellement cela, Nano Banana. C'est un modèle d'IA avancé de la famille Gemini, spécifiquement conçu pour la génération rapide et intelligente d'images et l'édition nuancée. Il comprend vos commandes en langage naturel, vous permettant de donner vie à des idées visuelles complexes ou d'apporter des modifications chirurgicales à des images existantes avec une facilité surprenante.

### Pourquoi « Nano Banana » ?

Parce qu'il est petit (flash !), plein de qualités, et vous donne l'impression de venir de découvrir une nouvelle couche de possibilités créatives. Il est rapide, efficace et incroyablement polyvalent.

**Les super-pouvoirs que vous obtenez :**

* **Édition parfaite par prompt :** Vous voulez changer un arrière-plan, modifier une pose ou ajouter un objet spécifique ? Demandez simplement. Nano Banana comprend et exécute.
    
* **Cohérence des personnages :** C'est un point crucial. Si vous créez une histoire ou une série d'images, maintenir l'apparence d'un personnage ou d'un objet spécifique est essentiel. Nano Banana excelle dans ce domaine, garantissant que votre protagoniste garde le même aspect, qu'il soit dans une forêt ou sur la lune.
    
* **Mashups visuels (Fusion multi-images) :** Vous avez plusieurs éléments visuels différents que vous souhaitez combiner de manière transparente ? Il peut les fusionner en une nouvelle image cohérente.
    

et bien plus encore !

Intéressé ? Passons à la pratique. Mais attendez ! Pour utiliser « Nano Banana », vous avez deux façons de procéder :

1. [Utiliser Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-2.5-flash-image-preview) : Le moyen le plus simple et le plus facile de générer ou d'éditer des images dans Google Studio. Il s'agit d'un outil Web qui vous donne un accès direct aux modèles Gemini sans écrire une seule ligne de code. C'est l'endroit idéal pour tester et commencer, et c'est utile aussi bien pour les développeurs que pour les non-développeurs. De plus, il n'est pas nécessaire d'installer des bibliothèques, de gérer des clés API ou d'écrire du code.
    
2. **Développer avec l'API Gemini :** C'est avantageux si vous souhaitez des solutions plus personnalisées pour votre application. Pour toute application sérieuse — qu'il s'agisse d'une application Web, d'une application mobile ou d'un service backend — vous devrez vous intégrer directement à l'API Gemini. C'est là que réside la véritable puissance, car cela vous permet d'automatiser des tâches et de créer des expériences interactives.
    

Dans ce tutoriel, vous verrez comment nous pouvons utiliser cet outil dans nos propres applications, en utilisant uniquement Python. Alors, commençons.

## Configuration de votre projet

### Étape 1 : Obtenir une clé API de Google Gemini

La toute première étape pour utiliser « Nano Banana » est d'obtenir une clé API. Rendez-vous sur [Google AI Studio](https://aistudio.google.com/apikey), cliquez sur « Create API key », et générez-en une nouvelle en spécifiant un projet parmi vos projets Google Cloud existants.

![Clé API générée depuis Google Gemini](https://cdn.hashnode.com/res/hashnode/image/upload/v1757429573699/1c5d1a52-2e63-476b-a957-604542044fc7.png align="center")

Une fois que vous avez généré une clé API, enregistrez-la en toute sécurité quelque part.

### Étape 2 : Installer le SDK et les autres dépendances

Ouvrez votre terminal et exécutez :

```bash
pip install google-generativeai pillow python-dotenv
```

Nous utiliserons `Pillow` pour une manipulation facile des images et `python-dotenv` pour gérer notre clé API en toute sécurité.

### Étape 3 : Configurer votre environnement

Il est crucial de garder votre clé API hors de votre code pour des raisons de sécurité. Pour cela, nous utilisons généralement des variables d'environnement. Créez donc un fichier nommé `.env` à la racine de votre projet et ajoutez votre clé API :

```bash
GEMINI_API_KEY="VOTRE_CLE_API_ICI"
```

### Étape 4 : Génération et édition d'images

**Exemple 1 : Génération de texte en image (Text-to-Image)**

Le Text-to-Image est comme un artiste qui peut dessiner tout ce que vous décrivez. Ici, vous écrivez simplement le prompt (une phrase ou une description), même très détaillé, et l'IA générera une image unique et de haute qualité correspondant à votre description. C'est parfait pour donner vie à vos idées les plus imaginatives avec seulement quelques mots.

```python
import os
import google.generativeai as genai
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Configuration
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash-image-preview')

# Configuration du prompt, de l'image et de la réponse
prompt = "Un chiot golden retriever assis dans un champ de marguerites, lumineux et joyeux"
output_filename = "resultat_texte_vers_image.png"

# Fonction utilitaire pour sauvegarder l'image à partir de la réponse du prompt textuel
def save_image_from_response(response, filename):
    """Fonction utilitaire pour sauvegarder l'image de la réponse API."""
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                image_data = BytesIO(part.inline_data.data)
                img = Image.open(image_data)
                img.save(filename)
                print(f"Image sauvegardée avec succès sous {filename}")
                return filename
    print("Aucune donnée d'image trouvée dans la réponse.")
    return None

def main():
    print(f"Génération de l'image pour le prompt : '{prompt}'...")
    response = model.generate_content(prompt)
    save_image_from_response(response, output_filename)

if __name__ == "__main__":
    main()
```

**Sortie :**

![Un chiot golden retriever assis joyeusement dans une prairie ensoleillée remplie de marguerites blanches, entouré d'herbe verte et d'une atmosphère vibrante et joyeuse.](https://cdn.hashnode.com/res/hashnode/image/upload/v1757485705896/50484418-c53c-4d61-8846-2c8875dc2cbd.png align="center")

Le code utilisé dans l'exemple gère tout ce qui est nécessaire pour communiquer avec l'API Gemini et sauvegarder l'image.

* Tout d'abord, nous importons les bibliothèques requises et chargeons la clé API depuis le fichier `.env` à l'aide de `load_dotenv()`. Cela rend la clé disponible pour nous connecter au service de Google avec `genai.configure()`.
    
* Le modèle que nous utilisons est `gemini-2.5-flash-image-preview`, conçu pour une génération d'images rapide.
    
* Nous définissons un `prompt` `("Un chiot golden retriever...")` et un nom de fichier pour sauvegarder l'image.
    
* La fonction utilitaire `save_image_from_response(...)` examine la réponse de l'API, extrait les données brutes de l'image et les sauvegarde sous forme de fichier PNG.
    
* Dans `main()`, nous appelons le modèle avec le prompt, puis passons la réponse à la fonction utilitaire pour sauvegarder le résultat.
    
* Le bloc `if __name__ == "__main__":` garantit que le script ne s'exécute que lorsqu'il est lancé directement, et non lorsqu'il est importé.
    

**Exemple 2 : Édition d'image à image (Image-to-Image)**

L'Image-to-Image est comme un éditeur de photos. Au lieu de partir de zéro, vous pouvez télécharger une photo existante et décrire comment la modifier. Par exemple, vous pouvez demander la suppression de l'arrière-plan, l'ajout de nouveaux objets ou même un changement complet de style artistique.

```python
import os
import google.generativeai as genai
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Configuration
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash-image-preview')

# Configuration du prompt, de l'image et de la réponse
input_image_path = "chien_entree.png"
prommpt = "Faites porter au chien un petit chapeau de sorcier et des lunettes."
output_filename = "resultat_image_editee.png"

# Fonction utilitaire pour sauvegarder l'image
def save_image_from_response(response, filename):
    """Fonction utilitaire pour sauvegarder l'image de la réponse API."""
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                image_data = BytesIO(part.inline_data.data)
                img = Image.open(image_data)
                img.save(filename)
                print(f"Image sauvegardée avec succès sous {filename}")
                return filename
    print("Aucune donnée d'image trouvée dans la réponse.")
    return None

def main():
    print(f"Édition de l'image '{input_image_path}' avec le prompt : '{prommpt}'...")
    try:
        img_to_edit = Image.open(input_image_path)
        response = model.generate_content([prommpt, img_to_edit])
        save_image_from_response(response, output_filename)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{input_image_path}' n'a pas été trouvé.")

if __name__ == "__main__":
    main()
```

**Sortie :**

![Une image avant et après d'un chien joueur portant un petit chapeau de sorcier pointu et des lunettes rondes, assis bien droit avec un look charmant et magique, donnant une impression de livre de contes fantaisiste.](https://cdn.hashnode.com/res/hashnode/image/upload/v1757486336530/84cba4bf-91bd-49b7-8fd3-e94b20eabbfb.png align="center")

Ce code est très similaire au premier exemple, mais la différence clé réside dans la logique centrale.

* `input_image_path` : Cette variable contient désormais le chemin du fichier de l'image que vous souhaitez éditer.
    
* [`Image.open`](http://Image.open)`(input_image_path)` : Cette ligne utilise la bibliothèque Pillow pour ouvrir votre fichier image local à utiliser.
    
* `model.generate_content([prommpt, img_to_edit])` : C'est la partie la plus importante. Contrairement à précédemment, nous passons maintenant une liste à la fonction `generate_content` qui contient à la fois le prompt textuel et l'objet image. Cela indique à l'API d'utiliser l'image fournie comme point de départ pour sa génération.
    
* Bloc `try...except` : Ici, nous gérons les erreurs. Il tente d'ouvrir le fichier image, et s'il échoue (parce que le fichier n'est pas là), il interceptera l'erreur `FileNotFoundError` et affichera un message convivial à l'utilisateur au lieu de planter.
    

**Exemple 3 : Fusion multi-images (Multi-Image Fusion)**

La fusion multi-images consiste à fusionner deux ou plusieurs images ou objets. Téléchargez plusieurs images et demandez à l'IA de les mélanger en une seule image composite de manière transparente. C'est un outil pour créer de nouvelles scènes, combiner des personnes et des arrière-plans, ou créer des maquettes de produits détaillées.

```python
import os
import google.generativeai as genai
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Configuration
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash-image-preview')

# Configuration du prompt, des images et de la réponse
image1_path = "image_chien.png"
image2_path = "image_casquette.png"
prompt = "Faites porter au chien de la première image la casquette de la deuxième image. La casquette doit être ajustée de manière réaliste sur la tête du chien."
output_filename = "resultat_chien_avec_casquette.png"

def save_image_from_response(response, filename):
    """Fonction utilitaire pour sauvegarder l'image de la réponse API."""
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                image_data = BytesIO(part.inline_data.data)
                img = Image.open(image_data)
                img.save(filename)
                print(f"Image sauvegardée avec succès sous {filename}")
                return filename
    print("Aucune donnée d'image trouvée dans la réponse.")
    return None

def main():
    print(f"Fusion des images '{image1_path}' et '{image2_path}'...")
    try:
        img1 = Image.open(image1_path)
        img2 = Image.open(image2_path)
        response = model.generate_content([prompt, img1, img2])
        save_image_from_response(response, output_filename)
    except FileNotFoundError:
        print("Erreur : L'un des fichiers image ou les deux n'ont pas été trouvés.")

if __name__ == "__main__":
    main()
```

**Sortie :**

![Image en trois parties montrant un chiot golden retriever dans un champ de marguerites, une casquette de baseball rouge avec la lettre « A », et la version finale éditée où le chiot porte la casquette rouge tout en étant assis joyeusement parmi les marguerites](https://cdn.hashnode.com/res/hashnode/image/upload/v1757486318798/2fe3ca32-3053-44cc-9350-b1c47abacdd9.png align="center")

La logique du code ci-dessus est une extension de l'exemple Image-to-Image.

* `image1_path` et `image2_path` : Ces variables contiennent les chemins vers les deux images que vous souhaitez fusionner ou mélanger.
    
* `model.generate_content([prompt, img1, img2])` : Ici, la liste passée à la fonction `generate_content` contient trois éléments : le prompt textuel et les deux objets image. Cela indique à l'IA d'utiliser le prompt pour combiner les éléments des deux images en une seule sortie.
    

**Exemple 4 : Restauration d'image**

Cette fonctionnalité peut restaurer des photos anciennes, décolorées ou endommagées. Téléchargez une photo et demandez à Gemini de la restaurer. Cela inclut la netteté des images de mauvaise qualité, la colorisation de vieilles photos en noir et blanc et l'amélioration des textures, ce qui peut redonner vie à vos souvenirs.

```python
import os
import google.generativeai as genai
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Configuration
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash-image-preview')

# Configuration du prompt, de l'image et de la réponse
input_image_path = "vieille_photo.png"
prompt = "Restaurez cette vieille photographie décolorée. Améliorez la netteté des détails, supprimez les rayures ou les dommages, et rehaussez les couleurs pour qu'elle ressemble à une photo neuve de haute qualité."
output_filename = "resultat_image_restauree.png"

def save_image_from_response(response, filename):
    """Fonction utilitaire pour sauvegarder l'image de la réponse API."""
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                image_data = BytesIO(part.inline_data.data)
                img = Image.open(image_data)
                img.save(filename)
                print(f"Image sauvegardée avec succès sous {filename}")
                return filename
    print("Aucune donnée d'image trouvée dans la réponse.")
    return None

def main():
    print(f"Tentative de restauration de l'image : '{input_image_path}'...")
    try:
        old_photo = Image.open(input_image_path)
        response = model.generate_content([prompt, old_photo])
        save_image_from_response(response, output_filename)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{input_image_path}' n'a pas été trouvé.")

if __name__ == "__main__":
    main()
```

**Sortie :**

![Comparaison côte à côte d'une vieille photographie et d'une version restaurée. À gauche, une photo sépia rayée d'une voiture ancienne sur une route rurale, tandis qu'à droite, la même scène est restaurée numériquement en couleur, avec une voiture classique bleue sous un ciel radieux dans une campagne dorée](https://cdn.hashnode.com/res/hashnode/image/upload/v1757486506412/201bf046-4c63-46eb-a026-f2a432ca8c3d.png align="center")

La structure ici est identique à l'exemple d'édition d'image à image car, d'un point de vue technique, la restauration d'image est une forme d'édition d'image à image.

* C'est dans le `prompt` que la magie opère. Le prompt textuel indique explicitement au modèle ce qu'il doit faire de l'image, en soulignant les étapes de restauration telles que « améliorer la netteté des détails », « supprimer les rayures » et « rehausser les couleurs ». L'intelligence du modèle lui permet de comprendre ces instructions abstraites et de les appliquer aux données visuelles pour vous donner une mise à jour meilleure et réaliste de votre ancienne image.
    

## Au-delà des bases : que pouvez-vous faire d'autre ?

Ce n'est que la partie émergée de l'iceberg ! Nano Banana est incroyablement polyvalent. Voici quelques idées pour vos projets :

* **Traitement par lots :** Automatisez la génération de plusieurs images à partir d'une liste de prompts.
    
* **Ressources créatives :** Concevez des icônes, des arrière-plans ou des sprites de personnages pour des jeux ou des applications directement depuis votre script Python.
    
* **Traitement de données :** Intégrez Nano Banana dans un pipeline de données pour éditer ou générer des images par programmation en fonction des entrées de données.
    
* **Galeries d'art IA :** Créez un service backend qui permet aux utilisateurs de soumettre des prompts et de recevoir des images.
    

## Conclusion

« Nano Banana » (Gemini 2.5 Flash Image) n'est pas seulement un outil technologique cool ; c'est un outil pratique et puissant pour les développeurs et les créatifs. Avec seulement quelques lignes de code, vous pouvez exploiter ses capacités et donner vie à vos idées visuelles. Cette approche simplifiée facilite le démarrage, l'expérimentation et l'intégration de cette magie visuelle dans vos projets.

Si vous avez trouvé cet article utile et souhaitez discuter du développement de l'IA, des LLM ou du développement logiciel, n'hésitez pas à me contacter sur [X/Twitter](https://x.com/itsTarun24), [LinkedIn](https://www.linkedin.com/in/tarunsingh24), ou à consulter mon portfolio sur mon [Blog](http://tarunportfolio.vercel.app/blog). Je partage régulièrement des informations sur l'IA, le développement, la rédaction technique et bien plus encore.

Bon codage, et puissent vos créations être aussi vibrantes qu'un champ de bananes fraîches !