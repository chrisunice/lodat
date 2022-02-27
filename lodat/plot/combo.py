import numpy as np
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from lodat.utils import detection_range
from plotly.subplots import make_subplots
from pandas.core.indexes.multi import MultiIndex


class ComboPlot:

    column_names = ['TestMean', 'TestInterval', 'BaseMean', 'BaseInterval', 'Delta']
    test_color = 'black'
    baseline_color = 'blue'

    def __init__(self, df: pd.DataFrame, title: str = None):
        pio.renderers.default = 'browser'

        self.df = df
        self.title = title
        self._check_input()

    def _check_input(self):
        # Check for input type
        assert isinstance(self.df, pd.DataFrame), 'Input needs to be a pandas data frame'

        # Check for a single index
        assert not isinstance(self.df.index, MultiIndex), 'Input must not be a multi-index data frame'

        # Check for matching column info
        dct = {name: (True if name in self.df.columns else False) for name in self.column_names}
        assert np.all(list(dct.values()))

    def render(self):
        if self.title is not None:
            _titles = (f"{self.title} RCS Measurement", f"{self.title} RCS Differences")
        else:
            _titles = self.title
        fig = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True,
            subplot_titles=_titles,
            specs=[[{"secondary_y": False}],
                   [{"secondary_y": True}]]
        )
        fig.update_xaxes(title_text='Look (deg)', range=[0, 360], dtick=30, row=2, col=1)

        # X-Y plot
        # test data
        test_traces = [
            go.Scatter(
                x=self.df.index,
                y=self.df.TestMean,
                name='Test Geometric Mean',
                marker=dict(color=self.test_color),
                error_y=dict(
                    type='data',
                    array=self.df.TestInterval.apply(lambda x: (x[1] - x[0]) / 2),
                    visible=False
                )
            ),
            go.Scatter(
                x=self.df.index.tolist()+self.df.index.tolist()[::-1],
                y=pd.concat((
                    self.df.TestInterval.apply(lambda x: x[0]),
                    self.df.TestInterval.apply(lambda x: x[1])[::-1]
                )),
                mode='none',
                fill='toself',
                fillcolor=self.test_color,
                opacity=0.2,
                hoverinfo='skip',
                name='Test Uncertainty'
            )
        ]
        fig.add_traces(test_traces, rows=1, cols=1)

        # baseline data
        base_traces = [
            go.Scatter(
                x=self.df.index,
                y=self.df.BaseMean,
                name='Baseline Geometric Mean',
                marker=dict(color=self.baseline_color),
                error_y=dict(
                    type='data',
                    array=self.df.BaseInterval.apply(lambda x: (x[1]-x[0])/2),
                    visible=False
                )
            ),
            go.Scatter(
                x=self.df.index.tolist()+self.df.index.tolist()[::-1],
                y=pd.concat((
                    self.df.BaseInterval.apply(lambda x: x[0]),
                    self.df.BaseInterval.apply(lambda x: x[1])[::-1]
                )),
                mode='none',
                fill='toself',
                fillcolor=self.baseline_color,
                opacity=0.2,
                hoverinfo='skip',
                name='Baseline Uncertainty'
            )
        ]
        fig.add_traces(base_traces, rows=1, cols=1)
        fig.update_yaxes(title_text='RCS (dBsm)', row=1, col=1)

        # Bar plot
        # deltas
        delta_trace = go.Bar(
            x=self.df.index,
            y=self.df.Delta,
            name='Differences',
            marker=dict(color=['red' if delta >= 0 else 'green' for delta in self.df.Delta])
        )
        fig.add_trace(delta_trace, row=2, col=1, secondary_y=False)
        fig.update_yaxes(title_text='Delta (dB)', range=[-12, 12], dtick=3, row=2, col=1, secondary_y=False)
        # TODO add second y-axis
        # # percent change in detection range
        # dr_trace = go.Bar(
        #     x=self.df.index,
        #     y=self.df.Delta,
        #     hoverinfo='none',
        #     visible=False,
        # )
        # fig.add_trace(dr_trace, row=2, col=1, secondary_y=True)
        # fig.update_yaxes(
        #     title_text='Detection Range (%)',
        #     secondary_y=True,
        #     showgrid=False,
        #     range=[-50, 100],
        #     dtick=10,
        #     row=2,
        #     col=1,
        # )

        fig.show()
        return True
