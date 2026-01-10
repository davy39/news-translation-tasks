---
title: 'Améliorez Votre Projet Bluetooth Avec Cet Outil Précieux : Partie 2 !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-01T07:57:49.000Z'
originalURL: https://freecodecamp.org/news/improve-your-bluetooth-project-with-this-valuable-tool-part-2
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Protocol-Buffers-Part-2.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: protocol-buffers
  slug: protocol-buffers
seo_title: 'Améliorez Votre Projet Bluetooth Avec Cet Outil Précieux : Partie 2 !'
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com.

  This is Part 2 of configuring your own Bluetooth Low Energy Service using a Nordic
  NRF52 series processor. If you haven’t seen Part 1 go back and check it out. I’ll
  be waiting right here...'
---

Par Jared Wolff

**Cet article provient à l'origine de [www.jaredwolff.com.](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-2/)**

Ceci est la Partie 2 de la configuration de votre propre service Bluetooth Low Energy en utilisant un processeur de la série Nordic NRF52. Si vous n'avez pas vu la [Partie 1][part1], retournez la consulter. Je vous attendrai ici...

Si vous êtes avec moi jusqu'à présent, haute cinq. ?

Plongeons-nous dans le vif du sujet !

Jusqu'à présent, nous avons créé une structure de données multiplateforme efficace en utilisant Protocol Buffers. Ce Protocol Buffer en particulier peut être utilisé pour envoyer ces structures de données définies à un service Bluetooth Low Energy. Dans cette partie, je vais vous montrer le fonctionnement interne de la création du service à partir de zéro.

P.S. cet article est long. Si vous voulez quelque chose à télécharger, [cliquez ici pour un PDF magnifiquement formaté.](https://www.jaredwolff.com/files/how-to-define-a-protocol-buffer-ble-service-pdf/) (Bonus supplémentaire, le PDF contient les trois parties de cette série !)


## Création du Service
![Door Peoeple](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-2/images/doorman.jpg)

Travailler avec le Bluetooth Low Energy en général peut sembler écrasant. Comme je l'ai discuté [ici][get-started], il y a quelques éléments mobiles que vous devez garder à l'esprit.

La meilleure façon de créer un nouveau service est de copier un service déjà existant ! Je l'ai fait en :

1. Allant dans le sdk -> components -> ble -> ble_services -> ble_bas
2. Copiant `ble_bas.h` vers `include/ble`
3. Copiant `ble_bas.c` vers `src/ble`

J'ai ensuite renommé ces fichiers de `ble_bas` en `ble_protobuf` pour être cohérent. J'ai également fait de même à l'intérieur des fichiers. (BAS est le service de niveau de batterie utilisé pour rapporter la tension de la batterie ou la charge relative en utilisant un pourcentage)

J'ai également supprimé toutes les fonctions de mesure de la batterie car elles seront remplacées. Cette partie du processus est assez fastidieuse et sujette aux erreurs. Si vous êtes nouveau dans le SDK Nordic, [je vous recommande vivement de télécharger le code exemple pour cet article.][code]

### Ajout d'un UUID

Normalement, pour un service défini par le fournisseur, vous devrez utiliser votre propre UUID. Il existe certaines plages d'UUID qui sont réservées pour le Bluetooth SIG. Supposément, vous pouvez également réserver votre propre UUID si vous êtes membre. [Voici un article utile sur Stack Overflow sur le sujet.](https://stackoverflow.com/questions/10243769/what-range-of-bluetooth-uuids-can-be-used-for-vendor-defined-profiles)

Dans notre cas, j'ai défini un UUID que j'ai utilisé pour d'autres projets. Si vous allez dans `ble_protobuf.h`, vous pouvez voir les UUID pour le service et la caractéristique :

```c
// UUID pour le Service & Char
#define PROTOBUF_UUID_BASE   {0x72, 0x09, 0x1a, 0xb3, 0x5f, 0xff, 0x4d, 0xf6, \
                               0x80, 0x62, 0x45, 0x8d, 0x00, 0x00, 0x00, 0x00}
#define PROTOBUF_UUID_SERVICE     0xf510
#define PROTOBUF_UUID_CONFIG_CHAR (PROTOBUF_UUID_SERVICE + 1)
```

`PROTOBUF_UUID_BASE` et `PROTOBUF_UUID_SERVICE` sont utilisés dans `ble_protobuf_init`. Le dernier est utilisé dans `command_char_add` (je vais le décrire un peu plus bas).

Vous pouvez vous passer de définir un BASE ID, mais je vous recommande vivement de faire l'effort supplémentaire. Ainsi, votre application sera imperméable aux futures mises à jour du protocole Bluetooth.

## Création de la Caractéristique
![Open Those PICKLES!](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-2/images/man-641691_1280.jpg)

Nordic a une méthode assez simple pour initialiser des caractéristiques séparées dans chaque service. Pour chaque caractéristique, il y a une fonction `char_add` qui configure et ajoute ensuite la caractéristique au service.

### Configurez votre Caractéristique avec `ble_add_char_params_t`

Nordic a mis les paramètres de configuration pour une caractéristique BLE dans une structure logique (et utile). Si vous développez sur une autre plateforme, vous pouvez trouver les mêmes paramètres, bien que pas tous au même endroit ! (Ou gérés logiquement... ?)

Voici la décomposition de la structure :

```c
typedef struct
{
    uint16_t                    uuid;
    uint8_t                     uuid_type;
    uint16_t                    max_len;
    uint16_t                    init_len;
    uint8_t *                   p_init_value;
    bool                        is_var_len;
    ble_gatt_char_props_t       char_props;
    ble_gatt_char_ext_props_t   char_ext_props;
    bool                        is_defered_read;
    bool                        is_defered_write;
    security_req_t              read_access;
    security_req_t              write_access;
    security_req_t              cccd_write_access;
    bool                        is_value_user;
    ble_add_char_user_desc_t    *p_user_descr;
    ble_gatts_char_pf_t         *p_presentation_format;
} ble_add_char_params_t;
```

C'est ici que vous informez la pile BLE du type de caractéristique. Dans cet exemple, j'utilise une poignée de paramètres pour définir la caractéristique de commande Protobuf.

`uuid` définit l'adresse de la manière dont la caractéristique sera accessible. Si vous définissez votre propre service.
`max_len` est la longueur maximale des données que vous pouvez envoyer via la caractéristique. C'est pourquoi il est important de définir `max_size` dans votre fichier `.options` de Protocol Buffer pour tous les paramètres de longueur variable. Une fois que vous compilez vos Protocol Buffers, vous obtiendrez une variable `*_size` similaire à celle définie dans `command.pb.h`. Voici un extrait de ce à quoi cela ressemble ci-dessous :

```c
/* Maximum encoded size of messages (where known) */
#define event_size                               67
```

Ainsi, lors de la définition de `ble_add_char_params_t`, je définis `max_len` à `event_size` :

```c
add_char_params.uuid                      = PROTOBUF_UUID_CONFIG_CHAR;
add_char_params.max_len                   = event_size;
add_char_params.is_var_len                = true;
```

Dans la même veine, parce que nous utilisons une *chaîne* comme l'un des paramètres dans le Protocol Buffer, ces données peuvent être de taille variable. `is_var_len` est utile pour s'assurer que le bon nombre d'octets est envoyé et reçu. La fonction de décodage des Protocol Buffers échouera si plus de données sont fournies que nécessaire. (Je l'ai appris à mes dépens !)

