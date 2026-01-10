---
title: Que sont les Data Transfer Objects ? Apprenez à utiliser les DTO dans vos projets
  Java basés sur Spring
subtitle: ''
author: Augustine Alul
co_authors: []
series: null
date: '2025-08-19T17:54:10.850Z'
originalURL: https://freecodecamp.org/news/what-are-dtos-java
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755626027353/feb7f6b6-4841-4559-a976-e73c708c7153.png
tags:
- name: Java
  slug: java
- name: Springboot
  slug: springboot
- name: dto
  slug: dto
- name: Security
  slug: security
seo_title: Que sont les Data Transfer Objects ? Apprenez à utiliser les DTO dans vos
  projets Java basés sur Spring
seo_desc: High performance and privacy are at the heart of most successful software
  systems. No one wants to use a software service that takes a ridiculous amount of
  time to load – and no company wants their users’ data exposed at the slightest vulnerability.
  ...
---

La haute performance et la confidentialité sont au cœur de la plupart des systèmes logiciels réussis. Personne ne souhaite utiliser un service logiciel qui met un temps fou à charger – et aucune entreprise ne veut voir les données de ses utilisateurs exposées à la moindre vulnérabilité. C'est pourquoi les DTO sont un sujet crucial à comprendre pour les ingénieurs logiciels.

L'utilisation des DTO est particulièrement utile lors de la création d'applications contenant des données sensibles comme des dossiers financiers ou médicaux. Lorsqu'ils sont utilisés correctement, les DTO peuvent empêcher l'exposition de champs sensibles côté client. Dans les systèmes critiques, ils permettent de renforcer davantage la sécurité et de réduire les conditions d'échec en garantissant que seuls les champs valides et requis sont acceptés.

Dans cet article, vous apprendrez ce que sont les DTO, pourquoi ils sont importants et les meilleures façons de les créer pour vos applications basées sur Spring.

## Prérequis

Ce tutoriel est d'un niveau légèrement avancé. Pour mieux le comprendre, vous devriez avoir des connaissances solides des concepts Java tels que les objets, les getters et setters, ainsi que de Spring/Spring Boot. Vous devriez également avoir une bonne compréhension du fonctionnement général des logiciels.

## Table des matières

