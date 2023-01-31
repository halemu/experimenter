"""
This type stub file was generated by pyright.
"""

from celery.exceptions import NotRegistered

"""Registry of available tasks."""
__all__ = ("TaskRegistry",)

class TaskRegistry(dict):
    """Map of registered tasks."""

    NotRegistered = NotRegistered
    def __missing__(self, key): ...
    def register(self, task):  # -> None:
        """Register a task in the task registry.

        The task will be automatically instantiated if not already an
        instance. Name must be configured prior to registration.
        """
        ...
    def unregister(self, name):  # -> None:
        """Unregister task by name.

        Arguments:
            name (str): name of the task to unregister, or a
                :class:`celery.app.task.Task` with a valid `name` attribute.

        Raises:
            celery.exceptions.NotRegistered: if the task is not registered.
        """
        ...
    def regular(self): ...
    def periodic(self): ...
    def filter_types(self, type): ...
