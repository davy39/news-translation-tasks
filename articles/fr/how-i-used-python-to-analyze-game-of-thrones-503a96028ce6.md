---
title: Comment j'ai utilisé Python pour analyser Game of Thrones
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-12T21:23:00.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-python-to-analyze-game-of-thrones-503a96028ce6
coverImage: https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/1_zWAQiGmSUNnBMl6D12xi7A.jpeg
tags:
- name: automation
  slug: automation
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment j'ai utilisé Python pour analyser Game of Thrones
seo_desc: 'By Rocky Kev

  I wanted to learn Python for a long time, but I could never find a reason. When
  my company had a bunch of daily reports that needed to be generated, I realized
  I had an opportunity to explore Python to cut out all the repetition.

  This ar...'
---

Par Rocky Kev

Je voulais apprendre Python depuis longtemps, mais je n'arrivais jamais à trouver une raison. Lorsque mon entreprise a eu une série de rapports quotidiens à générer, j'ai réalisé que j'avais une opportunité d'explorer Python pour éliminer toutes les répétitions.

Cet article est le résultat de quelques semaines d'apprentissage de Python, de manipulation des diverses bibliothèques et d'automatisation de certaines de mes tâches au travail.

Maintenant, je veux partager ce dont Python est capable.

Plutôt que de donner des exemples liés au bureau ennuyeux, mettons-les dans un cadre Game of Thrones !

