---
title: Ce qui rend le code vulnérable – et comment le corriger
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-04-21T16:59:21.428Z'
originalURL: https://freecodecamp.org/news/what-makes-code-vulnerable-and-how-to-fix-it
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745251285687/7ce5aca0-1edc-49e4-879d-b5690cbb64ea.png
tags:
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: vulnerability
  slug: vulnerability
- name: coding
  slug: coding
- name: Validation
  slug: validation
seo_title: Ce qui rend le code vulnérable – et comment le corriger
seo_desc: 'Writing code is relatively easy. But writing secure code is much harder.

  The truth is, most developers don’t realize their code is vulnerable until something
  breaks. Or, worse, until someone attacks it. So if you want secure code, you first
  have to k...'
---

Écrire du code est relativement facile. Mais écrire du code sécurisé est beaucoup plus difficile.

La vérité est que la plupart des développeurs ne réalisent pas que leur code est vulnérable jusqu'à ce que quelque chose se casse. Ou, pire, jusqu'à ce que quelqu'un l'attaque. Donc, si vous voulez un code sécurisé, vous devez d'abord savoir à quoi ressemble un mauvais code.

Dans ce tutoriel, nous verrons 10 signes clairs que votre code pourrait être vulnérable aux attaques. Et plus important encore, comment le corriger.

### Voici ce que nous allons couvrir :

