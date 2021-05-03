from pyper import *
import phate
import numpy

print("read in expression data")
r=R(use_pandas=True)
eset = 'data/'+sys.argv[1]
r.assign("eset", eset)
expr  = 'eset <- readRDS(eset)'
r(expr)
res= r.get('eset')
data = res['input_data']['eset']

print("Run PHATE")
phate_op = phate.PHATE()
data_phate = phate_op.fit_transform(data)

print("Save data")
numpy.savetxt("data/phate.csv", data_phate, delimiter=",")
