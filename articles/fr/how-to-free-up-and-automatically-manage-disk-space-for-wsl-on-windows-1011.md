---
title: Comment libérer et gérer automatiquement l'espace disque pour WSL sur Windows
  10/11
subtitle: ''
author: brooklyn
co_authors: []
series: null
date: '2025-08-06T23:34:09.564Z'
originalURL: https://freecodecamp.org/news/how-to-free-up-and-automatically-manage-disk-space-for-wsl-on-windows-1011
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754523230294/70893973-fddf-42a9-b41a-2a8f94a47e22.png
tags:
- name: WSL
  slug: wsl
- name: wsl2
  slug: wsl2
- name: disk management
  slug: disk-management
- name: disk
  slug: disk
- name: disk space
  slug: disk-space
- name: automation
  slug: automation
- name: Powershell
  slug: powershell
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
- name: windows 11
  slug: windows-11
seo_title: Comment libérer et gérer automatiquement l'espace disque pour WSL sur Windows
  10/11
seo_desc: Windows Subsystem for Linux (WSL) lets you run a Linux environment directly
  on Windows. This is particularly useful for web development where you can develop
  and test applications in a Linux environment without leaving Windows. You can even
  run freeC...
---

Windows Subsystem for Linux ([WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install)) vous permet d'exécuter un environnement Linux directement sur Windows. Cela est particulièrement utile pour le développement web où vous pouvez développer et tester des applications dans un environnement Linux sans quitter Windows. Vous pouvez même exécuter [freeCodeCamp localement](https://contribute.freecodecamp.org/how-to-setup-wsl/) avec celui-ci !

Mais la gestion de l'espace disque peut être un vrai défi, car WSL utilise des disques durs virtuels qui ne libèrent pas automatiquement l'espace inutilisé.

Ce tutoriel vous guidera à travers le processus de compactage manuel de vos disques durs virtuels WSL. Nous automatiserons cette tâche à l'aide d'un script PowerShell, garantissant que votre environnement WSL reste efficace et sans encombrement.

## Récupérez votre espace

WSL utilise une plateforme de virtualisation pour installer des distributions Linux sur votre système Windows. Chaque distribution que vous ajoutez obtient son propre disque dur virtuel (VHD), qui utilise le système de fichiers ext4 (commun dans Linux). Il est enregistré sur votre lecteur Windows sous forme de fichier ext4.vhdx.

Problèmes clés ici :

* Stockage inefficace : par défaut, les fichiers VHD **ne récupèrent pas** l'espace inutilisé. Cela signifie que lorsque vous supprimez un fichier dans WSL, l'espace disque associé n'est pas immédiatement libéré.

* Consommation d'espace disque : en raison de ce stockage inefficace, les **fichiers VHD peuvent devenir volumineux** grâce à ces données accumulées, surtout si vous êtes un utilisateur intensif de WSL.

* Besoin de maintenance : vous ne savez peut-être pas que vous devez **compacter** vos fichiers VHD afin de récupérer de l'espace disque.

Si vous remarquez que votre espace disque libre diminue même après avoir supprimé des fichiers et des applications, WSL pourrait en être la raison. Ce tutoriel vous aidera à maintenir votre environnement WSL et Windows en bon état de fonctionnement.

## Table des matières

