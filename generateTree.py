from ete3 import Tree

tree = Tree('Bio_2lab/fasttreeRez.txt', format=1)
tree.set_outgroup(
    'lcl|Query_47149_MN514967.1_Dromedary_camel_coronavirus_HKU23_isolate_DcCoV-HKU23/camel/Nigeria/NV1385/2016_complete_genome')

print(tree)
