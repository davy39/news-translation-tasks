---
title: Comment ajouter un certificat SSL et un domaine Namecheap personnalisé à un
  site GitLab Pages
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-30T16:57:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-an-ssl-certificate-and-custom-namecheap-domain-to-a-gitlab-pages-site-323f8f3ce642
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9QSXL-RF1rxq9xyoPZjFKw.jpeg
tags:
- name: GitLab
  slug: gitlab
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: SSL
  slug: ssl
- name: 'tech '
  slug: tech
seo_title: Comment ajouter un certificat SSL et un domaine Namecheap personnalisé
  à un site GitLab Pages
seo_desc: 'By Erica Pisani

  Adding an SSL certificate and custom Namecheap domain to a GitLab Pages site can
  be a bit more challenging than it seems.

  Crucial pieces of the setup information live in sometimes dense documentation across
  different sites. It can be ...'
---

Par Erica Pisani

Ajouter un certificat SSL et un domaine Namecheap personnalisé à un site GitLab Pages peut être un peu plus difficile que cela n'y paraît.

Des éléments cruciaux des informations de configuration se trouvent dans une documentation parfois dense sur différents sites. Il peut être difficile de savoir si vous avez correctement configuré les choses, car vous devez attendre des heures pour confirmer que vos modifications ont été propagées.

Même lorsque vous savez que quelque chose ne va pas, vous ne pouvez pas toujours dire quoi. Cela rend le débogage du problème frustrant et difficile à corriger.

Ce guide vise à rendre le processus un peu plus simple et moins frustrant. Il suppose que vous avez :

* Déjà configuré votre projet sur GitLab Pages et que vous pouvez y accéder en entrant `<votre-nom-d-utilisateur>.gitlab.io/<votre-nom-de-projet>` dans votre navigateur
* Acheté un nom de domaine personnalisé ainsi qu'un certificat SSL via Namecheap

### **Étape 1 : Activer le certificat SSL**

Dans Namecheap, allez sur la page "Liste des produits" > "Certificats SSL". Vous devriez voir une liste de certificats SSL que vous avez achetés mais que vous n'avez pas encore activés. Cliquez sur "Activer" pour le certificat SSL que vous souhaitez activer pour votre site.

### **Étape 2 : Générer la demande de certificat SSL**

Vous devriez être redirigé vers une page qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*u9hG-Wrtm22y9byC5SmQTA.png)

Pour générer une CSR, vous devrez exécuter la commande suivante dans votre terminal : `openssl req -new -newkey rsa:2048 -nodes -keyout <votre-nom-de-domaine>.key -out <votre-nom-de-domaine>.csr`.

Une clé privée sera générée à la suite de cette commande. **NE PERDEZ PAS CETTE CLÉ.** Vous en aurez besoin plus tard lorsque vous installerez votre certificat sur GitLab. Si vous la perdez, vous devrez soumettre une autre demande de CSR.

Vous pouvez lire les détails techniques [ici](https://www.namecheap.com/support/knowledgebase/article.aspx/9446/0/apache-opensslmodsslnginx) sur la génération d'une CSR si vous le souhaitez, mais en résumé :

* Il est fortement recommandé de remplir tous les champs obligatoires. Votre CSR pourrait être rejetée lors de l'activation si vous ne le faites pas. Si vous remplissez cette CSR pour un site personnel ou un hobby, vous pouvez entrer `NA` pour les champs "Organisation" et "Unité d'organisation".
* Si le certificat est émis pour un sous-domaine spécifique, vous devez spécifier le sous-domaine dans le champ "Nom commun". Exemple : `sous-domaine.ssl-certificate-host.com`
* Si le certificat doit être un certificat générique, le domaine doit commencer par un astérisque. Exemple : `*.ssl-certificate-host.com`

Pour les besoins de ce guide, nous supposerons que vous obtenez le certificat pour quelque chose comme `<exemple-domaine>.com`.

Une fois que vous avez exécuté la commande, vous devriez avoir un fichier `.csr` et `.key` dans votre répertoire de travail. Ouvrez le fichier `.csr` et copiez son contenu. Il devrait avoir l'en-tête `----- BEGIN CERTIFICATE REQUEST -----`.

Collez le contenu du fichier dans le champ "Enter CSR". La page remplira automatiquement le champ de domaine du formulaire en fonction des informations dans la CSR.

Une fois que vous cliquez sur "Suivant", vous devriez voir la page suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VYlKqYMsnvyaF0smz4q_8w.png)

