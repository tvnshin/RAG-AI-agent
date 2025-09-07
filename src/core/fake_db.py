from src.schemas.user import UserOut

fake_db = {
    101: {
        "name": "Alice Johnson",
        "status": "active"
    },
    102: {
        "name": "Bob Williams",
        "status": "inactive"
    },
    103: {
        "name": "Charlie Brown",
        "status": "active"
    },
    104: {
        "name": "Diana Prince",
        "status": "inactive"
    },
    105: {
        "name": "Edward Lee",
        "status": "active"
    }
}


async def get_user(user_id: int) -> UserOut:
    if user_id not in fake_db:
        raise ValueError(f"User with ID {user_id} not found.")
    user_data = fake_db[user_id]
    return UserOut(id=user_id, **user_data)