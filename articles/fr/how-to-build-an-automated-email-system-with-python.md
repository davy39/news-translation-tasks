---
title: Automatisation avec Python – Comment créer un système d'emails automatisé pour
  les candidatures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-12-11T18:39:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-automated-email-system-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/automate-email-with-python.png
tags:
- name: automation
  slug: automation
- name: Python
  slug: python
seo_title: Automatisation avec Python – Comment créer un système d'emails automatisé
  pour les candidatures
seo_desc: "By Jess Wilk\nWe all receive promotional emails from companies like Swiggy\
  \ and Amazon encouraging us to check out their new dish or flash sales. \nHave you\
  \ ever wondered how they manage to send emails to millions of customers? It’s impossible\
  \ to do it ..."
---

Par Jess Wilk

Nous recevons tous des emails promotionnels de la part d'entreprises comme Swiggy et Amazon qui nous encouragent à découvrir leur nouveau plat ou leurs ventes flash. 

Vous êtes-vous déjà demandé comment elles parviennent à envoyer des emails à des millions de clients ? Il est impossible de le faire manuellement ! Au lieu de cela, elles utilisent des systèmes d'emails automatisés pour gérer et planifier leurs emails de manière efficace. 

Le meilleur dans tout cela, c'est que vous pouvez le construire rapidement avec des packages Python open-source. Supposons que vous êtes un étudiant ou un professionnel en activité à la recherche d'un nouvel emploi. Envoyer manuellement votre CV et votre lettre de motivation à plusieurs recruteurs peut être chronophage et souvent sujet à des erreurs. 

Dans cet article, je vais montrer comment automatiser l'envoi de candidatures en utilisant la bibliothèque Python étape par étape avec du code. 

## Prérequis

Avant de plonger dans le processus d'automatisation des systèmes d'emails avec Python, assurez-vous d'avoir une connaissance de base des concepts généraux de Python. 