* [1\. Informations d'identification codées en dur](#heading-1-informations-didentification-codees-en-dur)

* [2\. Aucune validation des entrées](#heading-2-aucune-validation-des-entrees)

* [3\. Gestion des erreurs médiocre](#heading-3-gestion-des-erreurs-mediocre)

* [4\. Dépendances obsolètes](#heading-4-dependances-obsoletes)

* [5\. Aucune authentification ou authentification faible](#heading-5-aucune-authentification-ou-authentification-faible)

* [6\. Vérifications d'autorisation manquantes](#heading-6-verifications-dautorisation-manquantes)

* [7\. Données sensibles exposées dans les URLs](#heading-7-donnees-sensibles-exposees-dans-les-urls)

* [8\. Aucune limitation de débit](#heading-8-aucune-limitation-de-debit)

* [9\. Téléchargements de fichiers non sécurisés](#heading-9-telechargements-de-fichiers-non-securises)

* [10\. HTTPS manquant](#heading-10-https-manquant)

* [Réflexions finales](#heading-reflexions-finales)

## **1\. Informations d'identification codées en dur**

Cela est *partout*. Peut-être l'avez-vous vu vous-même – une clé API située directement dans le code. Un mot de passe de base de données écrit en texte brut.

Cela ressemble à ceci :

```plaintext
DB_PASSWORD = "supersecret123"
API_KEY = "sk_test_abc123"
```

Si ce code est divulgué (et il le sera), les attaquants peuvent faire ce qu'ils veulent. Ils peuvent se connecter à vos systèmes, voler vos données ou accumuler des factures énormes sur les services cloud – tout cela sans effort.

Et voici la partie effrayante : ce type de fuite ne se produit pas seulement lorsque votre projet entier est piraté. Cela peut se produire lorsque quelqu'un pousse du code vers GitHub et oublie d'ajouter `.env` à `.gitignore`. Boum – vos clés secrètes sont maintenant publiques.

### **Comment s'en protéger**

Ne codez jamais en dur les données sensibles comme les clés API, les mots de passe de base de données ou les jetons. Utilisez plutôt des variables d'environnement.

Celles-ci sont cachées du code source et peuvent être gérées en toute sécurité par environnement (dev, test, production). Par exemple, un fichier `.env` importé dans votre base de code :

```plaintext
import os
db_password = os.getenv("DB_PASSWORD")
```

## **2\. Aucune validation des entrées**

Si vous faites confiance à l'entrée utilisateur, vous êtes déjà dans l'embarras. Les attaquants adorent envoyer des choses étranges, comme des chaînes de caractères très longues, des caractères bizarres ou des formats inattendus.

Voici à quoi cela ressemble :

```plaintext
username = request.GET['username']
print("Hello " + username)
```

Maintenant, quelqu'un entre :

```plaintext
username=Robert'); DROP TABLE users; --
```

**Boum.** Vous venez d'être injecté en SQL. Votre table de base de données ? Disparue.

Sans validation, votre application peut se casser ou même être détournée. Les mauvaises entrées peuvent entraîner des problèmes comme l'injection SQL, le cross-site scripting (XSS) et des bugs généraux.

En gros, vous donnez aux attaquants un chèque en blanc.

### **Comment s'en protéger**

Assurez-vous de valider toutes les entrées. Par exemple :

```plaintext
import re
email = request.GET.get('email')
if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    return "Format d'email invalide"
```

Utilisez des requêtes paramétrées. Ne construisez jamais de chaînes SQL à partir d'entrées utilisateur brutes :

```plaintext
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
```

Et utilisez des types de données stricts. Ne supposez pas que l'entrée est propre. Faites-la passer un test. Limitez la longueur de l'entrée. Personne n'a besoin d'un nom d'utilisateur de 5 000 caractères. Échappez les caractères spéciaux, surtout si vous utilisez l'entrée en HTML ou SQL.

## **3\. Gestion des erreurs médiocre**

Voici à quoi ressemble une gestion des erreurs paresseuse :

```plaintext
except Exception as e:
    print(e)  # Expose les erreurs internes à l'utilisateur
```

Ou pire :

```plaintext
except:
    pass  # Ignore silencieusement toutes les erreurs
```

Dans le premier exemple, l'erreur est entièrement affichée à l'utilisateur. Le deuxième exemple ignore toutes les erreurs.

Les erreurs silencieuses sont dangereuses. Et montrer des messages d'erreur complets aux utilisateurs ? C'est comme leur donner une carte de votre système.

Imaginez qu'une erreur de base de données apparaît en production, et votre application affiche quelque chose comme :

```plaintext
psycopg2.OperationalError: could not connect to server: Connection refused
```

Super – maintenant les attaquants savent quelle base de données vous utilisez, et ils pourraient commencer à fouiner.

### **Comment s'en protéger**

* **Journalisez les erreurs détaillées** – mais faites-le de manière sécurisée. Utilisez des outils ou services de journalisation, et ne stockez pas les journaux là où les utilisateurs peuvent les voir.

* **Montrez aux utilisateurs des messages simples** comme :
  `"Oups ! Quelque chose s'est mal passé. Veuillez réessayer plus tard."`
  C'est tout ce qu'ils ont besoin de savoir.

* **Ne exposez jamais les traces de pile en production.** Désactivez le mode débogage et utilisez des pages d'erreur appropriées.

* **Gérez les exceptions spécifiques** lorsque cela est possible, afin de savoir exactement ce qui a échoué et pourquoi.

Exemple :

```plaintext
try:
    process_data()
except ValueError as e:
    logger.error(f"Erreur de données : {e}")
    return "Entrée invalide. Veuillez vérifier vos données."
except Exception as e:
    logger.exception("Erreur inattendue")
    return "Quelque chose s'est mal passé. Réessayez plus tard."
```

Utilisez des outils de surveillance des erreurs comme Sentry, Rollbar ou LogRocket. Ils capturent les erreurs, les suivent et vous aident à les corriger – avant même que les utilisateurs ne les remarquent.

## **4\. Dépendances obsolètes**

Utiliser des anciens packages, c'est comme laisser votre porte d'entrée grande ouverte. Les attaquants savent exactement où se trouvent les points faibles – et ils les recherchent activement.

Si votre fichier `package.json` ou `requirements.txt` n'a pas changé depuis des années, c'est un signal d'alarme.

### **Comment s'en protéger**

* **Mettez à jour régulièrement.** Les nouvelles versions corrigent souvent des failles de sécurité.

* **Auditez vos dépendances.** Utilisez des outils comme `npm audit` et `pip-audit` en fonction de votre base de code.

* **Automatisez les mises à jour** avec des outils comme Dependabot, Renovate ou PyUp.

```plaintext
pip-audit
# ou
npm audit
```

Même les petits packages peuvent avoir de grands impacts. Restez à jour, restez en sécurité.

## **5\. Aucune authentification ou authentification faible**

Si votre application laisse n'importe qui entrer sans vérifier qui ils sont, c'est la fin du jeu. Les connexions faibles sont tout aussi dangereuses.

Les erreurs courantes incluent :

* **Aucune règle de complexité des mots de passe** – Les mots de passe faibles comme "123456" ou "password" peuvent être craqués en quelques secondes en utilisant des attaques par force brute ou par dictionnaire.

* **Stockage des mots de passe en texte brut** – Si votre base de données est jamais compromise, toutes les informations d'identification des utilisateurs sont exposées instantanément, entraînant des fuites massives de données et des prises de contrôle de comptes.

* **Aucun verrouillage de compte après plusieurs tentatives de connexion échouées** – Sans limite sur les tentatives de connexion, les attaquants peuvent continuer à deviner les mots de passe indéfiniment en utilisant des outils automatisés.

### **Comment s'en protéger**

Tout d'abord, vous pouvez hacher les mots de passe en utilisant des algorithmes robustes comme `bcrypt`.

Voici un exemple en Python :

```plaintext
import bcrypt
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
```

Vous pouvez également imposer des politiques de mots de passe robustes (longueur minimale, symboles, etc.) et utiliser l'authentification multifacteur (MFA) si disponible pour une protection supplémentaire.

Quelques lignes de code supplémentaires peuvent empêcher une violation à grande échelle.

## **6\. Vérifications d'autorisation manquantes**

L'authentification vérifie *qui vous êtes*. L'autorisation vérifie *ce que vous pouvez faire*. Sauter la seconde, c'est comme donner à tout le monde un accès administrateur.

Exemple :

```plaintext
@app.route('/user/<id>')
def get_user(id):
    return User.query.get(id)
```

Ici, il n'y a aucune vérification pour voir si l'utilisateur actuel est autorisé à voir ces données.

### **Comment s'en protéger**

```plaintext
@app.route('/user/<id>')
@login_required
def get_user(id):
    if current_user.id != int(id):
        return "Non autorisé", 403
    return User.query.get(id)
```

Dans le code ci-dessus, une connexion est requise et l'utilisateur est vérifié avant de lui donner accès aux données.

* Vérifiez toujours la propriété et les rôles avant d'afficher ou de modifier des données.

* Implémentez des règles de contrôle d'accès dans votre API et votre frontend.

* Ne faites pas confiance aux IDs du frontend – vérifiez également sur le backend.

## **7\. Données sensibles exposées dans les URLs**

Vous avez déjà vu un lien de réinitialisation de mot de passe comme celui-ci ?

```plaintext
https://example.com/reset-password?token=abcd1234
```

Cela semble inoffensif – mais ce n'est pas le cas. Les jetons, les IDs de session et les clés API **ne devraient jamais être dans les URLs**. Ils sont enregistrés dans :

* L'historique du navigateur

* Les journaux du serveur

* Les outils d'analyse

### **Comment s'en protéger**

Assurez-vous d'envoyer les données sensibles uniquement dans les requêtes POST ou les en-têtes, comme ceci :

```plaintext
POST /reset-password
Authorization: Bearer abcd1234
```

## **8\. Aucune limitation de débit**

La limitation de débit est une technique de sécurité qui contrôle le nombre de fois qu'un utilisateur (ou un système) peut faire une requête à votre serveur dans un laps de temps donné – par exemple, pas plus de 10 tentatives de connexion par minute.

Sans limites de débit,

* Un attaquant peut faire 1 000 tentatives de connexion en une minute

* Votre serveur peut planter sous des requêtes falsifiées

### **Comment s'en protéger**

Définissez une limite maximale de requêtes par IP ou utilisateur. Vous pouvez utiliser des outils comme Cloudflare ou des outils intégrés dans les langages de programmation pour cela. Par exemple, en Python, nous pouvons utiliser flask_limiter.

```plaintext
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(app, key_func=get_remote_address)

@app.route("/login")
@limiter.limit("5 per minute")
def login():
    # logique de connexion
```

Dans le code ci-dessus, les tentatives de connexion sont limitées à 5 par minute. Arrêtez les abus avant qu'ils ne commencent.

## **9\. Téléchargements de fichiers non sécurisés**

Permettre aux utilisateurs de télécharger des fichiers ? Cool. Mais si vous n'êtes pas prudent, ils peuvent :

* Télécharger des logiciels malveillants

* Écraser des fichiers clés

* Exécuter des scripts sur votre serveur

Voici un exemple d'une erreur courante :

```plaintext
file.save(f"/uploads/{file.filename}")
```

N'importe quel type de fichier pourrait être téléchargé de cette manière.

### **Comment s'en protéger**

Pour commencer, vous pouvez renommer les fichiers avant de les enregistrer :

```plaintext
pythonCopyEditimport uuid
filename = str(uuid.uuid4()) + ".jpg"
```

Vous pouvez vérifier le type de contenu (pas seulement l'extension de fichier) :

```plaintext
pythonCopyEditif file.content_type not in ["image/jpeg", "image/png"]:
    return "Type de fichier invalide"
```

Vous pouvez également stocker les fichiers en dehors du répertoire public, et enfin limiter la taille des fichiers dans votre configuration serveur et votre code backend.

## **10\. HTTPS manquant**

Si votre application utilise toujours le vieux HTTP, toutes les données voyagent en clair – y compris :

* Mots de passe

* Jetons

* Informations personnelles

Les attaquants peuvent tout renifler avec des outils comme [Wireshark](https://www.freecodecamp.org/news/learn-wireshark-computer-networking/).

### **Comment s'en protéger**

Pour commencer, vous pouvez utiliser HTTPS partout et obtenir un certificat SSL gratuit de [Let’s Encrypt](https://letsencrypt.org/).

Vous pouvez également rediriger le trafic non sécurisé – voici comment vous le feriez dans Flask, par exemple :

```plaintext
@app.before_request
def before_request():
    if not request.is_secure:
        return redirect(request.url.replace("http://", "https://"))
```

Le chiffrement du trafic n'est pas optionnel – c'est une nécessité pour les applications modernes.

## **Réflexions finales**

Écrire du code sécurisé ne consiste pas à être parfait. Il s'agit d'être prudent. Ralentissez. Regardez votre code avec un regard neuf. Pensez comme un attaquant. Prévoyez l'échec avant qu'il ne se produise.

La meilleure sécurité n'est pas ajoutée plus tard – elle est intégrée dès le départ.

Pour plus de tutoriels sur la cybersécurité, [inscrivez-vous à ma newsletter](https://newsletter.stealthsecurity.sh/). Nouveau dans la cybersécurité ? Consultez mon [Cours de démarrage en sécurité](https://start.stealthsecurity.sh/).