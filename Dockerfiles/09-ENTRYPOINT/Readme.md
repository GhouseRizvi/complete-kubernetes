Entry point is also used to run the container just like cmd
with few diff
1. we cannot overrite entrypoint (but cmd can be overrriden)
2. entrypoint is used to run the container and cmd is used to run a command inside the container
if we override the entrypoint it won't allow instead it append
the input to the default values.

if you use cmd and entry point here cmd acts as argument provider to entrypoint

like
CMD["google.com]
ENTRYPOINT["ping","-c5"]

so here if command line argument is not provided it'll take the default from cmd

if provided argument like yahoo.com
cmd get overitten with yahoo.com and pass that argument to entrypoint.
