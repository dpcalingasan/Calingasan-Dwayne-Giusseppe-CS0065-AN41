import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# ---------------- USER INPUT ----------------

num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))


# ---------------- AGENT ----------------

class RandomWalker(ap.Agent):

    def setup(self):
        self.path = []

    def step(self):

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        random.shuffle(directions)

        x, y = self.position

        for dx, dy in directions:

            new_x = x + dx
            new_y = y + dy

            if not (
                0 <= new_x < self.model.p.grid_size[0]
                and 0 <= new_y < self.model.p.grid_size[1]
            ):
                continue

            new_position = (new_x, new_y)

            # TASK 2:
            occupied = [
                agent.position
                for agent in self.model.agents
                if agent != self
            ]

            if new_position not in occupied:
                self.position = new_position
                break

        # TASK 1:
        # Record the agent's position
        self.path.append(self.position)


# ---------------- MODEL ----------------

class RandomWalkModel(ap.Model):

    def setup(self):

        self.agents = ap.AgentList(
            self,
            self.p.agents,
            RandomWalker
        )

        # Give agents random starting positions
        for agent in self.agents:

            agent.position = (
                random.randint(0, self.p.grid_size[0] - 1),
                random.randint(0, self.p.grid_size[1] - 1)
            )

            # Record starting position
            agent.path.append(agent.position)

        self.grid = ap.Grid(
            self,
            self.p.grid_size,
            torus=False
        )

        self.grid.add_agents(self.agents)

    def step(self):

        for agent in self.agents:
            agent.step()


# ---------------- PARAMETERS ----------------

parameters = {
    "agents": num_agents,
    "grid_size": (grid_size, grid_size),
    "steps": num_steps
}


# ---------------- CREATE MODEL ----------------

model = RandomWalkModel(parameters)

model.setup()


# ---------------- ANIMATION ----------------

fig, ax = plt.subplots()

ax.set_xlim(-0.5, model.p.grid_size[0] - 0.5)
ax.set_ylim(-0.5, model.p.grid_size[1] - 0.5)

ax.set_xticks(range(model.p.grid_size[0]))
ax.set_yticks(range(model.p.grid_size[1]))

ax.grid(True)

scat = ax.scatter([], [], s=200)


def update(frame):

    model.step()

    x = [agent.position[0] for agent in model.agents]
    y = [agent.position[1] for agent in model.agents]

    scat.set_offsets(list(zip(x, y)))

    ax.set_title(f"Random Walk - Step {frame + 1}")

    return scat,


ani = animation.FuncAnimation(
    fig,
    update,
    frames=model.p.steps,
    interval=300,
    blit=False,
    repeat=False
)

plt.show()


# ---------------- RESULTS ----------------

print("\n========== FINAL RESULTS ==========")

for i, agent in enumerate(model.agents, start=1):

    print(f"\nAgent {i}")

    print(f"Final Position: {agent.position}")

    print("Path:")

    for position in agent.path:
        print(position, end=" -> ")

    print("END")


# ---------------- PATH VISUALIZATION ----------------

plt.figure()

for i, agent in enumerate(model.agents, start=1):

    x = [position[0] for position in agent.path]
    y = [position[1] for position in agent.path]

    plt.plot(
        x,
        y,
        marker="o",
        label=f"Agent {i}"
    )

plt.xlim(-0.5, grid_size - 0.5)
plt.ylim(-0.5, grid_size - 0.5)

plt.xticks(range(grid_size))
plt.yticks(range(grid_size))

plt.grid(True)

plt.title("Agent Movement Paths")

plt.xlabel("X Position")
plt.ylabel("Y Position")

plt.legend()

plt.show()