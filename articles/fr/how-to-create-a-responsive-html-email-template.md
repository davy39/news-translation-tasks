---
title: Comment créer un modèle d'email HTML réactif
subtitle: ''
author: Fanny Nyayic
co_authors: []
series: null
date: '2024-04-15T23:11:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-responsive-html-email-template
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/create-html-email-template-from-scratch.png
tags:
- name: CSS
  slug: css
- name: email
  slug: email
- name: HTML
  slug: html
- name: projects
  slug: projects
seo_title: Comment créer un modèle d'email HTML réactif
seo_desc: "In this beginner-friendly guide, you'll learn how to create a responsive\
  \ email template. You'll follow step-by-step instructions with code snippets to\
  \ design an email template that looks great on any device. \nThis project is perfect\
  \ for newcomers eag..."
---

Dans ce guide pour débutants, vous apprendrez à créer un modèle d'email réactif. Vous suivrez des instructions étape par étape avec des extraits de code pour concevoir un modèle d'email qui a fière allure sur n'importe quel appareil.

Ce projet est parfait pour les nouveaux venus désireux de maîtriser les bases de la conception d'emails !

## Étape 1 : Installer la structure de base

Pour construire un modèle d'email, vous pouvez commencer par une structure HTML de base. Cela inclut une déclaration `DOCTYPE` pour les emails, la définition des sections `head` et `body`, et l'utilisation de balises meta dans la section `head` pour assurer un rendu mobile et un zoom appropriés.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modèle d'email réactif</title>
</head>
<body>
    <!-- Le contenu de l'email va ici -->
</body>
</html>
```

## Étape 2 : Créer la structure de l'email

Utilisez des tableaux pour créer la structure de base de votre email. Cela garantira la compatibilité entre différents clients de messagerie.

```html
<table width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>
        <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" border="0">
                <!-- Le contenu de l'email va ici -->
            </table>
        </td>
    </tr>
</table>

```

## Étape 3 : Ajouter du contenu et des styles en ligne

Les clients de messagerie varient dans la manière dont ils rendent le CSS, il est donc plus sûr d'utiliser des styles en ligne. Voici un exemple de corps d'email simple :

```html
<body style="font-family: 'Poppins', Arial, sans-serif">
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
            <td align="center" style="padding: 20px;">
                <table class="content" width="600" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse; border: 1px solid #cccccc;">
                    <!-- En-tête -->
                    <tr>
                        <td class="header" style="background-color: #345C72; padding: 40px; text-align: center; color: white; font-size: 24px;">
                        Modèle d'email réactif
                        </td>
                    </tr>

                    <!-- Corps -->
                    <tr>
                        <td class="body" style="padding: 40px; text-align: left; font-size: 16px; line-height: 1.6;">
                        Bonjour à tous ! <br>
                        Lorem odio soluta quae dolores sapiente voluptatibus recusandae aliquam fugit ipsam.
                        <br><br>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam corporis sint eum nemo animi velit exercitationem impedit. Incidunt, officia facilis  atque? Ipsam voluptas fugiat distinctio blanditiis veritatis.            
                        </td>
                    </tr>

                    <!-- Bouton d'appel à l'action -->
                    <tr>
                        <td style="padding: 0px 40px 0px 40px; text-align: center;">
                            <!-- Bouton CTA -->
                            <table cellspacing="0" cellpadding="0" style="margin: auto;">
                                <tr>
                                    <td align="center" style="background-color: #345C72; padding: 10px 20px; border-radius: 5px;">
                                        <a href="https://www.yourwebsite.com" target="_blank" style="color: #ffffff; text-decoration: none; font-weight: bold;">Réserver une consultation gratuite</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td class="body" style="padding: 40px; text-align: left; font-size: 16px; line-height: 1.6;">
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam corporis sint eum nemo animi velit exercitationem impedit.             
                        </td>
                    </tr>
                    <!-- Pied de page -->
                    <tr>
                        <td class="footer" style="background-color: #333333; padding: 40px; text-align: center; color: white; font-size: 14px;">
                        Copyright &copy; 2024 | Nom de votre marque
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
```

Voici une ventilation des principaux éléments et de leurs fonctions :

### Balise Body et configuration de la police

```html
<body style="font-family: 'Poppins', Arial, sans-serif">
```

Cela définit la police par défaut pour l'email comme 'Poppins', avec des retours à Arial et sans-serif si 'Poppins' n'est pas disponible.

### Structure du tableau

```html
<table width="100%" border="0" cellspacing="0" cellpadding="0">
```

Il s'agit du tableau le plus externe qui occupe 100 % de la largeur de l'email. Le `border`, `cellspacing` et `cellpadding` sont définis à 0 pour supprimer le style et l'espacement par défaut.

À l'intérieur de ce tableau se trouve un autre `<table class="content">` avec une largeur fixe de 600 px, centré par son parent avec `td align="center"`.

Ce tableau intérieur inclut une bordure et un style spécifique, le définissant comme la zone de contenu principale.

### La section d'en-tête

L'en-tête est stylisé avec un fond bleu foncé utilisant le CSS en ligne (#345C72), une couleur de texte blanche et une taille de texte plus grande (24px). Il est conçu pour attirer l'attention dès le début de l'email.

**Remarque** : Vous pouvez personnaliser cette section avec le nom ou le logo de votre marque.

### Le contenu du corps

La section du corps contient le message principal de l'email, avec une taille de police de 16px et une hauteur de ligne de 1,6 pour une meilleure lisibilité. Le contenu est aligné à gauche, et l'utilisation des balises `<br>` aide à espacer les lignes.

### Bouton d'appel à l'action (CTA)

```html
<!-- Bouton d'appel à l'action -->
                    <tr>
                        <td style="padding: 0px 40px 0px 40px; text-align: center;">
                            <!-- Bouton CTA -->
                            <table cellspacing="0" cellpadding="0" style="margin: auto;">
                                <tr>
                                    <td align="center" style="background-color: #345C72; padding: 10px 20px; border-radius: 5px;">
                                        <a href="https://www.yourwebsite.com" target="_blank" style="color: #ffffff; text-decoration: none; font-weight: bold;">Réserver une consultation gratuite</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
