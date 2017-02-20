#!/bash/usr/python
filename='aravg.ann.land_ocean.90S.90N.v4.0.1.201612.asc'
wxdata={'year':[],'temperature':[]}
with open(filename, "r") as f:
    alist = f.read().splitlines()
for line in alist:
    wxdata['year'].append(int(line.split()[0]))
    wxdata['temperature'].append(float(line.split()[1]))
wxdata['temperature'], wxdata['year']=zip(*sorted(zip(wxdata['temperature'],wxdata['year']),reverse=True))
for x in range(0,10):
    print "year = " + repr(wxdata['year'][x]) +  " temperature = " + repr(wxdata['temperature'][x])
