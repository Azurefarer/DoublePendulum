# DoublePendulum
DblPend
This series is code that simulates double pendulum dynamics and animates them with PyGame.
I have separated the concerns of dynamics, drawing, and integrating into different modules for versatile use.

The dynamics module uses standard set state, get state, and get state prime funcionality which allows the integrator and drawer to be contructed generally for anything with these functions.

There are two methods of integrating in the integrator and there is a method to draw a single pendulum and a method to draw a double pendulum in the drawer.
