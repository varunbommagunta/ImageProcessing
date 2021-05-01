from matplotlib import pyplot as plt
def show(img,edge):
  plt.figure(figsize = (15,10))
  plt.subplot(121)
  plt.imshow(img,cmap = 'gray')
  plt.title("Original Image")
  plt.xticks([])
  plt.yticks([])
  plt.subplot(122)
  plt.imshow(edge,cmap = 'gray')
  plt.title("Edge Image")
  plt.xticks([])
  plt.yticks([]);