def alphanumeric(password):
    if len(password) < 1:
        return False
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    not_allowed = "_ "
    for character in password:
        if character not in alphabet and character not in digits or character in not_allowed:
            return False
    return True
