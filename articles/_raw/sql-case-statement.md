---
title: How to Use the SQL CASE Statement – with Example Challenge
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2022-11-04T14:28:57.000Z'
originalURL: https://freecodecamp.org/news/sql-case-statement
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Sql-case-banner.jpg
tags:
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: "Writing SQL with multiple conditions can be an arduous task, especially\
  \ if you need to make numerous checks. \nFor example, an if () else if () else {}\
  \ check case expression handles all SQL conditionals. If the first condition is\
  \ satisfied, the query ..."
---

Writing SQL with multiple conditions can be an arduous task, especially if you need to make numerous checks. 

For example, an `if () else if () else {}` check case expression handles all SQL conditionals. If the first condition is satisfied, the query stops executing with a return value. The value specified within the else is returned if no condition is satisfied.

In this article, we'll cover:

1. What the SQL CASE statement is and how it works
2. How to solve an exercise using the SQL CASE statement
3. What some important terms mean, like order by, limit, offset, left join and alias.

## SQL CASE Statement Explained

In programming when you have a given set of conditions, you end up using conditionals (`switch` or `if else`) to know which block of code to execute when a condition is met. 

With SQL, you can do this using the CASE statement. You use the CASE keyword together with the WHEN clause to execute a block of conditional statement code. You use a THEN statement to return the result of the expression. If none of the conditions are met, then you use a final ELSE clause to return a fallback result. 

The **SQL CASE statement has the following syntax**:

```sql
CASE
    WHEN conditional_statement1 THEN result1
    .
    .
    .
    .
    WHEN condition_statementN THEN resultN
    
    ELSE result
END;
```

When you use the CASE statement, it has to be followed by a WHEN and THEN the result if the first condition is met. If the first condition is not met it keeps on checking the other conditions until the nth (or final) condition. If that is still not met then the ELSE condition gets executed. 

Also, the ELSE part is optional when using the CASE statement. In scenarios where you don't use it, the query result returns NULL.

## SQL Challenge

In this section, we will take a case study of a real-life scenario to help you learn how to solve a SQL challenge that uses the CASE statement. 

The challenge is one I encountered on Coderbyte, a platform for practicing coding challenges. It was a bit tough to crack, and I will break down the step-by-step process involved in this article.

### What is the challenge?

The challenge involves coming up with a SQL query to return the employee with the third-highest salary from a table. 

You'll need to structure a query to find this employee and return that row. You also have to replace the position of the DivisionID column with the corresponding DivisionName from the table company_divisions. Then you'll need to replace the ManagerID column with the ManagerName if the ID exists in the table and is not NULL.

### What problem does the SQL CASE statement solve in this challenge?

In this challenge, we need the CASE statement to help achieve the followings:

1. Ensure that the MangerID is not NULL.
2. Match the company ManagerID to company ID and return the Name as the ManagerName.
3. Ensure that if no Name is returned, then the name Susan Wall is used as the default ManagerName.

**Here's the expected output:**

<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>DivisionName</th>
        <th>ManagerName</th>
        <th>Salary</th>
    </tr>
    <tr>
      	<td>222</td>
      	<td>Mark Red</td>
      	<td>Sales</td>
        <td>Susan Wall</td>
      	<td>86000</td>
     </tr>
</table>
        		

And here's the data you'll need to solve this challenge:

#### Table 1: company

<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>DivisionID</th>
        <th>ManagerID</th>
        <th>Salary</th>
    </tr>
    <tr>
        <td>356</td>
        <td>Daniel smith</td>
        <td>100</td>
        <td>133</td>
        <td>40000</td>
    </tr>
    <tr>
        <td>122</td>
        <td>Arnold Sully</td>
        <td>101</td>
        <td>null</td>
        <td>60000</td>
    </tr>
    <tr>
        <td>467</td>
        <td>Lisa Roberts</td>
        <td>100</td>
        <td>null</td>
        <td>80000</td>
    </tr>
    <tr>
        <td>112</td>
        <td>Mary Dial</td>
        <td>105</td>
        <td>467</td>
        <td>65000</td>
    </tr>
    <tr>
        <td>775</td>
        <td>Dennis Front</td>
        <td>103</td>
        <td>null</td>
        <td>90000</td>
    </tr>
    <tr>
        <td>111</td>
        <td>Larry Weis</td>
        <td>104</td>
        <td>35534</td>
        <td>75000</td>
    </tr>
    <tr>
        <td>222</td>
        <td>Mark Red</td>
        <td>102</td>
        <td>133</td>
        <td>86000</td>
    </tr>
    <tr>
        <td>577</td>
        <td>Robert Niger</td>
        <td>105</td>
        <td>12353</td>
        <td>76000</td>
    </tr>
    <tr>
        <td>133</td>
        <td>Susan Wall</td>
        <td>105</td>
        <td>577</td>
        <td>110000</td>
    </tr>
</table>
    
        

#### Table 2: company_divisions

<table>
    <tr>
        <th> ID </th>
        <th> </th>
        <th> DivisionName </th>
    </tr>
    <tr>
        <td> 100 </td>
        <td> </td>
        <td> Accounting </td>
    </tr>
    <tr>
        <td> 101 </td>
        <td> </td>
        <td> IT </td>
    </tr>
    <tr>
        <td> 102 </td>
        <td> </td>
        <td> Sales </td>
    </tr>
    <tr>
        <td> 103 </td>
        <td> </td>
        <td> Marketing </td>
    </tr>
    <tr>
        <td> 104 </td>
        <td> </td>
        <td> Engineering </td>
    </tr>
    <tr>
        <td> 105 </td>
        <td> </td>
        <td> Customer Support </td>
    </tr>
