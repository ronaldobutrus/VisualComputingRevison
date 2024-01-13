# Question Set 5 - Fundamentals of Visual Computing
### Question 1
What iis a box filter?

#### Answer 1:
A neighbourhood filter that gives equal weight to all neighbouring pixels to calculate an average for a given pixel.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 2
What is colour depth? For a colour depth of $n$, how many colours can be represented?

#### Answer 2:
Number of bits needed per colour. For a colour depth of $n$, $2^n$ colours can be represented.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 3
Consider a perspective camera with an image buffer. 
What is the homogeneous 2D matrix that transforms the image plane to the image buffer? What is this matrix called?

#### Answer 3:
$\bold{K}=\begin{bmatrix}
\alpha &\gamma & c_x\\
0 & \beta & c_y\\
0 & 0 & 1
\end{bmatrix}$ where $\alpha$ and $\beta$ scale it, $\gamma$ shears it and $c_x$ and $c_y$ translates it.<br> This matrix refers to the **intrinsic** parameters of the camera.

#### *[This question was from 10. Projection]*
<hr>

### Question 4
Assume we are using forward mapping. What do we do in the (likely) case that $(u,v)$ does not map directly to one surface mesh point, but somewhere in the middle of four?

#### Answer 4:
Use bilinear interpolation to read the contributions from the four corners on the surface mesh.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 5
What is a texel?

#### Answer 5:
A texture element.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 6
What is the vertical gradients Sobel filter matrix?

#### Answer 6:
$
\begin{bmatrix}
1&2&1\\
0&0&0\\
-1&-2&-1
\end{bmatrix}
$

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 7
How would you carry out a parallel/orthographic projection with a moved camera? Let $\bold{M}$ be the matrix that transforms points from the world reference frame to the camera's reference frame, and let $\bold{p}$ be the vector representing the point to be projected.

#### Answer 7:
1. Transform the object from the camera frame into the world frame, i.e. $\bold{q}=\bold{M}^{-1}\bold{p}$.
2. Project, i.e. $\bold{q^{\prime}}=\bold{K}_{parallel}\,\bold{q}$.

#### *[This question was from 10. Projection]*
<hr>

### Question 8
What is the horizontal gradients Sobel filter matrix?

#### Answer 8:
$
\begin{bmatrix}
1 & 0& -1\\
2 & 0& -2\\
1 & 0& -1
\end{bmatrix}
$

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 9
What is the formula for the Fourier Transform of a function $f:\mathbb{R}\to\mathbb{R}$?

#### Answer 9:
$$F(\omega) =\mathcal{F}[f](\omega) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} f(x) e^{-i\omega x} \, dx
$$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 10
What are some examples of rastering?

#### Answer 10:
Vector graphics and sampling an analogue signal (e.g. in a digital camera).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 11
What are the two main ways to create surface models?

#### Answer 11:
Artist-made modelling and 3D scanning.

#### *[This question was from 14. Geomtric Modelling]*
<hr>

### Question 12
What is the BRDF?

#### Answer 12:
The Bidirectional Reflectance Distribution Functions (BRDF) is a 4D function that takes in incoming light angle and outgoing light angle (in spherical coordinate pairs) and calculates how much light is reflected off a given material.

#### *[This question was from 12. Lighting]*
<hr>

### Question 13
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

#### Answer 13:
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

### Question 14
What is the name of the model that represents a reflection with diffuse incident and diffuse reflected light?

#### Answer 14:
Ambient lighting model

#### *[This question was from 12. Lighting]*
<hr>

### Question 15
What is fabrication?

#### Answer 15:
Turning computational models into physical 3D objects using additive (e.g. 3D printers) or subtractive (e.g. laser cutting) processes.

#### *[This question was from Maths Recap]*
<hr>

### Question 16
What is the Lambert's Law?

#### Answer 16:
The intensity of reflected light is proportional to the cosine of the angle between the incoming light and the surface normal.

#### *[This question was from 12. Lighting]*
<hr>

### Question 17
How do we rotate about an arbitrary point?

#### Answer 17:
Translate the centre of rotation to the origin, rotate about the origin then translate the centre of origin back.

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 18
For two Bezier curves defined by points $\bold{p}_i$ and $\bold{q}_i$, how do we achieve $C^1$ continuity?

#### Answer 18:
$\bold{p}^{\prime}(1)=\bold{q}^{\prime}(0)$<br>
$3(\bold{p}_3-\bold{p}_2)=3(\bold{q}_1-\bold{q}_0)$<br>
$\bold{q}_1=2\bold{p}_3-\bold{p}_2$

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 19
What happens in the ideal pinhole?

#### Answer 19:
Only one ray of light reaches each point on the sensor. The image can be really dark and has heavy diffraction effects.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 20
In specular to diffuse (Lambertian) reflection, describe how light is reflected.

#### Answer 20:
Light from a single source is reflected equally in all directions.

#### *[This question was from 12. Lighting]*
<hr>

