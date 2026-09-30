from __future__ import annotations
import math
G0=9.80665
C=299_792_458.0
WH_PER_J=1/3600

def symmetric_profile(distance_m,mass_kg,a_g=1.0):
    a=a_g*G0; half=distance_m/2
    t_half=math.sqrt(distance_m/a)
    t_total=2*t_half
    vmax=a*t_half
    ke=0.5*mass_kg*vmax**2
    force=mass_kg*a
    peak_power=force*vmax
    return dict(distance_m=distance_m,mass_kg=mass_kg,a_g=a_g,a_mps2=a,t_half_s=t_half,t_total_s=t_total,vmax_mps=vmax,ke_j=ke,force_n=force,peak_power_w=peak_power)

def sr_check(v):
    beta=v/C
    gamma=1/math.sqrt(1-beta*beta)
    return beta,gamma

def required_stored_energy(ke_j,efficiency=1.0,reserve=0.0,segments=4):
    # Four powered kinetic-energy legs for a symmetric round trip: accelerate/decelerate outbound and inbound.
    return ke_j*segments/(efficiency*(1-reserve))

def sweep(distances_km=(40e6,55e6,75e6),masses_t=(1,5,10,25,50,100),a_gs=(.1,.25,.5,1,2)):
    rows=[]
    for dkm in distances_km:
      for mt in masses_t:
       for ag in a_gs:
        r=symmetric_profile(dkm*1000,mt*1000,ag)
        beta,gamma=sr_check(r['vmax_mps'])
        rows.append({**r,'distance_km':dkm,'mass_t':mt,'beta':beta,'gamma':gamma,
                     'one_way_h':r['t_total_s']/3600,'vmax_km_s':r['vmax_mps']/1000,
                     'ke_mwh':r['ke_j']/3.6e9,'peak_gw':r['peak_power_w']/1e9})
    return rows
