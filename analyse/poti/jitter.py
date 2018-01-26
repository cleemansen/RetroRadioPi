# Retrievs the min and max value from the connected ADC in the given time.
# Usage:
# - determine the jitter
# - determine the characteristic of the poti (linear, log, ...)

from mcp3208 import MCP3208
import time
import sys

adc = MCP3208()
crt_val = None
min_val = None
max_val = None
r_max = float(4096)

for i in range(100): 
	crt_val = adc.read(0)
	if min_val is None:
		print('init min and max w/ {:.3f}'.format(crt_val))
		min_val = crt_val
		max_val = crt_val
	else:
		if crt_val < min_val:
			print('new min is {:.3f}'.format(crt_val))
			min_val = crt_val
		if crt_val > max_val:
			print('new max is {:.3f}'.format(crt_val))
			max_val = crt_val
	last_val = crt_val
	if (i % 10 == 0):
		print('{}%'.format(i))
	time.sleep(0.02)

print('angle {}: min_val {:.3f}, max_val {:.3f}'.format(sys.argv[1], min_val / r_max, max_val / r_max))
