# Mini Louie.AI

A starting point for dockerized python web application.

## Recent Updates

- **Code Cleanup (Python Backend)**: The Python backend has been refactored for improved readability and maintainability:
  - Added proper type hints and documentation
  - Separated markdown processing logic into a dedicated class
  - Improved error handling and messages
  - Added API documentation using FastAPI's built-in features
  - Configured proper CORS handling

## Development

### Prerequisites

- Docker
- Docker Compose
- Node.js

### Initialize data set

- `./init-data.sh`

### Frontend

- `cd frontend`
- `npm i`
- `npm run dev`

### Run Server on host

- `uvicorn server.main:app --reload`

### Docker

- `./dc build`
- `./dc up`

To update docker python libraries, add them to environment.yml. Note `./dc` is a convenience alias for `docker compose`.
