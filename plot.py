import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 360p & 1440p
def plot_A(df, res, HR_idx, LR_idx):

    x = [df.loc[row, 'RATIO'] for row in LR_idx]
    y1 = [df.loc[row, 'mAP@50-NoSR'] for row in LR_idx]
    y2 = [df.loc[row, 'mAP@50-BICUBIC'] for row in LR_idx]
    y3 = [df.loc[row, 'mAP@50-FSRCNN'] for row in LR_idx]
    y4 = [df.loc[row, 'mAP@50-BASICVSR++'] for row in LR_idx]

    plt.plot(x, y1, 'o-b', label='mAP@50-NoSR')
    plt.plot(x, y2, 'o-g', label='mAP@50-BICUBIC')
    plt.plot(x, y3, 'o-r', label='mAP@50-FSRCNN')
    plt.plot(x, y4, 'o-c', label='mAP@50-BASICVSR++')
    plt.xlabel('Bitrate Ratio')
    plt.ylabel('mAP@50')
    plt.title(f'bitrate vs mAP@50 w/o {res}')
    plt.xlim(0, 0.1)
    plt.ylim(0, 100)
    plt.legend()
    plt.savefig(f'plot/{res}_bitrate_mAP@50.png', dpi=200, transparent=True)
    plt.clf()    

    HR_x = [df.loc[row, 'RATIO'] for row in HR_idx]
    HR_y = [df.loc[row, 'mAP@50-NoSR'] for row in HR_idx]

    plt.plot(x, y1, 'o-b', label='mAP@50-NoSR')
    plt.plot(x, y2, 'o-g', label='mAP@50-BICUBIC')
    plt.plot(x, y3, 'o-r', label='mAP@50-FSRCNN')
    plt.plot(x, y4, 'o-c', label='mAP@50-BASICVSR++')
    plt.plot(HR_x, HR_y, 'o-m', label=f'mAP@50-{res}')
    plt.xlabel('Bitrate Ratio')
    plt.ylabel('mAP@50')
    plt.title(f'bitrate vs mAP@50 w {res}')
    plt.xlim(0, 0.1)
    plt.ylim(0, 100)
    plt.legend()
    plt.savefig(f'plot/{res}_bitrate_mAP@50_{res}.png', dpi=200, transparent=True)
    plt.clf()

    x2 = [df.loc[row, 'PSNR-BICUBIC'] for row in LR_idx]
    x3 = [df.loc[row, 'PSNR-FSRCNN'] for row in LR_idx]
    x4 = [df.loc[row, 'PSNR-BASICVSR++'] for row in LR_idx]
    x5 = [df.loc[row, 'PSNR-NoSR'] for row in HR_idx[1:]]

    plt.plot(x2, y2, 'o-g', label='PSNR-BICUBIC')
    plt.plot(x3, y3, 'o-r', label='PSNR-FSRCNN')
    plt.plot(x4, y4, 'o-c', label='PSNR-BASICVSR++')
    plt.plot(x5, HR_y[1:], 'o-b', label=f'PSNR-{res}')
    plt.xlabel('PSNR')
    plt.ylabel('mAP@50')
    plt.title('PSNR vs mAP@50')
    plt.xlim(30, 40)
    plt.ylim(0, 70)
    plt.legend()
    plt.savefig(f'plot/{res}_PSNR_mAP@50.png', dpi=200, transparent=True)
    plt.clf()

    plt.plot(x, x2, 'o-g', label='PSNR-BICUBIC')
    plt.plot(x, x3, 'o-r', label='PSNR-FSRCNN')
    plt.plot(x, x4, 'o-c', label='PSNR-BASICVSR++')
    plt.plot(HR_x[1:], x5, 'o-m', label=f'PSNR-{res}')
    plt.xlabel('bitrate')
    plt.ylabel('PSNR')
    plt.title('bitrate vs PSNR')
    plt.xlim(0, 0.1)
    plt.ylim(30, 50)
    plt.legend()
    plt.savefig(f'plot/{res}_bitrate_PSNR.png', dpi=200, transparent=True)
    plt.clf()

def plot_CQPandCRF(df, CRF_row_idx, CQP_row_idx):

    CRF_x = [df.loc[row, 'RATIO'] for row in CRF_row_idx]

    CRF_y1 = [df.loc[row, 'mAP@50-NoSR'] for row in CRF_row_idx]
    CRF_y2 = [df.loc[row, 'mAP@50-BICUBIC'] for row in CRF_row_idx]
    CRF_y3 = [df.loc[row, 'mAP@50-FSRCNN'] for row in CRF_row_idx]
    CRF_y4 = [df.loc[row, 'mAP@50-BASICVSR++'] for row in CRF_row_idx]

    CQP_x = [df.loc[row, 'RATIO'] for row in CQP_row_idx]

    CQP_y1 = [df.loc[row, 'mAP@50-NoSR'] for row in CQP_row_idx]
    CQP_y2 = [df.loc[row, 'mAP@50-BICUBIC'] for row in CQP_row_idx]
    CQP_y3 = [df.loc[row, 'mAP@50-FSRCNN'] for row in CQP_row_idx]
    CQP_y4 = [df.loc[row, 'mAP@50-BASICVSR++'] for row in CQP_row_idx]

    plt.plot(CRF_x, CRF_y1, 'o-b', label='CRF-NoSR')
    plt.plot(CQP_x, CQP_y1, 'o-r', label='QP-NoSR')
    plt.xlabel('Bitrate Ratio')
    plt.ylabel('mAP@50')
    plt.title('CRF/QP')
    plt.legend()
    plt.savefig('plot/CRF_QP_NoSR_mAP@50.png', transparent=True)
    plt.clf()

    plt.plot(CRF_x, CRF_y2, 'o-b', label='CRF-BICUBIC')
    plt.plot(CQP_x, CQP_y2, 'o-r', label='QP-BICUBIC')
    plt.xlabel('Bitrate Ratio')
    plt.ylabel('mAP@50')
    plt.title('CRF/QP')
    plt.legend()
    plt.savefig('plot/CRF_QP_BICUBIC_mAP@50.png', transparent=True)
    plt.clf()

    plt.plot(CRF_x, CRF_y3, 'o-b', label='CRF-FSRCNN')
    plt.plot(CQP_x, CQP_y3, 'o-r', label='QP-FSRCNN')
    plt.xlabel('Bitrate Ratio')
    plt.ylabel('mAP@50')
    plt.title('CRF/QP')
    plt.legend()
    plt.savefig('plot/CRF_QP_FSRCNN_mAP@50.png', transparent=True)
    plt.clf()

    plt.plot(CRF_x, CRF_y4, 'o-b', label='CRF-BASICVSR++')
    plt.plot(CQP_x, CQP_y4, 'o-r', label='QP-BASICVSR++')
    plt.xlabel('Bitrate Ratio')
    plt.ylabel('mAP@50')
    plt.title('CRF/QP')
    plt.legend()
    plt.savefig('plot/CRF_QP_BASICVSR_mAP@50.png', transparent=True)
    plt.clf()


if __name__ == '__main__':

    df = pd.read_csv('nslab_data.csv')

    res = '1440p'
    HR_idx = range(0, 11)
    LR_idx = range(11, 22)
    plot_A(df, res, HR_idx, LR_idx)

    res = '1080p'
    HR_idx = range(28, 39)
    LR_idx = range(39, 50)
    plot_A(df, res, HR_idx, LR_idx)

    # CRF_row_idx = [11,15,17,19,21]
    # CQP_row_idx = [22,23,24,25,26]
    # plot_CQPandCRF(df, CRF_row_idx, CQP_row_idx)