Vérifiez que les informations sont correctes, puis cliquez à nouveau sur "Suivant" pour passer à l'étape "Confirmez que vous possédez le domaine".

### **Étape 3 : Confirmez que vous possédez le domaine**

Il existe plusieurs options pour le faire :

* Email
* Basé sur HTTP
* Basé sur DNS

Personnellement, j'ai eu des problèmes de validation par email, donc pour les besoins de ce guide, sélectionnez "Basé sur DNS". Cela nécessite de configurer une valeur `CNAME` dans les paramètres DNS de votre domaine, ce que nous couvrirons plus tard dans ce guide.

Pour l'instant, cliquez sur "Suivant" après avoir sélectionné "Basé sur DNS", mais si vous changez d'avis sur cette forme de validation plus tard, il est possible de la modifier.

### **Étape 4 : Spécifiez qui recevra le fichier SSL**

Confirmez que l'email dans le champ est correct. C'est l'email qui recevra le certificat une fois qu'il aura été activé.

### **Étape 5 : Révision et soumission**

Confirmez que les informations affichées sont correctes, puis cliquez sur "Soumettre".

### **Étape 6 : Configurer l'enregistrement `CNAME` pour valider la propriété du domaine**

Une fois que vous avez soumis le formulaire, vous serez redirigé vers une page montrant les détails du certificat SSL avec une fenêtre de notification utile qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*rBxGLLFzyBqDRe1ROxYaTw.png)

Cliquez sur le lien pour la méthode DCV basée sur DNS. Vous serez redirigé vers une page qui montre les informations que vous avez entrées précédemment, telles que :

* Le nom de domaine
* Le type de serveur web qui aura le certificat installé (devrait être Apache, Nginx, cPanel, ou autre)
* Méthodes DCV en cours d'utilisation

Accédez aux options de la liste déroulante pour le bouton "Modifier les méthodes" à droite de "Méthodes DCV en cours d'utilisation" afin d'accéder et de cliquer sur l'option "Obtenir l'enregistrement".

Une fenêtre contextuelle apparaîtra montrant l'enregistrement `CNAME` que vous devez configurer afin de confirmer la propriété du domaine. Copiez ces valeurs dans un fichier texte vide, car vous devrez accéder à la page "DNS avancé" de votre domaine. Cela est accessible via "Tableau de bord" ou "Liste des domaines" > "Gérer" (à côté de votre domaine dans la liste) > "DNS avancé".

Dans la section "Enregistrements d'hôte" :

* Cliquez sur "Ajouter un nouvel enregistrement"
* Sélectionnez "Enregistrement CNAME".
* Collez les valeurs que vous avez copiées précédemment de la fenêtre contextuelle "Obtenir l'enregistrement" dans les champs correspondants.

Avant d'enregistrer ces valeurs, il y a un petit "piège".

