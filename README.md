# Trello Clone Backend

### Ejemplos de Consultas y Mutaciones

#### Get all Cards

```graphql
{
  cardsByStatus {
    id
    title
    description
    status
  }
}
```

#### Get all Cards with a specific status

```graphql
{
  cardsByStatus(status: [TO_DO, DONE]) {
    id
    title
    description
    status
  }
}
```

```graphql
{
  cardsByStatus(status: [IN_PROGRESS]) {
    description
    status
  }
}
```

#### Crear una Card

```graphql
mutation {
  createCard(id: "1", title: "Task 1", description: "Description for task 1", status: "To Do") {
    card {
      id
      title
      description
      status
    }
  }
}
```

#### Consultar una Card
```graphql
{
  card(id: "1") {
    id
    title
    description
    status
  }
}

```

#### Actualizar una Card
```graphql
mutation {
  updateCard(id: "1", title: "Updated Task 1", description: "Updated description", status: "In Progress") {
    card {
      id
      title
      description
      status
    }
  }
}
```

#### Eliminar una Card
```graphql
mutation {
  deleteCard(id: "1") {
    card {
      id
      title
      description
      status
    }
  }
}
```

