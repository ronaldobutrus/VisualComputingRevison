# Answer Set 3 - Fundamentals of Visual Computing
#### Answer:
Light from a single source is reflected equally in all directions.

#### *[This question was from 12 Lighting]*
<hr>

#### Answer:
1. Load 4 layers of the grid into memory.
2. Create a cube with vertices on the middle two layers.
3. Classify the vertices of the cube according to the implicit function.
4. Compute the configuration index.
5. Retreive the connectivity via a lookup table.
6. Compute the position of the boundary vertices using linear interpolation, i.e. $\bold{v}_s=t\bold{v}_a+(1-t)\bold{v}_b$
7. Repeat steps 2-7 for the next cube.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

#### Answer:
Turns continuous light into pixels by the use of cells which detect photons (as electons) over an array of pixels.

#### *[This question was from 3. Imaging & Display]*
<hr>

#### Answer:
Given an object modelled using planar surfaces, discard surfaces that face away from the camera.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

#### Answer:
- Trap the implicit surface in a grid. 
- For each point in the grid, if $f(\bold{x})<0, the point is inside the surface, otherwise if $f(\bold{x})>0$ it is outside the surface.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

#### Answer:
Synthesising an image from a model (usually geometry, appearance and lighting properties of a scene).

#### *[This question was from 1. Introduction]*
<hr>

#### Answer:
Number of bits needed per colour. For a colour depth of $n$, $2^n$ colours can be represented.

#### *[This question was from 4. Image Filtering]*
<hr>

#### Answer:
$x_2=\pm\sqrt{r^2-x_1^2}$

#### *[This question was from 15. 2D curves]*
<hr>

#### Answer:
$M=\begin{bmatrix}
\cos{\theta}&-\sin{\theta}\\
\sin{\theta}&\cos{\theta}
\end{bmatrix}$

#### *[This question was from 8. Rendering: Action]*
<hr>

#### Answer:
They make a digital representation of an image visible using reflective media (paper).

#### *[This question was from 1. Introduction]*
<hr>

#### Answer:
Corner-cutting.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

#### Answer:
Quantising, i.e. rounding, pixel values for use in computers. This limits precision and the number of intensity levels.

#### *[This question was from 4. Image Filtering]*
<hr>

#### Answer:
$F[k+N]=F[k]$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

#### Answer:
- Painters algorithm
- Back-face culling
- Z-buffer

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

#### Answer:
Bezier Curves are Hermite Curves where the gradient is encoded such that <br><br>
$\frac{d\bold{p}}{dt}(0)=3(\bold{p}_1-\bold{p}_0)$<br>
$\frac{d\bold{p}}{dt}(1)=3(\bold{p}_3-\bold{p}_2)$

#### *[This question was from 16. Bezier Curves]*
<hr>

#### Answer:
Geometry, light and colour.

#### *[This question was from 3. Imaging & Display]*
<hr>

#### Answer:
$x_2=mx_1+c$

#### *[This question was from 15. 2D curves]*
<hr>

#### Answer:
A mesh discretises a continuous geomtric surface with different levels of details.

#### *[This question was from 14. Geomtric Modelling]*
<hr>

#### Answer:
A texture element.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

#### Answer:
A camera is a rigid body, so it can be rotated and translated.

#### *[This question was from 10. Projection]*
<hr>

