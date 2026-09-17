# Application & User Flow: Freelance Invoice Manager

## 1. Primary User Journey: Create, Send, and Collect Invoice
This flow traces how an authenticated freelancer creates an invoice draft, publishes a Stripe Checkout session, and receives notification of payment.

## 2. Navigation & Workflow Flowchart

```mermaid
flowchart TD
    Dashboard["Freelancer Dashboard"] --> ClickCreate["Click '+ New Invoice'"]
    ClickCreate --> InvoiceEditor["Invoice Editor Screen (REQ-004)"]
    InvoiceEditor --> SelectClient{"Select or Add Client?"}
    SelectClient -->|Existing| PickClient["Choose Client from Autocomplete"]
    SelectClient -->|New| AddClientModal["Enter Client Details Modal (REQ-003)"]
    AddClientModal --> PickClient
    PickClient --> AddItems["Add Line Items & Tax Rate"]
    AddItems --> SaveDraft["Click 'Save Draft'"]
    SaveDraft --> Preview["Review Invoice Preview"]
    Preview --> Publish["Click 'Publish & Send' (REQ-005)"]
    Publish --> GenLink["System Generates Hosted Stripe Link"]
    GenLink --> EmailClient["Client receives email notification"]
    EmailClient --> ClientVisits["Client opens payment page"]
    ClientVisits --> StripePay["Client submits card in Stripe Checkout"]
    StripePay --> WebhookRecv["Stripe dispatches checkout.session.completed"]
    WebhookRecv --> MarkPaid["Invoice marked PAID (REQ-006)"]
    MarkPaid --> ReceiptSent["Receipt emailed to Client & Freelancer"]
```

## 3. Error Recovery & Edge Case Flows
* **Stripe Payment Cancellation:** If client aborts Checkout, Stripe redirects to `cancel_url`; invoice remains `UNPAID` and available for retry.
* **Network Timeout on Save:** Editor auto-saves drafts to browser `localStorage` to prevent data loss.
