---
title: Comment découvrir des sous-domaines cachés en tant que hacker éthique
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-01-07T19:46:53.022Z'
originalURL: https://freecodecamp.org/news/how-to-discover-hidden-subdomains-as-an-ethical-hacker
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1735806321604/dec39da9-6dd8-4a73-ba64-5cf894ce34f4.webp
tags:
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: gobuster
  slug: gobuster
- name: domain
  slug: domain
- name: subdomains
  slug: subdomains
- name: fuzzing
  slug: fuzzing
- name: Ethical Hacking
  slug: ethical-hacking
seo_title: Comment découvrir des sous-domaines cachés en tant que hacker éthique
seo_desc: 'Subdomains are an essential part of a website’s infrastructure. They provide
  additional functions in a web application, such as APIs, admin portals, and staging
  environments.

  As an ethical hacker, discovering subdomains is a critical step in learning...'
---

Les sous-domaines sont une partie essentielle de l'infrastructure d'un site web. Ils fournissent des fonctions supplémentaires dans une application web, telles que les API, les portails d'administration et les environnements de préproduction.

En tant que hacker éthique, la découverte de sous-domaines est une étape cruciale pour comprendre la surface d'attaque d'une cible. Les sous-domaines peuvent ne pas être bien protégés, contrairement au domaine principal. Ils peuvent donc être un excellent point d'entrée pour des audits de sécurité ou des programmes de bug bounty.

