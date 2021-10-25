from  run_sosreport import sos_report_run
import subprocess
#sosreport_file=''
def run_clean_sosreport():
	sosreport_file = sos_report_run()
	print('Sosreport file is saved in location:', sosreport_file)
	return sosreport_file

def run_sos_cleaner(sos_file):
	#print('entery for .... ', sos_file, end='')
	cmd = '/usr/bin/soscleaner '+ sos_file
	spc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE , stderr=subprocess.PIPE)	
	while spc.poll () is None:
		line_clean = spc.stdout.readline().decode()
		print(line_clean, end='')	 		
		if 'Creating SOSCleaner Archive' in line_clean:
			archive_file = line_clean.split()[-1]
	return archive_file

if __name__ == '__main__':
	sos_file=run_clean_sosreport()
	#sos_file='/var/tmp/sosreport-sos-centos-2021-08-08-qftqesl.tar.xz'
	arch_f = run_sos_cleaner(sos_file)
	print("soscleaner file to investigate: ", arch_f)
	#print(sos_file, end='')
