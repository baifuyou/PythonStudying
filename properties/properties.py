#!/usr/bin/env python
#encoding=UTF-8

import os

class Properties(object):
	data = dict()
	path = None
	def __init__(self, path):
		if os.path.isdir(path):
			raise IOError, "target path is a dir"
		if os.path.exists(path):
			dataFile = open(path, 'r')
			for line in dataFile:
				self.data[ self.getKey(line) ] = self.getValue(line)
		self.path = path
	def getKey(self, line):
		line.strip()
		key = line.split(':')[0]
		key = key.split('=')[0]
		return key.strip()

	def getValue(self, line):
		line.strip()
		if line.split(":")[0] == line:
			value = line.split('=')[1]
		else:
			value = line.split(':')[1]
		return value.strip()
	def getData(self):
		return self.data
	
	def setData(self, fData):
		self.data = fData
	
	def store(self, path = '#'):
		if path == '#':
			path = self.path
		dataFile = open(path, 'w')
		lines = list()
		for key in self.data:
			lines.append(key + ":" + self.data[key] + "\n")
		dataFile.writelines(lines)

def getProperties(path):
	return Properties(path)

