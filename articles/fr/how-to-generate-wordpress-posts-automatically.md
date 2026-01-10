---
title: Comment générer des articles WordPress automatiquement avec Python
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2022-08-22T20:55:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-wordpress-posts-automatically
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/-.png
tags:
- name: automation
  slug: automation
- name: Python
  slug: python
- name: WordPress
  slug: wordpress
seo_title: Comment générer des articles WordPress automatiquement avec Python
seo_desc: 'If you run a website, you are aware of the importance of content. It''s
  important for your web presence, to help you be recognized as a leader in your field,
  to improve your SEO ranking, to increase your audience, and more.

  WordPress is one of the mos...'
---

Si vous gérez un site web, vous connaissez l'importance du contenu. Il est essentiel pour votre présence en ligne, pour vous faire reconnaître comme un leader dans votre domaine, pour améliorer votre classement SEO, pour augmenter votre audience, et bien plus encore.

WordPress est l'un des outils les plus populaires et largement utilisés pour créer des blogs, des plateformes e-commerce et des sites web.

Dans cet article, je vais vous montrer comment créer du contenu automatiquement et le publier sur votre site WordPress avec Python. 

Voici comment cela fonctionne :

* Nous allons récupérer du contenu depuis notre source (par exemple, un autre site web que nous gérons)
* Nous allons le traduire dans notre langue
* Nous allons choisir une image à la une déjà disponible sur notre site et enfin le publier sur notre instance WordPress en tant qu'article.

Le script que nous allons développer peut être utile si vous souhaitez créer du contenu dans une autre langue rapidement pour élargir votre audience. 

Imaginons que vous avez un webzine avec du contenu écrit en anglais et que vous souhaitez que les utilisateurs hispanophones commencent à lire vos articles. Vous pouvez créer un nouveau blog et exécuter votre script pour obtenir vos articles traduits en espagnol et prêts à être lus par vos utilisateurs.

## Commençons 

Voici le script que nous allons développer à la fin de cet article :

```python
import requests
import json
import random
from googletrans import Translator
from requests.auth import HTTPBasicAuth

def post_creator(sourceURL, wpBaseURL, sourceLang, targetLang, postStatus):
    response_API = requests.get(sourceURL)
    data = response_API.text
    parse_json = json.loads(data)
    get_article_title = parse_json['title']
    get_article_content = parse_json['body']
    image_list = ["1689","1594","1612"]

    translator = Translator()

    title_translation = translator.translate(get_article_title, src=sourceLang, dest=targetLang)
    title_translation_text = title_translation.text 

    content_translation = translator.translate(get_article_content, src=sourceLang, dest=targetLang)
    content_translation_text = content_translation.text 

    random_image_list = random.choice(image_list)
 
    WP_url = wpBaseURL + "/wp-json/wp/v2/posts"

    auth = HTTPBasicAuth(<USERNAME>, <PASSWORD>)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps({ 
        "status":postStatus,
        "title": title_translation_text,
        "content": content_translation_text,
        "featured_media": random_image_list
    })

    response = requests.request(
    "POST",
    WP_url,
    data=payload,
    headers=headers,
    auth=auth
    )

    print(response)
    print(random_image_list)


post_creator("https://jsonplaceholder.typicode.com/posts/5", "<BASE_URL>", "la", "en", "publish")
```

Nous allons le décomposer en parties individuelles et voir, étape par étape, ce que nous devons faire. 

Avant cela, nous devons nous rendre sur le tableau de bord de notre site WordPress et créer un nouveau mot de passe d'application. Nous l'utiliserons pour construire notre authentification de base lors de la publication d'articles sur notre site. 

Si vous ne l'avez jamais fait auparavant, vous pouvez consulter la [documentation officielle](https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/) de WordPress sur la manière de procéder. Une fois que vous l'aurez créé, vous verrez quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/0-2.png)

N'oubliez pas de le sauvegarder, c'est la seule chance de l'obtenir !

## C'est l'heure de coder

Commençons par vérifier notre code à partir des bibliothèques dont nous avons besoin. Nous utiliserons la bibliothèque googletrans pour traduire notre contenu avec les API de Google Translate. Donc, depuis la ligne de commande, je me déplace dans mon répertoire de projet et je tape :

```python
pip install googletrans
```

Vous pourriez rencontrer cette erreur lorsque vous exécutez le script :

```cmd
AttributeError: 'NoneType' object has no attribute 'group'
```

Si vous voyez ce message d'erreur, vous devriez installer cette version :

```cmd
pip install googletrans==4.0.0-rc1

```

Je l'ai trouvé sur [cet](https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group) article StackOverflow. Si vous voulez en savoir plus, jetez un coup d'œil !

## Comment obtenir le contenu traduit

Une fois que nous avons installé googletrans, nous définissons une nouvelle fonction et l'appelons "post_creator" :

```python
def post_creator(sourceURL, wpBaseURL, sourceLang, targetLang, postStatus):
```

Nous passons à cette fonction cinq arguments :

* `sourceURL` : l'URL du site web d'où vous obtenez le contenu
* `wpBaseURL` : l'URL de votre nouveau site web où vous souhaitez importer le contenu traduit
* `sourceLang` : la langue originale du contenu
* `targetLang` : la langue dans laquelle vous souhaitez traduire votre contenu
* `postStatus` : le statut de votre article WordPress : par exemple "brouillon", "publié", etc.

