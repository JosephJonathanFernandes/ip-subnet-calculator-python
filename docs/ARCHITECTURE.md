# Architecture Overview

## Problem Statement
Modern networks require accurate, secure, and user-friendly tools for subnet calculation and IP analysis. This project provides a modular, extensible, and production-ready solution for both IPv4 and IPv6.

## High-Level Architecture
- **src/**: Core logic, no Flask or UI dependencies
- **app.py**: Flask entrypoint, imports from src/
- **templates/**: Jinja2 HTML templates
- **config/**: Environment and configuration files
- **tests/**: Unit and integration tests
- **scripts/**: Automation and developer utilities

## Key Modules
- `src/network/validation.py`: Input validation
- `src/network/calculation.py`: Subnet/IP calculations
- `src/network/csv_export.py`: CSV generation
- `src/web/app_factory.py`: Flask app factory

## Security
- No hardcoded secrets
- All user input validated
- Secure HTTP headers set

## Extensibility
- Add new calculation modules in `src/network/`
- Add new endpoints in `src/web/app_factory.py`

## Ownership
- See CODEOWNERS for maintainers

---
For more, see CONTRIBUTING.md and SECURITY.md.
