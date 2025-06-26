# Executable BDD Demo: Delivery Fee API (Hexagonal Architecture)

This repository is a **template and demonstration** for building robust, testable APIs using **Executable BDD (Behavior-Driven Development)** and the **Hexagonal Architecture (Ports & Adapters)** pattern.

> **Purpose:**
> - This repo is **not** the actual delivery fee implementation, but a foundation for teams to fork and build their own solution.
> - The real delivery fee logic must be implemented in a fork, strictly adhering to the provided BDD specs and architectural boundaries.

---

## Key Features
- **Executable BDD:**
  - BDD scenarios/specs are written in Gherkin and are executable via `behave`.
  - The API is wired to support test endpoints for setting up state and verifying outcomes.
- **Hexagonal Architecture:**
  - Clear separation between domain logic, ports (interfaces), and adapters (infrastructure/mocks).
  - Easily swap between mock and real adapters for testing/production.
- **Forkable Template:**
  - Intended to be forked for actual delivery fee implementation.
  - Ensures all implementations are compliant with the BDD contract.

---

## Structure

```
api/
  adapters/                # Adapters for real and mock infrastructure
  domain/                  # Domain logic and port interfaces
  mock_cart_data_provider.py
  mock_product_data_provider.py
  bdd_routes.py            # BDD-only endpoints for test setup
  api.py                   # App wiring and factories
features/
  delivery_fee.feature     # Executable BDD scenarios
  steps/                   # Step implementations for BDD
```

---

## Getting Started

1. **Fork this repo** to create your own delivery fee implementation.
2. Implement your delivery fee logic in the domain layer, using only the ports.
3. Ensure all BDD scenarios pass using `behave`:
   ```sh
   ./run_bdd.sh
   ```
4. Wire up your own adapters for production (real data) and testing (mocks).

---

## Philosophy

- **Executable BDD as a contract:**
  - The `.feature` files define the contract for delivery fee calculation.
  - Your implementation must pass these scenarios.
- **Hexagonal Architecture:**
  - Domain logic is isolated from infrastructure.
  - Adapters plug into ports to provide real or mock data.

---

## How to Use This Repo

- **As a template:**
  - Fork this repo for your delivery fee implementation.
  - Never modify the BDD specs unless you are the contract owner.
- **For compliance:**
  - Your API must pass all BDD scenarios to be considered compliant.
- **For learning:**
  - Study the structure to see how executable BDD and hexagonal architecture work together.

---

## License

This repository is provided as a template for delivery fee calculation projects using executable BDD and hexagonal architecture. Fork and modify as needed for your implementation.
