# Question Set 4 - Fundamentals of Visual Computing
### Question 1
What are the main two disadvantages of explicit representation?

#### Answer 1:
- Cannot represent vertical lines.
- Cannot represent a curve with two output values for a single input.

#### *[This question was from 15. 2D curves]*
<hr>

### Question 2
What is diffraction?

#### Answer 2:
Bending of light rays when they encounter an obstacle or slit.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 3
What is perspective projection, qualitatively?

#### Answer 3:
Light travels in straight lines, all rays from the object passing through one point (the *focus*).<br>
Ray colours are recorded on a planar surface (the *window*).

#### *[This question was from 10. Projection]*
<hr>

### Question 4
What is the complex conjugate of $z=a+bi$?

#### Answer 4:
$\bar z = a-bi =re^{-i\phi}$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 5
Assume we are using backward mapping. What do we do in the (likely) case that $(s,t)$ does not map directly to one texel, but somewhere in the middle of four?

#### Answer 5:
Use bilinear interpolation to read the contributions from the four corners in the texture.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 6
What is the name of the algorithm for sampling an implicit surface using a grid?

#### Answer 6:
Marching Squares.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 7
What does LCD stand for and how do they work?

#### Answer 7:
Liquid Crystal Displays (LCDs).
Incident light is polarised. Voltage across the liquid crystal controls how much light passes:<br>
Voltage **ON**: no light (crystals align the electric field).
Voltage **OFF**: maximum light (crystals align each other, twisting light, i.e. maintaining polarisation).

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 8
For matrix
$
\bold{A} = 
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{bmatrix}
$ what is $s\bold{A}$?

#### Answer 8:
$
s\bold{A} = 
\begin{bmatrix}
sa_{11} & sa_{12} \\
sa_{21} & sa_{22} \\
\end{bmatrix}
$

#### *[This question was from Maths Recap]*
<hr>

### Question 9
What would the formula for making an image brighter be?

#### Answer 9:
$O(x,y) = I(x,y) + k$ where $k$ is an arbitrary value.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 10
What is thermal noise and when is it common?

#### Answer 10:
Due to random fluctuations of electrons when photo sensor is ampligied. Common in low-light situations where more amplification is needed.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 11
What is Euler's formula? What are the formulae for $\cos{\phi}$ and $\sin{\phi}$ that are derived from it?

#### Answer 11:
$$e^{i\phi}=\cos{\phi}+i\sin{\phi}$$
$$\cos{\phi}=\frac{e^{i\phi}+e^{-i\phi}}{2}$$
$$\sin{\phi}=\frac{e^{i\phi}-e^{-i\phi}}{2}$$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 12
What is *good* sampling?

#### Answer 12:
Sampling often and wisely.

#### *[This question was from 7. Sampling Theory]*
<hr>

### Question 13
How can you carry out a perspective projection with a moved camera?

#### Answer 13:
A camera is a rigid body, so it can be rotated and translated.

#### *[This question was from 10. Projection]*
<hr>

### Question 14
What is digital imaging?

#### Answer 14:
Capturing digital photographic images.

#### *[This question was from 1. Introduction]*
<hr>

### Question 15
Give an example of an interpolating subdivision scheme.

#### Answer 15:
The 4-point scheme.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 16
For matrices 
$
\bold{A} = 
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{bmatrix}
$ and 
$
\bold{B} = 
\begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
\end{bmatrix}
$ what is $\bold{A} + \bold{B}$?

#### Answer 16:
$\bold{A} + \bold{B} = 
\begin{bmatrix}
a_{11}+b_{11}& a_{12}+b_{12} \\
a_{21}+b_{21}& a_{22}+b_{22} \\
\end{bmatrix}
$

#### *[This question was from Maths Recap]*
<hr>

### Question 17
What is an analogue signal?

#### Answer 17:
A continuous signal that contains time-varying quantities. <br>It is always smooth, carries repeated information.<br>
It is easily affected by noise and hard to analyse.

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 18
How can we use remove structured noise using the Discrete Fourier Transform?

#### Answer 18:
Discard the regions in spectrum associated with the patterned noise.

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 19
What determines the colour of a light ray?

#### Answer 19:
Its overall spectral disribution of energy in the light ray.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 20
What is the *linearity* property (Fourier Transform)?

#### Answer 20:
$\mathcal{F}[af+bg](\omega)=a\mathcal{F}[f](\omega)+b\mathcal{F}[g](\omega)$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

