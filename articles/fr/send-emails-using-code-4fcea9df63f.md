---
title: Envoyer des Emails en Utilisant Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-07T16:14:20.000Z'
originalURL: https://freecodecamp.org/news/send-emails-using-code-4fcea9df63f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qTKddOEkMZiri9ldfzBauQ.jpeg
tags:
- name: marketing
  slug: marketing
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Envoyer des Emails en Utilisant Python
seo_desc: 'By Arjun Krishna Babu

  As a learning exercise, I recently dug into Python 3 to see how I could fire off
  a bunch of emails. There may be more straightforward methods of doing this in a
  production environment, but the following worked well for me.

  So, h...'
---

Par Arjun Krishna Babu

En tant qu'exercice d'apprentissage, j'ai récemment exploré Python 3 pour voir comment je pouvais envoyer un ensemble d'emails. Il peut y avoir des méthodes plus directes pour faire cela dans un environnement de production, mais ce qui suit a bien fonctionné pour moi.

Voici un scénario : Vous avez les noms et les adresses email d'un ensemble de contacts. Et vous souhaitez envoyer un message à chacun de ces contacts, tout en ajoutant un _"Cher [nom]"_ en haut du message.

Pour simplifier, vous pouvez stocker les détails des contacts dans un fichier plutôt que dans une base de données. Vous pouvez également stocker le modèle du message que vous souhaitez envoyer dans un fichier.

