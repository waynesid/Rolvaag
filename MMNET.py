import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Generate synthetic data (replace with your actual data)
# Assume 1 = win, 0 = loss, 2 = Draw
historical_results = ["1", "2", "0", "2", "1", "1", "1", "2", "1"]

# Create a Markov chain transition matrix (same as before)
# ...

# PyTorch neural network
class WinLossPredictor(nn.Module):
    def __init__(self):
        super(WinLossPredictor, self).__init__()
        self.fc1 = nn.Linear(1, 16)  # One input feature (random input)
        self.fc2 = nn.Linear(16, 3)  # Three output classes: win or loss 0r draw

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.softmax(self.fc2(x), dim=1)
        return x

def train_neural_network():
    nn_model = WinLossPredictor()
    optimizer = optim.Adam(nn_model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    # Generate random input (replace with actual features)
    nn_input = torch.rand(1, 1)

    # Train on random input (replace with actual labels)
    labels = torch.tensor([0])  # 0 for win, 1 for loss
    for _ in range(10):
        optimizer.zero_grad()
        outputs = nn_model(nn_input)

        # Modify the number of output classes (3 in this case)
        num_classes = 3
        modified_labels = torch.zeros_like(labels, dtype=torch.long)
        modified_labels[labels == 0] = 0
        modified_labels[labels == 1] = 1
        modified_labels[labels == 2] = 2

        loss = criterion(outputs, modified_labels)
        loss.backward()
        optimizer.step()

    return nn_model

import numpy as np

def create_transition_matrix(results):
    # Define the possible states (e.g., "W" for win, "L" for loss)
    states = ["0", "1","2"]
    num_states = len(states)

    # Initialize the transition matrix with zeros
    transition_matrix = np.zeros((num_states, num_states))

    # Compute transition counts based on historical results
    for i in range(len(results) - 1):
        current_state = results[i]
        next_state = results[i + 1]
        current_idx = states.index(current_state)
        next_idx = states.index(next_state)
        transition_matrix[current_idx, next_idx] += 1

    # Normalize probabilities (convert counts to probabilities)
    transition_matrix /= transition_matrix.sum(axis=1, keepdims=True)

    return transition_matrix

# Example usage:
historical_results = ["2", "1", "0", "0", "2", "1", "2", "0", "1"]
transition_matrix = create_transition_matrix(historical_results)

# Now you can use this transition_matrix to compute next state probabilities


# Combine Markov chain and neural network
def predict_next_outcome(current_state, is_home=True):
    states = ["0", "1", "2"]
    # Use Markov chain probabilities
    next_state_probs = transition_matrix[states.index(current_state)]

    # Neural network predicts win/loss
    nn_input = torch.rand(1, 1)  # Random input
    nn_model = train_neural_network()
    nn_output = nn_model(nn_input)
    if nn_output.argmax() == 0:
        predicted_outcome = "Win"
    elif nn_output.argmax() == 1:
        predicted_outcome = "Loss"
    elif nn_output.argmax() == 2:
         predicted_outcome = "Draw"

    # Apply home/away strength
    strength_multiplier = 1.1 if is_home else 0.9
    adjusted_probs = next_state_probs * strength_multiplier

    return predicted_outcome, adjusted_probs

# Example usage
current_state = "0"
is_home_game = True
predicted_outcome, adjusted_probs = predict_next_outcome(current_state, is_home_game)
print(f"Predicted outcome for the next game: {predicted_outcome}")
print(f"Adjusted probabilities: Win={adjusted_probs[0]:.2f}, Loss={adjusted_probs[1]:.2f}, Draw={adjusted_probs[2]:.2f}")
