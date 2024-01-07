# Question Set 2 - Fundamentals of Visual Computing
### Question 1
For matrices 
$
\bold{A} = 
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{bmatrix}
$ and 
$
\bold{B} = 
\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
\end{bmatrix}
$ what is $\bold{A}\bold{B}$?

#### Answer:
$\bold{A}\bold{B} = 
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{bmatrix}\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
\end{bmatrix} \\
= \begin{bmatrix}
a_{11}b_{11} + a_{12}b_{21} & a_{11}b_{12} + a_{12}b_{22} \\
a_{21}b_{11} + a_{22}b_{21} & a_{21}b_{12} + a_{22}b_{22} \\
\end{bmatrix}
$</br></br>
For $\bold{C} = \bold{A}\bold{B}$: $c_{ij} = \sum_{k=1}^{n}{a_{ik}b_{kj}}$

#### *[This question was from Maths Recap]*
<hr>

### Question 2
How does back-face culling work, qualitatively?

#### Answer:
Given an object modelled using planar surfaces, discard surfaces that face away from the camera.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 3
How are digital images arranged in memory (usually)?

#### Answer:
Pixels from left to right within a row. Rows from top to bottom.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 4
What does a lens do?

#### Answer:
It focuses parallel light onto a single focal point.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 5
What are some examples of rastering?

#### Answer:
Vector graphics and sampling an analogue signal (e.g. in a digital camera).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 6
What is animation?

#### Answer:
Putting virtual objects into motion using physical models and/or motion capture.

#### *[This question was from 1. Introduction]*
<hr>

### Question 7
What is the Discrete Fourier Transform (DFT), qualitatively?

#### Answer:
Transforms discrete analogue to the continuous Fourier transform.
- Deals with finite sampled signals such as audio, images.
- $N$ values are decomposed into $N$ frequency components.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 8
Name three approaches to hidden surface removal.

#### Answer:
- Painters algorithm
- Back-face culling
- Z-buffer

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 9
What is the parametric representation of a line in 2D?

#### Answer:
$f(t)=\bold{a}+t\bold{v}$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 10
What is the focal point?

#### Answer:
A distance $f$ beyond the plane of the lens where the light is focused by the lens.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 11
What does an image histogram do?

#### Answer:
It summarises the distribution of intensities in an image.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 12
What is a pixel and what does it represent?

#### Answer:
Sampled digital values - smallest individual element in an image. Each pixel is a single sampled colour, usually represented in RGB.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 13
What is the formula for the inverse Fourier Transform that restores $f$ from $F$?

#### Answer:
$$f(x)=\mathcal{F}^{-1}[F](x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(\omega) e^{i\omega x} \, d\omega
$$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 14
How can you determine the depth of a pixel for a set of projected polygon vertices?

#### Answer:
Each vertex has a depth. Use *bi-linear interpolation* to calculate the depth of a point between these vertices.<br>
Consider a polygon with sides (clockwise) $h_{11}$, $h_{12}$, $h_{22}$ and $h_{21}$. <br>A point lies between these four vertices:
- a fractional length $0\leq a\leq1$ from $h_{11}$ to $h_{12}$
- a fractional length $0\leq b\leq1$ from $h_{11}$ to $h_{21}$<br><br>
The height at this point is given by
$$
(1-a)(1-b)h_{11} + (1-a)b\,h_{12} + a(1-b)\,h_{21} + ab\,h_{22}
$$

#### *[This question was from 12 Lighting]*
<hr>

### Question 15
What is modelling?

#### Answer:
Representing and manipulating virtual objects (including geometry, apperance and lighting properties).

#### *[This question was from 1. Introduction]*
<hr>

### Question 16
For $\bold{x} = \begin{bmatrix}
a & b \\
\end{bmatrix}^T$ and $\bold{y} =\begin{bmatrix}
c & d \\
\end{bmatrix}^T$ what is $\bold{x} + \bold{y}$?

#### Answer:
$\begin{bmatrix}
a+b & c+d \\
\end{bmatrix}^T$

#### *[This question was from Maths Recap]*
<hr>

### Question 17
What is the main advantage of parametric representation?

#### Answer:
Allows easy iteration along path of a curve.

#### *[This question was from 15. 2D curves]*
<hr>

### Question 18
What are Sobel filters?

#### Answer:
They are convolution filters that show horizontal, vertical and diagonal gradients.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 19
What is the affine transform to scale a point by factor $a$ in the $x$-direction and $b$ in the $y$-direction?

#### Answer:
$M=\begin{bmatrix}
a&0\\
0&b\\
\end{bmatrix}$

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 20
What is the complex conjugate of $z=a+bi$?

#### Answer:
$\bar z = a-bi =re^{-i\phi}$

#### *[This question was from 5. The Fourier Transform]*
<hr>

