"""
This module defines TemplateTask. TemplateTask is not meant
to be run. it just provides a template from which other
ETLTasks can be easily written.
"""
import os
from utils.tasks.etl_task import ETLTask

class TemplateTask(ETLTask):
    """
    Template task defining methods.

    Attributes:

    Methods:
    """
    def transform(self, data):
        """
        Transform the data.

        Parameters:
        ----------
        """

    def get_extract_file_path(self):
        """
        Get the extract file path.

        Parameters:
        ----------
        """
        result = os.path.join(
            self.extract_dir,
            "extract_stem.parquet"
        )
        return result

    def run(self, **kwargs):
        """
        Run the task.

        Parameters:
        ----------
        kwargs : dict
            Keyword arguments for configuring the task. This method expects the 
            following key(s):
        """

    def get_load_file_path(self):
        """
        Get the load file path.

        Parameters:
        ----------
        """
        result = os.path.join(
            self.extract_dir,
            "load_stem.parquet"
        )
        return result