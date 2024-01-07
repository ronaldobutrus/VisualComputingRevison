# Question Set 3 - Fundamentals of Visual Computing
### Question 1
What is the primary use difference between RGB and CYM?

#### Answer:
RGB is used for mixing lights (e.g. LCD monitor). CMY is used for filters and paints (e.g. printers).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 2
What is the parametric representation of a circle in 2D?

#### Answer:
$f(t)=r\begin{bmatrix}\cos{t}\\\sin{t}\end{bmatrix}$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 3
What is a Catmull-Rom curve?

#### Answer:
An interpolating curve where the gradients are chosen based on the control points, i.e.<br><br>
$$\bold{p}^{\prime}_k=\frac{\bold{p}_{k+1}-\bold{p}_{k-1}}{2}$$
$$\bold{p}^{\prime}_0=\bold{p}_{1}-\bold{p}_0$$
For the last point $K$:
$$\bold{p}^{\prime}_K=\bold{p}_{K}-\bold{p}_{K-1}$$

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 4
What is thermal noise and when is it common?

#### Answer:
Due to random fluctuations of electrons when photo sensor is ampligied. Common in low-light situations where more amplification is needed.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 5
What is the explicit representation of a circle in 2D?

#### Answer:
$x_2=\pm\sqrt{r^2-x_1^2}$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 6
Given an $m\times n$ RGB image with 16 bits per channel, how much memory is used to store the mipmaps?

#### Answer:
$3\times 16 \times(mn + \frac{1}{4}mn + \frac{1}{16}mn+\cdots)$<br>
$= 3\times 16 \times mn(1+\frac{1}{4}+\frac{1}{16}+\cdots)$<br>
$= 3\times 16 \times \frac{4}{3}mn$<br>
$= 64mn$ bits or $8mn$ bytes

#### *[This question was from 14. Geomtric Modelling]*
<hr>

### Question 7
Assuming the normalised vectors below, how can the multi-light standard lighting model be written using vector representation?
- $\bold{R}$: reflected ray
- $\bold{L}$: negative of incident ray
- $\bold{V}$: viewing ray
- $\bold{N}$: surface normal (out of surface)

#### Answer:
$$I=k_a i_a + k_d \sum_{j}{i_{d_j} (\bold{L}_i \cdot \bold{N})} + k_s \sum_{j}{i_{s_j} (\bold{R}_i \cdot \bold{V})}$$
This is true since for two **normalised** (unit) vectors $\bold{a}$ and $\bold{b}$, $\bold{a}\cdot\bold{b}=\cos\theta$.

#### *[This question was from 12 Lighting]*
<hr>

### Question 8
Give an example of an approximating subdivision scheme.

#### Answer:
Corner-cutting.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 9
How does the Z-buffer method work, qualitatively?

#### Answer:
For each polygon:
1. Project the polygon vertices onto a frame buffer.
2. Convert to pixels.
4. For each pixel, compare colour and depth with existing pixel colour and depth. If closer, then update colour and depth.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 10
Is the RGB model additive or subtractive?

#### Answer:
Additive (start with black and add R, G and B).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 11
What is the implicit representation of a circle in 2D?

#### Answer:
$f(\bold{x})=\lvert\lvert x\rvert\rvert-r$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 12
How can one solve a linear system of equations $2x+3y=6$ and $4x+9y=15$ using matrices?

#### Answer:
Express in matrix form $\bold{A}\bold{x}=\bold{b}$, calculate $\bold{A}^{-1}$. This gives $\bold{x} = \bold{A}^{-1}\bold{b}$. 

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 13
What determines the colour of light after it has reflected off a surface?

#### Answer:
Surfaces reflect light according to a spectral distribution, so the combination of incident spectrum and reflectance spectrum determines the light colour.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 14
What is the formula for Lambertian reflection?

#### Answer:
$I_d=k_d i_d\cos\theta$
where:
- $I_d$ is the diffuse component of the reflected light intensity
- $k_d$ is the diffuse reflectivity (reflection ratio)
- $i_d$ is the diffuse component of the light source intensity
- $\theta$ is the angle beteen the light source and the normal.

#### *[This question was from 12 Lighting]*
<hr>

### Question 15
What happens when the aperture becomes too big?

#### Answer:
The light rays from different parts of the image are mixed up on the image, so it becomes blurry.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 16
What is the *shifting* property (Fourier Transform)?

#### Answer:
For a constant $a$, if $g(x)=f(x-a)$, then
$$
\mathcal{F}[g](\omega)=e^{-ia\omega}\mathcal{F}[f](\omega)
$$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 17
What are the 3D non-homogeneous rotation matrices for rotation about the $y$-axis?

#### Answer:
$
\bold{R}_y(\theta) = \begin{bmatrix}
\cos{\theta} & 0 & -\sin{\theta}\\
0 & 1 & 0\\
\sin{\theta} & 0 & \cos{\theta}
\end{bmatrix}
$

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 18
Is multiplication of matrices commutative? (i.e. $\bold{A} \bold{B} = \bold{B}\bold{A}$)

#### Answer:
No, $\bold{A} \bold{B} \neq \bold{B}\bold{A}$. For a transformation $\bold{A} \bold{B}$, first matrix $\bold{B}$ is applied, then $\bold{A}$.

#### *[This question was from Maths Recap]*
<hr>

### Question 19
What is a Hermite Curve expressed in terms of?

#### Answer:
The geometry constraints, i.e. its values and gradients at the start and end points.

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 20
What is the convolution theorem?

#### Answer:
$\mathcal{F}[f\ast g](\omega)=\sqrt{2\pi}\mathcal{F}[f](\omega)\cdot\mathcal{F}[g](\omega)$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

