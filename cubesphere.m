% Define the number of points for each spherical coordinate
num_theta = 40; % Number of azimuthal points
num_phi = 20;   % Number of polar points

% Define the radius of the sphere
radius = 5;

% Define the ranges for the spherical coordinates
theta = linspace(0, 2 * pi, num_theta); % Azimuthal angle
phi = linspace(0, pi, num_phi);         % Polar angle

% Create the grid
[Theta, Phi] = meshgrid(theta, phi);

% Calculate the coordinates of points on the sphere surface
X = radius * sin(Phi) .* cos(Theta);
Y = radius * sin(Phi) .* sin(Theta);
Z = radius * cos(Phi);

% Define the cube vertices
cube_vertices = [-radius, -radius, -radius;
                 radius, -radius, -radius;
                 radius, radius, -radius;
                 -radius, radius, -radius;
                 -radius, -radius, radius;
                 radius, -radius, radius;
                 radius, radius, radius;
                 -radius, radius, radius];

% Define the cube faces
cube_faces = [1 2 3 4;
              5 6 7 8;
              1 2 6 5;
              2 3 7 6;
              3 4 8 7;
              4 1 5 8];

% Create the figure
figure;

% Plot the spherical surface
surf(X, Y, Z);
hold on;

% Plot the cube
patch('Vertices', cube_vertices, 'Faces', cube_faces, ...
      'FaceColor', 'none', 'EdgeColor', 'k', 'LineWidth', 1.5);

% Add labels and title
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
title('Spherical Surface Inside a Cube');

% Set aspect ratio and view for better visualization
axis equal;
grid on;
view(3);

