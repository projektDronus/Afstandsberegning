# coding=utf-8
import sys

FLength = 1015 # udregnet gennem tingene der står i "Den_nemme.txt", 
	      # kræver at man har taget et billede, hvor man kender afstanden til objektet
	      # til en initial udregning.
realWidth = 5.11811024
pixelWidth = float(sys.argv[1])

Distance = (realWidth * FLength)/pixelWidth #udregner længden fra objektet

print "Du er", Distance, "cm fra objektet"
