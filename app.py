"""
Main Application Entry Point

This is the main entry point for the Flask application with scheduled functions.
The application uses a modular structure with business logic separated into services.
"""

import sys
import os

# Add the current directory to Python path to ensure imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.app_factory import create_app, get_app_config


def main():
    """
    Main application entry point.

    Creates and runs the Flask application with all configured services.
    """
    try:
        # Create the Flask application
        app = create_app()

        # Get configuration
        config = get_app_config()

        # Run the application
        app.run(
            host=config.FLASK_HOST, port=config.FLASK_PORT, debug=config.FLASK_DEBUG
        )

    except KeyboardInterrupt:
        print("\nApplication stopped by user")
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
