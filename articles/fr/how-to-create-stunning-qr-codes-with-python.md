---
title: Comment créer des QR codes époustouflants avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-21T15:40:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-stunning-qr-codes-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/How-to-create-stunning-QR-codes-with-python-1.png
tags:
- name: Python
  slug: python
- name: qr code
  slug: qr-code
seo_title: Comment créer des QR codes époustouflants avec Python
seo_desc: "By Shittu Olumide\nA quick response (QR) code is a barcode that a digital\
  \ device can easily scan. It encodes data as a series of pixels in a square grid.\
  \ \nTracking information about supply chains using QR codes is very useful in marketing\
  \ and advertis..."
---

Par Shittu Olumide

Un code QR (Quick Response) est un code-barres qu'un appareil numérique peut facilement scanner. Il encode les données sous forme de série de pixels dans une grille carrée.

Le suivi d'informations sur les chaînes d'approvisionnement à l'aide de codes QR est très utile dans les campagnes de marketing et de publicité.

L'Organisation internationale de normalisation a certifié les codes QR comme norme mondiale en 2000. Ils représentent une amélioration par rapport aux codes-barres uni-dimensionnels précédents (ISO).

Les codes QR ont été développés dans les années 1990 pour fournir plus d'informations qu'un code-barres classique. Ils ont été créés par Denso Wave, une filiale de Toyota, pour surveiller la production de véhicules.

Contrairement aux codes-barres, qui nécessitent un faisceau de lumière pour rebondir sur les lignes parallèles, les codes QR peuvent être scannés numériquement par des appareils comme les smartphones.

Les codes QR sont utilisés dans les systèmes de cryptomonnaie pour permettre les paiements numériques, comme lors de l'affichage d'une adresse Bitcoin. Les codes QR sont également souvent utilisés pour communiquer les URLs de sites aux appareils mobiles.

Dans cet article, nous allons utiliser la bibliothèque `segno` pour créer de beaux codes QR qui remplissent de nombreuses fonctions.

## Qu'est-ce que Segno ?

[Segno](https://pypi.org/project/segno/0.1.5/#:~:text=Segno%20%E2%80%93%20Python%20QR%20Code%20and,Codes%20with%20nearly%20no%20effort.) est un générateur de codes QR open-source qui vous permet de créer des codes QR réguliers et micro avec très peu d'effort. Il n'a également aucune dépendance.

Segno offre plusieurs types de sérialisation comme SVG, EPS, PNG, PDF et sortie texte. Aucun de ces sérialiseurs ne fait appel à une bibliothèque externe. Grâce à un design de plugin, Segno offre d'autres types de sérialisation. PyPy et les versions Python 2.6 à 3.4 ont été utilisées pour les tests.

### Comment installer Segno

Comme pour toute autre bibliothèque Python, vous pouvez installer Segno via pip.

```py
pip install segno
```

## Comment créer un QR code

Alors, en utilisant la méthode `.make()`, commençons par créer le QR code le plus basique possible. Puisque le contenu est si bref, Segno génère automatiquement un code QR "micro" de taille amusante, qui transporte des données brutes et que vous pouvez copier ou transférer.

```py
import segno

price_tag = segno.make("Hello World")
price_tag.save("hello-world.png")
```

Le QR code est généré et enregistré dans notre répertoire de projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Price-Tag.png)
_hello-world.png_

Nous pouvons ajouter une bordure au QR code pour le rendre plus attrayant. Vous pouvez le faire en ajoutant le paramètre `border` à la méthode `.save()`.

```py
import segno
qrcode = segno.make('Vampire Blues')
qrcode.save('vampire-blues.png', border=5)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/vampire-blues.png)
_output: vapire-blues.png_

Les QR codes que nous avons créés jusqu'à présent ont été très petits. Nous pouvons les agrandir en ajoutant le paramètre scale comme ceci :

```py
import segno
qrcode = segno.make_qr('Welcome')
qrcode.save('welcome.png', scale=10)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/welcome.png)
_welcome.png_

### Comment créer des QR codes colorés

Nous pouvons également créer des QR codes colorés avec Segno – ils sont vraiment magnifiques. Cela est possible grâce à de nombreux sérialiseurs qui acceptent les paramètres dark et light pour spécifier la couleur des modules sombres et des modules clairs.

Voici quelques exemples pour vous donner une idée de ce qui est possible :

```py
import segno
qrcode = segno.make("Green ave, Kingston")
qrcode.save('address.png', dark='darkred', light='lightblue', scale=10)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/address.png)
_address.png_

```py
import segno
qrcode = segno.make("Green ave, Kingston")
# Modules sombres avec transparence alpha
qrcode.save('address2.png', dark='#0000ffcc', scale=10)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/address2.png)
_address2.png_

