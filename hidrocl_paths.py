import os
# import geopandas as gpd
from sys import platform


if platform == "linux" or platform == "linux2":
    nas_path = '/mnt/nas'
    github_path = '/home/aldo/github-hidrocl/HidroCL-DBCreation/'
elif platform == "darwin":
    nas_path = '/private/nfs2'
    github_path = '/Users/aldotapia/Documents/GitHub/HidroCL-OOP/'
# elif platform == "win32":
    # Windows...



# ----
# path to folders
# ----
# observed
mcd12q1_path = os.path.join(nas_path, 'observed/MCD12Q1/')  # lulc
mcd15a2h_path = os.path.join(nas_path, 'observed/MCD15A2H/')  # lai/fpar
mcd43a3_path = os.path.join(nas_path, 'observed/MCD43A3/')  # albedo
mod10a2_path = os.path.join(nas_path, 'observed/MOD10A2/')  # snow
mod13q1_path = os.path.join(nas_path, 'observed/MOD13Q1/')  # vegetation
mod16a2_path = os.path.join(nas_path, 'observed/MOD16A2/')  # et
imerghhl_path = os.path.join(nas_path, 'observed/GPM_3IMERGHHL/')  # pp + other
persiann = os.path.join(nas_path, 'observed/PERSIANN/')  # pp
gldas_noah025_3h_path = os.path.join(nas_path, 'observed/GLDAS_NOAH025_3H/')  # land data

# forecasted

# path to files
hidrocl_sinusoidal = os.path.join(nas_path,
                                  'base/boundaries/HidroCL_boundaries_sinu.shp')  # polys with sinusoidal projection
hidrocl_utm = os.path.join(nas_path, 'base/boundaries/HidroCL_boundaries_utm.shp')
hidrocl_wgs84 = os.path.join(nas_path, 'base/boundaries/HidroCL_boundaries.shp')
hidrocl_north = os.path.join(nas_path, 'static/DEM/HidroCL_north.shp')
hidrocl_south = os.path.join(nas_path, 'static/DEM/HidroCL_south.shp')

# ----
# databases
# ----
# static
# not for this module

# observed
snw_o_modis_sca_cum_n_d8_p0d = os.path.join(nas_path, 'databases/observed/snw_o_modis_sca_cum_n_d8_p0d.csv')
snw_o_modis_sca_cum_s_d8_p0d = os.path.join(nas_path, 'databases/observed/snw_o_modis_sca_cum_s_d8_p0d.csv')
veg_o_modis_ndvi_mean_b_d16_p0d = os.path.join(nas_path, 'databases/observed/veg_o_modis_ndvi_mean_b_d16_p0d.csv')
veg_o_modis_evi_mean_b_d16_p0d = os.path.join(nas_path, 'databases/observed/veg_o_modis_evi_mean_b_d16_p0d.csv')
veg_o_int_nbr_mean_b_d16_p0d = os.path.join(nas_path, 'databases/observed/veg_o_int_nbr_mean_b_d16_p0d.csv')
# sun_o_modis_al_mean_b_d16_p0d = os.path.join(nas_path, 'databases/observed/sun_o_modis_al_mean_b_d16_p0d.csv')
# sun_o_modis_al_p10_b_d16_p0d = os.path.join(nas_path, 'databases/observed/sun_o_modis_al_p10_b_d16_p0d.csv')
# sun_o_modis_al_p25_b_d16_p0d = os.path.join(nas_path, 'databases/observed/sun_o_modis_al_p25_b_d16_p0d.csv')
# sun_o_modis_al_median_b_d16_p0d = os.path.join(nas_path, 'databases/observed/sun_o_modis_al_median_b_d16_p0d.csv')
# sun_o_modis_al_p75_b_d16_p0d = os.path.join(nas_path, 'databases/observed/sun_o_modis_al_p75_b_d16_p0d.csv')
# sun_o_modis_al_p90_b_d16_p0d = os.path.join(nas_path, 'databases/observed/sun_o_modis_al_p90_b_d16_p0d.csv')
et_o_modis_eto_cum_b_d8_p0d = os.path.join(nas_path, 'databases/observed/et_o_modis_eto_cum_b_d8_p0d.csv')
veg_o_modis_lai_mean_b_d8_p0d = os.path.join(nas_path, 'databases/observed/veg_o_modis_lai_mean_b_d8_p0d.csv')
veg_o_modis_fpar_mean_b_d8_p0d = os.path.join(nas_path, 'databases/observed/veg_o_modis_fpar_mean_b_d8_p0d.csv')
pp_o_imerg_pp_mean_b_d_p0d = os.path.join(nas_path, 'databases/observed/pp_o_imerg_pp_mean_b_d_p0d.csv')

