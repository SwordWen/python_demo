import h5py
import numpy as np

file = h5py.File ('file.h5', 'w')

dataset = file.create_dataset("dset",(4, 6), h5py.h5t.STD_I32BE)

data = np.zeros((4,6))

dataset[...] = data # write to dataset
read_data = dataset[...] # read from dataset

group = file.create_group ('MyGroup')

#Create string
dataset.attrs["Units"] = "Meters per second"
#Create Intege
attr_data = np.zeros((2,))
attr_data[0] = 100
attr_data[1] = 200
dataset.attrs.create("Speed", attr_data, (2,), "i")


file.close ()
