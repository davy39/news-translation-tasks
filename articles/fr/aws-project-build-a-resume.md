---
title: Comment créer un CV en ligne sur AWS en utilisant S3, Route 53, CloudFront
  et ACM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-08T00:38:02.000Z'
originalURL: https://freecodecamp.org/news/aws-project-build-a-resume
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/thumbnail-final-1.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Job Hunting
  slug: job-hunting
- name: projects
  slug: projects
- name: Web Development
  slug: web-development
seo_title: Comment créer un CV en ligne sur AWS en utilisant S3, Route 53, CloudFront
  et ACM
seo_desc: "By Amber Israelsen\nIf you're new to AWS, you can probably appreciate the\
  \ sense of overwhelm that comes from trying to understand all the different services\
  \ (seriously, like, hundreds of them). What are they all for, and how do they work\
  \ together? \nAn..."
---

Par Amber Israelsen

Si vous êtes nouveau sur AWS, vous pouvez probablement apprécier le sentiment de surcharge qui vient de la tentative de comprendre tous les différents services (sérieusement, comme, des centaines d'entre eux). À quoi servent-ils tous, et comment fonctionnent-ils ensemble ?

Et une fois que vous avez maîtrisé quelques compétences de base, le prochain défi est de démontrer ces compétences à un employeur potentiel. Quel type de projet pouvez-vous mettre en avant sur votre CV, sans vous ruiner ?

Dans ce tutoriel pratique, vous obtiendrez de l'aide pour ces deux choses en construisant votre CV réel sur AWS, en suivant ces étapes :

* Écrire le code de votre CV en utilisant HTML, CSS et JavaScript
* Télécharger vos fichiers dans un bucket Simple Storage Service (S3) que vous configurez pour l'hébergement de sites web statiques, avec un accès public
* Utiliser Route 53 pour configurer un domaine personnalisé pour votre CV
* Configurer un certificat TLS/SSL avec AWS Certificate Manager (ACM)
* Créer une distribution CloudFront (qui pointe vers les fichiers dans S3) où vous pouvez appliquer le certificat.

Voici ce que nous allons construire :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Completed-resume-with-callouts-1-2.png)
_Exemple de CV sur AWS, utilisant S3, CloudFront, Certificate Manager et Route 53_

À la fin de ce tutoriel, vous aurez plus qu'un simple CV en ligne. Vous aurez un projet concret que vous pourrez utiliser pour impressionner vos amis, votre famille, votre réseau et vos employeurs potentiels.

Pour une démonstration en direct du projet, consultez cette vidéo :

