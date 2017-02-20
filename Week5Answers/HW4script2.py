filename='CMI.csv'
day=[]
temp=[]
obs=[]
with open(filename,"r") as f:
    first_line = f.readline()
    alist = f.read().splitlines()
for line in alist:
    day.append(line.split(',')[1])
    temp.append(line.split(',')[2])
    obs.append(line.split(',')[10])

day.remove('2016-12-20 11:53')
temp.remove('M')
day.remove('2016-05-01 00:00')
temp.remove('M')

temp_float=[float(i) for i in temp]
var_sum=sum(temp_float)
var_avg=var_sum/(len(temp_float))

day_temp=dict(zip(temp_float,day))

high_temp=[i for i in day_temp if i >= 90]
high_temp.sort(reverse=True)

light_snow=int(obs.count("-SN"))
brl_snow=int(obs.count("-SN BR"))
blowing_light=(obs.count("-SN BLSN"))
fzfog_light=(obs.count("-SN FZFG"))
blowing_snow=(obs.count("SN BLSN"))
mist_snow=(obs.count("SN BR"))
fzfog_snow=(obs.count("SN FZFG"))
fog_snow=(obs.count("SN FG"))
heavy_fog=(obs.count("+SN FG"))
all_snow=light_snow + brl_snow + blowing_light + fzfog_light +\
         blowing_snow + mist_snow + fzfog_snow + fog_snow + heavy_fog

num_obs=len(obs)
fraction_snow=float(all_snow/num_obs)

print(num_obs)
print('Reports of Snow', all_snow)
print('Fraction of Reports with Snow', fraction_snow)
print('Highest Temp and Time', high_temp[0], day_temp[high_temp[0]])
print('Mean Temperature', var_avg)

