# Question Set 8 - Fundamentals of Visual Computing
### Question 1
What is Computer Vision?

#### Answer 1:
Understanding and reconstructing information about real-world scenes from image and video data.

#### *[This question was from 1. Introduction]*
<hr>

### Question 2
Suppose we want to approximate an implicit surface with a mesh. How does sampling a surface in a grid work?

#### Answer 2:
- Trap the implicit surface in a grid. 
- For each point in the grid, if $f(\bold{x})<0$, the point is inside the surface, otherwise if $f(\bold{x})>0$ it is outside the surface.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 3
What is one use of homographies?

#### Answer 3:
Image stitching (by warping images together).

#### *[This question was from 10. Projection]*
<hr>

### Question 4
What is the affine transform that does nothing?

#### Answer 4:
$M=\begin{bmatrix}
0&1\\1&0
\end{bmatrix}$

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 5
What two main types of light are there?

#### Answer 5:
Specular and diffuse.

#### *[This question was from 12. Lighting]*
<hr>

### Question 6
What is the blending matrix for Bezier curves?

#### Answer 6:
$\bold{M}=\begin{bmatrix}
-1 & 3 & -3 & 1\\
3 & -6 & 3 & 0 \\
-3 & 3 & 0 & 0 \\
1 & 0 & 0 & 0 \\
\end{bmatrix}$

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 7
In specular (to specular) reflection, what does the intensity of the specular highlight depend on?

#### Answer 7:
The angle $\phi$ between the viewing direction and the reflected ray. The smaller the angle, the brighter the reflection.

#### *[This question was from 12. Lighting]*
<hr>

### Question 8
How can you determine the depth of a pixel for a set of projected polygon vertices?

#### Answer 8:
Each vertex has a depth. Use *bi-linear interpolation* to calculate the depth of a point between these vertices.<br>
Consider a polygon with sides (clockwise) $h_{11}$, $h_{12}$, $h_{22}$ and $h_{21}$. <br>A point lies between these four vertices:
- a fractional length $0\leq a\leq1$ from $h_{11}$ to $h_{12}$
- a fractional length $0\leq b\leq1$ from $h_{11}$ to $h_{21}$<br><br>
The height at this point is given by
$$
(1-a)(1-b)h_{11} + (1-a)b\,h_{12} + a(1-b)\,h_{21} + ab\,h_{22}
$$

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 9
What is the parametric representation of a circle in 2D?

#### Answer 9:
$f(t)=r\begin{bmatrix}\cos{t}\\\sin{t}\end{bmatrix}$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 10
How many hours of exposure did the first surviving photograph need? What sort of year range was this?

#### Answer 10:
1765-1833 - 8 hours. 

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 11
What do displays do (at a high level)?

#### Answer 11:
They make a digital representation of an image visible using emissive media.

#### *[This question was from 1. Introduction]*
<hr>

### Question 12
What do printers do (at a high level)?

#### Answer 12:
They make a digital representation of an image visible using reflective media (paper).

#### *[This question was from 1. Introduction]*
<hr>

### Question 13
How do frequencies apply to images?

#### Answer 13:
Images can be analysed using frequencies in the x and y directions.

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 14
What is the formula relating incident radiance $E(\lambda)$, outgoing radiance $R(\lambda)$ and reflectance $S(\lambda)$?

#### Answer 14:
$R(\lambda) = E(\lambda)S(\lambda)$

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 15
What is the Discrete Cosine Transform (DCT)?

#### Answer 15:
The Fourier Transform of an even, real-valued signal.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 16
Express $\bold{p}(t)=\bold{x}_0+t\bold{x}_1+t^2\bold{x}_2+t^3\bold{x}_3$ in matrix notation.

#### Answer 16:
$\bold{p}(t)=\begin{bmatrix}\bold{x}_3&\bold{x}_2&\bold{x}_1&\bold{x}_0\end{bmatrix}\begin{bmatrix}t^3\\t^2\\t\\1\end{bmatrix}=\bold{C}\bold{Q}(t)$

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 17
What is aliasing caused by?

#### Answer 17:
Sampling a high-frequency function with a low sampling frequency.

#### *[This question was from 7. Sampling Theory]*
<hr>

### Question 18
What is median filtering and what are its advantages?

#### Answer 18:
Replacing each pixel with the median value of all pixels in the neighbourhood.<br>
- Colour changes smoothly in a small patch.
- Good against sparse random noise.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 19
What is CIEXYZ and what is it used for?

#### Answer 19:
Specifying colours and their ranges absolutely (can describe all visible colours).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 20
What is the Fourier Series?

#### Answer 20:
If $f(x)$ is a period function with period $2\pi$, the function can be represented using the Fourier Series:
$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}{a_n \cos{nx}}+\sum_{n=1}^{\infty}{b_n \sin{nx}}
$$

#### *[This question was from 5. The Fourier Transform]*
<hr>

