import os
import logging
from pathlib import Path
from typing import List

# ✅ Configure logging to track the script's actions
logging.basicConfig(
    level=logging.INFO,  # Set logging level to INFO
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format with timestamp, level, and message
)

def create_project_structure(project_name: str, files: List[str]) -> None:
    """
    ✅ Create the required directory and file structure for a project.

    Args:
        project_name (str): Name of the root project directory.
        files (List[str]): List of file paths to create (relative to project root).
    """
    for filepath in files:
        path = Path(filepath)  # Convert string path to Path object for OS-independent operations
        
        try:
            # ✅ Create parent directory if it doesn't exist (skip if file is at root level)
            if path.parent != Path():
                os.makedirs(path.parent, exist_ok=True)  # Recursive directory creation
                logging.debug(f"Created directory: {path.parent}")  # Log for debugging

            # ✅ Create the file only if it doesn't exist or is empty
            if not path.exists() or path.stat().st_size == 0:
                path.touch()  # Create empty file
                logging.info(f"Created file: {path}")  # Log file creation
            else:
                logging.info(f"File already exists and is not empty: {path}")  # Log existing file
        except Exception as e:
            # ✅ Log any unexpected errors during file/directory creation
            logging.error(f"Failed to create {filepath}: {e}", exc_info=True)

if __name__ == "__main__":
    # ✅ Define the project name
    PROJECT_NAME = "sensor"

    # ✅ Define the complete list of files and folders to create
    FILE_LIST = [
        f"{PROJECT_NAME}/__init__.py",  # Package initializer
        f"{PROJECT_NAME}/components/__init__.py",
        f"{PROJECT_NAME}/components/data_ingestion.py",  
        f"{PROJECT_NAME}/components/data_validation.py",
        f"{PROJECT_NAME}/components/data_transformation.py",
        f"{PROJECT_NAME}/components/model_trainer.py",
        f"{PROJECT_NAME}/components/model_evaluation.py",
        f"{PROJECT_NAME}/components/model_pusher.py",
        f"{PROJECT_NAME}/configuration/__init__.py",
        f"{PROJECT_NAME}/constants/__init__.py",
        f"{PROJECT_NAME}/entity/__init__.py",
        f"{PROJECT_NAME}/entity/config_entity.py",  # Configuration dataclasses
        f"{PROJECT_NAME}/entity/artifact_entity.py",  # Artifacts for pipeline stages
        f"{PROJECT_NAME}/exception/__init__.py",  # Custom exceptions
        f"{PROJECT_NAME}/logger/__init__.py",  # Logging configuration
        f"{PROJECT_NAME}/pipeline/__init__.py",  # ⚠️ Fixed typo from "pipline"
        f"{PROJECT_NAME}/pipeline/training_pipeline.py",  # Training pipeline
        f"{PROJECT_NAME}/pipeline/prediction_pipeline.py",  # Inference pipeline
        f"{PROJECT_NAME}/utils/__init__.py",
        f"{PROJECT_NAME}/utils/main_utils.py",  # Common utility functions

        # ✅ Project-level files
        "app.py",  # Main app (e.g., FastAPI entrypoint)
        "requirements.txt",  # Dependencies list
        "Dockerfile",  # Container setup
        ".dockerignore",  # Files to ignore during docker build
        "demo.py",  # Optional demo/testing script
        "setup.py",  # Package metadata for pip install

        # ✅ Configuration files
        "config/model.yaml",  # Model-specific settings
        "config/schema.yaml",  # Data schema definitions
    ]

    # ✅ Run the structure creation function
    create_project_structure(PROJECT_NAME, FILE_LIST)