Dans cet article, je vais vous expliquer comment trouver des sous-domaines en utilisant plusieurs méthodes. Nous utiliserons [tesla.com](http://tesla.com/) comme exemple pour la recherche de sous-domaines.

> *Remarque : tesla.com fait partie des programmes de bug bounty, nous avons donc la permission de le scanner pour des sous-domaines. Si vous faites cela sur une autre application web, assurez-vous d'avoir la permission.*

## **Crt.sh**

L'une des façons les plus simples de commencer est de vérifier les journaux de transparence des certificats (CT) en utilisant [crt.sh](https://crt.sh/). Ce site web enregistre chaque certificat SSL/TLS émis pour un domaine, y compris les sous-domaines.

Pour rechercher les sous-domaines de Tesla, visitez [crt.sh](https://crt.sh/) et entrez `%.tesla.com` comme requête. Le `%` agit comme un caractère générique pour correspondre à n'importe quel sous-domaine.

Regardons les résultats :

![recherche de sous-domaines de tesla.com - résultats de l'exécution de tesla.com via crt.sh](https://cdn.hashnode.com/res/hashnode/image/upload/v1735806389562/eabc92c8-6fff-45fb-ba1c-00f582a31c4f.webp align="center")

Nous pouvons voir beaucoup de sous-domaines intéressants listés dans les résultats. Ces sous-domaines peuvent appartenir à différentes parties de l'infrastructure de Tesla.

Par exemple, `shop.tesla.com` est probablement pour leur boutique en ligne, tandis que `api.tesla.com` pourrait héberger des interfaces de programmation d'applications.

L'utilisation de `crt.sh` est passive, ce qui signifie qu'elle n'interagit pas avec la cible, ce qui la rend à la fois sûre et discrète.

Notez que [crt.sh](http://crt.sh) n'affichera que les sous-domaines qui ont des certificats valides. Si un sous-domaine utilise des certificats auto-signés ou n'utilise pas du tout SSL/TLS, il peut ne pas apparaître dans ces journaux. Malgré cette limitation, [crt.sh](http://crt.sh) reste un point de départ rapide et efficace pour l'énumération de sous-domaines.

## **Sublist3r**

[Sublist3r](https://github.com/aboul3la/Sublist3r) est un outil open-source pour automatiser la recherche de sous-domaines. Il est utile dans les évaluations de sécurité et la reconnaissance générale.

En utilisant plusieurs moteurs de recherche (comme Google, Bing, Yahoo, et plus), Sublist3r trouve des sous-domaines qui pourraient autrement rester cachés.

L'interface en ligne de commande de Sublist3r est simple à utiliser — vous lui donnez un domaine, et Sublist3r se met au travail.

Grâce à sa nature open-source, il est activement maintenu et amélioré par la communauté de la sécurité.

Sublist3r n'est pas préinstallé sur Kali, alors allons-y et installons-le. Tout d'abord, clonez le dépôt et installez les dépendances :

```plaintext
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
sudo pip install -r requirements.txt
```

Maintenant, nous sommes prêts à utiliser l'outil sublist3r. Voici la syntaxe à utiliser avec sublist3r :

```plaintext
python sublist3r.py -d tesla.com
```

Après quelques minutes, Sublist3r retournera une liste de sous-domaines découverts. Le drapeau `-d` indique à sublist3r que le domaine à utiliser est tesla.com

![réponse de sublist3r](https://cdn.hashnode.com/res/hashnode/image/upload/v1735806446961/b2f239bf-5a9b-4da6-a875-d9326e2b0621.webp align="center")

Vous pouvez voir que sublist3r a trouvé plus de 300 sous-domaines de [tesla.com](http://tesla.com). Sublist3r est un excellent moyen de démarrer le processus de reconnaissance, surtout si vous souhaitez automatiser la collecte de sous-domaines sans installer de nombreux outils séparés.

Notez que Sublist3r dépend des API de ces moteurs de recherche et d'autres sources de données. Il peut donc parfois manquer des sous-domaines qui n'ont pas été explorés ou indexés.

## **Google Dorking**

Le Google dorking (parfois appelé "Google hacking") fait référence à la pratique d'utiliser des requêtes de recherche spéciales sur Google. Ces opérateurs aident à trouver des informations cachées, des données sensibles ou d'autres ressources qui seraient autrement difficiles à localiser.

Les opérateurs courants incluent `site:`, `inurl:`, `filetype:`, et `intitle:`, parmi beaucoup d'autres. Commençons par l'opérateur `site:`:

```plaintext
site:*.tesla.com
```

Cette requête recherche n'importe quel sous-domaine de [`tesla.com`](http://tesla.com). Voici quelques résultats de recherche.

![google dork de tesla.com](https://cdn.hashnode.com/res/hashnode/image/upload/v1735806489328/fb4187aa-aa35-45d7-b975-5487de0093e2.webp align="center")

Pour creuser plus profond, essayez de combiner `site:` avec d'autres opérateurs. Par exemple, nous pouvons utiliser l'opérateur `inurl` avec le mot-clé 'admin' pour trouver des URL contenant le mot admin.

```plaintext
site:*.tesla.com inurl:admi
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1735806522371/02c44cdd-1bc3-4c8c-822a-16f883b6c166.webp align="center")

En utilisant ces opérateurs (connus sous le nom de Google dorks), vous pouvez filtrer les résultats de recherche pour trouver des types de fichiers spécifiques, des répertoires, ou même des informations privées qui peuvent être exposées involontairement sur Internet.

Le dorking peut produire beaucoup de données, vous devrez donc peut-être filtrer soigneusement vos recherches pour éviter d'être submergé par des informations non pertinentes.

[Voici un tutoriel complet](https://www.stealthsecurity.sh/p/google-dorking-the-ultimate-guide-to-finding-hidden-information-on-the-web) sur le Google dorking.

## **Fuzzing avec GoBuster**

Maintenant, que faire si les sous-domaines d'une cible ne sont listés nulle part sur Internet ? Nous utilisons le fuzzing.

Le fuzzing consiste simplement à brute-forcer des noms de sous-domaines potentiels en essayant des combinaisons à partir d'une liste de mots. Une liste de mots est une liste de mots que nous utiliserons avec l'outil de fuzzing pour voir si un sous-domaine existe.

Une liste de mots de sous-domaines peut contenir des mots comme :

```plaintext
ftp
root
admin
portal
api
```

Des outils comme Gobuster et Ffuf peuvent utiliser une liste de mots pour vérifier si ces sous-domaines existent. Voici un exemple de [liste de mots de sous-domaines](https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/DNS/subdomains-top1million-110000.txt).

### **Comment fonctionne Gobuster**

[Gobuster](https://www.stealthsecurity.sh/p/finding-hidden-directories-subdomains-s3-buckets-using-gobuster) est un outil de brute-force rapide pour découvrir des URL, des fichiers et des répertoires cachés dans les sites web.

Ffuf est un merveilleux fuzzer web, mais Gobuster est une alternative plus rapide et plus flexible. Gobuster prend en charge les extensions avec lesquelles nous pouvons augmenter ses capacités.

Gobuster peut également évoluer en utilisant plusieurs threads et effectuer des scans parallèles pour accélérer les résultats.

Gobuster est préinstallé dans Kali Linux. Exécutons la commande suivante pour rechercher des sous-domaines. Vous pouvez trouver la liste de mots sous /usr/share/wordlists/SecLists dans Kali Linux.

```plaintext
gobuster dns -d tesla.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt
```

La commande ci-dessus vérifie chaque mot dans la liste de mots pour voir s'il résout un sous-domaine valide. Voici un exemple de sortie :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1735806581200/46b3d437-9918-416c-a510-f647e9ac303e.webp align="center")

Les résultats de Gobuster montrent des sous-domaines valides, y compris certains qui peuvent ne pas apparaître dans les bases de données publiques, comme `staging.tesla.com` ou `dev.tesla.com`.

Le fuzzing doit être combiné avec d'autres méthodes car les résultats ne sont aussi bons que la liste de mots. Par exemple, prod-version-2.tesla.com peut être un sous-domaine qui peut ne pas faire partie de la liste de mots.

## **Autres méthodes pour la découverte de sous-domaines**

### **Transfert de zone DNS**

Bien que rare, des serveurs DNS mal configurés peuvent permettre des transferts de zone, révélant tous les sous-domaines en une seule fois. Vous pouvez tester cela en utilisant `dig` :

```plaintext
dig axfr @ns1.tesla.com tesla.com
```

Si le serveur est correctement sécurisé, il ne permettra pas un transfert de zone. Mais s'il est mal configuré, vous pourriez découvrir tous les sous-domaines utilisés par Tesla.

### **Outils en ligne**

Des sites web comme [SecurityTrails](https://securitytrails.com/), [Shodan](https://shodan.io/), et [Censys](https://censys.io/) agrègent des données de sous-domaines. Ces outils fournissent une vue centralisée des informations publiques disponibles.

### **Inspection des fichiers JavaScript**

Les sous-domaines apparaissent souvent dans les fichiers JavaScript d'un site web. En examinant le site web de Tesla, vous pourriez trouver des références à des points de terminaison d'API ou à d'autres sous-domaines.

## **Post-découverte de sous-domaines**

Une fois que vous avez une liste de sous-domaines, nous pouvons les sonder davantage. Nous pouvons découvrir des portails de connexion, des pages de développement ou des points de terminaison d'API.

Les hackers éthiques utilisent généralement des outils de scan de ports et d'énumération de services comme Nmap et Nikto pour trouver les ports ouverts et les services en cours d'exécution sur chaque sous-domaine. Identifier les logiciels obsolètes, les protocoles non sécurisés ou les identifiants par défaut est souvent l'étape critique suivante, car ce sont des points faibles courants dans tout environnement.

Les sous-domaines nous montrent souvent l'infrastructure plus large du site web s'ils sont laissés non protégés.

## **Conclusion**

La découverte de sous-domaines est une compétence cruciale pour les hackers éthiques. Elle nous aide à comprendre le tableau complet d'une application web. Plus nous en savons, meilleurs sont les points d'entrée que nous avons pour obtenir un accès.

Avant d'utiliser ces techniques, assurez-vous toujours d'avoir une autorisation appropriée. La découverte de sous-domaines aide aux audits de sécurité en découvrant des actifs cachés et en aidant les organisations à se protéger contre les menaces potentielles.

Pour plus de tutoriels pratiques sur la cybersécurité, rejoignez notre [**newsletter hebdomadaire**](https://www.stealthsecurity.sh/). Si vous souhaitez pratiquer ces techniques de découverte de sous-domaines à travers un laboratoire pratique, rejoignez-nous au [**Hacker's Hub**](https://www.skool.com/hackershub).