Le module [smtplib](https://docs.python.org/3/library/smtplib.html) de Python est essentiellement tout ce dont vous avez besoin pour envoyer des emails simples, sans ligne d'objet ou autres informations supplémentaires. Mais pour des emails _réels_, vous avez besoin d'une ligne d'objet et de nombreuses informations — peut-être même des images et des pièces jointes.

C'est là qu'intervient le package [email](https://docs.python.org/3/library/email.html) de Python. Gardez à l'esprit qu'il n'est pas possible d'envoyer un message email en utilisant uniquement le package `email`. Vous avez besoin d'une combinaison de `email` et `smtplib`.

Assurez-vous de consulter la documentation officielle complète pour ces deux packages.

Voici quatre étapes de base pour envoyer des emails en utilisant Python :

1. Configurer le serveur SMTP et se connecter à votre compte.
2. Créer l'objet de message `MIMEMultipart` et le charger avec les en-têtes appropriés pour les champs `From`, `To` et `Subject`.
3. Ajouter le corps de votre message.
4. Envoyer le message en utilisant l'objet serveur SMTP.

Maintenant, laissez-moi vous guider à travers tout le processus.

Supposons que vous avez un fichier de contacts `mycontacts.txt` comme suit :

```bash
user@computer ~ $ cat mycontacts.txt
john johndoe@example.com
katie katie2016@example.com
```

Chaque ligne représente un seul contact. Nous avons le nom suivi de l'adresse email. Je stocke tout en minuscules. Je laisse à la logique de programmation le soin de convertir les champs en majuscules ou en cas de phrase si nécessaire. Tout cela est assez facile en Python.

Ensuite, nous avons le fichier de modèle de message `message.txt`.

```bash
user@computer ~ $ cat message.txt 

Cher ${PERSON_NAME}, 

Ceci est un message de test. 
Passez un excellent week-end ! 

Cordialement
```

Remarquez le mot "`${PERSON_NAME}`" ? C'est une [chaîne de modèle](https://docs.python.org/3.5/library/string.html#template-strings) en Python. Les chaînes de modèle peuvent facilement être remplacées par d'autres chaînes ; dans cet exemple, `${PERSON_NAME}` va être remplacé par le nom réel de la personne, comme vous le verrez bientôt.

Maintenant, commençons avec le code Python. Tout d'abord, nous devons lire les contacts depuis le fichier `mycontacts.txt`. Nous pourrions tout aussi bien généraliser cette partie dans sa propre fonction.

```py
# Fonction pour lire les contacts depuis un fichier de contacts donné et retourner une
# liste de noms et d'adresses email
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails
```

La fonction `get_contacts()` prend un nom de fichier comme argument. Elle ouvrira le fichier, lira chaque ligne (c'est-à-dire chaque contact), le divisera en nom et email, puis les ajoutera à deux listes séparées. Enfin, les deux listes sont retournées par la fonction.

Nous avons également besoin d'une fonction pour lire un fichier de modèle (comme `message.txt`) et retourner un objet `Template` créé à partir de son contenu.

```py
from string import Template

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
```

Tout comme la fonction précédente, celle-ci prend un nom de fichier comme argument.

Pour envoyer l'email, vous devez utiliser [SMTP (Simple Mail Transfer Protocol)](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol). Comme mentionné précédemment, Python fournit des bibliothèques pour gérer cette tâche.

```py
# importer le module smtplib. Il devrait être inclus dans Python par défaut
import smtplib
# configurer le serveur SMTP
s = smtplib.SMTP(host='votre_adresse_hote_ici', port=votre_port_ici)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
```

Dans l'extrait de code ci-dessus, vous importez `smtplib` puis créez une [instance SMTP](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP) qui encapsule une connexion SMTP. Elle prend comme paramètres l'adresse hôte et un numéro de port, tous deux dépendant entièrement des paramètres SMPT de votre fournisseur de services email particulier. Par exemple, dans le cas d'Outlook, la ligne 4 ci-dessus serait plutôt :

```py
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
```

Vous devez utiliser l'adresse hôte et le numéro de port de votre fournisseur de services email particulier pour que tout fonctionne.

`MY_ADDRESS` et `PASSWORD` ci-dessus sont deux variables qui contiennent l'adresse email complète et le mot de passe du compte que vous allez utiliser.

Ce serait un bon moment pour récupérer les informations de contact et les modèles de message en utilisant les fonctions que nous avons définies ci-dessus.

```py
names, emails = get_contacts('mycontacts.txt')  # lire les contacts
message_template = read_template('message.txt')
```

Maintenant, pour chacun de ces contacts, envoyons le mail séparément.

```py
# importer les packages nécessaires
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Pour chaque contact, envoyer l'email :
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # créer un message

    # ajouter le nom réel de la personne au modèle de message
    message = message_template.substitute(PERSON_NAME=name.title())

    # configurer les paramètres du message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="Ceci est un TEST"

    # ajouter le corps du message
    msg.attach(MIMEText(message, 'plain'))

    # envoyer le message via le serveur configuré précédemment.
    s.send_message(msg)
    
    del msg
```

Pour chaque `name` et `email` (du fichier de contacts), vous créez un objet [MIMEMultipart](https://docs.python.org/3/library/email.mime.html#email.mime.multipart.MIMEMultipart), configurez les en-têtes de type de contenu `From`, `To`, `Subject` en tant que dictionnaire de mots-clés, puis attachez le corps du message à l'objet `MIMEMultipart` en tant que texte brut. Vous pourriez vouloir lire la documentation pour découvrir d'autres types MIME avec lesquels vous pouvez expérimenter.

Remarquez également qu'à la ligne 10 ci-dessus, je remplace `${PERSON_NAME}` par le nom réel extrait du fichier de contacts en utilisant le [mécanisme de modélisation en Python](https://docs.python.org/3.5/library/string.html#template-strings).

Dans cet exemple particulier, je supprime l'objet `MIMEMultipart` et le recrée chaque fois que vous itérez à travers la boucle.

Une fois cela fait, vous pouvez envoyer le message en utilisant la fonction pratique [send_message()](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.send_message) de l'objet SMTP que vous avez créé précédemment.

Voici le code complet :

```py
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'mon_adresse@example.comm'
PASSWORD = 'monmotdepasse'

def get_contacts(filename):
    """
    Retourne deux listes names, emails contenant les noms et les adresses email
    lus depuis un fichier spécifié par filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Retourne un objet Template comprenant le contenu du
    fichier spécifié par filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt') # lire les contacts
    message_template = read_template('message.txt')

    # configurer le serveur SMTP
    s = smtplib.SMTP(host='votre_adresse_hote_ici', port=votre_port_ici)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # Pour chaque contact, envoyer l'email :
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # créer un message

        # ajouter le nom réel de la personne au modèle de message
        message = message_template.substitute(PERSON_NAME=name.title())

        # Affiche le corps du message pour notre référence
        print(message)

        # configurer les paramètres du message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Ceci est un TEST"
        
        # ajouter le corps du message
        msg.attach(MIMEText(message, 'plain'))
        
        # envoyer le message via le serveur configuré précédemment.
        s.send_message(msg)
        del msg
        
    # Terminer la session SMTP et fermer la connexion
    s.quit()
    
if __name__ == '__main__':
    main()
```

Voilà ! Je crois que le code est maintenant assez clair.

N'hésitez pas à le copier et à le modifier selon vos besoins.

En plus de la documentation officielle de Python, je voudrais également mentionner [cette ressource](http://naelshiab.com/tutorial-send-email-python/) qui m'a beaucoup aidé.

Bon codage :)

_J'ai initialement publié cet article [ici](https://arjunkrishnababu96.gitlab.io/post/send-emails-using-code/). Si vous avez aimé cet article, n'hésitez pas à cliquer sur le petit cœur ci-dessous. Merci !_