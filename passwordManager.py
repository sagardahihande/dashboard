import string

class BasePasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self, password_attempt):
        return password_attempt == self.get_password()

class PasswordManager(BasePasswordManager):
    def __init__(self):
        super().__init__()

    def set_password(self, new_password):
        if self._is_valid_password(new_password):
            self.old_passwords.append(new_password)
            return True
        else:
            return False

    def get_level(self, password=None):
        password_to_check = password if password else self.get_password()

        if self._is_level_2(password_to_check):
            return 2
        elif self._is_level_1(password_to_check):
            return 1
        else:
            return 0

    def _is_valid_password(self, new_password):
        current_level = self.get_level()
        new_level = self.get_level(new_password)

        if (
            (current_level == 2 and new_level == 2)
            or (current_level == 1 and new_level >= 1)
            or (current_level == 0 and new_level == 0)
        ) and len(new_password) >= 6:
            return True
        else:
            return False

    def _is_level_1(self, password):
        return any(char.isalpha() for char in password) and any(char.isdigit() for char in password)

    def _is_level_2(self, password):
        return self._is_level_1(password) and any(char in string.punctuation for char in password)

# Example Usage:
if __name__ == "__main__":
    manager = PasswordManager()

    # Set an initial password
    initial_password = "abc123"
    manager.set_password(initial_password)

    # Get current password
    print("Current Password:", manager.get_password())

    # Check if a password is correct
    print("Is Correct:", manager.is_correct("abc123"))

    # Set a new password with a higher security level
    new_password = "Abc123!"
    if manager.set_password(new_password):
        print("Password changed successfully.")
        print("Current Password:", manager.get_password())
    else:
        print("Password change failed.")

    # Get the security level of the current password
    print("Security Level:", manager.get_level())
