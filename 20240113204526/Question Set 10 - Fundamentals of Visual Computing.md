# Question Set 10 - Fundamentals of Visual Computing
### Question 1
What is $(\bold{A}\bold{B}\bold{C})^T$ given by?

#### Answer 1:
$(\bold{A}\bold{B}\bold{C})^T = \bold{C}^T\bold{B}^T\bold{A}^T$.

#### *[This question was from Maths Recap]*
<hr>

### Question 2
What is the advantage of using the Fourier domain to carry out convolution?

#### Answer 2:
It becomes multiplication, which is more efficient especially for large kernels.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 3
What is the implicit representation of a line in 2D?

#### Answer 3:
$f(x)=\bold{n}\cdot(x-\bold{a})$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 4
What is the formula for the parametric representation of a sphere in 3D?

#### Answer 4:
$f(\theta,\phi)=r\begin{bmatrix}\sin\phi\cos\theta\\\sin\phi\sin\theta\\\cos\theta\end{bmatrix}$

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 5
What is the Gimbal lock?

#### Answer 5:
When two of the three rotational axes becomme aligned, we lose one degree of freedom. This means we cannot rotate in all three directions.

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 6
What is animation?

#### Answer 6:
Putting virtual objects into motion using physical models and/or motion capture.

#### *[This question was from 1. Introduction]*
<hr>

### Question 7
For a RGBA colour image that is $w$ pixels wide and $h$ pixels high, what is the index in memory of the pixel at column x, row y? Assume the pixels are stored row by row.

#### Answer 7:
$4(y\times w + x)$ where 4 is the number of channels (for RGBA).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 8
How does displacement mapping work and what is the formula for a normal $\bold{n}$ at a point $\bold{p}$ after it has been mapped?

#### Answer 8:
Perturb the surface height, so the surface becomes bumpy.<br>
$\bold{p}^{\prime}=\bold{p}+f(\bold{p})\bold{n}$

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 9
What is replacement noise (or *salt and pepper noise*)?

#### Answer 9:
Defective sensors cause *dead pixels*. Charge leakage in long exposures cause *hot pixels*.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 10
What is a B-spline?

#### Answer 10:
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
What is the complexity of the Discrete Fourier Transform?

#### Answer 11:
$O(N^2)$ since there are $N$ multiplications and $N-1$ additions.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 12
Homogeneous points scale freely - what does this mean?

#### Answer 12:
Homogeneous coordinates have an additional scaling factor $w$, e.g. $\begin{bmatrix}x&y&z&w\end{bmatrix}^T$. <br>
Two points $\bold{p}$ and $\bold{q}$ are equivalent ($\bold{p}\equiv\bold{q}$) if $\bold{p}=s\bold{q}$.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 13
What is the Convex Hull property of Bezier curves?

#### Answer 13:
The curve will never pass outside of the convex hull formed by its four control points.

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 14
Computer Vision and Computer Graphics do not use the same orientation of vectors? Which uses column vectors and which uses row vectors?

#### Answer 14:
Computer Vision uses column vectors.
Computer Graphics uses row vectors.

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 15
What is the magnitude of $z=a+bi$?

#### Answer 15:
$\lvert z\rvert=\sqrt{z \bar z}=\sqrt{a^2+b^2}$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 16
In what scenario will a surface be forward-facing but should not be rendered?

#### Answer 16:
If an object is not convex, then one face can be behind another. 

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 17
Describe what is meant by *Gouraud* shading.

#### Answer 17:
- Compute a normal at each vertex of a polygon (by averaging normals of connected polygons).
- Use standard lighting model to calculate reflected light at each vertex.
- Use bilinear interpolation to calculate light at each point on the polygon.

#### *[This question was from 12. Lighting]*
<hr>

### Question 18
What is the *shifting* property (Fourier Transform)?

#### Answer 18:
For a constant $a$, if $g(x)=f(x-a)$, then
$$
\mathcal{F}[g](\omega)=e^{-ia\omega}\mathcal{F}[f](\omega)
$$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 19
What is the formula for the Phong model?

#### Answer 19:
$I_s=k_s i_s\cos^{\alpha}\phi$
where:
- $I_s$ is the specular component of the reflected light intensity
- $k_s$ is the specular reflectivity (reflection ratio)
- $i_s$ is the specular component of the light source intensity
- $\phi$ is the angle beteen the viewing ray and the reflected ray
- $\alpha$ is the shininess coefficient.

#### *[This question was from 12. Lighting]*
<hr>

### Question 20
What is $i^2$?

#### Answer 20:
$i^2=-1$

#### *[This question was from 5. The Fourier Transform]*
<hr>

