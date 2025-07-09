"""
Routes Module

This module contains all the Flask routes and API endpoints.
It provides a clean separation of concerns for HTTP request handling.
"""

from flask import jsonify
from datetime import datetime
import logging

from .scheduler_service import function_every_1h, function_every_2h
from .scheduler_config import scheduler_manager

logger = logging.getLogger(__name__)


def register_routes(app):
    """
    Register all routes with the Flask app.

    Args:
        app: Flask application instance
    """

    @app.route("/")
    def home():
        """Home endpoint providing basic app information."""
        return jsonify(
            {
                "message": "Flask app with scheduled functions",
                "status": "running",
                "scheduled_jobs": scheduler_manager.get_job_count(),
            }
        )

    @app.route("/health")
    def health():
        """Health check endpoint for monitoring."""
        return jsonify(
            {
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "scheduler_running": scheduler_manager.is_running(),
            }
        )

    @app.route("/jobs")
    def jobs():
        """List all scheduled jobs with detailed information."""
        jobs = scheduler_manager.get_jobs_info()
        return jsonify({"jobs": jobs})

    @app.route("/trigger-1h")
    def trigger_1h():
        """Manually trigger the 1-hour function."""
        try:
            function_every_1h()
            return jsonify(
                {
                    "message": "1-hour function triggered manually",
                    "status": "success",
                    "timestamp": datetime.now().isoformat(),
                }
            )
        except Exception as e:
            logger.error(f"Error triggering 1-hour function: {e}")
            return jsonify(
                {
                    "message": "Error triggering 1-hour function",
                    "status": "error",
                    "error": str(e),
                }
            ), 500

    @app.route("/trigger-2h")
    def trigger_2h():
        """Manually trigger the 2-hour function."""
        try:
            function_every_2h()
            return jsonify(
                {
                    "message": "2-hour function triggered manually",
                    "status": "success",
                    "timestamp": datetime.now().isoformat(),
                }
            )
        except Exception as e:
            logger.error(f"Error triggering 2-hour function: {e}")
            return jsonify(
                {
                    "message": "Error triggering 2-hour function",
                    "status": "error",
                    "error": str(e),
                }
            ), 500

    @app.route("/scheduler/status")
    def scheduler_status():
        """Get detailed scheduler status."""
        return jsonify(
            {
                "scheduler_running": scheduler_manager.is_running(),
                "job_count": scheduler_manager.get_job_count(),
                "jobs": scheduler_manager.get_jobs_info(),
                "timestamp": datetime.now().isoformat(),
            }
        )

    @app.route("/scheduler/start", methods=["POST"])
    def start_scheduler():
        """Start the scheduler."""
        try:
            scheduler_manager.start()
            return jsonify(
                {
                    "message": "Scheduler started successfully",
                    "status": "success",
                    "scheduler_running": scheduler_manager.is_running(),
                }
            )
        except Exception as e:
            logger.error(f"Error starting scheduler: {e}")
            return jsonify(
                {
                    "message": "Error starting scheduler",
                    "status": "error",
                    "error": str(e),
                }
            ), 500

    @app.route("/scheduler/stop", methods=["POST"])
    def stop_scheduler():
        """Stop the scheduler."""
        try:
            scheduler_manager.stop()
            return jsonify(
                {
                    "message": "Scheduler stopped successfully",
                    "status": "success",
                    "scheduler_running": scheduler_manager.is_running(),
                }
            )
        except Exception as e:
            logger.error(f"Error stopping scheduler: {e}")
            return jsonify(
                {
                    "message": "Error stopping scheduler",
                    "status": "error",
                    "error": str(e),
                }
            ), 500

    logger.info("All routes registered successfully")
