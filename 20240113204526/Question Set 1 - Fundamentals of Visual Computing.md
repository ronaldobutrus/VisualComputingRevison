# Question Set 1 - Fundamentals of Visual Computing
### Question 1
Which three components of light does the standard model of light involve, and briefly what are each of these?

#### Answer 1:
**Specular**: shiny surfaces have small, intense highlights.<br>
**Diffuse**: dull surfaces have large highlights that fall off more gradually.<br>
**Ambient**: accounts for light scattered equally about entire scene.

#### *[This question was from 12. Lighting]*
<hr>

### Question 2
What is the formula for the explicit representation of a sphere in 3D?

#### Answer 2:
$x_3=\pm\sqrt{r^2-x_1^2-x_2^2}$

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 3
What three elements form an image?

#### Answer 3:
Geometry, light and colour.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 4
What is quantisation?

#### Answer 4:
Quantising, i.e. rounding, pixel values for use in computers. This limits precision and the number of intensity levels.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 5
What is the matrix form (in terms of the blending, parametrisation and geometry matrices) of a Hermite Curve?

#### Answer 5:
$\bold{p}(t)=\bold{G}\bold{M}\bold{Q}(t)$<br><br>
where $\bold{M}=\begin{bmatrix}
2&-3&0&1\\
-2&3&0&0\\
1&-2&1&0\\
1&-1&0&0
\end{bmatrix}$<br><br>
i.e. $\bold{p}(t)=\begin{bmatrix}\bold{p}(0)&\bold{p}(1)&\bold{p}^{\prime}(0)&\bold{p}^{\prime}(1)\end{bmatrix}\begin{bmatrix}
2&-3&0&1\\
-2&3&0&0\\
1&-2&1&0\\
1&-1&0&0
\end{bmatrix}\begin{bmatrix}t^3\\t^2\\t\\1\end{bmatrix}$

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 6
What would the formula for inverting an image be?

#### Answer 6:
$O(x,y) = 255 - I(x,y)$

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 7
What is the formula for the standard lighting model?

#### Answer 7:
$I=k_a i_a + k_d i_d \cos\theta + k_s i_s \cos^{\alpha}\phi$

#### *[This question was from 12. Lighting]*
<hr>

### Question 8
What is the *periodicity* property of the Discrete Fourier Transform?

#### Answer 8:
$F[k+N]=F[k]$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 9
For two curves $f(t)$ and $g(t)$ connected at $t_0$, what is meant by $C^{0}$ continuity?

#### Answer 9:
Curves are connected, i.e. $f(t_0)=g(t_0)$.

#### *[This question was from 15. 2D curves]*
<hr>

### Question 10
Which shape do meshes come in and why?

#### Answer 10:
Triangles, because:
- simple
- efficiently rendered (three vertices on a plane)
- output of most 3D acquisition tools (scanners).

#### *[This question was from 14. Geomtric Modelling]*
<hr>

### Question 11
What is the affine transform to perform a counter-clockwise rotation by $\theta$ about the origin?

#### Answer 11:
$M=\begin{bmatrix}
\cos{\theta}&-\sin{\theta}\\
\sin{\theta}&\cos{\theta}
\end{bmatrix}$

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 12
How many equivalence classes are there in 3D? (Marching Cubes Algorithm)

#### Answer 12:
15

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 13
How can we use a filter to remove high frequencies in a frequency spectrum?

#### Answer 13:
Use a low-pass filter to remove high frequencies.

#### *[This question was from 7. Sampling Theory]*
<hr>

### Question 14
What is the homogeneous matrix that represents a perspective projection (extrinsic parameters only)?

#### Answer 14:
$$\bold{K}_{perspective}=\frac{w}{z}\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 1/w & 0
\end{bmatrix}$$
Note that the multiplier is usually omitted and used at a later stage to make the coordinate non-homogeneous.

#### *[This question was from 10. Projection]*
<hr>

### Question 15
What was the first commercially successful photographic process called, how long for exposure and what was the image media?

#### Answer 15:
Daguerreotype process, minutes, on metallic plate (no copies) (1839).

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 16
How can a column vector be changed into a row vector?

#### Answer 16:
Transposition ($p^\prime = p^T$).

#### *[This question was from Maths Recap]*
<hr>

### Question 17
Give an example of an approximating subdivision scheme.

#### Answer 17:
Corner-cutting.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 18
Given an $m\times n$ RGB image with 16 bits per channel, how much memory is used to store the mipmaps?

#### Answer 18:
$3\times 16 \times(mn + \frac{1}{4}mn + \frac{1}{16}mn+\cdots)$<br>
$= 3\times 16 \times mn(1+\frac{1}{4}+\frac{1}{16}+\cdots)$<br>
$= 3\times 16 \times \frac{4}{3}mn$<br>
$= 64mn$ bits or $8mn$ bytes

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 19
What is modelling?

#### Answer 19:
Representing and manipulating virtual objects (including geometry, apperance and lighting properties).

#### *[This question was from 1. Introduction]*
<hr>

### Question 20
How is light recorded?

#### Answer 20:
Light is emitted from a source, it reflects off a scene element and enters the imaging system. The imaging syste produces an image on its image plane.

#### *[This question was from 3. Imaging & Display]*
<hr>

