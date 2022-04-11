# CS417 - Semester Project

## Running the Program



## My Notes

### How to Structure Data

- For "Global" linear least squares approximation
  - Consider using a np array of rows = number of sensor_readings
  - Two columns per row: X (seconds) and Y (temp reading)
    - Data type for each. Stick with float!
  - Since it's linear... should I consider two X columns??
    - `C0(1) + C1X` -> Meaning [[1, 0], [1, 30], ... [1, 30*row_count]]
  - So... should I break up X and Y into seperate np.arrays?
  
**Whatever you do, make sure to test it with a smaller dataset 
to confirm it's working correctly along the way**


### Tasks

- [X] Setup repo
- [X] Setup Pydoc
- [X] Setup module stubs
- [X] Accept file from command line arg
- [X] Rough-in output
- [X] Pre-process input file
- [X] Print out second-bounds in descending order
- [X] Print out yk in descending order
- [X] Create least squares approximation algorithm
    - [x] Test approx. algorithm with provided data
- [X] Create interpolation algorithm
    - [X] Test interpolation algo with provided data
- [X] Finalize output: Get a pair (C0 and C1) and create a function string
- [ ] Clean up code -> See Submission Guidelines
- [ ] Turn in