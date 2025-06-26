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

## Hexagonal Architecture Overview

```
         +----------------------------+
         |        BDD Tests           |
         +----------------------------+
                    |
                    v
         +----------------------------+
         |     HTTP API Endpoints     |
         +----------------------------+
                    |
                    v
         +----------------------------+
         |      Domain Services       |
         |   (Business Logic Only)    |
         +----------------------------+
             ^                ^
             |                |
   +----------------+   +-------------------+
   |   Adapters     |   |    Adapters       |
   | (Mocks/Test)   |   | (Real Data/Infra) |
   +----------------+   +-------------------+
```

---

## Key Concepts & Glossary

- **Hexagonal Architecture (Ports & Adapters):** A software architecture pattern that isolates the domain logic from external systems using ports (interfaces) and adapters (implementations).
- **Executable BDD:** Tests written in Gherkin (`.feature` files) that are run automatically to verify compliance with business requirements.
- **Port:** An interface defining what the domain needs from the outside world (e.g., `CartPort`).
- **Adapter:** Implements a port, connecting the domain to infrastructure (e.g., database, API, or test double).
- **Domain Layer:** Where all business rules and calculations live. No infrastructure code here!

---

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

## How to Implement Your Own Delivery Fee Logic

1. **Fork this repo** to create your own delivery fee implementation.
2. Implement your delivery fee logic in the domain layer (`api/domain/`), using only the ports.
3. Add or update adapters in `api/adapters/` as needed for your real infrastructure.
4. Do not change the BDD `.feature` files unless you are the contract owner.
5. Ensure all BDD scenarios pass using the instructions below.

---

## How to Run the BDD Tests

Run the following command from the project root:

```sh
./run_bdd.sh
```

You should see output indicating whether all BDD scenarios pass. All scenarios must pass for your implementation to be compliant.

---

## Troubleshooting & FAQ

- **Q: Why do BDD tests fail with `Expected total_delivery_fee = 0.0, got 1089.0`?**
  - A: The domain logic is still a placeholder. You must implement the real calculation in `DeliveryFeeService`.
- **Q: How do I switch between mock and real adapters?**
  - A: The wiring in `api.py` uses environment variables (e.g., `ENABLE_BDD_APP=1`) to control which adapters are used.
- **Q: Can I add new endpoints?**
  - A: Add endpoints only if they do not interfere with the contract defined by the BDD specs.

---

## Contribution Guidelines

- Fork the repo before making changes for your delivery fee implementation.
- If you want to improve this template, open a pull request with a clear description.
- Do not alter the BDD `.feature` files unless you are the contract owner.

---

## Further Reading

- [Hexagonal Architecture (Martin Fowler)](https://martinfowler.com/bliki/HexagonalArchitecture.html)
- [Behave Documentation](https://behave.readthedocs.io/en/stable/)
- [Ports and Adapters Explained](https://alistair.cockburn.us/hexagonal-architecture/)

---

## License

This repository is provided as a template for delivery fee calculation projects using executable BDD and hexagonal architecture. Fork and modify as needed for your implementation.
