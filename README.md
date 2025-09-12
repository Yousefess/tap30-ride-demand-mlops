# 🚖 Tap30 Ride Demand MLOps

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
![Status](https://img.shields.io/badge/status-α%20prototype-orange.svg)

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running Locally](#running-locally)
  - [Deployment](#deployment)
- [Acknowledgements & Sources](#acknowledgements--sources)

---

## About

Tap30 Ride Demand MLOps is a project to predict ride demand for the Tap30 platform (or similar ride-hailing service) by building a full ML pipeline: data ingestion, model training, evaluation, and deployment with operational best practices. The goal is to show how MLOps can be applied end-to-end to solve real forecasting / demand prediction problems.

---

## Features

- 📊 Data preprocessing & feature engineering
- 🔍 Model training + evaluation (forecasting / regression methods)
- 🧪 Versioning of data, models, and experiments
- 🐳 Dockerized environment for reproducibility
- 🌐 (Optional) Web / API interface for inference
- 🛠 CI/CD / pipeline setup for automating major tasks

---

## Project Structure

Here’s a high-level view of how things are organized in the repo:

```

.
├── .github/               # GitHub workflows (CI/CD, linting, etc.)
├── artifacts/             # Saved models, metrics, etc.
├── config/                # Configuration files (yaml / json / etc.)
├── manifests/             # Deployment / orchestration definitions (K8s, etc.)
├── notebook/              # Exploratory analysis / prototyping
├── pipeline/              # Pipeline definitions & workflow orchestration
├── src/                   # Core code (data, models, utilities)
├── web/                   # Web/API interface code
├── Dockerfile
├── docker\_compose.yaml
├── requirements.txt / pyproject.toml
└── setup.py

```

---

## Getting Started

### Prerequisites

Make sure you have:

- Python 3.8+
- Docker & Docker Compose installed
- (Optional) Kubernetes / other orchestration tools if deploying at scale
- (Optional) Access to compute for training (local or cloud)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Yousefess/tap30-ride-demand-mlops.git
   cd tap30-ride-demand-mlops
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) If developer / testing dependencies are needed:

   ```bash
   pip install -r dev-requirements.txt
   ```

### Running Locally

- Explore notebooks in `notebook/` for data exploration and prototyping.

- Run pipeline components via scripts in `pipeline/` + `src/`.

- To test the API / web interface, use Docker / Docker Compose:

  ```bash
  docker-compose up --build
  ```

- Monitor logs, metrics, etc., as configured in the project.

### Deployment

- Use the manifests under `manifests/` for whatever environment (e.g. Kubernetes) you have.
- Ensure Docker images are built and pushed to your registry.
- Set up CI/CD to automate training → evaluation → deployment stages.

---

## Acknowledgements & Sources

I used content from [these video](https://youtube.com/playlist?list=PLnEg28Nx10WELlSW6yzTnbpce4hWCPBlv&si=VzpdcxO-8TOiD869) sources to help build and guide this project.
