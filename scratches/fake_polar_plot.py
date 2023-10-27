import numpy as np
import pandas as pd

import plotly.io as pio
import plotly.offline as po
import plotly.graph_objects as go


def gen_fake_xv_data():
    # Make the fuzzball
    look = np.arange(0, 360)
    rcs = np.random.normal(loc=0, scale=3, size=len(look))

    # Add some spikes
    spike_angles = [45, 135, 225, 315]
    # spike_magnitudes = np.random.randint(10, 30, size=4)
    # rcs[spike_angles] = spike_magnitudes

    mag = np.random.randint(40, 50)
    for angle in spike_angles:
        rcs[angle - 2] = mag * 0.25
        rcs[angle-1] = mag * 0.50
        rcs[angle] = mag
        rcs[angle + 1] = mag * 0.50
        rcs[angle + 2] = mag * 0.25

    return pd.DataFrame(
        data=dict(
            Look=look,
            RCS=rcs,

        )
    )


if __name__ == '__main__':
    xv = gen_fake_xv_data()

    fig = go.Figure()
    trace = go.Scatterpolar(
        r=xv.RCS,
        theta=xv.Look,
        line=dict(color='red')
    )
    fig.add_trace(trace)

    fig.update_layout(
        polar=dict(
            bgcolor='rgba(255, 255, 255, 0)',
            radialaxis=dict(
                showgrid=True,
                gridcolor='lightgray',
                range=[-50, 50],
                tickvals=np.arange(-50, 51, 10),  # Set the radial axis tick values
                # ticktext=list(map(str, range(-50, 60, 10)))  # Set the radial axis tick labels
            ),
            angularaxis=dict(
                direction='clockwise',
                rotation=90,
                tickvals=list(range(0, 360, 30)),  # Set the angular axis tick values at 30-degree increments
                ticktext=np.concatenate((np.arange(0, 180, 30), np.arange(-180, 0, 30)))
                # ticktext=list(map(str, range(-180, 180, 30)))
            )
        ),
        paper_bgcolor='black',
        font=dict(color='white'),
        height=800,
        width=800
    )

    # po.plot(fig)

    pio.write_image(fig, r'C:\\Users\\ChrisUnice\\Downloads\\polar_plot.png')

