# BESSER Platform

Integrated modeling and code generation platform combining Apollon UML editor with BESSER framework.

## Quick Start

1. Clone the repository with submodules: 

bash
git clone --recursive https://github.com/BESSER-PEARL/besser-platform.git
cd besser-platform

2. Start the platform:

bash
docker-compose up

Access:
- Frontend: http://localhost:8888
- Backend API: http://localhost:8000

## Manual Development Setup

If you prefer to run the services separately:

### Frontend (Apollon)
```bash
cd apollon
yarn install
yarn start
```

### Backend (BESSER)
```bash
bash
cd besser
python setup_environment.py
cd besser_backend
python main.py
```

## Repository Structure

- `apollon/` - UML editor frontend (submodule)
- `besser/` - BESSER framework and backend (submodule)