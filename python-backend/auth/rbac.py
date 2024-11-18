class RoleManager:
    """Manages role-based access control (RBAC)."""

    def __init__(self):
        self.roles = {}

    def add_role(self, role_name, permissions):
        """
        Add a role with associated permissions.

        Args:
            role_name (str): The name of the role.
            permissions (list): List of permissions for the role.
        """
        self.roles[role_name] = set(permissions)

    def check_permission(self, role_name, permission):
        """
        Check if a role has a specific permission.

        Args:
            role_name (str): The role name.
            permission (str): The permission to check.

        Returns:
            bool: True if the role has the permission, otherwise False.
        """
        return permission in self.roles.get(role_name, set())

    def get_permissions(self, role_name):
        """
        Retrieve all permissions for a role.

        Args:
            role_name (str): The role name.

        Returns:
            list: List of permissions.
        """
        return list(self.roles.get(role_name, []))
