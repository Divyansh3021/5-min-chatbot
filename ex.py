import random

# Sample dataset and transition matrix
dataset = [
    "Once upon a time",
    "there was a cat",
    "The cat loved to",
    "explore the forest",
    "One day, it found",
    "a hidden treasure",
    "The treasure was",
    "guarded by a dragon",
]

transition_matrix = {
    "Once upon a time": {"there was a cat": 1.0},
    "there was a cat": {"The cat loved to": 1.0},
    "The cat loved to": {"explore the forest": 1.0},
    "explore the forest": {"One day, it found": 1.0},
    "One day, it found": {"a hidden treasure": 1.0},
    "a hidden treasure": {"The treasure was": 1.0},
    "The treasure was": {"guarded by a dragon": 1.0},
    "guarded by a dragon": {"The end": 1.0},
}

# Generate a story
def generate_story(transition_matrix, initial_state, length=5):
    current_state = initial_state
    story = [current_state]

    for _ in range(length):
        next_state_options = transition_matrix.get(current_state, {})
        if not next_state_options:
            break
        next_state = random.choices(list(next_state_options.keys()), list(next_state_options.values()))[0]
        story.append(next_state)
        current_state = next_state

    return " ".join(story)

# Generate a story starting from a specific state
initial_state = "Once upon a time"
generated_story = generate_story(transition_matrix, initial_state)
print(generated_story)
