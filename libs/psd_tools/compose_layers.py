import psd_tools

psd = psd_tools.PSDImage.open('/Users/dhan/temp/test2.psd')
layer_list = psd.descendants()

img_out = psd_tools.compose(layer_list)
img_out.save('/Users/dhan/temp/test2.png')