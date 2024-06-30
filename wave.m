// Define the domain and mesh
real L = 1.0; // Length of the square domain
int n = 30;  // Number of mesh points along each side

mesh Th = square(n, n, [x*L, y*L]);

// Define the finite element space (P1 elements)
fespace Vh(Th, P1);

// Define the functions
Vh u, uOld, uNew;  // u is the displacement, uOld is the previous timestep, uNew is the next timestep
Vh v;  // v is the test function

// Parameters
real c = 1.0;  // Wave speed
real dt = 0.01;  // Time step size
int T = 2;  // Total simulation time

// Initial conditions
u = sin(pi*x)*sin(pi*y);
uOld = u;

// Time-stepping loop
for (real t = 0; t < T; t += dt) {
    problem wave(uNew, v) =
        int2d(Th)(
            (uNew*v/dt^2) - (2*u*v/dt^2) + (uOld*v/dt^2)
            + c^2 * (dx(uNew)*dx(v) + dy(uNew)*dy(v))
        )
        + on(1, 2, 3, 4, uNew = 0); // Boundary conditions (u = 0 on all boundaries)

    // Solve the problem
    wave.solve();

    // Update the previous timesteps
    uOld = u;
    u = uNew;

    // Plot the solution
    plot(u, cmm = "Wave equation solution", value = true, fill = true);
}

// Save the final solution to a file
savevtk("wave_solution.vtk", Th, u, dataname = "u");
