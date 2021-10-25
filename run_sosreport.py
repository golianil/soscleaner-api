'''
  This script is to run the sosreport from python
'''

import subprocess
cmd = ['sosreport', '--batch']
file_sosreport = ''
def sos_report_run():
	sp = subprocess.Popen(cmd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE , stderr=subprocess.PIPE)
	#sp.wait()


	while sp.poll() is None:
	  line = sp.stdout.readline()
	  print(line.decode(), end='')
	  try:
	    line = line.decode()
	    if '/tmp/sosreport'  in line:
	      file_sosreport = line 
	  except AttributeError:
	    pass

	return file_sosreport
	#o, e = sp.communicate()
	#print("output ", file_sosreportlstrip())
	#print("error ", e)

if __name__ == '__main__':
	sos_report_run()
	print("output ", file_sosreport.lstrip())

