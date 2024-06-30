% Define the grid size and number of points
grid_size = 20;
num_points = 40;
[x, y, z] = ndgrid(linspace(-grid_size, grid_size, num_points));

% Define the wave speed
c = 1;

% Define the initial wave function (e.g., a Gaussian pulse)
sigma = 2;
u0 = exp(- (x.^2 + y.^2 + z.^2) / (2 * sigma^2));

% Define the initial time derivative of the wave function (e.g., zero)
u0_t = zeros(size(u0));

% Time step for simulation
dt = 0.01;
total_time = 2; % Time at which we want to visualize the wave

% Pre-allocate arrays for the wave function at different time steps
u_prev = u0;
u = u0 + dt * u0_t;

% Simulation loop to update the wave function
for t = dt:dt:total_time
    % Compute the Laplacian of u
    laplacian_u = del2(u);

    % Update the wave function using the finite difference method
    u_next = 2 * u - u_prev + (c^2 * dt^2) * laplacian_u;

    % Update the previous and current wave function
    u_prev = u;
    u = u_next;
end

% Visualize the wave function at the specified time
isosurface(x, y, z, u, 0.1); % Adjust the isosurface level as needed
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
title('3D Wave Equation');

% Set aspect ratio and view for better visualization
axis equal;
grid on;
view(3);

