# Things I’ve learned

1. Opening an image in python using PIL
    
    ```python
    from PIL import Image
    
    img = Image.open("Sample.png")
    ```
    
2. Converting an Image to numpy array (`np.asarray()`)
    
    ```python
    from PIL import Image
    from numpy import asarray
    
    # load the image using PIL
    img = Image.open("Sample.png")
    
    # asarray() is used to convert PIL images to Numpy arrays
    numpydata = asarray(img)
    ```
    
3. Using the `.shape`  method in numpy to know the dimensions of an array
    
    ```python
    # since img is RGB numpydata whill have three dimensions (rows, columns, layers)
    print(numpydata.shape) # (200, 400, 3)
    ```
    
4. Converting a np array to Image and saving and showing it using PIL (`PIL.Image.fromarray()`)
    
    ```python
    from PIL import Image
    
    img = Image.fromarray(npArray, mode="RGB")
    img.save("Sample.png") # saving the image localy
    img.show() # showing the image in a window
    ```
    
5. `np.zeros()`

# Resources

[Implementing Bilinear Interpolation for Image Resizing](https://meghal-darji.medium.com/implementing-bilinear-interpolation-for-image-resizing-357cbb2c2722)

Used this very useful guide to implement bilinear interpolation
