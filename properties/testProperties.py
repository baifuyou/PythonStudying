#!/usr/bin/env python
#encoding=UTF-8

import sys
sys.path.append('~/PythonWork/pythonStudying/properties/')
import properties

prop = properties.getProperties("test.prop")
kvData = prop.getData()
kvData['name'] = 'tom'
prop.store()

kvData['sex'] = 'male'
prop.store("test2.prop")

prop2 = properties.getProperties("test2")
kvData2 = prop2.getData()
print(kvData2)

kvData3 = {'name':'bob','sex':'male'}
prop2.setData(kvData3)
prop2.store('test3.prop')

prop2 = properties.getProperties("test3.prop")
print(prop2.getData())
