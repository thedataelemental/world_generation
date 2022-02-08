This is a crude random terrain generator.
Right now it just creates islands with appropriate shorelines.
Graphics are placeholder.
You'll need to install PyGame to run this on your computer.

Internal world representation is a 2D array.

It first fills the array with random 1s and 0s, for land and water.

From there, it uses the data from the first array to fill out a second array with a wider range of possible characters, in appropriate patterns.

PyGame then takes the second array and uses it to determine which tiles to display on the screen.


Jackie P / TheDataElemental
2/7/22
