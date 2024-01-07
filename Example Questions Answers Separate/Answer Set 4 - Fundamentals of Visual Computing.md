# Answer Set 4 - Fundamentals of Visual Computing
#### Answer:
It summarises the distribution of intensities in an image.

#### *[This question was from 4. Image Filtering]*
<hr>

#### Answer:
Dilation after erosion. Simplifies bright objects while avoiding shrinkage of boundaries caused by erosion.

#### *[This question was from 4. Image Filtering]*
<hr>

#### Answer:
Additive (start with black and add R, G and B).

#### *[This question was from 2. Images & Colours]*
<hr>

#### Answer:
Reduces the width of bright objects.
$$
(I\ominus B)(x,y) = \min_{(i,j)\in B}I(x-i, y-j)$$

#### *[This question was from 4. Image Filtering]*
<hr>

#### Answer:
Square matrix with non-zero determinant?

#### *[This question was from Maths Recap]*
<hr>

#### Answer:
Ambient lighting model

#### *[This question was from 12 Lighting]*
<hr>

#### Answer:
$\mathcal{F}[af+bg](\omega)=a\mathcal{F}[f](\omega)+b\mathcal{F}[g](\omega)$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

#### Answer:
Objects must be modelled with **planar** surfaces.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

#### Answer:
Scan conversion algorithm:
- Consider each scanline, one by one.
- Decide which pixels are 'in' and 'out' by switching between them at boundary crossings.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

#### Answer:
Pick one way to interpret the sample and stick to it.  

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

#### Answer:
$
\begin{bmatrix}
1 & 0& -1\\
2 & 0& -2\\
1 & 0& -1
\end{bmatrix}
$

#### *[This question was from 4. Image Filtering]*
<hr>

#### Answer:
$f(t)=r\begin{bmatrix}\cos{t}\\\sin{t}\end{bmatrix}$

#### *[This question was from 15. 2D curves]*
<hr>

#### Answer:
$$e^{i\phi}=\cos{\phi}+i\sin{\phi}$$
$$\cos{\phi}=\frac{e^{i\phi}+e^{-i\phi}}{2}$$
$$\sin{\phi}=\frac{e^{i\phi}-e^{-i\phi}}{2}$$

#### *[This question was from 5. The Fourier Transform]*
<hr>

#### Answer:
$\bold{K}=\begin{bmatrix}
\alpha &\gamma & c_x\\
0 & \beta & c_y\\
0 & 0 & 1
\end{bmatrix}$ where $\alpha$ and $\beta$ scale it, $\gamma$ shears it and $c_x$ and $c_y$ translates it.<br> This matrix refers to the **intrinsic** parameters of the camera.

#### *[This question was from 10. Projection]*
<hr>

#### Answer:
$
\begin{bmatrix}
0&-1&0\\
-1&5&-1\\
0&-1&0
\end{bmatrix}
$

#### *[This question was from 4. Image Filtering]*
<hr>

#### Answer:
For a vector $ 
\bold{x} =
\begin{bmatrix}
x_1 & x_2 & \cdots & x_n \\
\end{bmatrix}^T
$ its magnitude $\lvert\lvert \bold{x}\rvert\rvert = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$

#### *[This question was from Maths Recap]*
<hr>

#### Answer:
The geometry constraints, i.e. its values and gradients at the start and end points.

#### *[This question was from 16. Bezier Curves]*
<hr>

#### Answer:
Increases the width of bright objects.
$$
(I\oplus B)(x,y) = \max_{(i,j)\in B}I(x-i, y-j)$$

#### *[This question was from 4. Image Filtering]*
<hr>

#### Answer:
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

#### Answer:
First apply low-pass Guassian filter to blur the image, then subsample. The filter size should double for each reduction by power of 2.

#### *[This question was from 8. Rendering: Action]*
<hr>

