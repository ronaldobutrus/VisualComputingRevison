# Question Set 12 - Fundamentals of Visual Computing
### Question 1
What is Computer Graphics?

#### Answer 1:
Synthesising an image from a model (usually geometry, appearance and lighting properties of a scene).

#### *[This question was from 1. Introduction]*
<hr>

### Question 2
What would the formula for enhancing the contrast of an image be?

#### Answer 2:
$O(x,y) = \begin{bmatrix}
\frac{I(x,y)-p}{q}
\end{bmatrix}_0^{255}$ where $p$ is arbitary and $q<1$.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 3
What are Bezier Curves (in terms of Hermite Curves)?

#### Answer 3:
Bezier Curves are Hermite Curves where the gradient is encoded such that <br><br>
$\frac{d\bold{p}}{dt}(0)=3(\bold{p}_1-\bold{p}_0)$<br>
$\frac{d\bold{p}}{dt}(1)=3(\bold{p}_3-\bold{p}_2)$

#### *[This question was from 16. Bezier Curves]*
<hr>

### Question 4
What is the main disadvantage of FFT?

#### Answer 4:
It requires inputs of size $N=2^k$, so the input may need padding.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 5
What is the formula for the implicit representation of a sphere in 3D?

#### Answer 5:
$f(\bold{x})=\lvert\lvert \bold{x}\rvert\rvert-r$

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 6
What is the polar form of an imaginary number and what does each value represent?

#### Answer 6:
$z=re^{i\phi}$ where:
- $r$ is the radius (magnitude) of $z$
- $\phi$ is the argument (angle) equal to $\tan^{-1}{\frac{b}{a}}$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 7
What happens when the aperture becomes too big?

#### Answer 7:
The light rays from different parts of the image are mixed up on the image, so it becomes blurry.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 8
What is a texture?

#### Answer 8:
An image applied to a surface, which requires a mapping between points on the texture to points on the surface.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 9
What is a periodic function?

#### Answer 9:
A function $f(x)$ is periodic if it is defined for all real $x$ and if there is a positive number $T$ such that $f(x+T)=f(x)$.

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 10
What is the formula for the inverse Fourier Transform that restores $f$ from $F$?

#### Answer 10:
$$f(x)=\mathcal{F}^{-1}[F](x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(\omega) e^{i\omega x} \, d\omega
$$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 11
How does the Z-buffer method work, qualitatively?

#### Answer 11:
For each polygon:
1. Project the polygon vertices onto a frame buffer.
2. Convert to pixels.
4. For each pixel, compare colour and depth with existing pixel colour and depth. If closer, then update colour and depth.

#### *[This question was from 11. Hidden Surface Removal]*
<hr>

### Question 12
What is a reference frame?

#### Answer 12:
A collection of vectors (two for 2D space, three for 3D space) such that any vector in the space can be represented with respect to the reference frame.

#### *[This question was from 9. 3D Transformations]*
<hr>

### Question 13
What are the applications of the Fourier Transform in images?

#### Answer 13:
- Low and high pass filtering
- Fast linear filtering using the convolution theorem
- Removing structured noise
- Image compression (JPEG with DCT)

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 14
What are the four types of photoreceptor in the human retina and what are they sensitive to?

#### Answer 14:
Rods (night vision), blue cones, green cones and red cones sensitive to short, medium and long wavelengths respectively.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 15
Suppose we carry out the Marching Squares algorithm and we get the corners as ($out, in, out, in$) for ($a,b,c,d$). Does the boundary cross at $a$ and $c$ or $b$ and $d$? What should we do to avoid problems in the resulting mesh?

#### Answer 15:
Pick one way to interpret the sample and stick to it.  

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 16
Is CMY additive or subtractive?

#### Answer 16:
Subtractive. Start with white and subtract cyan, magenta and yellow.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 17
How many degrees of freedom does a homography have and why?

#### Answer 17:
8, as it is defined up to scale.

#### *[This question was from 10. Projection]*
<hr>

### Question 18
Consider this perspective projection.<br>
An object of height $H$ is at distance $W$ from the camera.<br>
An image plane of height $h$ is at distance $w$ from the camera.<br>
What is $h$ in terms of the other three variables?

#### Answer 18:
$h=w\frac{H}{W}$ (using similar triangles where side ratios within each triangle are equal).

#### *[This question was from 10. Projection]*
<hr>

### Question 19
What is HSV and what is it used for?

#### Answer 19:
Hue, Saturation, Value. Common for colour pickers in graphics packages - more intuitive.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 20
What is the norm (or magnitude) of a vector given by?

#### Answer 20:
For a vector $ 
\bold{x} =
\begin{bmatrix}
x_1 & x_2 & \cdots & x_n \\
\end{bmatrix}^T
$ its magnitude $\lvert\lvert \bold{x}\rvert\rvert = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$

#### *[This question was from Maths Recap]*
<hr>

