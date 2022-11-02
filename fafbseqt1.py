from fafbseg import flywire
import navis

n = flywire.skeletonize_neuron(720575940629522243, shave_skeleton=True)
navis.heal_fragmened_neuron(n, inplace=True)
n.to_swc('34fafswc')
