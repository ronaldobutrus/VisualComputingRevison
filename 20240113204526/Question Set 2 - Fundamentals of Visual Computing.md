# Question Set 2 - Fundamentals of Visual Computing
### Question 1
What is parallel projection? For a point $p=\begin{bmatrix}p_1\\p_2\\p_3\\1\end{bmatrix}$ what is the associated matrix (in the world reference frame)?

#### Answer 1:
In parallel/orthographic projection, the light rays are parallel. In the world frame, just drop the $z$ coordinate.<br>
$$\bold{K}_{parallel}=\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 1
\end{bmatrix}$$

#### *[This question was from 10. Projection]*
<hr>

### Question 2
What is the explicit representation of a circle in 2D?

#### Answer 2:
$x_2=\pm\sqrt{r^2-x_1^2}$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 3
How can two or more 2D images be used to create a 3D model?

#### Answer 3:
**Triangulation:** if we have a single point observed on two images, we can trace the rays back to where they intersect.

#### *[This question was from 10. Projection]*
<hr>

### Question 4
What happens if the aperture becomes too small?

#### Answer 4:
Less light gets throuogh (so you will need to increase the exposure). Diffraction effect increases.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 5
How does forward mapping work?

#### Answer 5:
Map each texel $(u,v)$ to surface point $(x,y,z)$. Copy the colour at $(u,v)$ to $(x,y,z)$.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 6
For $\bold{x} = \begin{bmatrix}
a & b \\
\end{bmatrix}^T$ and $\bold{y} =\begin{bmatrix}
c & d \\
\end{bmatrix}^T$ what is $\bold{x} + \bold{y}$?

#### Answer 6:
$\begin{bmatrix}
a+b & c+d \\
\end{bmatrix}^T$

#### *[This question was from Maths Recap]*
<hr>

### Question 7
For two Bezier curves defined by points $\bold{p}_i$ and $\bold{q}_i$, how do we achieve $C^0$ continuity?

#### Answer 7:
$\bold{p}(1)=\bold{q}(0)$<br>
$\bold{p}_3=\bold{q}_0$

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 8
What is a Hermite Curve expressed in terms of?

#### Answer 8:
The geometry constraints, i.e. its values and gradients at the start and end points.

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 9
What are Sobel filters?

#### Answer 9:
They are convolution filters that show horizontal, vertical and diagonal gradients.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 10
What is closing (in morphological filtering)?

#### Answer 10:
Erosion after dilation. Simplifies bright objects while avoiding expansion of boundaries caused by dilation.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 11
How does increasing the shininess ($\alpha$) affect the highlight on an object?

#### Answer 11:
As $\alpha$ increases, the highlight gets smaller and sharper.

#### *[This question was from 12. Lighting]*
<hr>

### Question 12
How do you deal with RGB with respect to reflection?

#### Answer 12:
Calculate the reflected intensity for red, green and blue individually.

#### *[This question was from 12. Lighting]*
<hr>

### Question 13
What is the main advantage of parametric representation?

#### Answer 13:
Allows easy iteration along path of a curve.

#### *[This question was from 15. 2D curves]*
<hr>

### Question 14
What is the formula for Lambertian reflection?

#### Answer 14:
$I_d=k_d i_d\cos\theta$
where:
- $I_d$ is the diffuse component of the reflected light intensity
- $k_d$ is the diffuse reflectivity (reflection ratio)
- $i_d$ is the diffuse component of the light source intensity
- $\theta$ is the angle beteen the light source and the normal.

#### *[This question was from 12. Lighting]*
<hr>

### Question 15
What is a high pass filter and what does it do?

#### Answer 15:
Passes signals with frequencies higher than the threshold - removes low frequencies (overall shape) and extracts the edge images.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 16
Assuming the normalised vectors below, how can the multi-light standard lighting model be written using vector representation?
- $\bold{R}$: reflected ray
- $\bold{L}$: negative of incident ray
- $\bold{V}$: viewing ray
- $\bold{N}$: surface normal (out of surface)

#### Answer 16:
$$I=k_a i_a + k_d \sum_{j}{i_{d_j} (\bold{L}_i \cdot \bold{N})} + k_s \sum_{j}{i_{s_j} (\bold{R}_i \cdot \bold{V})}$$
This is true since for two **normalised** (unit) vectors $\bold{a}$ and $\bold{b}$, $\bold{a}\cdot\bold{b}=\cos\theta$.

#### *[This question was from 12. Lighting]*
<hr>

### Question 17
What is a low pass filter and what does it do?

#### Answer 17:
Passes signals with frequencies lower than the threshold - removes fine details and hence blurs an image.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 18
How can we represent homogeneous transformations in 3D?

#### Answer 18:
Add an extra row and column.<br>
$\bold{M}=
\begin{bmatrix}
m_{11} & m_{12} & m_{13} & t_x\\
m_{21} & m_{22} & m_{23} & t_y\\
m_{31} & m_{22} & m_{33} & t_z\\
0 & 0 & 0 & 1
\end{bmatrix}
$

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 19
What do you need to do to 3D objects to enable texture mapping to take place?

#### Answer 19:
You need to 'flatten' the geometry so a (near) 1-1 correspondence between points on the surface and texture can take place.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 20
What is the formula for diffuse to diffuse (ambient) lighting?

#### Answer 20:
$I_a=k_a i_a$
where:
- $I_a$ is the ambient component of the reflected light intensity
- $k_a$ is the ambient reflectivity (reflection ratio)
- $i_a$ is the ambient component of the light source intensity.

#### *[This question was from 12. Lighting]*
<hr>

