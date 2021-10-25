import tarfile
import os
import sys
from run_soscleaner import *

def collect_log_file():
	#sos_file='/var/tmp/sosreport-sos-centos-2021-08-08-qftqesl.tar.xz'
	sos_file=run_clean_sosreport()
	arch_f = run_sos_cleaner(sos_file)
	print("soscleaner file to investigate: ", arch_f)
	return arch_f

def remove_log_file(cleaner_arch):
	if os.path.exists(cleaner_arch):
		print(cleaner_arch)
	else:
		print("Archive cleaner file not found !")
		sys.exit()
	file_to_remove = cleaner_arch.split('/')[2].split('.')[0]+'.log'
	print('----> ',file_to_remove)
	with tarfile.open(cleaner_arch, "r:gz") as trc:
		with tarfile.open('/tmp/new-soscleaner.tar.gz', "w:gz") as nrc:
			#trc.list()
			for fl in trc.getmembers():
				if fl.name == file_to_remove:
					continue
				try:
					xtra = trc.extractfile(fl)
				
				except KeyError:
					print('file not found ', fl.name)
				if not xtra:
					continue
				nrc.addfile(fl, xtra)


if __name__ == '__main__':
	cleaner_arch_file = collect_log_file()
	remove_log_file(cleaner_arch_file)
