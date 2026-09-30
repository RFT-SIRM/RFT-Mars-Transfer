import math,sys
sys.path.insert(0,'src')
from mission import *

def test_55m_1g_50t():
 r=symmetric_profile(55_000_000_000,50_000,1)
 assert abs(r['t_total_s']/3600-41.60528505193368)<1e-6
 assert abs(r['vmax_mps']/1000-734.4152435781817)<1e-9
 assert abs(r['force_n']-490332.5)<1e-6

def test_round_trip_time():
 r=symmetric_profile(55e9,50e3,1)
 assert abs(2*r['t_total_s']/3600-83.21057010386735)<1e-6

def test_energy_kinetic():
 r=symmetric_profile(55e9,50e3,1)
 assert abs(r['ke_j']/3.6e9-3.745595486111111e6)<1

def test_battery_gap():
 r=symmetric_profile(55e9,50e3,1)
 battery=12_000*1500/1e6
 ratio=(4*r['ke_j']/3.6e9)/battery
 assert ratio>200_000

def test_sr_small_correction():
 r=symmetric_profile(55e9,50e3,1)
 beta,gamma=sr_check(r['vmax_mps'])
 assert beta<0.0025 and gamma<1.000004

def test_parameter_sweep_count():
 rows=sweep()
 assert len(rows)==3*6*5

def test_energy_function():
 r=symmetric_profile(55e9,50e3,1)
 e=required_stored_energy(r['ke_j'],.9,.1,4)
 assert math.isclose(e,4*r['ke_j']/(.9*.9),rel_tol=1e-12)
