"""
Application Factory Module

This module handles the creation and initialization of the Flask application.
It provides a clean factory pattern for app creation and configuration.
"""

from flask import Flask
import logging

from .config import get_config, log_configuration
from .scheduler_config import scheduler_manager
from .routes import register_routes

logger = logging.getLogger(__name__)


def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask: Configured Flask application instance
    """
    # Get configuration
    config = get_config()

    # Create Flask app
    app = Flask(__name__)

    # Configure app
    app.config["DEBUG"] = config.FLASK_DEBUG

    # Register routes
    register_routes(app)

    # Initialize scheduler if enabled
    if config.SCHEDULER_ENABLED:
        scheduler_manager.start()
        logger.info("Scheduler started successfully")
    else:
        logger.info("Scheduler disabled by configuration")

    # Log startup information
    log_startup_info(config)

    return app


def log_startup_info(config):
    """Log startup information."""
    logger.info("=" * 50)
    logger.info(f"Starting {config.APP_NAME} v{config.APP_VERSION}")
    logger.info("=" * 50)

    log_configuration()

    logger.info(f"Scheduled jobs: {scheduler_manager.get_job_count()}")
    for job in scheduler_manager.get_jobs():
        logger.info(f"  Job: {job.name} - Next run: {job.next_run_time}")

    logger.info("=" * 50)


def get_app_config():
    """
    Get the application configuration for external use.

    Returns:
        Config: Application configuration object
    """
    return get_config()
