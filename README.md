# coding-test

This is the code for the following question: 

a) Write a launch file to launch a turtlesim node with two turtles named “turtle1” and “turtle2”.
Inside this launch file, also run the teleop node to teleop “turtle1”.

b. Write a C++/Python node for the following scenario:
“Turtle1” will be the leader and “Turtle2” will be the follower. The follower must stay behind the
leader and maintain a 0.8-meter distance. If you teleop turtle1, the follower turtle must follow
accordingly.
Hint: You will need to utilize TF library this task.

First clone the repo and build the package
```
cd ~/catkin_ws/src
git clone https://github.com/alam121/coding-test.git
cd ~/catkin_ws
catkin_make
```

# for a 
For this a launch file was written that sets up a turtlesim simulation environment with two turtles and allows keyboard control of first turtles.
Additionally, it spawns a new turtle named "turtle2" at coordinates (4.0, 4.0) within the simulation.


```
roslaunch coding-test turtlesim.launch
```

# for b

I also attempted this using two appraoches:

1) The leader turtle's pose and follower's pose is subsribed and whenever the leader moves, the follower turtle moves towards it until they are within a certain distance (0.8 units), after which the follower stops moving. 

This uses the pose error between the two turtles, and creates a proportional controller to reduce the error, until the error is less than 0.8

To run this->
```
roslaunch coding-test turtlesim.launch
rosrun coding-test follow.py
```

2) Using tf ROS package. This have 3 main parts:

-follow_tf:
The handle_turtle_pose function subsribes the turtle's pose and broadcasts the transform between the turtle and the world frame.

-follow_tf_listener:
It creates a TransformListener object to listen to transform data. It sets up a publisher to send velocity commands to 'turtle2'.
It looks up the transform between 'turtle2' and 'carrot1', calculates linear and angular velocities based on the transform, and publishes the velocity commands.
fixed_frame.

-fixed_frame:

The script creates a TransformBroadcaster object. A fixed transform is broadcasted between two frames: "carrot1" and "turtle1".
The transform consists of a translation of (0.8, 0.8, 0.0) and a rotation of (0.0, 0.0, 0.0, 1.0).

To run this->

```
roslaunch coding-test turtlesim_tf.launch
```
