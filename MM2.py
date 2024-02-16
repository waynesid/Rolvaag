import numpy as np

def create_transition_matrix():
    # Hypothetical transition probabilities (modify based on historical data)
    P = np.array([[0.6, 0.2, 0.2],  # Home win to home win, away win, draw
                  [0.3, 0.5, 0.2],  # Away win to home win, away win, draw
                  [0.1, 0.1, 0.8]]) # Draw to home win, away win, draw

    # Normalize rows to ensure probabilities sum to 1
    P_normalized = P / P.sum(axis=1, keepdims=True)

    return P_normalized

def predict_next_outcome(current_state, transition_matrix):
    next_state_probs = transition_matrix[current_state]
    next_outcome = np.random.choice([0, 1, 2], p=next_state_probs)
    return next_outcome

# Example usage
if __name__ == "__main__":
    transition_matrix = create_transition_matrix()
    current_state = 1  # Assume starting from home win state

    num_predictions = 1
    for _ in range(num_predictions):
        next_outcome = predict_next_outcome(current_state, transition_matrix)
        if next_outcome == 0:
            print("Predicted: Home win")
        elif next_outcome == 1:
            print("Predicted: Away win")
        else:
            print("Predicted: Draw")

        current_state = next_outcome
