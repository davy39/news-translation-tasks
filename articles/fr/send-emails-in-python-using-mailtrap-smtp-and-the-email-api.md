---
title: Comment envoyer des emails en Python en utilisant Mailtrap SMTP et l'API Email
subtitle: ''
author: Alex Tray
co_authors: []
series: null
date: '2025-03-28T13:59:31.054Z'
originalURL: https://freecodecamp.org/news/send-emails-in-python-using-mailtrap-smtp-and-the-email-api
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743110284000/6fb2a037-ddca-4625-acfb-cffbd167ec55.png
tags:
- name: Phyton
  slug: phyton
- name: smtp
  slug: smtp
- name: mailtrap
  slug: mailtrap
- name: api
  slug: api
seo_title: Comment envoyer des emails en Python en utilisant Mailtrap SMTP et l'API
  Email
seo_desc: "In this tutorial, I’ll walk you through the process of sending emails in\
  \ Python using two different methods: \n\nThe traditional SMTP setup with the built-in\
  \ ‘smtplib’ module. \n\nMailtrap email API via Mailtrap’s official SDK. \n\n\nIf\
  \ you’re unfamiliar wi..."
---

Dans ce tutoriel, je vais vous guider à travers le processus d'envoi d'emails en Python en utilisant deux méthodes différentes :

1. La configuration SMTP traditionnelle avec le module intégré 'smtplib'.

2. L'API email de Mailtrap via le SDK officiel de Mailtrap.

Si vous n'êtes pas familier avec les outils et les flux de travail, SMTP (Simple Mail Transfer Protocol) est le protocole couramment utilisé pour envoyer des emails via des applications et des sites web. Mailtrap est une plateforme de livraison d'emails conçue pour une haute délivrabilité avec des fonctionnalités axées sur la croissance et des analyses de pointe.

À la fin de cet article, vous comprendrez comment intégrer des capacités d'envoi d'emails dans des projets Python et utiliser Mailtrap pour une livraison d'emails fiable dans des scénarios réels.

## Table des matières

