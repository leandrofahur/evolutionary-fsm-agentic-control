# Evolutionary FSM with Agentic Control

<!-- [![CI/CD Pipeline](https://github.com/ufmg/evolutionary-fsm-agentic-control/actions/workflows/ci.yml/badge.svg)](https://github.com/ufmg/evolutionary-fsm-agentic-control/actions/workflows/ci.yml) -->
[![Code Coverage](https://codecov.io/gh/ufmg/evolutionary-fsm-agentic-control/branch/main/graph/badge.svg)](https://codecov.io/gh/ufmg/evolutionary-fsm-agentic-control)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Project Version](https://img.shields.io/badge/version-0.1.0-green.svg)](https://github.com/ufmg/evolutionary-fsm-agentic-control/releases)

> A local, self-evolving control framework where an adaptive agent can modify the finite state machine’s topology (states + transitions) based on reasoning, feedback, and/or observation.

## Motivation
Create Finite State Machines (FSMs) combined with Agentic Control, where the behavior and state transitions evolve based on internal reasoning or external signals. This new approach has major implications across robotics, embedded systems, simulation environments, and even AI decision systems.

## Architecture
🚧

## Features
🚧

## Getting started
### Installing Python Venvs

The Python packages are managed using the [uv](https://github.com/astral-sh/uv) package manager, In order to install it, you can follow the [installation guide](https://docs.astral.sh/uv/#getting-started). For Mac users, as of 22 Oct 2024 enter the following in your terminal:

```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once `uv` is installed and available in your terminal you can navigate to the course root directory and execute:

```
$ uv python install 3.12.7
$ uv venv --python 3.12.7
$ uv sync
```

> If the `uv` command is not recognized, try restarting your terminal.

With that we have our chapter venv installed. When working through the code for a specific chapter, always create a new venv to avoid dependency hell.


### Git Branching Strategy
Please, follow these branch naming and usage conventions in order to keep the repository maintainable and collaborative:

|Branch|	Purpose|
|------|-----------|
|main  |	Stable production-ready code|
|dev   | Ongoing development, always deployable|

All work should be merged into `dev`, and only thoroughly tested code gets merged into `main`.

| Prefix     | Used For               | Branches Off | Example                             |
|------------|------------------------|--------------|-------------------------------------|
| feature/   | New functionality      | `dev`        | `feature/fsm-diff-visualization`    |
| bugfix/    | Bug resolution         | `dev`        | `bugfix/fix-missing-transition`     |
| hotfix/    | Urgent production fix  | `main`       | `hotfix/fix-runtime-error`          |
| release/   | Production releases    | `dev`        | `release/v0.2.0`                    |
| test/      | Experimental testing   | `dev`        | `test/mutation-graph-export`        |
| doc/       | Documentation updates  | `dev`        | `doc/add-readme-branch-strategy`    |

In order to create a branch out of `dev`, for example, you should do the following:

```bash
$ git checkout dev
$ git checkout -b <branch_prefix>/<functionality>
```

### Run Linting and Formatting
```bash
ruff check .          # Check code
ruff check . --fix    # Auto-fix lint issues
black .               # Format code
```

## Contributors
🚧

## Bibliography
🚧

## License
MIT License. Please, look at [LICENSE](./LICENSE) for full context.

