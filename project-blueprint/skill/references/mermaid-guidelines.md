# Mermaid Diagram Standards & Best Practices

This guide establishes conventions and syntax rules for embedding Mermaid diagrams within Project Blueprint artifacts.

---

## 1. Why Diagrams Are First-Class Citizens

Text-based diagrams embedded in Markdown:
1. Are stored directly in Git history (trackable diffs across versions).
2. Render natively in GitHub, GitLab, IDEs, and modern Markdown viewers.
3. Allow reviewers to spot architectural bottlenecks or circular dependencies faster than reading 10 pages of prose.

---

## 2. Diagram Types by Artifact

### 1. `TRD.md`: System Architecture Block Diagrams
Use `flowchart TD` or `flowchart LR` to represent physical and logical component boundaries:

```mermaid
flowchart TD
    Client["Web Browser (React SPA)"] -->|HTTPS / REST| Gateway["API Gateway / Nginx"]
    Gateway --> Auth["Auth Service"]
    Gateway --> Core["Core Application API"]
    Core --> DB[("PostgreSQL 16")]
    Core --> Cache[("Redis 7 Cache")]
    Core --> Worker["Async Job Worker"]
    Worker --> Queue[("Redis Queue")]
```

### 2. `TRD.md`: Authentication & Payment Handshakes
Use `sequenceDiagram` for complex multi-party interactions:

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Browser
    participant API as Backend API
    participant OAuth as Google OAuth

    User->>Browser: Click "Sign in with Google"
    Browser->>API: GET /auth/google
    API-->>Browser: Redirect to Google Consent URL
    Browser->>OAuth: User authorizes app
    OAuth-->>Browser: Redirect to /auth/callback?code=XYZ
    Browser->>API: POST /auth/callback (code=XYZ)
    API->>OAuth: Exchange code for Access Token
    OAuth-->>API: Return User Profile & Email
    API->>API: Find or create User record
    API-->>Browser: Set HTTP-Only Session Cookie
    Browser->>User: Display Dashboard
```

### 3. `BACKEND_SCHEMA.md`: Entity-Relationship Diagrams
Use `erDiagram` to map relational schemas and foreign keys:

```mermaid
erDiagram
    ORGANIZATION ||--o{ USER : contains
    ORGANIZATION ||--o{ PROJECT : owns
    PROJECT ||--o{ TASK : includes
    USER ||--o{ TASK : assigned_to

    ORGANIZATION {
        uuid id PK
        string name
        string slug UK
        datetime created_at
    }

    USER {
        uuid id PK
        uuid organization_id FK
        string email UK
        string role
    }

    PROJECT {
        uuid id PK
        uuid organization_id FK
        string title
        string status
    }

    TASK {
        uuid id PK
        uuid project_id FK
        uuid assignee_id FK
        string title
        int priority
    }
```

### 4. `APP_FLOW.md`: Navigation & Decision Flowcharts
Use `flowchart TD` with decision diamonds (`{?}`) to map user journeys:

```mermaid
flowchart TD
    Start([User visits site]) --> CheckAuth{Is Authenticated?}
    CheckAuth -- No --> Landing[Landing Page]
    Landing --> LoginModal[Open Login Modal]
    LoginModal --> SubmitCreds[Submit Credentials]
    SubmitCreds --> AuthSuccess{Success?}
    AuthSuccess -- No --> ShowError[Display Error Message]
    ShowError --> LoginModal
    AuthSuccess -- Yes --> Dashboard[User Dashboard]
    CheckAuth -- Yes --> Dashboard
```

---

## 3. Syntax Rules to Prevent Rendering Errors

1. **Quote Node Labels with Special Characters:**
   Always wrap node labels containing parentheses, colons, or brackets in double quotes:
   * ❌ `id[Dashboard (Main View)]`
   * ✅ `id["Dashboard (Main View)"]`
2. **Avoid HTML Tags in Labels:**
   Use plain text inside labels to ensure cross-renderer compatibility.
3. **Partition Large Systems:**
   If a system has more than 15 entities, create one high-level domain diagram plus focused sub-diagrams (e.g. Auth Domain, Invoicing Domain) rather than one unreadable mega-diagram.
