from psd_tools import PSDImage

psd = PSDImage.open('/Users/dhan/temp/test2.psd')
#psd.composite().save('/Users/dhan/temp/test.png')

# for layer in psd:
#     print(layer)
layer_list = psd.descendants()
#new_layer_list = []
for layer in layer_list[:]:
    """
    layer_name = str(layer.name)
    layer_name = layer_name.replace('"', '')
    layer_name = layer_name.replace(' ', '')
    layer_name = layer_name.replace('.', '')
    layer_name = layer_name.replace('png', '')
    layer_name = layer_name.replace('/', '-')
    """
    #print(layer_name)
    #print("OBJ: ", layer)
    
    if layer.kind == 'type':
        print("NAME: ", layer.name)
        print("Text: ", layer.text)
        #if "325624325624325624" in layer.name:
        layer_list.remove(layer)
    #print('FILE: ', '/Users/dhan/temp/layer/'+str(layer_name)+'.png')

    #layer.compose().save('/Users/dhan/temp/layer/'+str(layer_name)+'.png')
    # print(layer)

    # if layer.kind == 'pixel':
    #     print(layer.name)
    #     print(layer.size)

out_img = psd.composite(layer_filter=lambda layer: layer.kind != 'type')
out_img.save('/Users/dhan/temp/test.png')
