import numpy as np

# Hypothetical transition probabilities (modify based on historical data)
P = np.array([[0.6, 0.2, 0.2],  # Home win to home win, away win, draw
              [0.3, 0.5, 0.2],  # Away win to home win, away win, draw
              [0.1, 0.1, 0.8]]) # Draw to home win, away win, draw

# Assume recent wins influence future outcomes
recent_win_bonus = 0.1  # Adjust this value as needed

# Update probabilities based on recent wins
P[0, 0] += recent_win_bonus  # Increase home win to home win probability
P[1, 0] += recent_win_bonus  # Increase away win to home win probability

# Normalize rows
P_normalized = P / P.sum(axis=1, keepdims=True)

def predict_next_outcome(historical_results):
    # Initialize the current state based on the most recurrent result
    current_state = max(set(historical_results), key=historical_results.count)

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
