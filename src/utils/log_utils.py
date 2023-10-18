"""log_utils.py
_summary_

_extended_summary_
"""

import time
from loguru import logger


# Basic Logging Setup
logger.remove()  # Remove the default handler
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

# Log to console with specific format and level
logger.add("stdout", format=LOG_FORMAT, level="INFO")

# 1. Log Rotation and Retention
LOG_FILE = "data/logs/app.log"
logger.add(LOG_FILE, rotation="1 week", retention="4 weeks", format=LOG_FORMAT, level="DEBUG")


def log(message, log_type="INFO"):
    """
    Log messages to a file or console.
    """
    if log_type == "INFO":
        logger.info(message)
    elif log_type == "ERROR":
        logger.error(message)
    elif log_type == "DEBUG":
        logger.debug(message)
    elif log_type == "WARNING":
        logger.warning(message)
    elif log_type == "CRITICAL":
        logger.critical(message)
    else:
        logger.info(message)


# 2. External Logging Services
def log_to_external_service(message, service="Sentry"):
    """
    Placeholder function for integrating with external logging services.
    """
    # TODO: Integrate with service API (e.g., Sentry, Loggly, ELK Stack)
    pass


# 3. Conditional Logging
def module_specific_log(module_name, message, log_type="INFO"):
    """
    Log messages conditionally based on the module.
    """
    if module_name == "ModuleNameToDebug":  # Replace with actual module name for debugging
        log(message, log_type)


# 4. Error and Exception Handling
def log_exception(exception):
    """
    Log exceptions with their stack traces.
    """
    logger.exception(exception)


# 5. Performance Logging
def log_performance(task_name, start_time):
    """
    Log the time taken for performance-critical operations.
    """
    elapsed_time = time.time() - start_time
    log(f"{task_name} took {elapsed_time:.2f} seconds", log_type="DEBUG")


# 6. User/Audit Logging
def log_user_action(user_name, action):
    """
    Log user actions for audit purposes.
    """
    log(f"User {user_name} performed action: {action}", log_type="AUDIT")  # 'AUDIT' is a custom log level. You can replace it with appropriate level.


# 7. External System Interactions
def log_external_interaction(system_name, interaction_type, status):
    """
    Log interactions with external systems.
    """
    log(f"{interaction_type} interaction with {system_name} - Status: {status}", log_type="DEBUG")


# Test functions
if __name__ == "__main__":
    start_time = time.time()

    log("This is an info message.")
    log_exception(ValueError("This is a test error"))
    log_performance("TestTask", start_time)
    log_user_action("JohnDoe", "Initiate Scan")
    log_external_interaction("Database", "READ", "SUCCESS")
