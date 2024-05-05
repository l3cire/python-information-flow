from abc import ABC, abstractmethod


class SecureType(ABC):
    """An abstract base class for all security types. This Python does not technically
    have interfaces as in other OO languages, this is our way of recreating that functionality.
    All classes that inherit from this class have to implement the following methods."""
    @abstractmethod
    def __repr__(self):
        """Returns the representation of the object."""
        pass

    @abstractmethod
    def __str__(self):
        """Returns the string representation of the object."""
        pass

    @abstractmethod
    def get_value(self):
        """Returns the underlying value that the type encapsulates."""
        pass

    @abstractmethod
    def set_value(self, val):
        """Sets the underlying value that the type encapsulates."""
        pass

    @abstractmethod
    def get_level(self):
        """Returns the security level of the type."""
        pass

    @abstractmethod
    def set_level(self, level):
        """Sets the security level of the type."""
        pass
