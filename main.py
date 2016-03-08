import os 
import sys
import gdal
import mapnik

from collections import namedtuple

def create_xml_file(file_name):
    return file_name + ".xml"
    
def main(dem_file, color_relief_file, color_slope_file, output_file):

    print(os.system("gdalinfo -mm " + dem_file))

    gtif = gdal.Open(dem_file)
    srcband = gtif.GetRasterBand(1)
    
    Statistics = namedtuple('Statistics', ['Minimum', 'Maximum', 'Mean', 'StdDev'])
    stats = Statistics._make(srcband.GetStatistics(True, True))
    
    print(gtif.RasterXSize)
    print(gtif.RasterYSize)

    file_name = (".").join(dem_file.split(".")[:-1])
    os.system("gdaldem hillshade " + dem_file + " " + file_name + "_hillshade.tif")

    #colors = []
    #with open(color_relief_file, 'r+') as f: 
    #    for line in f:
    #        colors.append(line.strip().split("\t"))

    #if len(colors[0]) == 3:
    #    increment = (stats.Maximum - stats.Minimum) / (len(colors) - 1)
    #    elevation = [str(stats.Minimum + increment * i) for i in xrange(len(colors))]
    #    with open(color_relief_file, 'w') as f:
    #        for item in zip(elevation, colors):
    #            f.write(item[0] + "\t" + ("\t").join(item[1]) + "\n")
    
    os.system("gdaldem color-relief " + dem_file + " " + color_relief_file + " " + file_name + "_color_relief.tif")
    
    os.system("gdaldem slope " + dem_file + " " + file_name + "_slope.tif")
    
    os.system("gdaldem color-relief " + file_name + "_slope.tif " + color_slope_file + " " + file_name + "_slopeshade.tif")

    map = mapnik.Map(gtif.RasterXSize, gtif.RasterYSize)
    xml_file = create_xml_file(file_name)
    mapnik.load_map(map, xml_file)
    map.zoom_all()

    mapnik.render_to_file(map, output_file)



if __name__ == "__main__":
    try:
        main(*sys.argv[1:])
    except Exception as e:
        print(e)