1. [Configuration 'smtplib'](#heading-installation-smtplib)

2. [Comment envoyer des emails avec Mailtrap SMTP](#heading-comment-envoyer-des-emails-avec-mailtrap-smtp)

3. [Comment envoyer des emails avec l'API Email de Mailtrap](#heading-comment-envoyer-des-emails-avec-lapi-email-de-mailtrap)

4. [Conclusion](#heading-conclusion)

## Configuration 'smtplib'

Pour commencer à envoyer des emails avec Python, je vais d'abord utiliser le module intégré 'smtplib'. Cela vous permet de vous connecter à un serveur SMTP et d'envoyer des emails directement depuis votre application.

Commencez donc par importer le module 'smtplib' avec l'instruction suivante :

```python
import smtplib
```

Ensuite, créez un objet 'SMTP' pour configurer la connexion à votre serveur SMTP. Cet objet gère l'envoi des emails.

```python
smtpObj = smtplib.SMTP(host, port)
```

* 'host' fait référence au point de terminaison du serveur SMTP, tel que 'live.smtp.mailtrap.io'

* 'port' est le canal de communication utilisé par le serveur. Le port recommandé est généralement 587 pour l'envoi sécurisé d'emails avec le chiffrement TLS.

**Astuce pro** : Un objet SMTP possède un objet d'instance 'sendmail' avec trois paramètres, où chaque paramètre est une chaîne ('receivers' est une liste de chaînes).

```python
smtpObj.sendmail(sender, receivers, message)
```

Si vous souhaitez vous assurer d'avoir correctement importé le module 'smtplib' et vérifier la description complète des arguments et des classes, exécutez la commande suivante :

```python
help(smtplib)
```

## Comment envoyer des emails avec Mailtrap SMTP

Cette méthode implique la configuration des identifiants SMTP personnalisés que vous obtenez pour Mailtrap.

**Notes importantes** :

* **Tester le service avec le domaine factice de Mailtrap** - Pour essayer Mailtrap, vous n'avez pas besoin de vérifier votre domaine tout de suite. Vous pouvez utiliser le domaine factice de Mailtrap (vous y avez accès lorsque vous vous inscrivez), ce qui vous permet de simuler l'envoi d'emails sans vous soucier des enregistrements DNS. Cela est idéal pour tester le service et vous familiariser avec les fonctionnalités de Mailtrap.

* **Vérification du domaine pour la production** - Si vous prévoyez d'envoyer des emails réels à des destinataires, vous devrez vérifier votre domaine. Cela implique d'ajouter des enregistrements DNS tels que SPF, DKIM et [DMARC](https://dmarcreport.com/) aux paramètres DNS de votre fournisseur de domaine. Ces enregistrements garantissent que vos emails sont livrés avec succès et aident à protéger contre le phishing et l'usurpation d'identité. Dans la section suivante, je vous montrerai comment les configurer dans le tableau de bord de votre fournisseur de domaine.

### Vérifiez votre domaine d'envoi (SPF, DKIM et DMARC)

Les enregistrements DNS sont essentiels pour garantir que vos emails sont livrés avec succès, et les fournisseurs de boîtes aux lettres tels que Gmail et Yahoo exigent une authentification DNS.

Mais avant de passer par un tutoriel rapide sur la façon de le faire, passons en revue chaque type d'enregistrement afin que vous compreniez pourquoi ils sont si importants :

* **SPF (Sender Policy Framework)** : L'enregistrement aide les serveurs de messagerie à déterminer si l'adresse IP de l'expéditeur est autorisée à envoyer des emails depuis votre domaine. En termes simples, l'ajout d'un enregistrement SPF empêche les spammeurs d'envoyer des emails qui semblent provenir de votre domaine.

* **DKIM (DomainKeys Identified Mail)** : DKIM utilise le chiffrement pour vérifier le domaine de l'expéditeur et garantit que le contenu de l'email n'a pas été falsifié pendant la transmission. Cela protège vos emails contre l'usurpation d'identité.

* **DMARC (Domain-based Message Authentication, Reporting & Conformance)** : DMARC lie SPF et DKIM ensemble, fournissant une politique pour gérer les emails non authentifiés et rapporter les activités des emails. En résumé, cela vous donne plus de contrôle sur la sécurité des emails de votre domaine.

Maintenant, voici comment ajouter les enregistrements :

1. Tout d'abord, vous devez accéder aux paramètres DNS de votre fournisseur de domaine. Habituellement, vous pouvez y accéder dans l'enregistrement de domaine ou les paramètres de domaine. Par exemple, GoDaddy appelle le menu Gérer DNS, et il est nommé de manière similaire avec d'autres fournisseurs.

2. Ensuite, ajoutez (copiez-collez) les enregistrements DNS fournis par Mailtrap dans les paramètres DNS de votre fournisseur de domaine. Notez que les enregistrements de Mailtrap sont prêts à l'emploi, et SPF est pré-analysé, donc vous n'avez pas besoin de créer quoi que ce soit d'additionnel - il suffit d'ajouter les enregistrements.

![Capture d'écran montrant la vérification du domaine](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfHx2AAc87krxYh7twU5Ypuz-Iu6gklvJeVBzpdgptvfc7B9g7X3BBnqWai8n47HTDJrj1rZ2ny0jfscJJYgAAFcuEsZeVqYO2OellzvQgaXMjnMMxIeOoPGF0ildRbecEi7rjPbg?key=CJmzmKUWxlFjIw3A041wXvaj align="left")

3. Enfin, vous pouvez vérifier l'état de vos enregistrements avec Mailtrap.

Voici le script de base pour envoyer des emails via Mailtrap en utilisant Python. Pour des raisons de sécurité, le script utilise des identifiants de remplissage pour le nom d'utilisateur et le mot de passe (à l'exception du point de terminaison du serveur SMTP et du port).

Lors de l'exécution du script, assurez-vous de remplacer ces remplacements par vos identifiants Mailtrap réels pour garantir l'envoi réussi de l'email.

```python
import smtplib
from email.mime.text import MIMEText

# Configuration
port = 587
smtp_server = "live.smtp.mailtrap.io"
login = "api"  # Votre login généré par Mailtrap
password = "1a2b3c4d5e6f7g"  # Votre mot de passe généré par Mailtrap

sender_email = "mailtrap@example.com"
receiver_email = "new@example.com"

# Contenu en texte brut
text = """\
Bonjour,
Consultez le nouveau post sur le blog de Mailtrap :
Serveur SMTP pour les tests : Basé sur le cloud ou local ?
https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
N'hésitez pas à nous faire savoir quel contenu serait utile pour vous !
"""

# Créer un objet MIMEText
message = MIMEText(text, "plain")
message["Subject"] = "Email en texte brut"
message["From"] = sender_email
message["To"] = receiver_email

# Envoyer l'email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Sécuriser la connexion
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Envoyé')
```

**Dans le script** :

* Les modules 'smtplib' et 'MIMEText' ont été importés depuis la bibliothèque Python.

* Comme mentionné, la configuration du serveur SMTP doit être mise à jour avec vos identifiants. Mais le point de terminaison du serveur et le port sont tels quels.

* Puisque ceci est un script de base, j'ai utilisé 'MIMEText', qui ne contient que du 'texte brut'. Mais le script peut être facilement refactorisé pour utiliser 'MIMEMultipart' pour le 'texte brut' et le 'HTML'. Passez au tutoriel rapide ci-dessous pour voir comment cela se fait.

* Lors de l'envoi de l'email, j'ai choisi d'utiliser l'instruction 'with' (gestionnaire de contexte) pour m'assurer que la connexion au serveur SMTP est fermée immédiatement après l'envoi de l'email.

**Astuce de sécurité** :

Les informations du serveur et les identifiants de connexion ne doivent pas être codés en dur dans votre script d'envoi. Lors de la configuration du script pour la production, assurez-vous d'utiliser des variables d'environnement pour stocker les informations sensibles. Cela rend le code plus sécurisé et plus flexible, en particulier lorsque vous le déplacez entre différentes étapes de développement. Par exemple ⬇️

```python
import os

smtp_server = os.getenv("SMTP_SERVER", "default.smtp.server")
login = os.getenv("SMTP_LOGIN")
password = os.getenv("SMTP_PASSWORD")

# Exemple d'utilisation dans une configuration de connexion SMTP
# smtp.login(login, password)
```

Notez que vous devez définir les variables dans votre système d'exploitation avant d'exécuter le script.

### Refactoriser le script pour utiliser des emails HTML

Les emails HTML offrent une meilleure expérience utilisateur. Ils vous permettent d'inclure du texte formaté, des images, des tableaux, des liens cliquables et des styles personnalisés. Cela fonctionne très bien pour les emails marketing, les newsletters ou toute communication où le design et la marque comptent.

Pour refactoriser le script, vous importeriez 'MIMEMultipart' et 'MIMEText'. Cette action vous permet de personnaliser les emails HTML tout en conservant les versions en texte brut comme solution de repli si vos destinataires ne peuvent pas ouvrir l'email HTML.

Voici le script révisé :

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuration
smtp_server = "live.smtp.mailtrap.io"
port = 587
login = "api"  # Login Mailtrap
password = "1a2b3c4d5e6f7g"  # Mot de passe Mailtrap

sender_email = "mailtrap@example.com"
receiver_email = "new@example.com"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Email HTML"

# Ajouter le contenu en texte brut (optionnel, pour les clients de messagerie qui ne rendent pas le HTML)
message.attach(MIMEText("Ceci est une version en texte brut de l'email.", "plain"))

# Ajouter le contenu HTML
html_content = """\
<html>
  <body>
    <h1>Bienvenue chez Mailtrap !</h1>
    <p>Ceci est un exemple d'email HTML.</p>
  </body>
</html>
"""
message.attach(MIMEText(html_content, "html"))

# Envoyer l'email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Envoyé')
```

Enfin, j'ai inclus des instructions vidéo pour la méthode SMTP - donc si cela fonctionne mieux pour vous, n'hésitez pas à les consulter 📽️.

[Comment envoyer un email en Python en utilisant Mailtrap - Tutoriel par Mailtrap](https://www.youtube.com/watch?v=ufLpTc9up8s&t=1s)

## Comment envoyer des emails avec l'API email de Mailtrap

Si vous cherchez à aller au-delà de l'utilisation de SMTP pour envoyer des emails et souhaitez intégrer l'API email de Mailtrap dans vos applications Python, cette section vous guidera à travers le processus.

L'API email SMTP de Mailtrap vous permet d'envoyer des emails plus efficacement, avec une flexibilité et une évolutivité accrues. Avant de commencer, assurez-vous d'avoir un domaine d'envoi vérifié sur Mailtrap et le jeton API Mailtrap, que vous utiliserez pour authentifier les requêtes.

**Note** : Je couvre l'intégration de l'API en utilisant le SDK Python officiel de Mailtrap.

Installez donc d'abord le SDK officiel avec la commande suivante.

```python
pip install mailtrap
```

**Prérequis** : Assurez-vous que votre version de package Python est 3.6+ ou supérieure.

Après avoir installé le SDK, l'étape suivante consiste à créer un objet Mail. Cet objet représentera l'email que vous souhaitez envoyer, y compris les détails essentiels tels que l'expéditeur, le destinataire, le sujet et le contenu de l'email.

```python
import mailtrap as mt

# Créer l'objet mail
mail = mt.Mail(
    sender=mt.Address(email="mailtrap@example.com", name="Mailtrap Test"),  # Informations de l'expéditeur
    to=[mt.Address(email="your@email.com")],  # Informations du destinataire
    subject="You are awesome!",  # Sujet de l'email
    text="Félicitations pour l'envoi d'un email de test avec Mailtrap !"  # Contenu de l'email (texte brut)
)

# Créer un client en utilisant votre clé API
client = mt.MailtrapClient(token="your-api-key")

# Envoyer l'email
client.send(mail)
```

**Notes rapides** :

* **Expéditeur et destinataire** : Vous devez spécifier l'adresse email de l'expéditeur, qui doit correspondre à votre domaine vérifié. De même, définissez l'email du destinataire.

* **Sujet et contenu texte** : Définissez le sujet et le contenu texte de l'email. Vous pouvez également ajouter du contenu HTML comme je le couvrirai plus tard.

* **Client et envoi** : Le 'MailtrapClient' est initialisé avec votre jeton API Mailtrap, qui authentifie la requête API. La méthode 'send' est ensuite appelée sur le client, en passant l'objet 'mail'.

Pour créer le client en utilisant le jeton API Mailtrap, suivez le chemin suivant dans Mailtrap :
**Paramètres** > **Jetons API** > **Ajouter un jeton**

![Ajouter des jetons API](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeLlNbf0Uiub9YYVxcfiNsZL6_uNHKfuO4dW6ZZGXWEGkF7X4mw82KMsrAWX4hA_u_jYqi1G8aoh1-vOnxKjdXKackVG8HdrsyfHulzaIJVMrMcxmZvllXcNOXVxG7hFOJXgl2VBw?key=CJmzmKUWxlFjIw3A041wXvaj align="left")

Avec cela, vous pouvez utiliser la commande suivante pour envoyer des emails :

```python
# créer le client et envoyer
client = mt.MailtrapClient(token="your-api-key")
client.send(mail)
```

Enfin, voici le script SDK pour envoyer un email 'texte brut' de base via le SDK Python.

```python
from mailtrap import Mail, Address, MailtrapClient

# Créer un objet Mail avec les détails de base pour un email en texte brut
mail = Mail(
    # Spécifier l'adresse email de l'expéditeur et le nom facultatif
    sender=Address(email="mailtrap@example.com", name="Mailtrap Test"),
    # Spécifier un ou plusieurs destinataires ; ici nous utilisons une liste avec un seul destinataire
    to=[Address(email="your@email.com", name="Your Name")],
    # Sujet de l'email
    subject="Email en texte brut simple",
    # Le contenu texte brut de l'email
    text="Ceci est un email en texte brut envoyé en utilisant le SDK Mailtrap. Simple et direct.",
    # Optionnel : catégoriser cet email pour un tri ou une gestion plus facile dans le service Mailtrap
    category="Test",
    # Optionnel : des en-têtes supplémentaires peuvent être spécifiés, mais ne sont pas requis pour les emails en texte brut
    headers={"X-Example-Header": "HeaderValue"}
)

# Initialiser le MailtrapClient avec votre jeton API
client = MailtrapClient(token="your-api-key")

# Envoyer l'email en utilisant la méthode send du client
client.send(mail)

print("Email en texte brut envoyé avec succès.")
```

**Dans le script** :

* Les classes importées incluent 'MailtrapClient', 'Mail' et 'Address' car j'envoie un message en texte brut.

* L'objet 'Mail' contient :

    * Le constructeur 'Mail' pour créer l'objet.

    * 'Sender' qui utilise la classe 'Address' pour définir le nom et l'email de l'expéditeur.

    * 'to' qui est généralement une liste d'objets 'Address', mais puisque ceci est un email en texte brut, il a généralement des destinataires directs au lieu de la liste.

    * 'subject' qui est le sujet de l'email.

    * 'text' qui contient le contenu de l'email (en 'texte brut')

    * 'headers' et 'category' qui sont des champs optionnels qui aident à mieux gérer vos emails.

* Le flux d'envoi d'emails :

    * 'MailtrapClient' est créé et authentifié via le jeton API.

    * La méthode 'send' de 'MailtrapClient' est appelée et passe l'objet 'mail' comme argument d'envoi d'email.

    * Le message "Email en texte brut envoyé avec succès." est imprimé pour confirmer l'action.

### Refactoriser le script pour inclure HTML et des pièces jointes

Encore une fois, il est assez simple de refactoriser le script en utilisant la classe 'MIMEMultipart' pour des structures d'emails plus complexes.

Voici le code refactorisé :

```python
import mailtrap as mt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Créer un message email multipartite
message = MIMEMultipart()
message["Subject"] = "Email HTML"

# Version en texte brut (pour les clients de messagerie qui ne supportent pas le HTML)
message.attach(MIMEText("Ceci est la version en texte brut.", "plain"))

# Version HTML
html_content = """\
<html>
  <body>
    <h1>Bienvenue chez Mailtrap !</h1>
    <p>Ceci est un email HTML avec du texte en <b>gras</b> et un <a href="https://example.com">lien</a>.</p>
  </body>
</html>
"""
message.attach(MIMEText(html_content, "html"))

client = mt.MailtrapClient(token="your-api-key")

# Maintenant, envoyez l'email avec l'API de Mailtrap
mail = mt.Mail(
    sender=mt.Address(email="mailtrap@example.com", name="Mailtrap Test"),
    to=[mt.Address(email="your@email.com")],
    subject="You are awesome!",
    html=message.as_string()  # Passer le contenu HTML sous forme de chaîne
)
client.send(mail)
```

### Configuration environnementale pour la production

Avant de plonger dans les détails, je tiens à vous rappeler les bonnes pratiques de sécurité :

1. **Stocker les clés API et les identifiants en toute sécurité** : En production, ne codez jamais en dur les données sensibles comme les clés API, les identifiants de connexion aux emails ou d'autres secrets directement dans votre code source. Cela expose votre application.

2. **Utiliser des variables d'environnement** : En faisant cela, vous pouvez garder vos identifiants en sécurité et basculer facilement entre différentes configurations (comme dev, staging et production).

Maintenant, voici comment tout configurer :

1. Utilisez le package 'python-dotenv' pour charger les variables d'environnement à partir d'un fichier '.env'. Installez la bibliothèque avec la commande suivante :

    ```python
    pip install python-dotenv
    ```

2. Créez un fichier '.env' à la racine de votre projet pour stocker vos variables d'environnement en toute sécurité. Ce fichier contiendra des informations sensibles, telles que votre clé API Mailtrap, vos identifiants de connexion et les détails de votre serveur SMTP. Voici un exemple :

    ```python
    SMTP_SERVER=smtp.mailtrap.io
    SMTP_PORT=587
    SMTP_LOGIN=your_mailtrap_login
    SMTP_PASSWORD=your_mailtrap_password
    MAILTRAP_API_KEY=your_mailtrap_api_key
    ```

**Note importante** : Assurez-vous que ce fichier '.env' n'est jamais poussé vers le contrôle de version (comme Git). Ajoutez-le à votre '.gitignore' pour éviter une exposition accidentelle.

3. Une fois que vous avez créé votre fichier '.env', vous devez charger les variables dans votre script Python. En haut de votre script, importez le package 'dotenv' et appelez 'load_dotenv()' pour charger les variables d'environnement.

    ```python
    from dotenv import load_dotenv
    import os

    # Charger les variables d'environnement à partir du fichier .env
    load_dotenv()

    # Récupérer les variables d'environnement en toute sécurité
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_login = os.getenv("SMTP_LOGIN")
    smtp_password = os.getenv("SMTP_PASSWORD")
    mailtrap_api_key = os.getenv("MAILTRAP_API_KEY")
    ```

4. Avec les variables d'environnement chargées, vous pouvez remplacer les identifiants codés en dur dans le script par ces variables d'environnement. Voici un exemple :

    ```python
    import smtplib
    from email.mime.text import MIMEText
    from dotenv import load_dotenv
    import os

    # Charger les variables d'environnement
    load_dotenv()

    # Récupérer les identifiants SMTP depuis les variables d'environnement
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_login = os.getenv("SMTP_LOGIN")
    smtp_password = os.getenv("SMTP_PASSWORD")

    sender_email = "mailtrap@example.com"
    receiver_email = "new@example.com"
    subject = "Email en texte brut"
    text = """\
    Bonjour,
    Consultez le nouveau post sur le blog de Mailtrap :
    https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
    """

    # Créer un objet MIMEText
    message = MIMEText(text, "plain")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Envoyer l'email en utilisant les variables d'environnement
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Sécuriser la connexion
        server.login(smtp_login, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email envoyé avec succès !")
    ```

#### Astuces pro :

Tout d'abord, assurez-vous que vos variables d'environnement ne sont accessibles qu'aux utilisateurs autorisés. Sur un serveur de production, cela signifie généralement ne permettre l'accès aux variables d'environnement que par le biais de la configuration de déploiement (par exemple, par le biais des variables de configuration de Heroku, AWS Secrets Manager ou d'autres outils de gestion des secrets basés sur le cloud).

Deuxièmement, utilisez différentes variables d'environnement pour le développement, la mise en scène et la production. Cela garantit que votre environnement de production est isolé et sécurisé par rapport au reste de votre processus de développement.

Une fois vos variables d'environnement configurées localement, déployez votre application dans un environnement de production. Assurez-vous de définir les mêmes variables d'environnement dans votre serveur ou service de production.

Si vous déployez sur des plateformes comme Heroku, AWS ou Google Cloud, vous pouvez utiliser leurs outils de gestion des variables d'environnement pour stocker et accéder à vos secrets en toute sécurité sans avoir à gérer manuellement un fichier '.env'.

## Conclusion

Ce tutoriel rapide fournit plus que suffisamment pour commencer à envoyer des emails en Python. Et notez que les scripts présentés ci-dessus peuvent être étendus pour inclure du HTML, plusieurs destinataires, des pièces jointes, des images, et ainsi de suite.

Si vous êtes intéressé par cela et plus de conseils de sécurité et de bonnes pratiques, vous pouvez consulter le blog de Mailtrap pour des tutoriels plus détaillés.