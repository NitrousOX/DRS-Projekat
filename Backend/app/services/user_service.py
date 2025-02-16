from app.repo.user_repo import UserRepository

def get_data():
    # Call the repository to fetch data
    data = UserRepository.get_all_data()
    
    if data is None:
        return {'error': 'Failed to retrieve data'}, 500
    
    return data
