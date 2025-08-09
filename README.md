# An airflow project template.

This project can configure and run [Apache Airflow](https://github.com/apache/airflow) on a [tmux session](https://github.com/tmux/tmux/wiki/Getting-Started).
A web interface is available at [localhost:8080](http://0.0.0.0:8080).

# Installation

*System dependencies:* [python](https://www.python.org/downloads/), [uv](https://github.com/astral-sh/uv.git), [tmux](https://github.com/tmux/tmux/wiki).

*Clone repository:*

```bash
git clone https://github.com/Phylosius/airflow_project.git
cd airflow_project
```

*Install pip dependencies:*

__This part is not necessary as the `init` script do it automatically.__
```bash
uv sync
```

*Run the initialization script:*

__This part is not necessary as the `start` script do it automatically.__
```bash
./bin/init
```

This creates an Admin user with name `admin` and with password `admin`.

# Documentation

*Run airflow*

```bash
./bin/start
```

This command creates a tmux session named airflow with windows running respectively the following commands: airflow dag-processor, airflow scheduler, and airflow api-server.

The Airflow API server will start at the default address: [localhost:8080](http://0.0.0.0:8080)

*Stop aiflow*

```bash
./bin/stop
```

This command stop the tmux session.

# Bug report

For issues, bug reports or features demands go [here](https://github.com/Phylosius/airflow_project/issues).
