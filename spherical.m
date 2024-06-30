% Define the number of points for each spherical coordinate
num_theta = 50;
num_phi = 100;
num_r = 10;

% Define the ranges for the spherical coordinates
theta = linspace(0, 2*pi, num_theta); % Azimuthal angle
phi = linspace(0, pi, num_phi);       % Polar angle
r = linspace(0, 10, num_r);           % Radial distance

% Create the grid
[Theta, Phi, R] = meshgrid(theta, phi, r);

% Convert spherical coordinates to Cartesian coordinates
X = R .* sin(Phi) .* cos(Theta);
Y = R .* sin(Phi) .* sin(Theta);
Z = R .* cos(Phi);

% Visualize the spherical grid points
scatter3(X(:), Y(:), Z(:), '.');

% Add labels and title
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
title('Spherical Grid Visualization');

% Set aspect ratio for better visualization
axis equal;
grid on;

