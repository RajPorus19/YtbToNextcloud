# Flask App with Scheduled Functions

A Flask application that runs scheduled functions every 1 hour and every 2 hours using APScheduler. The application follows a modular architecture with business logic separated into services.

## Features

- Flask web application with REST API endpoints
- Background scheduler using APScheduler
- Function that runs every 1 hour
- Function that runs every 2 hours
- Docker support with Ubuntu base image
- Health check and job monitoring endpoints
- Modular architecture with separated business logic
- Configuration management with environment variables

## Project Structure

```
YtbToNextcloud/
├── app.py                    # Main application entry point
├── services/                 # Business logic and services
│   ├── __init__.py          # Package initialization
│   ├── app_factory.py       # Flask application factory
│   ├── config.py            # Application configuration
│   ├── routes.py            # API routes and endpoints
│   ├── scheduler_config.py  # Scheduler management
│   ├── scheduler_service.py # Business logic functions
│   └── README.md           # Services documentation
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
└── README.md              # This file
```

## API Endpoints

- `GET /` - Home page with app status
- `GET /health` - Health check endpoint
- `GET /jobs` - List all scheduled jobs
- `GET /trigger-1h` - Manually trigger the 1-hour function
- `GET /trigger-2h` - Manually trigger the 2-hour function
- `GET /scheduler/status` - Get detailed scheduler status
- `POST /scheduler/start` - Start the scheduler
- `POST /scheduler/stop` - Stop the scheduler

## Running with Docker

### Using Docker Compose (Recommended)

```bash
# Build and run the application
docker-compose up --build

# Run in background
docker-compose up -d --build
```

### Using Docker directly

```bash
# Build the image
docker build -t flask-scheduled-app .

# Run the container
docker run -p 5000:5000 flask-scheduled-app
```

## Running Locally

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Customizing the Scheduled Functions

Edit the `function_every_1h()` and `function_every_2h()` functions in `services/scheduler_service.py` to add your custom logic.

## Configuration

The application supports configuration through environment variables:

- `FLASK_HOST`: Host to bind to (default: 0.0.0.0)
- `FLASK_PORT`: Port to bind to (default: 5000)
- `FLASK_DEBUG`: Enable debug mode (default: False)
- `SCHEDULER_ENABLED`: Enable scheduler (default: True)
- `LOG_LEVEL`: Logging level (default: INFO)

## Monitoring

- Check the application logs to see when functions are executed
- Use the `/jobs` endpoint to see scheduled job details
- Use the `/health` endpoint for health monitoring

## Docker Image Details

- Base image: Ubuntu 22.04
- Python 3 with pip
- Flask 2.3.3
- APScheduler 3.10.4