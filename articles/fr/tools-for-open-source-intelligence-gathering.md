---
title: Outils que vous pouvez utiliser pour la collecte de renseignement d'origine
  source ouverte (OSINT)
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-10-28T19:01:56.048Z'
originalURL: https://freecodecamp.org/news/tools-for-open-source-intelligence-gathering
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730102596033/092e5f4f-638a-437f-923f-89fba4185a61.jpeg
tags:
- name: cyber security
  slug: cyber-security
- name: Open Source
  slug: opensource
- name: OSINT
  slug: osint
seo_title: Outils que vous pouvez utiliser pour la collecte de renseignement d'origine
  source ouverte (OSINT)
seo_desc: 'Welcome to the world of Open-Source Intelligence (OSINT). OSINT is all
  about gathering public information from various online sources.

  OSINT can come from social media, websites, search engines, and even public databases.
  You’d be surprised at how mu...'
---

Bienvenue dans le monde du renseignement d'origine source ouverte (OSINT). L'OSINT consiste à collecter des informations publiques à partir de diverses sources en ligne.

L'OSINT peut provenir des médias sociaux, des sites web, des moteurs de recherche et même des bases de données publiques. Vous seriez surpris de la quantité d'informations précieuses disponibles. Et ce sont des informations librement accessibles à toute personne ayant les compétences nécessaires pour les trouver.

Les techniques OSINT vous permettent d'exploiter ces données pour découvrir des modèles, suivre des comportements et parfois même faire des prédictions.

Les entreprises utilisent également l'OSINT pour se protéger contre les cybermenaces. Les forces de l'ordre l'utilisent pour enquêter sur des affaires. Et les experts en cybersécurité l'utilisent pour identifier les vulnérabilités potentielles avant les attaquants.

Dans cet article, vous découvrirez les sept principaux outils utilisés dans la collecte de renseignement d'origine source ouverte.

**Remarque : L'OSINT doit toujours être utilisé de manière éthique. Respectez les lois sur la vie privée et comprenez les limites de la collecte légale de données. L'objectif est de collecter des informations de manière responsable à des fins de recherche, de sécurité ou d'investigation.**

## **Google Dorking — Moteurs de recherche surpuissants**

Le Google Dorking est une technique qui vous permet d'utiliser les opérateurs de recherche avancés de Google pour trouver des données cachées. Ces opérateurs peuvent affiner vos résultats de recherche pour trouver exactement ce que vous cherchez, même si ces données ne sont pas faciles à trouver via une recherche Google de base.

