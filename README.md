# DoublePendulum

This series is code that simulates double pendulum dynamics and animates them with PyGame.
I have separated the concerns of dynamics, drawing, and integrating into different modules for versatile use.

The dynamics module uses standard set state, get state, and get state prime funcionality which allows the integrator and drawer to be contructed generally for anything with these functions.

There are two methods of integrating in the integrator and there is a method to draw a single pendulum and a method to draw a double pendulum in the drawer.

Due to the robust nature of the RK4 integrator method I have multiplied the total energy to be draw by multiple factors of ten.  This is so we can see the noise generated by the discrete nature of computer programming.

The value z in the get state prime method is for damping which I have not implemented.
