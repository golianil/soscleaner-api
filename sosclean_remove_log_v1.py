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
			#trc.list()
			for fl in trc.getmembers():
				if fl.name == file_to_remove:
					print('File need to be removed --> ', fl.name)	
					user_prmpt = input("Do you want to proceed with sosclean log file: Select (y/n)")
					if (user_prmpt == 'y' or user_prmpt == 'Y') :
						continue_remove_file(file_to_remove)
					else:
						print("thank you for collecting Sosreport and Soscleaner ")
						sys.exit(0)

def continue_remove_file(file_rm):
	print('working with file : ' +cleaner_arch_file)
	fl_name, fl_zip = cleaner_arch_file.split('.')[:-1]
	#print(first , '  ' , second)
	#/tmp/soscleaner-2436325166968138.tar.gz
	os.system('gunzip '+cleaner_arch_file) 	
	os.system('tar -vf '+fl_name+'.'+fl_zip+' --delete '+file_rm )
	ret= os.system('gzip '+fl_name+'.'+fl_zip)
	print('return value final', ret) 
	

if __name__ == '__main__':
	cleaner_arch_file = collect_log_file()
	remove_log_file(cleaner_arch_file)
