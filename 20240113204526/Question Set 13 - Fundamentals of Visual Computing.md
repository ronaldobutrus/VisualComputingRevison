# Question Set 13 - Fundamentals of Visual Computing
### Question 1
For vectors $ 
\bold{x} =
\begin{bmatrix}
x_1 & x_2 & \cdots & x_n \\
\end{bmatrix}^T$ and 
$ 
\bold{y} =
\begin{bmatrix}
y_1 & y_2 & \cdots & y_n \\
\end{bmatrix}^T$ what is the cross product $\bold{x}\times\bold{y}$ and what does it represent geometrically?

#### Answer 1:
$
\bold{x}\times\bold{y}=\begin{bmatrix}
x_2 y_3 - x_3y_2 \\
x_3 y_1 - x_1y_3 \\
x_1 y_2 - x_2y_1 \\
\end{bmatrix}
$ represents the direction of the vector normal to the plane formed by vectors $\bold{x}$ and $\bold{y}$. The direction of this normal vector $\bold{x}\times\bold{y}$ is given by the right hand rule where the index and middle fingers point in the direction of $\bold{x}$ and $\bold{y}$ respectively and the thumb points in the direction of $\bold{x}\times\bold{y}$.

#### *[This question was from Maths Recap]*
<hr>

### Question 2
What is convolution?

#### Answer 2:
A general filtering approach that supports arbitrary kernels.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 3
What is subdivision?

#### Answer 3:
A process in which a polyline/mesh is recusively refined in order to achieve a smooth curve/surface.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 4
What property must a model have in order for us to be able to use back-face culling?

#### Answer 4:
Objects must be modelled with **planar** surfaces.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 5
Name three approaches to hidden surface removal.

#### Answer 5:
- Painters algorithm
- Back-face culling
- Z-buffer

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 6
What is Nyquist's Theorem?

#### Answer 6:
To sample a band-limited signal without aliasing, we need to sample the highest frequency ($W$) more than twice per period, i.e. the minimum sampling rate is $2W$ and the maximum samplign distance is $1/2W$.

#### *[This question was from 7. Sampling Theory]*
<hr>

### Question 7
Outline the three main ways to represent a 2D curve, and briefly explain how each one works.

#### Answer 7:
- **Explicit**: represent one axis with respect to the other. <br>
i.e. $x_2=f(x_1)$
- **Parametric**: maps from a parameter $t$ to points on the curve.<br>
i.e. $f(t)$
- **Implicit**: a function of points in space which evaluate to zero on the curve.<br>
i.e. $f(x=0)$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 8
What is the orientation of a polygon?

#### Answer 8:
A polygon is oriented by the ordering of its points, which can be either *clockwise* or *anti-clockwise*. 

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 9
What is a Catmull-Rom curve?

#### Answer 9:
An interpolating curve where the gradients are chosen based on the control points, i.e.<br><br>
$$\bold{p}^{\prime}_k=\frac{\bold{p}_{k+1}-\bold{p}_{k-1}}{2}$$
$$\bold{p}^{\prime}_0=\bold{p}_{1}-\bold{p}_0$$
For the last point $K$:
$$\bold{p}^{\prime}_K=\bold{p}_{K}-\bold{p}_{K-1}$$

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 10
What is the convolution $(f\ast g)(x)$ for functions $f$ and $g$ given by?

#### Answer 10:
$$
(f\ast g)(x)=\int^{\infty}_{-\infty}{f(x-y)g(y)\,dy}
$$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 11
Describe what is meant by *Phong* shading.

#### Answer 11:
- Compute a normal at each vertex of a polygon (by averaging normals of connected polygons).
- Use bilinear interpolation to calculate normal at each point on the polygon.
- Use standard lighting model to calculate reflected light at each point.

#### *[This question was from 12. Lighting]*
<hr>

### Question 12
What is the parametric representation of a line in 2D?

#### Answer 12:
$f(t)=\bold{a}+t\bold{v}$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 13
What is a **mipmap** and what is the main advantage of using mipmaps?

#### Answer 13:
A mipmap is a complete set of downsampled images for a given texture.<br>
The rendering engine will automatically determine the level of texture to use based on the object's size on the screen when it is rendered, so this **avoids aliasing** and **saves computation time**.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 14
If we have the Sun, Earth and Moon, how would you describe the hierarchy of transforms?

#### Answer 14:
1. Transform the Moon using the Earth frame. 
2. Transform the Earth and Moon using the Sun's frame.

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 15
What is the geometry matrix of a Hermite Curve?

#### Answer 15:
$\bold{G}=\begin{bmatrix}\bold{p}(0)&\bold{p}(1)&\bold{p}^{\prime}(0)&\bold{p}^{\prime}(1)\end{bmatrix}$

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 16
What are the two types of image compression, and how do they work (briefly)?

#### Answer 16:
**Lossless**: Enumerate frequent strings (e.g. PNG/GIF using LZW).<br>
**Lossy**: Encode high frequency components with fewer bits (e.g. JPEG using Discrete Cosine Transform).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 17
What is an affine transform, i.e. how is it expressed?

#### Answer 17:
$\bold{q}=\bold{M}\bold{p}+t$ where $\bold{p}=\begin{bmatrix}p_1\\p_2\end{bmatrix}$ and 
$\bold{M}=\begin{bmatrix}
m_{11}&m_{12}\\m_{21}&m_{22}
\end{bmatrix}$

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 18
What is the convolution theorem?

#### Answer 18:
$\mathcal{F}[f\ast g](\omega)=\sqrt{2\pi}\mathcal{F}[f](\omega)\cdot\mathcal{F}[g](\omega)$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 19
What are the formulae for the coefficients of the Fourier Series?

#### Answer 19:
$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}{f(x)\cos(nx)\,dx}
$$
$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}{f(x)\sin(nx)\,dx}
$$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 20
What is the *scaling* property (Fourier Transform)?

#### Answer 20:
For a constant $a$, if $g(x)=f(ax)$, then
$$
\mathcal{F}[g](\omega)=\frac{1}{\lvert a\rvert}\mathcal{F}[f](\frac{\omega}{a})
$$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

