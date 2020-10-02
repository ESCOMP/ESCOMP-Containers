# CESM module for python - includes toolkit (later) and tutorial stuff
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.util import add_cyclic_point

import cartopy
cartopy.config['pre_existing_data_dir'] = '/srv/conda/envs/default/lib/python3.7/site-packages/cartopy/data'

import os
import glob

def QuickViewATM(case, variable):
  # Currently supported variables:
  supported_3D = ( 'TS', )
  supported_4D = ( 'T', 'U', 'V', )

	# Check if we're using a supported variable:
  supported = supported_3D + supported_4D
  if variable not in supported:
    print('Variable is not supported - must be one of: ', supported)
    return

  # Get the list of all hist files for the atmosphere:
  files = glob.glob('/home/user/archive/' + case + '/atm/hist/*.nc')
  latest = max(files , key = os.path.getctime)
  dataset = xr.open_dataset(latest)

  if variable in supported_3D:
    vardata = dataset[variable][0,:,:]  # Fix the time later
  else:
    vardata = dataset[variable][0,25,:,:] # Fix the level later

  # Set figure size
  fig = plt.figure(figsize=(11,8.5))
  ax = plt.axes(projection=ccrs.Robinson())

  # Add cyclic point to data (to get rid of gap at dateline)
  data, lons = add_cyclic_point(vardata, coord=vardata['lon'])

  # Define contour levels
  clevs=np.arange(np.min(data),np.max(data),1)

  # Make a filled contour plot
  cs=ax.contourf(lons, vardata['lat'], data,clevs, transform = ccrs.PlateCarree(), cmap='coolwarm',extend='both')

  # Add coastlines
  ax.coastlines()

  # Add gridlines
  ax.gridlines()

  # Add colorbar
  cbar = plt.colorbar(cs,shrink=0.7,orientation='horizontal')

  # Add title
  plt.title(case + ' : ' + variable)

def QuickView(case, variable, model='atmosphere'):
  type = model.lower()
  if type in { 'atmosphere', 'atm', 'cam' }:
    QuickViewATM(case, variable)

