# Image Processing
<img width="1596" height="688" alt="image" src="https://github.com/user-attachments/assets/163b3059-4d67-420d-a39f-c722de19973c" />

<img width="1596" height="688" alt="image" src="https://github.com/user-attachments/assets/90adaad6-e939-4db7-915f-98c60e28fe35" />


## References
> Textbook digital image processing Gonzalez
> Fundamentals of Image Processing, Hacettepe University.


### What is measured in an image location?
<ul>
  <li>brightness</li>
  <li>color</li>
</ul>
> viewpoint
> illumination conditions
> local geometry
> local material properties

### Discretization
<ul>
  <li>in image space - sampling</li>
  <li>In image brightness - quantization</li>
</ul>
> The image is stored discretely, that is, as an array of numbers (matrix), and each cell represents the brightness level.

### Human eye
Two types of receptor cells in retina:

<ul>
  <li>Cone Receptor cells: 6-7 million → function
in bright light, color sensitive, fine detail</li>
  <li>Rod receptor cells: 75-150 million→function
in dim light, color insensitive, coarse detail</li>
</ul>

### color image
<img width="1330" height="713" alt="image" src="https://github.com/user-attachments/assets/f6fb49ba-ea5b-42be-85e3-8ae5c18b89af" />


### Image Filtering
Filtering out the irrelevant information <br>

f(x) = u(x) + n(x)
<ul>
  <li>Image denoising, image sharpening,
image smoothing, image deblurring, etc.</li>
  <li>Edge detection</li>
  <li>Required for many other image image
manipulation tasks</li>
</ul>

### Edge Detection

Edges: abrupt changes in the intensity , Uniformity of intensity or color <br>
Edges to object boundaries

### Structure-Preserving Smoothing
<img width="1330" height="713" alt="image" src="https://github.com/user-attachments/assets/8281cd7c-fb8a-458c-bcf9-a5920e9a3caa" />
<img width="1330" height="713" alt="image" src="https://github.com/user-attachments/assets/fad215e6-558d-40eb-8954-6261ebb6b598" />

### Prior Shape Guided Segmentation
Incorporate prior shape information into the segmentation process

<img width="1330" height="648" alt="image" src="https://github.com/user-attachments/assets/b78c91f3-441f-42df-ac72-0736c8efee38" />

### Style Transfer

<img width="1330" height="648" alt="image" src="https://github.com/user-attachments/assets/cd3d500e-b09c-48d6-a37d-0e06b25d6d84" />

### Digital camera

A digital camera replaces film with a sensor array
<ul>
  <li>Each cell in the array is light-sensitive diode that converts photons
to electrons</li>
  <li>Two common types: Charge Coupled Device (CCD) , CMOS</li>
  
</ul>
Color typically captured using color mosaic , Demosaicing
<img width="1557" height="358" alt="image" src="https://github.com/user-attachments/assets/17c535ba-52e5-4c2f-a3cd-64f004d85fea" />

### Datatypes for raster images
<ul>
  <li>Bitmaps: boolean per pixel (1bpp)</li>
  <li>Grayscale: integer per pixel</li>
  <li>Color: 3 integers per pixel</li>
  
</ul>

## Light is part of the EM wave
<img width="1566" height="514" alt="image" src="https://github.com/user-attachments/assets/0a8cc264-f57a-4254-a59c-355bab18f20f" />

### Three Attributes of Color
> Luminance (brightness)
> Chrominance
> > Hue (color tone) and Saturation (color purity)
> Represented by a "color cone"

### Trichromatic Color Mixing
> Primary colors for illuminating sources:
> > Red, Green, Blue (RGB)
> > Color monitor works by exciting red, green, blue
phosphors using separate electronic guns
> Primary colors for reflecting sources:
> > Cyan, Magenta, Yellow (CMY)
> > Color printer works by using cyan, magenta,
yellow and black (CMYK) dyes

<img width="1566" height="589" alt="image" src="https://github.com/user-attachments/assets/f10ce7ac-4b69-426a-aaf6-d94583805eab" />

### CIE 1931 XYZ Primaries
> XYZ do not correspond to real color primaries (Y=luminance,
Z=blue, X: mixed). They are imaginary primary colors.
> Using these color matching functions can however represent
any single spectral color using non-negative tristimulus values


### Values Tristimulus

<img width="1595" height="117" alt="image" src="https://github.com/user-attachments/assets/1be5d507-050d-4aa6-8ff2-771b2e61f5be" />

<img width="1595" height="356" alt="image" src="https://github.com/user-attachments/assets/4a6f85c5-5107-427e-b442-87e2907ffad2" />

### Color Representation Models
> Specify the luminance and chrominance
> > CIELAB (nonlinear transformation of XYZ, so that perceived difference in luminance
and chrominance are more uniformly spaced in LAB coordinates)
> > HSI (Hue, saturation, intensity)
> > YIQ (used in analog NTSC color TV)
> > YCbCr (used in digital color TV)

### Comparison of Different Color Spaces
<img width="1595" height="647" alt="image" src="https://github.com/user-attachments/assets/b797b01f-e3c1-42eb-911b-823eee5d73dc" />

### Grayscale Image Specification
> Matrix representation: An image of MxN pixels is represented by
an MxN array, each element being an unsigned integer of 8 bits

### Color Image Specification
<img width="1595" height="551" alt="image" src="https://github.com/user-attachments/assets/c3c063cb-9692-43c3-9e5c-57577a41c7d8" />
### Color Imaging Using Color Filter Arrays
> 1: original scene
> 2: output of a 120x80 pixel sensor with a Bayer filter
> 3: output color coded
> 4: Reconstructed image after interpolating missing colors (demosaicing)

<img width="1595" height="405" alt="image" src="https://github.com/user-attachments/assets/8cb8e3df-3de7-4102-af8a-d1487aa3cff3" />

## Texture
> What are the main difference between different textured surfaces?
> Change in
> > pattern elements
> > repetitions
> Patterns of structure from
> > changes in surface albedo (e.g., printed cloth)
> > changes in surface shape (e.g., bark)
> > many small surface patches (e.g., leaves on a bush)

### Representing Textures - Subelements

<img width="1595" height="189" alt="image" src="https://github.com/user-attachments/assets/6741d50e-fc15-495e-8c11-df8cfc2cddb1" />

To find familiar blocks, we use correlation, which is subtracting the average from each index of the array, multiplying it by the image matrix, and then dividing it by their variance and energy. This gives numbers between one and minus one. One means similarity, zero means dissimilarity, and minus one means similarity has changed by 180 degrees.

### Building a Dictionary
<img width="1595" height="486" alt="image" src="https://github.com/user-attachments/assets/553fd0d7-21c9-4740-961f-bdeced8b278f" />

### Representing a Region
> Cut region into patches
> Vector Quantization
> > Represent a high-dimensional data item with a single number
> > > Find and use the index of the nearest cluster center in dictionary
> > Visual words - a vector of quantized image patches
> Build histogram of resulting numbers

<img width="1595" height="298" alt="image" src="https://github.com/user-attachments/assets/1629a255-3de2-4ed3-80b6-0be4ebbc95fa" />














