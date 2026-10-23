def is_dirty(environment, room):
    """Perceive whether the selected room needs cleaning."""
    return environment[room] == "Dirty"


def clean_room(environment, room):
    """Update the environment after a cleaning action."""
    environment[room] = "Clean"


def read_room_state(room):
    """Accept only Dirty or Clean, ignoring case and extra spaces."""
    while True:
        state = input(f"Is room {room} Dirty or Clean? ").strip().lower()
        if state in ("dirty", "clean"):
            return state.capitalize()
        print("Invalid state. Please enter Dirty or Clean.")


def read_steps():
    """Accept a non-negative whole number of simulation steps."""
    while True:
        try:
            steps = int(input("How many steps should the agent run? "))
            if steps >= 0:
                return steps
        except ValueError:
            pass
        print("Invalid steps. Please enter a whole number of 0 or more.")


class VacuumAgent:
    """A rule-based agent that starts in room A."""

    def __init__(self, environment):
        self.environment = environment
        self.location = "A"

    def move(self):
        """Switch from A to B or from B to A."""
        self.location = "B" if self.location == "A" else "A"

    def perceive_and_act(self):
        """Apply exactly one rule and perform one action per step."""
        if is_dirty(self.environment, self.location):
            # Rule 1: stay in the current room and clean it if dirty.
            clean_room(self.environment, self.location)
            return f"Cleaned room {self.location}"

        # Rule 2: move to the other room if the current room is clean.
        previous_room = self.location
        self.move()
        return f"Moved from room {previous_room} to room {self.location}"


def main():
    print("RULE-BASED VACUUM CLEANER AGENT")
    # Task 1: initialize the two-room dictionary from user input.
    environment = {room: read_room_state(room) for room in ("A", "B")}
    steps = read_steps()
    agent = VacuumAgent(environment)
    print(f"\nInitial environment: {environment}")
    print(f"Starting location: {agent.location}")

    # Task 3: execute the requested number of perceive-and-act cycles.
    for step in range(1, steps + 1):
        print(f"\nStep {step} | Location before action: {agent.location}")
        action = agent.perceive_and_act()
        print(f"Action: {action}")
        print(f"Current location: {agent.location}")
        print(f"Environment state: {environment}")

    # Continue moving even if both rooms are clean, as Rule 2 requires.
    print(f"\nSimulation complete: {steps} step(s).")
    print(f"Final location: {agent.location}")
    print(f"Final environment: {environment}")


if __name__ == "__main__":
    main()
