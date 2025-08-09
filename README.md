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

*Run the initialization script:*

```bash
./bin/init
```

This creates an Admin user with name `admin` and with password `admin`.

# Documentation

*Run with the file `run`*

```bash
./bin/start
```

This command creates a tmux session named airflow with windows running the following commands: airflow dag-processor, airflow scheduler, and airflow api-server.

The Airflow API server will start at the default address: [localhost:8080](http://0.0.0.0:8080)

*Stop with the file `stop`*

```bash
./bin/stop
```

This command stop the tmux session.

# Bug report

For issues, bug reports or features demands go [here](https://github.com/Phylosius/airflow_project/issues).