# forecasted

# ----
# pixel count databases
# ----
# static

# observed
veg_o_modis_ndvi_mean_pc = os.path.join(nas_path, 'pcdatabases/observed/veg_o_modis_ndvi_mean_pc.csv')
veg_o_modis_evi_mean_pc = os.path.join(nas_path, 'pcdatabases/observed/veg_o_modis_evi_mean_pc.csv')
veg_o_int_nbr_mean_pc = os.path.join(nas_path, 'pcdatabases/observed/veg_o_int_nbr_mean_pc.csv')
snw_o_modis_sca_cum_n_pc = os.path.join(nas_path, 'pcdatabases/observed/snw_o_modis_sca_cum_n_pc.csv')
snw_o_modis_sca_cum_s_pc = os.path.join(nas_path, 'pcdatabases/observed/snw_o_modis_sca_cum_s_pc.csv')
et_o_modis_eto_cum_b_pc = os.path.join(nas_path, 'pcdatabases/observed/et_o_modis_eto_cum_b_pc.csv')
veg_o_modis_lai_mean_b_pc = os.path.join(nas_path, 'pcdatabases/observed/veg_o_modis_lai_mean_b_pc.csv')
veg_o_modis_fpar_mean_b_pc = os.path.join(nas_path, 'pcdatabases/observed/veg_o_modis_fpar_mean_b_pc.csv')
pp_o_imerg_pp_mean_b_pc = os.path.join(nas_path, 'pcdatabases/observed/pp_o_imerg_pp_mean_b_pc.csv')

# forecasted

# ----
# log files
# ----
# observed
log_snw_o_modis_sca_cum = os.path.join(nas_path, 'logs/log_snw_o_modis_sca_cum.txt')
log_veg_o_modis_ndvi_mean = os.path.join(nas_path, 'logs/log_veg_o_modis_ndvi_mean.txt')
log_veg_o_modis_evi_mean = os.path.join(nas_path, 'logs/log_veg_o_modis_evi_mean.txt')
log_veg_o_int_nbr_mean = os.path.join(nas_path, 'logs/log_veg_o_int_nbr_mean.txt')
# log_sun_o_modis_al_mean_b_d16_p0d = os.path.join(nas_path, 'logs/log_sun_o_modis_al_mean_b_d16_p0d.txt')
# log_sun_o_modis_al_median_b_d16_p0d = os.path.join(nas_path, 'logs/log_sun_o_modis_al_median_b_d16_p0d.txt')
# log_sun_o_modis_al_p90_b_d16_p0d = os.path.join(nas_path, 'logs/log_sun_o_modis_al_p90_b_d16_p0d.txt')
# log_sun_o_modis_al_p10_b_d16_p0d = os.path.join(nas_path, 'logs/log_sun_o_modis_al_p10_b_d16_p0d.txt')
# log_sun_o_modis_al_p25_b_d16_p0d = os.path.join(nas_path, 'logs/log_sun_o_modis_al_p25_b_d16_p0d.txt')
# log_sun_o_modis_al_p75_b_d16_p0d = os.path.join(nas_path, 'logs/log_sun_o_modis_al_p75_b_d16_p0d.txt')
log_et_o_modis_eto_cum_b_d8_p0d = os.path.join(nas_path, 'logs/log_et_o_modis_eto_cum_b_d8_p0d.txt')
log_veg_o_modis_lai_mean = os.path.join(nas_path, 'logs/log_veg_o_modis_lai_mean.txt')
log_veg_o_modis_fpar_mean = os.path.join(nas_path, 'logs/log_veg_o_modis_fpar_mean.txt')
log_pp_o_imerg_pp_mean = os.path.join(nas_path, 'logs/log_pp_o_imerg_pp_mean.txt')

# forecasted

"""
polys = gpd.read_file(hidrocl_sinusoidal)  # for getting gauge_id values
catchment_names = polys.gauge_id.tolist()
del polys
"""