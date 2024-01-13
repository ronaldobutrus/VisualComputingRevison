# Question Set 7 - Fundamentals of Visual Computing
### Question 1
What is meant by $C^n$ continuity?

#### Answer 1:
A curve is $C^n$ continuous if its $n^{th}$ derivative is continuous.<br>
$C^n$ continuity implies $C^{n-1}$ continuity.

#### *[This question was from 15. 2D curves]*
<hr>

### Question 2
What is the motion blur filter matrix?

#### Answer 2:
$\frac{1}{5}
\begin{bmatrix}
0&0&0&0&1\\
0&0&0&1&0\\
0&0&1&0&0\\
0&1&0&0&0\\
1&0&0&0&0\\
\end{bmatrix}
$

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 3
How does backward mapping work?

#### Answer 3:
Map each surface point $(s,t)$ at $(x,y,z)$ to its corresponding texture coordinates $(u,v)$. Copy the colour at $(u,v)$ to $(x,y,z)$.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 4
What are the 3D non-homogeneous rotation matrices for rotation about the $y$-axis?

#### Answer 4:
$
\bold{R}_y(\theta) = \begin{bmatrix}
\cos{\theta} & 0 & -\sin{\theta}\\
0 & 1 & 0\\
\sin{\theta} & 0 & \cos{\theta}
\end{bmatrix}
$

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 5
How many configurations are there in 3D? (Marching Cubes Algorithm)

#### Answer 5:
$2^8=256$ different configurations (since 8 corners).

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 6
What is a digital image in terms of a real scene?

#### Answer 6:
A 2D sampled representation of the real scene (i.e. of a continuous function).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 7
What does a Guassian filter do differently to a box filter?

#### Answer 7:
Gives more weight to the central and closer pixels than the further ones. Defined by a standar deviation $\sigma$.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 8
Describe the pinhole camera model.

#### Answer 8:
Captures all lights through a single point. <br>The point is called the **Centre of Projection** or **Optical Centre**.<br>
The size of the pinhole is called the **aperture**.<br>
The image is formed on the sensor (**image plane**) and is **inverted**.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 9
What is the focal point?

#### Answer 9:
A distance $f$ beyond the plane of the lens where the light is focused by the lens.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 10
How does environment mapping work?

#### Answer 10:
- Contain the scene with a texture sphere.
- Render the scene onto the sphere.
- Colour the surface using the reflection from the texture.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 11
What are right handed coordinates?

#### Answer 11:
With $x$ and $y$ displayed regularly on a page, the $z$ axis points out of the page.

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 12
How is the standard lighting model adapted for multiple lights?

#### Answer 12:
$$I=k_a i_a + k_d \sum_{j}{i_{d_j} \cos\theta_j} + k_s \sum_{j}{i_{s_j} \cos^{\alpha}\phi_j}$$

#### *[This question was from 12. Lighting]*
<hr>

### Question 13
What is the sharpening (unsharp masking) filter matrix?

#### Answer 13:
$
\begin{bmatrix}
0&-1&0\\
-1&5&-1\\
0&-1&0
\end{bmatrix}
$

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 14
What is opening (in morphological filtering)?

#### Answer 14:
Dilation after erosion. Simplifies bright objects while avoiding shrinkage of boundaries caused by erosion.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 15
What is the Fast Fourier Transform (FFT), at a high level? What is its complexity?

#### Answer 15:
Splits an input of size $N$ into $\log_{2}{N}$ stages, each with $N/2$ butterfly computations. Each butterfuly computation takes two complex numbers $p$ and $q$ and computes two numbers $p+ki$ and $p-ki$. It then  This results in less additions and multiplications, giving it a complexity of $O(N\log_{2}{N})$.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 16
How can one solve a linear system of equations $2x+3y=6$ and $4x+9y=15$ using matrices?

#### Answer 16:
Express in matrix form $\bold{A}\bold{x}=\bold{b}$, calculate $\bold{A}^{-1}$. This gives $\bold{x} = \bold{A}^{-1}\bold{b}$. 

#### *[This question was from Maths Recap]*
<hr>

### Question 17
Name three types of reconstruction filters.

#### Answer 17:
- Box filter - okay but leaky.
- Tent filter - suppresses high frequencies stronger, reduces artefacts.
- B-spline filter - ver smooth, removes alias spectra, but also smooths base spectrum.

#### *[This question was from 7. Sampling Theory]*
<hr>

### Question 18
What is a mesh?

#### Answer 18:
A mesh discretises a continuous geomtric surface with different levels of details.

#### *[This question was from 14. Geomtric Modelling]*
<hr>

### Question 19
What is the $3\times4$ projection matrix that defines perspective projection (intrinsic and extrinsic parameters)?
Let $\bold{R}$ represent the rotation of the camera and $\bold{t}$ represent its offset from the origin.

#### Answer 19:
$$\bold{P}=\bold{K}\begin{bmatrix}\bold{R}^{-1} &\vert&-\bold{R}^{-1}\bold{t}\end{bmatrix}$$
i.e. (with $r_{ij}$ as elements of $\bold{R}^{-1}$)
$$
\bold{P}=\bold{K}\begin{bmatrix}
r_{11} & r_{12} & r_{13} & -(r_{11}t_1+r_{12}t_2+r_{13}t_3)\\
r_{21} & r_{22} & r_{33} & -(r_{21}t_1+r_{22}t_2+r_{23}t_3)\\
r_{31} & r_{32} & r_{33} & -(r_{31}t_1+r_{32}t_2+r_{33}t_3)\\
\end{bmatrix}
$$
This applies the rotation $\bold{R}^{-1}$ followed by the translation $-\bold{t}$. The reason that the final column is $-\bold{R}^{-1}\bold{t}$ rather than simply $-\bold{t}$ is because the translations also need to be 'rotated'. 

#### *[This question was from 10. Projection]*
<hr>

### Question 20
What does an image histogram do?

#### Answer 20:
It summarises the distribution of intensities in an image.

#### *[This question was from 4. Image Filtering]*
<hr>

