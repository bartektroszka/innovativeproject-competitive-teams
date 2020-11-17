
from app.database import crud
from fastapi import HTTPException


def is_higher_role(role1, role2):
    roles = {}
    roles['admin'] = 10
    roles['moderator'] = 5
    roles['player'] = 1
    if role1 not in roles:
        raise Exception('role1 is not a role')
    if role2 not in roles:
        raise Exception('role2 is not a role')
    return roles[role1] >= roles[role2]


def is_accessible(db, firebase_id, clearance='player'):
    db_player = crud.get_player_by_firebase_id(db, firebase_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_role = db_player.role
    return is_higher_role(db_role, clearance)
    

