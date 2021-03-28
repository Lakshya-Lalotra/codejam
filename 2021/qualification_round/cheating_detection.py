import numpy as np

EPSILON = 0.0000001
NUMBER_OF_PLAYER = 100


def parse_input() -> np.ndarray:
    player_question_arr = list()
    for _ in range(NUMBER_OF_PLAYER):
        player_question_arr.append(
            [_ for _ in input()]
        )

    return np.array(player_question_arr, dtype=float)


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def estimate_difficulty(prob: np.ndarray) -> np.ndarray:
    epsilon = EPSILON
    prob = prob.clip(epsilon, 1 - epsilon)

    difficulties = np.log((1 - prob) / prob)
    return difficulties.clip(-3, 3)


def estimate_skill(prob: np.ndarray) -> np.ndarray:
    epsilon = EPSILON
    prob = prob.clip(epsilon, 1 - epsilon)

    skills = -np.log((1 - prob) / prob)
    return skills.clip(-3, 3)


def binary_cross_entropy(actual: np.ndarray, predicted: np.ndarray) -> np.ndarray:
    loss = - actual * np.log(predicted) - (1 - actual) * np.log(1 - predicted)
    return np.mean(loss)


def estimate_expected_loss(skill: float) -> float:
    prob = sigmoid(skill)
    loss = - prob * np.log(prob) - (1 - prob) * np.log(1 - prob)
    return loss


# mean field approximation?
# this approach can get test set 1&2 passed with 100% accuracy
def solve(arr: np.ndarray):
    # difficulties are averaged
    prob_of_answering_question_correctly = arr.mean(axis=1)
    skills = estimate_skill(prob_of_answering_question_correctly)

    # skill levels are averaged
    # it should be find because there is at most 1 cheater
    prob_of_each_question_being_correctly_answered = arr.mean(axis=0)
    difficulties = estimate_difficulty(prob_of_each_question_being_correctly_answered)

    # compute binary cross entropy loss
    # note that loss is skill dependent (summation -p log p), normalization is required! :(
    max_loss_ratio_so_far = 0
    cheater_id = -1
    for player_id in range(NUMBER_OF_PLAYER):
        predicted_prob_of_answering_correctly = sigmoid(skills[player_id] - difficulties)
        loss = binary_cross_entropy(arr[player_id], predicted_prob_of_answering_correctly)
        expected_loss = estimate_expected_loss(skills[player_id])
        loss_ratio = loss / expected_loss
        if max_loss_ratio_so_far < loss_ratio:
            max_loss_ratio_so_far = loss_ratio
            cheater_id = player_id

    return cheater_id + 1


if __name__ == "__main__":
    num_of_test_cases = int(input())
    prob_ = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        result = solve(parse_input())
        print("Case #{}: {}".format(test_id, result))
