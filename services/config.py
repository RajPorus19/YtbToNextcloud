"""
Configuration Module

This module handles application configuration and settings.
It provides a centralized place for all configuration management.
"""

import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


# Application configuration
class Config:
    """Application configuration class."""

    # Flask settings
    FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
    FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"

    # Scheduler settings
    SCHEDULER_ENABLED = os.getenv("SCHEDULER_ENABLED", "True").lower() == "true"

    # Logging settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Application metadata
    APP_NAME = "Flask Scheduled Functions App"
    APP_VERSION = "1.0.0"
    APP_DESCRIPTION = "A Flask application with scheduled background tasks"


def get_config():
    """
    Get the application configuration.

    Returns:
        Config: Configuration object with all settings
    """
    return Config()


def log_configuration():
    """Log the current configuration for debugging purposes."""
    config = get_config()
    logger = logging.getLogger(__name__)

    logger.info("Application Configuration:")
    logger.info(f"  Flask Host: {config.FLASK_HOST}")
    logger.info(f"  Flask Port: {config.FLASK_PORT}")
    logger.info(f"  Flask Debug: {config.FLASK_DEBUG}")
    logger.info(f"  Scheduler Enabled: {config.SCHEDULER_ENABLED}")
    logger.info(f"  Log Level: {config.LOG_LEVEL}")
    logger.info(f"  App Name: {config.APP_NAME}")
    logger.info(f"  App Version: {config.APP_VERSION}")
