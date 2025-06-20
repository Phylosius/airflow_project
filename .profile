
export AIRFLOW_HOME=$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && cd airflow_home && pwd )  # the airflow home directory
export AIRFLOW__WEBSERVER__CONFIG_FILE=$AIRFLOW_HOME/webserver_config.py  # webserver config file
export AIRFLOW__CORE__AUTH_MANAGER=airflow.providers.fab.auth_manager.fab_auth_manager.FabAuthManager  # set the authentication handler
export AIRFLOW__WEBSERVER__RBAC=True  # enable the users command

export AIRFLOW_TMUX_SESSION_NAME="airflow"