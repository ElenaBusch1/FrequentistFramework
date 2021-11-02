import matplotlib
matplotlib.use("Agg")
from datetime import datetime  # # Used to compute the execution time
import matplotlib.pyplot as plt
import uproot  # # Used to read data from a root file
import sys, re, os, argparse
import json
import numpy as np
import pyBumpHunter as BH

# from https://stackoverflow.com/a/47626762
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def main(args):

    parser = argparse.ArgumentParser(description='%prog [options]')
    parser.add_argument('--inputfile', dest='inputfile', type=str, required=True, help='Root file with bkg and data histograms')
    parser.add_argument('--datahist', dest='datahist', type=str, default='data', help='data hist name')
    parser.add_argument('--bkghist', dest='bkghist', type=str, default='postfit', help='bkg hist name')
    parser.add_argument('--outputjson', dest='outputjson', type=str, default='BHresults.json', help='Name of output file with BH results')
    parser.add_argument('--inputxmlcard', dest='inputxmlcard', type=str, help='Path of xmlAnaWSBuilder card to insert BlindRange into')
    parser.add_argument('--outputxmlcard', dest='outputxmlcard', type=str, help='Output path of modified xmlAnaWSBuilder card')
    parser.add_argument('--usebinnumbers', dest='usebinnumbers', action='store_true', help='Use bin numbers instead of observable for BlindRange')

    args = parser.parse_args(args)

    # Open the file
    # with uproot.open("../../run/PostFit_nloFit_J100yStar06_templates2021_CT14nnlo_scaledOnly_constr10_bkgonly.root") as file:
    with uproot.open(args.inputfile) as file:

        # Background
        bkg_th1 = file[args.bkghist]
        bkg, bins = bkg_th1.to_numpy()

        # Data
        data_th1 = file[args.datahist]
        data,_ = data_th1.to_numpy()

    # Create a BumpHunter1D class instance
    hunter = BH.BumpHunter1D(
        width_min=2,
        width_max=6,
        width_step=1,
        scan_step=1,
        npe=10000,
        nworker=1,
        seed=666,
        bins=bins)

    # Call the bump_scan method
    print("####bump_scan call####")
    begin = datetime.now()
    hunter.bump_scan(data, bkg, is_hist=True)
    end = datetime.now()
    print(f"time={end - begin}")
    print("")

    # Print bump
    hunter.print_bump_info()
    hunter.print_bump_true(data, bkg, is_hist=True)

    # Get and save tomography plot
    # hunter.plot_tomography(data, is_hist=True, filename="tomography.png")

    # Get and save bump plot
    hunter.plot_bump(data, bkg, is_hist=True, filename="bump.png")

    # Get and save statistics plot
    hunter.plot_stat(show_Pval=True, filename="BH_statistics.png")

    state = hunter.save_state()

    out_dict = {}
    out_dict["pyBHresult"] = state

    if args.usebinnumbers:
        out_dict["MaskMin"] = state["min_loc_ar"][0]
        out_dict["MaskMax"] = state["min_loc_ar"][0]+state["min_width_ar"][0]
    else:
        out_dict["MaskMin"] = bins[state["min_loc_ar"][0]]
        out_dict["MaskMax"] = bins[state["min_loc_ar"][0]+state["min_width_ar"][0]]

    out_dict["BlindRange"] = "%d,%d" % (out_dict["MaskMin"], out_dict["MaskMax"])

    with open(args.outputjson, 'w') as f:
        json.dump(out_dict, f, cls=NumpyEncoder)

    print(out_dict["BlindRange"])

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   