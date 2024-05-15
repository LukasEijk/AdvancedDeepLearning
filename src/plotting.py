from src.plotting_setup import *
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score
import numpy as np

def plot_loss(trn_losses,val_losses ):
    fig, axs = plt.subplots( 1, 1, figsize=(7,5) )

    c1 = 'tab:red'
    c2 = 'tab:green'

    axs.plot( trn_losses, label="train loss", color=c1 )
    axs.plot( val_losses, label="val   loss", color=c2 )

    axs.set_yscale('log')

    axs.set_xlabel( "epoch", fontproperties=axislabelfont )
    axs.set_ylabel( "Binary CE", fontproperties=axislabelfont )

    xticks = [ int(x) for x in axs.get_xticks() ]
    axs.set_xticklabels( xticks, fontproperties=tickfont )

    yticks = axs.get_yticks()
    axs.set_yticklabels( yticks, fontproperties=tickfont )

    axs.legend( loc='best', prop=tickfont )

    fig.tight_layout()
    plt.show()

def closest_point(array, tpr_p=0.3):
    dist = ((array-tpr_p)**2)
    return np.argmin(dist)

def plot_roc_and_efficiency_curves(y_test, test_pred, samp_size):
    fig, ax = plt.subplots(1, 2, figsize=(14,5))

    fpr, tpr, th = roc_curve(y_test[0:samp_size], test_pred)
    auc_score = roc_auc_score(y_test[0:samp_size], test_pred)
    rnd_class = np.linspace(0, 1, 100)

    ax[0].plot(fpr, tpr, label='AUC = {:.2f}'.format(auc_score) )
    ax[0].plot(rnd_class, rnd_class, '--', label='Rnd classifier')
    ax[1].plot(tpr, 1/fpr, label='AUC = {:.2f}\n $1/\epsilon_{{bkg}}$(0.3) = {:.0f}'.format(auc_score, 1/fpr[closest_point(tpr, tpr_p=0.3)]))
    ax[1].plot(rnd_class, 1/rnd_class, '--', label='Rnd classifier')
    ax[1].set_yscale('log')

    ax[0].set_xlabel('$\epsilon_{bkg}$ - FPR', fontproperties=axislabelfont)
    ax[0].set_ylabel('$\epsilon_{s}$ - TPR', fontproperties=axislabelfont)

    ax[1].set_xlabel('$\epsilon_{s}$ - TPR', fontproperties=axislabelfont)
    ax[1].set_ylabel('1/$\epsilon_{bkg}$ - Inverse FPR', fontproperties=axislabelfont)
    for i in range(len(ax)):
        ax[i].legend(prop=axislabelfont)
        ax[i].tick_params(labelsize=axisfontsize)
        ax[i].grid('on')
    plt.show()
