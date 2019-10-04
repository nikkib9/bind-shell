# bind-shell

Create a bind shell on other's host on port 12345.

"Fully" functioning code:

  Localhost can enter in any command found in the /usr/bin & /usr/sbin folders.
  cd will not work, but if you need to run code from another directory, you can enter: bash -c "cd <directory> ; ./<program>"
  less will not work - enter: set term=vt100 to set the terminal emulator. ess should work fine then.

Other's host will not see any output - only localhost will.
