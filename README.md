# PMS-DEOM-BACKEND

## Description

This project aim for demonstrating the partial function of PMS manangement system, 
refactoring with modern architecture design, and this is the backend part.

- Frontend: Next.js
- Backend: Django
- DB: Postgresql

Plus, shows how to automate the CI/CD pipeline with Drone CI.


## Setup

### Option1

- Package manager: [Poetry](https://python-poetry.org/)
- Python version Management: [Pyenv](https://github.com/pyenv/pyenv)

- Set python version
```sh
pyenv install 3.12
cd pms_demo_backend
pyenv local 3.12
```

- Install dependencies and launch virtual env
```sh
poetry install
$(poetry env activate)
```

> poetry deprecated `shell` command with version >= 2

### Option2

I also provided requirements.txt for general installation

```sh
pip install -r requirements.txt
```

## Usage

### Login
- `api/token/`
  - method: POST
  - type: JSON
  - field: username, password

### Refresh Token
- `api/token/refresh/`
  - method: POST
  - type: JSON
  - auth: Bearer token
  - field: refresh

### Logout
- `api/token/logout/`
  - method: POST
  - type: JSON
  - auth: Bearer token
  - field: refresh

```
Member fields
1. serial_number
2. card_number
3. username
4. gender
5. phone
6. address
7. photo
8. points
```

### List Member
- `api/member/`
  - method: GET
  - type: JSON
  - auth: Bearer token
  - return: list

### Get One Member
- `api/member/${serial_number}/`
  - method: GET
  - type: JSON
  - auth: Bearer token
  - return: dict
