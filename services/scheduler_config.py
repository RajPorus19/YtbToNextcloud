"""
Scheduler Configuration Module

This module handles the configuration and setup of the APScheduler
background scheduler and manages all scheduled jobs.
"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import logging

from .scheduler_service import get_scheduled_functions

logger = logging.getLogger(__name__)


class SchedulerManager:
    """
    Manages the APScheduler background scheduler and all scheduled jobs.

    This class provides a clean interface for setting up, managing,
    and monitoring scheduled tasks.
    """

    def __init__(self):
        """Initialize the scheduler manager."""
        self.scheduler = BackgroundScheduler()
        self._setup_jobs()

    def _setup_jobs(self):
        """Set up all scheduled jobs."""
        scheduled_functions = get_scheduled_functions()

        # Schedule the 1-hour function
        self.scheduler.add_job(
            func=scheduled_functions["function_1h"]["function"],
            trigger=IntervalTrigger(hours=1),
            id="function_1h",
            name=scheduled_functions["function_1h"]["name"],
            replace_existing=True,
        )

        # Schedule the 2-hour function
        self.scheduler.add_job(
            func=scheduled_functions["function_2h"]["function"],
            trigger=IntervalTrigger(hours=2),
            id="function_2h",
            name=scheduled_functions["function_2h"]["name"],
            replace_existing=True,
        )

        logger.info(f"Set up {len(scheduled_functions)} scheduled jobs")

    def start(self):
        """Start the scheduler."""
        if not self.scheduler.running:
            self.scheduler.start()
            logger.info("Scheduler started")

    def stop(self):
        """Stop the scheduler."""
        if self.scheduler.running:
            self.scheduler.shutdown()
            logger.info("Scheduler stopped")

    def get_jobs(self):
        """Get all scheduled jobs."""
        return self.scheduler.get_jobs()

    def get_job_count(self):
        """Get the number of scheduled jobs."""
        return len(self.scheduler.get_jobs())

    def is_running(self):
        """Check if the scheduler is running."""
        return self.scheduler.running

    def get_jobs_info(self):
        """Get detailed information about all scheduled jobs."""
        jobs = []
        for job in self.scheduler.get_jobs():
            jobs.append(
                {
                    "id": job.id,
                    "name": job.name,
                    "next_run_time": str(job.next_run_time)
                    if job.next_run_time
                    else None,
                    "trigger": str(job.trigger),
                }
            )
        return jobs


# Global scheduler instance
scheduler_manager = SchedulerManager()
