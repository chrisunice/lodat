import numpy as np
import statsmodels.api as sm
from scipy.signal import find_peaks


def infer_depressions(depr: np.ndarray):
    """ Inferring the depression centers from how the depression data is distributed """
    # Force to 2-d depray
    depr = np.reshape(depr, (-1, 1))

    # Calculate density of depression distribution
    kde = sm.nonparametric.KDEUnivariate(depr).fit()
    xs = np.linspace(depr.min()*1.25, depr.max()*1.25, 1000)  # restrict range to (0,1)
    density = kde.evaluate(xs)

    # Find peaks
    peak_indices = find_peaks(density)[0]
    depr_centers = np.round(xs[peak_indices], 1)

    return depr_centers.tolist()
