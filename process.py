#!/usr/bin/python

import fiona
import sys

input = fiona.open(sys.argv[1])
file_name_field = sys.argv[2]

for f in input:
  filename = f['properties'][file_name_field] + '.geojson'
  output = fiona.open(filename, 'w', schema = input.schema, driver='GeoJSON')
  output.write(f)
  output.close()



