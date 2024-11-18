from auth.rbac import RoleManager

# Initialize RoleManager
role_manager = RoleManager()

# Add roles and permissions
role_manager.add_role("admin", ["create_user", "delete_user", "view_reports"])
role_manager.add_role("user", ["view_profile", "edit_profile"])

# Check permissions
is_allowed = role_manager.check_permission("admin", "delete_user")
print("Admin Delete User Permission:", is_allowed)

permissions = role_manager.get_permissions("user")
print("User Permissions:", permissions)
