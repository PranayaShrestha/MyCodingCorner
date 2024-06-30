pkg load struct;  % Ensure the 'struct' package is loaded for 3D plotting

% Parameters
Lx = 1.0;  % Domain size in x-direction
Ly = 1.0;  % Domain size in y-direction
Lz = 1.0;  % Domain size in z-direction
Nx = 20;   % Number of grid points in x-direction
Ny = 20;   % Number of grid points in y-direction
Nz = 20;   % Number of grid points in z-direction
T = 2.0;   % Total time
dt = 0.01; % Time step
c = 1.0;   % Wave speed

% Grid spacing
dx = Lx / (Nx - 1);
dy = Ly / (Ny - 1);
dz = Lz / (Nz - 1);

% Create 3D grid
[x, y, z] = ndgrid(linspace(0, Lx, Nx), linspace(0, Ly, Ny), linspace(0, Lz, Nz));

% Initial condition
u = sin(pi*x) .* sin(pi*y) .* sin(pi*z);
uold = u;
unew = zeros(size(u));

% Time-stepping loop
for t = dt:dt:T
    % Finite difference approximation of the wave equation
    for i = 2:Nx-1
        for j = 2:Ny-1
            for k = 2:Nz-1
                unew(i, j, k) = 2*u(i, j, k) - uold(i, j, k) ...
                    + (c^2 * dt^2) * ( ...
                        (u(i+1, j, k) - 2*u(i, j, k) + u(i-1, j, k)) / dx^2 + ...
                        (u(i, j+1, k) - 2*u(i, j, k) + u(i, j-1, k)) / dy^2 + ...
                        (u(i, j, k+1) - 2*u(i, j, k) + u(i, j, k-1)) / dz^2);
            end
        end
    end

    % Update the solution
    uold = u;
    u = unew;
end

% Plot the solution at the final time step
[X, Y, Z] = ndgrid(linspace(0, Lx, Nx), linspace(0, Ly, Ny), linspace(0, Lz, Nz));

xlabel('x');
ylabel('y');
zlabel('z');
title(sprintf('Wave function at t = %.2f', t));
colorbar;

