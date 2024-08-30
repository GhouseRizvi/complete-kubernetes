stop signal is used for how to exit the container
# and the exit signal is used for how to exit the container
exit_signal = "SIGTERM"
docker by default request for exit and wait for sometimes
if it is not exiting it can force kill

* When container recieves stopsignal it can perform
    close db connection
    backup
    stop service
    stop server
    stop container
    