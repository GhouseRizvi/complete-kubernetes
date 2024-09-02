Disadvantages of dockkers:
1. Scalibily :
    Auto scalling 
        if traffic is more it should increate the number of containers
2. Realiability:
    Docker host are vulnerable we cannot shift containers to other hosts immediatly
3. networking;
    we have another network we've host network
    in bridge network sililar king of nework will be created
    if its a host network then the container is directly going to attach the host network
    But inside  the host network we can use the directly host port

    if you have a more container create two container continer cluster then create overlay network
    maintaining these things is very difficult here in docker, we've to do mannually.

4. Storage
    if host storage is crashed we're not going to get the data back
5. Logs
    dokcker logs will give limited logs

Maintaining docker manually is difficlut so we need container orchestration tool to manage it.
6. Monitoring also very difficulty, have to do it mannually.


