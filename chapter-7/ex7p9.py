from numpy import loadtxt, empty, fft, shape, arange, meshgrid, exp, sum
from pylab import imshow, show, figure, plot

img = loadtxt('./blur.txt')

sigma = 25

[M, N] = shape(img)
x = empty(M,float)
y = empty(N,float)

if M%2 == 0:
    x[0:M//2] = arange(0,M/2)
    x[M//2:] = arange(M/2,0,-1)
    # x[0:(N//2)] = arange(1,N/2+1)
    # x[(N//2):] = arange(N/2-1,-1,-1)
else:
    x[0:(M//2+1)] = arange(0,M/2+1)
    x[(M//2+1):] = arange(M/2-1,-1,-1)

if N%2 == 0:
    y[0:N//2] = arange(0, N/2)
    y[N//2:] = arange(N/2,0,-1)
    # y[0:(N//2)] = arange(1,N/2+1)
    # y[(N//2):] = arange(N/2-1,-1,-1)
else:
    y[0:(N//2+1)] = arange(0,N/2+1)
    y[(N//2+1):] = arange(N/2-1,-1,-1)

xs = arange(-M/2, M/2)
ys = arange(-N/2, N/2)

[X, Y] = meshgrid(x,y)

psf = exp(- (X**2 + Y**2)/(2*sigma**2))

xs = arange(-M/2, M/2)
ys = arange(-N/2, N/2)

[Xs, Ys] = meshgrid(xs,ys)

psfs = exp(- (Xs**2 + Ys**2)/(2*sigma**2))

img_fft = fft.rfft2(img)
psf_fft = fft.rfft2(psf)
psf_ffts = fft.rfft2(psfs)
eps = 1e-3
psf_fft[abs(psf_fft)<eps] = 1
psf_ffts[abs(psf_ffts)<eps] = 1

img_foc_fft = img_fft/psf_fft
img_foc_ffts = img_fft/psf_ffts
img_foc_shift = fft.fftshift(fft.irfft2(img_foc_ffts))
img_foc = fft.irfft2(img_foc_fft)

figure(1)
imshow(img)

figure(2)
imshow(psf)

figure(3)
imshow(img_foc)
figure(4)
imshow(img_foc_shift)
show()

#The ability of the deconvolution to recover the original image is limited by
#the finite support of the point spread function. The finite support can be a result
#of the analytical form of the point spread function or due to the finite accuracy
#of the numerical calculations involved as in this case. When the point spread function
#is bandlimited convolving the psf with the image nulls out spectral components
#present in the image that cannot be recovered, and thus limits the ability to recover
#the original image.
