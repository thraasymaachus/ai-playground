import ephem
import plotly.graph_objects as go
import math
import numpy as np

# Function to convert right ascension and declination to Cartesian coordinates
def ra_dec_to_cartesian(ra, dec, dist):
    phi = np.deg2rad(90 - dec)
    theta = np.deg2rad(ra * 15)
    
    x = dist * np.sin(phi) * np.cos(theta)
    y = dist * np.sin(phi) * np.sin(theta)
    z = dist * np.cos(phi)
    
    return x, y, z

# Define planets
planets = [
    ephem.Sun(),
    ephem.Moon(),
    ephem.Mercury(),
    ephem.Venus(),
    ephem.Mars(),
    ephem.Jupiter(),
    ephem.Saturn(),
    ephem.Uranus(),
    ephem.Neptune(),
]

# Create observer object
observer = ephem.Observer()
observer.date = '2023/04/05'  # Set date

# Get the x, y, and z coordinates of the planets
x, y, z = [], [], []
for planet in planets:
    planet.compute(observer)
    ra, dec, dist = planet.ra, planet.dec, planet.earth_distance
    x_val, y_val, z_val = ra_dec_to_cartesian(ra, dec, dist)
    x.append(x_val)
    y.append(y_val)
    z.append(z_val)

# Create 3D scatter plot
fig = go.Figure(
    data=[
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=6, color='DarkOrange', opacity=0.8),
            text=[planet.name for planet in planets],
            hovertemplate="%{text}<br>x: %{x:.2f}<br>y: %{y:.2f}<br>z: %{z:.2f}<extra></extra>",
        )
    ],
)

# Update plot layout
fig.update_layout(
    title='Position of Astronomical Bodies',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
)

# Show the plot
fig.show()
