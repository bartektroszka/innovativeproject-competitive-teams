from typing import ForwardRef, List, Optional
from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    description: Optional[str] = None
    colour: Optional[str] = None


class PlayerUpdate(BaseModel):
    name: str
    description: Optional[str] = None
    colour: Optional[str] = None


class PlayerCreate(PlayerBase):
    firebase_id: str


class Player(PlayerBase):
    id: int
    role: Optional[str] = None

    class Config:
        orm_mode = True


class TeamBase(BaseModel):
    name: str
    description: Optional[str] = None
    colour: Optional[str] = None


class TeamUpdate(BaseModel):
    description: Optional[str] = None
    colour: Optional[str] = None


class TeamCreate(TeamBase):
    pass


class Team(TeamBase):
    id: int
    captain_id: Optional[int] = None
    players: List[Player] = []

    class Config:
        orm_mode = True


class MatchBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[str] = None
    finished: Optional[bool] = False
    score1: Optional[int] = 0
    score2: Optional[int] = 0


class MatchUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[str] = None
    finished: Optional[bool] = False
    score1: Optional[int] = 0
    score2: Optional[int] = 0


class MatchResult(BaseModel):
    score1: int
    score2: int


class MatchCreate(MatchBase):
    pass


class Match(MatchBase):
    id: int

    team1_id: Optional[int] = None
    team2_id: Optional[int] = None

    team1: Optional[Team] = None
    team2: Optional[Team] = None

    tournament_id: Optional[int] = None
    tournament_place: Optional[int] = None

    class Config:
        orm_mode = True


class TournamentBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    tournament_type: Optional[str] = None
    swiss_rounds: Optional[int] = 3
    start_time: Optional[str] = None


class TournamentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[str] = None


class TournamentCreate(TournamentBase):
    teams_ids: List[int] = []


class TeamResults(BaseModel):
    team: Team
    tournament_points: float
    match_points: int


class TournamentResults(BaseModel):
    matches_finished: int
    matches_unfinished: int
    matches_total: int
    swiss_round: Optional[int] = 0
    finished: bool

    results: List[TeamResults] = []


class Tournament(TournamentBase):
    id: int
    teams: List[Team] = []
    matches: List[Match] = []

    class Config:
        orm_mode = True


Player.update_forward_refs()