Si vous êtes nouveau dans Python, vous pouvez consulter le cours [Introduction à Python](https://hyperskill.org/tracks/6) sur Hyperskill, où je contribue en tant qu'expert.

## Étape 1 : Configurer la connexion à votre serveur d'emails

Smtplib est un package Python intégré. Il est gratuit et permet d'envoyer des emails via n'importe quel service comme Gmail, Yahoo, etc. J'utiliserai Gmail dans cet exemple. 

Le numéro de port dépend du serveur que vous choisissez. Nous pouvons démarrer la connexion en utilisant la classe `smtplib.SMTP` du package, avec le serveur et le port comme paramètres d'entrée. SMTP signifie Simple Mail Transfer Protocol.

```python

    import smtplib 
   
    my_email='jess_xxx@gmail.com'
    password_key='xxxxx'
    
    # Serveur SMTP et numéro de port pour GMAIL.com
    gmail_server= "smtp.gmail.com"
    gmail_port= 587


    # Démarrage de la connexion
    my_server = smtplib.SMTP(gmail_server, gmail_port)
    my_server.ehlo()
    my_server.starttls()
      
    # Connexion avec votre email et mot de passe
    my_server.login(my_email, password_key)

```

Ensuite, pour identifier le client auprès du serveur, nous appelons la méthode `ehlo()` ou extended hello. Il est également crucial de s'assurer que votre connexion est sécurisée et qu'il n'y a pas de fuite d'informations. 

Nous pouvons activer le chiffrement pour la connexion en utilisant le **Transport Layer Security** (TLS) en appelant la méthode `starttls()`. Après cela, vous pouvez utiliser la méthode login() avec vos identifiants d'email et de mot de passe.

## Étape 2 : Ajouter différents types de contenu en utilisant MIME

Votre connexion est prête ! Mais avant de voir comment envoyer des emails à une liste de personnes, il est crucial de comprendre comment joindre différents types de contenu à votre email.  
  
Vous pouvez envoyer votre email directement à votre serveur SMTP si votre email est un message texte. Mais que faire si vous souhaitez ajouter un lien vers votre profil LinkedIn ou un PDF de votre relevé de notes ou de votre CV ?  

Voici MIMEMultipart. MIME signifie **Multipurpose Internet Mail Extensions**. Il est également appelé Multipart, qui prend en charge le texte brut et les langues HTML. L'utilisation de HTML pour ajouter votre contenu offre une flexibilité dans la mise en forme et la jointure d'images.  
  
Le module `MIMEMultipart` fournit une classe pour créer des documents MIME représentant un message multipartite. Il peut inclure du texte, des images et des pièces jointes.  
  
Créons un objet `MIMEMultipart` nommé _message_, comme montré ci-dessous. Nous utilisons le sous-type alternatif, qui inclut le texte brut et les versions HTML du message.

```python
from email.mime.multipart import MIMEMultipart
message = MIMEMultipart("alternative")
```

### Comment ajouter du contenu texte :

Le module `MIMEText` fournit une classe pour créer des documents MIME représentant du texte brut dans un message email.

```python
from email.mime.text import MIMEText


text_content= "Bonjour, je suis un étudiant en dernière année avec un diplôme de Mtech en informatique spécialisé en intelligence artificielle. Je m'intéresse aux rôles de data science au sein de votre organisation."


message.attach(MIMEText(text_content))

```

### Comment ajouter des images à votre email :

Le module `MIMEImage` fournit une classe pour créer des documents MIME représentant des données d'image dans un message email.   
  
Importez le module `MIMEImage` et définissez le chemin qui contient votre fichier image. Ici, nous lisons ses données binaires et les joignons à l'objet message en tant que partie MIMEImage.

```python
from email.mime.image import MIMEImage
import os


# définissez votre emplacement
grade_card_path = 'path/to/your/grade_card.jpg'


# Lire l'image depuis l'emplacement
grade_card_img = open(grade_card_path, 'rb').read()


# Joindre votre image
message.attach(MIMEImage(grade_card_img, name=os.path.basename(grade_card_path)))

```

### Comment joindre des fichiers à votre email :

Le module `MIMEApplication` fournit une classe pour créer des documents MIME représentant des données binaires arbitraires dans un message email. Il est souvent utilisé pour joindre des fichiers.  
  
Tout d'abord, définissez le chemin vers un fichier joint (_resume_file_), lisez ses données binaires et joignez-le à l'objet message en tant que partie MIMEApplication. Il définit également l'en-tête Content-Disposition pour spécifier le nom du fichier.

```python
resume_file = '...../resume.txt'


# Lire le fichier depuis l'emplacement
with open(resume_file, 'rb') as f:
    file = MIMEApplication(
        f.read(),
        name=os.path.basename(resume_file)
    )
    file['Content-Disposition'] = f'attachment; 


    filename="{os.path.basename(resume_file)}"'
    message.attach(file)

```

Lorsque vous joignez des fichiers, remplacez les chemins d'accès par les chemins réels. Vous pouvez également joindre une liste de fichiers en utilisant cette fonction.

## Étape 3 : Envoyer plusieurs emails personnalisés

J'espère que vous êtes familiarisé avec la manière d'ajouter différents types de contenu à votre email. Préparez-vous et commençons notre projet : automatiser les emails personnalisés pour les recruteurs.   
  
Lors de la création d'un système d'automatisation, il est essentiel de le personnaliser selon des besoins spécifiques. Par exemple, si vous êtes un recruteur, vous préféreriez un email adapté à votre entreprise et à vous plutôt qu'un email qui vous adresse simplement comme 'Monsieur/Madame'. 

Pour y parvenir, vous créerez des champs personnalisés dans votre message texte qui reçoivent des paramètres d'entrée.  
  
Créez un fichier CSV avec les informations que vous souhaitez personnaliser dans différentes colonnes. Par exemple, j'ai créé un CSV avec le Nom du recruteur, l'Email du recruteur, le Nom de l'organisation et le Rôle du poste.

Enregistrez le fichier CSV sous _job_contacts.csv_. Assurez-vous qu'une virgule sépare les valeurs et qu'il n'y a pas d'espaces blancs pour éviter les problèmes de formatage. Concevez un message texte en ajoutant du contenu personnalisé en utilisant la fonction **str.format()**. Vous pouvez utiliser des espaces réservés entre accolades pour les parties que vous souhaitez personnaliser.

Voici mon exemple :

> text_content= """  
> Bonjour **{recruiter_name}**, j'espère que vous allez bien. Je suis Jane Doe, une diplômée en ingénierie avec un Mtech en informatique et une spécialisation en intelligence artificielle.   
>   
> Je vous écris pour me renseigner sur les postes ouverts en **{job_role}** chez **{organization}**. J'ai de l'expérience dans l'analyse et la modélisation de données grâce à mes stages et projets de recherche. Je suis enthousiaste à l'idée d'avoir l'opportunité d'appliquer mes compétences et d'en apprendre davantage dans le **{organization_sector}**.   
>   
> J'ai joint mon relevé de notes et mon CV ci-dessous. J'attends avec impatience de recevoir de vos nouvelles.  
>   
> Merci,  
> ... """

Voici la partie finale. Nous lisons le fichier CSV et parcourons chaque ligne, comme montré dans l'extrait ci-dessous. De nouveaux détails sur le poste sont lus et remplacés à chaque étape dans le message, et un email est envoyé au recruteur.

```python
import csv


with open("job_contacts.csv") as csv_file:
        jobs = csv.reader(csv_file)
        next(jobs)  # Sauter la ligne d'en-tête
        
        for recruiter_name, recruiter_email, organization, 
        organization_sector, job_role in jobs:
            
            email_text=text_content.format(recruiter_name=recruiter_name, recruiter_email=recruiter_email,
            organization=organization, organization_sector=organization_sector, job_role=job_role)
            
            # Joindre le texte personnalisé à notre message
            message.attach(MIMEText(email_text, 'plain'))
            
            my_server.sendmail(
                from_addr=my_email,
                to_addrs=recruiter_email,
                msg=message.as_string()
            )




my_server.quit()

```

Enfin, nous utilisons la fonction `sendmail()` de SMTP avec les adresses email de l'expéditeur et du destinataire et les messages comme entrée. N'oubliez pas de quitter le serveur une fois le processus terminé.

## Conseils et bonnes pratiques

J'espère que vous avez apprécié le projet. Vous pouvez utiliser ce modèle pour créer un système d'emails automatisé pour divers objectifs comme des campagnes marketing, la promotion de votre newsletter, et plus encore. 

Voici quelques recommandations à retenir :

* Vous ne devriez pas stocker votre mot de passe d'email dans le code. Au lieu de cela, demandez-le via une entrée ou stockez-le comme une variable d'environnement.
* Vous pouvez créer une connexion SMTP sécurisée avec SSL (Secure Sockets Layer). C'est une alternative au TLS que nous avons utilisé pour fournir un chiffrement sur une connexion non sécurisée.
* Vous pouvez créer plusieurs messages email personnalisés pour différents secteurs d'activité et utiliser le plus adapté en utilisant une correspondance switch-case.

Merci d'avoir lu ! Je suis Jess, et je suis une experte chez Hyperskill. Vous pouvez consulter un cours **[Introduction à Python](https://hyperskill.org/tracks/6)** sur la plateforme.