* [Partie 1 : Comment compacter manuellement votre disque dur virtuel](#heading-partie-1-comment-compacter-manuellement-votre-disque-dur-virtuel)

  * [Prérequis](#heading-prérequis)

  * [Étape 1 : Vérifiez votre version et votre statut WSL](#heading-étape-1-vérifiez-votre-version-et-votre-statut-wsl)

  * [Étape 2 : Listez toutes les distributions installées de manière détaillée](#heading-étape-2-listez-toutes-les-distributions-installées-de-manière-détaillée)

  * [Étape 3 : Localisez le chemin de votre disque dur virtuel Linux (VHDX)](#heading-étape-3-localisez-le-chemin-de-votre-disque-dur-virtuel-linux-vhdx)

  * [Étape 4 : Arrêtez toutes les instances WSL](#heading-étape-4-arrêtez-toutes-les-instances-wsl)

  * [Étape 5 : Compacter le disque dur virtuel Linux à l'aide de DiskPart](#heading-étape-5-compacter-le-disque-dur-virtuel-linux-à-laide-de-diskpart)

  * [Étape 6 : Redémarrez WSL et vérifiez](#heading-étape-6-redémarrez-wsl-et-vérifiez)

* [Partie 2 : Comment faciliter votre vie avec l'automatisation](#heading-partie-2-comment-faciliter-votre-vie-avec-lautomatisation)

  * [Prérequis](#heading-prérequis-1)

  * [Étape 1 : Découvrez les distributions WSL2 installées](#heading-étape-1-découvrez-les-distributions-wsl2-installées)

  * [Étape 2 : Sélectionnez une distribution à compacter](#heading-étape-2-sélectionnez-une-distribution-à-compacter)

  * [Étape 3 : Localisez le fichier ext4.vhdx](#heading-étape-3-localisez-le-fichier-ext4vhdx)

  * [Étape 4 : L'invite de confirmation](#heading-étape-4-linvite-de-confirmation)

  * [Étape 5 : Arrêtez WSL et compacter](#heading-étape-5-arrêtez-wsl-et-compacter)

  * [Étape 6 : Exécutez un script DiskPart](#heading-étape-6-exécutez-un-script-diskpart)

## **Partie 1 : Comment compacter manuellement votre disque dur virtuel**

Commençons par passer par le processus manuellement. Cette section vous guidera à travers la vérification de votre version WSL et des distributions Linux associées, la recherche des fichiers VHD, l'arrêt de WSL et le compactage du disque virtuel.

### **Prérequis**

* Windows 10 (20H1/2004+) ou Windows 11 avec WSL2 installé

* PowerShell ou l'invite de commande s'exécutant en tant qu'**Administrateur** (à partir du menu Windows, cliquez avec le bouton droit sur l'icône et choisissez exécuter en tant qu'Administrateur).

### **Étape 1 : Vérifiez votre version et votre statut WSL**

Tout d'abord, assurez-vous que vous utilisez la version 2 de WSL (communément appelée WSL2). La première version est obsolète et WSL2 offre des améliorations significatives. Ouvrez PowerShell (en tant qu'Admin) ou l'invite de commande (en tant qu'Admin) et exécutez :

```powershell
wsl -v

wsl --status
```

Ces commandes affichent la version du client WSL et si votre distribution par défaut utilise WSL 2. Voici la sortie de la commande `wsl -v` :

![Invite de commande affichant la version WSL 2.5.9.0, avec du texte corrompu ou incomplet suivant "Version du noyau :", "Version WSLg :", et d'autres étiquettes de version.](https://cdn.hashnode.com/res/hashnode/image/upload/v1754250376279/ef11af4b-ba5b-43f9-9532-db2634eed154.png align="left")

Et voici la sortie de la commande `wsl --status`.

![Texte de la ligne de commande montrant "C:\Users>wsl --status" avec les informations "Distribution par défaut : Ubuntu" et "Version par défaut : 2".](https://cdn.hashnode.com/res/hashnode/image/upload/v1754250364365/6cea2d97-0796-4320-8f84-58d1b5e62c5e.png align="left")

### **Étape 2 : Listez toutes les distributions installées de manière détaillée**

Pour voir une liste détaillée de vos distributions WSL (y compris la version utilisée par chacune), exécutez :

```powershell
wsl.exe --list --verbose
```

![Sortie de la commande WSL --list --verbose.](https://cdn.hashnode.com/res/hashnode/image/upload/v1754250281542/1826814a-5516-483e-b8ab-6477fd950e21.png align="left")

Ci-dessus, vous pouvez voir la sortie de la commande WSL `--list --verbose`.

Recherchez le nom de votre distribution (par exemple, "Ubuntu") et notez sa version WSL. Si elle indique "Version 2", vous pouvez procéder au compactage.

### **Étape 3 : Localisez le chemin de votre disque dur virtuel Linux (VHDX)**

Les fichiers de chaque distribution WSL résident dans un [fichier VHDX](https://fr.wikipedia.org/wiki/VHD_(format_de_fichier)) sur votre lecteur Windows. Pour trouver le chemin de toute distribution Linux, utilisez ce snippet PowerShell :

```powershell
(Get-ChildItem 

-Path HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss 

| Where-Object { $_.GetValue("DistributionName") -eq 'NOM_DE_VOTRE_DISTRO' }

).GetValue("BasePath") + "\ext4.vhdx"
```

Où vous remplacez `NOM_DE_VOTRE_DISTRO` par le vôtre (Ubuntu, Debian, Kali-linux..). Voici la sortie de la commande affichée ci-dessus dans PowerShell (le chemin du fichier a été anonymisé) :

![Une commande PowerShell est affichée, utilisée pour localiser le fichier ext4.vhdx pour la distribution Ubuntu. La commande récupère le chemin de base du sous-système Windows pour Linux (WSL) pour Ubuntu.](https://cdn.hashnode.com/res/hashnode/image/upload/v1754251303855/ea3b3880-5804-4f50-97c8-327ffd017084.png align="left")

Cette commande lit la clé de registre de votre distribution Linux, puis ajoute "\\ext4.vhdx" pour construire le chemin complet du fichier.

Assurez-vous de copier toute la ligne. Nous en aurons besoin dans les étapes ultérieures.

### **Étape 4 : Arrêtez toutes les instances WSL**

Avant de pouvoir compacter un disque virtuel, assurez-vous que WSL est complètement arrêté. Dans PowerShell ou l'invite de commande (toujours en tant qu'Administrateur), exécutez :

```powershell
wsl.exe --shutdown
```

### **Étape 5 : Compacter le disque dur virtuel Linux à l'aide de DiskPart**

Vous avez réussi à rassembler toutes les informations nécessaires (sur votre système, les distributions disponibles et leur chemin de fichier VHDX) pour procéder à la tâche principale. Dans cette étape, vous procédez effectivement au compactage.

1. Lancez DiskPart dans la même invite élevée (*admin*) :

```powershell
diskpart
```

DiskPart s'ouvrira dans une nouvelle fenêtre. C'est un outil en ligne de commande Windows pour gérer les partitions de disque. Soyez prudent lorsque vous l'utilisez, car des actions incorrectes peuvent entraîner une perte de données sérieuse.

2. Dans l'invite DiskPart, sélectionnez le fichier VHDX que vous avez trouvé précédemment. Remplacez le chemin comme indiqué ci-dessous par votre chemin réel (la ligne que vous avez copiée avant) :

```powershell
select vdisk file="C:\Users\username\AppData\path\to\ext4.vhdx"
```

![Capture d'écran d'une fenêtre d'invite de commande montrant les informations de version de Microsoft DiskPart. Une commande est entrée pour sélectionner un fichier de disque virtuel, et un message confirme la sélection réussie.](https://cdn.hashnode.com/res/hashnode/image/upload/v1754251748072/91795798-0896-4fcc-994c-0ab311955bee.png align="left")

Ci-dessus se trouve la sortie de la commande select vdisk (certaines données ont été anonymisées).

3. Attachez le disque virtuel en mode lecture seule :

Le compactage doit uniquement analyser les blocs vides dans le fichier, sans écrire dans le système de fichiers Linux à l'intérieur. Le mode lecture seule garantit que DiskPart n'inspecte que les blocs pour le zéro-remplissage sans aucune chance d'endommager ou d'altérer votre système de fichiers Linux.

```powershell
attach vdisk readonly
```

![Invite de commande montrant la sortie pour "DISKPART> attach vdisk readonly" avec un message d'attachement réussi.](https://cdn.hashnode.com/res/hashnode/image/upload/v1754251937734/a90af720-1511-42cc-bc37-63439d855907.png align="left")

Vous pouvez voir sur la capture d'écran ci-dessus que le disque dur virtuel a été attaché avec succès.

4. Compacter le disque :

Cela libère l'espace disque en réduisant la taille physique du fichier `.vhdx` pour correspondre aux **données réellement utilisées** à l'intérieur.

```powershell
compact vdisk
```

Cette opération peut prendre un certain temps. Lorsque vous voyez le message « DiskPart a compacté avec succès le fichier de disque virtuel », passez à l'étape suivante. Dans l'image ci-dessous, le disque dur virtuel a été compacté avec succès.

![Sortie du terminal montrant "DISKPART> compact vdisk" avec "100 pour cent terminé," indiquant un compactage réussi du fichier de disque virtuel.](https://cdn.hashnode.com/res/hashnode/image/upload/v1754252148605/51cc9739-775b-4a84-a526-7c2a6d2a9722.png align="left")

5. Détachez le disque virtuel :

```powershell
detach vdisk
```

![Invite de commande montrant "DISKPART> detach vdisk" et un message de confirmation indiquant que DiskPart a détaché avec succès le fichier de disque virtuel.](https://cdn.hashnode.com/res/hashnode/image/upload/v1754252460797/e29387d7-4f03-4ddb-80f7-f14a5051b0fe.png align="left")

Voilà – le disque dur virtuel a été détaché avec succès.

Cette commande libère tous les verrous sur le disque virtuel et le démonte effectivement. Si vous n'utilisez pas cette commande, le fichier reste "en cours d'utilisation", empêchant WSL (ou vous) d'y accéder jusqu'à ce que vous redémarrez ou le fermiez manuellement.

6. Quittez DiskPart :

```powershell
exit
```

### **Étape 6 : Redémarrez WSL et vérifiez**

De retour dans PowerShell ou l'invite de commande, vous pouvez relancer votre distribution :

```powershell
wsl -d NOM_DE_VOTRE_DISTRO
```

Vous pouvez même essayer la commande Unix `df -h` dans votre invite WSL pour vérifier vos nouveaux espaces disque disponibles.

Félicitations, vous venez d'accomplir une tâche de maintenance qui peut libérer des gigaoctets de stockage au fil du temps. Maintenant, il est temps d'automatiser.

![Un bouton rectangulaire blanc minimaliste avec un câble sur une surface rose.](https://cdn.hashnode.com/res/hashnode/image/upload/v1754321783829/4325a626-806e-47e7-9147-a76f4c91a93a.jpeg align="center")

## **Partie 2 : Comment faciliter votre vie avec l'automatisation**

Puisqu'il est souvent difficile de se souvenir exactement où se trouve votre distribution WSL et que vous ne l'utiliserez probablement pas très souvent, ce script PowerShell automatisera l'ensemble du processus que nous avons couvert dans la partie 1. Voici un aperçu des étapes que vous suivrez :

* Détecter les distributions WSL installées.

* En sélectionner une (et gérer les cas où il y en a plus d'une).

* Localiser le fichier `ext4.vhdx` correspondant.

* Arrêter WSL et utiliser DiskPart pour compacter le disque virtuel.

### **Prérequis**

* Windows 10 (20H1/2004+) ou Windows 11 avec WSL 2 activé.

* PowerShell ou l'invite de commande (en tant qu'Administrateur).

Vous aurez également besoin d'un éditeur de code. Le bloc-notes Windows suffit pour accomplir cette tâche. Vous pouvez également utiliser un IDE (Environnement de Développement Intégré) comme VS Code ou un ISE (Environnement de Script Intégré) comme PowerShell ISE (inclus avec Windows).

Pour tester le script, téléchargez-le depuis [GitHub](https://github.com/brooks-code/WSL-VHDX-Compact/blob/main/wsl_compactor.ps1). Ouvrez un PowerShell ou une invite de commande élevée et naviguez jusqu'au dossier du script. Avec simplement la commande ci-dessous, vous pourrez l'exécuter et libérer de l'espace disque :

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\wsl_compactor.ps1
```

### **Étape 1 : Découvrez les distributions WSL2 installées**

L'un des principaux défis est de trouver les distributions Linux disponibles sur le système hôte. Vérifions le premier bloc et voyons de quoi il s'agit :

```powershell
$lxssKey = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss'
$distros = Get-ChildItem $lxssKey | ForEach-Object {
    $p = Get-ItemProperty $_.PSPath
    [PSCustomObject]@{
        Name     = $p.DistributionName
        BasePath = $p.BasePath
    }
}
```

WSL enregistre chaque distribution sous cette clé de registre Windows :

`HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss`

Chaque sous-clé a deux valeurs importantes :

* **DistributionName** (par exemple, Ubuntu)

* **BasePath** (C'est là que sont stockés les fichiers de la distribution. C'est le répertoire qui contient le fichier `ext4.vhdx`.)

Le script utilise `Get-ChildItem` et `Get-ItemProperty` pour énumérer ces sous-clés et construire une liste des distributions Linux disponibles.

```powershell
if ($distros.Count -eq 0) {
Throw-And-Exit "Aucune distribution WSL trouvée dans le registre."
}
```

Si aucune distribution n'est trouvée, le script se termine et affiche ce message d'erreur sur le terminal : `"Aucune distribution WSL trouvée dans le registre."`

### **Étape 2 : Sélectionnez une distribution à compacter**

Ici, le processus comporte deux étapes :

* Si plusieurs distributions sont trouvées, il affiche toutes les distributions avec un menu numéroté et vous invite à en choisir une :

```powershell
if ($distros.Count -gt 1) {
    Write-Host "Plusieurs distributions détectées. Veuillez en choisir une :`n"

    for ($i = 0; $i -lt $distros.Count; $i++) {
        Write-Host "[$($i+1)] $($distros[$i].Name)"
    }
    $selected = $distros[[int]$choice - 1]
}
```

Le menu calculé ressemblera à ceci :

```markdown
Plusieurs distributions détectées. Veuillez en choisir une :

[1] Ubuntu 20.04

[2] Debian

[3] Alpine
```

* Si une seule distribution est trouvée sur le système hôte, le script la sélectionne automatiquement :

```powershell
else {
$selected = $distros[0]
}
```

Lors de la configuration d'une distribution, qu'elle soit choisie manuellement par l'utilisateur ou sélectionnée automatiquement, **l'information importante est le chemin vers le disque dur virtuel de chaque distribution**. Ce chemin est enregistré dans deux variables principales : `'distro'` (qui identifie la distribution spécifique) et `'basePath'` (qui montre où se trouve son disque virtuel).

```powershell
$distro = $selected.Name
$basePath = $selected.BasePath

Write-Host "`nDistribution sélectionnée : $distro" -ForegroundColor DarkYellow
Write-Host "BasePath : $basePath"
```

Les lignes ci-dessus affichent une sortie qui ressemble à ceci :

```markdown
Distribution sélectionnée : Ubuntu (ou toute autre distribution)
BasePath : C:\Users\<Nom_utilisateur>\AppData\Local\Packages\026
```

Comme pour toutes les autres étapes, il est important de prendre en compte le cas où quelque chose ne va pas, en lançant une erreur et en quittant le programme :

```powershell
if (-not (Test-Path $basePath)) {
Throw-And-Exit "Le BasePath '$basePath' n'existe pas sur le disque."
}
```

### **Étape 3 : Localisez le fichier ext4.vhdx**

Dans la première étape, nous avons collecté les informations nécessaires sur les distributions disponibles et où elles sont stockées sur le système Windows. En choisissant une entrée (soit manuellement, soit automatiquement), nous pouvons trouver le bon fichier. Parfois, le fichier ext4 est situé entre le chemin de base et un dossier *LocalState*. Ce script gère les deux situations. Il construit les emplacements habituels où le fichier peut être trouvé.

Ils ressemblent à ceci :

* `$BasePath\ext4.vhdx`

* `$BasePath\LocalState\ext4.vhdx`

Cela peut se traduire par quelque chose comme ceci sur votre système (option 1) :

```markdown
C:\Users\Alice\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\ext4.vhdx
```

ou comme ceci (option 2) :

```markdown
C:\Users\Alice\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\ext4.vhdx
```

(Vous pourriez découvrir que votre distribution WSL2 est située dans un autre répertoire que "Packages" – mais ne vous inquiétez pas, votre BasePath correspondra aux bons dossiers).

L'idée est de construire les deux options de chemin possibles :

```powershell
$possible = @(
Join-Path $basePath 'ext4.vhdx'
Join-Path $basePath 'LocalState\ext4.vhdx'
)
```

Et de choisir la première qui contient effectivement le fichier :

```powershell
$vhdx = $possible | Where-Object { Test-Path $_ } | Select-Object -First 1
```

Encore une fois, nous lançons un message d'erreur si aucun fichier approprié n'est trouvé :

```powershell
if (-not $vhdx) {
Throw-And-Exit "Aucun ext4.vhdx trouvé sous '$basePath'."
}
```

### **Étape 4 : L'invite de confirmation**

Les outils de gestion de disque nécessitent de la prudence et vous devez comprendre les conséquences potentielles de vos actions. Une invite de confirmation est toujours une bonne mesure de sécurité pour prévenir la perte de données accidentelle ou les modifications indésirables du système.

Avant de procéder, le script vous montre :

* un nom de distribution

* son BasePath

* le chemin du fichier VHDX

```powershell
Write-Host "`nSur le point de compacter cette distribution WSL :" -ForegroundColor Magenta
Write-Host " Distribution : $distro"
Write-Host " BasePath : $basePath"
Write-Host " Fichier VHDX : $vhdx`n"
```

Il vous demande ensuite **"Êtes-vous sûr de vouloir continuer ? (O/N)"** :

```powershell
Write-Host "Êtes-vous sûr de vouloir continuer ? (O/N) " -ForegroundColor DarkCyan -NoNewline

# Puis lit la réponse
$answer = Read-Host
```

Vous êtes ensuite invité à taper O (insensible à la casse) pour continuer ou autre chose pour annuler.

```powershell
if ($answer.ToUpper() -ne 'O') {
    Write-Warning "Opération annulée"
    exit
}
```

Pour les deux étapes ci-dessus, j'ai dû utiliser une astuce pour imprimer la question en couleur mais une option simple (sans couleurs) pourrait être :

```powershell
if ((Read-Host 'Êtes-vous sûr de vouloir continuer ? (O/N)').ToUpper() -ne 'O') { 
    Write-Warning 'Opération annulée'
    exit 
}
```

### **Étape 5 : Arrêtez WSL et compacter**

Avant de procéder à l'utilitaire DiskPart, il est important d'arrêter toutes les instances WSL en cours d'exécution. Passez la commande d'arrêt directement dans PowerShell.

```powershell
Write-Host "Arrêt de WSL…" -ForegroundColor Cyan
wsl.exe –shutdown
```

Une erreur courante est d'oublier de lancer PowerShell ou l'invite de commande avec les droits d'administrateur. Vous pouvez prévenir ce cas avec un message :

```powershell
if ($LASTEXITCODE -ne 0) {
     Throw-And-Exit "Échec de l'arrêt de WSL (code de sortie $LASTEXITCODE). Exécutez-vous en tant qu'administrateur ?"
}
```

### **Étape 6 : Exécutez un script DiskPart**

#### Construction du script :

Le processus est le même que dans la partie manuelle, mais cette fois, nous « injectons » les commandes DiskPart prêtes à l'emploi dans le script.

```powershell
$dpScript = @"
select vdisk file="$vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit
"@
```

Avant de lancer, il y a deux étapes que vous devez suivre :

1. Le script PowerShell écrit les lignes ci-dessus dans un fichier temporaire :

```powershell
$tempFile = [IO.Path]::GetTempFileName()
Set-Content -LiteralPath $tempFile -Value $dpScript -Encoding ASCII
```

Cela équivaut aux commandes passées dans la partie manuelle :

`select vdisk file="`[`C:\`](/home/C:/)`026\ext4.vhdx" # chemin complet vers le fichier vdisk`

`attach vdisk readonly`

`compact vdisk`

`detach vdisk`

`exit`

2. Le compactage peut prendre un certain temps, surtout si vous n'avez jamais désencombré votre disque virtuel auparavant. Il est judicieux d'afficher un avertissement avant de procéder :

```powershell
Write-Host "Exécution de DiskPart pour compacter le VHDX. Soyez patient, cela peut prendre un certain temps..." -ForegroundColor Cyan
```

#### **Invoquer DiskPart :**

```powershell
# Exécute DiskPart avec le script sauvegardé dans le fichier temporaire et traite chaque ligne de sortie à son arrivée
diskpart /s $tempFile | ForEach-Object {
    # Prend tout message de type "NN pour cent" de la ligne
    if ($_ -match '(\d+)\s+percent') {
        # N'imprime que lorsque le pourcentage change réellement
        Write-Host "$($Matches[1])% terminé"
    }
    else {
        # Écho simplement tous les autres types de lignes, mot à mot
        Write-Host $_
    }
}
```

Plusieurs points à noter ici :

* Il exécute `diskpart /s $tempFile` : DiskPart lit et exécute les commandes à partir du fichier temporaire dans la boucle PowerShell pour un traitement à la volée.

* Pour une meilleure expérience utilisateur : le snippet ci-dessous fait le tour de filtrer les valeurs de statut répétées en comparant `$pct` avec le sentinelle `$lastPct`, et n'écrit de nouvelles lignes que lorsqu'elles diffèrent.

Comment ?

Avant d'entrer dans la boucle, nous initialisons :

```powershell
$lastPct avec -1
$lastPct = -1 # Nous initialisons une valeur sentinelle
```

Nous avons une valeur « première » garantie qu'aucun pourcentage réel (0–100) n'égalera. Ainsi, dès que vous voyez le premier 0 pour cent, 10 pour cent, ou autre, il diffère de -1.

Ensuite :

```powershell
if ($_ -match '(\d+)\s+percent') {
    # Imprime uniquement lorsque le pourcentage change
    Write-Host "$($Matches[1])% terminé"
}
```

Cela garantit que lors de la toute première mise à jour de pourcentage (par exemple « 0 pour cent » ou « 10 pour cent »), `$pct –ne $lastPct` sera `true`, donc il émet la première ligne. Par la suite, `$lastPct` contient le dernier pourcentage réel, et il n'imprime à nouveau que lorsqu'un nouveau pourcentage de progression différent arrive.

La sortie est plus propre :

```markdown
10% terminé
20% terminé
026
```

Sinon, il inonderait l'écran avec des dizaines de mises à jour identiques « 20 pour cent terminé » (par exemple).

Bien sûr, nous gérons le cas des autres valeurs (lignes non pour cent) normalement :

```powershell
else {
    # lignes non pour cent : imprimer mot à mot
    if ($_ -match '\S') {
        Write-Host $_
    }
}
```

Une fois le processus terminé, n'oubliez pas de nettoyer le fichier temporaire.

```powershell
Remove-Item $tempFile -ErrorAction SilentlyContinue
```

À la fin du processus, vous devriez voir quelque chose comme ceci

```markdown
Quitter DiskPart...
```

D'accord, c'est tout pour le script ! Si vous avez collecté tous les extraits jusqu'à présent, enregistrez-les simplement avec une extension de fichier `.ps1`, ou téléchargez l'exemple complet depuis ce [dépôt GitHub](https://github.com/brooks-code/WSL-VHDX-Compact).

### **Utilisation :**

Vous avez maintenant une compréhension complète de ce qui se passe. Prêt à commencer ? Dans Windows, ouvrez l'invite de commande ou PowerShell **en tant qu'administrateur.**

* Naviguez jusqu'au répertoire contenant votre script `.ps1`.

* Exécutez le script avec la commande suivante, en remplaçant `<Nom_du_fichier_ici>` par votre nom de fichier réel :

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\<Nom_du_fichier_ici>.ps1
```

Les paramètres `-NoProfile -ExecutionPolicy Bypass` lancent PowerShell dans un environnement propre et sans restriction qui ignore les paramètres spécifiques à l'utilisateur et permet l'exécution de scripts sans restrictions de sécurité. Ne vous inquiétez pas, dans ce cas, c'est bon de le faire.

*Attendez...attendez...attendez...*

![Capture d'écran d'une interface de ligne de commande montrant l'exécution d'un script PowerShell pour compacter une distribution WSL (Windows Subsystem for Linux). Le script confirme la distribution sélectionnée "Ubuntu" et procède au compactage du fichier VHDX en utilisant DiskPart. La progression est affichée en incréments de pourcentage, avec des messages finaux indiquant l'achèvement réussi du processus de compactage.](https://cdn.hashnode.com/res/hashnode/image/upload/v1754315563256/a709192a-6626-4a12-b411-46c8591c5eb6.jpeg align="center")

Eh bien bravo ! Vous venez de récupérer tout cet espace inutilisé à l'intérieur de votre WSL2 (presque) sans effort !

Maintenant, vous pouvez aller plus loin en modifiant ce script pour qu'il s'exécute complètement automatiquement, sans l'invite de confirmation (étape 4). Vous pouvez également le planifier comme une tâche de maintenance régulière en utilisant un planificateur de tâches :

```powershell
schtasks /create /tn "Nom_de_la_planification" /tr "powershell.exe -ExecutionPolicy Bypass -File C:\chemin\vers\script.ps1" /sc monthly /d 15 /st 09:00
```

Ceci est un exemple pour une exécution mensuelle où `/d 15` signifie le 15 de chaque mois et `/st 09:00` est une heure de début fixée à 9 heures.

C'est tout ! N'oubliez pas, une maintenance régulière, que vous la fassiez manuellement ou automatiquement, est essentielle pour prévenir une utilisation inutile de l'espace disque et garantir une expérience fluide avec WSL.

### Merci d'avoir lu !

Vous pouvez trouver une liste de mes projets actuels sur [GitHub](https://github.com/brooks-code?tab=repositories).