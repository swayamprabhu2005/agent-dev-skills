# Backend & Database Schema: Freelance Invoice Manager

## 1. Relational Schema Overview
The database uses PostgreSQL with foreign key cascades and UUID primary keys.

## 2. Entity-Relationship Diagram

```mermaid
erDiagram
    ORGANIZATION ||--o{ USER : contains
    ORGANIZATION ||--o{ CLIENT : manages
    ORGANIZATION ||--o{ INVOICE : issues
    CLIENT ||--o{ INVOICE : billed_to
    INVOICE ||--o{ LINE_ITEM : contains
    INVOICE ||--o{ PAYMENT : settles

    ORGANIZATION {
        uuid id PK
        string name
        string stripe_account_id
        datetime created_at
    }

    USER {
        uuid id PK
        uuid organization_id FK
        string email UK
        string role "OWNER or MEMBER"
    }

    CLIENT {
        uuid id PK
        uuid organization_id FK
        string name
        string email
        string address
    }

    INVOICE {
        uuid id PK
        uuid organization_id FK
        uuid client_id FK
        string invoice_number UK
        string status "DRAFT, UNPAID, PAID, CANCELLED"
        decimal subtotal
        decimal tax_rate
        decimal total
        datetime due_date
        datetime paid_at
    }

    LINE_ITEM {
        uuid id PK
        uuid invoice_id FK
        string description
        decimal quantity
        decimal unit_price
        decimal amount
    }

    PAYMENT {
        uuid id PK
        uuid invoice_id FK
        string stripe_checkout_session_id UK
        string stripe_payment_intent_id UK
        decimal amount
        string status
        datetime created_at
    }
```

## 3. Database Constraints & Indexes
* `invoices (organization_id, invoice_number)` has a composite UNIQUE constraint.
* `invoices (status)` is indexed for dashboard status filtering.
* `payments (stripe_checkout_session_id)` has a unique index for webhook deduplication.
