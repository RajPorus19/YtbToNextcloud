# Services Module

This directory contains all the business logic and application services organized in a modular structure.

## Structure

```
services/
├── __init__.py              # Package initialization
├── app_factory.py           # Flask application factory
├── config.py                # Application configuration
├── routes.py                # API routes and endpoints
├── scheduler_config.py      # Scheduler management
├── scheduler_service.py     # Business logic functions
└── README.md               # This file
```

## Modules

### `app_factory.py`
- Creates and configures the Flask application
- Handles application initialization
- Manages the application lifecycle

### `config.py`
- Centralized configuration management
- Environment variable handling
- Application settings

### `routes.py`
- All Flask API endpoints
- HTTP request handling
- Response formatting

### `scheduler_config.py`
- APScheduler configuration and management
- Job scheduling setup
- Scheduler lifecycle management

### `scheduler_service.py`
- Business logic functions
- Scheduled task implementations
- Core application functionality

## Usage

The services are automatically imported and used by the main `app.py` file. Each module has a specific responsibility and follows the Single Responsibility Principle.

## Adding New Business Logic

To add new scheduled functions:

1. Add your function to `scheduler_service.py`
2. Update the `get_scheduled_functions()` function
3. Add the job configuration in `scheduler_config.py`
4. Add any new API endpoints in `routes.py`

## Configuration

Environment variables can be used to configure the application:

- `FLASK_HOST`: Host to bind to (default: 0.0.0.0)
- `FLASK_PORT`: Port to bind to (default: 5000)
- `FLASK_DEBUG`: Enable debug mode (default: False)
- `SCHEDULER_ENABLED`: Enable scheduler (default: True)
- `LOG_LEVEL`: Logging level (default: INFO) 