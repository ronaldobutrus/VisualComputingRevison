# Question Set 11 - Fundamentals of Visual Computing
### Question 1
What is the diagonal gradients Sobel filter matrix?

#### Answer 1:
$
\begin{bmatrix}
2&1&0\\
1&0&-1\\
0&-1&-2
\end{bmatrix}
$ or 
$
\begin{bmatrix}
0&-1&-2\\
1&0&-1\\
2&1&0
\end{bmatrix}
$

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 2
What is the primary use difference between RGB and CYM?

#### Answer 2:
RGB is used for mixing lights (e.g. LCD monitor). CMY is used for filters and paints (e.g. printers).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 3
What is the *cyclical convolution* formula for the Discrete Fourier Transform?

#### Answer 3:
$$(f\ast g)[n]=\sum_{m=0}^{N-1}f[m]g[n-m]$$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 4
What is the Discrete Fourier Transform (DFT), qualitatively?

#### Answer 4:
Transforms discrete analogue to the continuous Fourier transform.
- Deals with finite sampled signals such as audio, images.
- $N$ values are decomposed into $N$ frequency components.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 5
How does morphological filtering work? Does it use kernels?

#### Answer 5:
It uses set theory to filter images using a **structuring element** (set of pixel offsets) to deetermine which pixels should be in the set.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 6
What shape are lens

#### Answer 6:
Usually spherical (easier to produce).

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 7
What is meant by an active transformation?

#### Answer 7:
Points are transformed in the original coordinate system.

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 8
How are digital images arranged in memory (usually)?

#### Answer 8:
Pixels from left to right within a row. Rows from top to bottom.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 9
What is a kernel?

#### Answer 9:
A matrix that defines the weight of neighbouring pixels in calculating the weighted average.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 10
Consider this perspective projection.<br>
A point $\begin{bmatrix}x & y & z\end{bmatrix}^T$ is observed, which projects to the point $\begin{bmatrix}u & v & w\end{bmatrix}^T$ on the window.<br>
The window is planar, parallel to the $x$-$y$ plane, a distance $w$ to the origin.<br>
Express $\begin{bmatrix}u & v & w\end{bmatrix}^T$ in terms of $x$, $y$, $z$ and $w$. 

#### Answer 10:
$\begin{bmatrix}u \\ v \\ w\end{bmatrix}=\begin{bmatrix}wx/z \\ wy/z \\ wz/z\end{bmatrix}=w\begin{bmatrix}x/z \\ y/z \\ 1\end{bmatrix}$

#### *[This question was from 10. Projection]*
<hr>

### Question 11
What are the two approaches to texture mapping?

#### Answer 11:
Forward mapping and backward mapping.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 12
What is the name of the model that represents a reflection with specular incident and specular reflected light?

#### Answer 12:
Phong model

#### *[This question was from 12. Lighting]*
<hr>

### Question 13
What is the *modulation* property (Fourier Transform)?

#### Answer 13:
For a constant $a$, if $g(x)=e^{-ia\omega}f(x)$, then
$$
\mathcal{F}[g](\omega)=\mathcal{F}[f](\omega-a)
$$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 14
What is the right-hand screw rule?

#### Answer 14:
For a rotation about an axis, the thumb aligning with the axis, the other fingers indicate a positive (counter-clockwise) rotation.

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 15
For $\bold{x} = \begin{bmatrix}
a & b \\
\end{bmatrix}^T$ what is $k\bold{x}$?

#### Answer 15:
$\begin{bmatrix}
ka & kb \\
\end{bmatrix}^T$

#### *[This question was from Maths Recap]*
<hr>

### Question 16
What does an image sensor do?

#### Answer 16:
Turns continuous light into pixels by the use of cells which detect photons (as electons) over an array of pixels.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 17
How does aliasing happen in signal samples? How does increasing the sample rate affect this?

#### Answer 17:
Naive downsampling causes overlapping overlapping spectra that cause fluctuations at certain frequencies. Increasing the sample rate moves overlapping spectra further apart in the frequency domain, reducing aliasing.

#### *[This question was from 7. Sampling Theory]*
<hr>

### Question 18
What is the formula that relates the focal distance $f$, the object distance $u$ and the image distance $v$?

#### Answer 18:
$\frac{1}{f}=\frac{1}{u}+\frac{1}{v}$

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 19
What is sampling?

#### Answer 19:
Capturing the value of a function at specific points.

#### *[This question was from 7. Sampling Theory]*
<hr>

### Question 20
What is the main advantage of implicit representation?

#### Answer 20:
You can easily check if a point is on/inside/outside a curve by evaluating the function value.

#### *[This question was from 15. 2D curves]*
<hr>