Comme le souligne Namecheap dans leur [documentation](https://www.namecheap.com/support/knowledgebase/article.aspx/9637/68/how-can-i-complete-the-domain-control-validation-dcv-for-my-SSL-certificate#dns), ils "ajoutent automatiquement le nom de domaine aux valeurs soumises lors de la création de l'enregistrement". Cela signifie que le nom de domaine qui apparaît dans la valeur "hôte" est une valeur dupliquée. Supprimez `<votre-domaine-personnalise>.com` à la fin de la valeur "hôte" et vous serez prêt à partir.

Après avoir enregistré cet enregistrement, il faudra un certain temps avant que le certificat ne soit émis. Une fois que vous avez reçu le certificat par email, passez à l'étape 8. Si vous ne l'avez pas déjà fait, configurons les enregistrements supplémentaires nécessaires pour envoyer les personnes vers `<votre-nom-d-utilisateur>.gitlab.io/<votre-projet>` lorsqu'elles entrent `<votre-domaine-personnalise>.com`.

### **Étape 7 : Configurer vos enregistrements d'hôte dans Namecheap**

Comme indiqué dans la [documentation de GitLab](https://docs.gitlab.com/ee/user/project/pages/getting_started_part_three.html#dns-txt-record), vous devrez également prouver du côté de GitLab que vous possédez le domaine personnalisé sur lequel vous souhaitez servir votre site GitLab Pages.

Comme mentionné précédemment, ce guide suppose que vous souhaitez simplement utiliser `exemple.com` (ou `www.exemple.com`), vous devrez donc ajouter les enregistrements d'hôte suivants :

* Type `A Record`, Hôte `@`, Valeur `35.185.44.232` (il s'agit de l'IP actuelle de GitLab Pages au moment de la rédaction)
* Type `CNAME Record`, Hôte `www`, Valeur `exemple.com` (cela garantit que les personnes qui entrent le sous-domaine 'www' (c'est-à-dire : `www.exemple.com`) atteignent toujours votre site)
* _Remarque : Vous ne pourrez pas entrer celui-ci tant que vous n'aurez pas ajouté le domaine via le flux "Nouveau domaine Pages" décrit dans l'étape 8._ Type `TXT Record`, Hôte `@`, Valeur `gitlab-pages-verification-code=11112222aaaabbbb`

### **Étape 8 : Installer le certificat dans GitLab**

Rendez-vous sur la page "Pages" de votre projet GitLab que vous essayez de configurer (sous "Paramètres" > "Pages" dans la barre latérale).

Pour ajouter votre domaine personnalisé que GitLab sert pour votre site Pages, cliquez sur le bouton "Nouveau domaine" en haut à droite. Vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tjmYJy0dsUrhDJH0Re4PRw.png)

Entrez votre domaine personnalisé (`exemple.com`) dans le champ de domaine, puis la partie suivante est celle où cela devient intéressant.

Si vous essayez simplement d'entrer votre certificat (`exemple_com.crt`) et votre clé privée (générée lorsque vous avez initialement envoyé la demande de certificat) dans les champs, vous obtiendrez probablement une erreur "Le certificat manque des intermédiaires".

Cela est dû au fait que GitLab utilise quelque chose comme NGINX pour recevoir les requêtes sur son IP Pages avant de router la requête vers le site correct. Namecheap, dans leur [documentation](https://www.namecheap.com/support/knowledgebase/article.aspx/9474/69/how-do-i-create-a-pem-file-from-the-certificates-i-received-from-you), souligne qu'il est "nécessaire de combiner votre certificat avec les certificats CA dans un seul fichier".

Cela signifie pour vous que vous devez combiner le texte trouvé dans vos fichiers `exemple_com.crt` et `exemple_com.ca-bundle` dans le champ "certificat". À la fin, vous devriez avoir quelque chose comme :

Ajoutez la clé privée au dernier champ, et vous avez terminé. Il faudra du temps pour que les modifications se propagent. Si vous vérifiez dans quelques heures, vous devriez voir une indication à côté de votre adresse dans la barre d'URL montrant que votre connexion à votre site est maintenant sécurisée.

### **Ressources/Références**

* [https://about.gitlab.com/features/pages/](https://about.gitlab.com/features/pages/)
* [https://docs.gitlab.com/ee/user/project/pages/getting_started_part_three.html#dns-txt-record](https://docs.gitlab.com/ee/user/project/pages/getting_started_part_three.html#dns-txt-record)
* [https://www.namecheap.com/support/knowledgebase/article.aspx/9474/69/how-do-i-create-a-pem-file-from-the-certificates-i-received-from-you](https://www.namecheap.com/support/knowledgebase/article.aspx/9474/69/how-do-i-create-a-pem-file-from-the-certificates-i-received-from-you)
* [https://www.namecheap.com/support/knowledgebase/article.aspx/9637/68/how-can-i-complete-the-domain-control-validation-dcv-for-my-SSL-certificate#dns](https://www.namecheap.com/support/knowledgebase/article.aspx/9637/68/how-can-i-complete-the-domain-control-validation-dcv-for-my-SSL-certificate#dns)
* [https://stackoverflow.com/a/49124195/2719852](https://stackoverflow.com/a/49124195/2719852)