---
title: Comment envoyer des emails avec Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-17T02:25:12.145Z'
originalURL: https://freecodecamp.org/news/how-to-send-emails-with-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744856526204/09de1f52-e08a-4b4c-a5fe-199aea652e20.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Comment envoyer des emails avec Django
seo_desc: 'If you''re building a Django app and you want to connect with users – maybe
  to welcome them, send password reset links, or deliver updates – email is one of
  the best tools you’ve got.

  Setting up email in Django might sound tricky at first, but it''s pr...'
---

Si vous construisez une application Django et que vous souhaitez communiquer avec les utilisateurs - peut-être pour les accueillir, envoyer des liens de réinitialisation de mot de passe ou livrer des mises à jour - l'email est l'un des meilleurs outils que vous avez.

La configuration de l'email dans Django peut sembler compliquée au premier abord, mais c'est assez simple une fois que vous avez compris.

J'ai guidé beaucoup de gens à travers ce processus, et à la fin de ce guide, vous vous sentirez confiant pour envoyer des emails depuis vos propres projets Django.

## Pourquoi l'email est important dans les applications web

L'email n'est pas juste un plus - il est essentiel pour la communication, la confiance et l'expérience utilisateur.

Réfléchissez-y :

* Comment confirmez-vous le compte de quelqu'un ? Par email.
  
* Comment aidez-vous les utilisateurs à réinitialiser un mot de passe ? Par email.
  
* Vous voulez envoyer des mises à jour, des alertes ou des rapports personnalisés ? Vous l'avez deviné - par email.
  

C'est pourquoi il vaut la peine de le configurer correctement.

## Ce que vous apprendrez dans ce guide

Voici ce que je vais vous expliquer :

* Comment configurer l'email dans Django
  
* Comment choisir entre les paramètres de développement et de production
  
* Comment envoyer des emails basiques
  
* Comment envoyer des emails HTML et multipartites
  
* Comment utiliser des templates pour les emails
  
* Les erreurs courantes à éviter
  

Commençons.

## Comment envoyer des emails avec Django

Voici comment commencer.

### Étape 1 : Configurer vos paramètres d'email dans Django

Django utilise la classe `EmailMessage` et la fonction intégrée `send_mail` pour envoyer des emails. Mais d'abord, vous devez indiquer à Django comment se connecter à votre fournisseur d'email.

Ouvrez votre fichier `settings.py` et ajoutez votre configuration de backend d'email.

Voici un exemple utilisant Gmail :

```python
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre_email@gmail.com'
EMAIL_HOST_PASSWORD = 'votre_mot_de_passe_appli'
```

**Important :** Si vous utilisez Gmail, vous devrez configurer des mots de passe d'application car les mots de passe de compte réguliers ne fonctionnent plus avec SMTP.

#### Pour le développement

Si vous testez simplement des emails localement et ne voulez pas les envoyer réellement, Django facilite cela.

Utilisez ceci dans votre `settings.py` :

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Cela imprime les emails dans votre console au lieu de les envoyer. Parfait pour le débogage !

### Étape 2 : Envoyer un email simple

Maintenant que vos paramètres sont en place, vous pouvez envoyer un email avec seulement quelques lignes de code.

Voici un exemple rapide utilisant la fonction `send_mail` de Django :

```python
# views.py ou là où vous voulez que cette logique réside

from django.core.mail import send_mail

send_mail(
    'Bienvenue sur Mon Site !',
    'Merci de vous être inscrit. Heureux de vous compter parmi nous !',
    'from@example.com',        # De
    ['to@example.com'],        # À
    fail_silently=False,
)
```

Et voilà, vous avez envoyé un email.

### Étape 3 : Envoyer des emails HTML

Le texte brut est bien, mais les emails HTML sont bien meilleurs. Django vous permet d'envoyer des messages multipartites qui incluent à la fois du texte brut et du HTML.

Voici comment faire :

```python


from django.core.mail import EmailMultiAlternatives

subject = 'Bienvenue !'
text_content = 'Merci de nous avoir rejoints.'
html_content = '<p>Merci de <strong>nous avoir rejoints</strong>.</p>'

msg = EmailMultiAlternatives(subject, text_content, 'from@example.com', ['to@example.com'])
msg.attach_alternative(html_content, "text/html")
msg.send()
```