* [Qu'est-ce qu'un DTO ?](#heading-quest-ce-quun-dto)
    
* [Comment créer un DTO pour une application Spring](#heading-comment-creer-un-dto-pour-une-application-spring)
    
* [Comment créer des DTO à partir de deux ou plusieurs objets](#heading-comment-creer-des-dto-a-partir-de-deux-ou-plusieurs-objets)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce qu'un DTO ?

DTO signifie Data Transfer Objects (Objets de Transfert de Données). Il s'agit d'un patron de conception logiciel (design pattern) qui assure le transfert d'objets de données personnalisés et simplifiés entre les différentes couches d'un système logiciel.

![Image montrant le cycle de vie du DTO dans un système logiciel](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfY0uhU1igdbtYzBocBZFOY37O2IjXOD5wCJ26DS0B3U6SZnIswn1n8kWi7ZKL5tQfSQjAZR7ecJ-5Aavop5iB3meJA5ywuKlv7fChG2Oq1_fxNtNW_8RijTFQx2d1ZG-A5y5uYag?key=3uLKQHZqj2e_zuUsBBBZwg align="center")

Source de l'image [ici](https://www.linkedin.com/pulse/clean-spring-boot-apis-separating-entities-dtos-mappers-fabio-ribeiro-zrn9f?utm_source=share&utm_medium=member_ios&utm_campaign=share_via) | Fabio Ribeiro

La direction du transfert de données avec les DTO à travers les différentes couches logicielles est bidirectionnelle. Les DTO sont soit utilisés pour transporter des données entrant d'un client/utilisateur externe vers le logiciel, soit construits et utilisés pour transporter des données sortant du logiciel.

Les DTO ne contiennent que des données de champs, des constructeurs et les méthodes getter et setter nécessaires. Ce sont donc des Plain Old Java Objects (POJOs).

Vous pouvez voir le flux bidirectionnel dans l'image ci-dessous :

![Image montrant le flux bidirectionnel du DTO dans un système logiciel, circulant du contrôleur vers la base de données et de la base de données vers le contrôleur](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdHient8hAwmq3b3KhZi2tNuh0n_1ZuIFJxef1VnM_R5K4KoC0gjeZAF1vZ1d1_lliWKmltiNhhtlfCpadydurab8dNkfLQiru1wGcl2Egak-_3-IYI_n5adrbcrU-4ezKIVERU?key=3uLKQHZqj2e_zuUsBBBZwg align="left")

Source de l'image [ici](https://www.linkedin.com/pulse/clean-spring-boot-apis-separating-entities-dtos-mappers-fabio-ribeiro-zrn9f?utm_source=share&utm_medium=member_ios&utm_campaign=share_via) | Fabio Ribeiro

### Pourquoi utiliser des DTO ?

#### 1. Confidentialité des données

Dans Spring Boot, les entités servent de modèle pour créer des objets de données. Ces entités sont des classes annotées avec `@Entity` et correspondent à une table de base de données. Une instance de la classe d'entité représente une ligne ou un enregistrement de la base de données, tandis qu'un champ dans la classe d'entité représente une colonne de la base de données.

Lors de l'inscription à un service ou produit logiciel, l'utilisateur peut être invité à fournir des données sensibles et non sensibles pour le bon fonctionnement de l'application. Ces données sont conservées sous forme de champs par la classe d'entité et enfin mappées et persistées dans la base de données.

Lorsque nous devons récupérer des données de la base de données et les exposer via un point de terminaison API basé sur la requête fournie – par exemple, une requête pour récupérer un enregistrement utilisateur ou une entité – Jackson (la dépendance de sérialisation couramment utilisée dans les applications basées sur Spring) sérialise tous les champs de données contenus dans l'entité utilisateur récupérée. Maintenant, imaginez que vous avez une entité `User` qui contient des champs tels que le mot de passe, les détails de la carte de crédit, la date de naissance, l'adresse du domicile et d'autres données sensibles que vous ne voudriez pas révéler lors de la sérialisation de l'entité `User`. Eh bien, c'est là que les DTO interviennent.

Avec les DTO, vous pouvez récupérer l'entité complète (contenant à la fois les données sensibles et non sensibles) de la base de données, créer une classe personnalisée (par exemple `UserDTO.java`) qui ne contient que les champs non sensibles que vous estimez sûrs à exposer, et enfin, mapper l'entité récupérée en base de données vers l'objet `UserDTO` sécurisé. De cette façon, c'est le `UserDTO` qui est sérialisé et exposé via l'API, et non l'entité complète – gardant ainsi les données sensibles confidentielles.

#### 2. Amélioration des performances logicielles

Les DTO peuvent améliorer les performances de votre application logicielle en réduisant le nombre d'appels API pour la récupération de données. Avec les DTO, vous pouvez renvoyer des données sérialisées provenant de plusieurs entités en un seul appel API.

Supposons que dans votre application Spring Boot, il existe des entités `User` et `Follower`, et que vous souhaitiez renvoyer les données de l'utilisateur ainsi que ses abonnés. Typiquement, Jackson ne peut sérialiser qu'une seule entité à la fois, soit `User`, soit `Follower`. Mais avec un DTO, vous pouvez combiner ces deux entités en une seule et finalement sérialiser et renvoyer toutes les données dans une seule requête, au lieu de construire deux points de terminaison distincts.

Dans la section suivante, je vais vous montrer les différentes façons de créer des DTO pour votre projet Spring Boot avec des implémentations de code.

## Comment créer un DTO pour une application Spring

Il existe deux approches principales pour créer des DTO dans Spring/Spring Boot :

### 1. Création d'objets personnalisés et gestion manuelle du mapping

Cette approche nécessite que vous gériez vous-même le mapping/la transformation de votre entité existante vers l'objet personnalisé (DTO) – c'est-à-dire que vous écriviez le code qui crée le DTO et définit ses champs avec les valeurs présentes dans l'entité. C'est une pratique courante pour les développeurs qui préfèrent un contrôle granulaire, mais cela peut être fastidieux pour les projets à grande échelle.

Suivez les étapes ci-dessous pour créer un `UserDTO` à partir d'une entité `User` :

#### Étape 1 : Créer la classe DTO

Créez un nouveau fichier nommé **UserDTO.java** et écrivez le code ci-dessous :

```java
public class UserDTO {
    private Long id;
    private String firstName;
    private String lastName;
    private String email;

    // Constructeur sans argument
    public UserDTO() {}

    // Constructeur avec tous les arguments
    public UserDTO(Long id, String firstName, String lastName, String email) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
    }

    // Getters et Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
```

La classe `UserDTO` définie ne peut contenir que quatre (4) champs : `id`, `firstName`, `lastName` et `email`. Elle n'est pas capable d'exposer ou de recevoir plus que ce nombre de champs. La classe contient également des méthodes getter et setter pour récupérer et assigner des données aux champs.

#### Étape 2 : Créer des méthodes de mapping dans une classe utilitaire

Créez un nouveau fichier nommé **UserMapper.java** et insérez ce code :

```java
public class UserMapper {

    // Convertir l'Entité en DTO
    public static UserDTO toDTO(UserEntity user) {
        if (user == null) return null;

        UserDTO dto = new UserDTO();
        dto.setId(user.getId());
        dto.setFirstName(user.getFirstName());
        dto.setLastName(user.getLastName());
        dto.setEmail(user.getEmail());
        return dto;
    }

    // Convertir le DTO en Entité
    public static UserEntity toEntity(UserDTO dto) {
        if (dto == null) return null;

        UserEntity user = new UserEntity(); 
        user.setFirstName(dto.getFirstName());
        user.setLastName(dto.getLastName());
        user.setEmail(dto.getEmail());
        return user;
    }
}
```

La classe `UserMapper` est une classe utilitaire qui mappe le `UserEntity` vers un DTO et inversement. C'est ici que le transfert de données bidirectionnel dont j'ai parlé plus tôt entre en jeu. Premièrement, la direction `UserEntity` -> `DTO` implique de récupérer l'enregistrement complet de la base de données et de le transformer en un objet simplifié (sans informations inutiles) avant qu'il ne soit sérialisé et exposé au client.

La direction `DTO` -> `UserEntity` consiste à prendre l'objet du côté client comme entrée dans le système, mais cette fois-ci, pour limiter le client quant au nombre de champs de données qu'il peut transmettre. Cet objet est reçu, mappé vers une entité et sauvegardé dans le système. C'est important lorsque vous ne voulez pas que le client ait accès à certains champs critiques (qui rendraient votre application vulnérable). C'est pourquoi les ingénieurs logiciels disent toujours : "Ne faites pas confiance à l'utilisateur".

Voici un aperçu de ce à quoi ressemble notre `UserEntity` :

```java
import jakarta.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "users")
public class UserEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String firstName;
    private String lastName;

    @Column(unique = true)
    private String email;
    private String password;
    private String phoneNumber;
    private String gender;
    private LocalDate dateOfBirth;
    private String address;
    private String city;
    private String state;
    private String country;
    private String profilePictureUrl;
    private boolean isVerified;
    private LocalDate createdAt;
    private LocalDate updatedAt;

    // Constructeurs
    public UserEntity() {}

    // Getters et Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public LocalDate getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getProfilePictureUrl() {
        return profilePictureUrl;
    }

    public void setProfilePictureUrl(String profilePictureUrl) {
        this.profilePictureUrl = profilePictureUrl;
    }

    public boolean isVerified() {
        return isVerified;
    }

    public void setVerified(boolean verified) {
        isVerified = verified;
    }

    public LocalDate getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDate createdAt) {
        this.createdAt = createdAt;
    }

    public LocalDate getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDate updatedAt) {
        this.updatedAt = updatedAt;
    }
}
```

Dans l'extrait de code ci-dessus, vous pouvez voir que le `UserDTO` ne contient que quatre (4) champs, qui ne sont pas sensibles et peuvent être exposés en toute sécurité lors de la sérialisation. Ces champs sont `id`, `firstName`, `lastName` et `email` – contrairement au `UserEntity`, qui contient à la fois des champs sensibles et non sensibles. Ainsi, le `UserEntity` (non sécurisé à l'exposition) est mappé vers le `UserDTO` (sécurisé à l'exposition). Une fois cela fait, l'objet `UserDTO` peut être sérialisé et renvoyé via un point de terminaison API. Vous comprenez maintenant pourquoi les DTO nous aident à empêcher l'exposition d'informations confidentielles.

### 2. Création d'objets personnalisés et gestion du mapping via une bibliothèque externe

Utiliser une bibliothèque externe signifie ajouter une couche d'abstraction au processus de mapping. La bibliothèque gère les parties fastidieuses du travail pour vous, et c'est souvent le choix préféré pour les projets à grande échelle. Dans cet article, nous utilisons **MapStruct** car elle est populaire et facile à utiliser. Maven sera notre outil de construction (build tool).

#### Étape 1 : Ajouter la dépendance à votre projet

Comme vous utilisez Maven, ouvrez votre fichier `pom.xml` et ajoutez ce code :

```xml
<dependencies>
    <!-- MapStruct API -->
    <dependency>
        <groupId>org.mapstruct</groupId>
        <artifactId>mapstruct</artifactId>
        <version>1.5.5.Final</version>
    </dependency>
</dependencies>
<build>
    <plugins>
        <!-- Plugin de processeur d'annotations -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.10.1</version>
            <configuration>
                <annotationProcessorPaths>
                    <path>
                        <groupId>org.mapstruct</groupId>
                        <artifactId>mapstruct-processor</artifactId>
                        <version>1.5.5.Final</version>
                    </path>
                </annotationProcessorPaths>
            </configuration>
        </plugin>
    </plugins>
</build>
```

Cela aidera à télécharger la dépendance lors de la construction du projet.

#### Étape 2 : Définir votre DTO

Utilisez le fichier `UserDTO.java` fourni à l'étape 1 de la première approche.

#### Étape 3 : Créer l'interface de mapping MapStruct

Créez un fichier nommé **UserMapper.java** et ajoutez-y le code suivant :

```java
import org.mapstruct.Mapper;
import org.mapstruct.factory.Mappers;

@Mapper(componentModel = "spring")
public interface UserMapper {
    UserMapper INSTANCE = Mappers.getMapper(UserMapper.class);
    UserDTO toDTO(UserEntity user);
    UserEntity toEntity(UserDTO userDTO);
}
```

L'interface `UserMapper` contient le champ `INSTANCE` et deux méthodes, à savoir `toDTO` et `toEntity`, qui prennent respectivement des objets de type `UserEntity` et `UserDTO` en arguments. Les implémentations de ces méthodes sont abstraites et gérées par la bibliothèque pour nous.

Vous pouvez maintenant utiliser les méthodes du mapper (`toDTO` et `toEntity`) dans votre Service ou votre Contrôleur.

## Comment créer des DTO à partir de deux ou plusieurs objets

C'est l'une des façons les plus importantes d'utiliser les DTO : créer des DTO à partir de plusieurs entités et les combiner en une seule, afin qu'elles puissent être renvoyées dans un seul appel API ou une seule requête.

Il existe de nombreuses façons d'appliquer cette technique et de créer des DTO de réponse complexes, selon les exigences de votre projet. La forme ou la structure de votre objet de réponse API pourrait ne pas être la même que l'exemple donné dans ce tutoriel – mais le même principe s'applique, à savoir créer des DTO individuels et les combiner en un seul DTO, qui servira finalement de DTO de réponse.

L'exemple ci-dessous n'est pas extrêmement complexe, mais il est suffisant pour vous aider à comprendre comment cela fonctionne afin que vous puissiez exploiter cette technique pour créer des objets de réponse API plus complexes. Cet exemple combinera les DTO d'un médecin (doctor) et de ses rendez-vous (appointments).

#### Étape 1 : Créer les classes DTO

Créez un fichier nommé **DoctorProfileDTO.java** :

```java
public class DoctorProfileDTO {
    private String doctorId;
    private String fullName;
    private String email;
    private String specialization;

   // Constructeur sans argument
   public DoctorProfileDTO() {}

    // Getter et Setter pour doctorId
    public String getDoctorId() {
        return doctorId;
    }

    public void setDoctorId(String doctorId) {
        this.doctorId = doctorId;
    }

    // Getter et Setter pour fullName
    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    // Getter et Setter pour email
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    // Getter et Setter pour specialization
    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }
}
```

Créez-en un autre appelé **AppointmentDTO.java** :

```java
public class AppointmentDTO {
    private String appointmentId;
    private String appointmentDate;
    private String status;
    private String patientName;
    private String patientEmail;

   // Constructeur sans argument
   public AppointmentDTO() {}

    // Getter et Setter pour appointmentId
    public String getAppointmentId() {
        return appointmentId;
    }

    public void setAppointmentId(String appointmentId) {
        this.appointmentId = appointmentId;
    }

    // Getter et Setter pour appointmentDate
    public String getAppointmentDate() {
        return appointmentDate;
    }

    public void setAppointmentDate(String appointmentDate) {
        this.appointmentDate = appointmentDate;
    }

    // Getter et Setter pour status
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    // Getter et Setter pour patientName
    public String getPatientName() {
        return patientName;
    }

    public void setPatientName(String patientName) {
        this.patientName = patientName;
    }

    // Getter et Setter pour patientEmail
    public String getPatientEmail() {
        return patientEmail;
    }

    public void setPatientEmail(String patientEmail) {
        this.patientEmail = patientEmail;
    }
}
```

#### Étape 2 : Créer un DTO composite combinant les deux entités

Créez un fichier nommé **DoctorWithAppointmentsDTO.java** :

```java
import java.util.List;

public class DoctorWithAppointmentsDTO {
    private DoctorProfileDTO doctorProfile;
    private List<AppointmentDTO> appointments;

    // Constructeur sans argument
    public DoctorWithAppointmentsDTO() {}

    // Getter et Setter pour doctorProfile
    public DoctorProfileDTO getDoctorProfile() {
        return doctorProfile;
    }

    public void setDoctorProfile(DoctorProfileDTO doctorProfile) {
        this.doctorProfile = doctorProfile;
    }

    // Getter et Setter pour appointments
    public List<AppointmentDTO> getAppointments() {
        return appointments;
    }

    public void setAppointments(List<AppointmentDTO> appointments) {
        this.appointments = appointments;
    }
}
```

#### Étape 3 : Créer une classe de mapping

Créez une classe mapper **MapperClass.java** contenant la logique de mapping vers la classe **DoctorWithAppointmentsDTO** :

```java
public class MapperClass {

    public DoctorWithAppointmentsDTO toDTO(Doctor doctor, List<Appointment> appointments) {

        DoctorProfileDTO doctorProfile = new DoctorProfileDTO();
        doctorProfile.setDoctorId(doctor.getId());
        doctorProfile.setFullName(doctor.getFullName());
        doctorProfile.setEmail(doctor.getEmail());
        doctorProfile.setSpecialization(doctor.getSpecialization());

        List<AppointmentDTO> appointmentDTOs = appointments.stream().map(appt -> {
            AppointmentDTO dto = new AppointmentDTO();
            dto.setAppointmentId(appt.getId());
            dto.setAppointmentDate(appt.getDate().toString()); 
            dto.setStatus(appt.getStatus().name());
            dto.setPatientName(appt.getPatient().getName());
            dto.setPatientEmail(appt.getPatient().getEmail());
            return dto;
        }).toList();

        DoctorWithAppointmentsDTO doctorWithAppointment = new DoctorWithAppointmentsDTO();
        doctorWithAppointment.setDoctorProfile(doctorProfile);
        doctorWithAppointment.setAppointments(appointmentDTOs);

        return doctorWithAppointment;
    }
}
```

Dans l'exemple ci-dessus, vous pouvez voir que deux DTO distincts (`AppointmentDTO` et `DoctorProfileDTO`) ont été créés avant de créer le DTO composite, `DoctorWithAppointmentsDTO`. La classe DTO composite contient des champs qui détiennent les instances des DTO de rendez-vous et de profil de médecin. La classe mapper prend l'entité `Doctor` et une liste d'entités `Appointment` en arguments, les mappe respectivement vers `DoctorProfileDTO` et `AppointmentDTO`. Enfin, les champs de la classe DTO composite sont définis à l'aide des objets DTO mappés à partir des entités.

Le **DoctorWithAppointmentsDTO**, une fois sérialisé et renvoyé via un point de terminaison, devrait vous donner une sortie comme celle-ci :

```json
{
  "doctorProfile": {
    "doctorId": "abc123",
    "fullName": "Dr. Susan Emeka",
    "email": "suzan.emeka@example.com",
    "specialisation": "Cardiology"
  },
  "appointments": [
    {
      "appointmentId": "appt001",
      "appointmentDate": "2025-07-10T09:00:00",
      "status": "CONFIRMED",
      "patientName": "James Agaji",
      "patientEmail": "james.agaji@example.com"
    },
    {
      "appointmentId": "appt002",
      "appointmentDate": "2025-08-12T07:05:08",
      "status": "CONFIRMED",
      "patientName": "Jane Augustine",
      "patientEmail": "jane.augustine@example.com"
    }
  ]
}
```

## Conclusion

Si vous êtes un ingénieur logiciel soucieux de la confidentialité et de l'efficacité, l'utilisation de DTO dans vos applications est indispensable.

Dans cet article, vous avez appris ce que sont les DTO ainsi que les principales approches pour les créer et les utiliser. Prenez le temps de parcourir les extraits de code fournis et de vous exercer avec eux jusqu'à ce que vous soyez à l'aise pour les implémenter vous-même. Merci de votre lecture.