```

Le bouton CTA est conçu pour se démarquer avec une couleur de fond qui correspond à l'en-tête, des coins arrondis (`border-radius: 5px`), et un texte blanc en gras.

La balise `<a>` à l'intérieur du bouton est stylisée pour supprimer le soulignement par défaut (`text-decoration: none`) et est liée à une page web où les destinataires peuvent "Réserver une consultation gratuite".

### Pied de page

Le pied de page reprend l'approche de style de l'en-tête mais utilise un fond plus sombre (#333333) et une taille de police plus petite (14px). Il peut contenir des informations de copyright et des liens ou d'autres détails de contact.

### Illustration

![Image](https://www.freecodecamp.org/news/content/images/2024/04/email-template-illustration.png)
_illustration des différentes parties du modèle : en-tête, bouton CTA et pied de page_

## Étape 4 : Le rendre réactif

Pour garantir que l'email ait une belle apparence sur les appareils mobiles, vous pouvez utiliser des requêtes média CSS. Bien que la plupart des styles soient en ligne, pour un comportement réactif, vous devrez ajouter un bloc `<style>` dans le `head`.

Les requêtes média ajustent les styles en fonction de la largeur de l'appareil.

```css
<style>
  @media screen and (max-width: 600px) {
    .content {
        width: 100% !important;
        display: block !important;
        padding: 10px !important;
    }
    .header, .body, .footer {
        padding: 20px !important;
    }
  }
