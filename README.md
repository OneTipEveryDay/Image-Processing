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

## Morphological Image Processing
> Binary dilation and erosion
Set-theoretic interpretation
Opening, closing, morphological edge detectors
Hit-miss filter
Morphological filters for gray-level images
Cascading dilations and erosions
Rank filters, median filters, majority filters

### Shift invariance
Assume that digital images f [x,y] and g [x,y] have infinite support <br>
[x,y]  E {,-2,-1,0,1,2,}x{-2,-1,0,1,2,}
then, for all integers a and Ь
<img width="1573" height="273" alt="image" src="https://github.com/user-attachments/assets/50e249fe-4016-40b3-a610-1c37a4b36594" />

### Structuring Element
Neighborhood "window" operator

<img width="1573" height="207" alt="image" src="https://github.com/user-attachments/assets/29c69189-9e5a-4fae-9269-c2f012ea081b" />
Example structuring elements Пxy:

<img width="1573" height="285" alt="image" src="https://github.com/user-attachments/assets/51e9ec8f-ba80-45cc-aff9-a60127488f5d" />

### Binary dilation (expanding foreground)

<img width="1701" height="644" alt="image" src="https://github.com/user-attachments/assets/749de6ab-a53e-4fdb-825d-27da54e2792f" />
> Expands the size of 1-valued objects
> Smoothes object boundaries
> Closes holes and gaps


### Binary erosion (shrinking foreground)

<img width="1701" height="524" alt="image" src="https://github.com/user-attachments/assets/2add5817-d85c-47fc-8ae4-5e2c9fbdd480" />
### Relationship between dilation and erosion
Duality: erosion is dilation of the background , But: erosion is not the inverse of dilation

<img width="1701" height="249" alt="image" src="https://github.com/user-attachments/assets/7077081f-9228-49fa-bb19-7059beebe6f1" />

### Set-theoretic interpretation
> Set of object pixels, Continuous (x,y).  Works for discrete [x,y]  in the same way.

<img width="809" height="88" alt="image" src="https://github.com/user-attachments/assets/476fd798-506b-4f53-9c7b-f83a374269e3" />

> Background: complement of foreground set


<img width="809" height="88" alt="image" src="https://github.com/user-attachments/assets/5e8338f2-b13d-4b53-96d2-69e8b1c4bb89" />
> Dilation is Minkowski set addition

<img width="937" height="317" alt="image" src="https://github.com/user-attachments/assets/98315eb9-36b8-42a1-911a-b2d5532feb86" />

### Opening and closing
> Goal: smoothing without size change
> Open filter open(f,W)= dilate(erode(f,W),w)
> Close filter close(f,W)= erode{dilate(f,w),w)
> Open filter and close filter are biased
> > Open filter removes small 1-regions
> > Close filter removes small 0-regions
> Unbiased size-preserving smoothers
close- open(f,W)= close(open(f,W),W)
open- close(f,W)=open(close(f,W),W)
> close-open and open-close are duals, but not inverses of each other.
opening

<img width="1730" height="663" alt="image" src="https://github.com/user-attachments/assets/efa771f9-f2de-427f-bf94-6c8381ea542a" />

closing

<img width="1730" height="663" alt="image" src="https://github.com/user-attachments/assets/1994b2e1-3087-4233-b8bb-5ef075127b26" />

### An Example of Opening & Closing
> An opening removes all noise
> > removing the white noise by erosion
> > removing the black noise by dilation
> An additional closing fills the gaps


<img width="1730" height="472" alt="image" src="https://github.com/user-attachments/assets/ae40bdb5-5d6e-44e1-9dba-568a2376156c" />

### Morphological filters for gray-level images
> Threshold sets of a gray-level image f [x,y] (aka level sets)

<img width="1730" height="78" alt="image" src="https://github.com/user-attachments/assets/ea2441e1-2feb-48d7-9ab9-235b6338394a" />
> Reconstruction of original image from threshold sets

<img width="1730" height="78" alt="image" src="https://github.com/user-attachments/assets/8241616f-8a23-4335-b961-ff580ff22109" />
### Dilation/erosion for gray-level images
> Explicit decomposition into threshold sets not required in practice
> Flat dilation operator: local maximum over window W

<img width="1730" height="78" alt="image" src="https://github.com/user-attachments/assets/61372c37-aa94-403c-9bfd-858fdf24f0e2" />
> Flat erosion operator: local minimum over window W

<img width="1730" height="78" alt="image" src="https://github.com/user-attachments/assets/68c7bcea-65af-442e-95f9-eda944ba0ad2" />
### 1-d illustration of erosion and dilation

<img width="1729" height="656" alt="image" src="https://github.com/user-attachments/assets/99251516-9a4f-4c7c-9808-48238e422896" />
### Beyond flat morphological operators
> General dilation operator Like linear convolution, with sup replacing summation, addition replacing multiplication

<img width="1740" height="105" alt="image" src="https://github.com/user-attachments/assets/f0ac030b-c5a7-43b2-beb1-82a156bc9c8e" />

> Dilation with "unit impulse"

<img width="1740" height="133" alt="image" src="https://github.com/user-attachments/assets/a4d2275f-92ad-4f0f-91fd-29b5a1b01859" />