À l'intérieur de la fonction, nous déclarons six variables. Voyons-les.

Nous utilisons la méthode GET pour appeler une API afin d'obtenir le contenu que nous voulons traduire :

```python
response_API = requests.get(sourceURL)
```

Ensuite, nous stockons dans la variable "data" le texte de la requête :

```python
data = response_API.text
```

Nous analysons le JSON avec la méthode ".loads()" pour le convertir en un dictionnaire Python :

```python
parse_json = json.loads(data)

```

Ensuite, nous stockons la valeur de la clé JSON "title" :

```python
get_article_title = parse_json['title']

```

Nous faisons de même avec la clé "body" :

```python
get_article_content = parse_json['body']

```

Enfin, nous stockons dans une variable une liste où nous avons les ID des médias que nous voulons utiliser comme "image à la une" :

```python
image_list = ["1689","1594","1612"]

```

Après avoir créé les variables ci-dessus, nous instancions Translator() :

```python
translator = Translator()
```

Maintenant, nous pouvons commencer à traduire le contenu. Nous traduisons le titre de l'article que nous avons obtenu de l'appel API précédent et le stockons dans la variable "title_translation". Nous obtenons ensuite son texte et le stockons dans la variable "title_translation_text" :

```python
title_translation = translator.translate(get_article_title, src=sourceLang, dest=targetLang)
title_translation_text = title_translation.text 
```

Nous faisons de même avec le contenu de l'article :

```python
content_translation = translator.translate(get_article_content, src=sourceLang, dest=targetLang)
content_translation_text = content_translation.text 
```

Nous obtenons une image aléatoire à partir de la liste des ID d'images que nous avons créée précédemment. Les images doivent déjà être disponibles dans notre instance WordPress. Ensuite, nous en choisissons une simplement en spécifiant son ID :

```python
random_image_list = random.choice(image_list)
```

## Comment créer notre article de blog WordPress

Maintenant, nous configurons les choses pour pousser le contenu que nous avons vers notre site WordPress. Tout d'abord, nous stockons l'URL que nous appelons pour pousser le contenu dans une variable :

```python
WP_url = wpBaseUrl + "/wp-json/wp/v2/posts"

```

Nous stockons dans une variable les identifiants pour notre authentification de base : le nom d'utilisateur et le mot de passe d'application que nous avons créés précédemment. Nous utilisons "HTTPBasicAuth" pour gérer notre authentification :

```python
auth = HTTPBasicAuth(<USERNAME>, <PASSWORD>)
```

Nous stockons dans une variable les en-têtes que nous voulons passer. Nous définissons le type de sortie en JSON et indiquons que le format du corps de la requête est JSON :

```python
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
```

Il est temps de définir la charge utile. Nous utilisons la fonction dumps() pour convertir l'objet Python que nous avons créé en une chaîne JSON, puis nous passons les données dont nous avons besoin pour créer l'article de blog :

```python
payload = json.dumps({ 
        "status":postStatus,
        "title": title_translation_text,
        "content": content_translation_text,
        "featured_media": random_image_list
    })
```

Ensuite, nous utilisons la méthode request() pour effectuer notre appel API :

```python
response = requests.request(
    "POST",
    WP_url,
    data=payload,
    headers=headers,
    auth=auth
    )
```

À la fin de la fonction, nous imprimons la réponse de l'appel POST et l'ID du média que nous utiliserons comme image à la une :

```python
print(response)
print(random_image_list)
```

Une fois que nous avons complété notre fonction, il est temps de l'appeler et de passer les arguments corrects :

```python
post_creator("https://jsonplaceholder.typicode.com/posts/5", <BASEURL>, "la", "en", "publish")
```

* `https://jsonplaceholder.typicode.com/posts/5` : l'URL que nous appelons pour obtenir le contenu que nous voulons traduire
* `<BASEURL>` : l'URL de base de notre site WordPress
* `la` : le code de langue du contenu que nous obtenons de notre appel API. Dans ce cas, il s'agit de contenu "Lorem Ipsum", nous le définissons donc en latin
* `en` : le code de langue dans lequel nous voulons traduire notre contenu. Nous le définissons en anglais.
* `publish` : le statut de l'article WordPress que nous créons

Si nous exécutons le script via la ligne de commande, nous voyons ce message :

```cmd
<Response [201]> 
1594
```

Et si vous visitez le site web, vous pouvez voir l'article :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/1-1.png)

Pour vous donner un aperçu complet, voici le JSON à partir duquel nous avons obtenu le contenu :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/2.png)

## Réflexions finales

Dans cet article, nous avons vu comment automatiser la publication d'articles en quelques lignes de code avec Python. Il peut être exécuté en tant que batch ou lorsque cela est nécessaire. 

Le contenu est toujours un point clé lorsque vous gérez un site web. J'espère que cet article vous aidera à traduire du contenu rapidement et à développer votre audience encore plus vite. [Ici](https://github.com/mventuri/python-wordpress-blog-post) vous pouvez trouver le dépôt sur GitHub. 

Amusez-vous bien et continuez à coder ! 😊