</style>
```

Voici une ventilation de cet extrait CSS spécifique :

```css
@media screen and (max-width: 600px) { ... }
```

Cette requête média cible les écrans avec une largeur maximale de 600 pixels. Elle applique les styles suivants uniquement lorsque l'email est consulté sur des appareils avec une largeur d'écran de 600px ou moins, ce qui inclut généralement les smartphones et certaines tablettes plus petites.

Styles au sein des classes de requête média :

### .content

*  `width: 100% !important;` : Ce style change la largeur du tableau `.content` pour utiliser toute la largeur de l'écran au lieu des 600px spécifiés dans le HTML. La règle `!important` est utilisée pour remplacer tout autre style conflictuel.
* `display: block !important;` : Bien que les éléments `<table>` soient naturellement des éléments de niveau bloc, définir `display: block` explicitement peut aider dans certains clients de messagerie pour s'assurer que l'élément se comporte comme prévu.
* `padding: 10px !important;` : Ajoute un remplissage autour du contenu dans le tableau `.content`, le réduisant de 40px d'origine dans le HTML pour mieux utiliser l'espace d'écran réduit sur les appareils plus petits.

### .header, .body, .footer

* `padding: 20px !important;` : Ce style définit uniformément le remplissage des sections _header, body et footer_ à _20px_ sur tous les côtés, optimisant l'espacement pour les petits écrans. Il remplace les différents paramètres de remplissage définis dans le HTML, qui incluent des valeurs plus grandes dans certains cas.

Dans le contexte de la conception d'emails, l'utilisation de **!important** est assez courante pour s'assurer que les styles sont appliqués comme prévu, remplaçant à la fois les styles par défaut et d'autres styles potentiellement conflictuels qui pourraient être appliqués par le client de messagerie lui-même.

## Étape 5 : Tester sur différents clients de messagerie

Il est crucial de tester votre modèle d'email sur différents clients de messagerie (comme Gmail, Outlook et Apple Mail) et appareils pour assurer la compatibilité et la réactivité. Des outils comme Litmus ou Email on Acid peuvent aider avec cela.

## Étape 6 : Ajouter une police Google

Incorporer des polices Google dans un modèle d'email HTML peut améliorer considérablement son attrait visuel.

Cependant, il est important de noter que tous les clients de messagerie ne supportent pas les polices web. Certains, comme Apple Mail, supportent les polices Google, mais d'autres comme Gmail ne le font pas. Pour vous assurer que votre email a fière allure pour tous les destinataires, fournissez toujours une police de repli.

Voici comment vous pouvez ajouter une police Google à votre modèle d'email, ainsi qu'une option de repli pour les clients qui ne la supportent pas :

### Choisissez votre police Google

Tout d'abord, visitez le site [Google Fonts](https://fonts.google.com/) et choisissez une police. Pour cet exemple, utilisons _"Poppins"_.

### Ajoutez le lien de la police à l'en-tête de votre email

Incluez le lien vers la police Google dans la section `<head>` de votre document HTML. Comme cela peut ne pas être supporté dans tous les clients de messagerie, assurez-vous d'avoir une police de repli appropriée dans vos styles.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
```

### Appliquez la police dans vos styles

Utilisez le CSS en ligne pour appliquer la police Google à vos éléments HTML, et incluez toujours une police de repli générique. Dans les modèles d'email, il est plus sûr d'appliquer les styles en ligne en raison du support variable des balises `<style>` entre les clients de messagerie.

Voici comment appliquer la police au `body` de votre email et inclure une police de repli :

```html
<body style="font-family: 'Poppins', Arial, sans-serif;">
    <table width="100%" cellspacing="0" cellpadding="0">
        <!-- Contenu de l'email -->
    </table>
</body>
```

## Ce que nous avons créé

Ci-dessous se trouve une capture d'écran du modèle d'email que nous avons conçu. Il présente une mise en page professionnelle avec un en-tête contenant un espace réservé pour un logo, une section principale pour votre message, et un pied de page sombre avec des liens de contact et de gestion d'abonnement.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/email-template.png)
_capture d'écran du modèle d'email_

## Conseils supplémentaires :

* Gardez votre CSS en ligne autant que possible, car de nombreux clients de messagerie ne supportent pas les balises `<style>`.
* Utilisez des polices web-sécurisées pour vous assurer que votre texte apparaît correctement dans tous les clients de messagerie.
* Fournissez toujours une version en texte brut de votre email pour les clients qui ne supportent pas le HTML, ou qui ont le HTML désactivé.

J'espère que ce guide vous fournit un cadre de base pour créer un modèle d'email réactif. À mesure que vous devenez plus à l'aise avec la conception d'emails, vous pouvez expérimenter avec des mises en page et des styles plus complexes.

**Bon codage !**