Maintenant, votre email aura l'air professionnel dans les clients email modernes mais fonctionnera toujours si le lecteur d'email de quelqu'un ne supporte que le texte brut.

### Étape 4 : Utiliser des templates pour de meilleurs emails

Si vous envoyez des emails avec une structure similaire - comme un message de bienvenue ou une facture - il est logique d'utiliser des templates.

Créez un fichier comme `welcome_email.html` dans votre dossier de templates :

```xml
<!-- templates/welcome_email.html -->
<h2>Bonjour {{ user.first_name }} !</h2>
<p>Bienvenue sur notre plateforme. Nous sommes heureux que vous soyez ici.</p>
```

Ensuite, chargez et rendez-le dans votre email :

```python
from django.template.loader import render_to_string

html_message = render_to_string('welcome_email.html', {'user': user})
```

Vous pouvez intégrer cela dans la configuration `EmailMultiAlternatives` que nous avons utilisée ci-dessus.

### Étape 5 : Pièges courants et comment les éviter

Voici quelques problèmes que j'ai vus les gens rencontrer :

1. **Mots de passe d'application incorrects** : Si vous utilisez Gmail et que cela échoue constamment, vérifiez à nouveau la configuration de votre mot de passe d'application.
  
2. **Confusion entre port et TLS** : Pour la plupart des fournisseurs SMTP :
  
  * Utilisez le port **587** avec `EMAIL_USE_TLS = True`
      
  * Ou le port **465** avec `EMAIL_USE_SSL = True`
      
3. **Email allant dans les spams** : Utilisez des noms d'expéditeur réels et évitez les lignes d'objet spammy. Envisagez de configurer les enregistrements SPF, DKIM et DMARC si vous passez en production. Voici un guide simple sur l'authentification des emails.
  
## Comment tester les emails sans les envoyer

Vous pouvez utiliser [Mailtrap](https://mailtrap.io/) ou [Papercut SMTP](https://github.com/ChangemakerStudios/Papercut-SMTP) pour tester les emails dans un environnement sandboxé.

Ces outils interceptent les emails dans une fausse boîte de réception, donc rien n'est envoyé aux vrais utilisateurs. Très utile lorsque vous travaillez sur des templates de niveau production ou des emails transactionnels.

## FAQ

### **Puis-je envoyer des pièces jointes avec les emails Django ?**

Oui ! Utilisez `msg.attach()` avec `EmailMessage` ou `EmailMultiAlternatives`. Voici un exemple :

```python
msg.attach('facture.pdf', pdf_content, 'application/pdf')
```

### **Quelle est la différence entre** `send_mail` et `EmailMessage` ?

`send_mail` est un raccourci pour les cas d'utilisation simples. Pour les cas plus complexes - comme les emails HTML, les pièces jointes ou les en-têtes personnalisés - `EmailMessage` ou `EmailMultiAlternatives` est meilleur.

### **Comment envoyer des emails en masse ?**

Utilisez la fonction `send_mass_mail()` ou parcourez une liste et envoyez des emails individuellement. Si vous envoyez de nombreux emails, il est préférable d'utiliser un fournisseur de services d'email (comme SendGrid, Mailgun, etc.) qui supporte la livraison en masse et gère les limites de taux.

## Conclusion

L'email est l'une de ces fonctionnalités qui semble petite jusqu'à ce qu'elle casse - ou jusqu'à ce que vous ayez besoin qu'elle brille.

Est-ce que cela fonctionne pour vous ? Super.

Toujours bloqué ? Ne vous inquiétez pas - c'est l'une de ces choses qui devient plus facile à chaque fois.

### Ressources supplémentaires

Si vous voulez approfondir les emails avec Django, consultez ces liens :

* [Documentation officielle sur les emails Django](https://docs.djangoproject.com/en/stable/topics/email/)
  
* [Guide Django de Mailtrap](https://mailtrap.io/blog/django-send-email/)
  
* [Intégration Django de SendGrid](https://www.twilio.com/docs/sendgrid/for-developers/sending-email/django)
  
* [Package de templates d'email Django](https://github.com/milkpep/django-email-templates)