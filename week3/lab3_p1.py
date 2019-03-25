ans = int(input('Enter USB size (GB) : '))
gifSize = ((8/8) * (800 * 600)) / 5
jpegSize = ((24/8) * (800 * 600)) / 25
pngSize = ((24/8) * (800 * 600)) / 8
tiffSize = ((48/8) * (800 * 600)) / 1
ansByte = ans * 1000000000

gifCount = int(ansByte//gifSize)
jpegCount = int(ansByte//jpegSize)
pngCount = int(ansByte//pngSize)
tiffCount = int(ansByte//tiffSize)


print('{:>5} images in {} format can be stored'.format(gifCount, 'GIF'))
print('{:>5} images in {} format can be stored'.format(jpegCount, 'JPEG'))
print('{:>5} images in {} format can be stored'.format(pngCount, 'PNG'))
print('{:>5} images in {} format can be stored'.format(tiffCount, 'TIFF'))
