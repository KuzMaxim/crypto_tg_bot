from repositories.db.top_crypto_repository import crypto_repository

class TopCryptoService():
    def __init__(self):
        self.repository = crypto_repository
        
    def add_crypto(self, username: str, email: str):
        self.repository.set(username, email)
        print(f'User {username} added with email: {email}')

    def get_crypto(self, username: str):
        email = self.repository.get(username) 
        if email:
            print (f'User {username} found with email: {email}')
        print (f'User {username} not found')