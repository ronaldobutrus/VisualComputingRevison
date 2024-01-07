# Answer Set 2 - Fundamentals of Visual Computing
#### Answer:
Discard the regions in spectrum associated with the patterned noise.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

#### Answer:
- Contain the scene with a texture sphere.
- Render the scene onto the sphere.
- Colour the surface using the reflection from the texture.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

#### Answer:
$\bold{M}=\begin{bmatrix}
-1 & 3 & -3 & 1\\
3 & -6 & 3 & 0 \\
-3 & 3 & 0 & 0 \\
1 & 0 & 0 & 0 \\
\end{bmatrix}$

#### *[This question was from 16. Bezier Curves]*
<hr>

#### Answer:
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

#### Answer:
Sampling often and wisely.

#### *[This question was from 7. Sampling Theory]*
<hr>

#### Answer:
The cross product of the edge vectors gives the normal vector $\bold{n}=\bold{a}\times\bold{b}$. <br>
Calculate the dot product of the normal with the viewing vector (i.e. $\bold{n}\cdot\bold{v}$).<br>
This also equal to $\lvert \bold{a}\rvert\lvert \bold{b}\rvert\cos\theta$ where $\theta$ is the angle between the two vectors, so the sign is siginificant.<br><br>
If the polygon is oriented **anti-clockwise**, then $\bold{n}$ points outward from the **front face** of the polygon.<br>
If the polygon is oriented **clockwise**, then $\bold{n}$ points outward from the **back face** of the polygon.<br><br>
Therefore in this case (clockwise):<br>
If $\bold{n}\cdot\bold{v}>0$ then the surface is facing away from the camera. ($\theta$ is between $-90\degree$ and $90\degree$)<br>
If $\bold{n}\cdot\bold{v}<0$ then the surface is facing towards the camera. ($\theta$ is less than $-90\degree$ or greater than $90\degree$)

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

#### Answer:
$$I=k_a i_a + k_d \sum_{j}{i_{d_j} (\bold{L}_i \cdot \bold{N})} + k_s \sum_{j}{i_{s_j} (\bold{R}_i \cdot \bold{V})}$$
This is true since for two **normalised** (unit) vectors $\bold{a}$ and $\bold{b}$, $\bold{a}\cdot\bold{b}=\cos\theta$.

#### *[This question was from 12 Lighting]*
<hr>

#### Answer:
**Lossless**: Enumerate frequent strings (e.g. PNG/GIF using LZW).<br>
**Lossy**: Encode high frequency components with fewer bits (e.g. JPEG using Discrete Cosine Transform).

#### *[This question was from 2. Images & Colours]*
<hr>

#### Answer:
Points remain fixed and the coordinate system moves.

#### *[This question was from 8. Rendering: Action]*
<hr>

#### Answer:
A neighbourhood filter that gives equal weight to all neighbouring pixels to calculate an average for a given pixel.

#### *[This question was from 4. Image Filtering]*
<hr>

#### Answer:
Due to random fluctuations of electrons when photo sensor is ampligied. Common in low-light situations where more amplification is needed.

#### *[This question was from 3. Imaging & Display]*
<hr>

#### Answer:
A distance $f$ beyond the plane of the lens where the light is focused by the lens.

#### *[This question was from 3. Imaging & Display]*
<hr>

#### Answer:
Representing and manipulating virtual objects (including geometry, apperance and lighting properties).

#### *[This question was from 1. Introduction]*
<hr>

#### Answer:
Map each surface point $(s,t)$ at $(x,y,z)$ to its corresponding texture coordinates $(u,v)$. Copy the colour at $(u,v)$ to $(x,y,z)$.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

#### Answer:
15

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

#### Answer:
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

#### Answer:
$f(\theta,\phi)=r\begin{bmatrix}\sin\phi\cos\theta\\\sin\phi\sin\theta\\\cos\theta\end{bmatrix}$

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

#### Answer:
$y\times w + x$

#### *[This question was from 2. Images & Colours]*
<hr>

#### Answer:
A function $f(x)$ is periodic if it is defined for all real x and if there is a positive number $T$ such that $f(xx+T)=f(x)$.

#### *[This question was from 5. The Fourier Transform]*
<hr>

#### Answer:
$
\begin{bmatrix}
1&2&1\\
0&0&0\\
-1&-2&-1
\end{bmatrix}
$

#### *[This question was from 4. Image Filtering]*
<hr>

