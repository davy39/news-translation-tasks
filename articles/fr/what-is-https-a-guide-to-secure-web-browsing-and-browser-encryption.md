---
title: Qu'est-ce que HTTPS ? Un guide pour la navigation web sécurisée et le chiffrement
  du navigateur
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-13T18:05:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-https-a-guide-to-secure-web-browsing-and-browser-encryption
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/HTTPS-image.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: https
  slug: https
seo_title: Qu'est-ce que HTTPS ? Un guide pour la navigation web sécurisée et le chiffrement
  du navigateur
seo_desc: 'You may have noticed the "https" at the beginning of a URL. Or you may
  have noticed a lock in the URL bar of your browser.

  What does "https" mean? What does the lock icon in your browser mean? These things
  are key to secure web browsing. In this arti...'
---

Vous avez peut-être remarqué le "https" au début d'une URL. Ou vous avez peut-être remarqué un cadenas dans la barre d'URL de votre navigateur.

Que signifie "https" ? Que signifie l'icône de cadenas dans votre navigateur ? Ces éléments sont essentiels pour une navigation web sécurisée. Dans cet article, vous apprendrez tout sur la navigation web sécurisée et le chiffrement du navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-6.png)

Le "S" dans "HTTPS" signifie **Sécurisé**. Apprenons d'abord ce qu'est HTTP.

## Qu'est-ce que HTTP ?

HTTP (qui signifie HyperText Transfer Protocol) est un protocole réseau. Il indique aux navigateurs web comment se connecter aux pages web et à d'autres documents sur Internet. Il est sans connexion, ce qui signifie qu'une nouvelle connexion est établie chaque fois qu'un navigateur doit charger un nouveau fichier ou élément.

Si vous tapez une URL de site web dans votre navigateur, le navigateur enverra une requête HTTP au serveur hébergeant le site web. Le serveur renverra ensuite la page web demandée, en envoyant chaque partie (c'est-à-dire images, texte, styles) séparément.

Il y a cependant un problème majeur avec HTTP. Les informations transmises en utilisant HTTP ne sont pas chiffrées du tout. Toute personne qui sait comment faire peut surveiller le trafic et voir toutes les données transmises. Cela inclut les noms d'utilisateur et les mots de passe !

HTTPS sécurise et chiffre tout le processus.

## Qu'est-ce que HTTPS ?

HTTPS (HyperText Transfer Protocol Secure) assure une communication sécurisée entre un navigateur et un serveur web. Il chiffre chaque paquet de données envoyé en utilisant soit le chiffrement SSL, soit TLS. Sans cette sécurité supplémentaire, toute information que vous entrez sur un site sera envoyée en texte clair et pourrait potentiellement être vue par quelqu'un essayant de pirater vos données.

TLS est plus récent et plus sécurisé que SSL, et est ce que la plupart des sites HTTPS utilisent. TLS s'assurera que les deux parties sont bien celles qu'elles prétendent être. Il s'assure également que les données envoyées n'ont pas été altérées.

TLS utilise le chiffrement asymétrique pour créer un lien entre l'utilisateur et le serveur en utilisant des clés privées/publiques. Ces clés sont comme un ensemble de serrure et clé. L'une chiffre les données avec une serrure et la personne déchiffre les données avec une clé.

Les serveurs passent au chiffrement symétrique après le début de la session car il est plus rapide et peut transmettre de plus grandes quantités de données. Au lieu d'utiliser une clé publique/privée, le chiffrement symétrique utilise un secret partagé. C'est comme parler à quelqu'un dans une pièce que personne d'autre ne connaît. Puisque la pièce est secrète, vous n'avez pas à vous soucier que d'autres personnes soient dans la pièce et entendent ce dont vous parlez.

La plupart des sites aujourd'hui utilisent HTTPS au lieu de HTTP puisque cela présente des avantages majeurs et peu d'inconvénients.

Avant de soumettre des informations confidentielles telles que des mots de passe, vous devriez toujours vous assurer que le site utilise HTTPS.

La plupart des navigateurs web afficheront une icône de cadenas à gauche de l'URL pour indiquer que le site est sécurisé. De plus, la plupart des navigateurs avertiront les utilisateurs avec un avertissement 'non sécurisé' si le site n'utilise pas HTTPS.

## Réseaux Privés Virtuels

Même avec HTTPS activé, les FAI sauront toujours quels sites web vous visitez, même s'ils ne savent pas ce que vous y faites.

Et savoir simplement où vous allez — les "métadonnées" de votre activité web — donne aux FAI beaucoup d'informations qu'ils peuvent vendre.

Donc, si vous voulez prendre la sécurité au niveau supérieur, envisagez d'utiliser un Réseau Privé Virtuel (VPN). Les VPN chiffreront tout, y compris les sites web que vous visitez. Pour plus d'informations sur les VPN et comment en configurer un, consultez [cet article de Quincy Larson](https://www.freecodecamp.org/news/how-to-set-up-a-vpn-in-5-minutes-for-free-and-why-you-urgently-need-one-d5cdba361907/).