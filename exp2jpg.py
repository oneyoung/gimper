from gimpfu import *


def plugin_main(img, drawable, max_size, filename):
    # resize image
    max_pixel = max_size
    scale = float(max_pixel) / (img.width if img.width > img.height else img.height)
    if scale < 1:
        img.scale(int(img.width * scale), int(img.height * scale))

    # save as jpeg
    if not filename:
        filename = img.filename
    pdb.file_jpeg_save(img,  # input image
                       drawable,  # Drawable to save
                       filename,  # filename
                       filename,  # raw-filename
                       0.98,  # quality
                       1,  # smoothing
                       1,  # optimize
                       1,  # enable progressive jpeg image loading
                       '',  # comment
                       0, 1, 0, 1)


register(
    "python_jpg_saver",
    "Save current image, resize and export to jpeg format.",
    "Resize current image first, then export to jpeg format, save and close current image.",
    "oneyoung",
    "Copyright 2014 oneyoung",
    "2014",
    "<Image>/File/Save to jpeg",  # menu item
    "RGB*, GRAY*",  # image type
    [
        (PF_INT, "max_size", "Max Size of Image", 2500),
        (PF_FILE, "filename", "Save As...", ""),
    ],  # parameters
    [],  # return value
    plugin_main,
)

main()
