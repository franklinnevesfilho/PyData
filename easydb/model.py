class Model:
    def __init_subclass__(cls):
        """Automatically extract attributes and types from class definition."""
        cls._columns = {
            key: type(value) for key, value in cls.__annotations__.items()
        }
        cls._defaults = {
            key: value for key, value in cls.__dict__.items() if not key.startswith("__")
        }

    def __init__(self, **kwargs):
        """Initialize an instance with defaults or user-provided values."""
        for key, value in self._defaults.items():
            setattr(self, key, kwargs.get(key, value))

    def to_dict(self):
        """Convert instance to dictionary."""
        return {key: getattr(self, key) for key in self._columns.keys()}