```py
import segno
micro_qrcode = segno.make('Rain', error='q')
micro_qrcode.save('rain.png', dark='darkblue', data_dark='steelblue', scale=5)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/rain.png)
_rain.png_

## Comment enregistrer des QR codes dans différents formats

Segno nous offre la flexibilité d'enregistrer nos QR codes générés dans différents formats de fichiers tels que `.svg`, `.png`, `.eps` et `.pdf`.

Voici comment procéder :

```py
import segno
qrcode = segno.make('Beatles')
qrcode.save('Beatles.svg')
qrcode.save('Beatles.png')
qrcode.save('Beatles.eps')
```

## Cas d'utilisation des QR codes avec des exemples

### Comment créer un QR code pour le partage d'URL

Nous pouvons facilement générer un QR code qui pointe vers une URL. Cela nous permet d'obtenir du contenu en ligne en utilisant la même technique avec une charge utile un peu plus grande.

Nous allons créer un QR code qui pointe vers ma chaîne YouTube (Velcast Podcast), puis nous allons l'enregistrer.

Voici le code pour cela :

```py
import segno

video = segno.make('https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A')
video.save('Video.png', dark="yellow", light="#323524", scale=5)
```

Et le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Video.png)
_video.png_

### Comment créer un QR code pour une configuration WiFi

Nous pouvons également utiliser la bibliothèque Segno pour créer un QR code pour la configuration WiFi. Le module `segno.helpers` offre des méthodes de fabrication pour générer des QR codes standard pour encoder des coordonnées géographiques, des `vCards` et `MeCards`, des configurations `WIFI`, et des `EPC QR Codes`.

Le niveau de correction d'erreur "L" est utilisé pour créer des QR codes. Si possible, nous appliquerons le niveau de correction d'erreur supérieur sans modifier la version du QR Code.

La densité de l'image du QR code diminue avec la diminution du niveau de correction d'erreur, ce qui améliore la taille minimale d'impression. Plus le niveau de correction d'erreur est élevé, plus il peut résister aux dommages avant de perdre sa capacité à être lu.

L'équilibre optimal entre densité et robustesse pour une utilisation marketing générale est le niveau L ou le niveau M. Dans les environnements industriels où le maintien d'un QR code propre ou non endommagé peut être difficile, les niveaux Q et H sont les meilleures options.

```py
from segno import helpers

qrcode = helpers.make_wifi(ssid='MyWifi', password='1234567890', security='WPA')
qrcode.designator
'3-M'
qrcode.save('wifi-access.png', scale=10)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/wifi-access.png)
_wifi-access.png_

Nous pouvons également faire ce code de cette manière :

```py
import segno
wifi_settings = {    
    ssid='(Nom du Wifi)',    
    password='(Mot de passe du Wifi)',    
    security='WPA',
    }
wifi = segno.helpers.make_wifi(**wifi_settings)
wifi.save("Wifi.png", dark="yellow", light="#323524", scale=8)
```

Nous pouvons utiliser l'une ou l'autre des deux options pour le code. Elles donnent le même résultat mais représentent différents styles d'écriture et de présentation.

Les cas d'utilisation courants des QR codes pour l'accès WiFi incluent :

* Au lieu de donner aux consommateurs des codes d'accès uniques, les entreprises peuvent utiliser des QR codes pour offrir un accès WiFi gratuit. Les clients n'ont besoin que de scanner le code pour avoir accès.
* Les familles peuvent l'utiliser pour accorder aux visiteurs l'accès à leur internet à la maison.

### Comment encoder les détails de contact dans les QR codes

Nous pouvons également stocker des détails de contact dans un QR code. Nous devons simplement utiliser la méthode `helpers.make_mecard()` et nous pouvons passer les détails de contact. Il est également important de noter que nous pouvons passer une liste à la méthode.

Regardons un exemple :

```py
from segno import helpers
qrcode = helpers.make_mecard(name='Shittu Olumide', email='me@example.com', phone='+123456789')
qrcode.designator
'3-L'
# Certains paramètres acceptent plusieurs valeurs, comme email, phone, url
qrcode = helpers.make_mecard(name='Shittu Olumide', 
                             email=('me@example.com', 'email@example.com'),
                             url=['http://www.example.com', 'https://example.come/~olu'])
qrcode.save('mycontact.png', scale=5)
```

Segno vous permet également d'effectuer les actions suivantes :

* **segno.helpers.make_geo** : Lancer le programme de cartographie intégré à une certaine latitude et longitude.
* **segno.helpers.make_email** : Envoyer un message en utilisant un sujet et un corps prédéfinis. Excellent pour activer un nombre quelconque d'activités potentielles à partir d'un serveur de messagerie, comme s'abonner à des newsletters, enregistrer votre arrivée quelque part, et plus encore.
* **segno.helpers.make_epc_qr** : Initiation d'un paiement électronique.

### Cas d'utilisation des QR codes

Maintenant que vous avez appris à créer des QR codes, voici quelques-unes de leurs applications dans les entreprises et dans notre vie quotidienne :

* Paiements numériques.
* Partage d'informations commerciales.
* Partage d'informations de contact personnelles.
* Menus QR codes dans les restaurants.
* Facilitation de l'authentification WiFi.

Et bien plus encore.

## Conclusion

Espérons que cet article court a aiguisé votre appétit et vous inspire à utiliser des QR codes dans votre travail et vos projets personnels.

En développant quelques QR codes attrayants et fonctionnels dans cet article, nous avons testé le module Segno Python. Vous pouvez lire la documentation officielle pour en savoir plus sur la bibliothèque.