`char_props` définit les permissions pour la caractéristique. Si vous êtes familier avec les permissions du système de fichiers sur un ordinateur, cela vous sera naturel. Dans cet exemple, **lecture** et **écriture** sont ce que nous recherchons.

Enfin, les paramètres se terminant par `_access` déterminent le type de sécurité utilisé. Dans la plupart des cas, `SEC_OPEN` ou `SEC_JUST_WORKS` est plus que suffisant. Si vous gérez des données critiques (mots de passe, etc.), vous devrez peut-être implémenter une deuxième couche de chiffrement ou activer un mode de sécurité de niveau supérieur.

Si vous cherchez plus d'informations sur la sécurité Bluetooth Low Energy, [voici un article utile sur le sujet.](https://duo.com/decipher/understanding-bluetooth-security)

### Ajout. dat. char.

Une fois que vous avez défini vos paramètres, il est aussi simple que d'appeler la fonction `characteristic_add`. Cela associera cette nouvelle caractéristique au service lié. Le premier argument est le handle du service, le second les paramètres de configuration et le troisième est un pointeur vers les handles pour la caractéristique. (Voir ci-dessous)

```c
uint32_t characteristic_add(uint16_t                   service_handle,
                            ble_add_char_params_t *    p_char_props,
                            ble_gatts_char_handles_t * p_char_handle)
```

## Mise en Route
Configurer tout dans `ble_protobuf.c` représente 90 % de la bataille. Le dernier kilomètre nécessite quelques bits ajoutés à `services_init` dans `main.c`

