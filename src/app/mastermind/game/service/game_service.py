from app.mastermind.game.unit_of_work.use_cases.create_game_use_case import CreateGameUseCase
from app.mastermind.game.unit_of_work.use_cases.create_guess_use_case import CreateGuessUseCase, CreateGuessUseCaseArgs
from app.mastermind.game.unit_of_work.use_cases.retrieve_game_use_case import RetrieveGameUseCase, RetrieveGameUseArgs


class GameService:
    @classmethod
    def create_game(cls, create_game_use_case: CreateGameUseCase):
        return create_game_use_case(None)

    @classmethod
    def retrieve_game(cls, game_id: str, retrieve_game_use_case: RetrieveGameUseCase):
        return retrieve_game_use_case(RetrieveGameUseArgs(game_id=game_id))

    @classmethod
    def create_guess(cls, game_id: str, guess_code: str, create_guess_use_case: CreateGuessUseCase):
        return create_guess_use_case(args=CreateGuessUseCaseArgs(game_id=game_id, guess_code=guess_code))