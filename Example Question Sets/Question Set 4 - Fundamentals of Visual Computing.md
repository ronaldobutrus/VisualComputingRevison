# Question Set 4 - Fundamentals of Visual Computing
### Question 1
What is the formula for the Fourier Transform of a function $f:\mathbb{R}\to\mathbb{R}$?

#### Answer:
$$F(\omega) =\mathcal{F}[f](\omega) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} f(x) e^{-i\omega x} \, dx
$$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 2
How do CCD sensors differ from CMOS sensors?

#### Answer:
**CCD**: serial devices where pixels are read out one at a time.<br>
**CMOS**: each pixel contains an amplifier, so read-out can be faster.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 3
What would the formula for enhancing the contrast of an image be?

#### Answer:
$O(x,y) = \begin{bmatrix}
\frac{I(x,y)-p}{q}
\end{bmatrix}_0^{255}$ where $p$ is arbitary and $q<1$.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 4
Computer Vision and Computer Graphics do not use the same orientation of vectors? Which uses column vectors and which uses row vectors?

#### Answer:
Computer Vision uses column vectors.
Computer Graphics uses row vectors.

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 5
For a RGBA colour image that is $w$ pixels wide and $h$ pixels high, what is the index in memory of the pixel at column x, row y? Assume the pixels are stored row by row.

#### Answer:
$4(y\times w + x)$ where 4 is the number of channels (for RGBA).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 6
What is erosion? And what is the formula?

#### Answer:
Reduces the width of bright objects.
$$
(I\ominus B)(x,y) = \min_{(i,j)\in B}I(x-i, y-j)$$

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 7
How do you deal with RGB with respect to reflection?

#### Answer:
Calculate the reflected intensity for red, green and blue individually.

#### *[This question was from 12 Lighting]*
<hr>

### Question 8
What are the main two groups of schemes for subdivision?

#### Answer:
**Approximation**: original vertices are moved.
**Interpolation**: introduce new vertices without affecting original vertices.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 9
What is meant by an active transformation?

#### Answer:
Points are transformed in the original coordinate system.

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 10
What is a B-spline?

#### Answer:
A Hermite curve defined in terms of its basis functions.<br>
The basis functions are those resulting from from $\bold{M}\bold{Q}(t)$, i.e.<br><br>
$\begin{bmatrix}
2&-3&0&1\\
-2&3&0&0\\
1&-2&1&0\\
1&-1&0&0
\end{bmatrix}\begin{bmatrix}t^3\\t^2\\t\\1\end{bmatrix}=\begin{bmatrix}
1-3t^2+2t^3\\
3t^2-2t^3\\
t-2t^2+t^3\\
-t^2+t^3
\end{bmatrix}$<br><br>
The Hermite function can therefore be written as:<br>
$\bold{p}(t)\\=\bold{p}(0)(1-3t^2+2t^3)\\+\bold{p}(1)(3t^2-2t^3)\\+\bold{p}^{\prime}(0)(t-2t^2+t^3)\\+\bold{p}^{\prime}(1)(-t^2+t^3)\\$

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 11
Suppose we carry out the Marching Squares algorithm and we get the corners as ($out, in, out, in$) for ($a,b,c,d$). Does the boundary cross at $a$ and $c$ or $b$ and $d$? What should we do to avoid problems in the resulting mesh?

#### Answer:
Pick one way to interpret the sample and stick to it.  

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 12
Express $\bold{p}(t)=\bold{x}_0+t\bold{x}_1+t^2\bold{x}_2+t^3\bold{x}_3$ in matrix notation.

#### Answer:
$\bold{p}(t)=\begin{bmatrix}\bold{x}_3&\bold{x}_2&\bold{x}_1&\bold{x}_0\end{bmatrix}\begin{bmatrix}t^3\\t^2\\t\\1\end{bmatrix}=\bold{C}\bold{Q}(t)$

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 13
What is colour depth? For a colour depth of $n$, how many colours can be represented?

#### Answer:
Number of bits needed per colour. For a colour depth of $n$, $2^n$ colours can be represented.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 14
What is a reference frame?

#### Answer:
A collection of vectors (two for 2D space, three for 3D space) such that any vector in the space can be represented with respect to the reference frame.

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 15
What is Nyquist's Theorem?

#### Answer:
To sample a band-limited signal without aliasing, we need to sample the highest frequency ($W$) more than twice per period, i.e. the minimum sampling rate is $2W$ and the maximum samplign distance is $1/2W$.

#### *[This question was from 7. Sampling Theory]*
<hr>

### Question 16
What is one use of homographies?

#### Answer:
Image stitching (by warping images together).

#### *[This question was from 10. Projection]*
<hr>

### Question 17
Can the RGB colour model generate every perceivable colour?

#### Answer:
In theory yes, but this would involve negative weights. In practice, it can generate a good fraction of all visible colours.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 18
How is a point represented as a vector in 2D and 3D respectively?

#### Answer:
$ 
\begin{bmatrix}
x & y \\
\end{bmatrix}^T
$ and 
$ 
\begin{bmatrix}
x & y & z \\
\end{bmatrix}^T
$

#### *[This question was from Maths Recap]*
<hr>

### Question 19
What is the formula relating the speed $s$ of an electromagnetic wave, its frequency $f$ and its wavelength $\lambda$?

#### Answer:
$s=f\lambda$ where $s$ is constant ($s=3\times10^8\textrm{ms}^{-1}$).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 20
What is the Gimbal lock?

#### Answer:
When two of the three rotational axes becomme aligned, we lose one degree of freedom. This means we cannot rotate in all three directions.

#### *[This question was from 9. 3D Transformations]*
<hr>

