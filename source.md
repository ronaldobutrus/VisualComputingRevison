# 1. Introduction
### Question
What is digital imaging?
### Answer
Capturing digital photographic images.
### Question
What is image processing?
### Answer
Performing operations to an image to produce another image.
### Question
What do displays do (at a high level)?
### Answer
They make a digital representation of an image visible using emissive media.
### Question
What do printers do (at a high level)?
### Answer
They make a digital representation of an image visible using reflective media (paper).
### Question
What is Computer Vision?
### Answer
Understanding and reconstructing information about real-world scenes from image and video data.
### Question
What is Computer Graphics?
### Answer
Synthesising an image from a model (usually geometry, appearance and lighting properties of a scene).
### Question
What is modelling?
### Answer
Representing and manipulating virtual objects (including geometry, apperance and lighting properties).
### Question
What is animation?
### Answer
Putting virtual objects into motion using physical models and/or motion capture.
### Question
What is fabrication?
### Answer
Turning computational models into physical 3D objects using additive (e.g. 3D printers) or subtractive (e.g. laser cutting) processes.
# Maths Recap
### Question
How is a point represented as a vector in 2D and 3D respectively?
### Answer
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
### Question
How can a column vector be changed into a row vector?
### Answer
Transposition ($p^\prime = p^T$).
### Question
What is the norm (or magnitude) of a vector given by?
### Answer
For a vector $ 
\bold{x} =
\begin{bmatrix}
x_1 & x_2 & \cdots & x_n \\
\end{bmatrix}^T
$ its magnitude $\lvert\lvert \bold{x}\rvert\rvert = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$
### Question
For $\bold{x} = \begin{bmatrix}
a & b \\
\end{bmatrix}^T$ and $\bold{y} =\begin{bmatrix}
c & d \\
\end{bmatrix}^T$ what is $\bold{x} + \bold{y}$?
### Answer
$\begin{bmatrix}
a+b & c+d \\
\end{bmatrix}^T$
### Question
For $\bold{x} = \begin{bmatrix}
a & b \\
\end{bmatrix}^T$ what is $k\bold{x}$?
### Answer
$\begin{bmatrix}
ka & kb \\
\end{bmatrix}^T$
### Question
For vectors $ 
\bold{x} =
\begin{bmatrix}
x_1 & x_2 & \cdots & x_n \\
\end{bmatrix}^T$ and 
$ 
\bold{y} =
\begin{bmatrix}
y_1 & y_2 & \cdots & y_n \\
\end{bmatrix}^T$ what is the dot product $\bold{x}\cdot\bold{y}$ and what does it represent geometrically?
### Answer
$\bold{x}\cdot\bold{y} = \sum_{i=0}^n{x_i y_i}$
which is equal to $\lvert\lvert \bold{x}\rvert\rvert\,\lvert\lvert \bold{y}\rvert\rvert\cos{\theta}$ where $\theta$ is the angle between the two vectors.
### Question
For vectors $ 
\bold{x} =
\begin{bmatrix}
x_1 & x_2 & \cdots & x_n \\
\end{bmatrix}^T$ and 
$ 
\bold{y} =
\begin{bmatrix}
y_1 & y_2 & \cdots & y_n \\
\end{bmatrix}^T$ what is the cross product $\bold{x}\times\bold{y}$ and what does it represent geometrically?
### Answer
$
\bold{x}\times\bold{y}=\begin{bmatrix}
x_2 y_3 - x_3y_2 \\
x_3 y_1 - x_1y_3 \\
x_1 y_2 - x_2y_1 \\
\end{bmatrix}
$ represents the direction of the vector normal to the plane formed by vectors $\bold{x}$ and $\bold{y}$. The direction of this normal vector $\bold{x}\times\bold{y}$ is given by the right hand rule where the index and middle fingers point in the direction of $\bold{x}$ and $\bold{y}$ respectively and the thumb points in the direction of $\bold{x}\times\bold{y}$.
### Question
What is a matrix?
### Answer
A rectangular array of numbers.
### Question
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
### Answer
$\bold{A} + \bold{B} = 
\begin{bmatrix}
a_{11}+b_{11}& a_{12}+b_{12} \\
a_{21}+b_{21}& a_{22}+b_{22} \\
\end{bmatrix}
$
### Question
For matrix
$
\bold{A} = 
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{bmatrix}
$ what is $s\bold{A}$?
### Answer
$
s\bold{A} = 
\begin{bmatrix}
sa_{11} & sa_{12} \\
sa_{21} & sa_{22} \\
\end{bmatrix}
$
### Question
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
$ what is $\bold{A}\bold{B}$?
### Answer
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
### Question
Is addition of matrices commutative? (i.e. $\bold{A} + \bold{B} = \bold{B} + \bold{A}$)
### Answer
Yes
### Question
Is multiplication of matrices commutative? (i.e. $\bold{A} \bold{B} = \bold{B}\bold{A}$)
### Answer
No, $\bold{A} \bold{B} \neq \bold{B}\bold{A}$. For a transformation $\bold{A} \bold{B}$, first matrix $\bold{B}$ is applied, then $\bold{A}$.
### Question
Is multiplication of matrices associative? (i.e. $(\bold{A} \bold{B})\bold{C} = \bold{A}(\bold{B}\bold{C})$)
### Answer
Yes.
### Question
Is multiplication of matrices distributive? (i.e. $\bold{A} (\bold{B}+\bold{C}) = \bold{A}\bold{C}+\bold{A}\bold{C}$)
### Answer
Yes.
### Question
What is $(\bold{A}\bold{B}\bold{C})^T$ given by?
### Answer
$(\bold{A}\bold{B}\bold{C})^T = \bold{C}^T\bold{B}^T\bold{A}^T$.
### Question
What are the two requirements for calculating an inverse matrix $\bold{A}^{-1}$ from $\bold{A}$ where $\bold{A}\bold{A}^{-1}=\bold{I}$.
### Answer
Square matrix with non-zero determinant.
### Question
How can one solve a linear system of equations $2x+3y=6$ and $4x+9y=15$ using matrices?
### Answer
Express in matrix form $\bold{A}\bold{x}=\bold{b}$, calculate $\bold{A}^{-1}$. This gives $\bold{x} = \bold{A}^{-1}\bold{b}$. 
### Question
# 2. Images & Colours
What is the range of wavelengths of visible light? Which colours have the longest and shortest wavelengths?
### Answer
380nm (blue) to 750nm (red).
### Question
What is the formula relating the speed $s$ of an electromagnetic wave, its frequency $f$ and its wavelength $\lambda$?
### Answer
$s=f\lambda$ where $s$ is constant ($s=3\times10^8\textrm{ms}^{-1}$).
### Question
What determines the colour of a light ray?
### Answer
Its overall spectral disribution of energy in the light ray.
### Question
What determines the colour of light after it has reflected off a surface?
### Answer
Surfaces reflect light according to a spectral distribution, so the combination of incident spectrum and reflectance spectrum determines the light colour.
### Question
What is the formula relating incident radiance $E(\lambda)$, outgoing radiance $R(\lambda)$ and reflectance $S(\lambda)$?
### Answer
$R(\lambda) = E(\lambda)S(\lambda)$
### Question
What are the four types of photoreceptor in the human retina and what are they sensitive to?
### Answer
Rods (night vision), blue cones, green cones and red cones sensitive to short, medium and long wavelengths respectively.
### Question
Is the RGB model additive or subtractive?
### Answer
Additive (start with black and add R, G and B).
### Question
Can the RGB colour model generate every perceivable colour?
### Answer
In theory yes, but this would involve negative weights. In practice, it can generate a good fraction of all visible colours.
### Question
What is a digital image in terms of a real scene?
### Answer
A 2D sampled representation of the real scene (i.e. of a continuous function).
### Question
What is a pixel and what does it represent?
### Answer
Sampled digital values - smallest individual element in an image. Each pixel is a single sampled colour, usually represented in RGB.
### Question
What is rasterisation?
### Answer
Converting a continuous or vector image representation into a rectangular sampled grid of pixels.
### Question
What are some examples of rastering?
### Answer
Vector graphics and sampling an analogue signal (e.g. in a digital camera).
### Question
How are digital images arranged in memory (usually)?
### Answer
Pixels from left to right within a row. Rows from top to bottom.
### Question
For a greyscale image that is $w$ pixels wide and $h$ pixels high, what is the index in memory of the pixel at column x, row y? Assume the pixels are stored row by row.
### Answer
$y\times w + x$
### Question
For a RGBA colour image that is $w$ pixels wide and $h$ pixels high, what is the index in memory of the pixel at column x, row y? Assume the pixels are stored row by row.
### Answer
$4(y\times w + x)$ where 4 is the number of channels (for RGBA).
### Question
What are the two types of image compression, and how do they work (briefly)?
### Answer
**Lossless**: Enumerate frequent strings (e.g. PNG/GIF using LZW).<br>
**Lossy**: Encode high frequency components with fewer bits (e.g. JPEG using Discrete Cosine Transform).
### Question
What is the primary use difference between RGB and CYM?
### Answer
RGB is used for mixing lights (e.g. LCD monitor). CMY is used for filters and paints (e.g. printers).
### Question
Is CMY additive or subtractive?
### Answer
Subtractive. Start with white and subtract cyan, magenta and yellow.
### Question
What is CMYK? Give three reasons for using K?
### Answer
Cyan Magenta Yellow Black. Black added to:
- accurately print black
- save ink compared to using C+M+Y
- print fine black text without having to align colour perfectly
- save moneyy (black ink is cheaper)
### Question
What is HSV and what is it used for?
### Answer
Hue, Saturation, Value. Common for colour pickers in graphics packages - more intuitive.
### Question
What is CIEXYZ and what is it used for?
### Answer
Specifying colours and their ranges absolutely (can describe all visible colours).
### Question
# 3. Imaging & Display
How many hours of exposure did the first surviving photograph need? What sort of year range was this?
### Answer
1765-1833 - 8 hours. 
### Question
What was the first commercially successful photographic process called, how long for exposure and what was the image media?
### Answer
Daguerreotype process, minutes, on metallic plate (no copies) (1839).
### Question
How long must calotype photography undergo exposure, and what was the image media?
### Answer
Seconds, on paper (multiple copies). Used early paper-based negatives (1841).
### Question
What three elements form an image?
### Answer
Geometry, light and colour.
### Question
Describe the pinhole camera model.
### Answer
Captures all lights through a single point. <br>The point is called the **Centre of Projection** or **Optical Centre**.<br>
The size of the pinhole is called the **aperture**.<br>
The image is formed on the sensor (**image plane**) and is **inverted**.
### Question
What happens if the aperture becomes too small?
### Answer
Less light gets throuogh (so you will need to increase the exposure). Diffraction effect increases.
### Question
What is diffraction?
### Answer
Bending of light rays when they encounter an obstacle or slit.
### Question
What happens when the aperture becomes too big?
### Answer
The light rays from different parts of the image are mixed up on the image, so it becomes blurry.
### Question
What happens in the ideal pinhole?
### Answer
Only one ray of light reaches each point on the sensor. The image can be really dark and has heavy diffraction effects.
### Question
What does a lens do?
### Answer
It focuses parallel light onto a single focal point.
### Question
What is the focal point?
### Answer
A distance $f$ beyond the plane of the lens where the light is focused by the lens.
### Question
What shape are lens
### Answer
Usually spherical (easier to produce).
### Question
What is the formula that relates the focal distance $f$, the object distance $u$ and the image distance $v$?
### Answer
$\frac{1}{f}=\frac{1}{u}+\frac{1}{v}$
### Question
How is light recorded?
### Answer
Light is emitted from a source, it reflects off a scene element and enters the imaging system. The imaging syste produces an image on its image plane.
### Question
What does an image sensor do?
### Answer
Turns continuous light into pixels by the use of cells which detect photons (as electons) over an array of pixels.
### Question
How do CCD sensors differ from CMOS sensors?
### Answer
**CCD**: serial devices where pixels are read out one at a time.<br>
**CMOS**: each pixel contains an amplifier, so read-out can be faster.
### Question
What does LCD stand for and how do they work?
### Answer
Liquid Crystal Displays (LCDs).
Incident light is polarised. Voltage across the liquid crystal controls how much light passes:<br>
Voltage **ON**: no light (crystals align the electric field).
Voltage **OFF**: maximum light (crystals align each other, twisting light, i.e. maintaining polarisation).
### Question
How do LCDs achieve colour?
### Answer
They have small RGB filters over the pixels to provide three colours. <br>Projectors use 3LCD panels to mix the light using mirrors and lens.
### Question
What is thermal noise and when is it common?
### Answer
Due to random fluctuations of electrons when photo sensor is ampligied. Common in low-light situations where more amplification is needed.
### Question
What is shot noise?
### Answer
Since photons hit sensor randomly, this is inevitable.
### Question
What is replacement noise (or *salt and pepper noise*)?
### Answer
Defective sensors cause *dead pixels*. Charge leakage in long exposures cause *hot pixels*.
### Question
# 4. Image Filtering
What is quantisation?
### Answer
Quantising, i.e. rounding, pixel values for use in computers. This limits precision and the number of intensity levels.
### Question
What is colour depth? For a colour depth of $n$, how many colours can be represented?
### Answer
Number of bits needed per colour. For a colour depth of $n$, $2^n$ colours can be represented.
### Question
What would the formula for inverting an image be?
### Answer
$O(x,y) = 255 - I(x,y)$
### Question
What would the formula for making an image brighter be?
### Answer
$O(x,y) = I(x,y) + k$ where $k$ is an arbitrary value.
### Question
What would the formula for enhancing the contrast of an image be?
### Answer
$O(x,y) = \begin{bmatrix}
\frac{I(x,y)-p}{q}
\end{bmatrix}_0^{255}$ where $p$ is arbitary and $q<1$.
### Question
What does an image histogram do?
### Answer
It summarises the distribution of intensities in an image.
### Question
What does histogram equalisation do?
### Answer
Redestributes intensities to enhance the image contrast.
### Question
What iis a box filter?
### Answer
A neighbourhood filter that gives equal weight to all neighbouring pixels to calculate an average for a given pixel.
### Question
What does a Guassian filter do differently to a box filter?
### Answer
Gives more weight to the central and closer pixels than the further ones. Defined by a standar deviation $\sigma$.
### Question
What is convolution?
### Answer
A general filtering approach that supports arbitrary kernels.
### Question
What is a kernel?
### Answer
A matrix that defines the weight of neighbouring pixels in calculating the weighted average.
### Question
What are Sobel filters?
### Answer
They are convolution filters that show horizontal, vertical and diagonal gradients.
### Question
What is the horizontal gradients Sobel filter matrix?
### Answer
$
\begin{bmatrix}
1 & 0& -1\\
2 & 0& -2\\
1 & 0& -1
\end{bmatrix}
$
### Question
What is the vertical gradients Sobel filter matrix?
### Answer
$
\begin{bmatrix}
1&2&1\\
0&0&0\\
-1&-2&-1
\end{bmatrix}
$
### Question
What is the diagonal gradients Sobel filter matrix?
### Answer
$
\begin{bmatrix}
2&1&0\\
1&0&-1\\
0&-1&-2
\end{bmatrix}
$ or 
$
\begin{bmatrix}
0&-1&-2\\
1&0&-1\\
2&1&0
\end{bmatrix}
$
### Question
What is the motion blur filter matrix?
### Answer
$\frac{1}{5}
\begin{bmatrix}
0&0&0&0&1\\
0&0&0&1&0\\
0&0&1&0&0\\
0&1&0&0&0\\
1&0&0&0&0\\
\end{bmatrix}
$
### Question
What is the sharpening (unsharp masking) filter matrix?
### Answer
$
\begin{bmatrix}
0&-1&0\\
-1&5&-1\\
0&-1&0
\end{bmatrix}
$
### Question
What is median filtering and what are its advantages?
### Answer
Replacing each pixel with the median value of all pixels in the neighbourhood.<br>
- Colour changes smoothly in a small patch.
- Good against sparse random noise.
### Question
How does morphological filtering work? Does it use kernels?
### Answer
It uses set theory to filter images using a **structuring element** (set of pixel offsets) to deetermine which pixels should be in the set.
### Question
What is erosion? And what is the formula?
### Answer
Reduces the width of bright objects.
$$
(I\ominus B)(x,y) = \min_{(i,j)\in B}I(x-i, y-j)$$
### Question
What is dilation? And what is the formula?
### Answer
Increases the width of bright objects.
$$
(I\oplus B)(x,y) = \max_{(i,j)\in B}I(x-i, y-j)$$
### Question
What is opening (in morphological filtering)?
### Answer
Dilation after erosion. Simplifies bright objects while avoiding shrinkage of boundaries caused by erosion.
### Question
What is closing (in morphological filtering)?
### Answer
Erosion after dilation. Simplifies bright objects while avoiding expansion of boundaries caused by dilation.
### Question
# 5. The Fourier Transform
What is an analogue signal?
### Answer
A continuous signal that contains time-varying quantities. <br>It is always smooth, carries repeated information.<br>
It is easily affected by noise and hard to analyse.
### Question
What is a periodic function?
### Answer
A function $f(x)$ is periodic if it is defined for all real $x$ and if there is a positive number $T$ such that $f(x+T)=f(x)$.
### Question
What is the Fourier Series?
### Answer
If $f(x)$ is a period function with period $2\pi$, the function can be represented using the Fourier Series:
$$
f(x)=\frac{a_0}{2}+\sum_{n=1}^{\infty}{a_n \cos{nx}}+\sum_{n=1}^{\infty}{b_n \sin{nx}}
$$
### Question
What are the formulae for the coefficients of the Fourier Series?
### Answer
$$
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}{f(x)\cos(nx)\,dx}
$$
$$
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}{f(x)\sin(nx)\,dx}
$$
### Question
For a complex number $z=a+bi\in\mathbb{C}$, what are the real and imaginary parts?
### Answer
$\mathrm{Re}(z) = a\in\mathbb{R}$<br>
$\mathrm{Im}(z) = b\in\mathbb{R}$
### Question
What is $i^2$?
### Answer
$i^2=-1$
### Question
What is the polar form of an imaginary number and what does each value represent?
### Answer
$z=re^{i\phi}$ where:
- $r$ is the radius (magnitude) of $z$
- $\phi$ is the argument (angle) equal to $\tan^{-1}{\frac{b}{a}}$
### Question
What is the complex conjugate of $z=a+bi$?
### Answer
$\bar z = a-bi =re^{-i\phi}$
### Question
What is the magnitude of $z=a+bi$?
### Answer
$\lvert z\rvert=\sqrt{z \bar z}=\sqrt{a^2+b^2}$
### Question
What is Euler's formula? What are the formulae for $\cos{\phi}$ and $\sin{\phi}$ that are derived from it?
### Answer
$$e^{i\phi}=\cos{\phi}+i\sin{\phi}$$
$$\cos{\phi}=\frac{e^{i\phi}+e^{-i\phi}}{2}$$
$$\sin{\phi}=\frac{e^{i\phi}-e^{-i\phi}}{2}$$
### Question
What is the formula for the Fourier Transform of a function $f:\mathbb{R}\to\mathbb{R}$?
### Answer
$$F(\omega) =\mathcal{F}[f](\omega) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} f(x) e^{-i\omega x} \, dx
$$
### Question
What is the formula for the inverse Fourier Transform that restores $f$ from $F$?
### Answer
$$f(x)=\mathcal{F}^{-1}[F](x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(\omega) e^{i\omega x} \, d\omega
$$
### Question
What is the Fourier Transform, qualitatively?
### Answer
A transformation that represents signals in terms of their frequencies.
### Question
How do frequencies apply to images?
### Answer
Images can be analysed using frequencies in the x and y directions.
### Question
What are the applications of the Fourier Transform in images?
### Answer
- Low and high pass filtering
- Fast linear filtering using the convolution theorem
- Removing structured noise
- Image compression (JPEG with DCT)
### Question
# 6. Properties & Applications of the Fourier Transform
What is the *linearity* property (Fourier Transform)?
### Answer
$\mathcal{F}[af+bg](\omega)=a\mathcal{F}[f](\omega)+b\mathcal{F}[g](\omega)$
### Question
What is the *shifting* property (Fourier Transform)?
### Answer
For a constant $a$, if $g(x)=f(x-a)$, then
$$
\mathcal{F}[g](\omega)=e^{-ia\omega}\mathcal{F}[f](\omega)
$$
### Question
What is the *modulation* property (Fourier Transform)?
### Answer
For a constant $a$, if $g(x)=e^{-ia\omega}f(x)$, then
$$
\mathcal{F}[g](\omega)=\mathcal{F}[f](\omega-a)
$$
### Question
What is the *scaling* property (Fourier Transform)?
### Answer
For a constant $a$, if $g(x)=f(ax)$, then
$$
\mathcal{F}[g](\omega)=\frac{1}{\lvert a\rvert}\mathcal{F}[f](\frac{\omega}{a})
$$
### Question
What is the convolution $(f\ast g)(x)$ for functions $f$ and $g$ given by?
### Answer
$$
(f\ast g)(x)=\int^{\infty}_{-\infty}{f(x-y)g(y)\,dy}
$$
### Question
What is the convolution theorem?
### Answer
$\mathcal{F}[f\ast g](\omega)=\sqrt{2\pi}\mathcal{F}[f](\omega)\cdot\mathcal{F}[g](\omega)$
### Question
What is the advantage of using the Fourier domain to carry out convolution?
### Answer
It becomes multiplication, which is more efficient especially for large kernels.
### Question
What is the Discrete Fourier Transform (DFT), qualitatively?
### Answer
Transforms discrete analogue to the continuous Fourier transform.
- Deals with finite sampled signals such as audio, images.
- $N$ values are decomposed into $N$ frequency components.
### Question
What is the formula for the Discrete Fourier Transform (DFT)?
### Answer
$$
F[k]=\sum_{n=0}^{N-1}{f[n]e^{-2\pi i\frac{kn}{N}}}\,\,\,\, \mathrm{for}\,k=0,1,\cdots,N-1
$$
### Question
What is the formula for the inverse Discrete Fourier Transform (DFT)?
### Answer
$$
f(n)=\frac{1}{N}\sum_{n=0}^{N-1}{F[k]e^{2\pi i\frac{kn}{N}}}\,\,\,\, \mathrm{for}\,k=0,1,\cdots,N-1
$$
### Question
What is the *periodicity* property of the Discrete Fourier Transform?
### Answer
$F[k+N]=F[k]$
### Question
What is the *cyclical convolution* formula for the Discrete Fourier Transform?
### Answer
$$(f\ast g)[n]=\sum_{m=0}^{N-1}f[m]f[n-m]$$
### Question
How can the Discrete Fourier Transform be generalised to n-D functions?
### Answer
$$
F[k,j]=\sum_{m=0}^{M-1}\sum_{n=0}^{N-1}{f[n,m]e^{-2\pi i(\frac{kn}{N}+\frac{jm}{M})}}\,\,\,\, \mathrm{for}\,j,k=0,1,\cdots,N-1 \,\mathrm{independently}
$$
The inverse follows the same pattern.
### Question
What is a low pass filter and what does it do?
### Answer
Passes signals with frequencies lower than the threshold - removes fine details and hence blurs an image.
### Question
What is a high pass filter and what does it do?
### Answer
Passes signals with frequencies higher than the threshold - removes low frequencies (overall shape) and extracts the edge images.
### Question
How can we use remove structured noise using the Discrete Fourier Transform?
### Answer
Discard the regions in spectrum associated with the patterned noise.
### Question
What is the Fast Fourier Transform (FFT), at a high level? What is its complexity?
### Answer
Splits an input of size $N$ into $\log_{2}{N}$ stages, each with $N/2$ butterfly computations. Each butterfuly computation takes two complex numbers $p$ and $q$ and computes two numbers $p+ki$ and $p-ki$. It then  This results in less additions and multiplications, giving it a complexity of $O(N\log_{2}{N})$.
### Question
What is the main disadvantage of FFT?
### Answer
It requires inputs of size $N=2^k$, so the input may need padding.
### Question
What is the complexity of the Discrete Fourier Transform?
### Answer
$O(N^2)$ since there are $N$ multiplications and $N-1$ additions.
### Question
What is the Discrete Cosine Transform (DCT)?
### Answer
The Fourier Transform of an even, real-valued signal.
### Question
How can we make audio signals and images even?
### Answer
Reflecting about n=0, canceling out purely imaginary, sine-related terms.
### Question
# 7. Sampling Theory
What is sampling?
### Answer
Capturing the value of a function at specific points.
### Question
What do we use to reconstruct the original continuous signal from samples?
### Answer
Convolution.
### Question
What is *good* sampling?
### Answer
Sampling often and wisely.
### Question
What is aliasing caused by?
### Answer
Sampling a high-frequency function with a low sampling frequency.
### Question
How does aliasing happen in signal samples? How does increasing the sample rate affect this?
### Answer
Naive downsampling causes overlapping overlapping spectra that cause fluctuations at certain frequencies. Increasing the sample rate moves overlapping spectra further apart in the frequency domain, reducing aliasing.
### Question
How can we use a filter to remove high frequencies in a frequency spectrum?
### Answer
Use a low-pass filter to remove high frequencies.
### Question
What is Nyquist's Theorem?
### Answer
To sample a band-limited signal without aliasing, we need to sample the highest frequency ($W$) more than twice per period, i.e. the minimum sampling rate is $2W$ and the maximum samplign distance is $1/2W$.
### Question
Name three types of reconstruction filters.
### Answer
- Box filter - okay but leaky.
- Tent filter - suppresses high frequencies stronger, reduces artefacts.
- B-spline filter - ver smooth, removes alias spectra, but also smooths base spectrum.
### Question
How can we better downsample images to prevent aliasing? 
### Answer
First apply low-pass Guassian filter to blur the image, then subsample. The filter size should double for each reduction by power of 2.
### Question
# 8. Rendering: Action
What is an affine transform, i.e. how is it expressed?
### Answer
$\bold{q}=\bold{M}\bold{p}+t$ where $\bold{p}=\begin{bmatrix}p_1\\p_2\end{bmatrix}$ and 
$\bold{M}=\begin{bmatrix}
m_{11}&m_{12}\\m_{21}&m_{22}
\end{bmatrix}$
### Question
What is the affine transform that does nothing?
### Answer
$M=\begin{bmatrix}
0&1\\1&0
\end{bmatrix}$
### Question
What is the affine transform to perform a counter-clockwise rotation by $\theta$ about the origin?
### Answer
$M=\begin{bmatrix}
\cos{\theta}&-\sin{\theta}\\
\sin{\theta}&\cos{\theta}
\end{bmatrix}$
### Question
What is the affine transform to scale a point by factor $a$ in the $x$-direction and $b$ in the $y$-direction?
### Answer
$M=\begin{bmatrix}
a&0\\
0&b\\
\end{bmatrix}$
### Question
What is the affine transform of a shear of factor $a$ in the $x$-direction and $b$ in the $y$-direction?
### Answer
$M=\begin{bmatrix}
1&a\\
b&1\\
\end{bmatrix}$
### Question
Given a translation $\bold{t}=\begin{bmatrix}t_1\\t_2\end{bmatrix}$ and transformation
$\bold{M}=\begin{bmatrix}
m_{11}&m_{12}\\m_{21}&m_{22}
\end{bmatrix}$, what is the homogeneous transformation matrix that represents $\bold{M}\bold{t}$?
### Answer
$\begin{bmatrix}
m_{11}&m_{12}&t_1\\
m_{21}&m_{22}&t_2\\
0&0&1
\end{bmatrix}$ which will apply on $\begin{bmatrix}
p_1\\
p_2\\
1
\end{bmatrix}$
### Question
Computer Vision and Computer Graphics do not use the same orientation of vectors? Which uses column vectors and which uses row vectors?
### Answer
Computer Vision uses column vectors.
Computer Graphics uses row vectors.
### Question
What is meant by an active transformation?
### Answer
Points are transformed in the original coordinate system.
### Question
What is meant by a passive transformation?
### Answer
Points remain fixed and the coordinate system moves.
### Question
How do we rotate about an arbitrary point?
### Answer
Translate the centre of rotation to the origin, rotate about the origin then translate the centre of origin back.
### Question
# 9. 3D Transformations
What is a reference frame?
### Answer
A collection of vectors (two for 2D space, three for 3D space) such that any vector in the space can be represented with respect to the reference frame.
### Question
What are right handed coordinates?
### Answer
With $x$ and $y$ displayed regularly on a page, the $z$ axis points out of the page.
### Question
What is the right-hand screw rule?
### Answer
For a rotation about an axis, the thumb aligning with the axis, the other fingers indicate a positive (counter-clockwise) rotation.
### Question
What are the 3D non-homogeneous rotation matrices for rotation about the $x$-axis?
### Answer
$
\bold{R}_x(\theta) = \begin{bmatrix}
1 & 0 & 0\\
0 & \cos{\theta} & -\sin{\theta}\\
0 & \sin{\theta} & \cos{\theta}
\end{bmatrix}
$
### Question
What are the 3D non-homogeneous rotation matrices for rotation about the $y$-axis?
### Answer
$
\bold{R}_y(\theta) = \begin{bmatrix}
\cos{\theta} & 0 & -\sin{\theta}\\
0 & 1 & 0\\
\sin{\theta} & 0 & \cos{\theta}
\end{bmatrix}
$
### Question
What are the 3D non-homogeneous rotation matrices for rotation about the $z$-axis?
### Answer
$
\bold{R}_z(\theta) = \begin{bmatrix}
\cos{\theta} & -\sin{\theta} & 0\\
\sin{\theta} & \cos{\theta} & 0\\
0 & 0 & 1\\
\end{bmatrix}
$
### Question
How can you rotate about an arbitrary axis $\bold{u}$?
### Answer
There are two ways - either use Rodrugies' rotation formula or:
1. Use $\bold{T}$ to translate the rotation axis to pass through the origin.
2. Use $\bold{R}_x$ and $\bold{R}_y$ to rotate $\bold{u}$ onto the $z$-axis.
3. Rotate about the $z$-axis by $\theta$.
4. Rotate $\bold{u}$ back into place.
5. Translate $\bold{u}$ back into place.<br><br>
This can be written as $\bold{T}^{-1}\bold{R}_x^{-1}\bold{R}_y^{-1}\bold{R}_z\bold{R}_y\bold{R}_x\bold{T}$.
### Question
What is the Gimbal lock?
### Answer
When two of the three rotational axes becomme aligned, we lose one degree of freedom. This means we cannot rotate in all three directions.
### Question
How can we represent homogeneous transformations in 3D?
### Answer
Add an extra row and column.<br>
$\bold{M}=
\begin{bmatrix}
m_{11} & m_{12} & m_{13} & t_x\\
m_{21} & m_{22} & m_{23} & t_y\\
m_{31} & m_{22} & m_{33} & t_z\\
0 & 0 & 0 & 1
\end{bmatrix}
$
### Question
If we have the Sun, Earth and Moon, how would you describe the hierarchy of transforms?
### Answer
1. Transform the Moon using the Earth frame. 
2. Transform the Earth and Moon using the Sun's frame.
### Question
# 10. Projection
What is parallel projection? For a point $p=\begin{bmatrix}p_1\\p_2\\p_3\\1\end{bmatrix}$ what is the associated matrix (in the world reference frame)?
### Answer
In parallel/orthographic projection, the light rays are parallel. In the world frame, just drop the $z$ coordinate.<br>
$$\bold{K}_{parallel}=\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 1
\end{bmatrix}$$
### Question
How would you carry out a parallel/orthographic projection with a moved camera? Let $\bold{M}$ be the matrix that transforms points from the world reference frame to the camera's reference frame, and let $\bold{p}$ be the vector representing the point to be projected.
### Answer
1. Transform the object from the camera frame into the world frame, i.e. $\bold{q}=\bold{M}^{-1}\bold{p}$.
2. Project, i.e. $\bold{q^{\prime}}=\bold{K}_{parallel}\,\bold{q}$.
### Question
What is perspective projection, qualitatively?
### Answer
Light travels in straight lines, all rays from the object passing through one point (the *focus*).<br>
Ray colours are recorded on a planar surface (the *window*).
### Question
Consider this perspective projection.<br>
An object of height $H$ is at distance $W$ from the camera.<br>
An image plane of height $h$ is at distance $w$ from the camera.<br>
What is $h$ in terms of the other three variables?
### Answer
$h=w\frac{H}{W}$ (using similar triangles where side ratios within each triangle are equal).
### Question
Consider this perspective projection.<br>
A point $\begin{bmatrix}x & y & z\end{bmatrix}^T$ is observed, which projects to the point $\begin{bmatrix}u & v & w\end{bmatrix}^T$ on the window.<br>
The window is planar, parallel to the $x$-$y$ plane, a distance $w$ to the origin.<br>
Express $\begin{bmatrix}u & v & w\end{bmatrix}^T$ in terms of $x$, $y$, $z$ and $w$. 
### Answer
$\begin{bmatrix}u \\ v \\ w\end{bmatrix}=\begin{bmatrix}wx/z \\ wy/z \\ wz/z\end{bmatrix}=w\begin{bmatrix}x/z \\ y/z \\ 1\end{bmatrix}$
### Question
What is the homogeneous matrix that represents a perspective projection (extrinsic parameters only)?
### Answer
$$\bold{K}_{perspective}=\frac{w}{z}\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 1/w & 0
\end{bmatrix}$$
Note that the multiplier is usually omitted and used at a later stage to make the coordinate non-homogeneous.
### Question
How can you carry out a perspective projection with a moved camera?
### Answer
A camera is a rigid body, so it can be rotated and translated.
### Question
How would you carry out a parallel/orthographic projection with a moved camera? Let $\bold{M}$ be the matrix that transforms points from the world reference frame to the camera's reference frame, and let $\bold{p}$ be the vector representing the point to be projected.
### Answer
1. Transform the object from the camera frame into the world frame, i.e. $\bold{q}=\bold{M}^{-1}\bold{p}$.
2. Project, i.e. $\bold{q^{\prime}}=\bold{K}_{parallel}\,\bold{q}$.
### Question
Consider a perspective camera with an image buffer. 
What is the homogeneous 2D matrix that transforms the image plane to the image buffer? What is this matrix called?
### Answer
$\bold{K}=\begin{bmatrix}
\alpha &\gamma & c_x\\
0 & \beta & c_y\\
0 & 0 & 1
\end{bmatrix}$ where $\alpha$ and $\beta$ scale it, $\gamma$ shears it and $c_x$ and $c_y$ translates it.<br> This matrix refers to the **intrinsic** parameters of the camera.
### Question
What is the $3\times4$ projection matrix that defines perspective projection (intrinsic and extrinsic parameters)?
Let $\bold{R}$ represent the rotation of the camera and $\bold{t}$ represent its offset from the origin.
### Answer
$$P=\bold{K}\begin{bmatrix}R &\vert&t\end{bmatrix}$$
i.e.
$$
P=\bold{K}\begin{bmatrix}
r_{11} & r_{12} & r_{13} & t_1\\
r_{21} & r_{22} & r_{33} & t_2\\
r_{31} & r_{32} & r_{33} & t_3\\
\end{bmatrix}
$$
The fourth row is often omitted, but would be $\begin{bmatrix}
0 & 0 & 0 & 1
\end{bmatrix}$.
### Question
What is a homography?
### Answer
A perspective-like transform in the plane, represented by a $3\times3$ matrix.
### Question
How many degrees of freedom does a homography have and why?
### Answer
8, as it is defined up to scale.
### Question
What transformations does a homography comprise of?
### Answer
Translation, rotation, scale, stretch and shear.
### Question
What is one use of homographies?
### Answer
Image stitching (by warping images together).
### Question
How can two or more 2D images be used to create a 3D model?
### Answer
**Triangulation:** if we have a single point observed on two images, we can trace the rays back to where they intersect.
### Question
# 11. Hidden Surface Removal
Homogeneous points scale freely - what does this mean?
### Answer
Homogeneous coordinates have an additional scaling factor $w$, e.g. $\begin{bmatrix}x&y&z&w\end{bmatrix}^T$. <br>
Two points $\bold{p}$ and $\bold{q}$ are equivalent ($\bold{p}\equiv\bold{q}$) if $\bold{p}=s\bold{q}$.
### Question
What is meant by *hidden surface removal*?
### Answer
Not depicting those parts of a scene that are not visible.
### Question
Name three approaches to hidden surface removal.
### Answer
- Painters algorithm
- Back-face culling
- Z-buffer
### Question
How does back-face culling work, qualitatively?
### Answer
Given an object modelled using planar surfaces, discard surfaces that face away from the camera.
### Question
What property must a model have in order for us to be able to use back-face culling?
### Answer
Objects must be modelled with **planar** surfaces.
### Question
What is the orientation of a polygon?
### Answer
A polygon is oriented by the ordering of its points, which can be either *clockwise* or *anti-clockwise*. 
### Question
Consider two edge vectors $\bold{a}=\overrightarrow{AB}$ and $\bold{b}=\overrightarrow{BC}$, connected tip-to-tail in clockwise fashion. The vector $\bold{v}$ is the viewing vector, i.e. vector pointing in the direction going from the object to the camera.<br><br>
How can we use edge vectors to determine if a surface faces away from the camera?
### Answer
The cross product of the edge vectors gives the normal vector $\bold{n}=\bold{a}\times\bold{b}$. <br>
Calculate the dot product of the normal with the viewing vector (i.e. $\bold{n}\cdot\bold{v}$).<br>
This also equal to $\lvert \bold{a}\rvert\lvert \bold{b}\rvert\cos\theta$ where $\theta$ is the angle between the two vectors, so the sign is siginificant.<br><br>
If the polygon is oriented **anti-clockwise**, then $\bold{n}$ points outward from the **front face** of the polygon.<br>
If the polygon is oriented **clockwise**, then $\bold{n}$ points outward from the **back face** of the polygon.<br><br>
Therefore in this case (clockwise):<br>
If $\bold{n}\cdot\bold{v}>0$ then the surface is facing away from the camera. ($\theta$ is between $-90\degree$ and $90\degree$)<br>
If $\bold{n}\cdot\bold{v}<0$ then the surface is facing towards the camera. ($\theta$ is less than $-90\degree$ or greater than $90\degree$)<br>
*Note that this is slightly different to what is in the slides, as they consider a normal going into the page to be $-\bold{n}$.
### Question
In what scenario will a surface be forward-facing but should not be rendered?
### Answer
If an object is not convex, then one face can be behind another. 
### Question
How does the Z-buffer method work, qualitatively?
### Answer
For each polygon:
1. Project the polygon vertices onto a frame buffer.
2. Convert to pixels.
4. For each pixel, compare colour and depth with existing pixel colour and depth. If closer, then update colour and depth.
### Question
How can you convert a projected polygon into pixels?
### Answer
Scan conversion algorithm:
- Consider each scanline, one by one.
- Decide which pixels are 'in' and 'out' by switching between them at boundary crossings.
### Question
How can you determine the depth of a pixel for a set of projected polygon vertices?
### Answer
Each vertex has a depth. Use *bi-linear interpolation* to calculate the depth of a point between these vertices.<br>
Consider a polygon with sides (clockwise) $h_{11}$, $h_{12}$, $h_{22}$ and $h_{21}$. <br>A point lies between these four vertices:
- a fractional length $0\leq a\leq1$ from $h_{11}$ to $h_{12}$
- a fractional length $0\leq b\leq1$ from $h_{11}$ to $h_{21}$<br><br>
The height at this point is given by
$$
(1-a)(1-b)h_{11} + (1-a)b\,h_{12} + a(1-b)\,h_{21} + ab\,h_{22}
$$
### Question
# 12. Lighting
What two main types of light are there?
### Answer
Specular and diffuse.
### Question
What is the name of the model that represents a reflection with specular incident and diffuse reflected light?
### Answer
Lambertian reflection model
### Question
What is the name of the model that represents a reflection with specular incident and specular reflected light?
### Answer
Phong model
### Question
What is the name of the model that represents a reflection with diffuse incident and diffuse reflected light?
### Answer
Ambient lighting model
### Question
Which three components of light does the standard model of light involve, and briefly what are each of these?
### Answer
**Specular**: shiny surfaces have small, intense highlights.<br>
**Diffuse**: dull surfaces have large highlights that fall off more gradually.<br>
**Ambient**: accounts for light scattered equally about entire scene.
### Question
What is the Lambert's Law?
### Answer
The intensity of reflected light is proportional to the cosine of the angle between the incoming light and the surface normal.
### Question
In specular to diffuse (Lambertian) reflection, describe how light is reflected.
### Answer
Light from a single source is reflected equally in all directions.
### Question
What is the formula for Lambertian reflection?
### Answer
$I_d=k_d i_d\cos\theta$
where:
- $I_d$ is the diffuse component of the reflected light intensity
- $k_d$ is the diffuse reflectivity (reflection ratio)
- $i_d$ is the diffuse component of the light source intensity
- $\theta$ is the angle beteen the light source and the normal.
### Question
In specular (to specular) reflection, what does the intensity of the specular highlight depend on?
### Answer
The angle $\phi$ between the viewing direction and the reflected ray. The smaller the angle, the brighter the reflection.
### Question
What is the formula for the Phong model?
### Answer
$I_s=k_s i_s\cos^{\alpha}\phi$
where:
- $I_s$ is the specular component of the reflected light intensity
- $k_s$ is the specular reflectivity (reflection ratio)
- $i_s$ is the specular component of the light source intensity
- $\phi$ is the angle beteen the viewing ray and the reflected ray
- $\alpha$ is the shininess coefficient.
### Question
How do you deal with RGB with respect to reflection?
### Answer
Calculate the reflected intensity for red, green and blue individually.
### Question
How does increasing the shininess ($\alpha$) affect the highlight on an object?
### Answer
As $\alpha$ increases, the highlight gets smaller and sharper.
### Question
What is the formula for diffuse to diffuse (ambient) lighting?
### Answer
$I_a=k_a i_a$
where:
- $I_a$ is the ambient component of the reflected light intensity
- $k_a$ is the ambient reflectivity (reflection ratio)
- $i_a$ is the ambient component of the light source intensity.
### Question
What is the formula for the standard lighting model?
### Answer
$I=k_a i_a + k_d i_d \cos\theta + k_s i_s \cos^{\alpha}\phi$
### Question
How is the standard lighting model adapted for multiple lights?
### Answer
$$I=k_a i_a + k_d \sum_{j}{i_{d_j} \cos\theta_j} + k_s \sum_{j}{i_{s_j} \cos^{\alpha}\phi_j}$$
### Question
Assuming the normalised vectors below, how can the multi-light standard lighting model be written using vector representation?
- $\bold{R}$: reflected ray
- $\bold{L}$: negative of incident ray
- $\bold{V}$: viewing ray
- $\bold{N}$: surface normal (out of surface)
### Answer
$$I=k_a i_a + k_d \sum_{j}{i_{d_j} (\bold{L}_i \cdot \bold{N})} + k_s \sum_{j}{i_{s_j} (\bold{R}_i \cdot \bold{V})}$$
This is true since for two **normalised** (unit) vectors $\bold{a}$ and $\bold{b}$, $\bold{a}\cdot\bold{b}=\cos\theta$.
### Question
Describe what is meant by *Gouraud* shading.
### Answer
- Compute a normal at each vertex of a polygon (by averaging normals of connected polygons).
- Use standard lighting model to calculate reflected light at each vertex.
- Use bilinear interpolation to calculate light at each point on the polygon.
### Question
Describe what is meant by *Phong* shading.
### Answer
- Compute a normal at each vertex of a polygon (by averaging normals of connected polygons).
- Use bilinear interpolation to calculate normal at each point on the polygon.
- Use standard lighting model to calculate reflected light at each point.
### Question
What is meant by flat shading?
### Answer
Using one normal (per polygon) to calculate light (once) for the entire polygon.
### Question
What is the BRDF?
### Answer
The Bidirectional Reflectance Distribution Functions (BRDF) is a 4D function that takes in incoming light angle and outgoing light angle (in spherical coordinate pairs) and calculates how much light is reflected off a given material.
### Question
# 13. Texturing Surfaces
What is a texture?
### Answer
An image applied to a surface, which requires a mapping between points on the texture to points on the surface.
### Question
What do you need to do to 3D objects to enable texture mapping to take place?
### Answer
You need to 'flatten' the geometry so a (near) 1-1 correspondence between points on the surface and texture can take place.
### Question
What are the two approaches to texture mapping?
### Answer
Forward mapping and backward mapping.
### Question
What is a texel?
### Answer
A texture element.
### Question
How does forward mapping work?
### Answer
Map each texel $(u,v)$ to surface point $(x,y,z)$. Copy the colour at $(u,v)$ to $(x,y,z)$.
### Question
How does backward mapping work?
### Answer
Map each surface point $(s,t)$ at $(x,y,z)$ to its corresponding texture coordinates $(u,v)$. Copy the colour at $(u,v)$ to $(x,y,z)$.
### Question
Assume we are using backward mapping. What do we do in the (likely) case that $(s,t)$ does not map directly to one texel, but somewhere in the middle of four?
### Answer
Use bilinear interpolation to read the contributions from the four corners in the texture.
### Question
Assume we are using forward mapping. What do we do in the (likely) case that $(u,v)$ does not map directly to one surface mesh point, but somewhere in the middle of four?
### Answer
Use bilinear interpolation to read the contributions from the four corners on the surface mesh.
### Question
How does bump mapping work and what is the formula for a normal $\bold{n}$ at a point $\bold{p}$ after it has been mapped?
### Answer
Perturb the surface normal, so even though the surface is flat, it looks bumpy.<br>
$\bold{n}^{\prime}=\bold{n}+f(\bold{p})$
### Question
How does displacement mapping work and what is the formula for a normal $\bold{n}$ at a point $\bold{p}$ after it has been mapped?
### Answer
Perturb the surface height, so the surface becomes bumpy.<br>
$\bold{p}^{\prime}=\bold{p}+f(\bold{p})\bold{n}$
### Question
How does environment mapping work?
### Answer
- Contain the scene with a texture sphere.
- Render the scene onto the sphere.
- Colour the surface using the reflection from the texture.
### Question
What is a **mipmap** and what is the main advantage of using mipmaps?
### Answer
A mipmap is a complete set of downsampled images for a given texture.<br>
The rendering engine will automatically determine the level of texture to use based on the object's size on the screen when it is rendered, so this **avoids aliasing** and **saves computation time**.
### Question
Given an $m\times n$ RGB image with 16 bits per channel, how much memory is used to store the mipmaps?
### Answer
$3\times 16 \times(mn + \frac{1}{4}mn + \frac{1}{16}mn+\cdots)$<br>
$= 3\times 16 \times mn(1+\frac{1}{4}+\frac{1}{16}+\cdots)$<br>
$= 3\times 16 \times \frac{4}{3}mn$<br>
$= 64mn$ bits or $8mn$ bytes
### Question
# 14. Geomtric Modelling
What are the three most common types of model, and briefly what is each?
### Answer
- **Solid**: implicit representation (used in CAD)
- **Voxel**: explicit representation (used in medical imaging/robotics)
- **Surface**: parametric representation (used in games/films)
### Question
What are the two main ways to create surface models?
### Answer
Artist-made modelling and 3D scanning.
### Question
What is a mesh?
### Answer
A mesh discretises a continuous geomtric surface with different levels of details.
### Question
Which shape do meshes come in and why?
### Answer
Triangles, because:
- simple
- efficiently rendered (three vertices on a plane)
- output of most 3D acquisition tools (scanners).
### Question
What is the face-vertex data structure?
### Answer
For each face, we have its three vertices.
For each vertex, we have its connected faces.
### Question
What is the face-edge-vertex data structure?
### Answer
Stores all relationships between faces, edges and vertexes (easily accessible but highly redundant).
For each face, we have its three vertices and three edges.
For each vertex, we have its connected faces and connected edges.
For each edge, we have its two vertices and two faces.
### Question
# 15. 2D curves
Outline the three main ways to represent a 2D curve, and briefly explain how each one works.
### Answer
- **Explicit**: represent one axis with respect to the other. <br>
i.e. $x_2=f(x_1)$
- **Parametric**: maps from a parameter $t$ to points on the curve.<br>
i.e. $f(t)$
- **Implicit**: a function of points in space which evaluate to zero on the curve.<br>
i.e. $f(x=0)$
### Question
What are the main two disadvantages of explicit representation?
### Answer
- Cannot represent vertical lines.
- Cannot represent a curve with two output values for a single input.
### Question
What is the main advantage of implicit representation?
### Answer
You can easily check if a point is on/inside/outside a curve by evaluating the function value.
### Question
What is the main advantage of parametric representation?
### Answer
Allows easy iteration along path of a curve.
### Question
What is the parametric representation of a line in 2D?
### Answer
$f(t)=\bold{a}+t\bold{v}$
### Question
What is the implicit representation of a line in 2D?
### Answer
$f(x)=\bold{n}\cdot(x-\bold{a})$
### Question
What is the explicit representation of a line in 2D?
### Answer
$x_2=mx_1+c$
### Question
What is the parametric representation of a circle in 2D?
### Answer
$f(t)=r\begin{bmatrix}\cos{t}\\\sin{t}\end{bmatrix}$
### Question
What is the implicit representation of a circle in 2D?
### Answer
$f(\bold{x})=\lvert\lvert x\rvert\rvert-r$
### Question
What is the explicit representation of a circle in 2D?
### Answer
$x_2=\pm\sqrt{r^2-x_1^2}$
### Question
What is meant by $C^n$ continuity?
### Answer
A curve is $C^n$ continuous if its $n^{th}$ derivative is continuous.<br>
$C^n$ continuity implies $C^{n-1}$ continuity.
### Question
For two curves $f(t)$ and $g(t)$ connected at $t_0$, what is meant by $C^{0}$ continuity?
### Answer
Curves are connected, i.e. $f(t_0)=g(t_0)$.
### Question
For two curves $f(t)$ and $g(t)$ connected at $t_0$, what is meant by $C^{1}$ continuity?
### Answer
Curves are connected smoothly, i.e. $f^{\prime}(t_0)=g^{\prime}(t_0)$.
### Question
# 16. Bezier Curves
Express $\bold{p}(t)=\bold{x}_0+t\bold{x}_1+t^2\bold{x}_2+t^3\bold{x}_3$ in matrix notation.
### Answer
$\bold{p}(t)=\begin{bmatrix}\bold{x}_3&\bold{x}_2&\bold{x}_1&\bold{x}_0\end{bmatrix}\begin{bmatrix}t^3\\t^2\\t\\1\end{bmatrix}=\bold{C}\bold{Q}(t)$
### Question
What is a Hermite Curve expressed in terms of?
### Answer
The geometry constraints, i.e. its values and gradients at the start and end points.
### Question
What is the geometry matrix of a Hermite Curve?
### Answer
$\bold{G}=\begin{bmatrix}\bold{p}(0)&\bold{p}(1)&\bold{p}^{\prime}(0)&\bold{p}^{\prime}(1)\end{bmatrix}$
### Question
What is the matrix form (in terms of the blending, parametrisation and geometry matrices) of a Hermite Curve?
### Answer
$\bold{p}(t)=\bold{G}\bold{M}\bold{Q}(t)$<br><br>
where $\bold{M}=\begin{bmatrix}
2&-3&0&1\\
-2&3&0&0\\
1&-2&1&0\\
1&-1&0&0
\end{bmatrix}$<br><br>
i.e. $\bold{p}(t)=\begin{bmatrix}\bold{p}(0)&\bold{p}(1)&\bold{p}^{\prime}(0)&\bold{p}^{\prime}(1)\end{bmatrix}\begin{bmatrix}
2&-3&0&1\\
-2&3&0&0\\
1&-2&1&0\\
1&-1&0&0
\end{bmatrix}\begin{bmatrix}t^3\\t^2\\t\\1\end{bmatrix}$
### Question
What is a B-spline?
### Answer
A Hermite curve defined in terms of its basis functions.<br>
The basis functions are those resulting from from $\bold{M}\bold{Q}(t)$, i.e.<br><br>
$\begin{bmatrix}
2&-3&0&1\\
-2&3&0&0\\
1&-2&1&0\\
1&-1&0&0
\end{bmatrix}\begin{bmatrix}t^3\\t^2\\t\\1\end{bmatrix}=\begin{bmatrix}
1-3t^2+2t^3\\
3t^2-2t^3\\
t-2t^2+t^3\\
-t^2+t^3
\end{bmatrix}$<br><br>
The Hermite function can therefore be written as:<br>
$\bold{p}(t)\\=\bold{p}(0)(1-3t^2+2t^3)\\+\bold{p}(1)(3t^2-2t^3)\\+\bold{p}^{\prime}(0)(t-2t^2+t^3)\\+\bold{p}^{\prime}(1)(-t^2+t^3)\\$
### Question
What are Bezier Curves (in terms of Hermite Curves)?
### Answer
Bezier Curves are Hermite Curves where the gradient is encoded such that <br><br>
$\frac{d\bold{p}}{dt}(0)=3(\bold{p}_1-\bold{p}_0)$<br>
$\frac{d\bold{p}}{dt}(1)=3(\bold{p}_3-\bold{p}_2)$
### Question
What is the Convex Hull property of Bezier curves?
### Answer
The curve will never pass outside of the convex hull formed by its four control points.
### Question
What is the blending matrix for Bezier curves?
### Answer
$\bold{M}=\begin{bmatrix}
-1 & 3 & -3 & 1\\
3 & -6 & 3 & 0 \\
-3 & 3 & 0 & 0 \\
1 & 0 & 0 & 0 \\
\end{bmatrix}$
### Question
For two Bezier curves defined by points $\bold{p}_i$ and $\bold{q}_i$, how do we achieve $C^0$ continuity?
### Answer
$\bold{p}(1)=\bold{q}(0)$<br>
$\bold{p}_3=\bold{q}_0$
### Question
For two Bezier curves defined by points $\bold{p}_i$ and $\bold{q}_i$, how do we achieve $C^1$ continuity?
### Answer
$\bold{p}^{\prime}(1)=\bold{q}^{\prime}(0)$<br>
$3(\bold{p}_3-\bold{p}_2)=3(\bold{q}_1-\bold{q}_0)$<br>
$\bold{q}_1=2\bold{p}_3-\bold{p}_2$
### Question
What is a Catmull-Rom curve?
### Answer
An interpolating curve where the gradients are chosen based on the control points, i.e.<br><br>
$$\bold{p}^{\prime}_k=\frac{\bold{p}_{k+1}-\bold{p}_{k-1}}{2}$$
$$\bold{p}^{\prime}_0=\bold{p}_{1}-\bold{p}_0$$
For the last point $K$:
$$\bold{p}^{\prime}_K=\bold{p}_{K}-\bold{p}_{K-1}$$
### Question
# 17. Surfaces & Volumes
What is the formula for the explicit representation of a sphere in 3D?
### Answer
$x_3=\pm\sqrt{r^2-x_1^2-x_2^2}$
### Question
What is the formula for the parametric representation of a sphere in 3D?
### Answer
$f(\theta,\phi)=r\begin{bmatrix}\sin\phi\cos\theta\\\sin\phi\sin\theta\\\cos\theta\end{bmatrix}$
### Question
What is the formula for the implicit representation of a sphere in 3D?
### Answer
$f(\bold{x})=\lvert\lvert \bold{x}\rvert\rvert-r$
### Question
What is the name of the algorithm for sampling an implicit surface using a grid?
### Answer
Marching Squares.
### Question
Suppose we want to approximate an implicit surface with a mesh. How does sampling a surface in a grid work?
### Answer
- Trap the implicit surface in a grid. 
- For each point in the grid, if $f(\bold{x})<0$, the point is inside the surface, otherwise if $f(\bold{x})>0$ it is outside the surface.
### Question
How many different configurations of corner values are there in 2D? (Marching Squares algorithm)
### Answer
$2^4=16$ different configurations.
### Question
How many equivalence classes are there in 2D, and what are they? (Marching Squares Algorithm)
### Answer
Four equivalence classes (up to rotational symmetry, reflection symmetry and complement):
- all out
- one out, three in
- two (same side) out, two (same side) in
- two (opposite sides) out, two (opposite sides) in
### Question
Suppose we carry out the Marching Squares algorithm and we get the corners as ($out, in, out, in$) for ($a,b,c,d$). Does the boundary cross at $a$ and $c$ or $b$ and $d$? What should we do to avoid problems in the resulting mesh?
### Answer
Pick one way to interpret the sample and stick to it.  
### Question
How many configurations are there in 3D? (Marching Cubes Algorithm)
### Answer
$2^8=256$ different configurations (since 8 corners).
### Question
How many equivalence classes are there in 3D? (Marching Cubes Algorithm)
### Answer
15
### Question
What are the steps in the Marching Cubes Algorithm?
### Answer
1. Load 4 layers of the grid into memory.
2. Create a cube with vertices on the middle two layers.
3. Classify the vertices of the cube according to the implicit function.
4. Compute the configuration index.
5. Retreive the connectivity via a lookup table.
6. Compute the position of the boundary vertices using linear interpolation, i.e. $\bold{v}_s=t\bold{v}_a+(1-t)\bold{v}_b$
7. Repeat steps 2-7 for the next cube.
### Question
What is subdivision?
### Answer
A process in which a polyline/mesh is recusively refined in order to achieve a smooth curve/surface.
### Question
What is a subdivision surface and what are the benefits of using subdivision surfaces?
### Answer
A subdivision surface is generated by repeatedly applying a subdivision operator onto the control polygon. These have guaranteed continuity and a flexible level of detail.
### Question
What are the main two groups of schemes for subdivision?
### Answer
**Approximation**: original vertices are moved.
**Interpolation**: introduce new vertices without affecting original vertices.
### Question
Give an example of an approximating subdivision scheme.
### Answer
Corner-cutting.
### Question
Give an example of an interpolating subdivision scheme.
### Answer
The 4-point scheme.