![Image](https://cdn-media-1.freecodecamp.org/images/1*j3vovuLmWm3zhTClxI9vnw.gif align="left")

*Toute excuse pour parler de Game of Thrones*

Dans cet article, je vais mettre en œuvre l'automatisation web avec la bibliothèque [Selenium](https://selenium-python.readthedocs.io/), [le web scraping avec la bibliothèque BeautifulSoup](https://rockykev.com/python-and-game-of-thrones-part-2-of-3/), et [la génération de rapports avec le module csv](https://rockykev.com/python-and-game-of-thrones-part-3-of-3/) — ce qui simule en quelque sorte tout le côté Pandas/Data Science de Python.

Et comme je l'ai mentionné auparavant — tous les exemples utiliseront Game of Thrones.

### Quelques notes rapides :

1. Vous n'avez pas besoin d'expérience en Python pour faire cela. Je vais expliquer le code, et vous devriez avoir assez pour commencer.

2. Je ne suis pas un super-expert en Python. **Cela représente environ quelques semaines d'expérience en Python.** C'était juste assez pour automatiser mon travail et créer ces exemples.

3. Python est [BIEN DOCUMENTÉ](https://docs.python.org/3/). Il existe de nombreux guides gratuits pour apprendre Python, comme [Automate the Boring Stuff](https://automatetheboringstuff.com/), [Python for Beginners](https://www.pythonforbeginners.com/), et la formidable piste [Dataquest.io data science](https://www.dataquest.io/). Il y a encore plus de liens dans la [base de connaissances freeCodeCamp](https://guide.freecodecamp.org/python/).

### Python, le meilleur langage de programmation basé sur les reptiles

![Image](https://cdn-media-1.freecodecamp.org/images/1*zWAQiGmSUNnBMl6D12xi7A.jpeg align="left")

*Python n'est pas du tout aussi intimidant. Honnête.*

**Pour ceux qui ne sont pas familiers avec la programmation —**

> *Python est un langage de programmation polyvalent qui est strictement typé, interprété et connu pour sa facilité de lecture avec de grands principes de conception.*
>
> — *Via le* [guide freecodecamp.com](https://guide.freecodecamp.org/python/)

Selon l'[enquête des développeurs 2018 de Stack Overflow](https://insights.stackoverflow.com/survey/2018), Python est le langage que la plupart des développeurs veulent apprendre (et aussi l'un des langages de programmation majeurs à la croissance la plus rapide).

Python alimente des sites comme Reddit, Instagram et Dropbox. C'est aussi un langage très lisible qui possède de nombreuses bibliothèques puissantes.

Python est nommé d'après Monty Python, pas le reptile. MAIS — malgré cela, c'est toujours le langage de programmation basé sur les reptiles le plus populaire, battant Serpent, Gecko, Cobra et Raptor ! (J'ai dû rechercher cette blague !)

**Si vous avez quelques connaissances en programmation (par exemple en JavaScript) —**

Quelques choses sur Python :

* Python utilise l'indentation au lieu des accolades. Voir l'exemple ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/0*T-_gCGIc-fu08OtW align="left")

*Via les* [diapositives JavaScript 101, du Professeur Mindy McAdams](https://www.slideshare.net/macloo/javascript-101-16754994)

* Python utilise l'héritage basé sur les classes — il est donc plus proche des langages C, tandis que JavaScript peut simuler des classes.

* Python est également fortement typé. Pas de mélange. Par exemple, si vous ajoutez une chaîne de caractères et un entier ensemble, il commencera à se plaindre.

### Commençons tout de suite !

Je vais diviser cela en 3 parties.

* **Game of Thrones et Python #1** : Automatisation web

* **Game of Thrones et Python #2** : Web Scraping

* **Game of Thrones et Python #3** : Génération de rapports avec le module CSV

![Image](https://cdn-media-1.freecodecamp.org/images/0*Pgy4fHbVh3FeXVEC.jpg align="left")

### Game of Thrones et Python #1 — Automatisation web

L'une des choses les plus cool que vous pouvez faire avec Python est l'automatisation web.

Par exemple — vous pouvez écrire un script Python qui :

1. Ouvre un navigateur

2. Visite automatiquement un site web spécifique

3. Vous connecte à ce site

4. Va à une autre partie de ce site web

5. Trouve le dernier article de blog.

6. Ouvre cet article de blog.

7. Soumet un commentaire qui dit : « Super écriture ! High five ! »

8. Et enfin vous déconnecte de ce site web

Cela ne semble peut-être pas si difficile à faire. Cela prend quoi... 20 secondes ?

Mais si vous deviez faire cela encore et encore, cela vous rendrait fou.

Par exemple — que se passe-t-il si vous aviez un site de staging qui est encore en développement avec 100 articles de blog, et que vous vouliez poster un commentaire sur chaque page pour tester sa fonctionnalité ?

Cela fait 100 articles de blog * 20 secondes = **environ 33 minutes**

Et s'il y a MULTIPLES phases de test, et que vous deviez répéter le test six fois de plus ?

**D'autres cas d'utilisation pour l'automatisation web incluent :**

* Vous pourriez vouloir automatiser la création de comptes sur votre site.

* Vous pourriez vouloir exécuter un bot du début à la fin dans votre cours en ligne.

* Vous pourriez vouloir pousser 100 bots à soumettre un formulaire sur votre site avec un seul script.

### Ce que nous allons faire

Pour cette partie, nous allons automatiser le processus de connexion à tous nos sites de fans préférés de Game of Thrones.

Ne détestez-vous pas quand vous devez perdre du temps à vous connecter à westeros.org, au subreddit /r/freefolk, winteriscoming.net et tous vos autres sites de fans ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*tHf45KF34EH3vFqNJz0OCg.gif align="left")

*Littéralement... LE PIRE.*

Avec ce modèle, vous pouvez vous connecter automatiquement à divers sites web !

Maintenant, pour Game of Thrones !

### Le Code

Vous devrez installer Python 3, Selenium et les webdrivers Firefox pour commencer. *Si vous voulez suivre, consultez mon tutoriel sur* [Comment automatiser les soumissions de formulaires avec Python](https://rockykev.com/how-to-automate-form-submissions-logins/)*.*

Celui-ci pourrait devenir compliqué. Je vous recommande donc de vous asseoir et de profiter du voyage.

```python
## Script de connexion facile à Game of Thrones
##
## Description : Ce code se connecte automatiquement à tous vos sites de fans

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


driver = webdriver.Firefox()
driver.implicitly_wait(5)
    ## implicitly_wait fait attendre le bot 5 secondes avant chaque action
    ## pour que le contenu du site puisse se charger

# Définir les fonctions

def login_to_westeros (username, userpass):

    ## Ouvrir la page de connexion
    driver.get('https://asoiaf.westeros.org/index.php?/login/')    

    ## Journaliser les détails
    print(username + " se connecte à westeros.")
    
    ## Trouver les champs et se connecter au compte.
    textfield_username = driver.find_element_by_id('auth')
    textfield_username.clear()
    textfield_username.send_keys(username)

    textfield_email = driver.find_element_by_id('password')
    textfield_email.clear()
    textfield_email.send_keys(userpass)

    submit_button = driver.find_element_by_id('elSignIn_submit')
    submit_button.click()

    ## Journaliser les détails
    print(username + " est connecté ! -> westeros")



		
def login_to_reddit_freefolk (username, userpass):

    ## Ouvrir la page de connexion
    driver.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2Fr%2Ffreefolk')    

    ## Journaliser les détails
    print(username + " se connecte à /r/freefolk.")
    
    ## Trouver les champs et se connecter au compte.
    textfield_username = driver.find_element_by_id('loginUsername')
    textfield_username.clear()
    textfield_username.send_keys(username) 
    textfield_email = driver.find_element_by_id('loginPassword')
    textfield_email.clear()
    textfield_email.send_keys(userpass)

    submit_button = driver.find_element_by_class_name('AnimatedForm__submitButton')
    submit_button.click()

    ## Journaliser les détails
    print(username + " est connecté ! -> /r/freefolk.")
    

## Définir la combinaison utilisateur et mot de passe.

login_to_westeros("gameofthronesfan86", PASSWORDHERE)

time.sleep(2)
driver.execute_script("window.open('');")
Window_List = driver.window_handles
driver.switch_to_window(Window_List[-1])

login_to_reddit_freefolk("MyManMance", PASSWORDHERE)

time.sleep(2)
driver.execute_script("window.open('');")
Window_List = driver.window_handles
driver.switch_to_window(Window_List[-1])


## attendre 2 secondes
time.sleep(2)


print("tâche terminée")
```

#### Décomposer le code

Pour commencer, j'importe la bibliothèque *Selenium* pour aider à faire le gros du travail.

J'ai également importé la bibliothèque *time*, donc après chaque action, elle attendra x secondes. Ajouter une attente permet à la page de se charger.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time 
```

#### Qu'est-ce que Selenium ?

Selenium est la bibliothèque Python que nous utilisons pour l'automatisation web. Selenium a développé une API afin que des auteurs tiers puissent développer des webdrivers pour la communication avec les navigateurs. Ainsi, l'équipe Selenium peut se concentrer sur leur base de code, tandis qu'une autre équipe peut se concentrer sur le middleware.

Par exemple :

* L'équipe Chromium a créé son propre webdriver pour Selenium appelé [chromedriver](http://chromedriver.chromium.org/).

* L'équipe Firefox a créé son propre webdriver pour Selenium appelé [geckodriver](https://github.com/mozilla/geckodriver).

* L'équipe Opera a créé son propre webdriver pour Selenium appelé [operadriver](https://github.com/operasoftware/operachromiumdriver).

```python
driver = webdriver.Firefox()
driver.get('https://www.hbo.com/game-of-thrones')
driver.close()
```

Dans le code ci-dessus, je demande à Selenium de faire des choses comme « **Configurer Firefox comme navigateur de choix** », et « **passer ce lien à Firefox** », et enfin « **Fermer Firefox** ». J'ai utilisé le geckodriver pour faire cela.

#### Connexion aux sites

Pour faciliter la lecture, j'ai écrit une fonction séparée pour se connecter à chaque site, afin de montrer le modèle que nous créons.

```python
def login_to_westeros (username, userpass):

    ## Se connecter
    driver.get('https://asoiaf.westeros.org/index.php?/login/')    

    ## Journaliser les détails
    print(username + " se connecte à westeros.")
    
    ## 2) Chercher la boîte de connexion sur la page
    textfield_username = driver.find_element_by_id('auth')
    textfield_username.clear()
    textfield_username.send_keys(username)
    textfield_email = driver.find_element_by_id('password')
    textfield_email.clear()
    textfield_email.send_keys(userpass)

    submit_button = driver.find_element_by_id('elSignIn_submit')
    submit_button.click()

    ## Journaliser les détails
    print(username + " est connecté ! -> westeros")
```

Si nous décomposons cela encore plus — chaque fonction a les éléments suivants.

Je dis à Python de :

1. Visiter une page spécifique.  
    `driver.get('https://asoiaf.westeros.org/index.php?/login/')`
    
2. Chercher la boîte de connexion

* Effacer le texte s'il y en a

* Soumettre ma variable

```python
    textfield_username = driver.find_element_by_id('auth')
    textfield_username.clear()
    textfield_username.send_keys(username)
```

3. Chercher la boîte de mot de passe

* Effacer le texte s'il y en a

* Soumettre ma variable

```python
    textfield_email = driver.find_element_by_id('password')
    textfield_email.clear()
    textfield_email.send_keys(userpass)
```

4. Chercher le bouton de soumission, et cliquer dessus

```python
    submit_button = driver.find_element_by_id('elSignIn_submit')
    submit_button.click() 
```

À noter : chaque site web a des façons différentes de trouver les champs de nom d'utilisateur/mot de passe et les boutons de soumission. Vous devrez faire un peu de recherche pour cela.

#### Comment trouver la boîte de connexion et la boîte de mot de passe pour n'importe quel site web

La bibliothèque Selenium a plusieurs façons pratiques de trouver des éléments sur une page web. Voici quelques-unes de celles que j'aime utiliser.

* find\_element\_by\_id

* find\_element\_by\_name

* find\_element\_by\_xpath

* find\_element\_by\_class\_name

Pour la liste complète, visitez la [documentation Python de Selenium pour localiser les éléments](https://selenium-python.readthedocs.io/locating-elements.html).

Pour utiliser [asoiaf.westeros.com comme exemple](https://asoiaf.westeros.org/index.php?/login/), lorsque j'inspecte les éléments — ils ont tous des ID... ce qui est GÉNIAL ! Cela me facilite la vie.

![Image](https://cdn-media-1.freecodecamp.org/images/0*MwnwHFAGMUw3EPpi.jpg align="left")

*Inspecter l'élément et chercher le code. Cela vous donnera des indices sur le ciblage.*

### Exécuter le code

Voici une courte vidéo de moi en train d'exécuter le code :

[https://www.loom.com/share/87f0785c9c354c7282f7340c022c3291?sid=e55237cd-a693-4834-93bc-e14cb04ef147](https://www.loom.com/share/87f0785c9c354c7282f7340c022c3291?sid=e55237cd-a693-4834-93bc-e14cb04ef147)

#### Profiter du voyage

Avec l'automatisation web, vous jouez à un jeu de « comment puis-je faire pour que Selenium trouve l'élément ». Une fois que vous l'avez trouvé, vous pouvez alors le manipuler.

### Game of Thrones et Python #2 — Web Scraping

Dans cette partie, nous allons explorer le web scraping.

Le processus global est :

1. Nous allons faire visiter une page web à Python.

2. Nous allons ensuite analyser cette page web avec BeautifulSoup.

3. Vous configurez ensuite le code pour récupérer des données spécifiques.

**Par exemple :** Vous pourriez vouloir récupérer toutes les balises h1. Ou tous les liens. Ou dans notre cas, toutes les images d'une page.

**D'autres cas d'utilisation pour le Web Scraping :**

* Vous pouvez récupérer tous les liens d'une page web.

* Vous pouvez récupérer tous les titres de publications dans un forum

* Vous pouvez l'utiliser pour récupérer la valeur quotidienne du NASDAQ sans jamais visiter le site.

* Vous pouvez l'utiliser pour télécharger tous les liens d'un site web qui n'a pas de fonction « Télécharger tout ».

En bref, le web scraping vous permet de récupérer automatiquement du contenu web via Python.

**Globalement, un processus très simple. Sauf quand ce n'est pas le cas !**

### **Le défi du Web Scraping pour les images**

Mon objectif était de transformer mes connaissances en web scraping de contenu pour récupérer des images.

Alors que le web scraping pour les liens, le texte du corps et les en-têtes est **très simple**, le web scraping pour les images est significativement plus complexe. Laissez-moi expliquer.

En tant que développeur web, héberger MULTIPLES images en taille réelle sur une seule page web ralentira toute la page. Au lieu de cela, utilisez des miniatures et ne chargez l'image en taille réelle que lorsque la miniature est cliquée.

Par exemple : Imaginez si nous avions vingt images d'un mégaoctet sur notre page web. À l'arrivée, un visiteur devrait télécharger 20 mégaoctets d'images ! La méthode la plus courante consiste à créer vingt images miniatures de 10 ko. Maintenant, votre charge utile est seulement de 200 ko, soit environ 1/100 de la taille !

Alors, quel est le rapport avec le web scraping d'images et ce tutoriel ?

Cela signifie qu'il est assez difficile d'écrire un **bloc de code générique** qui fonctionne toujours pour chaque site web. Les sites web mettent en œuvre différentes façons de transformer une miniature en une image en taille réelle, ce qui rend difficile la création d'un modèle « taille unique ».

Je vais quand même enseigner ce que j'ai appris. Vous allez quand même acquérir beaucoup de compétences. Soyez simplement conscient que l'essai de ce code sur d'autres sites **nécessitera des modifications majeures**. Hourra pour la Zone de Développement Proximal.

### Python et Game of Thrones

Le but de ce tutoriel est que nous allons rassembler des images de nos acteurs préférés ! Ce qui nous permettra de faire des choses étranges comme créer un collage d'acteurs de crush d'adolescence que nous pouvons accrocher dans notre chambre (comme ceci).

![Image](https://cdn-media-1.freecodecamp.org/images/0*YfyqObexD1PryQCC.png align="left")

*Je faisais ce collage lorsque ma partenaire est entrée. Elle est ensuite sortie promptement.*

Pour rassembler ces images, nous allons utiliser Python pour faire du web scraping. Nous allons utiliser la bibliothèque [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) pour visiter une page web et récupérer toutes les balises d'image.

*NOTE : Dans de nombreux termes et conditions des sites web, ils interdisent tout web scraping de leurs données. Certains développent des API pour vous permettre d'accéder à leurs données. D'autres non. De plus, essayez d'être conscient que vous utilisez leurs ressources. Donc cherchez à faire une requête à la fois plutôt que d'ouvrir beaucoup de connexions en parallèle et de faire planter leur site.*

### Le Code

```python
# Importer les bibliothèques nécessaires
import requests
import time
from bs4 import BeautifulSoup

# L'URL à scraper
url = 'https://www.popsugar.com/celebrity/Kit-Harington-Rose-Leslie-Cutest-Pictures-42389549?stream_view=1#photo-42389576'
#url = 'https://www.bing.com/images/search?q=jon+snow&FORM=HDRSC2'

# Connexion
response = requests.get(url)

# Récupérer le HTML et utiliser Beautiful
soup = BeautifulSoup (response.text, 'html.parser')

#Un code de boucle pour parcourir chaque lien, et le télécharger
for i in range(len(soup.findAll('img'))):

    tag = soup.findAll('img')[i]
    link = tag['src']

    #sauter si cela ne commence pas par http
    if "http" in full_link: 
        print("url récupéré : " + link)

        filename = str(i) + '.jpg'
        print("Téléchargement : " + filename)

        r = requests.get(link)
        open(filename, 'wb').write(r.content)

    else:
        print("url récupéré : " + link)
        print("sauter")

    
    time.sleep(1)Décomposer le code
```

#### Faire visiter la page web par Python

Nous commençons par importer les bibliothèques nécessaires, puis stockons le lien de la page web dans une variable.

* La bibliothèque [Requests](https://realpython.com/python-requests/) est utilisée pour effectuer toutes sortes de requêtes HTTP

* La bibliothèque [Time](https://docs.python.org/3/library/time.html) est utilisée pour mettre une attente de 1 seconde après chaque requête. Si nous ne l'avions pas incluse, toute la boucle se déclencherait aussi vite que possible, ce qui n'est pas très amical pour les sites que nous scrapons.

* La bibliothèque [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) est utilisée pour faciliter l'exploration de l'arbre DOM.

#### Analyser cette page web avec BeautifulSoup

Ensuite, nous poussons notre URL dans BeautifulSoup.

#### Trouver le contenu

Enfin, nous utilisons une boucle pour récupérer le contenu.

Cela commence par une boucle FOR. BeautifulSoup fait un filtrage intéressant, où mon code demande à BeautifulSoup de trouver toutes les balises 'img', et de les stocker dans un tableau temporaire. Ensuite, la fonction **len** demande la longueur du tableau.

```bash
#Un code de boucle pour parcourir chaque lien, et le télécharger
for i in range(len(soup.findAll('img'))):
```

Donc en termes humains, si le tableau contenait 51 éléments, le code ressemblerait à

`For i in range(50):`

Ensuite, nous retournerons à notre objet soup, et ferons le vrai filtrage.

```python
tag = soup.findAll('img')[i]
   link = tag['src']
```

Rappelez-vous que nous sommes dans une boucle For, donc \[i\] représente un nombre.

Nous disons donc à BeautifulSoup de trouver toutes les balises 'img', de les stocker dans un tableau temporaire, et de référencer un numéro d'index spécifique basé sur l'endroit où nous en sommes dans la boucle.

Au lieu d'appeler un tableau directement comme allOfTheImages\[10\], nous utilisons soup.findAll('img')\[10\], puis nous le passons à la variable **tag**.

Les données dans la variable **tag** ressembleront à quelque chose comme :

```xml
<img src="smiley.gif" alt="Smiley face" height="42" width="42">
```

C'est pourquoi l'étape suivante consiste à extraire le 'src'.

![Image](https://cdn-media-1.freecodecamp.org/images/0*tC7zm_JNPdbtPZI3.jpg align="left")

### Télécharger le contenu

Enfin — c'est la partie amusante !

Nous allons à la partie finale de la boucle, avec le téléchargement du contenu.

Il y a quelques éléments de conception étranges ici que je veux souligner.

1. L'instruction IF est en fait un hack que j'ai fait pour d'autres sites que je testais. Il y avait des moments où je récupérais des images qui faisaient partie du site racine (comme la favicon ou les icônes des médias sociaux) que je ne voulais pas. Donc utiliser l'instruction IF m'a permis de l'ignorer.

2. J'ai également forcé toutes les images à être en .jpg. J'aurais pu écrire un autre morceau d'instructions IF pour vérifier le type de données, puis ajouter le type de fichier correct. Mais cela ajoutait un morceau de code significatif qui rendait ce tutoriel plus long.

3. J'ai également ajouté toutes les commandes print. Si vous vouliez récupérer tous les liens d'une page web, ou un contenu spécifique — vous pouvez vous arrêter ici ! Vous l'avez fait !

Je veux également souligner le code **requests.get(link)** et **open(filename, 'wb').write(r.content)**.

```python
r = requests.get(link)
open(filename, 'wb').write(r.content) 
```

Comment cela fonctionne :

1. [Requests](https://realpython.com/python-requests/) obtient le lien.

2. [Open](https://docs.python.org/3/library/functions.html#open) est une fonction Python par défaut qui ouvre ou crée un fichier, lui donne un accès en mode écriture et binaire (puisque les images ne sont que des 1 et des 0), et écrit le contenu du lien dans ce fichier.

```python
#sauter si cela ne commence pas par http
    if "http" in full_link: 
        print("url récupéré : " + link)

        filename = str(i) + '.jpg'
        print("Téléchargement : " + filename)

        r = requests.get(link)
        open(filename, 'wb').write(r.content)

    else:
        print("url récupéré : " + link)
        print("sauter")

    
    time.sleep(1)
```

Le Web Scraping a beaucoup de fonctionnalités utiles.

Ce code ne fonctionnera pas directement pour la plupart des sites avec des images, mais il peut servir de base pour savoir comment récupérer des images sur différents sites.

### Game of Thrones et Python #3 — Génération de rapports et de données

Rassembler des données est facile. Interpréter les données est difficile. C'est pourquoi il y a une énorme demande de data scientists qui peuvent donner un sens à ces données. Et les data scientists utilisent des langages comme R et Python pour les interpréter.

Dans ce tutoriel, nous allons utiliser le module csv, ce qui sera suffisant pour générer un rapport. Si nous travaillions avec un énorme ensemble de données, un ensemble de 50 000 lignes ou plus, nous devrions utiliser la bibliothèque Pandas.

Ce que nous allons faire est de télécharger un CSV, de faire interpréter les données par Python, d'envoyer une requête basée sur le type de question à laquelle nous voulons répondre, puis de faire imprimer la réponse.

### Python VS les fonctions de base des feuilles de calcul

Vous pourriez vous demander :

*« Pourquoi devrais-je utiliser Python alors que je peux facilement utiliser des fonctions de feuille de calcul comme =SUM ou =COUNT, ou filtrer les lignes dont je n'ai pas besoin manuellement ? »*

Comme pour tous les autres trucs d'automatisation des parties 1 et 2, vous pouvez définitivement faire cela manuellement.

Mais imaginez si vous deviez générer un nouveau rapport **chaque jour.**

Par exemple : Je construis des cours en ligne. Et nous voulons un rapport quotidien de la progression de chaque étudiant. Combien d'étudiants ont commencé aujourd'hui ? Combien d'étudiants sont actifs cette semaine ? Combien d'étudiants ont atteint le Module 2 ? Combien d'étudiants ont soumis leurs devoirs du Module 3 ? Combien d'étudiants ont cliqué sur le bouton de complétion sur les appareils mobiles ?

Je peux soit passer 15 minutes à trier les données pour générer un rapport pour mon équipe. OU écrire un code Python qui le fait quotidiennement.

**D'autres cas d'utilisation pour utiliser du code au lieu des fonctions de feuille de calcul par défaut :**

* Vous pourriez travailler avec un énorme ensemble de données (énorme comme 50 000 lignes et 20 colonnes)

* Vous avez besoin de plusieurs tranches de filtres et de segmentation pour obtenir vos réponses.

* Vous devez exécuter la même requête sur un ensemble de données qui change répétitivement

### Génération de rapports avec Game of Thrones

Chaque année, [Winteriscoming.net,](https://winteriscoming.net/) un site d'actualités sur Game of Thrones, organise son March Madness annuel. Les visiteurs votent pour leurs personnages préférés, et les gagnants montent dans le tableau et concourent contre une autre personne. Après 6 tours de votes, un gagnant est déclaré.

![Image](https://cdn-media-1.freecodecamp.org/images/0*xdxZpQOA9e7YqFhH.jpg align="left")

*C'est le Thrones Madness de 2018*

Puisque les votes de 2019 sont encore en cours, j'ai récupéré les 6 tours de données de 2018 et les ai compilés dans un fichier CSV. Pour voir à quoi ressemblait le sondage sur winteriscoming.net, [cliquez ici](https://winteriscoming.net/2018/03/11/game-of-thrones-march-madness-round-1-vote-for-your-favorite-character/).

![Image](https://cdn-media-1.freecodecamp.org/images/0*-25cwQQD-GvYJiBD.png align="left")

*Vous pouvez voir tout le CSV en tant que* [fichier Google Sheets](https://docs.google.com/spreadsheets/d/12XU-Ce5uF_wlWmFrzHLPm524Wl6y6wZefI8fBBEgsV8/edit?usp=sharing)

J'ai également ajouté quelques données de fond supplémentaires (comme leur origine), pour rendre le rapport un peu plus intéressant.

### Poser des questions

Pour générer un rapport, nous devons poser quelques questions.

**Par définition :** Le devoir principal d'un rapport est de RÉPONDRE aux questions.

Alors, inventons-les maintenant.

Sur la base de cet ensemble de données... voici quelques questions.

1. Qui a remporté le vote de popularité ?

2. Qui a gagné en fonction des moyennes ?

3. Qui est la personne non originaire de Westeros la plus populaire ? (personnages non nés à Westeros)

### Avant de répondre aux questions — configurons notre code Python

Pour faciliter les choses, j'ai écrit tout le code, y compris les révisions — dans mon nouvel IDE en ligne préféré, Repl.it.

```python
import csv

# Importer les données
f_csv = open('winter-is-coming-2018.csv')
headers = next(f_csv) 
f_reader = csv.reader(f_csv)
file_data = list(f_reader)

# Transformer toutes les cellules vides en zéros
# https://stackoverflow.com/questions/2862709/replacing-empty-csv-column-values-with-a-zero
for row in file_data:
  for i, x in enumerate(row):
    if len(x)< 1:
      x = row[i] = 0
```

Voici mon processus avec le code.

1. J'ai importé le module csv.

2. J'ai importé le fichier csv, et l'ai transformé en un type de liste appelé **file\_data**.

* La façon dont Python lit votre fichier est en passant d'abord les données à un objet.

* J'ai supprimé l'en-tête, car il fausserait les données.

* J'ai ensuite passé l'objet à un lecteur, et enfin à une liste.

* *Note : Je viens de réaliser que je l'ai fait de la manière Python 2. Il y a une* [manière plus propre de le faire en Python 3](https://docs.python.org/3.7/library/csv.html)*. Oh bien. Cela fonctionne toujours.*

3. Pour additionner les totaux, j'ai fait en sorte que toutes les cellules vides deviennent 0.

* C'était l'un de ces moments où j'ai trouvé une solution [Stack Overflow](https://stackoverflow.com/questions/2862709/replacing-empty-csv-column-values-with-a-zero) qui était meilleure que ma version originale.

Avec cette configuration, nous pouvons maintenant parcourir la liste de données et répondre aux questions !

#### Question #1 — Qui a remporté le vote de popularité ?

**La méthode de la feuille de calcul :**

La manière la plus simple serait d'additionner chaque cellule, en utilisant une formule.  
En utilisant la ligne 2 comme exemple, dans une colonne vide, vous pouvez écrire la formule :

```python
=sum(E2:J2)
```

Vous pouvez ensuite faire glisser cette formule pour les autres lignes.

Ensuite, triez-la par total. Et vous avez un gagnant !

![Image](https://cdn-media-1.freecodecamp.org/images/0*leXUT8cq12ZEkfNJ.png align="left")

*C'est Jon Snow — avec 12959 points*

```python
## Inclure le code ci-dessus

# Pousser les données vers un dictionnaire
total_score = {}

# Passer chaque personnage et leur score final dans le dictionnaire total_score
for row in file_data:
  total = (int(row[4]) + 
          int(row[5]) + 
          int(row[6]) + 
          int(row[7]) + 
          int(row[8]) + 
          int(row[9]) )

  total_score[row[0]] = total

# Les dictionnaires ne sont pas triables par défaut, nous devrons emprunter à ces deux classes.
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
from operator import itemgetter
from collections import OrderedDict

sorted_score = OrderedDict(sorted(total_score.items(), key=itemgetter(1) ,reverse=True))

# Nous obtenons le nom du gagnant et leur score
winner = list(sorted_score)[0] #jon snow
winner_score = sorted_score[winner] #score

print(winner + " avec " + str(winner_score))

## RÉSULTAT => Jon Snow avec 12959
```

Les étapes que j'ai suivies sont :

1. L'ensemble de données est juste une grande liste. En utilisant une boucle for, vous pouvez ensuite accéder à chaque ligne.

2. Dans cette boucle for, j'ai additionné chaque cellule. (en émulant toute la formule « =sum(E:J) »)

3. Comme les dictionnaires ne sont pas exactement triables, j'ai dû importer deux classes pour m'aider à trier le dictionnaire par leurs valeurs, du plus haut au plus bas.

4. Enfin, j'ai passé le gagnant, et la valeur du gagnant en texte.

Pour aider à comprendre cette boucle, j'ai dessiné un diagramme.

![Image](https://cdn-media-1.freecodecamp.org/images/0*MfxMvgAbxnBtpaz7.png align="left")

Globalement, ce processus est un peu plus long par rapport à la méthode de la feuille de calcul. Mais attendez, cela devient plus facile !

![Image](https://cdn-media-1.freecodecamp.org/images/1*skwU3z1U-lMLexX4vkbgwQ.gif align="left")

*Félicitations Jon, tu es le personnage le plus populaire de GOT !*

#### Question 2 — Qui a gagné en fonction des moyennes ?

Vous avez peut-être remarqué que ceux qui ont progressé plus loin dans les classements obtiendraient évidemment plus de votes.

Par exemple : Si *Jon Snow* a obtenu 500 points au premier tour et 1000 points au deuxième tour, il bat déjà *The Mountain* qui n'avait que 1000 points et n'a jamais dépassé son tableau.

La prochaine meilleure chose est donc de faire la somme du total, puis de le diviser en fonction du nombre de tours auxquels ils ont participé.

**La méthode de la feuille de calcul :**

C'est facile. Dans la colonne B se trouve le nombre de tours auxquels ils ont participé. Vous diviseriez les tours par la somme, et presto !

```python
## ANCIEN CODE DE LA QUESTION 1
# Passer chaque personnage et leur score final dans le dictionnaire total_score
for row in file_data:
  total = (int(row[4]) + 
          int(row[5]) + 
          int(row[6]) + 
          int(row[7]) + 
          int(row[8]) + 
          int(row[9]) )

  total_score[row[0]] = total

## NOUVEAU CODE
# Passer chaque personnage et leur score final dans le dictionnaire total_score
for row in file_data:
  total = (int(row[4]) + 
          int(row[5]) + 
          int(row[6]) + 
          int(row[7]) + 
          int(row[8]) + 
          int(row[9]) )

  # NOUVELLE LIGNE - diviser par le nombre de tours
  new_total = total / int(row[2])

  total_score[row[0]] = new_total

# RÉSULTAT => Davos Seaworth avec 2247.6666666666665
```

Avez-vous remarqué le changement ? J'ai juste ajouté une ligne supplémentaire.

C'est tout ce qu'il a fallu pour répondre à cette question ! SUIVANT !

![Image](https://cdn-media-1.freecodecamp.org/images/0*RcjIMkQPF-rmaILe align="left")

*En moyenne, Davos Seaworth a le plus de points.*

#### Question 3 — Qui est la personne non originaire de Westeros la plus populaire ?

Avec les deux premiers exemples, il est assez facile de calculer le total avec les fonctions de feuille de calcul par défaut. Pour cette question, les choses sont un peu plus compliquées.

**La méthode de la feuille de calcul :**

1. En supposant que vous avez déjà la somme

2. Vous devez maintenant la filtrer en fonction de leur origine à Westeros/Autre

3. Ensuite, trier par la somme

![Image](https://cdn-media-1.freecodecamp.org/images/0*azDaokcyjcXYcuwX.png align="left")

```python
## ANCIEN CODE DE LA QUESTION 1
# Passer chaque personnage et leur score final dans le dictionnaire total_score
for row in file_data:
  total = (int(row[4]) + 
          int(row[5]) + 
          int(row[6]) + 
          int(row[7]) + 
          int(row[8]) + 
          int(row[9]) )

  # NOUVELLE LIGNE - diviser par le nombre de tours
  new_total = total / int(row[2])

  total_score[row[0]] = new_total

## NOUVEAU CODE
# Passer chaque personnage et leur score final dans le dictionnaire total_score
for row in file_data:

  # Ajouter une instruction IF-THEN
  if (row[3] == 'other'):
    total = (int(row[4]) + 
            int(row[5]) + 
            int(row[6]) + 
            int(row[7]) + 
            int(row[8]) + 
            int(row[9]) )
  else:
    total = 0

  total_score[row[0]] = total

# RÉSULTAT => Missandei avec 4811
```

Dans la Question 2, j'ai ajouté une ligne de code pour répondre à cette nouvelle question.

Dans la Question 3, j'ai ajouté une instruction IF-ELSE. Si ils ne sont pas de Westeros, alors comptez leur score. Sinon, donnez-leur un score de 0.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vswWUGsv9PsGe0eg.jpg align="left")

*Wow, énorme surprise ! J'espérais que c'était Grey Worm !*

### **Revue de ceci :**

Bien que la méthode de la feuille de calcul ne semble pas impliquer beaucoup d'étapes, elle nécessite certainement beaucoup plus de clics. La méthode Python a pris beaucoup plus de temps à configurer, mais chaque requête supplémentaire impliquait de changer quelques lignes de code.

Imaginez si le responsable demandait une douzaine de questions supplémentaires.

Par exemple :

1. Combien de points les personnages dont les noms commencent par L ont-ils obtenus ?

2. Ou combien de points tout le monde dans le tour 3 a-t-il obtenus qui vivaient à Westeros ?

3. Ou s'il y avait 640 personnages de GoT au lieu de seulement 64 ?

Mais imaginez aussi ceci — vous recevez un ensemble de données d'environ 50 mégaoctets (Notre fichier csv Game of Thrones faisait à peine 50 kilooctets — environ 1/1000 de la taille). Un fichier de 50 Mo de cette taille prendrait probablement quelques minutes à Excel pour le charger. De plus, il n'est pas inhabituel pour les Data Scientists d'utiliser des ensembles de données qui sont dans la gamme des 10 gigaoctets !

Globalement, à mesure que l'ensemble de données s'agrandit, il faudra de plus en plus de temps pour le traiter. Et c'est là que la puissance de Python entre en jeu.

### Conclusion

Dans la Partie 1, j'ai couvert l'automatisation web avec la bibliothèque Selenium. Dans la Partie 2, j'ai couvert le web scraping avec la bibliothèque BeautifulSoup. Et dans la Partie 3, j'ai couvert la génération de rapports avec le module csv.

Bien que je les aie couverts en morceaux — il y a aussi une synergie entre eux. Imaginez si vous aviez un projet où vous deviez découvrir qui meurt ensuite dans Game of Thrones en fonction des commentaires des acteurs de l'émission. Vous pourriez commencer par scraper tous les noms des acteurs sur IMDB. Vous pourriez utiliser Selenium pour vous connecter automatiquement à diverses plateformes de médias sociaux et rechercher leur nom de média social. Vous pourriez ensuite compiler toutes les données et les interpréter sous forme de csv ou, si elles sont vraiment énormes, en utilisant la bibliothèque Pandas.

Nous n'avons même pas abordé le Machine Learning, l'IA, le développement web, ou les dizaines d'autres choses pour lesquelles les gens utilisent Python.

Que cela soit une pierre d'achoppement dans votre voyage Python !

---

👏 Un énorme merci à mJordan pour avoir relu mon travail lors de la rencontre Puppies and Portfolios. Elle est l'une des développeuses CSS les plus talentueuses que j'ai jamais rencontrées.

💰 Si vous aimez parler de la construction de cours, de l'éducation en ligne et de l'avenir de l'éducation — contactez-moi sur mon Linkedin ou Twitter.

👏 J'apprécierais un clap (ou 50 !) Cela me met vraiment un sourire sur le visage.