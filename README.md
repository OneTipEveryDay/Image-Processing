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

## Image Transformations
g(x,y)=T[f(x,y)]
> 1. Point operations: operations on single pixels
> 2. Spatial filtering: operations considering pixel neighborhoops
> 3. Global methods: operations considering whole image
### point operations
> Smallest possible neighborhood is of size Ixl
> Process each point independently of the others
> Transformation function T remaps the sample's value: s = T(r)
> > r is the value at the point in question
> > s is the new value in the processed result
> > T is a intensity transformation functio

### Point Processing Examples
<img width="1810" height="766" alt="image" src="https://github.com/user-attachments/assets/96da45cb-cd15-40cd-a950-b8f250aa41be" />

### Point Operations: Contrast stretching and Thresholding
> Contrast stretching: produces an image of higher contrast than the original
> Thresholding: produces a binary (two-intensity level) image  

### Histogram
Histogram: a discrete function h(r) which counts
the number of pixels in the image having intensity r
If h(r) is normalized, it measures the probability of
occurrence of intensity level r in an image
<img width="1810" height="766" alt="image" src="https://github.com/user-attachments/assets/fa27f573-31b8-4ad3-8d84-cf3356ee0eca" />

### Intensity quantization in practice

> Option 1: linear quantization
> > pro: simple, convenient, amenable to arithmetic
> > con: requires more steps (wastes memory)
> Option 2: power-law quantization
> > pro: fairly simple, approximates ideal exponential quantization
> > con: need to linearize before doing pixel arithmetic
> Option 2: floating-point quantization
> > pro: close to exponential; no parameters; amenable to arithmetic
> > con: definitely takes more than 8 bits

### Gamma quantization
Close enough to ideal perceptually uniform exponential
<img width="1810" height="638" alt="image" src="https://github.com/user-attachments/assets/ba064e76-5233-4137-b53c-5fa7eaf8f89b" />

### Images and histograms
<img width="1810" height="605" alt="image" src="https://github.com/user-attachments/assets/7de9041a-458d-4b5a-b5d5-16ed875431b5" />
<img width="1810" height="516" alt="image" src="https://github.com/user-attachments/assets/62372d83-becb-4708-9f9b-a46761d9b58d" />

<img width="1810" height="581" alt="image" src="https://github.com/user-attachments/assets/e2f7ace8-017c-452e-a4e3-41bf29183703" />

<img width="1810" height="758" alt="image" src="https://github.com/user-attachments/assets/66e89775-c890-44d7-a357-269c2faff865" />


### Image Statistics
<img width="1810" height="455" alt="image" src="https://github.com/user-attachments/assets/3051cb09-d23b-4bc3-bfeb-8ec19178d387" />

### Image Entropy
The image entropy specifies the uncertainty in
the image values.Measures the averaged amount of information
required to encode the image values. 
<img width="1810" height="143" alt="image" src="https://github.com/user-attachments/assets/20b15951-5053-4ed8-ab8c-bf63c490f206" />
<img width="1837" height="657" alt="image" src="https://github.com/user-attachments/assets/d89ec624-f74b-4d80-91e1-d3c915efc2cb" />

### Histogram based image distance
> Problem: Given two images A and B whose (normalized) histogram
are P and P define the distance D(A,B) between the images.
<img width="1837" height="355" alt="image" src="https://github.com/user-attachments/assets/8ab11f1a-d5be-4f4f-9679-2198fbaa4cf6" />

## Inage Filtering 
Image filtering: computes a function of a
local neighborhood at each pixel position
Called "Local operator," "Neighborhood
operator," or "Window operator"
> We can transform the signal into repeating blocks, so we can write a Fourier series for it and filter it in the frequency domain by changing the frequency range to achieve the desired result.
<img width="1764" height="635" alt="image" src="https://github.com/user-attachments/assets/76826877-fcdf-4ecd-aebf-44165ab26ebd" />
LPF --> smooth the image

### Common types of noise
> Salt and pepper noise:
>  > random occurrences of black and white pixels
>  Impulse noise:
>  >   random occurrences of white pixels
>   Gaussian noise:
>  > variations in intensity drawn from a Gaussian normal distribution
Idea: Use the information coming from the
neighboring pixels for processing . Design a transformation function of the local
neighborhood at each pixel in the image

### First attempt at a solution
Let's replace each pixel with an average
of all the values in its neighborhood
Moving average in 1D:
<img width="1764" height="465" alt="image" src="https://github.com/user-attachments/assets/20f7ec43-ccd9-422e-8d4e-64c78460e076" />

### Discrete convolution
Simple averaging:every sample gets the same weight
<img width="1764" height="169" alt="image" src="https://github.com/user-attachments/assets/4445b933-b79a-4a2c-a7c2-11af037e61ec" />
Convolution: same idea but with weighted average  , each sample gets its own weight (normally zero far away) . This is all convolution is: it is a moving weighted average
<img width="1764" height="169" alt="image" src="https://github.com/user-attachments/assets/d84122d4-0616-4a80-a556-2bb9e228a317" />
Sequence of weights a[j] is called a filter
Filter is nonzero over its region of support
### Discrete filtering in 2D
Same equation, one more index
<img width="1764" height="132" alt="image" src="https://github.com/user-attachments/assets/dd23dbba-21d8-456b-8074-f421eb5e98fe" />
often apply several filters one after another: (((a * b1) * b2) * b3)

### Image Correlation Filtering
> Center filter g at each pixel in image f
> Multiply weights by corresponding pixels
> Set resulting value in output image h
> g is called a filter, mask, kernel, or template
> Linear filtering is sum of dot product at each pixel position
> Filtering operation called cross-correlation

### Sharpening
<img width="1764" height="559" alt="image" src="https://github.com/user-attachments/assets/58feae39-570d-421a-9933-bbef8c2a218d" />











