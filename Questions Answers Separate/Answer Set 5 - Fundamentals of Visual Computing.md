# Answer Set 5 - Fundamentals of Visual Computing
#### Answer:
An interpolating curve where the gradients are chosen based on the control points, i.e.<br><br>
$$\bold{p}^{\prime}_k=\frac{\bold{p}_{k+1}-\bold{p}_{k-1}}{2}$$
$$\bold{p}^{\prime}_0=\bold{p}_{1}-\bold{p}_0$$
For the last point $K$:
$$\bold{p}^{\prime}_K=\bold{p}_{K}-\bold{p}_{K-1}$$

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

#### Answer:
A collection of vectors (two for 2D space, three for 3D space) such that any vector in the space can be represented with respect to the reference frame.

#### *[This question was from 9. 3D Transformations]*
<hr>

#### Answer:
Surfaces reflect light according to a spectral distribution, so the combination of incident spectrum and reflectance spectrum determines the light colour.

#### *[This question was from 2. Images & Colours]*
<hr>

#### Answer:
$\begin{bmatrix}u \\ v \\ w\end{bmatrix}=\begin{bmatrix}wx/z \\ wy/z \\ wz/z\end{bmatrix}=w\begin{bmatrix}x/z \\ y/z \\ 1\end{bmatrix}$

#### *[This question was from 10. Projection]*
<hr>

#### Answer:
Passes signals with frequencies higher than the threshold - removes low frequencies (overall shape) and extracts the edge images.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

#### Answer:
Converting a continuous or vector image representation into a rectangular sampled grid of pixels.

#### *[This question was from 2. Images & Colours]*
<hr>

#### Answer:
For a constant $a$, if $g(x)=f(ax)$, then
$$
\mathcal{F}[g](\omega)=\frac{1}{\lvert a\rvert}\mathcal{F}[f](\frac{\omega}{a})
$$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

#### Answer:
They are convolution filters that show horizontal, vertical and diagonal gradients.

#### *[This question was from 4. Image Filtering]*
<hr>

#### Answer:
- Cannot represent vertical lines.
- Cannot represent a curve with two output values for a single input.

#### *[This question was from 15. 2D curves]*
<hr>

#### Answer:
$
s\bold{A} = 
\begin{bmatrix}
sa_{11} & sa_{12} \\
sa_{21} & sa_{22} \\
\end{bmatrix}
$

#### *[This question was from Maths Recap]*
<hr>

#### Answer:
Homogeneous coordinates have an additional scaling factor $w$, e.g. $\begin{bmatrix}x&y&z&w\end{bmatrix}^T$. <br>
Two points $\bold{p}$ and $\bold{q}$ are equivalent ($\bold{p}\equiv\bold{q}$) if $\bold{p}=s\bold{q}$.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

#### Answer:
Not depicting those parts of a scene that are not visible.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

#### Answer:
$M=\begin{bmatrix}
a&0\\
0&b\\
\end{bmatrix}$

#### *[This question was from 8. Rendering: Action]*
<hr>

#### Answer:
**CCD**: serial devices where pixels are read out one at a time.<br>
**CMOS**: each pixel contains an amplifier, so read-out can be faster.

#### *[This question was from 3. Imaging & Display]*
<hr>

#### Answer:
$M=\begin{bmatrix}
0&1\\1&0
\end{bmatrix}$

#### *[This question was from 8. Rendering: Action]*
<hr>

#### Answer:
$O(N^2)$ since there are $N$ multiplications and $N-1$ additions.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

#### Answer:
$$
F[k]=\sum_{n=0}^{N-1}{f[n]e^{-2\pi i\frac{kn}{N}}}\,\,\,\, \mathrm{for}\,k=0,1,\cdots,N-1
$$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

#### Answer:
Turning computational models into physical 3D objects using additive (e.g. 3D printers) or subtractive (e.g. laser cutting) processes.

#### *[This question was from Maths Recap]*
<hr>

#### Answer:
Subtractive. Start with white and subtract cyan, magenta and yellow.

#### *[This question was from 2. Images & Colours]*
<hr>

#### Answer:
Allows easy iteration along path of a curve.

#### *[This question was from 15. 2D curves]*
<hr>

