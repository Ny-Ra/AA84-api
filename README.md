## Installation

1. Create virtual environment:
```bash
uv venv
```

2. Install dependencies:
```bash
uv sync
```

3. Configure environment variables in `.env`:
```env
DB_HOST=your-supabase-host
DB_NAME=postgres
DB_USER=your-username
DB_PASSWORD=your-password
```

## Usage

```bash
./run.sh
```

API will be available at http://localhost:8000

## Documentation

- Swagger UI: http://localhost:8000/docs

## Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/v1/users` - List users
- `POST /api/v1/users` - Create user
- `GET /api/v1/items` - List items
- `POST /api/v1/items` - Create item