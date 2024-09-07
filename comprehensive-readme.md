# OSINT Research System

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Project Structure](#project-structure)
5. [Setup Instructions](#setup-instructions)
6. [Usage](#usage)
7. [API Documentation](#api-documentation)
8. [Development Guidelines](#development-guidelines)
9. [Testing](#testing)
10. [Deployment](#deployment)
11. [Security Considerations](#security-considerations)
12. [Contributing](#contributing)
13. [License](#license)

## Introduction
The OSINT Research System is a proof-of-concept for an advanced Open-Source Intelligence gathering and analysis tool. It leverages multiple AI models and specialized research tools to provide comprehensive insights on various topics.

## Features
- Multi-model AI research capabilities (OpenAI, Anthropic, Google VertexAI)
- Integration with specialized OSINT tools (Perplexity, Serper, NewsAPI)
- Scalable backend using FastAPI and CrewAI
- React-based frontend for intuitive user interaction
- PostgreSQL database for structured data storage
- Elasticsearch for efficient full-text search and analytics
- Docker containerization for easy deployment and scaling
- Rate-limited API endpoints to prevent abuse
- Interactive API documentation with Swagger UI

## Prerequisites
- Docker Desktop
- Node.js (v14 or later)
- npm (v6 or later)
- Python 3.8+
- Git

## Project Structure
```
osint-research-system/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── research_tools.py
│   │   ├── data_processing.py
│   │   └── security.py
│   ├── tests/
│   ├── alembic/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── auth/
│   │   ├── utils/
│   │   ├── App.js
│   │   └── index.js
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
├── .env.example
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── docs/
    ├── user_guide.md
    ├── api.md
    ├── https_setup.md
    └── cloud_deployment.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/your-repo/osint-research-system.git
   cd osint-research-system
   ```

2. Create a `.env` file in the root directory:
   ```
   cp .env.example .env
   ```
   Edit the `.env` file and fill in your API keys and other configuration values.

3. Build and start the Docker containers:
   ```
   docker-compose up --build
   ```

4. Initialize the database:
   ```
   docker-compose exec backend alembic upgrade head
   ```

5. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API documentation: http://localhost:8000/docs

## Usage
Refer to the [User Guide](docs/user_guide.md) for detailed instructions on how to use the OSINT Research System.

## API Documentation
Interactive API documentation is available at `http://localhost:8000/docs` when the backend is running. This Swagger UI interface allows you to:
- View all available endpoints
- Test API calls directly from the browser
- Understand request and response formats

## Development Guidelines
- Follow PEP 8 style guide for Python code
- Use ESLint and Prettier for JavaScript code formatting
- Write unit tests for new features
- Update documentation when making significant changes

To run linters:
```
# Backend
docker-compose exec backend flake8 .

# Frontend
cd frontend && npm run lint
```

## Testing
Run backend tests:
```
docker-compose exec backend pytest
```

Run frontend tests:
```
cd frontend && npm test
```

## Deployment
For detailed deployment instructions, including setting up HTTPS and deploying to cloud environments, refer to:
- [HTTPS Setup Guide](docs/https_setup.md)
- [Cloud Deployment Guide](docs/cloud_deployment.md)

## Security Considerations
- Keep API keys and secrets secure
- Regularly update dependencies
- Use HTTPS in production
- Implement rate limiting for API endpoints
- Regularly audit and update security measures

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
