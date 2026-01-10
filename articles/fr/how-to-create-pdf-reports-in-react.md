---
title: Comment créer des rapports PDF dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-15T20:16:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-pdf-reports-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-from-2020-06-13-17-14-12.png
tags:
- name: React
  slug: react
seo_title: Comment créer des rapports PDF dans React
seo_desc: 'By Adebola Adeniran

  In this article, we''ll be building a button that generates a PDF document (like
  you see above) based on data from an API call.

  A couple of days ago, I built a full stack CRM application to manage communication
  between customers an...'
---

Par Adebola Adeniran

Dans cet article, nous allons créer un bouton qui génère un document PDF (comme vous le voyez ci-dessus) basé sur des données provenant d'un appel API.

Il y a quelques jours, j'ai construit une application CRM full stack pour gérer la communication entre les clients et les agents de support.

J'avais besoin d'un moyen pour que les agents génèrent un résumé des tickets clôturés sous forme de fichier PDF. Après avoir recherché sur Internet un moyen FACILE de faire cela, je peux dire que cet article vous montrera la manière la plus simple qui existe.

Commençons, d'accord ?

## **Installation des packages**

Tout d'abord, installons les packages dont nous avons besoin.

```
npm i jspdf jspdf-autotable
```

## Définir une fonction pour générer les PDF

Ensuite, définissons une fonction que nous pouvons appeler n'importe où pour générer un PDF pour nous. J'ai ajouté beaucoup de commentaires pour vous aider à comprendre ce qui se passe avec chaque ligne.

```
// services/reportGenerator.js

import jsPDF from "jspdf";
import "jspdf-autotable";
// Date Fns est utilisé pour formater les dates que nous recevons
// de notre appel API
import { format } from "date-fns";

// définir une fonction generatePDF qui accepte un argument tickets
const generatePDF = tickets => {
  // initialiser jsPDF
  const doc = new jsPDF();

  // définir les colonnes que nous voulons et leurs titres
  const tableColumn = ["Id", "Titre", "Problème", "Statut", "Clôturé le"];
  // définir un tableau vide de lignes
  const tableRows = [];

  // pour chaque ticket, passer toutes ses données dans un tableau
  tickets.forEach(ticket => {
    const ticketData = [
      ticket.id,
      ticket.title,
      ticket.request,
      ticket.status,
      // appelé date-fns pour formater la date sur le ticket
      format(new Date(ticket.updated_at), "yyyy-MM-dd")
    ];
    // pousser les infos de chaque ticket dans une ligne
    tableRows.push(ticketData);
  });


  // startY est essentiellement margin-top
  doc.autoTable(tableColumn, tableRows, { startY: 20 });
  const date = Date().split(" ");
  // nous utilisons une chaîne de date pour générer notre nom de fichier.
  const dateStr = date[0] + date[1] + date[2] + date[3] + date[4];
  // titre du ticket. et margin-top + margin-left
  doc.text("Tickets clôturés au cours du dernier mois.", 14, 15);
  // nous définissons le nom de notre fichier PDF.
  doc.save(`report_${dateStr}.pdf`);
};

export default generatePDF;
```

## Créer un composant pour sauvegarder les tickets à rendre

Maintenant, créons un simple composant qui récupère et sauvegarde les tickets dans l'état.

```
import React, { useEffect, useState } from "react";
import generatePDF from "../services/reportGenerator";

const Tickets = () => {
  
  const [tickets, setTickets] = useState([]);
  

  useEffect(() => {
    const getAllTickets = async () => {
      try {
        const response = await axios.get("http://localhost:3000/tickets");
        setTickets(response.data.tickets);
      } catch (err) {
        console.log("erreur");
      }
    };
    getAllTickets();
  }, []);

const reportTickets = tickets.filter(ticket => ticket.status === "completed");
  
  return (
    <div>
      <div className="container mb-4 mt-4 p-3">
        <div className="row">
          {user.user.role === "user" ? (
            <> </>
          ) : (
            <button
              className="btn btn-primary"
              onClick={() => generatePDF(reportTickets)}
            >
              Générer un rapport mensuel
            </button>
          )}
        </div>
      </div>
      <TicketsComponent tickets={tickets} />
    </div>
  );
};

export default Tickets;
```

Quelques points concernant notre composant **`<Tickets />`**. Lorsque notre composant se charge, nous faisons une requête à **http://localhost:3000/tickets** pour récupérer tous nos tickets. Nous les sauvegardons ensuite dans l'état **`tickets`**. Et enfin, nous les passons en tant que prop au **`<TicketsComponent />`** pour rendre les tickets dans le DOM.

Nous avons également une variable **`reportTickets`** qui filtre nos tickets pour obtenir uniquement les tickets qui ont le statut **`completed`**.

Remarquez que nous avons également créé le bouton **Générer un rapport mensuel** qui appelle la fonction **`generatePDF()`** que nous avons définie précédemment lorsqu'il est cliqué.

## Créer un composant pour afficher les tickets dans un tableau

Ensuite, définissons notre **`<TicketsComponent />`** qui sera responsable de l'affichage de nos tickets dans un tableau bien présenté. N'oubliez pas qu'il accepte les tickets à afficher en tant que prop du composant **`<Tickets />`**.

```
import React from "react";
import { Link } from "react-router-dom";

const TicketsComponent = ({ tickets }) => {

// une fonction qui attribue des classes de style bootstrap en fonction
// du statut du ticket
  const assignColorToTicketStatus = ticket => {
    if (ticket.status === "completed") {
      return "p-3 mb-2 bg-success text-white";
    } else if (ticket.status === "in_progress") {
      return "p-3 mb-2 bg-warning text-dark";
    } else if (ticket.status === "opened") {
      return "p-3 mb-2 bg-light text-dark";
    }
  };
  return (
    <div className="container">
      {tickets.length === 0 ? (
        "Vous n'avez actuellement aucun ticket créé"
      ) : (
        <table className="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Titre</th>
              <th scope="col">Problème</th>
              <th scope="col">Statut</th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody>
            {tickets.map(ticket => (
              <tr key={ticket.id}>
                <td>{ticket.id}</td>
                <td>{ticket.title}</td>
                <td>{ticket.request}</td>
                <td className={assignColorToTicketStatus(ticket)}>
                  {ticket.status}
                </td>
                <td>
                  <Link to={`/ticket/${ticket.id}`}>Voir les commentaires</Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default TicketsComponent;

```

Maintenant, voyons à quoi ressemble actuellement notre application. Nous avons 10 tickets dans notre état, mais j'en montrerai 6 ici pour plus de commodité.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-51.png)

Comme vous pouvez le voir, nous avons un certain nombre de tickets à différents statuts. Nous avons également notre bouton **Générer un rapport mensuel** qui, lorsqu'il est cliqué, exportera le fichier PDF.

Et c'est tout. Vous devriez obtenir un fichier PDF avec le nom de fichier sous la forme _**report_dddmmyyyy**_ téléchargé dans votre navigateur.

Si cet article vous a aidé, dites bonjour sur [twitter](https://www.freecodecamp.org/news/p/aef1e33f-31a6-4fa3-80e3-ac1e2d49a2e8/twitter.com/debosthefirst).