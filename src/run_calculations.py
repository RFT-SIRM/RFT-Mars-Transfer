import csv,json,sys,os
sys.path.insert(0,os.path.dirname(__file__))
from mission import *
out=os.path.join(os.path.dirname(__file__),'..','results'); os.makedirs(out,exist_ok=True)
r=symmetric_profile(55e9,50e3,1); beta,gamma=sr_check(r['vmax_mps'])
summary={
 'mission':'RFT-Mars-Transfer','mass_kg':50000,'distance_km':55000000,'a_g':1.0,
 'one_way_hours':r['t_total_s']/3600,'round_trip_hours':2*r['t_total_s']/3600,
 'vmax_km_s':r['vmax_mps']/1000,'beta':beta,'gamma':gamma,
 'thrust_kN':r['force_n']/1000,'peak_power_GW':r['peak_power_w']/1e9,
 'kinetic_energy_MWh_one_accel':r['ke_j']/3.6e9,
 'battery_MWh':12000*1500/1e6,
 'round_trip_ideal_kinetic_MWh':4*r['ke_j']/3.6e9,
 'round_trip_battery_energy_ratio':4*r['ke_j']/3.6e9/(12000*1500/1e6),
}
with open(os.path.join(out,'SUMMARY.json'),'w') as f: json.dump(summary,f,indent=2)
rows=sweep()
with open(os.path.join(out,'PARAMETER_SWEEP.csv'),'w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print(json.dumps(summary,indent=2))