Par exemple, utiliser `financial report site:`[`miscosoft.com`](http://miscosoft.com) `filetype:pdf` nous donnera les fichiers PDF contenant le texte "financial report" du site [microsoft.com](http://microsoft.com).

![rapports financiers pdf](https://cdn.hashnode.com/res/hashnode/image/upload/v1730102651973/a1a2dc42-e130-45cd-8005-5bddfe7674ab.jpeg align="center")

D'autres opérateurs courants incluent :

* `site:` pour rechercher dans un site web spécifique.

* `intitle:` pour rechercher des mots spécifiques dans le titre des pages web.

* `inurl:` pour trouver des termes spécifiques dans les URLs.

[Voici un tutoriel détaillé sur le Google Dorking](https://www.freecodecamp.org/news/google-dorking-how-to-find-hidden-information-on-the-web/) si vous souhaitez en savoir plus.

En utilisant le Google Dorking, vous pouvez trouver des documents, des fichiers exposés, des pages de connexion et d'autres informations qui pourraient autrement être cachées.

## **Collecte d'emails, d'IP et plus avec theHarvester**

[theHarvester](https://github.com/laramies/theHarvester) est un outil spécialement conçu pour la collecte d'OSINT. Il peut collecter des adresses email, des sous-domaines, des IP et plus encore en interrogeant divers moteurs de recherche et bases de données.

Il est incroyablement utile lorsque vous souhaitez collecter rapidement des informations sur une cible spécifique, comme une entreprise ou un site web.

Pour utiliser theHarvester, il vous suffit d'entrer un domaine, et il extraira les données de sources comme Google, Bing, LinkedIn et autres. Par exemple :

```plaintext
theHarvester -d kali.org -b bing
```

Cette commande indique à theHarvester de rechercher sur Bing des informations liées à [`kali.`](http://example.com/)`org`. En quelques secondes, vous pouvez obtenir une liste d'emails, d'adresses IP et d'autres informations qui peuvent être publiques.

![résultat theHarvester pour kali.org](https://cdn.hashnode.com/res/hashnode/image/upload/v1730102690834/44f66e2d-b1be-442f-b833-b1fc6923c9b8.jpeg align="center")

## **Extraction de métadonnées avec ExifTool**

Les métadonnées sont des données sur les données. Les fichiers, comme les PDF et les images, contiennent souvent des métadonnées qui peuvent révéler des détails utiles.

Cela peut inclure des informations comme l'auteur d'un document, le logiciel utilisé pour le créer, et même l'emplacement où une photo a été prise.

[ExifTool](https://github.com/exiftool/exiftool) se spécialise dans l'extraction de métadonnées à partir de fichiers. Vous pouvez voir des informations sur l'endroit et le moment où une image a été prise, ce qui peut être crucial dans certaines investigations.

L'utilisation d'ExifTool est simple :

```plaintext
exiftool file.jpg
```

Cette commande affichera toutes les métadonnées disponibles pour le fichier donné.

![résultat exif tool](https://cdn.hashnode.com/res/hashnode/image/upload/v1730103140901/50c90fe3-e141-4034-969d-8209da4b6104.jpeg align="center")

Soyez prudent lorsque vous utilisez des outils d'extraction de métadonnées, car certaines métadonnées peuvent contenir des informations sensibles.

## **Automatisation de la collecte d'informations avec Photon**

[Photon](https://github.com/s0md3v/Photon) est un puissant crawler web conçu pour automatiser la collecte de données à partir de sites web. Une fois que vous spécifiez une URL cible, Photon peut parcourir le site, collectant des informations comme des liens, des images, des emails et même des fichiers.

Photon est particulièrement utile pour les grands sites web où la collecte manuelle de données prendrait trop de temps.

Par exemple :

```plaintext
python3 photon.py -u https://example.com -o output_folder
```

Cette commande indique à Photon de crawler [`https://example.com`](https://example.com%60/) et de sauvegarder les données collectées dans un dossier appelé `output_folder`.

Voici un exemple de réponse après avoir crawlé le site archive.org :

![exemple de réponse Photon](https://cdn.hashnode.com/res/hashnode/image/upload/v1730103200363/f2679e98-f63e-4ecc-bed7-ae776b48301a.jpeg align="center")

Photon peut vous faire gagner beaucoup de temps en collectant des données étendues pour vous.

## **Trouver des noms d'utilisateur sur différentes plateformes avec Sherlock**

Sherlock est un outil qui recherche des noms d'utilisateur sur des centaines de plateformes de médias sociaux et de sites web. Si vous enquêtez sur quelqu'un ou effectuez une évaluation de sécurité, Sherlock peut rapidement vous montrer où un nom d'utilisateur spécifique existe en ligne.

Pour utiliser Sherlock :

```plaintext
python3 sherlock username
```

Remplacez `username` par le nom d'utilisateur que vous souhaitez rechercher. Sherlock vous indiquera si le nom d'utilisateur est enregistré sur des plateformes comme Twitter, Facebook, Instagram, et plus encore.

![exemple de réponse Sherlock](https://cdn.hashnode.com/res/hashnode/image/upload/v1730103240471/26843e89-42ca-4a57-a204-7877f74e10e0.jpeg align="center")

Cet outil est particulièrement utile pour identifier la présence en ligne d'une personne ou d'une entité.

## **Visualisation des relations avec Maltego**

[Maltego](https://www.maltego.com/) est un outil OSINT unique qui crée des cartes visuelles des relations entre les personnes, les entreprises et les entités. En utilisant des "transformations", Maltego vous permet de rechercher dans différentes sources de données et de cartographier les connexions.

![Maltego](https://cdn.hashnode.com/res/hashnode/image/upload/v1730103285033/947347c9-4773-49b6-9b10-8c84eb9f1c53.jpeg align="center")

L'approche visuelle de Maltego est utile pour les investigations où vous devez comprendre comment différents éléments sont liés entre eux. Il est populaire parmi les forces de l'ordre et les experts en cybersécurité pour cartographier des réseaux complexes.

## **Shodan — Moteur de recherche pour les appareils connectés à Internet**

[Shodan](https://www.shodan.io/) est un moteur de recherche spécialement conçu pour trouver des appareils de l'Internet des objets (IoT). Il vous permet de rechercher des appareils en ligne comme des webcams, des routeurs, des serveurs, et plus encore.

Shodan est largement utilisé en cybersécurité pour vérifier les appareils exposés qui pourraient avoir des vulnérabilités de sécurité.

![shodan](https://cdn.hashnode.com/res/hashnode/image/upload/v1730103337532/f4f07fb9-91ea-47c1-a858-1e67b0eac87a.jpeg align="center")

Pour utiliser Shodan, vous aurez besoin d'un compte. Une fois configuré, vous pouvez rechercher des appareils par adresse IP, localisation ou type d'appareil.

Les puissantes options de filtrage de Shodan en font un outil essentiel pour toute personne surveillant les appareils connectés. Vous pouvez [en savoir plus ici](https://www.freecodecamp.org/news/shodan-what-to-know-about-the-internets-most-dangerous-search-engine/).

# **Conclusion**

L'OSINT offre un pouvoir incroyable pour la collecte d'informations, mais avec ce pouvoir vient la responsabilité. Ces outils sont conçus pour vous aider à trouver des données publiques, mais vous devez toujours les utiliser de manière éthique et légale.

L'objectif de l'OSINT doit être la collecte responsable de données à des fins de recherche, de cybersécurité ou d'investigations — et non pour envahir la vie privée ou des activités illégales.

Pour plus de tutoriels sur la cybersécurité, [**inscrivez-vous à notre newsletter hebdomadaire**](https://www.stealthsecurity.sh/). Si vous êtes nouveau dans le domaine de la cybersécurité, consultez le [**Manuel du Hacker**](https://book.stealthsecurity.sh/).