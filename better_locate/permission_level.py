from typing import Literal


class PermissionLevel:
    """
    Permission levels for MCDR
    """

    # Define allowed string literals for permission kinds
    Kind = Literal['guest', 'user', 'helper', 'admin', 'owner']
    # Default permission kind is 'guest'
    kind: Kind = 'guest'

    # Mapping from permission kind to integer level
    _mapping: dict[Kind, int] = {
        'guest': 0,
        'user': 1,
        'helper': 2,
        'admin': 3,
        'owner': 4,
    }
    # Reverse mapping from integer level to permission kind
    _reverse_mapping = {v: k for k, v in _mapping.items()}

    @staticmethod
    def from_int(level: int) -> 'PermissionLevel':
        """
        Create a PermissionLevel instance from an integer level.
        Raises ValueError if the integer is not a valid level.
        """
        permission_level = PermissionLevel()
        if level not in permission_level._reverse_mapping:
            raise ValueError(f'Invalid permission level: {level}')
        permission_level.kind = permission_level._reverse_mapping[level]
        return permission_level

    @staticmethod
    def from_str(level: str) -> 'PermissionLevel':
        """
        Create a PermissionLevel instance from a string.
        Raises ValueError if the string is not a valid permission kind.
        """
        permission_level = PermissionLevel()
        if level not in permission_level._mapping:
            raise ValueError(f'Invalid permission level: {level}')
        permission_level.kind = level  # type: ignore
        return permission_level

    @staticmethod
    def from_kind(level: Kind) -> 'PermissionLevel':
        """
        Create a PermissionLevel instance from a Kind type.
        """
        permission_level = PermissionLevel()
        permission_level.kind = level
        return permission_level

    def as_kind(self) -> Kind:
        """
        Return the permission kind as a Literal type.
        """
        return self.kind

    def as_int(self) -> int:
        """
        Return the integer representation of the permission level.
        """
        return self._mapping[self.kind]

    def as_str(self) -> str:
        """
        Return the string representation of the permission kind.
        """
        return self.as_kind()

    def is_valid(self, require: 'PermissionLevel'):
        """
        Check if the current permission level is greater than or equal to the required level.
        """
        return self >= require

    def __eq__(self, other: 'PermissionLevel'):
        """
        Compare equality of two PermissionLevel instances.
        """
        return self.kind == other.as_kind()

    def __gt__(self, other: 'PermissionLevel'):
        """
        Check if the current permission level is greater than another.
        """
        return self._mapping[self.kind] > self._mapping[other.as_kind()]

    def __lt__(self, other: 'PermissionLevel'):
        """
        Check if the current permission level is less than another.
        """
        return self._mapping[self.kind] < self._mapping[other.as_kind()]
