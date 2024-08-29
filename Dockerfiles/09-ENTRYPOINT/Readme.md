Entry point is also used to run the container just like cmd
with few diff
1. we cannot overrite entrypoint (but cmd can be overrriden)
2. entrypoint is used to run the container and cmd is used to run a command inside the container
if we override the entrypoint it won't allow instead it append
the input to the default values.
