import numpy as np
import matplotlib.pyplot as plt


def plot(Y, F, n):
    fig, axes = plt.subplots(2, 2)

    for index in range(Y.shape[1]):
        ax = axes[0][index]  # real and estimated graphs
        norm_ax = axes[1][index]  # abs residual graph
        ax.set_xticks(np.arange(0, n + 1, 5))
        ax.plot(np.arange(1, n + 1), Y[:, index],
                'r-', label='$Y_{0}$'.format(index + 1))
        ax.plot(np.arange(1, n + 1), F[:, index],
                'b-', label='$F_{0}$'.format(index + 1))
        ax.legend(loc='upper right', fontsize=16)
        ax.set_title('Coordinate {0}'.format(index + 1))
        ax.grid()

        norm_ax.set_xticks(np.arange(0, n + 1, 5))
        norm_ax.plot(np.arange(1, n + 1),
                     abs(Y[:, index] - F[:, index]), 'g-')
        norm_ax.set_title('Residual {0}'.format(index + 1))
        norm_ax.grid()

    manager = plt.get_current_fig_manager()
    manager.set_window_title('Graph')
    plt.show()