```c
    ble_protobuf_init_t       protobuf_init = {0};

    protobuf_init.evt_handler          = ble_protobuf_evt_hanlder;
    protobuf_init.bl_rd_sec            = SEC_JUST_WORKS;
    protobuf_init.bl_cccd_wr_sec       = SEC_JUST_WORKS;
    protobuf_init.bl_wr_sec            = SEC_JUST_WORKS;

    err_code = ble_protobuf_init(&m_protobuf,&protobuf_init);
    APP_ERROR_CHECK(err_code);
```

Ce qui précède permet aux événements d'être redirigés vers le contexte principal. Ainsi, votre application devient beaucoup plus interactive avec la logique centrale de votre code de firmware. Dans les exemples de Nordic, ils ont également sorti les paramètres de sécurité afin qu'ils puissent être définis dans le contexte principal également.

*Note de côté :* `m_protobuf` est défini en utilisant une macro de `ble_protobuf.h`. Il crée non seulement une instance statique du service, mais il définit également le callback qui est utilisé pour gérer les événements.

```c
/**@brief Macro pour définir une instance ble_protobuf.
 *
 * @param   _name  Nom de l'instance.
 * @hideinitializer
 */
#define BLE_PROTOBUF_DEF(_name)                          \
    static ble_protobuf_t _name;                         \
    NRF_SDH_BLE_OBSERVER(_name ## _obs,             \
                         BLE_PROTOBUF_BLE_OBSERVER_PRIO, \
                         ble_protobuf_on_ble_evt,        \
                         &_name)
```

Si vous créez votre propre service, vous devrez mettre à jour le nom de la fonction pour le gestionnaire d'événements. Si vous devez ajuster les priorités, vous pouvez définir/mettre à jour cela également.

## Que se passe-t-il lorsque cette caractéristique est écrite ?
![Smoke Signal](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-2/images/person-629676_1280.jpg)


`ble_protobuf_on_ble_evt` est le principal moyen de gérer les événements dans les services Bluetooth Low Energy. Nous nous intéressons principalement à l'événement `BLE_GATTS_EVT_WRITE`, mais vous pouvez déclencher n'importe quel événement GATT qui vous plaît.

`on_write` est l'endroit où l'action se produit. Il prend les données écrites dans la caractéristique et les décode selon `event_fields`. Tout est mis commodément dans une structure pour un traitement supplémentaire, etc. Si une erreur se produit lors du décodage, `pb_decode` retourne une erreur. Une fois modifiées, les données sont encodées et mises à disposition pour la lecture. Depuis la lecture de la [Partie 1][part1], les appels à `pb_decode` et `pb_encode` devraient vous être très familiers !

Bien sûr, vous pouvez faire en sorte que votre firmware fasse ce que vous voulez. Le monde de l'énergie Bluetooth est votre huître.

## Notes Finales
Lors de l'ajout de nouveaux services à un exemple Bluetooth Low Energy, vous devrez peut-être apporter quelques modifications au code sous-jacent.

Par exemple, `sdk_config.h` peut nécessiter quelques changements. En particulier, `NRF_SDH_BLE_VS_UUID_COUNT` doit être augmenté en fonction du nombre d'UUID de service mis à disposition. Pour ce projet, j'utilise également le service DFU (car il devrait être un défaut pour tous les projets connectés !!)

Un autre aspect important est la gestion de la mémoire et du flash. Le fichier `.ld` par défaut qui accompagne le service BLE DFU peut ne pas être suffisant pour un autre service BLE. La seule façon de savoir qu'il n'y a pas assez de mémoire est lorsque vous compilez et flashez sur un appareil NRF52. Si l'appareil démarre en indiquant qu'il n'y a pas assez de mémoire, vous devrez apporter les modifications suggérées. L'erreur apparaîtra sur la console de débogage où ce message apparaît normalement :

```bash
<info> app: Définition de la table de vecteurs pour le bootloader : 0x00078000
<info> app: Définition de la table de vecteurs pour l'application principale : 0x00026000
```

Apprenez-en plus sur la configuration de la console de débogage [dans le code exemple ici.][code]

## Conclusion
Dans cette partie, je vous ai montré le fonctionnement interne d'un service Bluetooth Low Energy personnalisé utilisant Protocol Buffers. Dans la dernière partie, je vous montrerai comment charger le firmware, exécuter l'exemple d'application javascript et tester notre Protocol Buffer fraîchement développé !


[code]: https://www.jaredwolff.com/files/protobuf/
[part1]: https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf
[get-started]: https://www.jaredwolff.com/get-started-with-bluetooth-low-energy/