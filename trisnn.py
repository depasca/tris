from itertools import count


class TrisNN:
    size = 0
    def __init__(self):
        self.sixe = 9
        self.input_size = 9
        self.output_size = 9
        self.weights = self.initialize_weights(self.input_size, self.output_size)

    def initialize_weights(self, in_size, out_size):
        return [[0.5] * out_size for _ in range(in_size)]

    def calculate(self, input_vector: list) -> list:
        output_vector = [0] * self.output_size
        for i in range(len(input_vector)):
            for j in range(len(self.weights[0])):
                output_vector[j] += input_vector[i] * self.weights[i][j]
        for j in range(len(output_vector)):
            output_vector[j] = 1 / (1 + pow(2.71828, -output_vector[j]))  # Sigmoid activation
        return output_vector
    
    def choose_move(self, board_state: list) -> int:
        output = self.calculate(board_state)
        # Choose the move with the highest score
        move = output.index(max(output))
        return move
    
    def train(self, training_data: list, epochs: int = 1000, learning_rate: float = 0.01):
        for epoch in range(epochs):
            for input_vector, target_vector in training_data:
                output_vector = self.calculate(input_vector)
                for i in range(len(self.weights)):
                    for j in range(len(self.weights[0])):
                        error = target_vector[j] - output_vector[j]
                        self.weights[i][j] += learning_rate * error * input_vector[i]

    def print_weights(self):
        for row in self.weights:
            print(row)

if __name__ == "__main__":
    nn = TrisNN()
    # Example training data: (input_vector, target_vector)
    training_data = [
        ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0]),  # Prefer center
        ([1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0]),  # Prefer opposite
        ([0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0]),  # Prefer adjacent
        ([-1, -1, 0, 1, 0, 0, 1, 0, 0], [-1, -1, 1, 1, 0, 0, 1, 0, 0]) 
         
    ]
    nn.train(training_data, epochs=5000)
    nn.print_weights()
    
    # def calc_score(self, board_state: list) -> float:
    #     possible_wins = self.get_possible_wins()
    #     score = 0.0
    #     for combo in possible_wins:
    #         if all(board_state[i] == 1 for i in combo):
    #             return 10000.0
    #         elif all(board_state[i] == -1 for i in combo):
    #             return -10000.0
    #         elif any(board_state[i] == 1 for i in combo) and any(board_state[i] == -1 for i in combo):
    #             continue
    #         elif any(board_state[i] == 0 for i in combo):
    #             for i in combo:
    #                 if board_state[i] == 1:
    #                     score += 1.0
    #                 elif board_state[i] == -1:
    #                     score -= 1.0
    #         else:
    #             continue
    #     return score
    
    # def get_possible_wins(self) -> list:
    #     winning_combinations_ind = [
    #         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    #         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    #         [0, 4, 8], [2, 4, 6]              # diagonals
    #     ]
    #     return winning_combinations_ind
    
# if __name__ == "__main__":
#     nn = TrisNN()
#     board_state = [0, 1, -1, 
#                    0, 1, 0, 
#                    -1, 0, 0]
#     score = nn.calc_score(board_state)
#     print("Board score:", score) 
#     move = nn.choose_move(board_state)
#     board_state[move] = 1  # Simulate making the move
#     score = nn.calc_score(board_state)
#     print("Chosen move:", move)
#     print("Board score:", score) 