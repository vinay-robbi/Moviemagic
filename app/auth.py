import uuid

# Temporary in-memory user store (will be replaced by DynamoDB)
users = {}

def register_user(email, password):
    if email in users:
        return None  # user already exists
    user_id = str(uuid.uuid4())
    users[email] = {'user_id': user_id, 'password': password}
    return user_id

def login_user(email, password):
    user = users.get(email)
    if user and user['password'] == password:
        return user['user_id']
    return None
