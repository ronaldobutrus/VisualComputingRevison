# Question Set 6 - Fundamentals of Visual Computing
### Question 1
What is meant by a passive transformation?

#### Answer 1:
Points remain fixed and the coordinate system moves.

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 2
What is the Fourier Transform, qualitatively?

#### Answer 2:
A transformation that represents signals in terms of their frequencies.

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 3
What are the 3D non-homogeneous rotation matrices for rotation about the $z$-axis?

#### Answer 3:
$
\bold{R}_z(\theta) = \begin{bmatrix}
\cos{\theta} & -\sin{\theta} & 0\\
\sin{\theta} & \cos{\theta} & 0\\
0 & 0 & 1\\
\end{bmatrix}
$

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 4
Is multiplication of matrices distributive? (i.e. $\bold{A} (\bold{B}+\bold{C}) = \bold{A}\bold{C}+\bold{A}\bold{C}$)

#### Answer 4:
Yes.

#### *[This question was from Maths Recap]*
<hr>

### Question 5
How can you rotate about an arbitrary axis $\bold{u}$?

#### Answer 5:
There are two ways - either use Rodrugies' rotation formula or:
1. Use $\bold{T}$ to translate the rotation axis to pass through the origin.
2. Use $\bold{R}_x$ and $\bold{R}_y$ to rotate $\bold{u}$ onto the $z$-axis.
3. Rotate about the $z$-axis by $\theta$.
4. Rotate $\bold{u}$ back into place.
5. Translate $\bold{u}$ back into place.<br><br>
This can be written as $\bold{T}^{-1}\bold{R}_x^{-1}\bold{R}_y^{-1}\bold{R}_z\bold{R}_y\bold{R}_x\bold{T}$.

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 6
Is the RGB model additive or subtractive?

#### Answer 6:
Additive (start with black and add R, G and B).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 7
What is a pixel and what does it represent?

#### Answer 7:
Sampled digital values - smallest individual element in an image. Each pixel is a single sampled colour, usually represented in RGB.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 8
What determines the colour of light after it has reflected off a surface?

#### Answer 8:
Surfaces reflect light according to a spectral distribution, so the combination of incident spectrum and reflectance spectrum determines the light colour.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 9
What does histogram equalisation do?

#### Answer 9:
Redestributes intensities to enhance the image contrast.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 10
How can the Discrete Fourier Transform be generalised to n-D functions?

#### Answer 10:
$$
F[k,j]=\sum_{m=0}^{M-1}\sum_{n=0}^{N-1}{f[n,m]e^{-2\pi i(\frac{kn}{N}+\frac{jm}{M})}}\,\,\,\, \mathrm{for}\,j,k=0,1,\cdots,N-1 \,\mathrm{independently}
$$
The inverse follows the same pattern.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 11
What are the steps in the Marching Cubes Algorithm?

#### Answer 11:
1. Load 4 layers of the grid into memory.
2. Create a cube with vertices on the middle two layers.
3. Classify the vertices of the cube according to the implicit function.
4. Compute the configuration index.
5. Retreive the connectivity via a lookup table.
6. Compute the position of the boundary vertices using linear interpolation, i.e. $\bold{v}_s=t\bold{v}_a+(1-t)\bold{v}_b$
7. Repeat steps 2-7 for the next cube.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 12
For two curves $f(t)$ and $g(t)$ connected at $t_0$, what is meant by $C^{1}$ continuity?

#### Answer 12:
Curves are connected smoothly, i.e. $f^{\prime}(t_0)=g^{\prime}(t_0)$.

#### *[This question was from 15. 2D curves]*
<hr>

### Question 13
What is rasterisation?

#### Answer 13:
Converting a continuous or vector image representation into a rectangular sampled grid of pixels.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 14
Given a translation $\bold{t}=\begin{bmatrix}t_1\\t_2\end{bmatrix}$ and transformation
$\bold{M}=\begin{bmatrix}
m_{11}&m_{12}\\m_{21}&m_{22}
\end{bmatrix}$, what is the homogeneous transformation matrix that represents $\bold{M}\bold{t}$?

#### Answer 14:
$\begin{bmatrix}
m_{11}&m_{12}&t_1\\
m_{21}&m_{22}&t_2\\
0&0&1
\end{bmatrix}$ which will apply on $\begin{bmatrix}
p_1\\
p_2\\
1
\end{bmatrix}$

#### *[This question was from 8. Rendering: Action]*
<hr>

### Question 15
What are the 3D non-homogeneous rotation matrices for rotation about the $x$-axis?

#### Answer 15:
$
\bold{R}_x(\theta) = \begin{bmatrix}
1 & 0 & 0\\
0 & \cos{\theta} & -\sin{\theta}\\
0 & \sin{\theta} & \cos{\theta}
\end{bmatrix}
$

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 16
What are the two requirements for calculating an inverse matrix $\bold{A}^{-1}$ from $\bold{A}$ where $\bold{A}\bold{A}^{-1}=\bold{I}$.

#### Answer 16:
Square matrix with non-zero determinant.

#### *[This question was from Maths Recap]*
<hr>

### Question 17
What is the face-edge-vertex data structure?

#### Answer 17:
Stores all relationships between faces, edges and vertexes (easily accessible but highly redundant).
For each face, we have its three vertices and three edges.
For each vertex, we have its connected faces and connected edges.
For each edge, we have its two vertices and two faces.

#### *[This question was from 14. Geomtric Modelling]*
<hr>

### Question 18
How can we make audio signals and images even?

#### Answer 18:
Reflecting about n=0, canceling out purely imaginary, sine-related terms.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 19
What is erosion? And what is the formula?

#### Answer 19:
Reduces the width of bright objects.
$$
(I\ominus B)(x,y) = \min_{(i,j)\in B}I(x-i, y-j)$$

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 20
Is multiplication of matrices associative? (i.e. $(\bold{A} \bold{B})\bold{C} = \bold{A}(\bold{B}\bold{C})$)

#### Answer 20:
Yes.

#### *[This question was from Maths Recap]*
<hr>

