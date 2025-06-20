# An airflow project template.

# Installation

*System dependencies:* [python](https://www.python.org/downloads/), [uv](https://github.com/astral-sh/uv.git), [tmux](https://github.com/tmux/tmux/wiki).

*Clone repository:*

```bash
git clone https://github.com/Phylosius/airflow_project.git
```

*Install pip dependencies:*

```bash
cd airflow_project
uv sync
```

*Create the admin user:*

```bash
./create-admin-user
```

# Documentation

*Run with the file `run`*

```bash
./run
```

This command create a tmux session for named `airflow` with windows with the commands: `airflow dag-processor`, `airflow sheduler` and `airflow api-server`.

The airflow api server is started on the default address ([localhost:8080](http://0.0.0.0:8080))

*Stop with the file `stop`*

```bash
./stop
```