</table>

## How to Solve the SQL CASE Statement Challenge

In this section, we will look at the step-by-step process involved in solving the challenge.

### Step 1: Get the third-highest salary

First, you'll need to structure a query to return the third-highest salary. You'll do this by selecting from the company table and ordering by salary (since we're interested in the record with the third-highest salary). 

You can do that like this:

```sql
SELECT *

FROM company

ORDER BY salary DESC limit 1 offset 2;
```

The query returns the employee's row with the third highest salary, as expected.

<table>
    <tr>
     	<th>ID</th>
        <th>Name</th>
        <th>DivisionID</th>
        <th>ManagerID</th>
        <th>Salary</th>   
    </tr>
    <tr>
        <td>222</td>
        <td>Mark Red</td>
        <td>102</td>
        <td>133</td>
        <td>86000</td>
    </tr>
</table>

So what's going on in this query?

`SELECT`: you use the SELECT command with the asterisk (*), also known as a wildcard) to retrieve all columns from the **company** table.

`ORDER BY`: The ORDER BY command orders column(s) in ascending or descending order. SQL orders by ascending (**ASC**) by default, but we will order the salary column by descending (**DESC**). This is because we need the desc salary from the highest to the lowest, that is 110,000 - 40,000.

`limit`: The limit command limits the number of records returned based on the limit's set value. Since we are only interested in just one row, we will set the limit in the query to 1. This ensures that we will get a return value of a single record every time this query gets executed.

`offset`: Using the offset clause here helps you specify the number of rows to skip before the start of actually returning the row from the query. Offset lets us skip the two highest-paid rows (Susan Wall and Dennis Front) and return the third highest-paid (Mark Red).

### Step 2: Replace DivisionID with DivisionName

Now, you need to modify the query by selecting only the columns you need – ID, Name, ManagerID, DivisionName, and Salary. Then you need to replace the DivisionID column with the corresponding DivisionName from the table **company_divisions**.

You can do that like this:

```sql
SELECT c.ID, c.Name, c.ManagerID, c.salary, cd.DivisionName

FROM company as c

LEFT JOIN company_divisions as cd ON c.DivisionId = cd.id

ORDER BY salary DESC limit 1 offset 2;
```

Here's the output:

<table>
    <tr>
     	<th>ID</th>
        <th>Name</th>
        <th>DivisionName</th>
        <th>ManagerID</th>
        <th>Salary</th>   
    </tr>
    <tr>
        <td>222</td>
        <td>Mark Red</td>
        <td>Sales</td>
        <td>133</td>
        <td>86000</td>
    </tr>
</table>

Let's discuss what's going on in the above query:

`LEFT JOIN`: Since records are returned from the left side (company), we will match them using the LEFT JOIN on the right side (company_divisions) using the `company_division.id and company.DivisionID`. 

If a matching record is found, that is the company's id is also present in company division, then the DivisionName column is populated with the actual value from the left join, in our case (Sales). If there is no record, nothing is returned.

`as` (alias): The alias used is a temporary name for the table. So rather than company.name with an alias for the company as c, we can define it as c.name. Using aliases helps improve readability.

### Step 3: Replace ManagerID with ManagerName

We will build on the result of the query from Step 2. We'll use the CASE statement we learned to add conditionals for when the ManagerId is not null and to check if the ManagerId also exists.

The first thing we need to do is check if the company.ManagerID is not null and make sure that the ID exist in the table. We will apply the CASE statement here.

```sql
CASE WHEN c.ManagerID IS NOT NULL 

AND c.ManagerID = c.ID

```

The second part of the CASE statement is to replace the ManagerID column with the ManagerName. Then we'll need to use the THEN block we learnt earlier like this:

```sql
CASE WHEN c.ManagerID IS NOT NULL 

AND c.ManagerID = c.ID

THEN Name ELSE 'Susan Wall' END AS 'ManagerName'
```

Finally, we can now include the CASE block into the already existing code snippet we had from STEP 2. This will look somewhat like this now:

```sql
SELECT c.ID, c.Name, c.salary, cd.DivisionName

CASE WHEN c.ManagerID IS NOT NULL 

AND c.ManagerID = c.ID

THEN Name ELSE 'Susan Wall' END AS 'ManagerName'

FROM company as c

LEFT JOIN company_divisions as cd ON c.DivisionId = cd.id

ORDER BY salary DESC limit 1 offset 2;
```

The result of Step 3 is the expected output – the employee with third-highest salary.

<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>DivisionName</th>
        <th>ManagerName</th>
        <th>Salary</th>
    </tr>
    <tr>
      	<td>222</td>
      	<td>Mark Red</td>
      	<td>Sales</td>
        <td>Susan Wall</td>
      	<td>86000</td>
     </tr>
</table>
        		

## **Wrapping up**

In this article, I hope you learned about the CASE statement in SQL and how to approach a real-world problem using CASE.

You also learned other SQL commands such as SELECT, ORDER BY, LIMIT, OFFSET, LEFT JOIN, and ALIAS.

