# Question Set 3 - Fundamentals of Visual Computing
### Question 1
What is the range of wavelengths of visible light? Which colours have the longest and shortest wavelengths?

#### Answer 1:
380nm (blue) to 750nm (red).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 2
What is the formula for the inverse Discrete Fourier Transform (DFT)?

#### Answer 2:
$$
f(n)=\frac{1}{N}\sum_{n=0}^{N-1}{F[k]e^{2\pi i\frac{kn}{N}}}\,\,\,\, \mathrm{for}\,k=0,1,\cdots,N-1
$$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 3
Can the RGB colour model generate every perceivable colour?

#### Answer 3:
In theory yes, but this would involve negative weights. In practice, it can generate a good fraction of all visible colours.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 4
Is multiplication of matrices commutative? (i.e. $\bold{A} \bold{B} = \bold{B}\bold{A}$)

#### Answer 4:
No, $\bold{A} \bold{B} \neq \bold{B}\bold{A}$. For a transformation $\bold{A} \bold{B}$, first matrix $\bold{B}$ is applied, then $\bold{A}$.

#### *[This question was from Maths Recap]*
<hr>

### Question 5
What is a homography?

#### Answer 5:
A perspective-like transform in the plane, represented by a $3\times3$ matrix.

#### *[This question was from 10. Projection]*
<hr>

### Question 6
How long must calotype photography undergo exposure, and what was the image media?

#### Answer 6:
Seconds, on paper (multiple copies). Used early paper-based negatives (1841).

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 7
How does bump mapping work and what is the formula for a normal $\bold{n}$ at a point $\bold{p}$ after it has been mapped?

#### Answer 7:
Perturb the surface normal, so even though the surface is flat, it looks bumpy.<br>
$\bold{n}^{\prime}=\bold{n}+f(\bold{p})$

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 8
What are the main two groups of schemes for subdivision?

#### Answer 8:
**Approximation**: original vertices are moved.
**Interpolation**: introduce new vertices without affecting original vertices.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 9
What is the implicit representation of a circle in 2D?

#### Answer 9:
$f(\bold{x})=\lvert\lvert x\rvert\rvert-r$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 10
What transformations does a homography comprise of?

#### Answer 10:
Translation, rotation, scale, stretch and shear.

#### *[This question was from 10. Projection]*
<hr>

### Question 11
How does back-face culling work, qualitatively?

#### Answer 11:
Given an object modelled using planar surfaces, discard surfaces that face away from the camera.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 12
Consider two edge vectors $\bold{a}=\overrightarrow{AB}$ and $\bold{b}=\overrightarrow{BC}$, connected tip-to-tail in clockwise fashion. The vector $\bold{v}$ is the viewing vector, i.e. vector pointing in the direction going from the object to the camera.<br><br>
How can we use edge vectors to determine if a surface faces away from the camera?

#### Answer 12:
The cross product of the edge vectors gives the normal vector $\bold{n}=\bold{a}\times\bold{b}$. <br>
Calculate the dot product of the normal with the viewing vector (i.e. $\bold{n}\cdot\bold{v}$).<br>
This also equal to $\lvert \bold{a}\rvert\lvert \bold{b}\rvert\cos\theta$ where $\theta$ is the angle between the two vectors, so the sign is siginificant.<br><br>
If the polygon is oriented **anti-clockwise**, then $\bold{n}$ points outward from the **front face** of the polygon.<br>
If the polygon is oriented **clockwise**, then $\bold{n}$ points outward from the **back face** of the polygon.<br><br>
Therefore in this case (clockwise):<br>
If $\bold{n}\cdot\bold{v}>0$ then the surface is facing away from the camera. ($\theta$ is between $-90\degree$ and $90\degree$)<br>
If $\bold{n}\cdot\bold{v}<0$ then the surface is facing towards the camera. ($\theta$ is less than $-90\degree$ or greater than $90\degree$)<br>
*Note that this is slightly different to what is in the slides, as they consider a normal going into the page to be $-\bold{n}$.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 13
How can we better downsample images to prevent aliasing? 

#### Answer 13:
First apply low-pass Guassian filter to blur the image, then subsample. The filter size should double for each reduction by power of 2.

#### *[This question was from 7. Sampling Theory]*
<hr>

### Question 14
What is the face-vertex data structure?

#### Answer 14:
For each face, we have its three vertices.
For each vertex, we have its connected faces.

#### *[This question was from 14. Geomtric Modelling]*
<hr>

### Question 15
How many equivalence classes are there in 2D, and what are they? (Marching Squares Algorithm)

#### Answer 15:
Four equivalence classes (up to rotational symmetry, reflection symmetry and complement):
- all out
- one out, three in
- two (same side) out, two (same side) in
- two (opposite sides) out, two (opposite sides) in

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 16
How many different configurations of corner values are there in 2D? (Marching Squares algorithm)

#### Answer 16:
$2^4=16$ different configurations.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 17
How is a point represented as a vector in 2D and 3D respectively?

#### Answer 17:
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

### Question 18
What is the formula relating the speed $s$ of an electromagnetic wave, its frequency $f$ and its wavelength $\lambda$?

#### Answer 18:
$s=f\lambda$ where $s$ is constant ($s=3\times10^8\textrm{ms}^{-1}$).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 19
What is image processing?

#### Answer 19:
Performing operations to an image to produce another image.

#### *[This question was from 1. Introduction]*
<hr>

### Question 20
What is CMYK? Give three reasons for using K?

#### Answer 20:
Cyan Magenta Yellow Black. Black added to:
- accurately print black
- save ink compared to using C+M+Y
- print fine black text without having to align colour perfectly
- save moneyy (black ink is cheaper)

#### *[This question was from 2. Images & Colours]*
<hr>

