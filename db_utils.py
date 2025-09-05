def get_user_data(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'" # Potential SQL injection
    # ... rest of the code
    return query