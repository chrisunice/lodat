# Imports
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from lodat.data import DataObject


# Helper functions
def percentile_inclusive(arr, q):
    return np.percentile(arr, q, method='linear')


def percentile_exclusive(arr, q):
    return np.percentile(arr, q, method='weibull')


# Main code
if __name__ == '__main__':

    # parameters
    num_bins = 61
    mc_iterations = int(1e4)
    min_num_hits = 4
    max_num_hits = 50
    colors = sns.color_palette()

    # region Study #1. Cramm vs. P50
    cramms = []
    p50s = []
    higher = []
    for i in range(mc_iterations):
        rand_num_hits = np.random.randint(min_num_hits, max_num_hits)
        rand_rcs = np.random.rand(rand_num_hits,) * 10

        cramm = np.percentile(rand_rcs, 50, method='lower')
        p50 = np.percentile(rand_rcs, 50, method='midpoint')
        high = np.percentile(rand_rcs, 50, method='higher')

        cramms.append(cramm)
        p50s.append(p50)
        higher.append(high)

    fig, ax0 = plt.subplots()
    fig.subplots_adjust(left=0.05, right=0.95)
    fig.set_size_inches((16, 9))
    # fig.suptitle

    # Subplot 1
    title = 'Cramm Median (P50 Lower) vs. Median (P50 Midpoint) Distributions\n' \
            f"Random Measurements $\it{{D:[0, 10)}}$\t" \
            f"Random Sample Size = $\it{{D:[4, 50)}}$\t" \
            f"Iterations = {mc_iterations}"
    ax0.set_title(title)
    ax0 = sns.kdeplot(cramms, shade=True, color=colors[0], label='P50 (lower)', ax=ax0)
    ax0 = sns.kdeplot(p50s, shade=True, color=colors[1], label='P50 (midpoint)', ax=ax0)
    y0, y1 = ax0.get_ylim()
    ax0.vlines(
        np.mean(cramms),
        ymin=y0, ymax=y1,
        colors=colors[0],
        linestyles='dashed',
        label=f'Mean: {np.mean(cramms):.2f}'
    )
    ax0.vlines(
        np.mean(p50s),
        ymin=y0, ymax=y1,
        colors=colors[1],
        linestyles='dashed',
        label=f'Mean: {np.mean(p50s):.2f}'
    )
    ax0.legend()
    ax0.set_xlabel('Measurements')

    # # Subplot 2
    # title = 'Cramm Median (P50 Lower) vs. P50 (Higher) Distributions\n' \
    #         f"Random Measurements $\it{{D:[0, 10)}}$\t" \
    #         f"Random Sample Size $\it{{D:[4, 50)}}$\t" \
    #         f"Iterations = {mc_iterations}"
    # ax1.set_title(title)
    # ax1 = sns.kdeplot(cramms, shade=True, color=colors[0], label='P50 (lower)', ax=ax1)
    # ax1 = sns.kdeplot(higher, shade=True, color=colors[2], label='P50 (higher)', ax=ax1)
    # y0, y1 = ax1.get_ylim()
    # ax1.vlines(
    #     np.mean(cramms),
    #     ymin=y0, ymax=y1,
    #     colors=colors[0],
    #     linestyles='dashed',
    #     label=f'Mean: {np.mean(cramms):.2f}'
    # )
    # ax1.vlines(
    #     np.mean(higher),
    #     ymin=y0, ymax=y1,
    #     colors=colors[2],
    #     linestyles='dashed',
    #     label=f'Mean: {np.mean(higher):.2f}'
    # )
    # ax1.legend()
    # ax1.set_xlabel('Measurements')
    #
    # # Subplot 3
    # title = 'Median (P50 Midpoint) vs. P50 (Higher) Distributions\n' \
    #         f"Random Measurements $\it{{D:[0, 10)}}$\t" \
    #         f"Random Sample Size $\it{{D:[4, 50)}}$\t" \
    #         f"Iterations = {mc_iterations}"
    # ax2.set_title(title)
    # ax2 = sns.kdeplot(p50s, shade=True, color=colors[1], label='P50 (lower)', ax=ax2)
    # ax2 = sns.kdeplot(higher, shade=True, color=colors[2], label='P50 (midpoint)', ax=ax2)
    # y0, y1 = ax2.get_ylim()
    # ax2.vlines(
    #     np.mean(p50s),
    #     ymin=y0, ymax=y1,
    #     colors=colors[1],
    #     linestyles='dashed',
    #     label=f'Mean: {np.mean(p50s):.2f}'
    # )
    # ax2.vlines(
    #     np.mean(higher),
    #     ymin=y0, ymax=y1,
    #     colors=colors[2],
    #     linestyles='dashed',
    #     label=f'Mean: {np.mean(higher):.2f}'
    # )
    # ax2.legend()
    # ax2.set_xlabel('Measurements')

    # endregion

    # region Study #2. P90 Inclusive vs. P90 Exclusive
    # uniform distribution
    random_samples = np.random.rand(num_bins, mc_iterations) * 100

    # Definition 6 - Weibull and Gumbel 1939
    weibull = np.percentile(random_samples, q=50, axis=0, method='weibull')

    # Definition 7 - Gumbel 1939
    gumbel = np.percentile(random_samples, q=50, axis=0, method='linear')

    # Definition 8 - Median unbiased Reiss 1989
    reiss = np.percentile(random_samples, q=50, axis=0, method='median_unbiased')

    fig, ax = plt.subplots()
    fig.set_size_inches((16, 9))
    fig.suptitle('P90 Inclusive vs. P90 Exclusive Distributions')
    ax = sns.kdeplot(weibull, shade=True, color=colors[0], label='Weibull\nExcel PERCENTILE.EXC', ax=ax)
    y0, y1 = ax.get_ylim()
    ax.vlines(
        np.mean(weibull),
        ymin=y0, ymax=y1,
        colors=colors[0],
        linestyles='dashed',
        label=f'Mean: {np.mean(weibull):.2f}'
    )
    ax.vlines(
        np.median(weibull),
        ymin=y0, ymax=y1,
        colors=colors[0],
        linestyles='solid',
        label=f'Median: {np.median(weibull):.2f}'
    )
    ax = sns.kdeplot(gumbel, shade=True, color=colors[1], label='Modal\nPERCENTILE.INC', ax=ax)
    ax.vlines(
        np.mean(gumbel),
        ymin=y0, ymax=y1,
        colors=colors[1],
        linestyles='dashed',
        label=f'Mean: {np.mean(gumbel):.2f}'
    )
    ax.vlines(
        np.median(gumbel),
        ymin=y0, ymax=y1,
        colors=colors[1],
        linestyles='solid',
        label=f'Median: {np.median(gumbel):.2f}'
    )
    # ax = sns.kdeplot(reiss, shade=True, color=colors[2], label='Reiss (Exclusive)', ax=ax)
    # ax.vlines(
    #     np.mean(reiss),
    #     ymin=y0, ymax=y1,
    #     colors=colors[2],
    #     linestyles='dashed',
    #     label=f'Mean: {np.mean(reiss):.2f}'
    # )
    ax.legend(loc='upper left')
    ax.set_title(
        f"Random Measurements $\it{{D:[0, 100)}}$\tSample Size = {num_bins}\tIterations = {mc_iterations}"
    )
    # endregion

    # region Study #3: Combination of P50 and P90
    obj = DataObject(r"C:\LODAT\test_assets\baseline_data.csv")
    xv_upper_front = obj.slice_data(10000, 'VV', 0, 2.5, (61, 5))
    bin_rcs = []
    for look in np.concatenate((np.arange(330, 360, 1), np.arange(0, 31, 1))):

        l0 = look - 0.5
        l1 = look + 0.5

        if l0 < 0:
            l0 += 360
            look_mask = np.logical_or(xv_upper_front.Look >= l0, xv_upper_front.Look < l1)
        else:
            look_mask = np.logical_and(xv_upper_front.Look >= l0, xv_upper_front.Look < l1)

        bin_data = xv_upper_front[look_mask]
        cramm = np.percentile(bin_data.RCS, q=50, method='lower')
        bin_rcs.append(cramm)

    fig, ax = plt.subplots()
    ax = sns.kdeplot(bin_rcs, shade=True, ax=ax, label='P90')
    ax = sns.kdeplot(xv_upper_front.RCS, shade=True, ax=ax, label='P90 of P50s')
    ax.legend()

    #
    random_samples = np.random.randn(num_bins, mc_iterations) * 10        # notional target 0 to 10 dBsm
    bin_data = np.percentile(random_samples, q=50, axis=0, method='lower')
    merge_data = random_samples.ravel()

    fig, ax = plt.subplots()
    ax = sns.kdeplot(bin_data, shade=True, ax=ax, label='bin data')
    ax = sns.kdeplot(merge_data, shade=True, ax=ax, label='merge data')
    ax.legend()


    # end region