%[https://youtu.be/NiCZSdWucZE]

## Table des matières

* [Ce dont vous avez besoin pour suivre](#heading-ce-dont-vous-avez-besoin-pour-suivre)
* [Mais d'abord, combien cela coûtera-t-il ?](#heading-mais-dabord-combien-cela-coutera-t-il)
* [Créer le code (HTML, CSS, JavaScript) pour votre CV](#heading-creer-le-code-html-css-javascript-pour-votre-cv)
* [Créer un bucket S3 et le configurer pour l'hébergement de sites web statiques et l'accès public](#heading-creer-un-bucket-s3-et-le-configurer-pour-lhebergement-de-sites-web-statiques-et-lacces-public)
* [Option de nom de domaine 1 : Enregistrer un nouveau nom de domaine avec Route 53](#heading-option-de-nom-de-domaine-1-enregistrer-un-nouveau-nom-de-domaine-avec-route-53)
* [Option de nom de domaine 2 : Utiliser un nom de domaine d'un fournisseur tiers](#heading-option-de-nom-de-domaine-2-utiliser-un-nom-de-domaine-dun-fournisseur-tiers)
* [Créer un enregistrement A avec un alias pour pointer vers le site web S3](#heading-creer-un-enregistrement-a-avec-un-alias-pour-pointer-vers-le-site-web-s3)
* [Créer un certificat TLS/SSL public en utilisant AWS Certificate Manager](#heading-creer-un-certificat-tlsssl-public-en-utilisant-aws-certificate-manager)
* [Créer une distribution CloudFront](#heading-creer-une-distribution-cloudfront)
* [Mettre à jour Route 53 pour pointer vers la distribution CloudFront](#heading-mettre-a-jour-route-53-pour-pointer-vers-la-distribution-cloudfront)
* [Admirez le résultat final](#heading-admirez-le-resultat-final)
* [IMPORTANT ! Supprimez vos ressources](#heading-important-supprimez-vos-ressources)
* [Conclusion](#heading-conclusion)

## Ce dont vous avez besoin pour suivre

Pour compléter ce tutoriel avec succès, vous aurez besoin des éléments suivants :

* **Un compte AWS** : Vous pouvez [en créer un gratuitement](https://portal.aws.amazon.com/billing/signup) (bien qu'il nécessite une carte de crédit pour la validation).
* **Expérience de base** : Avoir une certaine expérience de base avec AWS rendra le tutoriel plus facile, mais vous devriez toujours pouvoir suivre même si vous êtes un débutant complet.
* **Permissions appropriées** : Je suggère de vous connecter en tant qu'utilisateur IAM avec des privilèges d'administrateur, ou d'utiliser votre compte root (bien que je sois obligé de dire que travailler dans votre compte root au quotidien n'est pas recommandé/n'est pas une meilleure pratique).

## Mais d'abord, combien cela coûtera-t-il ?

Avant d'aller trop loin, décomposons les différents services et ce qu'ils coûteront. 

Si vous souhaitez tout supprimer après le tutoriel, assurez-vous de consulter cette section vers la fin de cet article. Je recommande également de [configurer un budget AWS](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) afin de pouvoir limiter les dépenses et être averti si vous allez les dépasser (pas de factures surprises, s'il vous plaît !).

* **S3** : Utilisé pour héberger les fichiers du site web. Si vous êtes toujours dans le [niveau gratuit AWS](https://aws.amazon.com/free), il ne devrait y avoir aucun coût. En dehors du niveau gratuit, le coût devrait être minimal, de l'ordre de quelques centimes.
* **Route 53** : Si vous décidez d'acheter un nom de domaine via Route 53 (optionnel – vous pouvez également "apporter votre propre" nom de domaine d'un autre fournisseur), cela coûtera 10 $ ou plus. Vous aurez également besoin d'une zone hébergée, ce qui vous coûtera 50 centimes par mois. Et les requêtes Route 53 (quand quelqu'un visite votre domaine) coûteront 40 centimes par million de requêtes.
* **AWS Certificate Manager** : Un certificat TLS/SSL via ACM est gratuit.
* **CloudFront** : Dans le niveau gratuit, il n'y a aucun coût. En dehors du niveau gratuit, cela dépendra du trafic, mais pour nos besoins, cela coûtera probablement seulement quelques centimes. Consultez la [page de tarification complète](https://aws.amazon.com/cloudfront/pricing/?nc=sn&loc=3) pour plus d'informations.

## Créer le code (HTML, CSS, JavaScript) pour votre CV

Cette section est l'endroit où vous pouvez laisser libre cours à votre créativité (et à vos compétences en codage). Rien ici n'est spécifique à AWS – c'est juste du bon vieux développement web.

Vous utiliserez finalement un bucket S3 pour héberger les fichiers de votre CV (HTML, CSS et JavaScript). S3 ne peut héberger qu'un site web statique, ce qui signifie que vous ne pouvez pas inclure quoi que ce soit qui nécessite du code côté serveur. Mais du contenu front-end toute la journée.

Je ne serai pas trop prescriptif pour le code que vous utilisez ici – c'est votre CV, après tout. Mais vous voudrez mettre en avant les éléments "habituels" du CV : historique de l'emploi, éducation, compétences/certifications, et peut-être des choses comme les honneurs/récompenses ou les loisirs pour vous rendre plus humain.

Si vous souhaitez lister des compétences en HTML, CSS et JavaScript sur votre CV, vous voudrez idéalement coder cette partie à la main (clin d'œil, pas d'aide de ChatGPT !), mais vous êtes également libre d'utiliser mon code ci-dessous comme point de départ.

### Fichier index.html

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV en ligne - Votre Nom</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <img src="headshot.jpg" alt="Photo de profil" class="headshot">
            <h1 id="name">Nom</h1>
            <p id="contactInfo">Localisation | Email</p>
        </header>
        <section id="employmentHistory">
            <h2>Historique de l'emploi</h2>
            <div id="timeline"></div> <!-- Placeholder pour le tableau JavaScript -->
        </section>
        <section id="education">
            <h2>Éducation</h2>
            <ul>
                <li>Diplôme | Université (Année)</li>
                <li>Diplôme | Université (Année)</li>
                <!-- Ajoutez plus d'éléments de liste si nécessaire -->
            </ul>
        </section>
        <section id="skills">
            <h2>Compétences/Certifications</h2>
            <ul>
				<li>Compétence 1</li>
				<li>Compétence 2</li>
				<li>Compétence 3</li>
				<li>Compétence 4</li>
                <!-- Ajoutez plus d'éléments de liste si nécessaire -->
			</ul>
        </section>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

### Fichier styles.css

```css
/* Réinitialisation de base pour le padding et la margin de tous les éléments */
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

/* Style du corps */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Conteneur pour centrer le contenu */
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
    padding: 20px;
}

/* Style de l'en-tête */
header {
    background: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

/* Style de l'image et du nom de l'en-tête */
.headshot {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    display: block;
    margin: 20px auto;
}

header h1 {
    margin-bottom: 10px;
}

/* Style des informations de contact */
#contactInfo {
    font-size: 1.1em;
    margin-bottom: 20px;
    color: #fff; 
    padding: 15px;
}


/* Style de la section pour l'emploi, l'éducation et les compétences */
section {
    background: #fff;
    margin: 20px 0;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

section h2 {
    margin-bottom: 10px;
}

/* Style de la timeline */
#timeline .entry {
    border-left: 3px solid #333;
    margin-bottom: 5px;
    cursor: pointer;
}

#timeline .entry-header {
    background: #e2e2e2;
    padding: 10px;
    margin-left: -3px; 
}

#timeline .entry-header:hover {
    background: #ccc; 
    color: #333; 
}

/* Style pour le contenu de la description du travail */
#timeline .entry-content p {
    padding: 5px 10px;
    background: #f9f9f9;
    border-left: 3px solid #333;
    display: block; 
}

/* Style de la liste pour l'éducation et les compétences */
section ul {
    list-style: inside square;
    padding: 0 20px;
}

section ul li {
    padding: 2px 0;
}

/* Ajustements pour la classe active */
.entry.active .entry-header {
    background-color: #e2e2e2; 
    color: #333; 
}

.entry.active .entry-content {
    display: block; 
}

/* Indice visuel pour les éléments cliquables */
.entry .entry-header:after {
    content: ' (cliquer pour développer)';
    font-size: 0.8em;
    color: #666;
}

.entry.active .entry-header:after {
    content: ' (cliquer pour réduire)';
    font-size: 0.8em;
    color: #666; 
}
```

### Fichier script.js

```javascript
// Utilisé sur le CV pour rendre l'historique de l'emploi interactif (chaque emploi est cliquable)
document.addEventListener('DOMContentLoaded', function () {
    // Tableau de placeholder avec les données de l'historique de l'emploi
    const employmentHistory = [
        { id: 1, title: 'Titre du poste', company: 'Nom de l\'entreprise', years: 'Année - Année', description: 'Description de ce que vous avez fait' },
        { id: 2, title: 'Titre du poste', company: 'Nom de l\'entreprise', years: 'Année - Année', description: 'Description de ce que vous avez fait' },
        { id: 3, title: 'Titre du poste', company: 'Nom de l\'entreprise', years: 'Année - Année', description: 'Description de ce que vous avez fait' }
        // Ajoutez plus d'entrées si nécessaire
    ];

    const timeline = document.getElementById('timeline');

    // Créer les entrées de la timeline
    employmentHistory.forEach(job => {
        // Conteneur d'entrée pour le travail
        const entry = document.createElement('div');
        entry.className = 'entry';
        entry.id = 'entry-' + job.id;

        // En-tête de titre pour le travail
        const header = document.createElement('div');
        header.className = 'entry-header';
        header.innerText = job.title;

        // Conteneur de contenu pour le travail, initialement caché
        const content = document.createElement('div');
        content.className = 'entry-content';
        content.innerHTML = `<strong>Entreprise :</strong> ${job.company}<br>
                             <strong>Années :</strong> ${job.years}<br>
                             <p>${job.description}</p>`;
        content.style.display = 'none';

        // Ajouter l'en-tête et le contenu à l'entrée
        entry.appendChild(header);
        entry.appendChild(content);

        // Écouteur d'événement pour basculer la visibilité du contenu
        header.addEventListener('click', function () {
            // Vérifier si le contenu de l'en-tête cliqué est actuellement affiché
            const isContentShown = content.style.display === 'block';
            // Masquer tout le contenu ouvert
            document.querySelectorAll('.entry-content').forEach(el => {
                el.style.display = 'none'; // Masquer le contenu
            });
            // Désactiver tous les en-têtes
            document.querySelectorAll('.entry').forEach(el => {
                el.classList.remove('active'); // Supprimer la classe active
            });

            if (!isContentShown) {
                // Si ce n'était pas affiché avant, l'afficher
                content.style.display = 'block';
                entry.classList.add('active');
            } // Si c'était affiché, il sera masqué dans le cadre de la boucle ci-dessus
        });

        timeline.appendChild(entry);
    });
});
```

## Créer un bucket S3 et le configurer pour l'hébergement de sites web statiques et l'accès public

Maintenant que vous avez vos trois fichiers de code (plus n'oubliez pas un "headshot.jpg" pour afficher votre visage souriant), vous avez besoin d'un endroit pour les mettre. 

Dans AWS, S3 est une excellente option pour le stockage d'objets (lire : fichiers) peu coûteux. Et si vous n'utilisez que du code côté client comme vous le faites, alors vous pouvez configurer S3 pour l'hébergement de sites web statiques.

### Créer un bucket S3

Dans la [Console de gestion AWS](https://console.aws.amazon.com/), naviguez vers **S3**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Navigate-to-S3.png)
_Naviguer vers S3_

Cliquez sur **Créer un bucket**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-an-S3-bucket.png)
_Créer un nouveau bucket_

Entrez les détails de votre bucket.

* **Nom du bucket** : **IMPORTANT !** Si vous prévoyez d'utiliser un domaine personnalisé pour votre CV, alors ce nom de bucket doit correspondre exactement au nom de domaine. Par exemple, j'utiliserai "amberaws.com" donc le nom de mon bucket doit être "amberaws.com". Si vous utilisez un nom différent, vous rencontrerez des problèmes lorsque vous arriverez à la partie Route 53 du tutoriel.
* **Région AWS** : Vous pouvez choisir n'importe quelle région, mais je recommande de choisir celle qui est la plus proche de vous. 
* **Propriété de l'objet** : Laissez le défaut **ACLs désactivés (recommandé)**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Bucket-details-1.png)
_Entrez le nom du bucket, la région et la propriété de l'objet_

En faisant défiler vers le bas, **désélectionnez** le paramètre pour **Bloquer tout accès public**. **NOTE** : Dans la plupart des scénarios, cela n'est pas recommandé, comme vous le verrez dans l'avertissement que vous recevez lorsque vous le désactivez. Mais parce que vous créez un CV public que vous voulez ouvrir au monde, alors désactiver cela est approprié.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Block-all-public-access-1.png)
_Désélectionnez l'option pour bloquer tout accès public, puis reconnaissez le paramètre_

Utilisez les valeurs par défaut pour le reste des paramètres du bucket, puis cliquez sur **Créer un bucket**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Bucket-defaults-and-create.png)
_Sélectionnez les valeurs par défaut pour le reste des paramètres du bucket, puis créez le bucket_

Vous avez maintenant un bucket vide, mais il n'est pas tout à fait prêt pour l'hébergement de sites web. Vous devrez apporter quelques mises à jour supplémentaires.

### Activer l'hébergement de sites web statiques

Pour que S3 puisse servir vos fichiers en tant que site web, vous devrez activer cela sur le bucket.

Cliquez sur le bucket que vous venez de créer et allez dans l'onglet **Propriétés**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Properties-tab.png)
_Naviguer vers l'onglet Propriétés du bucket_

Faites défiler _tout en bas_ de la page, et dans la section **Hébergement de sites web statiques**, cliquez sur **Modifier**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Static-website-hosting-edit.png)
_Modifier le paramètre d'hébergement de sites web statiques_

Sélectionnez **Activer**. Cela ouvrira des options supplémentaires.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Enable-static-website-hosting.png)
_Activer l'hébergement de sites web statiques_

Pour le **Document d'index**, entrez **index.html**. Cela spécifie la page d'accueil par défaut pour le site (votre code HTML pour votre CV). Ensuite, cliquez sur **Enregistrer les modifications**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Static-website-hosting-index-page.png)
_Spécifiez la page d'accueil par défaut (index.html) et enregistrez les modifications_

### Ajouter une politique de bucket pour permettre au contenu du bucket d'être accessible publiquement

Lorsque vous avez créé le bucket, vous avez dit que vous ne vouliez pas bloquer tout accès public. Mais même avec ce paramètre, le comportement par défaut de S3 est de "refuser" tout. Donc si vous ne dites pas explicitement que les gens peuvent accéder aux fichiers dans votre bucket, ils ne pourront pas. Vous accorderez des permissions de lecture avec une politique de bucket.

En haut de la page, cliquez sur l'onglet **Permissions**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Permissions-tab.png)
_Cliquez sur l'onglet Permissions du bucket_

Faites défiler vers le bas jusqu'à la section **Politique de bucket**, et cliquez sur **Modifier**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Edit-bucket-policy.png)
_Modifier la politique de bucket_

Copiez la politique de bucket suivante (code JSON).

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::Nom-du-Bucket/*"
            ]
        }
    ]
}
```

Collez le code dans la section Politique dans la console AWS. Cette politique dit "Autoriser" tout le monde (le Principal de "*") à prendre l'action "GetObject" (basiquement "lire") sur tous les fichiers dans votre bucket ("Nom-du-Bucket/*").

**IMPORTANT** : Mettez à jour "Nom-du-Bucket" avec le nom de votre bucket. Ensuite, cliquez sur **Enregistrer les modifications**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Bucket-policy-1.png)
_Collez le code JSON pour la politique de bucket, en mettant à jour "Nom-du-Bucket" par le vôtre_

Vous avez maintenant un bucket configuré pour l'hébergement de sites web statiques, et vous avez appliqué une politique qui permettra aux gens d'accéder au site. Il est maintenant temps d'ajouter vos fichiers de code impressionnants que vous avez créés précédemment.

En haut de la page, cliquez sur l'onglet **Objets**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Objects-tab.png)
_Cliquez sur l'onglet Objets du bucket_

Cliquez sur le bouton **Télécharger**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Upload-files.png)
_Cliquez sur le bouton Télécharger pour télécharger vos fichiers de code_

Glissez et déposez vos quatre fichiers dans le navigateur. Cela devrait inclure **index.html**, **styles.css**, **script.js** et **headshot.jpg**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Drag-and-drop-files.png)
_Glissez et déposez vos quatre fichiers (code et headshot.jpg)_

Après que les fichiers ont été téléchargés et que les quatre s'affichent dans la section **Fichiers et dossiers**, cliquez sur le bouton **Télécharger**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Upload-files-2.png)
_Téléchargez les fichiers_

Il est maintenant temps de tester que votre CV se charge. Pour ce faire, vous devrez obtenir le point de terminaison du site web du bucket S3.

Naviguez vers l'onglet **Propriétés** du bucket.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Properties-tab-1.png)
_Naviguez vers l'onglet Propriétés_

Faites défiler _tout en bas_ de la page, jusqu'à la section **Hébergement de sites web statiques**. Cliquez sur le lien **Point de terminaison du site web du bucket** (il s'ouvrira dans un nouvel onglet).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Website-endpoint-1.png)
_Cliquez sur le point de terminaison du site web du bucket pour voir votre CV (dans un nouvel onglet)_

Si tout a fonctionné, vous devriez voir votre travail affiché dans le navigateur. Hourra !

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Website-test-1-1.png)
_Cela fonctionne ! Votre CV est servi par S3._

Félicitations pour avoir hébergé votre CV dans S3 avec un accès public ! Mais aussi impressionnant que cela soit, ce serait encore plus impressionnant s'il utilisait un domaine personnalisé. Actuellement, il utilise l'URL du site web S3, formatée comme [nomdubucket].s3-website-[nomdela région].amazonaws.com. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/S3-bucket-URL.png)
_Le CV serait beaucoup plus cool avec son propre nom de domaine personnalisé_

Travaillons sur le nom de domaine ensuite, en utilisant Route 53, qui est le service de noms de domaine et DNS d'Amazon.

## Option de nom de domaine 1 : Enregistrer un nouveau nom de domaine avec Route 53

Si vous n'avez pas déjà un nom de domaine, vous pouvez en enregistrer un avec AWS, en utilisant Route 53. (Si vous avez déjà un nom de domaine avec un autre fournisseur, je vous donnerai quelques conseils généraux sur son utilisation dans la section suivante.)

Naviguez vers **Route 53**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Navigate-to-Route-53.png)
_Naviguer vers Route 53_

Sur le tableau de bord de Route 53, entrez simplement le **nom de domaine** qui vous intéresse, puis cliquez sur **Vérifier**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Check-domain-name-availability-1.png)
_Vérifier la disponibilité d'un nom de domaine_

Si le nom de domaine est disponible, vous pourrez le **sélectionner** (et s'il n'est pas disponible, vous verrez quelques noms alternatifs). Le sélectionner l'ajoutera à votre panier, vous fera passer par un processus de paiement, puis la charge apparaîtra sur votre facture AWS.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Select-available-domain.png)
_Sélectionnez le domaine disponible ou choisissez des alternatives_

Après avoir acheté le domaine, il créera automatiquement une **zone hébergée** pour vous. Vous pouvez penser à un domaine hébergé comme un conteneur pour les enregistrements et les règles qui contrôlent la manière dont le trafic est routé.  

Une zone hébergée publique (avec laquelle vous allez travailler) contrôle le trafic depuis Internet. Une zone hébergée privée contrôle le trafic interne à un AWS Virtual Private Cloud (VPC).

Vous pouvez consulter vos zones hébergées en cliquant sur **Zones hébergées** dans la navigation de gauche, puis en cliquant sur la zone qui correspond au nom de domaine que vous avez acheté ("amberaws.com" dans mon cas).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Hosted-zones.png)
_Sélectionnez la zone hébergée pour votre nom de domaine_

## Option de nom de domaine 2 : Utiliser un nom de domaine d'un fournisseur tiers

Donc, vous avez déjà un nom de domaine d'un autre endroit, comme GoDaddy, Namecheap, Google Domains ou similaire. Il est tout à fait possible d'utiliser Route 53 comme votre service DNS (ce qui a beaucoup d'avantages, et est facile à intégrer avec d'autres services AWS), tout en gardant le nom de domaine avec votre autre fournisseur.

Les détails de chaque bureau d'enregistrement sont légèrement différents, donc je vais donner quelques conseils généraux ici. Sachez également que la propagation des modifications DNS prendra plus de temps avec un fournisseur externe, et si les choses tournent mal, vous devrez probablement travailler directement avec eux. Mais je vais vous aider à commencer !

### Créer une zone hébergée et obtenir vos serveurs de noms

Même si vous n'utilisez pas un nom de domaine de Route 53, vous aurez toujours besoin d'une zone hébergée (encore une fois, cela contient les enregistrements et les règles qui contrôlent la manière dont le trafic est routé). 

Cliquez sur **Zones hébergées** dans la navigation de gauche, puis cliquez sur **Créer une zone hébergée**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-a-hosted-zone-1.png)
_Créer une zone hébergée pour votre nom de domaine externe_

Entrez le **nom de domaine** du fournisseur tiers, sélectionnez **Zone hébergée publique**, puis cliquez sur **Créer une zone hébergée**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Created-hosted-zone-details.png)
_Remplissez les détails pour la zone hébergée publique_

Une fois votre zone hébergée publique créée, vous verrez quatre **serveurs de noms** listés. Prenez note de ceux-ci.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Name-servers.png)
_Prenez note de vos serveurs de noms afin de pouvoir les entrer avec le fournisseur tiers_

Ensuite, allez dans les paramètres DNS de votre fournisseur de domaine actuel. Trouvez vos paramètres de serveur de noms, et remplacez-les par les serveurs de noms de Route 53.

Pour plus de détails, voici des guides de certains des fournisseurs de noms de domaine les plus populaires :

* [GoDaddy](https://uk.godaddy.com/help/edit-my-domain-nameservers-664)
* [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-change-dns-for-a-domain/)
* [Google Domains](https://support.google.com/domains/answer/3290309?hl=en)
* [Hostgator](https://www.hostgator.com/help/article/how-do-i-change-my-dns-or-name-servers)

Après avoir apporté les mises à jour sur le site tiers, et que les modifications ont été propagées, vous devriez être prêt à suivre le reste de cet article.

## Créer un enregistrement A avec un alias pour pointer vers le site web S3

Maintenant que vous avez une zone hébergée publique, vous devez créer un enregistrement qui indique comment le trafic doit être routé lorsque quelqu'un accède à votre nom de domaine.

Cliquez sur votre zone hébergée, puis cliquez sur **Créer un enregistrement**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-record.png)
_Créer un nouvel enregistrement_

**NOTE** : Si vous obtenez la vue "assistant" ci-dessous, cliquez sur **Passer à la création rapide**. (Si vous ne voyez pas cette vue "tuile", alors vous êtes déjà en mode création rapide.)

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Switch-to-quick-create.png)
_Passer à la vue création rapide_

Remplissez les détails de l'enregistrement.

* **Nom de l'enregistrement** : Laissez le sous-domaine vide, et utilisez simplement le domaine racine (comme "amberaws.com").
* **Type d'enregistrement** : A
* **Alias** : Activez cette option. Un alias vous permet de router vers des ressources AWS comme S3, CloudFront, Elastic Beanstalk, etc.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Record-details-1.png)
_Remplissez le domaine, le type d'enregistrement, puis activez l'alias_

Maintenant, remplissez les détails de l'endroit où router le trafic. Vous pouvez taper dans ces listes déroulantes pour filtrer les valeurs.

* **Alias vers le point de terminaison du site web S3**
* **Votre région** (j'utilise US West (Oregon))
* La dernière liste déroulante devrait se remplir automatiquement avec **votre site web S3**. **NOTE** : Si rien ne s'affiche ici, c'est probablement parce que vous n'avez pas nommé votre bucket de la même manière que votre nom de domaine. D'oh ! Vous devrez recréer le bucket avec le nom exact de votre domaine.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Route-traffic-to.png)
_Remplissez les détails pour le routage du trafic_

Pour la **Stratégie de routage**, sélectionnez **Routage simple**. Pour **Évaluer la santé de la cible**, laissez le défaut **Oui**, puis cliquez sur **Créer des enregistrements**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-record-details-2.png)
_Choisissez la stratégie de routage, la santé de la cible, puis créez l'enregistrement_

Il peut falloir jusqu'à 60 secondes pour que vos modifications prennent effet. Vous pouvez consulter l'état de la propagation en cliquant sur le pratique **Voir l'état** en haut de la page.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/View-DNS-status.png)
_Voir l'état de propagation de vos modifications_

Après que le **Statut** passe de PENDING à **INSYNC**, vous devriez être prêt à tester vos modifications.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Status-of-INSYNC.png)
_Assurez-vous que le statut indique INSYNC avant de tester les choses_

Maintenant, testons ! Si tout a fonctionné, alors lorsque vous **tapez votre nom de domaine dans un navigateur** (comme amberaws.com), Route 53 devrait vous diriger vers le site web S3, ce qui signifie que vous devriez voir votre (superbe) CV.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Test-domain-name-1-1.png)
_Cela fonctionne ! Votre nom de domaine devrait maintenant afficher votre CV._

Félicitations ! Vous avez fait un énorme progrès. La dernière étape est d'obtenir une connexion sécurisée (HTTPS, avec un certificat TLS/SSL) pour pouvoir vous débarrasser de ce message "Non sécurisé" de votre navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Test-domain-name-cert.png)

Abordons cette étape ensuite, en utilisant AWS Certificate Manager.

## Créer un certificat TLS/SSL public en utilisant AWS Certificate Manager

Si vous avez besoin d'un rappel sur les certificats, ceux-ci aident à garantir une connexion sécurisée entre les utilisateurs et le serveur auquel ils font une demande. 

Par exemple, si j'envoie des informations bancaires sur Internet, je veux savoir qu'elles vont à un serveur de confiance et que la connexion est cryptée. Et même pour quelque chose d'aussi "simple" qu'un CV, une connexion sécurisée donnera aux visiteurs la confiance qu'ils ne sont pas arrivés sur un site web douteux.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Certificates.png)
_Pourquoi nous avons besoin de certificats_

Dans l'univers AWS, les certificats sont créés et gérés dans AWS Certificate Manager (ACM). (Vous pouvez également importer des certificats existants d'une autre autorité si vous en avez.)

Naviguez vers **Certificate Manager**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Navigate-to-ACM.png)
_Naviguer vers Certificate Manager_

**IMPORTANT !** Pour cette section, vous devez changer votre région pour **us-east-1 (N. Virginie)**. Si vous créez un certificat dans une autre région, vous ne pourrez pas l'utiliser avec CloudFront (où vous finirez par aboutir).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/us-east-1.png)
_Changer de région pour us-east-1 (N. Virginie)_

À partir de la page d'accueil de Certificate Manager, cliquez sur **Demander un certificat**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Request-a-certificate.png)
_Demander un certificat_

Sélectionnez **Demander un certificat public** puis cliquez sur **Suivant**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Request-public-certificate.png)
_Sélectionnez un certificat public puis cliquez sur suivant_

Entrez votre **nom de domaine** (comme "amberaws.com"), laissez le reste des options par défaut, puis cliquez sur **Demander**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Details-of-certificate.png)
_Entrez votre nom de domaine puis demandez_

La demande a réussi, mais elle aura un statut "en attente de validation" jusqu'à ce que vous validiez le DNS. Cliquez sur **Voir le certificat**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/View-certificate.png)
_Voir le certificat pour prendre des mesures supplémentaires_

Avant qu'un certificat puisse être émis, Amazon doit confirmer que vous possédez ce domaine et que vous êtes en mesure de modifier les paramètres DNS (dans Route 53). Pour démarrer ce processus, cliquez sur **Créer des enregistrements dans Route 53**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-records-in-Route-53.png)
_Créer des enregistrements dans Route 53 pour valider le DNS_

Il y a divers filtres appliqués à cet écran suivant, vérifiant l'état de validation et si votre domaine est trouvé dans Route 53. À partir de là, vous pouvez cliquer sur **Créer des enregistrements**, ce qui créera effectivement – attendez-le – un enregistrement dans Route 53 pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-records-from-ACM.png)
_Créer des enregistrements, ce qui créera un enregistrement CNAME dans Route 53_

Si la création de l'enregistrement a réussi, vous devriez voir un message à cet effet.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Success-DNS-record.png)
_Enregistrement créé avec succès dans Route 53 pour valider le DNS_

L'enregistrement a été créé dans Route 53. Donc, naviguez vers **Route 53**, vers **votre zone hébergée** sur laquelle vous travailliez précédemment. Vous devriez voir un nouvel **enregistrement CNAME** qui a été créé à partir de Certificate Manager.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/CNAME-record-in-Route-53.png)
_Voir le nouvel enregistrement CNAME dans Route 53_

Super ! Vous avez un certificat TLS/SSL, mais que faites-vous avec maintenant ?

Vos fichiers de site web sont actuellement hébergés dans S3, mais malheureusement, vous ne pouvez pas utiliser un certificat sur un bucket S3.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/No-cert-on-S3.png)
_Les certificats ne fonctionnent pas avec S3_

Ce dont vous avez besoin à la place, c'est une distribution CloudFront qui pointe vers le bucket S3. Et ensuite, le certificat est appliqué à la distribution CloudFront.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Cert-on-CloudFront.png)
_CloudFront est la solution !_

Vous savez ce que cela signifie, n'est-ce pas ? Cela signifie que nous devons nous rendre à CloudFront ensuite !

## Créer une distribution CloudFront

CloudFront est le réseau de diffusion de contenu, ou CDN, d'Amazon. Il est utilisé pour obtenir du contenu plus rapidement pour les utilisateurs en le mettant en cache dans des "emplacements de périphérie" à travers le monde. Cela fonctionne très bien pour des choses comme les vidéos et les images, les rendant plus rapides à charger.  

Pour votre simple CV, parce que les fichiers sont si petits, vous ne remarquerez pas beaucoup de différence de performance. Mais c'est _la_ façon dont vous pourrez appliquer le certificat TLS/SSL que vous avez créé dans la section précédente.

Naviguez vers **CloudFront**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Navigate-to-CloudFront.png)
_Naviguer vers CloudFront_

Sur la page d'accueil de CloudFront, cliquez sur **Créer une distribution CloudFront**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Create-a-CloudFront-distribution.png)
_Créer une distribution CloudFront_

Le domaine d'origine est l'endroit où se trouvent vos fichiers de site web, qui est dans S3. Si vous tapez **S3** pour filtrer, il devrait faire apparaître votre bucket.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Origin-domain.png)
_Filtrer par S3 pour trouver votre bucket comme domaine d'origine_

Mais attendez ! Vous obtenez un message concernant l'utilisation du point de terminaison du site web plutôt que du point de terminaison du bucket. Oui, c'est ce que vous voulez ! Cliquez sur **Utiliser le point de terminaison du site web**, et AWS mettra à jour le point de terminaison pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Website-endpoint-not-bucket-endpoint.png)
_Utiliser le point de terminaison du site web, pas le point de terminaison du bucket_

Il y a des tonnes de paramètres sur le reste de cette page, mais vous n'avez besoin de mettre à jour que quelques-uns.

Faites défiler jusqu'à la section **Comportement du cache par défaut**, puis sous **Visionneuse**, sélectionnez **Rediriger HTTP vers HTTPS**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Redirect-HTTP-to-HTTPS.png)
_Rediriger HTTP vers HTTPS_

Faites défiler jusqu'à **Pare-feu d'application Web (WAF)** et sélectionnez **Ne pas activer les protections de sécurité**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/WAF.png)
_Ne pas activer le WAF_

Dans la section suivante, **Paramètres** :

* Pour **Nom de domaine alternatif (CNAME)**, entrez votre nom de domaine (comme "amberaws.com").
* Pour **Certificat SSL personnalisé**, sélectionnez le certificat que vous avez configuré précédemment. **NOTE** : si vous l'avez configuré dans une région autre que us-east-1 (N. Virginie), il n'apparaîtra pas ici. D'oh ! Vous devrez le recréer dans us-east-1.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Settings-for-CloudFront.png)
_Entrez un nom de domaine alternatif et le certificat SSL personnalisé_

Faites défiler jusqu'en bas de la page.

Pour **Objet racine par défaut**, entrez **index.html** (votre page d'accueil par défaut) puis cliquez sur **Créer une distribution**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Index-and-create-distribution.png)
_Définissez l'objet racine par défaut comme index.html puis créez la distribution_

Il faudra plusieurs minutes pour que la distribution CloudFront termine le déploiement (même si en haut de la page il est indiqué "Créé avec succès"). Vous saurez qu'elle est terminée lorsque la valeur **Dernière modification** affiche une date et une heure.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Last-modified.png)
_Le déploiement est terminé lorsqu'une date/heure apparaissent dans "Dernière modification"_

Pour tester que tout fonctionne avec CloudFront et le certificat TLS/SSL, copiez le **Nom de domaine de la distribution**. Ouvrez un nouvel onglet dans le navigateur et naviguez vers cette adresse. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Distribution-domain-name.png)
_Copiez le nom de domaine de la distribution et ouvrez-le dans un nouvel onglet_

Si tout a fonctionné, vous devriez maintenant voir l'icône de cadenas tant attendue dans votre navigateur, indiquant que vous êtes sur une connexion sécurisée utilisant le certificat configuré via Certificate Manager.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/CloudFront-cert.png)
_Le certificat TLS/SSL fonctionne avec CloudFront !_

Super ! Mais avant de vous exciter en pensant que nous avons terminé, rappelez-vous que vous voulez finalement accéder à votre nom de domaine personnalisé pour charger le CV, et non à ce long nom de domaine de distribution CloudFront.

## Mettre à jour Route 53 pour pointer vers la distribution CloudFront

À l'heure actuelle, l'enregistrement A dans Route 53 pointe vers le bucket S3, comme ceci...

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Current-setup.png)
_Route 53 pointe actuellement vers le bucket S3_

Au lieu de cela, nous voulons que Route 53 pointe vers la distribution CloudFront, qui pointe ensuite vers S3, comme ceci...

![Image](https://www.freecodecamp.org/news/content/images/2023/11/What-we-want.png)
_Route 53 devrait pointer vers CloudFront, qui pointe ensuite vers S3_

Naviguez à nouveau vers **Route 53**, vers la **zone hébergée** avec laquelle vous avez travaillé. **Sélectionnez l'enregistrement A**, puis sur le côté droit de l'écran, cliquez sur **Modifier l'enregistrement**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Edit-A-record.png)
_Modifier l'enregistrement A de Route 53_

Au lieu de router le trafic vers S3, mettez à jour les trois listes déroulantes pour pointer vers votre distribution CloudFront.

* **Alias vers la distribution CloudFront** 
* **US East (N. Virginie)** (cette option est sélectionnée pour vous et grisée)
* **Choisissez votre distribution** (elle devrait se remplir automatiquement dans la troisième liste déroulante)

Cliquez sur **Enregistrer**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Edit-A-record-details.png)
_Mettre à jour l'enregistrement A pour router le trafic vers CloudFront_

## Admirez le résultat final

Et maintenant le moment de vérité : si tout a fonctionné, vous devriez pouvoir naviguer vers votre nom de domaine personnalisé et avoir votre CV chargé sur une connexion sécurisée.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Final-resume.png)
_CV final chargé sur un nom de domaine personnalisé via une connexion sécurisée_

Et VOILÀ ! Cela fonctionne.

Les fichiers du CV (provenant de S3 via CloudFront) se chargent sur le nom de domaine personnalisé (de Route 53) via une connexion sécurisée utilisant le certificat TLS/SSL (de Certificate Manager). Beau travail.

Voici ce que vous avez construit :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Final-diagram.png)
_Un diagramme du projet final_

## IMPORTANT ! Supprimez vos ressources

Au début de l'article, j'ai couvert les coûts des services. Si vous choisissez de les laisser fonctionner, cela ne devrait pas vous coûter une fortune (sauf, bien sûr, si votre CV devient viral et que vous payez soudainement pour une tonne de trafic Route 53 et CloudFront... peut-être un bon problème ?).  

Mais définissez définitivement un [Budget AWS](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) pour être averti lorsque les charges atteignent un certain seuil.

Pour ceux d'entre vous qui souhaitent supprimer tout ce que vous avez construit, faisons cela maintenant.

### Désactiver et supprimer la distribution CloudFront

Naviguez vers **CloudFront** et sélectionnez votre distribution. Avant de pouvoir la supprimer, vous devez d'abord la **Désactiver**. 

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Disable-CloudFront-distribution-1.png)
_Désactiver la distribution CloudFront_

Cela prendra plusieurs minutes à compléter, et cela doit être terminé avant de pouvoir supprimer certaines autres choses. Donc laissez-le fonctionner. Lorsqu'il est terminé, vous devriez voir une date et une heure dans la colonne **Dernière modification**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/CloudFront-disabled.png)
_Assurez-vous que la distribution CloudFront est désactivée_

Une fois la distribution désactivée, sélectionnez-la puis cliquez sur **Supprimer**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-CloudFront-distribution.png)
_Supprimer la distribution CloudFront_

### Supprimer les enregistrements de la zone hébergée Route 53

Naviguez vers **Route 53** et la zone hébergée avec laquelle vous avez travaillé. Les enregistrements ne coûteront pas d'argent, mais si vous ne prévoyez pas de les utiliser, il est bon de les supprimer pour éviter toute confusion à l'avenir.

Sélectionnez l'**enregistrement A** et l'**enregistrement CNAME** puis cliquez sur **Supprimer les enregistrements**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-Route-53-records.png)
_Supprimer l'enregistrement A et l'enregistrement CNAME de Route 53_

### Supprimer la zone hébergée (optionnel)

Vous pouvez également choisir de supprimer votre zone hébergée dans Route 53, mais si vous le faites, votre domaine pourrait devenir indisponible sur Internet.  

Si vous prévoyez d'utiliser votre nom de domaine à un moment donné dans le futur, je recommande de garder la zone hébergée (j'ai choisi de garder la mienne). **Garder la zone vous coûtera 50 centimes par mois.**

Mais si vous souhaitez procéder à la suppression, il suffit de **sélectionner la zone hébergée** et de cliquer sur **Supprimer**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-hosted-zone.png)
_Supprimer la zone hébergée Route 53_

Confirmez que vous avez terminé les actions dans ce message d'avertissement, tapez "**supprimer**", puis cliquez sur **Supprimer**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-hosted-zone-1.png)
_Confirmer la suppression de la zone hébergée Route 53_

### Supprimer le certificat de Certificate Manager

Naviguez vers **Certificate Manager**. Sélectionnez **le certificat** que vous avez créé, puis cliquez sur **Supprimer**. (Si la distribution CloudFront n'a pas encore été désactivée, vous obtiendrez une erreur à cette étape indiquant que la ressource est toujours utilisée.)

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-certificate.png)
_Supprimer le certificat de Certificate Manager_

### Vider le bucket S3 puis le supprimer

Naviguez vers **S3**, vers la liste de tous vos buckets. Sélectionnez le bucket puis cliquez sur **Supprimer**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-bucket.png)
_Supprimer le bucket S3_

Avant de pouvoir supprimer un bucket, vous devez d'abord supprimer les fichiers qu'il contient. AWS fournit un lien pratique pour cela. Cliquez sur le lien pour **vider la configuration du bucket**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Empty-bucket.png)
_Vider les fichiers du bucket S3_

Confirmez que vous souhaitez supprimer définitivement les fichiers (vous le souhaitez) en tapant "**supprimer définitivement**" puis en cliquant sur **Vider**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Permanently-delete.png)
_Confirmer la suppression des fichiers_

Maintenant que le bucket est vide, vous pouvez le supprimer. Et dans le message de succès en haut de l'écran, il y a un lien pratique pour le faire. Cliquez sur **supprimer la configuration du bucket**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-bucket-configuration.png)
_Supprimer le bucket S3_

Confirmez cette action en tapant le **nom de votre bucket**, puis en cliquant sur **Supprimer le bucket**.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Delete-bucket-final.png)

Et c'est tout ! Les ressources ont été supprimées, et vous ne devriez pas encourir de frais supplémentaires.

## Conclusion

Félicitations pour être arrivé jusqu'à la fin ! J'espère que vous avez réussi à construire un CV, et en même temps à consolider certaines de vos compétences AWS pour l'avenir. N'hésitez pas à le partager avec le monde, et bonne chance dans votre recherche d'emploi.

_Pour plus de tutoriels sur AWS et d'autres technologies, rendez-vous sur [Tiny Technical Tutorials](https://www.youtube.com/playlist?list=PLwyXYwu8kL0wg9R_VMeXy0JiK5_c70IrV) sur YouTube._