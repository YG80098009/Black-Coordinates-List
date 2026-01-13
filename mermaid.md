```mermaid

sequenceDiagram
    autonumber

    participant Client as Client / User
    participant A as service-a
    participant B as service-b
    participant DB as Data Storage

    Client->>A: HTTP Request
    A->>A: routes.py\n(handle request)
    A->>A: schemas.py\n(validate data)
    A->>A: services.py\n(business logic)

    A->>B: Internal API Call
    B->>B: routes.py\n(handle request)
    B->>B: schemas.py\n(validate data)
    B->>B: storage.py\n(read/write)

    B->>DB: Save / Fetch data
    DB-->>B: Data result

    B-->>A: Response
    A-->>Client: HTTP Response
