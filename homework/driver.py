# DO NOT CHANGE ANY CODE IN THIS SCRIPT
import read

file_path = "./planets.txt"

maximum_distance = read.maxDistance(file_path)
minimum_distance = read.minDistance(file_path)

read.log()
read.reportMax(maximum_distance)
read.reportMin(minimum_distance)
