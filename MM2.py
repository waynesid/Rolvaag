import numpy as np

# Hypothetical transition probabilities (modify based on historical data)
P = np.array([[0.6, 0.2, 0.2],  # Home win to home win, away win, draw
              [0.3, 0.5, 0.2],  # Away win to home win, away win, draw
              [0.1, 0.1, 0.8]]) # Draw to home win, away win, draw

# Normalize rows
P_normalized = P / P.sum(axis=1, keepdims=True)

def predict_next_outcome(historical_results):
    # Initialize the current state based on the entire historical sequence
    current_state = historical_results[0]  # Assume the first match outcome

    # Update the current state using the entire historical sequence
    for result in historical_results[1:]:
        current_state = result

    # Predict next match outcome
    next_state_probs = P_normalized[current_state]
    next_outcome = np.argmax(next_state_probs)

    return next_outcome

# Example usage
if __name__ == "__main__":
    # Historical match results (0: home win, 1: away win, 2: draw)
    historical_results = [0, 1, 2, 0, 1, 2, 0, 1, 2]

    next_outcome = predict_next_outcome(historical_results)
    if next_outcome == 0:
        print("Predicted: Home win")
    elif next_outcome == 1:
        print("Predicted: Away win")
    else:
        print("Predicted: Draw")
