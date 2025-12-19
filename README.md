
# 🌐 IP Subnet Calculator (Flask)

A **world-class, modular, and secure open-source web application** for IP and subnet calculations.
Built for **production use**, **recruiter evaluation**, and **security auditor review**.

---

## 🚀 Problem Statement

Modern networks require **accurate, secure, and user-friendly** tools for subnet calculation and IP analysis.
This project delivers a **scalable, extensible, and production-ready solution** for both **IPv4 and IPv6**, with a strong emphasis on:

* Code quality
* Security best practices
* Maintainability
* Professional documentation

---

## 🏗️ Architecture & Tech Stack

* **Python** 3.8+
* **Flask** (Web Framework)

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.x-black)
![License](https://img.shields.io/badge/license-MIT-green)

![Build](https://img.shields.io/github/actions/workflow/status/JosephJonathanFernandes/ip-subnet-calculator-python/ci.yml)
![Coverage](https://img.shields.io/badge/coverage-90%25%2B-brightgreen)
![Code Style](https://img.shields.io/badge/code%20style-black-000000)
![Linting](https://img.shields.io/badge/linting-flake8-blueviolet)
![Security](https://img.shields.io/badge/security-best%20practices-success)


### Project Organization

```
.
├── src/            # Core application logic (SOLID, DRY)
├── config/         # Environment & configuration
├── tests/          # Unit & integration tests (pytest)
├── docs/           # Architecture, changelog, security, contributing
├── scripts/        # Automation & developer utilities
├── .github/        # CI/CD workflows (GitHub Actions)
```

---

## ✨ Features

* ✅ IPv4 and IPv6 subnet calculations
* ✅ Subnet mask, CIDR, wildcard, and host range computation
* ✅ Download calculation results as **CSV**
* ✅ Secure-by-default configuration
* ✅ Modular, testable, and extensible architecture
* ✅ Production-ready documentation and ownership model

---

## ⚡ Quick Start

### 1️⃣ Clone the repository

```bash
git clone https://github.com/JosephJonathanFernandes/ip-subnet-calculator-python
cd ip-subnet-calculator
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set environment variables

```bash
cp config/.env.example config/.env
```

Set a secure secret key inside `config/.env`:

```env
FLASK_SECRET_KEY=your-secure-secret-key
```

### 4️⃣ Run the application

```bash
flask run
```

---

## 🧪 Testing

All core logic is fully tested using **pytest**.

```bash
pytest --cov=src
```

* 🎯 **Coverage Goal:** 90%+ for core logic

---

## 🧹 Linting & Formatting

* **Linting**

```bash
flake8 src/ tests/
```

* **Formatting**

```bash
black src/ tests/
```

* **Pre-commit Hooks**
  See `.pre-commit-config.yaml`

---

## 🔄 CI/CD

Automated using **GitHub Actions** (`.github/workflows/ci.yml`):

* Runs lint checks
* Executes unit & integration tests
* Measures test coverage
* Triggered on every **push** and **pull request**

---

## 🔒 Security

* 🔐 No hardcoded secrets (`.env.example` provided)
* 🛡️ All user input validated and sanitized
* 🌐 Secure HTTP headers enabled by default
* 📄 See [`SECURITY.md`](docs/SECURITY.md) for full security policy

---

## 👥 Ownership & Contribution

* **Maintainers:** Defined in `CODEOWNERS`
* **Contributing:** See [`CONTRIBUTING.md`](docs/CONTRIBUTING.md)

Contributions are welcome and encouraged!

---

## 💡 Project Value

* ⭐ Recruiter- and reviewer-friendly
* 🧩 Clean, maintainable, and extensible codebase
* 🔐 Secure by default
* 🚀 Ready for production and open-source adoption

---

## 📝 Documentation

* `ARCHITECTURE.md` – High-level system design
* `CHANGELOG.md` – Release history
* `CONTRIBUTING.md` – Contribution guidelines
* `SECURITY.md` – Security policy

---

## 🛠️ Developer Experience

* Recommended: **pre-commit** hooks
* Enforced linting & formatting
* Automated CI/CD ensures code quality on every PR

---

## 📄 License

This project is licensed under the **MIT License**.



