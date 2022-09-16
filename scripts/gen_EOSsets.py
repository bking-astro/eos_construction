import MR_generator
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Make N EOS sets with specified parameters.')
	parser.add_argument('datapath', metavar='path',
                    help='Directory where data is stored.')
	parser.add_argument('number_tables', metavar='N', type=int,
                    help='Number of tables to generate.')
	parser.add_argument('nsamp', metavar='nsamp', type=int,
                    help='Number of density samples in EOS.')
	parser.add_argument('ext_type', metavar='ext',
                    help='Type of extenstion to perform. Either cs, poly, or lin')

MR_generator.generate_tables(datapath=path, number_tables=N, nsamp_EOS=nsamp, ext_type=ext)

