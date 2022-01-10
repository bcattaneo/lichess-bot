import subprocess
import sys
import time
import chess

MOVEMENT_PREFIX = "position startpos move"
THREADS_PREFIX = "setoption name threads value"


class StockfishGame:
    def __init__(self, stockfish_path, starting_position=[], depth=20, threads=1):
        self.board = chess.Board()
        self.position = starting_position
        self.stockfish_path = stockfish_path
        self.__init_board()  # throws exception on first bad move in starting position
        self.depth = depth
        self.threads = threads

    def sanToUciSteps(steps):
        temp_board = chess.Board()
        return list(map(lambda step: str(temp_board.push_san(step)), steps))

    def move(self, movement):
        self.board.push_uci(movement)  # throws exception if bad move
        self.position.append(movement)

    def display(self):
        return "\n".join(self.__run_stockfish("d").split("\n")[2:20])

    def best_move(self):
        # TODO: include ponder in the API response?
        output = self.__run_stockfish(
            f"go depth {self.__get_depth()}").split("\n")[-1]
        return "" if "bestmove (none)" in output else output[9:13]

    def apply_best_move(self):
        new_best_move = self.best_move()
        self.move(new_best_move)
        return new_best_move

    def __run_stockfish(self, command):
        commands = [self.__get_threads(), self.__get_position(), command]
        print("Opening stockfish...")
        process = subprocess.Popen([self.__get_stockfish_path()],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)
        for c in commands:
            print(c, file=process.stdin, flush=True)

        time.sleep(2)  # TODO: make a parameter and find relation with depth

        output = process.communicate()[0]
        return output.strip()

    def __init_board(self):
        for move in self.position:
            self.board.push_uci(move)

    def __get_stockfish_path(self):
        return self.stockfish_path

    def __get_position(self):
        return f"{MOVEMENT_PREFIX} {' '.join(self.position)}"

    def __get_depth(self):
        return self.depth

    def __get_threads(self):
        return f"{THREADS_PREFIX} {self.threads}"
