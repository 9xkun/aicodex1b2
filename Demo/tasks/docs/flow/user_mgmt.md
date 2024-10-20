sequenceDiagram
    participant User
    participant AdminApp
    participant FlaskAPI

    User->>AdminApp: Open Admin App
    AdminApp->>FlaskAPI: Send GET request to /api/users. Params: pagers
    FlaskAPI-->>AdminApp: Return JSON data
    AdminApp-->>User: Display data