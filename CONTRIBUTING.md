# Contributing to Google Form Clone

Thank you for your interest in contributing! Bug fixes, new features, and improvements are all welcome.

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/google_form_clone.git
   cd google_form_clone
   ```
3. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Follow the [local setup instructions](README.md#getting-started).

## How to Contribute

### Reporting Bugs

Open a [GitHub Issue](https://github.com/shan19990/google_form_clone/issues) with:
- A clear title and description
- Steps to reproduce
- Expected vs. actual behaviour
- Python/Django version and OS

### Suggesting Features

Open a GitHub Issue with the `enhancement` label and describe the use-case.

### Submitting a Pull Request

1. Keep changes focused — one feature or fix per PR.
2. Write a clear PR description with **what** changed and **why**.
3. Make sure both the backend and frontend run without errors.
4. Reference related issues with `Closes #<issue-number>`.

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/).
- Use Django REST Framework conventions for API views and serializers.
- Never commit `.env` files, secrets, or `db.sqlite3`.

## Security

Please **do not** open public issues for security vulnerabilities. Contact the maintainer directly.