### erosions Cascaded 
> Cascaded erosions can be lumped into single erosion
erode [erode (f, w₁), w2] = erode [-dilate (-f, w₁), w₂]
= -dilate [dilate (-f, ŵ₁), ŵ2]
= -dilate (-f,w)
= erode (f, w)
where w = dilate (w1, W2)
### Fast dilation and erosion
> Idea: build larger dilation and erosion operators by cascading simple, small operators
>Example: binary erosion by 11x11 window
### Rank Filters
> Generalisation of flat dilation/erosion: in lieu of min or max value in window, use the p-th ranked value
> Increases robustness against noise
> Best-known example: median filter for noise reduction
> Concept useful for both gray-level and binary images
> All rank filters are commutative with thresholding

## Edge detection
> Goal: Identify sudden changes (discontinuities) in an image
> > Intuitively, most semantic and shape information from the image can be encoded in the edges
> > More compact than pixels
> Ideal: artist's line drawing (but artist is also using object - level knowledge)

### Gradient-based edge detection
> Idea (continous-space): local gradient magnitude indicates edge strength
> Digital image: use finite differences to approximate derivatives
> Edge templates


<img width="1557" height="488" alt="image" src="https://github.com/user-attachments/assets/dbf224b3-b838-4f35-ad86-33fcbc8560aa" />

###  Laplacian operator
> Detect edges by considering second derivative

<img width="1582" height="156" alt="image" src="https://github.com/user-attachments/assets/f869b7a1-7d38-41c8-8f4c-f8d85bb84319" />

> Isotropic (rotationally invariant) operator
> Zero-crossings mark edge location

### Canny edge detector
> Smooth image with a Gaussian filter
> Approximate gradient magnitude and angle (use Sobel, Prewitt...)

<img width="1582" height="217" alt="image" src="https://github.com/user-attachments/assets/7be59bfa-5418-447e-814c-831ab5009e5f" />

> Apply nonmaxima suppression to gradient magnitude
> Double thresholding to detect strong and weak edge pixels
> Reject weak edge pixels not connected with strong edge pixels
### Hough transform
> Problem: fit a straight line (or curve) to a set of edge pixels
> Hough transform (1962): generalized template matching technique
> Consider detection of straight lines y = mx + c <br>
> Subdivide (m,c) plane into discrete "bins," initialize all bin counts by 0
> Draw a line in the parameter space [m,c] for each edge pixel [x,y] and
> increment bin counts along line.
> Detect peak(s) in [m,c] plane

<img width="1549" height="442" alt="image" src="https://github.com/user-attachments/assets/8e5eb0f1-b3fd-41a4-b10f-18480ad00bf9" />
## Image segmentation
Goal: identify groups of pixels that go together and  Separate image into coherent "objects"
### What is segmentation?
> Clustering image elements that "belong together"
>Partitioning
> > Divide into regions/sequences with coherent internal properties
> Grouping
> > Identify sets of coherent tokens in image

### Segmentation methods
> Segment foreground from background
> Histogram-based segmentation
> Segmentation as clustering
> > K-means clustering
> > Mean-shift segmentation
> Graph-theoretic segmentation
> > Min cut
> >‌ Normalized cuts
> Interactive segmentation
### Clustering
> With this objective, it is a "chicken and egg" problem:
> > If we knew the cluster centers, we could allocate points to groups by assigning each to its closest center.
> > If we knew the group memberships, we could get the centers by computing the mean per group.

### Segmentation as clustering
> Cluster together (pixels, tokens, etc.) that belong together...
> Agglomerative clustering
> > attach closest to cluster it is closest to - repeat
> Divisive clustering
> > split cluster along best boundary - repeat
> Dendrograms
yield a picture of output as clustering process continues

<img width="1553" height="654" alt="image" src="https://github.com/user-attachments/assets/2fa7cab1-abba-453f-a029-0569d171421e" />

### K-means clustering
> Basic idea: randomly initialize the k cluster centers,
and iterate between the two steps we just saw.
> > 1. Randomly initialize the cluster centers, C..., CK
>‌ > 2. Given cluster centers, determine points in each cluster
> > > For each point p, find the closest c. Put p into cluster i
> > 3. Given points in each cluster, solve for c
> > > Set c, to be the mean of points in cluster i
> > 4. If c, have changed, repeat Step 2
> Properties
> > Will always converge to some solution
> > Can be a "local minimum"
> > >does not always find the global minimum of objective function:
> Depending on what we choose as the feature space, we can group pixels in different ways
> Grouping pixels based on color similarity
> Feature space: color value (3-d)
<img width="1553" height="471" alt="image" src="https://github.com/user-attachments/assets/a71a143e-cb4a-4290-8eef-46f474a782f7" />

### Mean shift clustering and segmentation
An advanced and versatile technique for clustering-based segmentation
<img width="1553" height="603" alt="image" src="https://github.com/user-attachments/assets/dedc33ad-933b-49e7-a546-d6480375c0d7" />
### Mean shift algorithm
> 1. Choose a search window size.
> 2. Choose the initial location of the search window.
> 3. Compute the mean location (centroid of the data) in the search window.
> 4. Center the search window at the mean location computed in Step 3.
> 5. Repeat Steps 3 and 4 until convergence. The mean shift algorithm seeks the "mode" or point of highest density of a data distribution:
> Two issues:
> > (1) Kernel to interpolate density based on sample positions.
>‌ > (2) Gradient ascent to mode.

### Graph-Theoretic Image Segmentation








