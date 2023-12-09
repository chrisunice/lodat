import numpy as np
import plotly.graph_objects as go


if __name__ == '__main__':

    # Constants
    c = 299792458  # Speed of light in m/s

    # Simulation parameters
    frequency = 10e9  # Frequency in Hz (e.g., 10 GHz)
    wavelength = c / frequency
    grid_size = 100  # Number of grid cells in each direction
    grid_resolution = wavelength / 10  # Spatial resolution in meters (lambda/10)
    time_steps = 100  # Number of time steps
    incident_angle = 0  # Incident angle in degrees (Change this to any desired angle)

    # Create a 2D grid for the metallic plate (all cells initialized with 0)
    metallic_plate = np.zeros((grid_size, grid_size), dtype=np.complex128)

    # Set the metallic plate's properties (for simplicity, assume it's a perfect electric conductor)
    metallic_plate[:, grid_size // 2] = np.inf

    # Initialize incident electric field
    incident_field = np.zeros((grid_size, grid_size), dtype=np.complex128)
    incident_field[0, :] = 1.0  # Incident wave is a unit-amplitude pulse at the left boundary

    # Time-stepping loop
    for t in range(time_steps):
        # Update electric field using FDTD algorithm (2D update equation)
        for i in range(1, grid_size - 1):
            for j in range(1, grid_size - 1):
                incident_term = np.exp(1j * 2 * np.pi * frequency * t * grid_resolution / c)
                incident_term *= np.exp(-1j * 2 * np.pi * frequency * np.sin(np.radians(incident_angle)) * j * grid_resolution / c)

                # FDTD update equation
                incident_field[i, j] = (
                    incident_term
                    * (incident_field[i, j] - incident_field[i - 1, j])
                    + (1 - 1j * frequency * grid_resolution / (2 * c))
                    * incident_field[i, j]
                )

        # Apply metallic plate boundary condition (perfect electric conductor)
        incident_field[:, grid_size // 2] = 0

    # Calculate RCS (sum of the scattered field over a specified region)
    # For simplicity, let's assume the region of interest is the rightmost column of the grid.
    RCS = np.abs(np.sum(incident_field[:, -1])) ** 2

    # Print RCS value
    print("Radar Cross-Section (RCS) for incident angle of", incident_angle, "degrees:", RCS, "square meters")

    # Create Plotly surface plot for the incident field amplitude
    x = np.arange(0, grid_size * grid_resolution, grid_resolution)
    y = np.arange(0, grid_size * grid_resolution, grid_resolution)
    X, Y = np.meshgrid(x, y)

    fig = go.Figure(data=go.Surface(x=X, y=Y, z=np.abs(incident_field), colorscale="Jet"))
    fig.update_layout(
        title="RCS Simulation",
        scene=dict(xaxis_title="X (meters)", yaxis_title="Y (meters)", zaxis_title="Electric Field Amplitude"),
    )
    fig.show()
