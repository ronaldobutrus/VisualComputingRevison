# Question Set 1 - Fundamentals of Visual Computing
### Question 1
For two curves $f(t)$ and $g(t)$ connected at $t_0$, what is meant by $C^{0}$ continuity?

#### Answer:
Curves are connected, i.e. $f(t_0)=g(t_0)$.

#### *[This question was from 15. 2D curves]*
<hr>

### Question 2
What is Euler's formula? What are the formulae for $\cos{\phi}$ and $\sin{\phi}$ that are derived from it?

#### Answer:
$$e^{i\phi}=\cos{\phi}+i\sin{\phi}$$
$$\cos{\phi}=\frac{e^{i\phi}+e^{-i\phi}}{2}$$
$$\sin{\phi}=\frac{e^{i\phi}-e^{-i\phi}}{2}$$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 3
What is a digital image in terms of a real scene?

#### Answer:
A 2D sampled representation of the real scene (i.e. of a continuous function).

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 4
What is CMYK? Give three reasons for using K?

#### Answer:
Cyan Magenta Yellow Black. Black added to:
- accurately print black
- save ink compared to using C+M+Y
- print fine black text without having to align colour perfectly
- save moneyy (black ink is cheaper)

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 5
What is a mesh?

#### Answer:
A mesh discretises a continuous geomtric surface with different levels of details.

#### *[This question was from 14. Geomtric Modelling]*
<hr>

### Question 6
How many hours of exposure did the first surviving photograph need? What sort of year range was this?

#### Answer:
1765-1833 - 8 hours. 

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 7
What is the Fourier Series?

#### Answer:
If $f(x)$ is a period function with period $2\pi$, the function can be represented using the Fourier Series:
$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}{a_n \cos{nx}}+\sum_{n=1}^{\infty}{b_n \sin{nx}}
$$

#### *[This question was from 5. The Fourier Transform]*
<hr>

### Question 8
Name three types of reconstruction filters.

#### Answer:
- Box filter - okay but leaky.
- Tent filter - suppresses high frequencies stronger, reduces artefacts.
- B-spline filter - ver smooth, removes alias spectra, but also smooths base spectrum.

#### *[This question was from 7. Sampling Theory]*
<hr>

### Question 9
What is a homography?

#### Answer:
A perspective-like transform in the plane, represented by a $3\times3$ matrix.

#### *[This question was from 10. Projection]*
<hr>

### Question 10
What is a **mipmap** and what is the main advantage of using mipmaps?

#### Answer:
A mipmap is a complete set of downsampled images for a given texture.<br>
The rendering engine will automatically determine the level of texture to use based on the object's size on the screen when it is rendered, so this **avoids aliasing** and **saves computation time**.

#### *[This question was from 13. Texturing Surfaces]*
<hr>

### Question 11
What is shot noise?

#### Answer:
Since photons hit sensor randomly, this is inevitable.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 12
What is the implicit representation of a line in 2D?

#### Answer:
$f(x)=\bold{n}\cdot(x-\bold{a})$

#### *[This question was from 15. 2D curves]*
<hr>

### Question 13
What does histogram equalisation do?

#### Answer:
Redestributes intensities to enhance the image contrast.

#### *[This question was from 4. Image Filtering]*
<hr>

### Question 14
What is the convolution $(f\ast g)(x)$ for functions $f$ and $g$ given by?

#### Answer:
$$
(f\ast g)(x)=\int^{\infty}_{-\infty}{f(x-y)g(y)\,dy}
$$

#### *[This question was from 6. Properties & Applications of the Fourier Transform]*
<hr>

### Question 15
What happens if the aperture becomes too small?

#### Answer:
Less light gets throuogh (so you will need to increase the exposure). Diffraction effect increases.

#### *[This question was from 3. Imaging & Display]*
<hr>

### Question 16
What is subdivision?

#### Answer:
A process in which a polyline/mesh is recusively refined in order to achieve a smooth curve/surface.

#### *[This question was from 17. Surfaces & Volumes]*
<hr>

### Question 17
Is CMY additive or subtractive?

#### Answer:
Subtractive. Start with white and subtract cyan, magenta and yellow.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 18
What is rasterisation?

#### Answer:
Converting a continuous or vector image representation into a rectangular sampled grid of pixels.

#### *[This question was from 2. Images & Colours]*
<hr>

### Question 19
What are the three most common types of model, and briefly what is each?

#### Answer:
- **Solid**: implicit representation (used in CAD)
- **Voxel**: explicit representation (used in medical imaging/robotics)
- **Surface**: parametric representation (used in games/films)

#### *[This question was from 14. Geomtric Modelling]*
<hr>

### Question 20
What is a matrix?

#### Answer:
A rectangular array of numbers?

#### *[This question was from Maths Recap]*
<hr>

